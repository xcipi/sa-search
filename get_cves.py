from ares import CVESearch
import requests
import json

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016
>>>>>>> origin/xcipi-patch-1

@author: skipi

<<<<<<< HEAD
    cveBaseUrl = "http://192.168.56.101:5000/api/cve/"
    cveUrl = cveBaseUrl + cveid
    print ('### Zhanam ' + cveid + ' na URL ' + cveUrl + ' ...')

#    cve = ./../cve-search/bin/search.py -c cveid
    #CVE-2016-4429

    try:
        cveResponse = requests.get(cveUrl)
    except Exception as e:
        print (e)
        
    #, headers = csaHeaders)

#    CVESearch()

    if (cveResponse.ok):
        cveContent = json.loads(cveResponse.content)            
        for line in cveContent["Modified"]:
           print ('- Getting CSA XML description file for ' + line["Modified"])
#        print (cveResponse)
#        print (cveContent)

#    print (cveResponse)
#    .search(cveid))

get_cve('CVE-2016-4429')
=======
get CVE database from Cisco API

"""

import os
import requests
import json
import urllib
import datetime


def get_cves(ciscoToken):
    date = str(datetime.date.today())

    os.makedirs('./CSAs', exist_ok=True)

    ciscoTokenHeader = "Bearer " + ciscoToken
    advUrl = 'https://api.cisco.com/security/advisories/cvrf/year/2016'

    advHeaders = {'Accept': 'application/json', 'Authorization': ciscoTokenHeader}

    advResponse = requests.get(advUrl, headers=advHeaders)

    if (advResponse.ok):
        advCritical = json.loads(advResponse.content)

        csvFile = open("./REPORTS/" + date + ".csv", 'wb')

        #        print "sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list"
        csvFile.write("sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list")

        for line in advCritical["advisories"]:

            cve_list = ""
            for cve in line["cves"]:
                if cve_list == "":
                    cve_list = cve
                else:
                    cve_list = cve_list + ", " + cve

            report = line["sir"] + ";" + line["advisoryId"] + ";" + line["lastUpdated"] + ";" + line[
                "firstPublished"] + ";" + cve_list + ";" + line["cvrfUrl"]

            #            print report
            csvFile.write("\n" + report)

        csvFile.close()


# FUNKCNY download CSA files - NEMAZAT !!!
#            csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wb')
#            csaFile.write(requests.get(line["cvrfUrl"]).content)
#            csaFile.close()

get_cves("ZxpN9LrcHeC4WNtILZbunqYKYKo0")
