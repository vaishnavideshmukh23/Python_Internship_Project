# A Basic File Handling Project.2
print("Welcome to the Basic File Handling Project")

while True:
    print("1. Add Note ")
    print("2. View Notes")
    print("3. Edit Notes")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter you choice :  ")

    if choice == "1":
        note = input("Enter your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved!")

    elif choice == "2":
        try:
            file = open("notes.txt", "r")
            print("\nYour Notes:")
            print(file.read())
            file.close()

        except FileNotFoundError:
            print("File not found!")

    elif choice == "3":
        try:
            file = open("notes.txt", "r")
            content = file.read()
            file.close()
            old_word = input("Enter word to find: ")
            new_word = input("Enter replacement word: ")

            content = content.replace(old_word, new_word)

            file = open("notes.txt", "w")
            file.write(content)
            file.close()

            print("Note updated successfully!")

        except FileNotFoundError:
            print("File not found!")

    elif choice == "4":
        try:
            file = open("notes.txt", "r")
            content = file.read()
            file.close()

            word = input("Enter word to remove: ")

            content = content.replace(word,"")

            file = open("notes.txt", "w")
            file.write(content)
            file.close()

            print("Removed successfully!")
        except FileNotFoundError:
            print("File not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


