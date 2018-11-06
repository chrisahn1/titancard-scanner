import sqlite3
# conn = sqlite3.connect('tcscanner.db')
# 
# c = conn.cursor()
# 
# c.execute('''CREATE TABLE person (id real, card_number real, cwid real, name text, email text)''')
# 
# c.execute("INSERT INTO person VALUES('1', '1234567890000', '333222111', 'Neil Breen', 'neilb4breen@gmail.com')")
# 
# conn.commit()
# 
# 
# for row in c.execute('SELECT * FROM person ORDER BY id'):
#     print(row)
# 
# conn.close()






class TitanCardScanner:
    """Local database class that holds data."""

    locale = "tcscanner.db"

    def __init__(self):
        """Initialize instance variables and creates connection to the database."""
        self.conn = sqlite3.connect(TitanCardScanner.locale)
        self.curr = self.conn.cursor()

    def create_tables(self):
        """Create the tables if they don't exist."""
        self.curr.execute('''CREATE TABLE person (id real, card_number real, cwid real, name text, email text)''')

        self.conn.commit()

    def add_person(self, id1, card_number1, cwid1, name1, email1):
        """Add a person to the database."""
        self.curr.execute("INSERT INTO person (id, card_number, cwid, name, email) VALUES (?)",
                          (id1, card_number1, cwid1, name1, email1))
        self.conn.commit()

    'name and id for checking'
