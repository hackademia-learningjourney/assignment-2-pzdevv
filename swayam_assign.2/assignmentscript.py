import json
import random

#making an error code to make it seem hacker like
errcode = random.randint(1, 122)


def load_data(filename='users.json'):

        with open(filename, 'r') as f:
            return json.load(f)



def save_data(data, filename='users.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)


def signup(data):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    number = input("Enter your number: ")

    if username in data:
        print("Username already exist")
    else:
        data[username] = password
        save_data(data)
        print(f"Signup successful! {number}")


def signin(data):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    stored_password = data.get(username)

    if stored_password and stored_password == password:
        print(f"Login Successful! ")
    else:
        print(f"Login failed! {errcode}")


def main():
    data = load_data()

    while True:
        print("1) Signup")
        print("2) Login")
        print("3) Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            signup(data)
        elif choice == '2':
            signin(data)
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

#i dont know what this is but i saw in many other people's code footers. it is a popular idiom.
if __name__ == "__main__":
    main()
