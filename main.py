import json
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_numbers + random_letters + random_symbols

    random.shuffle(password_list)
    print(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_to_file():
    website = website_entry.get()
    print(website)
    email = email_entry.get()
    print(email)
    password = password_entry.get()
    print(password)

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please dont leave any fields empty!")
    else:
        try:
            with open("data-main.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open('data-main.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("data-main.json", "w") as file:
                #saving the updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    print("Searching...")

    website = website_entry.get()
    print(website)

    try:
        with open("data-main.json", "r") as file:
            data = json.load(file)
            print(data.get(website))

            if website in data.keys():
                messagebox.showinfo(website, f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")

            else:
                messagebox.showerror("Error", "No details for the website exists")

    except FileNotFoundError:
        print("File not found.")
        messagebox.showerror("Error", "No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img =tk.PhotoImage(file="logo.png")
canvas.create_image(100, 113, image=logo_img)
canvas.grid(row=0, column=1, pady=10)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, pady=10)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=10)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, pady=10)

# website_entry = tk.Entry()
website_entry = tk.Entry(width=27)
website_entry.focus()
website_entry.grid(row=1, column=1, pady=10)
# website_entry.grid(row=1, column=1, pady=10)

email_entry = tk.Entry(width=45)
email_entry.insert(0, "ashwath@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=10)

password_entry = tk.Entry(width=27)
password_entry.grid(row=3, column=1, pady=10)

gen_pass_button = tk.Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2, pady=10)

add_button = tk.Button(text="Add", width=40, command=save_password_to_file)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

search_button = tk.Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, pady=10)

window.mainloop()