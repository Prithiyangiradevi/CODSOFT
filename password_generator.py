# CODSOFT Internship - Task 2 (Password Generator)
# Author: Prithiyangira Devi
# Project: Smart Password Generator

import random
import string

def show_intro():
    print("\n🔐 Welcome to Smart Password Generator 🔐")
    print("Create secure passwords with just a few choices.\n")

def choose_length():
    while True:
        try:
            length = int(input("👉 Enter desired password length (minimum 4): "))
            if length < 4:
                print("❌ Password length too short! Try again.")
            else:
                return length
        except ValueError:
            print("❌ Please enter a valid number.")

def choose_complexity():
    print("\nChoose password complexity level:")
    print("1. Easy   (Letters only)")
    print("2. Medium (Letters + Numbers)")
    print("3. Strong (Letters + Numbers + Symbols)")
    
    while True:
        choice = input("👉 Enter 1, 2, or 3: ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

def generate_password(length, complexity):
    if complexity == 1:
        chars = string.ascii_letters
    elif complexity == 2:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def password_strength(length, complexity):
    if complexity == 1 and length < 8:
        return "Weak ⚠️"
    elif complexity == 2 and length >= 8:
        return "Moderate 💡"
    elif complexity == 3 and length >= 10:
        return "Strong 💪"
    else:
        return "Okay 👍"

def main():
    show_intro()
    
    length = choose_length()
    complexity = choose_complexity()
    
    # Ask if user wants more than one password
    try:
        count = int(input("\n👉 How many passwords do you want to generate? (default = 1): ") or 1)
    except ValueError:
        count = 1
    
    print("\n🔑 Generated Passwords:")
    for i in range(count):
        pwd = generate_password(length, complexity)
        print(f"{i+1}. {pwd}")
    
    print("\n💡 Password Strength Hint:", password_strength(length, complexity))
    print("\n✅ Done! Use these passwords safely.")

if __name__ == "__main__":
    main()
