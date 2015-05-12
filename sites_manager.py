'''
Created on May 11, 2015

@author: acabreza
'''
import requests
import settings

class SitesManager(object):
    
    def __init__(self, num_sites):
        self.num_sites = int(num_sites)
        
    
    def sites(self):
        for _ in xrange(self.num_sites):
            # get sites from random url generator
            yield requests.get(settings.random_sites).content