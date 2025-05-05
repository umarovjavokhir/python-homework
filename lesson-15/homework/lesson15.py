import sqlite3

# Create a new database and a table named 'Roster'
def create_database():
    connection = sqlite3.connect('roster.db')
    cursor = connection.cursor()
    
    # Create table 'Roster'
    cursor.execute('''CREATE TABLE IF NOT EXISTS Roster (
                        Name TEXT,
                        Species TEXT,
                        Age INTEGER)''')
    
    # Insert the initial data into the table
    cursor.executemany('''INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)''', [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ])
    
    connection.commit()
    print("Database and table created, and initial data inserted.")

# Update the Name of Jadzia Dax to Ezri Dax
def update_name():
    connection = sqlite3.connect('roster.db')
    cursor = connection.cursor()
    
    # Update Jadzia Dax's name to Ezri Dax
    cursor.execute('''UPDATE Roster SET Name = ? WHERE Name = ?''', ('Ezri Dax', 'Jadzia Dax'))
    
    connection.commit()
    print("Name updated from Jadzia Dax to Ezri Dax.")

# Display Name and Age of everyone classified as Bajoran
def display_bajoran():
    connection = sqlite3.connect('roster.db')
    cursor = connection.cursor()
    
    # Retrieve and display Bajoran details
    cursor.execute('''SELECT Name, Age FROM Roster WHERE Species = ?''', ('Bajoran',))
    bajoran_data = cursor.fetchall()
    
    print("Bajoran Members:")
    for row in bajoran_data:
        print(f"Name: {row[0]}, Age: {row[1]}")

# Main function to execute the tasks
def main():
    create_database()
    update_name()
    display_bajoran()

if __name__ == "__main__":
    main()

