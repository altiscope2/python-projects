from contacts2 import *
import tkinter as tk
from tkinter import Listbox, GROOVE, SINGLE, NO, END, mainloop
from tkinter.ttk import Button,Frame, Treeview
import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('contacts.db')

    # Get a database cursor.
    cur = conn.cursor()
    menu(cur,conn)

def menu(cur,conn):
    print("\t\t\t Contact Action Menu", flush=False)
    print("                    ")
    print("\tPlease select an option \n"
              "------------------------------------------\n"+
               "Enter a number 1-6:\n"+
               "Enter 1 To Display Your Contacts Records\n" +
               "Enter 2 To Add a New Contact Record\n"+
               "Enter 3. Remove a contact\n"+
               "Enter 4. Update a contact\n"+
               "Enter 5. To search your contacts\n"+
               "Enter 6. To Quit\n")
    choice = input("Please enter number for action: ")
    if choice == "1":
        displayContacts(cur,conn)
        ent = input("Press Enter to continue ...")
        menu(cur,conn)
    elif choice == "2":
        addEntry(cur,conn)
        ent = input("Press Enter to continue ...")
        menu(cur,conn)
    elif choice == "3":
        removeEntry(cur,conn)
        ent = input("Press Enter to continue ...")
        menu(cur,conn)
    elif choice== "4":
         updateEntry(cur,conn)
         ent = input("Press Enter to continue ...")
         menu(cur,conn)
    elif choice== "5":
        searchEntry(cur,conn)
        ent = input("Press Enter to continue ...")
        menu(cur,conn)
    elif choice == "6":
        print('exit')
        ent = input("Press Enter to continue ...")
        menu(cur,conn)
    else:
        print("Wrong choice please select a number 1-6")
        menu(cur,conn)

    # Commit the changes.
    conn.commit()
    # Close the connection.
    conn.close()

def displayContacts(cur,conn):
    print('Contents of contacts.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]},{row[1]},{row[2]},{row[3]}{row[4]},{row[5]}{row[6]},{row[7]},{row[8]},{row[9]}')
    print('                     ')
    print('_______________________________')

def addEntry(cur,conn):
    print('Please enter contact info')
    s_fName =input('First Name:')
    s_lName= input('Last Name:')
    s_cellNum=input('cellNum:')
    s_Wkphone=input(' Workphone:' )
    s_emailAdd=input('emailAddree: ')
    s_address=input('address:' )
    s_city=input('city: ')
    s_state=input('state:')
    s_zipCode=input('zip Code: ')
    s_blank=input('please leave blank')
    cur.execute('''INSERT INTO Entries (fName,lName,cellNum,Wkphone,emailAdd,address,city,state,zipCode,blank)
    VALUES(?,?,?,?,?,?,?,?,?,?)''', ( s_fName,s_lName,s_cellNum,s_Wkphone,s_emailAdd,s_address,s_city,s_state,s_zipCode,s_blank))

    conn.commit()
    print(cur.rowcount, 'record inserted in to contacts')
    print('                     ')
    print('_______________________________')

def removeEntry(cur,conn):
    removeEntry=input('Please select a user by first name to remove from Contacts:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]},{row[1]},{row[2]},{row[3]}{row[4]},{row[5]}{row[6]},{row[7]},{row[8]},{row[9]}')
    cur.execute('''DELETE from Entries WHERE fName=?''', (removeEntry,))
    conn.commit()
    print(cur.rowcount, 'record removed from Entries table')
    print('                     ')
    print('_______________________________')

def updateEntry(cur,conn):
     select=input('Please select a contact by first name to update address: ')
     newAddress=input('Please enter a new address for selection')
     cur.execute('''UPDATE Entries SET address= ? WHERE  fname= ?''', (newAddress,select))
     print('                     ')
     print('_______________________________')

def searchEntry(cur,conn):
    searchEntry=input('Please enter first name of student to check for Contact: ')
    cur.execute('''SELECT * FROM Entries WHERE fName=?''',(searchEntry,))
    entry=cur.fetchone()
    print(entry)

#print('entry not found')

# Execute the main function. 
if __name__ == '__main__':
         main()