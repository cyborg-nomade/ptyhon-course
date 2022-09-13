"""Assignment 6

1) Write a short Python script which queries the user for input
(infinite loop with exit possibility) and writes the input to a file.

2) Add another option to your user interface:
The user should be able to output the data stored in the file in the terminal.

3) Store user input in a list (instead of directly adding it to the file)
and write that list to the file – both with pickle and json.

4) Adjust the logic to load the file content to work with pickled/ json data.
"""

import pickle
import json

USER_INPUT = ""
WRITE_CONTENT = []
while USER_INPUT != "exit":
    print("Choose an option:")
    print("1- Write to file")
    print("2- Read from file")
    print("3- Exit")
    USER_INPUT = input("Your choice: ")
    match USER_INPUT:
        case "1":
            LINE_OF_CONTENT = input("Content to write to file: ")
            WRITE_CONTENT.append(LINE_OF_CONTENT)
        case "2":
            with open("assignment.txt", mode="r", encoding="utf-8") as f:
                JSON_CONTENT = json.loads(f.read())
                print("\nThis is the json file content")
                print(20 * "-")
                for line in JSON_CONTENT:
                    print(line)
                print(20 * "-")
            with open("assignment.b", mode="rb") as f:
                PICKLE_CONTENT = pickle.loads(f.read())
                print("\nThis is the pickle file content")
                print(20 * "-")
                for line in PICKLE_CONTENT:
                    print(line)
                print(20 * "-")
        case "3":
            USER_INPUT = "exit"
    with open("assignment.txt", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(WRITE_CONTENT))
    with open("assignment.b", mode="wb") as f:
        f.write(pickle.dumps(WRITE_CONTENT))
