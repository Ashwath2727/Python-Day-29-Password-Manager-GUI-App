import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

add_button = tk.Button(text="Add", width=40)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()