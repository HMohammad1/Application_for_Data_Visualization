from tkinter import *

class Gui:
    def __init__(self):
        master = Tk()
        master.title("Document Tracker")
        canvas = Canvas(master, width=1500, height=900, bg='bisque')
        canvas.pack()

        # Input
        label = Label(master, text="Input file", bg='bisque')
        input = Entry()
        label.pack()
        input.pack()  
        label.place(x = 135, y = 55)
        input.place(x = 50, y = 85, width = 250)

        # Buttons
        button_views_by_country = Button(master, text ="Views by country", bg='white')
        button_views_by_country.place(x=50, y=150, width=250, height=50)

        button_views_by_continent = Button(master, text ="Views by continent", bg='white')
        button_views_by_continent.place(x=50, y=230, width=250, height=50)

        button_views_by_browser = Button(master, text ="Views by browser", bg='white')
        button_views_by_browser.place(x=50, y=310, width=250, height=50)

        button_reader_profiles = Button(master, text ="Reader profiles", bg='white')
        button_reader_profiles.place(x=50, y=390, width=250, height=50)

        # Vertical line
        canvas.create_line(350, 1500, 350, 0, fill="black", width=2)

        master.mainloop() 

    
