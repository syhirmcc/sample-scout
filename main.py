# 'pathlib' is a tool that helps Python understand your computer's folders
from pathlib import Path
import csv
from re import search

samples_folder = Path("/Users/sypooda/Desktop/sample_library_test")
audio_extensions =[".wav", ".mp3", ".aiff", ".flac"]
output_file = "sample_database.csv"
sample_count = 0


with open (output_file, mode="w", newline="", encoding = "utf-8") as csv_file: #opens "paper" for writing
    writer = csv.writer(csv_file) #creates pen object that writes (also .writer method comes from the library) then saves it in variable "writer"
    writer.writerow(["Category", "Filename", "Extension", "Full Path"]) #writes header aka first row using the "writer" tool we created above. Think.. "use writer (object) to write row (method)"

    for file in samples_folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in audio_extensions:
            category = file.parent.name
            filename = file.name
            extension = file.suffix.lower()
            full_path = str(file)

            writer.writerow([category, filename, extension, full_path])
            sample_count += 1
            print(file.parent.name, ":", file.name)

print("\nDatabase created:",output_file)
print("Total samples found:", sample_count)


search_type = input("\nSearch by category or filename?")


search_query = input("\nEnter search term: ")

with open(output_file, mode="r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    print("\nSearch results:")

    for row in reader:

        #categorysearch
        if search_type.lower() == "category":

            if row ["Category"].lower() == search_query.lower():

                print("\nCategory match found:")
                print("Category:", row["Category"])
                print("Filename:", row["Filename"])
                print("Extension", row["Extension"])


        #filenamesearch
        if search_type.lower() == "filename":

            if search_query.lower() in row["Filename"].lower():

                print("\nFilename match found:")
                print("Category:", row["Category"])
                print("Filename:", row["Filename"])
                print("Extension:", row["Extension"])






            










