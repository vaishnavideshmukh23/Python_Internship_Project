#Simple Currency Converter

print("=== Currency Converter ===")

print("1. USD to INR")
print("2. INR to USD")
print("3. EUR to INR")
print("4. INR to EUR")

choice = input("Enter choice: ")
amount = float(input("Enter amount: "))

if choice == "1":
    print("INR =", amount * 83.5)

elif choice == "2":
    print("USD =", amount / 83.5)

elif choice == "3":
    print("INR =", amount * 95)

elif choice == "4":
    print("EUR =", amount / 95)

else:
    print("Invalid choice!")
