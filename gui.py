from tkinter import *
import numpy as np
from task import Task
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re


class Gui():
    global master
    clear_graph = None
    toolbar = None
    global user_id_box
    global visitor_uuid
    global doc_id_box
    global graph_frame
    global doc_id
    global filename

    # Load new file
    def load(self, doc=None, visitor=None):
        # get user input
        file = self.doc_id_box.get()
        visitor = self.user_id_box.get()
        # update current file and get rid of white spaces
        self.doc_id = re.sub(r"\s+", "", file)
        self.visitor_uuid = re.sub(r"\s+", "", visitor)

    # Generate graph
    # task_number denotes what task to display on the graph
    def graph(self, task_number, graph_name=None, x_axis=None, y_axis=None):
        # clear the graph and toolbar when displaying new graphs
        if self.clear_graph is not None:
            self.clear_graph.destroy()

        t = Task(self.filename)
        x = None
        y = None
        # display the graph depending on which button is pressed
        if task_number == 1:
            x, y = t.task_2_a(self.doc_id)
        if task_number == 2:
            x, y = t.task_2_b(self.doc_id)
        if task_number == 31:
            x, y = t.task_3_a()
        if task_number == 32:
            x, y = t.task_3_b()
        if task_number == 4:
            x, y = t.task_4()
        if task_number == 5:
            x, y = t.task_5_d(self.doc_id)

        # creates new figure
        figure = Figure(figsize=(10, 10), dpi=70)
        # new canvas to insert in figure
        figure_canvas = FigureCanvasTkAgg(figure, self.graph_frame)
        # add graph toolbar
        # self.toolbar = NavigationToolbar2Tk(figure_canvas, graph_frame)
        axes = figure.add_subplot()
        axes.bar(x, y)
        axes.set_title(graph_name, fontsize=12)
        axes.set_xlabel(x_axis, fontsize=12)
        axes.set_ylabel(y_axis, fontsize=12)
        axes.tick_params(axis='x', labelsize=10)
        # adjusts labels for reader profiles to fit in frame
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
        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=0.5)
        self.clear_graph = figure_canvas.get_tk_widget()

    def __init__(self, filename, task=None, visitor=None, doc=None):
        t = Task(filename)
        self.filename = filename
        self.doc_id = re.sub(r"\s+", "", doc)
        self.visitor_uuid = re.sub(r"\s+", "", visitor)
        self.master = Tk()
        self.master.title("Document Tracker")
        self.input_doc_id = StringVar()

        canvas = Canvas(self.master, width=1550, height=890, bg='bisque')
        canvas.pack()

        # Input field
        doc_id_label = Label(self.master, text='Document UUID: ', bg='bisque')
        self.doc_id_box = Entry()
        doc_id_label.pack()
        self.doc_id_box.pack()
        doc_id_label.place(x=40, y=5)
        self.doc_id_box.place(x=40, y=35, width=270)

        set_file_button = Button(master=self.master, text='Submit', command=self.load)
        set_file_button.pack()
        set_file_button.place(x=136, y=125)

        user_id_label = Label(self.master, text='Visitor UUID: ', bg='bisque')
        self.user_id_box = Entry()
        user_id_label.pack()
        self.user_id_box.pack()
        user_id_label.place(x=40, y=65)
        self.user_id_box.place(x=40, y=95, width=270)

        self.doc_id_box.insert(0, doc)
        self.user_id_box.insert(0, visitor)

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
                                         command=lambda: t.task_6(self.doc_id, self.visitor_uuid),
                                         text="Also Likes Graph", bg='white')
        button_also_likes_graph.place(x=40, y=650, width=270, height=50)

        # Vertical line
        canvas.create_line(350, 1500, 350, 0, fill="black", width=2)

        # Graph frame
        self.graph_frame = Frame(self.master, bg='white')
        self.graph_frame.place(x=400, y=50, width=1100, height=800)

        if task == "7" or task == "6":
            t.task_6(doc, visitor)
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
