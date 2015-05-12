'''
Created on May 11, 2015

@author: acabreza
'''
from collections import defaultdict
import threading
import settings
import progressbar
import sys
import connection
import sites_manager


results = defaultdict(list)
pbar = None
progress = 0
lock = threading.Lock()


def update_results(response):
    # user server type as key
    global results
    if response:
        server = "unknown"
        if "server" in response.headers:
            server = response.headers["server"]
        results[server].append(response)


def update_progress():
    global progress, pbar
    with lock:
        progress = progress + 1
        pbar.update(progress) 


def print_servers():
    global results
    report = ""
    for key in results.keys():
        report = report + "Server Type: %s Count: %s\n" % (key, len(results[key]))
        for server in results[key]:
            report = report + "\turl: %s\n" % server.url
    return report


def exit():
    global pbar
    pbar.finish()
    print print_servers()


def wait_results():
    t = threading.Timer(settings.main_timeout, exit)
    t.start()


def get_sites(num_sites):
    global pbar
    results = {}
    num_sites = int(num_sites)
    pbar = progressbar.ProgressBar(widgets=[progressbar.Bar()], maxval=int(num_sites)).start()
    
    for site in sites_manager.SitesManager(num_sites).sites():
        if site and site.url:
            conn = connection.Connection(site.url, update_progress, update_results)
            conn.start()
    
    wait_results()
    

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