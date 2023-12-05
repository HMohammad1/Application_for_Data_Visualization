from gui import Gui
from task import Task

global input_doc_id
import sys
import argparse

if __name__ == '__main__':
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Process user input')

    # Add the expected arguments
    parser.add_argument('-u', '--user_uuid', type=str, help='User UUID')
    parser.add_argument('-d', '--doc_uuid', type=str, help='Document UUID')
    parser.add_argument('-t', '--task_id', type=str, help='Task ID')
    parser.add_argument('-f', '--file_name', type=str, help='File Name')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using the argument names
    visitor_uuid = args.user_uuid
    doc_uuid = args.doc_uuid
    task_id = args.task_id
    file_name = args.file_name

    if visitor_uuid is None and doc_uuid is None and task_id is None and file_name is None:
        Gui()
    elif task_id == "7" or task_id == "6":
        gui = Gui(file_name, "7", visitor_uuid, doc_uuid)
    elif task_id == "5d":
        gui = Gui(file_name, "5d", visitor_uuid, doc_uuid)
    elif task_id == "4":
        gui = Gui(file_name, "4", visitor_uuid, doc_uuid)
    elif task_id == "3a":
        gui = Gui(file_name, "3a", visitor_uuid, doc_uuid)
    elif task_id == "3b":
        gui = Gui(file_name, "3b", visitor_uuid, doc_uuid)
    elif task_id == "2a":
        gui = Gui(file_name, "2a", visitor_uuid, doc_uuid)
    elif task_id == "2b":
        gui = Gui(file_name, "2b", visitor_uuid, doc_uuid)
