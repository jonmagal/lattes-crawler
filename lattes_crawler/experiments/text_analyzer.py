#!/usr/bin/env python
# -*- coding: utf8 -*- 
'''
Módulo responsável por fazer o processamento textual de informações textuais 
contidas num documento.

Created on 28/03/2012

@author: Jonathas Magalhães
'''
from nltk.tokenize          import wordpunct_tokenize
from nltk.corpus            import stopwords
from nltk.stem.lancaster    import LancasterStemmer
import string
import re
import unicodedata


class TextAnalyzer():
    
    def normal_unicode(self, udata):
        return unicodedata.normalize('NFKD', unicode(udata)).encode('ascii', 'ignore')

    def lower_case(self, document):
        return document.lower()
    
    def tokenizer(self, document):
        #tokens = nltk.tokenize()
        return wordpunct_tokenize(document)
        
    def remove_stop_words(self, document):
        return [w for w in document if not w in stopwords.words('english')]
    
    def remove_special_char_term(self, document):
        remove = ["-",".","?","+","!","[","]"]
        for x in remove:
            document = document.replace(x,"")
        return document 
            
    def remove_special_char(self, document):
        #remove = ["-",".","?","+","!","\",'"',":",";","(",")","\","0","-","9",/]
        punctuation = re.compile(r'[-.?++!,\\":;()\0-9/]')
        document =  [punctuation.sub("", w) for w in document]
        return [w for w in document if w not in string.punctuation or w not in string.digits]
    
    def remove_short_words(self, document):
        return  [w for w in document if len(w)>1]
    
    def stemming(self, document):
        st = LancasterStemmer()
        return  [st.stem(w) for w in document]
    
    def analyzer_document(self, document):
        document = self.normal_unicode(document)
        document = self.remove_special_char_term(document)
        document = self.lower_case(document)
        document = self.tokenizer(document)
        document = self.remove_special_char(document)
        document = self.remove_short_words(document)
        document = self.remove_stop_words(document)
        document = self.stemming(document)
        document = self.remove_special_char(document)
        #document = self.remove_special_char_term(document)
        return document