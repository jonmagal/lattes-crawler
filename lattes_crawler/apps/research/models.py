# -*- coding: utf8 -*-

'''
'''
from django.db                  import models
from picklefield.fields         import PickledObjectField

class Research(models.Model):
    ''' 
    This class represents a Researcher.
    '''
    lattes_information  = PickledObjectField(null = True)
    lattes_id           = models.CharField(max_length = 30)
    update              = models.DateTimeField(blank = True, auto_now = True)
    
    collaborators       = models.ManyToManyField('self')
    
    def is_saved(self):
        #print self.lattes_information, 'verify'
        return self.lattes_information is not None
    
#######################################################################################################################

