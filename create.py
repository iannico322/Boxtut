
from tkinter import *
import mysql.connector
import json
black = "#0F172A"
white = "#FFFFFF"
gray = "#64748B"

root = Tk()
root.title('Create Form')
# root.iconbitmap('./images/icon2.ico')
width = 534
height = 433
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, True)
root.configure(bg=white)


with open('data.json', 'r') as f:
    data = json.load(f)



print('ID:', data['id'])


ID = IntVar() 
NAME = StringVar()

ID.set(data['id'])
NAME.set(data['name'])



cnx = mysql.connector.connect(user='root', password='',
                              host='localhost')
cursor = cnx.cursor()

cursor.execute("create DATABASE IF NOT EXISTS boxtot_db;")
cursor.execute("USE boxtot_db")
cursor.execute("CREATE TABLE IF NOT EXISTS Users  ( id INT, name VARCHAR(255));")

def Update():
    cursor.execute(f"UPDATE Users SET name = '{NAME.get()}' WHERE id = {ID.get()};")
    print("Updated data")
    print(ID.get())
    print(NAME.get())

    cnx.commit()
    ID.set(0)
    NAME.set("")

def Create():
    cursor.execute(f"INSERT INTO Users (id, name) VALUES ({ID.get()}, '{NAME.get()}');")
    print("added data")
    cnx.commit()
    print(ID.get())
    print(NAME.get())
    ID.set(0)
    NAME.set("")

bg = PhotoImage(file='Frame 2.png')
btn =   PhotoImage(file='btn.png')
bgf=Label(root,image=bg,bg=white)

id = Entry(root,textvariable=ID,font=("Arial ", 20),fg=black,bg=white,width=27,bd=0)
name = Entry(root,textvariable=NAME,font=("Arial ", 20),fg=black,bg=white,width=27,bd=0)

name.place(x=56,y=288)




btnf = Button(root,image=btn,bd=0,bg=white,command=Create)
btnf.place(x=420,y=0)
id.place(x=56,y=165)

bgf.place(x=0,y=0)
root.mainloop()