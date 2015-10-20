# -*- coding: utf8 -*-
'''
@author: Marcus V.G. Pestana
'''

import os
from lattes_crawler.apps import research
from lattes_crawler.experiments.text_analyzer import TextAnalyzer
import unicodedata

os.environ['DJANGO_SETTINGS_MODULE'] = 'lattes_crawler.settings'

import django
django.setup()



from lattes_crawler.apps.research.models import ResearchInfo, SmallArea

def removeAccent(graduation):
    aaccent = ['á', 'ã', 'à', 'â']
    eaccent = ['é', 'ẽ', 'è', 'ê']
    iaccent = ['í', 'ĩ', 'ì', 'î']
    oaccent = ['ó', 'õ', 'ó', 'ô']
    uaccent = ['ú', 'ũ', 'ù', 'û']
    for a in aaccent:
        if a in graduation:
            graduation = graduation.replace(a, 'a')
    for e in eaccent:
        if e in graduation:
            graduation = graduation.replace(e, 'e')
    for i in iaccent:
        if i in graduation:
            graduation = graduation.replace(i, 'i')
    for o in oaccent:
        if o in graduation:
            graduation = graduation.replace(o, 'o')
    for u in uaccent:
        if u in graduation:
            graduation = graduation.replace(u, 'u')
    if 'ç' in graduation:
            graduation = graduation.replace('ç', 'c')
    return graduation

def main():
    graduation_list = ResearchInfo.objects.filter(data_type = "Graduação").values("description").distinct()
    #graduation_list = ["Administração de Interiores", "Administração", "administracao"]
    for graduation in graduation_list:
        analyzer = TextAnalyzer()
        #graduation = unicodedata.normalize('NFKD', unicode(graduation.decode('utf8').encode('ascii', 'ignore')))#['description'])
        graduation = analyzer.lower_case(graduation['description'].encode('utf8'))
        graduation = removeAccent(graduation)
        graduation = analyzer.remove_special_char_term(graduation)
        print graduation
        
        if 'administracao' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Administração"
            designation.save()
            print "check"
            
        if 'matematica' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Matemática"
            designation.save()
            print "check"
            
        if 'sociologia' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Sociologia"
            designation.save()
            print "check"
            
        if 'filosofia' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Filosofia"
            designation.save()
            print "check"
            
        if 'fisica' in graduation:
            if 'educacao' in graduation:
                designation = SmallArea()
                designation.area = graduation
                designation.bigarea = "Educação Física"
                designation.save()
                print "check"
            else:
                designation = SmallArea()
                designation.area = graduation
                designation.bigarea = "Física"
                designation.save()
                print "check"
        
        if 'medicina' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Medicina"
            designation.save()
            print "check"
        
        if 'enfermagem' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Enfermagem"
            designation.save()
            print "check"
        
        if 'computacao' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Computação"
            designation.save()
            print "check"
        
if __name__ == '__main__':
    main()
    