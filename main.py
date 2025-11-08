import tkinter as tk
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_to_file():
    website = website_entry.get()
    print(website)
    email = email_entry.get()
    print(email)
    password = password_entry.get()
    print(password)

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                                      f"\nEmail: {email}"
                                                      f"\nPassword: {password}"
                                                      f"\nIs is ok to save?")
        if is_ok:

            with open("data-main.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

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

website_entry = tk.Entry(width=45)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, pady=10)

email_entry = tk.Entry(width=45)
email_entry.insert(0, "ashwath@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=10)

password_entry = tk.Entry(width=27)
password_entry.grid(row=3, column=1, pady=10)

gen_pass_button = tk.Button(text="Generate Password")
gen_pass_button.grid(row=3, column=2, pady=10)

add_button = tk.Button(text="Add", width=40, command=save_password_to_file)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()