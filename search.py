import sqlite3


def search_samples():

    search_type = input("\nSearch by category or filename?")

    search_query = input("\nEnter search term: ")

    connection =sqlite3.connect("samples.db")
    cursor = connection.cursor()

    print("\nSearching samples....:")

    results = []

    if search_type.lower()== "category":

        cursor.execute(
            "SELECT * FROM samples WHERE category = ?",
            (search_query,)
        )
        results = cursor.fetchall()

        for row in results:
            print("\n<Match found:")
            print(("ID:", row[0]))
            print("Category:", row [1])
            print("Filename:", row[2])
            print("Extension:", row[3])









    if search_type.lower() == "filename":

        cursor.execute(
            "SELECT FROM sample WHERE filename LIKE ?",
            ('%' + search_query + '%',)
        )
        results = cursor.fetchall()

