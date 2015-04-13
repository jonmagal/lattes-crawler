# -*- coding: utf8 -*-

'''
Created on 31/12/2014

@author: Jonathas Magalhães
'''

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lattes_crawler.settings'

import django
django.setup()

import gc

from lattes_crawler.crawler                 import lattes
from lattes_crawler.apps.research.models    import Research

from xml.dom import minidom

def get_collab(research):
    """
    Receives an object, parses it's XML and returns 
    a list of it's collaborators's lattes_id. 
    
    @param research: Research class object

    @rtype: List
    @return: A list of Researcher's collaborators's Lattes IDs.

    """ 
    parsedxml           = minidom.parseString(research.lattes_information.encode('utf8'))
    curriculo_lattes    = parsedxml.getElementsByTagName("curriculo_lattes")[0]
    pesquisador         = curriculo_lattes.getElementsByTagName("pesquisador")[0]
    colaboradores       = pesquisador.getElementsByTagName("colaboradores")
    if colaboradores == []:
        return 
    else:
        idcolaboradorlist   = colaboradores[0].getElementsByTagName("id_lattes_colaborador")
    
    col_list = [ x.firstChild.nodeValue for x in idcolaboradorlist ]
    
    gc.enable()
    del parsedxml          
    del curriculo_lattes   # Attempt to resolve Memory Overuse
    del pesquisador
    del colaboradores 
    gc.collect()
    return col_list
    
def save_attributes(lattes_id):
    """
    Receives a string, searches if the object 
    is on the database. If object's XML isn't saved, get_cv_lattes
    downloads the desired XML. Object is saved. Returns the object.
    
    @type lattes_id: string
    @param lattes_id: Researcher's Lattes ID.
    
    @rtype: Research class object.
    @return: A Researcher.
    """
    research, created = Research.objects.get_or_create(lattes_id = lattes_id)
    if created == False:
        if not research.is_saved():
            research.lattes_information = lattes.get_cv_lattes(lattes_id)
            research.save()
    else:
        research.save()
    
    return research

def save_lattes(research):
    """
    Receives an object whose lattes_id is received as argument
    by save_attributes function. If the research's XML is already
    saved, it's collaborators are saved and passed as arguments by
    save_attributes.
    
    @type research: Research class object
    @param research: A Researcher.
    """
    research = save_attributes(research.lattes_id) 
    
    if research.lattes_information is not None:
        collaborators = get_collab(research)
        if collaborators is not None:
            for col in collaborators:
                research_col            = save_attributes(col)
                research.collaborators.add(research_col)
                research.save()
    gc.enable()
    del research
    del collaborators
    gc.collect()
    
def walk_lattes(lattes_id_seed = None):
    """
    Receives a list of lattes_id as seeds. Saves all CV Lattes.
 
    @warning: Causing memory overuse

    @type lattes_id_seed: list 
    @param lattes_id_seed: A list of Lattes IDs to use as seeds
                           for the crawler. 
    """
    if lattes_id_seed != None:
        save_attributes(lattes_id_seed)
    
    while True:
        research = Research.objects.filter(lattes_information = None).first()
        if not research:
            return
        save_lattes(research)
        gc.enable()
        del research
        gc.collect()
    print "FINISHED"
        
def test():
    researches = Research.objects.all()
    for research in researches:
        print research.lattes_information

def test2():
    research = Research.objects.get(id = 1)
    collaborators = get_collab(research)
    print collaborators

def test3():
    print lattes.get_cv_lattes(lattes_id = "7151033935149782")
                    

def main():
    seeds = ["8951598251334162", "5760364940162939", "6935433850568144", "7337100011232657", "3697034512999386", 
             "4671683163069536", "3198452549472216", "6322106621770962", "2127559774805521", "9348556938029052", 
             "5192472683408995", "9747151229532463", "8053391833089941", "0590320684933608", "5787113463718492",
             "7151033935149782"]
    for seed in seeds[::-1]:
        walk_lattes(lattes_id_seed = seed)

if __name__ == '__main__':
    walk_lattes()
    
