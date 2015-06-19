# -*- coding: utf8 -*- 

'''
@author: Marcus V. G. Pestana
'''
from django.test import TestCase
from models import Research
from lattes_crawler.experiments.crawler import get_collab
from lattes_crawler.crawler.lattes import get_cv_lattes


class CrawlerTest(TestCase):
    def create_research(self, lattes_id = "7151033935149782",
                        lattes_information = get_cv_lattes("7151033935149782")):
        """
        Creates a Research object for test.
        """
        return Research.objects.create(lattes_id = lattes_id,
                                       lattes_information = lattes_information)
    def test_get_collab(self):
        """
        Tests if get_collab is returning a valid collaborators list. 
        """
        research = self.create_research()
        
        collabs = ["8520797274035207", "7179691582151907", "4473869298847632", 
                   "1161431252605700", "9400781845930828", "0995435972741771",
                   "9808563385937929", "8255133166870232", "5760364940162939",
                   "6422000452330465", "1992640052129381", "2926865445767566",
                   "1824772427399881", "2729979018100977", "9474452617185092",
                   "0181615416246917", "0289751922059625", "9513711322466680",
                   "8980213630090119", "7832536123089184", "4688807528550419",
                   "4155051332618408", "7627571580413875", "8460962053427361"]
        
        self.assertEqual(get_collab(research), collabs)
