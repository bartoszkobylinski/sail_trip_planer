import logging
import sqlite3

from points import points


def make_database():
    database_connection = sqlite3.connect('weather.db')
    database_connection.execute("DROP TABLE IF EXISTS Conditions")
    database_connection.commit()

    try:
        with database_connection:
            database_connection.execute("""CREATE TABLE Conditions(
                Points TEXT,
                Dates TEXT,
                Dayquaters TEXT,
                Windspeed INTEGER,
                Gust INTEGER,
                Winddirection TEXT,
                Wave INTEGER,
                Wavepeak INTEGER,
                Wavedirection TEXT,
                Periods INTEGER 
            )
            """)
    except sqlite3.OperationalError as error:
        logging.warning(error)

def insert_data_to_database(dictionary,point):
    # Inserting a data to a database from given dictionary
    database_connection = sqlite3.connect('weather.db')
    cursor = database_connection.cursor()
    cursor.execute("SELECT Points, Dates, Dayquaters from Conditions WHERE Points=? AND Dates=? AND Dayquaters=?",(point, dictionary['Dates'],dictionary['Dayquaters']))
    result = cursor.fetchone()
    if not result:
        cursor.execute("INSERT INTO Conditions VALUES (?,?,?,?,?,?,?,?,?,?)",
        [point,
        dictionary['Dates'],
        dictionary['Dayquaters'],
        dictionary['Windspeed'],
        dictionary['Gust'],
        dictionary['Winddirection'],
        dictionary['Wave'],
        dictionary['Wavepeak'],
        dictionary['Wavedirection'],
        dictionary['Periods']])

    database_connection.commit()
    cursor.close()

def get_data_from_database():
    database_connection = sqlite3.connect('weather.db')
    cursor = database_connection.cursor()
    cursor.execute("SELECT * FROM Conditions")
    rows = cursor.fetchall()
    return rows
