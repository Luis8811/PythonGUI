import mysql.connector
from mysql.connector import Error

class MySQLPythonDBController:
    
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
    def insertBLOB(self, datetime, image, processed):
        print("Inserting BLOB into table images")
        try:
            host = 'host=' + self.host
            dbname = 'database=' + self.dbname
            user = 'user=' + self.user
            password = 'password=' + self.password
            print('host:' + self.host)
            print('database:' + self.dbname)
            print('user:' + self.user)
            print('pass:' + self.password)
            connection = mysql.connector.connect(host=self.host,
                                                database=self.dbname,
                                                user=self.user,
                                                password=self.password)
            cursor = connection.cursor()
            sql_insert_blob_query = """ INSERT INTO images
                            (datetime, image, processed) VALUES (%s,%s,%s)"""

            empPicture = self.convertToBinaryData(image)
            file = self.convertToBinaryData(processed)

            # Convert data into tuple format
            insert_blob_tuple = (datetime, empPicture, file)
            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            connection.commit()
            print("Image and processed image were inserted successfully as a BLOB into table images", result)
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))



    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def readBLOB(self, emp_id, photo, bioData):
        print("Reading BLOB data from python_employee table")

        try:
            connection = mysql.connector.connect(host=self.host,
                                                database=self.dbname,
                                                user=self.user,
                                                password=self.password)

            cursor = connection.cursor()
            sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""

            cursor.execute(sql_fetch_blob_query, (emp_id,))
            record = cursor.fetchall()
            for row in record:
                print("Id = ", row[0], )
                print("Name = ", row[1])
                image = row[2]
                file = row[3]
                print("Storing employee image and bio-data on disk \n")
                self.write_file(image, photo)
                self.write_file(file, bioData)

        except mysql.connector.Error as error:
            print("Failed to read BLOB data from MySQL table {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")




# Testing 
# database = MySQLPythonDBController("localhost", "python_db", "root", "")
# database.insertBLOB(3, "Roberto", "C:\\Users\\Luis\\Desktop\\roberto.jpg", "C:\\Users\\Luis\Desktop\\bio_Roberto.txt")
# database.readBLOB(3, "C:\\Users\\Luis\\Desktop\\Photos\\Roberto.jpg", "C:\\Users\\Luis\\Desktop\\Photos\\bio_Roberto.txt")

