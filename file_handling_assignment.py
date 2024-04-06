def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("012345\n")
            file.write("New line here.\n")
        print("File created successfully.")
    except FileNotFoundError:
        print("File not found or cannot be created.")
    except PermissionError:
        print("Permission denied.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found or cannot be opened.")
    except PermissionError:
        print("Permission denied.")

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("111222\n")
            file.write("Yet another line appended.\n")
        print("File appended successfully.")
    except FileNotFoundError:
        print("File not found or cannot be opened.")
    except PermissionError:
        print("Permission denied.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()

