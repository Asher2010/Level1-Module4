"""
Log Search using a Id-Name Dictionary
"""
import tkinter as tk
from tkinter import simpledialog, messagebox
# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.


class LogSearch(tk.Tk):

    def __init__(self):

        super().__init__()
        self.button = tk.Button(self, text='Add', fg='black',
                                font=('courier new', 16, 'bold'), command=self.add_entry)
        self.button.place(relx=0.0, rely=0.1, relwidth=0.25, relheight=0.1)
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.

#  Button 2: Search by ID
        self.button2 = tk.Button(self, text='Search', fg='black',
                                font=('courier new', 16, 'bold'), command=self.search_entry)
        self.button2.place(relx=0.25, rely=0.1, relwidth=0.25, relheight=0.1)
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
# Button 3: View List
        self.button3 = tk.Button(self, text='View', fg='black',
                                font=('courier new', 16, 'bold'), command=self.view_entry)
        self.button3.place(relx=0.5, rely=0.1, relwidth=0.25, relheight=0.1)
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
        self.button4 = tk.Button(self, text='Remove', fg='black',
                                font=('courier new', 16, 'bold'), command=self.remove_entry)
        self.button4.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.1)
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.

    def add_entry(self):
        simpledialog.askstring(title="ID", prompt="Enter an ID")
    def search_entry(self):
        pass
    def view_entry(self):
        pass
    def remove_entry(self):
        pass
if __name__ == '__main__':

    logsearch = LogSearch()

    logsearch.geometry('1000x1000')

    logsearch.mainloop()


