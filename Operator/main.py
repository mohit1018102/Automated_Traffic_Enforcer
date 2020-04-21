import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox

import smtplib

print("email_id",end=":")
EMAIL=input()
print()
print("password :",end="")
PASSWORD=input()

'''------>database connectivity<------------'''
import MySQLdb as mdb
DBNAME="ate"
DBHOST="localhost"
DBPASS=""
DBUSER="root"
mydb=mdb.connect(DBHOST,DBUSER,DBPASS,DBNAME)
cursor=mydb.cursor()
sql="select plateNumber, FirstName,secondName,email from vehicle_details,currentvoilator where plateNumber=p_number;"
cursor.execute(sql)
rows=cursor.fetchall()
total=cursor.rowcount
print("Data Count : "+str(total))
data=rows

'''--------------->Frame<------------------'''
win=Tk()
win.title("Operator Window")
win.geometry("850x300")
win.resizable(False,False)
win.configure(background="#F2D7D5")





frm=Frame(win)
frm.pack(side=tk.TOP,padx=20)
tv=ttk.Treeview(frm,columns=(1,2,3,4), show="headings",height="9")
tv.pack()

tv.heading(1,text="P_Number")
tv.heading(2,text="F_Name")
tv.heading(3,text="S_Name")
tv.heading(4,text="Email_Id")

num=0
for i in rows:
	tv.insert('','end',iid=str(num),values=i)
	num=num+1

def sendTicket():
	sql="select plateNumber, FirstName,secondName,email from vehicle_details,currentvoilator where plateNumber=p_number;"
	cursor.execute(sql)
	data=cursor.fetchall()
	count=cursor.rowcount
	if count>0:
		messagebox.showinfo("information","process initiated....")
	else:
		messagebox.showinfo("information","No voilator found....")

	num=0
	for row in data:

		name=row[1]+" "+row[2]
		plate=row[0]
		email=row[3]
		content=name+",\nYou got a red light voilation \nticket no : "+plate+", \n contact your near Police station\n Regards,\n ATE Team,\nDehradun(U.K)"
		mail=smtplib.SMTP('smtp.gmail.com',25)
		mail.ehlo()
		mail.starttls()
		mail.login(EMAIL,PASSWORD)
		mail.sendmail(EMAIL, email, content)
		mail.close()
		sql="INSERT INTO `processedvoilator`(`p_number`) VALUES ('"+row[0]+"')"
		cursor.execute(sql)
		tv.selection_set(str(num))
		print(tv.selection())
		num=num+1
		tv.delete(tv.selection()[0])

	
	sql="delete FROM `currentvoilator`"
	cursor.execute(sql)






btn1=Button(win,text="Send Ticket",command=sendTicket)
btn1.pack()
win.mainloop()