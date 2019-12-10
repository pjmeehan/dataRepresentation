import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE datarepresentation")


sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, n
ame VARCHAR(255), age INT)"
mycursor.execute(sql


# insert data
cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)


# view data
cursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
 print(x)
 
 # update data
 cursor = db.cursor()
sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)
cursor.execute(sql, values)
db.commit()
print("update done")

# delete data
cursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)
cursor.execute(sql, values)
db.commit()
print("delete done")


# file that can be used from another file  (ie flask)
import mysql.connector
class StudentDAO:
 db=""
 def __init__(self):
 self.db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 #user="datarep", # this is the user name on my mac
 #passwd="password" # for my mac
 database="datarepresentation"
 )
 def create(self, values):
 cursor = self.db.cursor()
 sql="insert into student (name, age) values (%s,%s)"
 cursor.execute(sql, values)
 self.db.commit()
 return cursor.lastrowid
 def getAll(self):
 cursor = self.db.cursor()
 sql="select * from student"
 cursor.execute(sql)
 result = cursor.fetchall()
 return result
 def findByID(self, id):
 cursor = self.db.cursor()
 sql="select * from student where id = %s"
 values = (id,)
 cursor.execute(sql, values)
 result = cursor.fetchone()
 return result
 def update(self, values):
 cursor = self.db.cursor()
 sql="update student set name= %s, age=%s where id = %s"
 cursor.execute(sql, values)
 self.db.commit()
 def delete(self, id):
 cursor = self.db.cursor()
 sql="delete from student where id = %s"
 values = (id,)
 cursor.execute(sql, values)
 self.db.commit()
 print("delete done")
studentDAO = StudentDAO()

# test code
from zstudentDAO import studentDAO
#create
latestid = studentDAO.create(('mark', 45))
# find by id
result = studentDAO.findByID(latestid);
print (result)
#update
studentDAO.update(('Fred',21,latestid))
result = studentDAO.findByID(latestid);
print (result)
# get all
allStudents = studentDAO.getAll()
for student in allStudents:
 print(student)
# delete
studentDAO.delete(latestid)