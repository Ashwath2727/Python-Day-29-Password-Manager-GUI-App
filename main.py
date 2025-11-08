import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo_img =tk.PhotoImage(file="logo.png")
canvas.create_image(100, 113, image=logo_img)


canvas.grid(row=0, column=0)


window.mainloop()