# Application for Data Visualization
An application that provides data analysis of a document tracker (via parsed json files). The application both supports a command line interface to quickly show a specific graph when loading a gui or using just the gui to navigate the different graphs avaliable. 

To run load the program into your IDE and run the main.py file. You will be shown the main interface: 

<img width="1168" alt="image" src="https://github.com/user-attachments/assets/00212e91-6b19-4769-8009-e6b71d430c01" />

To load a file select 'File' and locate 'test.json'. Open the file in notepad or alternative and locate the variable named 'env_doc_id'. Copy it's ID into the 'Document UUID' field. This is the unique identifier for each document. Locate the variable named 'visitor_uuid' and copy it's content into 'Visitor UUID', the unique identifier for a person. Click submit to load it into the application. 

The 7 functions avaliable include:

1. Views by country: Displays a bar chart of the total number of viewers from each country that
viewed the input document.

2. Views by continent: Groups the countries from the previous functionality and displays a bar
chart of the total number of viewers from each continent that viewed the input document.

3. Views by browser: Displays a bar chart of all browsers used by viewers, plus an additional
functionality to display a bar chart of only the main browser names.

4. As above but only shows the main browsers. 

5. Reader profiles: Displays a bar chart of the top 10 most avid readers and their total time
spent reading.

6. Also likes functionality: Displays a bar chart of the top 10 documents also liked by other
readers based on the number of readers of the same input document. Uses a sorting function
parameter

7. Also likes graph: Generates a graph representation of the above functionality in .pdf format.
Document UUIDs and visitor UUIDs have been shortened to their last 4 hex digits. To run this function download: https://graphviz.org/download/ which is used to render the graph and make the pdf. A windows restart will be required.

