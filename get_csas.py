# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016

@author: skipi

get CSA database from Cisco API

"""

# import requests
import json
import datetime
import urllib.request
from urllib.parse import urlencode

import write_csa
import CSA_CRUD as db
from skputils import insert_csa


def get_csas(ciscoToken, csaParam, csaParamValue, bendType):
    """
    get_csas
    
    ciscoToken - auth token from Cisco API Oauth
    csaParam - search by what
    csaParamValue - search parameter value
    
    """

    print ('+++ ENTERING get_csas() ...')
    date = str(datetime.date.today())

    ciscoTokenHeader = "Bearer " + ciscoToken

    csaBaseUrl = 'https://api.cisco.com/security'

    csaUrlY = '/advisories/cvrf/year/'  # <YYYY - year>
    csaUrlAll = '/advisories/cvrf/all'
    csaUrlCve = '/advisories/cvrf/cve/'  # <CVEID>
    csaUrlAdv = '/advisories/cvrf/advisory/'  # <advisoryId>
    csaUrlSev = '/advisories/cvrf/severity/'  # <critical|high|medium|low>
    csaUrlLatest = '/advisories/cvrf/latest/'  # <number of latest csas>

    if csaParam == 'YEAR':
        csaUrl = csaBaseUrl + csaUrlY + csaParamValue
    elif csaParam == 'ALL':
        csaUrl = csaBaseUrl + csaUrlAll + csaParamValue
    elif csaParam == 'CVE':
        csaUrl = csaBaseUrl + csaUrlCve + csaParamValue
    elif csaParam == 'ADVIS':
        csaUrl = csaBaseUrl + csaUrlAdv + csaParamValue
    elif csaParam == 'SEV':
        csaUrl = csaBaseUrl + csaUrlSev + csaParamValue
    elif csaParam == 'LATEST':
        csaUrl = csaBaseUrl + csaUrlLatest + csaParamValue

    print ('### Getting CSA JSON from ' + csaUrl)

    csaHeaders = {'Accept': 'application/json', 'Authorization': ciscoTokenHeader}
    data = urlencode('').encode('utf8')
    print ('### Headers: ', csaHeaders)
    print ('### Data: ', data)
    req = urllib.request.Request(csaUrl, headers=csaHeaders)
    try:
        csaResponseRaw = urllib.request.urlopen(req).read()
    # print ('### CSA response RAW: ', csaResponseRaw)
    except HTTPError as e:
        print ('$$$ The server cannot fulfill the request.')
        print ('$$$ Error code is: ', e.code)
    except URLError as e:
        print ('$$$ Failed to reach the server.')
        print ('$$$ Error code is: ', e.reason)
    except Exception as e:
        print('$$$ ERROR!!!', e)
    else:
        csaResponse = csaResponseRaw.decode('utf8')
        print ('### Writing to ', bendType)
        if bendType == 'DB':
            write_csa.write_csa_to_db(csaResponse)
        elif bendType == 'CSV':
            write_csa.write_csa_to_csv(csaResponse)

            #	FUNKCNY download CSA files - NEMAZAT !!!

            #            csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wb')
            #            csaFile.write(requests.get(line["cvrfUrl"]).content)
            #            csaFile.close()

            # get_csas('cisco-sa-20161026-linux')
    print ('--- LEAVING get_csas() ...')
