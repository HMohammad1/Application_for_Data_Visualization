from tkinter import *
from task import Task
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import re

class Gui:

    global master
    clear_graph = None
    toolbar = None

    # Load new file
    # Load new file
    def load(self):
        file = self.input_doc_id.get()  # get user input
        # update current file and get rid of white spaces
        self.doc_id = re.sub(r"\s+", "", file)
        print("New file:", self.doc_id)  # debug
        new_file_label = Label(master=self.master, text=self.doc_id, bg='bisque')
        new_file_label.pack()
        new_file_label.place(x=600, y=20)

    # Generate graph
    # task_number denotes what task to display on the graph
    def graph(self, task_number, graph_name, x_axis, y_axis):
        # clear the graph and toolbar when displaying new graphs
        if self.clear_graph is not None:
            self.clear_graph.destroy()
            self.toolbar.pack_forget()

        t = Task(self.doc_id) # new task object
        x = None
        y = None
        # display the graph depending on which button is pressed
        if task_number == 1:
            x, y = t.task_2_a()
        if task_number == 2:
            x, y = t.task_2_b()

        figure = Figure(figsize=(5,5), dpi=100) # creates new figure
        figure_canvas = FigureCanvasTkAgg(figure, graph_frame) # new canvas to insert in figure
        self.toolbar = NavigationToolbar2Tk(figure_canvas, graph_frame) # add graph toolbar
        axes = figure.add_subplot()
        axes.bar(x, y)
        axes.set_title(graph_name)
        axes.set_xlabel(x_axis)
        axes.set_ylabel(y_axis)
        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1) # displays graph
        self.clear_graph = figure_canvas.get_tk_widget()

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
        button_views_by_country = Button(master=self.master, command=lambda: self.graph(1, 'Viewers by Country', 'Countries', 'Viewers'), text ="Views by country", bg='white')
        button_views_by_country.place(x=50, y=180, width=250, height=50)

        button_views_by_continent = Button(master=self.master, command=lambda: self.graph(2, 'Viewers by Continent', 'Continents', 'Viewers'), text ="Views by continent", bg='white')
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


