import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('contacts.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Entries table.
    addTable(cur)
    
    # Add rows to the Entries table.
    add_entries(cur)
    
 

    # Display the entries.
    display_entries(cur)
    # Commit the changes.
    conn.commit()
    # Close the connection.
    conn.close()

# The add_entries_table adds the Entries table to the database.
def addTable(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                         fName TEXT,
                                         lName TEXT,
                                         cellNum TEXT,
                                         Wkphone TEXT,
                                         emailAdd TEXT,
                                         address TEXT,
                                         city TEXT,
                                         state TEXT,
                                         zipCode TEXT,
                                         blank TEXT)''')

# The add_entries function adds 6 rows to the Entries table.
def add_entries(cur):
    entries_list = [('Andy', 'Mai','555-1212','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' '),
                    ('Jacky', 'Wu','555-0101','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' '),
                    ('Sumenko', 'Dmitrii','555-9090','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' '),
                    ('Allison' ,'Tate','555-1234','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' '),
                    ('Lillian', 'Kwakye','555-1234','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' '),
                    ('Landon' ,'Balckburn','555-1234','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' '),
                    ('Anthony' ,'Woods','555-2345','666-666-6666','student@ccc.edu','321 Madeup street','Chicago','Illinois','60601',' ')]
    
    for row in entries_list:
        cur.execute('''INSERT INTO Entries (fName,lName,cellNum,Wkphone,emailAdd,address,city,state,zipCode,blank)
                       VALUES (?,?,?,?,?,?,?,?,?,?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
# The display_entries function displays the contents of
# the Entries table.
def display_entries(cur):
    print('Contents of contacts.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]},{row[1]},{row[2]},{row[3]}{row[4]},{row[5]}{row[6]},{row[7]},{row[8]},{row[9]}')

# Execute the main function. 
if __name__ == '__main__':
         main()