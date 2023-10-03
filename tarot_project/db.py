import psycopg2
import csv

cred={
    "host":"localhost",
    "user":"postgres",
    "password":"postgres",
    "database":"tarotapp",
    "port":"5432"
}

data_to_insert=[]

with open("1.csv","r") as f:
    data=csv.reader(f)
    for row in data:
        data_to_insert.append(row)
        print(row)

try:
    connection=psycopg2.connect(**cred)
    print("Connected to the database successfully.")
    cursor=connection.cursor()

    # queryInsert="insert into users (firstname,gender,startdate,lastlogintime,salary,bonus,seniormanagement,team) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    queryInsert="insert into tarotapp_tarotcard (number,name,image_url,meaning) values (%s,%s,%s,%s)"

    cursor.executemany(queryInsert,data_to_insert)
    connection.commit()
    # cursor.execute("select * from employees limit 5")
    # read=cursor.fetchall()
    # print(read)
    cursor.close()
    connection.close()
    print("Data added successfully")
except psycopg2.Error as e:
    print(f"Failed to insert data in to the db {e}")


