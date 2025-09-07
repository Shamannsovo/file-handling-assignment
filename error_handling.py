# error_handling.py

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as f:
        print("\n📂 File content:\n")
        print(f.read())
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print("⚠️ An unexpected error occurred:", e)