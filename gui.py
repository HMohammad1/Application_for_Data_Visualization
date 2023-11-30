from tkinter import *
import numpy as np
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
    def load(self):
        # get user input
        file = self.input_doc_id.get()
        # update current file and get rid of white spaces
        self.doc_id = re.sub(r"\s+", "", file)
        new_file_label = Label(master=self.master, text=self.doc_id, bg='bisque')
        new_file_label.pack()
        new_file_label.place(x=600, y=20)

    # Generate graph
    # task_number denotes what task to display on the graph
    def graph(self, task_number, graph_name, x_axis, y_axis):
        # clear the graph and toolbar when displaying new graphs
        if self.clear_graph is not None:
            self.clear_graph.destroy()

        t = Task()
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
        figure_canvas = FigureCanvasTkAgg(figure, graph_frame)
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
        current_file_label.place(x=380, y=20, width=250)

        # Input field
        input_label = Label(self.master, text='Document ID: ', bg='bisque')
        input_box = Entry(textvariable=self.input_doc_id)
        input_label.pack()
        input_box.pack()
        input_label.place(x=50, y=55)
        input_box.place(x=50, y=85, width=250)
        set_file_button = Button(master=self.master, text='Load', command=self.load)
        set_file_button.pack()
        set_file_button.place(x=136, y=120)

        # Buttons
        button_views_by_country = Button(master=self.master,
                                         command=lambda: self.graph(1, 'Viewers by Country', 'Countries', 'Viewers'),
                                         text="Views by country", bg='white')
        button_views_by_country.place(x=50, y=180, width=250, height=50)

        button_views_by_continent = Button(master=self.master,
                                           command=lambda: self.graph(2, 'Viewers by Continent', 'Continents',
                                                                      'Viewers'), text="Views by continent", bg='white')
        button_views_by_continent.place(x=50, y=260, width=250, height=50)

        button_views_by_browser = Button(master=self.master, command=lambda: self.graph(31, 'Views by Browser', 'Browser', 'Views'),text="Views by browser", bg='white')
        button_views_by_browser.place(x=50, y=340, width=250, height=50)

        button_views_by_browser = Button(master=self.master,
                                         command=lambda: self.graph(32, 'Views by Browser Simplified', 'Browser', 'Views'),
                                         text="3b", bg='white')
        button_views_by_browser.place(x=50, y=440, width=250, height=50)

        button_reader_profiles = Button(master=self.master,
                                        command=lambda: self.graph(4, 'Reader Profiles: Top 10 Most Avid Readers',
                                                                   'Visitor UUID', 'Time Spent Reading'),
                                        text="Reader profiles", bg='white')
        button_reader_profiles.place(x=50, y=520, width=250, height=50)

        button_reader_profiles = Button(master=self.master,
                                        command=lambda: self.graph(5, 'Also Likes', 'Document UUID', 'No. of users'),
                                        text="Also Likes", bg='white')
        button_reader_profiles.place(x=50, y=620, width=250, height=50)

        # Vertical line
        canvas.create_line(350, 1500, 350, 0, fill="black", width=2)

        # Graph frame
        graph_frame = Frame(self.master, bg='white')
        graph_frame.place(x=400, y=50, width=1100, height=800)

        self.master.mainloop()
