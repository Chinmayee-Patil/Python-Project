import mysql.connector
 
#it will create a connection between python program and mysql database.
db=mysql.connector.connect(host="localhost",user="root",password="", database="library")

cursor=db.cursor()#to get a cursor from the connection

#cursor.execute("create database library")
'''cursor.execute("SHOW DATABASES")
for i in cursor:
     print(i)'''

'''#To create tables-
cursor.execute("create table if not exists books(bid int, bname text, bauthor text, totalbooks int);")
cursor.execute("create table if not exists issue(issue_id int, issue_date date, expiry_date date, book_name text, book_id int);")
cursor.execute("create table if not exists submit(name text, bid int, submitdate date);")
'''
def insertbook():
     book_id=input("Enter book id")
     book_name=input("Enter book name")
     book_author=input("Enter the book author's name")
     Total_book=input("Total no of books")
     data=(book_id,book_name,book_author,Total_book)
     sql='insert into books values(%s,%s,%s,%s)'
     c=db.cursor()
     c.execute(sql,data)
     db.commit()
     print("**************************************")
     print("inserted data into books successfully....")
     main()

def issuebook():
     n=input("Enter the name")
     id=input("Enter the book id")
     r=input("Enter registration no")
     dt=input("Enter the issue date")
     a='insert into issue values(%s,%s,%s,%s)'
     data=(n,id,r,dt)
     c=db.cursor()
     c.execute(a,data)
     db.commit()
     print("**************************************")
     print("Book is issued to :",n)
     bookupdate(id,-1)
     
def submitbook():
     n=input("Enter the name")
     id=input("Enter the book id")
     r=input("Enter registration no")
     dt=input("Enter the submit date")
     a='insert into submit values(%s,%s,%s,%s)'
     data=(n,id,r,dt)
     c=db.cursor()
     c.execute(a,data)
     db.commit()
     print("**************************************")
     print("Book submitted by:",n)
     bookupdate(id,1)

def bookupdate(id,u):
     a="select totalbooks from books where bid =%s"
     data=(id,)
     c=db.cursor()
     c.execute(a,data)  #(10,)
     result=c.fetchone()
     t=result[0]+u
     sql="update books set totalbooks =%s where bid=%s"
     d=(t,id)
     c.execute(sql,d)
     db.commit()
     main()

def deletebook():
     x=input("Enter the book id")
     a = "delete from books where bid = %s"
     data = (x,)
     c=db.cursor()
     c.execute(a,data)
     db.commit()
     main()

def displaybook():
     sql="select * from books"
     c = db.cursor()
     c.execute(sql)
     result = c.fetchall()   #[(1,2,3,4),(1,2,3,4)]
     for i in result:
          print("Book ID:", i[0])
          print("Book Name:", i[1])
          print("Book Author:", i[2])
          print("Total no of books:", i[3])
          print("**************************************")

def main():
     print("""1.Add Book
     2.issue book 
     3.submit book 
     4.delete book 
     5.display books""")
     choice=input("Enter your choice option from above")
     print("**************************************")
     if(choice=='1'):
          insertbook()
     elif(choice=='2'):
          issuebook()
     elif(choice=='3'):
          submitbook()
     elif(choice=='4'):
          deletebook()
     elif(choice=='5'):
          displaybook()
     else:
          print("You have entered invalid choice option!!")
          main()   

def password():
     pw = input("Enter your password")
     if pw=="chinmayee":
          print("You are logged in successfully!!!!")
          main()
     else:
          print("Please enter valid password!")
          password()
password()
