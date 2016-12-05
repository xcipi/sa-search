from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.CSAtest

#def main():
#    while(1):
#	# chossing option to do CRUD operations
#        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
#    
#        if selection == '1':
#            insert()
#        elif selection == '2':
#            update()
#        elif selection == '3':
#            read()
#        elif selection == '4':
#            print ('delete')
#            delete()
#        else:
#            print ('\n INVALID SELECTION \n')


# Function to insert data into mongo db
def csa_insert_db(CSAtoInsert):
    try:
        print (CSAtoInsert)        
#        db.Employees.insert_one(
#	    {
#	        "slaId": slaId,
#	        "slaCustomer": slaCustomer,
#	        "slaType": slaType,
#		"id": employeeId,
##B	        "name":employeeName,
#		"age":employeeAge,
#		"country":employeeCountry
#	    })
        print ('\nInserted data successfully\n')
	
    except:
        print ('ERROR')
	
# Function to update record to mongo db
def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        db.Employees.update_one(
	    {"id": criteria},
	    {
		"$set": {
		    "name":name,
		    "age":age,
		    "country":country
		}
	    }
	)
        print ("\nRecords updated successfully\n")	
	
    except:
        print ('ERROR')

# function to read records from mongo db
def read():
    try:
        empCol = db.Employees.find()
        print ('\n All data from SLA Database \n', db)
        for sla in slaCol:
            print (sla)

    except:
        print ('ERROR')

# Function to delete record from mongo db
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id":criteria})
        print ('\nDeletion successful\n')
    except:
        print ('ERROR')

#main()
