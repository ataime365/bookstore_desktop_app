from tkinter import *
from backend import Database #importing the Database class

database = Database('books.db')

window = Tk()
window.wm_title("My BookStore")


def view_command():
	Lb1.delete(0, END) #TO make the Listbox empty at the begining
	for row in database.view(): #This is the list of tuples from the database
		Lb1.insert(END, row) #index here is END, and elements is row #Listbox has an insert function #new row will be put at the end of the Listbox

def clear_entry_boxes():
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	e4.delete(0, END)

def search_entry():
	title_text = e1.get()
	author_text = e2.get()
	year_text = e3.get()
	isbn_text = e4.get()
	rows = database.search(title_text, author_text, year_text, isbn_text)
	Lb1.delete(0, END)
	for row in rows: #This is the list of tuples from the database
		Lb1.insert(END, row) 


def add_entry():
	#Its meant to be title_text.get() #The very first one which is StringVar()
	title_text = e1.get()
	author_text = e2.get()
	year_text = e3.get()
	isbn_text = e4.get()
	#This is where the main inserting happens
	database.insert(title_text, author_text, year_text, isbn_text)
	clear_entry_boxes()
	Lb1.delete(0, END) #TO make the Listbox empty at the begining
	for row in database.view(): #This is the list of tuples from the database
		Lb1.insert(END, row)


'''because of the event special parameter that wouldnt let us use the funtion easily, 
   let us make selected_tuple_original_values a global variable from inside the function,
   since we only need values from selected_tuple_original_values'''
def listbox_click(event): #event is a special parameter
	try:
		global selected_tuple_original_values
		index = Lb1.curselection()[0] #index of selection.....[0] since its inside a tuple e.g (2, )
		selected_tuple_original_values = Lb1.get(index) #selected_tuple_original_values[0] #real index inside tuple

		# To make it appear in the entry columns
		e1.delete(0, END)
		e1.insert(END, selected_tuple_original_values[1])
		e2.delete(0, END)
		e2.insert(END, selected_tuple_original_values[2])
		e3.delete(0, END)
		e3.insert(END, selected_tuple_original_values[3])
		e4.delete(0, END)
		e4.insert(END, selected_tuple_original_values[4])
	except IndexError:
		pass

def delete_command():
	title_text = e1.get()
	author_text = e2.get()
	year_text = e3.get()
	isbn_text = e4.get()
	#select and delete
	database.delete(selected_tuple_original_values[0]) #This is selecting the 'id' which is the primary key
	view_command()
	clear_entry_boxes()
 

def update_command():
	title_text = e1.get()
	author_text = e2.get()
	year_text = e3.get()
	isbn_text = e4.get()
	#select and update
	database.update(selected_tuple_original_values[0], title_text, author_text,
					year_text, isbn_text) #This is selecting the 'id' which is the primary key
	view_command()
	clear_entry_boxes()


#The Four types of widgets
b1 = Button(window, text="View all", width=12,command=view_command) 
b1.grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_entry) 
b2.grid(row=3, column=3)
b3 = Button(window, text="Add entry",  width=12, command=add_entry) 
b3.grid(row=4, column=3)
b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12, command=delete_command) 
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy) 
b6.grid(row=7, column=3)

# Create a Label widget with "Kg" as label
L1=Label(window,text="Title")
L1.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window
L2=Label(window,text="Author")
L2.grid(row=1,column=0) # The Label is placed in position 0, 0 in the window
L3=Label(window,text="Year")
L3.grid(row=0,column=2) # The Label is placed in position 0, 0 in the window
L4=Label(window,text="ISBN")
L4.grid(row=1,column=2) # The Label is placed in position 0, 0 in the window 

#This acts as a string Input, thats why it is called Entry
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=1, column=1)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=0, column=3)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#Listbox
Lb1 = Listbox(window, height=6, width=35)
Lb1.grid(row=2, column=0, rowspan=6, columnspan=2)

#Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#Inform the Lb1 that there is a scrollbar for it 
#configure both sb and Lb
Lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command = Lb1.yview)

#bind is used to bind a widget event to a function
Lb1.bind('<<ListboxSelect>>', listbox_click)

window.mainloop() #very important, so that our window doesn't close immediately after opening 
