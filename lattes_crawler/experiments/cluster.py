#!/usr/bin/python
#encoding: utf-8
'''
Created on 30/08/2015

@author: Jonathas Magalhães
'''

import os
import codecs
import sklearn
import numpy as np

from os.path import isfile, join
from nltk.tokenize          import word_tokenize
from sklearn.feature_extraction.hashing import FeatureHasher
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster.k_means_ import KMeans



class ReadData(object):
    '''
    classdocs
    ''' 
    
    def read_utf8_file_as_uni(self, filename):
        try:
            with codecs.open(filename, 'rb', 'UTF-8') as f:
                return f.read()
        except Exception, e:
            pass
            #print filename, e 
    
    def __read_directory(self, directory):
        files       = [ f for f in os.listdir(directory) if isfile(join(directory,f)) and not f.startswith('.') ]
        sentences   = []
        
        for filename in files:
            filename = join(directory,filename)
            sentence = self.read_utf8_file_as_uni(filename) 
            if sentence is not None:
                sentences.append(sentence)
        
        return sentences
    
    def read_dataset(self):
        d1 = "/Users/jon/Dropbox/Projetos/dataset1"
        sentences = self.__read_directory(directory = d1)
        d2 = "/Users/jon/Dropbox/Projetos/dataset2"
        sentences += self.__read_directory(directory = d2)
        
        return sentences
        
    def tokenizer(self, sentence):
        print sentence
        #print wordpunct_tokenize(sentence)
        print word_tokenize(sentence)
        
        
        print "--------------------------------------"
        pass
    
    
    def train_model(self):
        pass
    
    def token_features(self, token):
        if token.isdigit():
            yield "numeric"
        else:
            yield "token={}".token
            
    
    def prepare_data(self, corpus):
        vectorizer = CountVectorizer(min_df=1)
        #corpus = [['a', 'b'], ['a', 'c'], ['b', 'c']]
        #corpus = ['apple banana', 'apple cake', 'banana cake']
        #hasher = FeatureHasher(input_type='string')
        X = vectorizer.fit_transform(corpus)
        #raw_X = (self.token_features(tok) for tok in corpus)
        #X = hasher.transform(raw_X)
        #print X
        voc =  vectorizer.get_feature_names()
        
        #print X.toarray()
        """
        target = ['apple banana falcon cake cake apple']
        vec2 = CountVectorizer(vocabulary = voc)
        Y = vec2.fit_transform(target)
        print Y.toarray()
        """
        return X, voc
    
    def learn_model(self, dataset):
        km = KMeans(n_clusters = 2, max_iter = 2000)
        km.fit(X = dataset)
        #print km.get_params()
        
        return km
    
    def verify_model(self, model, target, voc):
        vec2 = CountVectorizer(vocabulary = voc)
        Y = vec2.fit_transform(target)
        results = model.predict(Y)
        for res in results:
            print res
        
if __name__ == '__main__':
    exp = ReadData()
    #sentences = exp.read_dataset()
    sentences = ['apple banana', 'apple cake', 'banana cake cake']
    target = sentences[0:1]
    for t in target:
        print t
        print exp.tokenizer(t)
        
    vec2 = CountVectorizer()
    Y = vec2.fit_transform(target)
    print vec2.get_feature_names()
    
    for t in vec2.get_feature_names():
        print t
        
    corpus, voc = exp.prepare_data(corpus = sentences)
    km = exp.learn_model(dataset = corpus)
    print len(voc)
    exp.verify_model(km, target, voc)
    print km.cluster_centers_
    
    for cluster in km.cluster_centers_:
        #print "cluster", cluster
        indexes = np.argsort(cluster)[-10:]
        print indexes
        for index in indexes:
            print voc[index]
        #for value in indexes:
        #    print value
        print "----------------------------------"