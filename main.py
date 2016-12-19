# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016

@author: skipi

get CVE database from Cisco API Oauth2 

"""

# import requests
import json
from pprint import pprint
import get_token
import get_csas
import yaml
from urllib.parse import urlencode
import urllib.request
from skputils import read_csadb

print ('+++ ENTERING main() ...')
print ('### Parsing configs ...')
with open("config.yaml", 'r') as yamlfile:
    cfg = yaml.load(yamlfile)

for section in cfg:
    # Cisco credentials
    clientId = cfg['CiscoCreds']['clientId']
    clientSecret = cfg['CiscoCreds']['clientSecret']
    # backend type for CSA database [DB|CSV]
    bendType = cfg['CsaConf']['backendType']
print ('BENDTYPE is: ', bendType)
print ('### done ...')

# clientID = 'zetgk3mrfy58nwvbe239tqtr'
# clientSecret = 'JkSydPCAnS28M82dKXG94RfY'

ciscoToken = get_token.get_token(clientId, clientSecret)
print ('### Cisco API token fetched ... ')
print ('### Getting according CSAs ...')

# 'YEAR':'ALL':'CVE':'ADVIS':'SEV':'LATEST'
get_csas.get_csas(ciscoToken, 'LATEST', '10', bendType)

print ('### Done getting CSAs ...')
# read_csadb()
print ('--- LEAVING main() ...')
#import get_cves

clientID = 'zetgk3mrfy58nwvbe239tqtr'
clientSecret = 'JkSydPCAnS28M82dKXG94RfY'

ciscoToken = get_token.get_token(clientID, clientSecret)

#get_cves.get_cves(ciscoToken)
