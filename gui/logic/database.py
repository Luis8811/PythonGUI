import psycopg2
import json
from psycopg2.extras import Json

# Function to print a list
def printList(message, list):
    print(message)
    for item in list:
        print(item)


class PostgreSQLDBUtils:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
    
    # Inserts a  basic data and a JSON in the table countries
    def insertBasicDataAndJSON(self, basicData1, basicData2, JSONDoc):
        print('Method InsertJSON>>>')
        host = "host=" + self.host
        dbname = "dbname=" + self.dbname
        user= "user=" + self.user
        password ="password=" + self.password
        seq = (host, dbname, user, password)
        sep = " "
        connStr = sep.join(seq)
        print('Connection str: ' + connStr)
        conn = psycopg2.connect(connStr)
        cur = conn.cursor()
        cur.execute('INSERT INTO nations(name, capital, info) VALUES (%s, %s, %s);', [basicData1, basicData2, Json(JSONDoc)])
        conn.commit()
        cur.close()
        conn.close()

    # BASIC SELECT from a PostgreSQL Database
    def getCountries(self):
        results = []
        host = "host=" + self.host
        dbname = "dbname=" + self.dbname
        user= "user=" + self.user
        password ="password=" + self.password
        seq = (host, dbname, user, password)
        sep = " "
        connStr = sep.join(seq)
        print('Connection str: ' + connStr)
        conn = psycopg2.connect(connStr)
        cur = conn.cursor()
        sqlCommand = 'SELECT* FROM nations;'
        cur.execute(sqlCommand)
        for record in cur:
            results.append(record)
        cur.close()
        conn.close()
        return results



# Testing
accessToBD = PostgreSQLDBUtils("localhost", "countries", "postgres", "postgres")
accessToBD = PostgreSQLDBUtils("localhost", "countries", "postgres", "postgres")
accessToBD.insertBasicDataAndJSON('Cuba', 'La Habana', {"language" : "Spanish", "currency" : "CUP"})
accessToBD.insertBasicDataAndJSON('Ecuador', 'Quito', {"language" : "Spanish", "currency" : "USD"})
accessToBD.insertBasicDataAndJSON('Japón', 'Tokio', {"language" : "Japanese", "currency" : "JPY"})
listOfCountries = accessToBD.getCountries()
print('List of countries:', listOfCountries)

