from tkinter import *
from tkinter import messagebox

import numpy as np
from task import Task
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re


class Gui:
    # initialise contractor with all the variables needed for this class
    def __init__(self, filename, task, visitor=None, doc=None):
        self.visitor_uuid = None
        self.doc_id = None
        self.filename = filename
        self.graph_frame = None
        self.master = Tk()
        self.master.title("Document Tracker")
        self.input_doc_id = StringVar()
        self.doc_id_box = None
        self.user_id_box = None
        self.clear_graph = None

        # get rid of any white spaces to ensure correct loading
        if doc is not None:
            self.doc_id = re.sub(r"\s+", "", doc)
        else:
            self.doc_id = None
        if visitor is not None:
            self.visitor_uuid = re.sub(r"\s+", "", visitor)
        else:
            self.visitor_uuid = None
        # run the gui depending on the task
        self.run_gui(task)

    # Load new file and visitor uuid for the application
    def load(self):
        # get user input
        file = self.doc_id_box.get()
        visitor = self.user_id_box.get()
        # update current file and get rid of white spaces
        self.doc_id = re.sub(r"\s+", "", file)
        self.visitor_uuid = re.sub(r"\s+", "", visitor)

    # Generate graph and add it inside the tkinter window.
    # task_number denotes what task to display on the graph, graph name is the name of the graph, x and y axis are for
    # displaying the name of each axis respectively.
    def graph(self, task_number, graph_name=None, x_axis=None, y_axis=None):
        # clear the graph and toolbar when displaying new graphs
        if self.clear_graph is not None:
            self.clear_graph.destroy()

        t = Task(self.filename)
        x = None
        y = None
        # display the graph depending on which button is pressed.
        # Checks the returned arguments and prints the necessary warnings if found any.
        if task_number == 1:
            x, y = t.task_2_a(self.doc_id)
            if x is False:
                messagebox.showinfo("Warning", y)
                return
        if task_number == 2:
            x, y = t.task_2_b(self.doc_id)
            if x is False:
                messagebox.showinfo("Warning", y)
                return
        if task_number == 31:
            x, y = t.task_3_a()
            if x is False:
                messagebox.showinfo("Warning", y)
                return
        if task_number == 32:
            x, y = t.task_3_b()
            if x is False:
                messagebox.showinfo("Warning", y)
                return
        if task_number == 4:
            x, y = t.task_4()
            if x is False:
                messagebox.showinfo("Warning", y)
                return
        if task_number == 5:
            x, y, z = t.task_5_d(self.doc_id, self.visitor_uuid)
            if x is False:
                messagebox.showinfo("Warning", y)
                return
            if z is False:
                messagebox.showinfo("Warning", "The visitor uuid entered has not read the document")
        if task_number == 6:
            param1, param2 = t.task_6(self.doc_id, self.visitor_uuid)
            if param1 is False:
                messagebox.showinfo("Warning", param2)
                return
            if param2 is False:
                messagebox.showinfo("Warning", "The visitor uuid entered has not read the document")
                return
            return

        # creates new figure
        figure = Figure(figsize=(10, 10), dpi=70)
        # new canvas to insert in figure
        figure_canvas = FigureCanvasTkAgg(figure, self.graph_frame)
        # setup the axes to plot
        axes = figure.add_subplot()
        axes.bar(x, y)
        axes.set_title(graph_name, fontsize=12)
        axes.set_xlabel(x_axis, fontsize=12)
        axes.set_ylabel(y_axis, fontsize=12)
        axes.tick_params(axis='x', labelsize=10)
        # adjusts labels for graphs depending on the task number to fit in the axes names and data
        if task_number == 4:
            current_ticks = axes.get_xticks()
            adjusted_ticks = np.array(current_ticks) - 0.5
            axes.set_xticks(adjusted_ticks)
            axes.tick_params(axis='x', rotation=20, labelsize=6)
            axes.tick_params(axis='y', rotation=20, labelsize=8)
            axes.get_yaxis().get_major_formatter().set_scientific(False)
            figure.subplots_adjust(bottom=0.1)
        if task_number == 31:
            axes.tick_params(axis='x', rotation=60, labelsize=7)
            figure.subplots_adjust(bottom=0.2)
        if task_number == 5:
            axes.tick_params(axis='x', rotation=60, labelsize=5)
            figure.subplots_adjust(bottom=0.2)
        # plot the actual graph
        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=0.5)
        self.clear_graph = figure_canvas.get_tk_widget()

    # runs the tkinter window that shows all the buttons and the graph inside it.
    def run_gui(self, task):
        t = Task(self.filename)
        # actual window of tkinter
        canvas = Canvas(self.master, width=1550, height=890, bg='bisque')
        canvas.pack()

        # Input fields for doc uuid
        doc_id_label = Label(self.master, text='Document UUID: ', bg='bisque')
        self.doc_id_box = Entry()
        doc_id_label.pack()
        self.doc_id_box.pack()
        doc_id_label.place(x=40, y=5)
        self.doc_id_box.place(x=40, y=35, width=270)
        # button to submit the data so that the new doc / visitor uuid can be used.
        set_file_button = Button(master=self.master, text='Submit', command=self.load)
        set_file_button.pack()
        set_file_button.place(x=136, y=125)
        # input label for visitor uuid
        user_id_label = Label(self.master, text='Visitor UUID: ', bg='bisque')
        self.user_id_box = Entry()
        user_id_label.pack()
        self.user_id_box.pack()
        user_id_label.place(x=40, y=65)
        self.user_id_box.place(x=40, y=95, width=270)
        # write the data from the command line into their input fields
        if self.doc_id is not None:
            self.doc_id_box.insert(0, self.doc_id)
        if self.visitor_uuid is not None:
            self.user_id_box.insert(0, self.visitor_uuid)

        # all the buttons for each graph. It calls the graph method to display the graph.
        button_views_by_country = Button(master=self.master,
                                         command=lambda: self.graph(1, 'Views by Country', 'Countries', 'Viewers'),
                                         text="Views by Country", bg='white')
        button_views_by_country.place(x=40, y=180, width=270, height=50)

        button_views_by_continent = Button(master=self.master,
                                           command=lambda: self.graph(2, 'Views by Continent', 'Continents',
                                                                      'Viewers'), text="Views by Continent", bg='white')
        button_views_by_continent.place(x=40, y=260, width=270, height=50)

        button_views_by_browser = Button(master=self.master,
                                         command=lambda: self.graph(31, 'Views by Browser', 'Browser', 'Views'),
                                         text="Views by Browser", bg='white')
        button_views_by_browser.place(x=40, y=340, width=270, height=50)

        button_views_by_browser_simplified = Button(master=self.master,
                                                    command=lambda: self.graph(32, 'Views by Browser Simplified',
                                                                               'Browser',
                                                                               'Views'),
                                                    text="Views by Browser Simplified", bg='white')
        button_views_by_browser_simplified.place(x=40, y=420, width=270, height=50)

        button_reader_profiles = Button(master=self.master,
                                        command=lambda: self.graph(4, 'Reader Profiles: Top 10 Most Avid Readers',
                                                                   'Visitor UUID', 'Time Spent Reading'),
                                        text="Reader Profiles", bg='white')
        button_reader_profiles.place(x=40, y=500, width=270, height=50)

        button_also_likes = Button(master=self.master,
                                   command=lambda: self.graph(5, 'Also Likes', 'Document UUID', 'No. of users'),
                                   text="Also Likes", bg='white')
        button_also_likes.place(x=40, y=580, width=270, height=50)

        button_also_likes_graph = Button(master=self.master,
                                         command=lambda: self.graph(6),
                                         text="Also Likes Graph", bg='white')
        button_also_likes_graph.place(x=40, y=650, width=270, height=50)

        # Vertical line to split the buttons and graphs
        canvas.create_line(350, 1500, 350, 0, fill="black", width=2)

        # Graph frame of where it should be placed
        self.graph_frame = Frame(self.master, bg='white')
        self.graph_frame.place(x=400, y=50, width=1100, height=800)
        # get the data from the command line and pre insert / run the selected graph onto the display
        print("Loading, please wait")
        if task == "7" or task == "6":
            button_also_likes_graph.invoke()
        elif task == "5d":
            button_also_likes.invoke()
        elif task == "4":
            button_reader_profiles.invoke()
        elif task == "3a":
            button_views_by_browser.invoke()
        elif task == "3b":
            button_views_by_browser_simplified.invoke()
        elif task == "2a":
            button_views_by_country.invoke()
        elif task == "2b":
            button_views_by_continent.invoke()

        self.master.mainloop()
