# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 2016

@author: skipi

write CVE database to CSV file

"""

#import requests
import re
import json
import datetime
from pymongo import MongoClient
from urllib.parse import urlencode
import urllib.request
from skputils import get_url_content, insert_csa

# creating connectioons for communicating with Mongo DB

client = MongoClient('localhost:27017')
db = client.CSAs
date = str(datetime.date.today())

csaFilenameRegex = r"^https?\:\/\/tools\.cisco\.com\/security\/center\/contentxml\/[Cc]isco[Ss]ecurity[Aa]dvisory\/cisco\-sa\-\d+\-\w+\/cvrf\/"

def write_csa_to_csv(csaEntry):

    print ('+++ ENTERING write_csa_to_csv() ...')
    date = str(datetime.date.today())
    print ('### Writting CSA to CSV file ...')
    csaContent = json.loads(csaEntry)
    csvFile = open("./REPORTS/" + date + ".csv",'wt')
 
    headerLine = 'sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list\n'
    csvFile.write(headerLine)
    
    for line in csaContent['advisories']:
        print ('### Getting CSA XML description file for ' + line ['advisoryId'])
        csaFilename = './CSAs/' + re.sub(csaFilenameRegex, '', line['cvrfUrl'], 0)
        print ('### Writting to file ', csaFilename)
        csaFile = open(csaFilename,'wt')        

#        csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wt')

        print ('### CVRFURL: ', line['cvrfUrl'])
        pokus = 'b' + get_url_content(line['cvrfUrl'])
        csaFile.write(pokus)
        csaFile.close()

        cve_list = ""
        for cve in line["cves"]:
            print ('*** ToDo: Download description for ', cve)
#            print get_cves.get_cve(cve)
            if cve_list == "":
                cve_list = cve
            else:
                cve_list = cve_list + ", " + cve
        report = line["sir"] + ";" + line["advisoryId"] + ";" + line["lastUpdated"] + ";" + line["firstPublished"] + ";" + cve_list + ";" + line["cvrfUrl"] + '\n'
        csvFile.write(report)
    csvFile.close()

def write_csa_to_db(csaEntry):
    print ('+++ ENTERING write_csa_to_db() ...')    
    print ('### Writting CSA CSV file to DB: ', db)
    csaContent = json.loads(csaEntry)

    for line in csaContent["advisories"]:
        print ('### Getting CSA XML description file for ' + line ['advisoryId'] + '...')
        csaFilename = './CSAs/' + re.sub(csaFilenameRegex, '', line['cvrfUrl'], 0)
        print ('###  Writting to file ', csaFilename)
        csaFile = open(csaFilename,'wt')        
#        csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wt')

        print ('### CVRFURL: ', line['cvrfUrl'])
        pokus = get_url_content(line['cvrfUrl'])
        csaFile.write(pokus)
        csaFile.close()

        cve_list = ""
        for cve in line["cves"]:
            print ('--- ToDo: Download description for ' + cve + ' ...')
#            print get_cves.get.cve(cve)
            if cve_list == "":
                cve_list = cve
            else:
                cve_list = cve_list + ", " + cve
        
        insert_csa(line,cve_list)
#        read_lastcsa(line)    
#        read_csadb()
             
#        deleteAnyInDb()
    print ('--- LEAVING write_csa_to_db() ...')                            
    