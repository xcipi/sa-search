from urllib.parse import urlencode
import urllib.request
import datetime
from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB

client = MongoClient('localhost:27017')
db = client.CSAs
date = str(datetime.date.today())


# Get data from URL using URL, headers and data in request
def get_url_content(url, data='None', headers=None):
    if headers is None:
        headers = {}
    print ('+++ ENTERING get_url_content() ...')
    if data != 'None':
        #        print('- DATA inserted!!!')
        if headers != {}:
            #            print('-- HEADERS inserted!!!')
            reqData = urlencode(data).encode("utf-8")
            req = urllib.request.Request(url, reqData, headers)
    elif headers != {}:
        #        print('- DATA NOT iserted!!!\n-- HEADERS inserted !!!')
        req = urllib.request.Request(url, headers)
    else:
        #        print('- NO DATA nor HEADERS inserted !!!')
        req = urllib.request.Request(url)

    try:
        responseRaw = urllib.request.urlopen(req).read()
    # print ('### URL response: ', responseRaw)
    except HTTPError as e:
        print ('$$$ The server cannot fulfill the request.')
        print ('$$$ Error code is: ', e.code)
    except URLError as e:
        print ('$$$ Filed to reach the server.')
        print ('$$$ Error code is: ', e.reason)
    else:
        response = responseRaw.decode('utf8')
        print ('--- LEAVING get_url_content() ...')
        return (response)


### DATABASE FCNTS
# Function to insert data record into mongo db

def insert_csa(csaRecord, csaCveList):
    print ('+++ ENTERING insert_csa() ...')
    try:
        db.csas.insert_one(
            {
                # sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list
                "csaSir": csaRecord['sir'],
                "csaCvrfUrl": csaRecord['cvrfUrl'],
                "csaLastUpdated": csaRecord['lastUpdated'],
                "csaFirstPublished": csaRecord['firstPublished'],
                "csaAdvisoryId": csaRecord['advisoryId'],
                "csaCveList": csaCveList,
            })
        print ('- Data inserted successfully ...')
        read_lastcsa(csaRecord)
    except Exception as e:
        print ('INSERT ERROR')
        print (e)
    print ('--- LEAVING insert_csa() ...')


# function to read ALL records from mongo db
def read_csadb():
    print ('+++ ENTERING read_csadb() ...')
    try:
        #        print (db.find_one())
        csaCol = db.csas.find()
        print ('\nAll data from CSA Database \n', db)
        for csa in csaCol:
            print (csa)
    except Exception as e:
        print ('READ ERROR')
        print (e)
    print ('--- LEAVING read_csadb() ...')


# function to read LAST INSERTED record from mongo db
def read_lastcsa(csaRecord):
    print ('+++ ENTERING read_lastcsa() ...')
    csa = db.csas
    search = csaRecord['advisoryId']
    try:
        print ('# Reading ID ' + search + '\n')
        test = db.csas.find_one({'csaAdvisoryId': search})
        print(test)
    except Exception as e:
        print ('READ ERROR')
        print (e)
    print ('--- LEAVING read_lastcsa() ...')


# Function to delete record from mongo db
def deleteAnyInDb():
    print ('+++ ENTERING deleteAnyInDb() ...')
    try:
        csaCol = db.CSAs.find()

        for csa in csaCol:
            print ('Deleting ' + csa['advisoryId'])
            csa.deleteOne({'advisoryId': csa['advisoryId']})
        # criteria = input('\nEnter employee id to delete\n')
        #        db.csas.delete_many({"advisoryId":criteria})
        print ('- Deletion of ' + csa['advisoryId'] + ' successful ...')

    except Exception as e:
        print ('DELETE ERROR')
        print (e)
    print ('--- LEAVING deleteAnyInDb() ...')


# Function to drop database
def drop_db(db):
    print ('+++ ENTERING drop_db() ...')
    try:
        db.drop()
        print ('- Databae DROPed ...')
    except Exception as e:
        print ('DROP DB ERROR')
        print (e)
    print ('--- LEAVING drop_db() ...')


############################################################################
# CVFR parsing based on cvrfparse from Mike Schiffman (mschiffm@cisco.com) #
############################################################################
def fix_prefix(EL):
    return (EL[EL.rindex('}') + 1:])


def chop_ns_prefix(element):
    """
    Return the element of a fully qualified namespace URI

    element: a fully qualified ET element tag
    """
    print ('+++ ENTERING chop_ns_prefix() ...')
    return element[element.rindex("}") + 1:]
    print ('--- LEAVING chop_ns_prefix() ...')
