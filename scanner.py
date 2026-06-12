# 'pathlib' is a tool that helps Python understand your computer's folders
import sqlite3
from pathlib import Path
import csv
from re import search

def scan_samples():
    samples_folder = Path("/Users/sypooda/Desktop/sample_library_test")

    audio_extensions =[".wav", ".mp3", ".aiff", ".flac"]

    output_file = "sample_database.csv"

    connection = sqlite3.connect("samples.db")
    cursor = connection.cursor() #db command tool, sends commands to db

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS samples (
        id INTEGER PRIMARY KEY,
        category TEXT,
        filename TEXT,
        extension TEXT,
        full_path TEXT
    
    )
    """)

    connection.commit() #saves db changes



    sample_count = 0


    with open (output_file, mode="w", newline="", encoding = "utf-8") as csv_file: #opens "paper" for writing
        writer = csv.writer(csv_file) #creates pen object that writes (also .writer method comes from the library) then saves it in variable "writer"
        writer.writerow(["Category", "Filename", "Extension", "Full Path"]) #writes header aka first row using the "writer" tool we created above. Think.. "use writer (object) to write row (method)"

        for file in samples_folder.rglob("*"): #everytime loop finds a valid file, the variables get new values
            if file.is_file() and file.suffix.lower() in audio_extensions:
                category = file.parent.name
                filename = file.name
                extension = file.suffix.lower()
                full_path = str(file)

                cursor.execute("""
                INSERT INTO samples (category, filename, extension, full_path)
                VALUES (?, ?, ?, ?)
                """, (category, filename, extension, full_path))

                sample_count += 1

    connection.commit()

    cursor.execute("SELECT * FROM samples")

    rows = cursor.fetchall()

    print("\nDatabase contents:")

    for row in rows:
        print(row)

    connection.close()



    print("\nDatabase created:",output_file)
    print("Total samples found:", sample_count)