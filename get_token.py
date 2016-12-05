# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016

@author: skipi

get auth token from Cisco API Oauth2 

"""

# import requests
import json
from urllib.parse import urlencode
import urllib.request

# from pprint import pprint

clientID = 'zetgk3mrfy58nwvbe239tqtr'
clientSecret = 'JkSydPCAnS28M82dKXG94RfY'


def get_token(client_id, client_secret):
    tokenURL = 'https://cloudsso.cisco.com/as/token.oauth2'
    tokenHeaders = {'Content-Type': 'application/x-www-form-urlencoded'}
    tokenData = {'client_id': clientID, 'client_secret': clientSecret, 'grant_type': 'client_credentials'}

    data = urlencode(tokenData).encode("utf-8")
    print ('+++ ENTERING get_token() ...')
    req = urllib.request.Request(tokenURL, data, tokenHeaders)

    try:
        tokenResponseRaw = urllib.request.urlopen(req).read()
    #        print ('### Token response: ', tokenResponseRaw)
    except HTTPError as e:
        print ('$$$ The server cannot fulfill the request.')
        print ('$$$ Error code is: ', e.code)
    except URLError as e:
        print ('$$$ Filed to reach the server.')
        print ('$$$ Error code is: ', e.reason)
    else:
        tokenResponse = tokenResponseRaw.decode('utf8')

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)

        tokenData = json.loads(tokenResponse)

    print ('--- LEAVING get_token() ...')
    return (tokenData["access_token"])
