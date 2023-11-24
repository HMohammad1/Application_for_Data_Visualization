from tkinter import *
from task import Task
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Gui:

    global master

    # Load new file
    def load(self):
        file = self.input_doc_id.get() # get user input
        self.doc_id = file # update current file
        print("New file:", self.doc_id) # debug
        new_file_label = Label(master=self.master, text=self.doc_id, bg='bisque')
        new_file_label.pack()
        new_file_label.place(x = 600, y = 20)

    # Generate graph 
    def graph(self):
        t = Task(self.doc_id) # new task object
        x = t.unique() # get x labels
        y = t.values() # get y values  

        figure = Figure(figsize=(5,5), dpi=100) # creates new figure
        figure_canvas = FigureCanvasTkAgg(figure, graph_frame) # new canvas to insert in figure
        NavigationToolbar2Tk(figure_canvas, graph_frame) # add graph toolbar

        axes = figure.add_subplot()

        axes.bar(x, y)
        axes.set_title('Viewers by Country')
        axes.set_xlabel('Countries')
        axes.set_ylabel('Viewers')

        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1) # displays graph
        
    def __init__(self):
        global graph_frame

        self.master = Tk()
        self.master.title("Document Tracker")
        canvas = Canvas(self.master, width=1500, height=900, bg='bisque')
        canvas.pack()

        self.input_doc_id = StringVar()

        # Current loaded file
        self.current_file = "Current file: "
        current_file_label = Label(self.master, text='Current file: ', bg='bisque')
        current_file_label.pack()
        current_file_label.place(x = 380, y = 20, width = 250)

        # Input field
        input_label = Label(self.master, text='Document ID: ', bg='bisque')
        input_box = Entry(textvariable=self.input_doc_id)
        input_label.pack()
        input_box.pack()  
        input_label.place(x = 50, y = 55)
        input_box.place(x = 50, y = 85, width = 250)
        set_file_button = Button(master=self.master, text='Load', command=self.load)
        set_file_button.pack()
        set_file_button.place(x = 136, y = 120)

        # Buttons
        button_views_by_country = Button(master=self.master, command=self.graph, text ="Views by country", bg='white')
        button_views_by_country.place(x=50, y=180, width=250, height=50)

        button_views_by_continent = Button(master=self.master, text ="Views by continent", bg='white')
        button_views_by_continent.place(x=50, y=260, width=250, height=50)

        button_views_by_browser = Button(master=self.master, text ="Views by browser", bg='white')
        button_views_by_browser.place(x=50, y=340, width=250, height=50)

        button_reader_profiles = Button(master=self.master, text ="Reader profiles", bg='white')
        button_reader_profiles.place(x=50, y=420, width=250, height=50)

        # Vertical line
        canvas.create_line(350, 1500, 350, 0, fill="black", width=2)

        # Graph frame
        graph_frame = Frame(self.master, bg='white')
        graph_frame.place(x=450, y=150, width=950, height=700)

        self.master.mainloop() 

    
