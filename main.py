from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    def __init__(self, visitor):
        self.visitor = visitor
        super().__init__(f"Visitor '{visitor}' has already visited." )

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    try:
        with open(FILENAME, "r") as f:
            pass 
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found. Creating the file now.")
        with open(FILENAME, "w") as f:
            pass

def get_last_visitor():
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if lines:
            return lines[-1].strip().split(" | ")[0] 

def add_visitor(visitor_name):
    last_visitor = get_last_visitor()

    if visitor_name == last_visitor:
        raise DuplicateVisitorError(visitor_name)
    
    timestamp = datetime.now().isoformat()
    entry = f"{visitor_name} | {timestamp}\n"

    with open(FILENAME, "a") as f:
        f.write(entry)

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
