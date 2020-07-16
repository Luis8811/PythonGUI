import psycopg2

# Connect to an existing database
conn = psycopg2.connect("host=localhost dbname=countries user=postgres password=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()
cur.execute("SELECT* FROM nations")
for record in cur:
    print("Country: {}, Capital: {}".format(record[0], record[1]))
