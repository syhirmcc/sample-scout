import sqlite3
from scanner import scan_samples
from search import search_samples

print("\nSample Scout")

print("1. Scan Library")
print("2. Search Samples")
print("3. Exit")

choice = input("\n Select option: ")
if choice == "1":
    scan_samples()

elif choice == "2":


    results = search_samples()

    print("\nReturned Results:")
    print(results)

elif choice == "3":
    print("Goodbye.")
else:
    print("Invalid option.")

