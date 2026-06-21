#Word Count Tool

print("=== Word Count Tool ===")

while True:
    text = input("\nEnter text: ")

    words = len(text.split())
    characters = len(text)

    print("\nWord Count:", words)
    print("Character Count:", words)

    choice = input("\nCount another text? (yes/no): ")

    if choice.lower() != "yes":
        print("Goodbye!")
        break
