'''
Created on May 11, 2015

@author: acabreza
'''
import threading
import responses
import requests


class Connection(threading.Thread):

    def __init__(self, url, progress_callback, results_callback):
        threading.Thread.__init__(self)
        self.url = url
        self.mocked = None
        self.progress_callback = progress_callback
        self.results_callback = results_callback
        
    def set_mocked(self, mocked):
        self.mocked = mocked
        
    def run(self):
        print "connecting " + self.url
        if self.mocked:
            with responses.RequestsMock() as rsps:
                rsps.add(self.mocked.get_type(), self.url, body=self.mocked.get_body(),
                         status=self.mocked.get_status(), content_type=self.mocked.get_content_type())
        resp = requests.get(self.url)

        if resp.status_code == 200 and self.results_callback:
            self.results_callback(resp)
        print "exiting " + self.url
        self.progress_callback()