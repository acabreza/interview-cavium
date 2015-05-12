'''
Created on May 11, 2015

@author: acabreza
'''
from collections import defaultdict
import progressbar
import sys
import connection
import sites_manager


results = defaultdict(list)
pbar = None
progress = 0


def results(response):
    # user server type as key
    if response:
        results[response.get_server_type()].append(response)

def progress(pbar):
    progress = progress + 1
    pbar.update(progress) 

def print_servers():
    report = ""
    for key in results.keys():
        report = "Server Type: %s Count: %s\n" % (key, len(results[key]))
        for server in results[key]:
            report = report + "url: %s\n" % server.url
    return report


def get_sites(num_sites):
    results = {}
    pbar = progressbar.ProgressBar().start()
    
    for sites in sites_manager.SitesManager(num_sites).sites():
        conn = connection.Connection(sites, progress, results)
        conn.start()
    
    pbar.finish()
    print_servers()


def usage():
    print "test_main.py [n]"
    print "n - number of random websites to retrieve."   


def main():
    if len(sys.argv) != 2:
        usage()
    else: 
        get_sites(sys.argv[1])


if __name__ == "__main__":
    main()