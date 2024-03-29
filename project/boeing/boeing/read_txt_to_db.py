# this file only needs to be run once per txt file to initialize the table

import sqlite3
from settings import BASE_DIR, DATABASES


def init_table(table, route, source):
    # connect to database
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    # check if table already exists (to avoid adding to an existing table)
    table_list = cursor.execute("SELECT flight_name FROM flights").fetchall()
    if table in [i[0] for i in table_list]:
        print("This table already exists!")
        return

    # create table with given name
    cursor.execute("""CREATE TABLE {} (
                   Row INT NOT NULL,
                   Seat CHAR(2) NOT NULL ,
                   Occupied BOOLEAN NOT NULL,
                   Userid INT
                   );""".format(table))

    # read from given text file
    with open(source) as f:
        text_file = f.read().split()

    # text_file = [element for element in text_file if element.isalpha()]  # remove numbers from text file
    rows = 0
    columns = len(set(text_file))
    # text_file = text_file[columns:]  # remove the first line of seats (it is only used as a header in the txt file)
    first_row = []
    for i in text_file:
        if i.isnumeric():
            rows += 1
            counter = 0
        elif rows == 0:
            first_row.append(i)
        elif rows >= 1:
            counter += 1
            if i == "X":
                # add rows, i, False to table
                cursor.execute("""INSERT INTO {} VALUES (?, ?, ?, ?)""".format(table),
                               (rows, first_row[counter-1], True, None))
            else:
                cursor.execute("""INSERT INTO {} VALUES (?, ?, ?, ?)""".format(table),
                               (rows, i, False, None))

    cursor.execute("INSERT INTO flights VALUES (?, ?)", (table, route))
    # commit changes and close connection
    connection.commit()
    connection.close()
    print(f"Created new table {table} and added it to flights with route {route}")


if __name__ == "__main__":
    file_name = r"chartIn3.txt"
    init_table("flight05", "Bremen - Seattle",
               str(BASE_DIR).removesuffix("boeing") + "project_description\\" + file_name)
