# -*- coding: utf8 -*-
'''
@author: Marcus V.G. Pestana
'''

import os
from lattes_crawler.apps import research

os.environ['DJANGO_SETTINGS_MODULE'] = 'lattes_crawler.settings'

import django
django.setup()

from lattes_crawler.apps.research.models import ResearchInfo

def main():
    graduation_list = ResearchInfo.objects.filter(data_type = "Graduação").values("description").distinct()
    for graduation in graduation_list:
        if '''contains the normalized graduation''':
            '''Area = Big Area'''
if __name__ == '__main__':
    main()