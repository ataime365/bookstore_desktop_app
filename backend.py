import sqlite3

class Database:

	def __init__(self, db): #create table
		self.conn = sqlite3.connect(db) #Creates the database if none
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT,author TEXT, year INTEGER, isbn INTEGER)")
		self.conn.commit()

	#Avoid sql injection by using VALUES (?,?) which we have to use the meaning of those fields after it
	#we have to use these in a function, to avoid it inserting the same values twice
	def insert(self, title, author, year, isbn):
		self.cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)", (title, author, year, isbn)) #Null for the primary key, python will understand this, since the Primary key is Auto incremental 
		self.conn.commit()

	#lets create a function the grabls the data from the database for us
	def view(self):
		self.cur.execute("SELECT * FROM book")
		rows = self.cur.fetchall() #To fetch the data from the cursor #returns a list of tuples
		return rows

	# connect() #This function will run anytime we execute the frontend scripts, since we have called it
	# insert('The Bold one', 'John Cena', 1934, 913433132)
	# insert('The Lone ranger one', 'Bush Cena', 1932, 916433132)

	#These empty strings enable us parse less than the number of arguments required, the rest will assume a default empty string if none is given
	def search(self, title='', author='', year='', isbn=''):
		self.cur.execute("SELECT * FROM book WHERE title= ?  OR  author= ? OR year=? OR isbn=? ", (title, author, year, isbn))
		rows = self.cur.fetchall() #To fetch the data from the cursor #returns a list of tuples
		return rows

	# print(search('The Bold one'))

	def delete(self, id):
		self.cur.execute("DELETE FROM book WHERE id = ?", (id, ))
		self.conn.commit()

	def update(self, id, title, author, year, isbn):
		self.cur.execute("UPDATE book SET title = ?, author = ?, year=?, isbn=? WHERE id = ?", (title, author, year, isbn, id)) #must be put in the same order as what is on the left
		self.conn.commit()

	def __del__(self): #This method executes when we try to close the program
		self.conn.close()

	# delete(search('The Sea')[0][0]) #This is the complete delete function, function of function
	# delete(4)
	# print(search('The Lone ranger one')[0][0])
	# update(search('The Lone ranger one')[0][0], 'Now here', 'John Lenon', 1945, 9884848484) 
	# print(view()) 

# Database('books.db').conn.close() #funtion __del__ does the same thing as this line




