#!/usr/bin/python3

import pymysql

db_creds = {
        'host':'35.236.115.197', 
        'user':'megan', 
        'passwd':'FV5T%c*R|dNOsA4A(',
        'database':'geoInfo',
        'port':3306}

# Open database connection
db = pymysql.connect(
    host=db_creds['host'],
    user=db_creds['user'],
    passwd=db_creds['passwd'],
    db=db_creds['database'],
    port=db_creds['port'],
    ssl={'ssl':{
            'ca':'/home/tensorflow/.keys/server-ca.pem',
            'key':'/home/tensorflow/.keys/client-key.pem',
            'cert':'/home/tensorflow/.keys/client-cert.pem'
            }
        }
)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print (data)

# disconnect from server
db.close()
