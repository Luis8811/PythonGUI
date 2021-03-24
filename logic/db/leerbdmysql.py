import mysql.connector
from mysql.connector import Error


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(emp_id, photo, bioData):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='root',
                                             password='')

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
            write_file(image, photo)
            write_file(file, bioData)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

readBLOB(1, "C:\\Users\\Luis\\Desktop\\Photos\\mojon.jpg",
         "C:\\Users\\Luis\\Desktop\\Photos\\pito.txt")
readBLOB(2, "C:\\Users\\Luis\\Desktop\\Photos\\cojones.jpg",
         "C:\\Users\\Luis\\Desktop\\Photos\\mierd.txt")