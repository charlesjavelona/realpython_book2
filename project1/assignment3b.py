import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    cursor = connection.cursor()

    prompt = """
            Select the operation that you want to perform [1-5]:
            1. Average
            2. Max
            3. Min
            4. Sum
            5. Exit
            """

    while True:
        choice = input(prompt)

        if choice in set(["1", "2", "3", "4"]):
            #Parse the corresponding operation text
            operation = {1: "avg", 2: "max",
                         3: "min", 4: "sum"}
            #Retrieve data
            cursor.execute("SELECT {}(num) from numbers".format(operation))

            #Fetch one record from the database
            get_data = cursor.fetchone()

            #Output result
            print(operation + ": %f" % get_data[0])
        elif choice == "5":
            print("Exiting...\n Goodbye!")
            break

            
