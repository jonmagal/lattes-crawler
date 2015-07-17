# -*- coding: utf8 -*-
'''
@author: Marcus V.G. Pestana
'''

import os
from lattes_crawler.apps import research
from lattes_crawler.experiments.text_analyzer import TextAnalyzer

os.environ['DJANGO_SETTINGS_MODULE'] = 'lattes_crawler.settings'

import django
django.setup()

from lattes_crawler.apps.research.models import ResearchInfo, SmallArea

def main():
    graduation_list = ResearchInfo.objects.filter(data_type = "Graduação").values("description").distinct()
    for graduation in graduation_list:
        graduation = TextAnalyzer()
        graduation = graduation.lower_case()
        graduation = graduation.remove_special_char()
        
        if '%administracao%' in graduation:
            designation = SmallArea()
            designation.area = graduation
            designation.bigarea = "Administração"
if __name__ == '__main__':
    main()
    