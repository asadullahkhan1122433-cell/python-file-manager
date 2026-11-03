from pathlib import Path


def readfileandfolder():
    path = Path(".")
    items = list(path.iterdir())

    print("\n----- Files and Folders -----")
    for i, item in enumerate(items, 1):
        print(f"{i}: {item}")


def createfile():
    try:
        name = input("Enter your file name: ")
        p = Path(name)

        if p.exists():
            print("File already exists!")
            return

        data = input("What do you want to write: ")

        with open(p, "w") as fs:
            fs.write(data)

        print("File created successfully!")

    except Exception as err:
        print(f"Error: {err}")


def readfile():
    name = input("Which file do you want to read: ")
    p = Path(name)

    try:
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                print("\nFile Content:")
                print(fs.read())

            print("File read successfully!")
        else:
            print("File does not exist!")

    except Exception as err:
        print(f"Error: {err}")


def updatefile():
    readfileandfolder()
    name = input("Enter the file name to update: ")
    p = Path(name)

    if not p.exists() or not p.is_file():
        print("File does not exist!")
        return

    print("\n1. Rename file")
    print("2. Overwrite file")
    print("3. Append content")

    try:
        option = int(input("Enter your choice: "))

        if option == 1:
            new_name = input("Enter new file name: ")
            p.rename(Path(new_name))
            print("File renamed successfully!")

        elif option == 2:
            data = input("Enter new content: ")
            with open(p, "w") as fs:
                fs.write(data)
            print("File overwritten successfully!")

        elif option == 3:
            data = input("Enter content to append: ")
            with open(p, "a") as fs:
                fs.write("\n" + data)
            print("Content appended successfully!")

        else:
            print("Invalid choice!")

    except Exception as err:
        print(f"Error: {err}")


def deletefile():
    readfileandfolder()
    name = input("Which file do you want to delete: ")
    p = Path(name)

    try:
        if p.exists() and p.is_file():
            confirm = input("Are you sure? (y/n): ")

            if confirm.lower() == "y":
                p.unlink()
                print("File deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("File does not exist!")

    except Exception as err:
        print(f"Error: {err}")


def main():
    while True:
        print("\n===== PYTHON FILE MANAGER =====")
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. List Files and Folders")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                createfile()
            elif choice == 2:
                readfile()
            elif choice == 3:
                updatefile()
            elif choice == 4:
                deletefile()
            elif choice == 5:
                readfileandfolder()
            elif choice == 6:
                print("Thank you for using Python File Manager!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main()