import psycopg2
import json
from psycopg2.extras import Json
# from psycopg2 import Json
# psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)
# import psycopg2.extras.Json
# psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)
# psycopg2.extras.register_default_jsonb(loads=ujson.loads, globally=True)

# Connect to an existing database
""" conn = psycopg2.connect("host=localhost dbname=countries user=postgres password=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()
cur.execute("SELECT* FROM nations")
for record in cur:
    print("Country: {}, Capital: {}".format(record[0], record[1]))
conn.close() """

# Function to print a list
def printList(message, list):
    print(message)
    for item in list:
        print(item)

""" class MyJson(Json):
    def dumps(self, obj):
        return simplejson.dumps(obj) """

class PostgreSQLDBUtils:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        # psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)
    
    # Inserts a JSON in the table usersjson
    def insertJSON(self, JSONDoc):
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
        # sqlCommand = 'INSERT INTO public.usersjson ("user") VALUES (%s);'
        # strJson ="{'loco':MataDeCoco}"
        data = {'a': 340}
        newCountry = 'Japan'
        newCapital = 'Tokio'
        sql = "INSERT INTO nations (name, capital) VALUES (%s, %s);"
        dataInsert = ("Pingon", "Parado")
        # cur.execute('INSERT INTO nations(name, capital) VALUES (%s, %s);', ['Ping', 'cojone'])
        cur.execute(sql, dataInsert)
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
        conn.close()
        return results



# Testing
accessToBD = PostgreSQLDBUtils("localhost", "countries", "postgres", "postgres")
listOfCountries = accessToBD.getCountries()
print('List of countries:', listOfCountries)
userJSON = '{"name":"Luis Manuel","gender":"Male","age":31}'
accessToBD = PostgreSQLDBUtils("localhost", "countries", "postgres", "postgres")
accessToBD.insertJSON(userJSON)
# y = json.loads(userJSON)
# text = str(y)
# print(text)
# accessToBD.insertJSON('{"s":30}')
# accessToBD.insertJSON(userJSON)

