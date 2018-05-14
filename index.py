import mysql.connector
from mysql.connector import errorcode
from main import main
import sys
reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')

def work():
    try:
        cnn = mysql.connector.connect(user='admin', password='admin', host='127.0.0.1',
                                      database='csiresume')
        #print("It works!")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username or password authentication problem")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB does not exist")
        else:
            print(e)

    cursor = cnn.cursor()

    imageList=[]
    main(imageList)

    for i in range(0,len(imageList)):
        email = str(imageList[i].getImageID()).replace("[", "").replace("'", "").replace("]", "")

        text = str(imageList[i].getImageText())
        data = (email,text)
        data2 = (text, email)
        print("E:"+email+ "K"+text.encode('utf-8'))

        try:
            query = "INSERT INTO Resumes VALUES (%s, %s)"
            cursor.execute(query, data)
            cnn.commit()
        except mysql.connector.IntegrityError:
            query2 = "UPDATE Resumes SET TextFile = %s WHERE email= %s"
            cursor.execute(query2, data2)
            cnn.commit()
            print("Giris saglandi")
            continue
            # print("Error")
            # continue
        except:
            print("Not found")
            continue

    cursor.close()
    cnn.close()