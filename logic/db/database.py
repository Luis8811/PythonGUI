import psycopg2
import json
from psycopg2.extras import Json
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Function to print a list
def printList(message, list):
    print(message)
    for item in list:
        print(item)
        if type(item) is bytes:
            print('Tipo bytes')
        elif type(item) is memoryview:
            print('Tipo memoryview')
        elif type(item) is bytearray:
            print('Tipo bytearray')
        else:
            print('Unknow data type')


class PostgreSQLDBUtils:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
    
    # Inserts a  basic data and a JSON in the table countries
    def insertBasicDataAndJSON(self, basicData1, basicData2, JSONDoc, pathOfImage):
        image = open(pathOfImage, 'rb').read()
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
        cur.execute('INSERT INTO nations(name, capital, info, flag) VALUES (%s, %s, %s, %s);', [basicData1, basicData2, Json(JSONDoc), psycopg2.Binary(image)])
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
print('Displaying image to insert')
image = 'C:\\Users\\Luis\\Desktop\\20206221850.jpg'
im = cv2.imread(image)
im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
plt.show()
accessToBD = PostgreSQLDBUtils("localhost", "countries", "postgres", "postgres")
accessToBD.insertBasicDataAndJSON('USA', 'Washington', {"language" : "English", "currency" : "USD"}, image)
listOfCountries = accessToBD.getCountries()
print('List of countries:', listOfCountries)
print('item 7')
print(listOfCountries[7])
data = listOfCountries[7]
columnOfImg = data[3]
img_array = np.reshape(np.frombuffer(columnOfImg, dtype="Int16"), (10697,10697, 3))
cv2.namedWindow("Image", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.imshow("Image", img_array)
cv2.waitKey(0)
cv2.destroyAllWindows()
""" norm = cm.colors.Normalize(vmax=abs(img_array).max(), vmin=-abs(img_array).max())
plt.matshow(img_array, norm=norm, cmap="gray")
plt.show() """
# print(type(listOfCountries[0]))

