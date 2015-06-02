# -*- coding: utf8 -*-

'''
'''
from django.db                  import models
from picklefield.fields         import PickledObjectField

class Research(models.Model):
    ''' 
    This class represents a Researcher.
    '''
    lattes_information            = PickledObjectField(null = True)
    lattes_id                     = models.CharField(max_length = 30)
    update                        = models.DateTimeField(blank = True, auto_now = True)
    information                   = models.ForeignKey('Info')
    
    collaborators                 = models.ManyToManyField('self', null = True)

    def is_saved(self):
        #print self.lattes_information, 'verify'
        return self.lattes_information is not None

class Info(models.Model):
    '''
    This class represents a Rearcher's information.
    '''
    description = models.TextField(blank=True)
    year        = models.PositiveIntegerField(blank=True)
    researcher  = models.ForeignKey('Research')
    data_type   = models.CharField(max_length = 50, blank = True)
    
    
    
    
#######################################################################################################################

