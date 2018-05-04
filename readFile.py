import mysql.connector
from mysql.connector import errorcode

print(mysql)

try:
    cnn = mysql.connector.connect(user='seniorProject', password='seniorProject', host='127.0.0.1',database='alikemal')
    print("It works!")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Sth is wrong with username or pw")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("DB does not exist")
    else:
        print(e)


cursor = cnn.cursor()

sql = ("SELECT * FROM Resumes")

cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    email = row[0]
    text = row[1]

      # Now print fetched result
    print "%s" % \
        (text)

cnn.commit()
cursor.close()
cnn.close()