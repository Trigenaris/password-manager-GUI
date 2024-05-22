from random import randint, choice, shuffle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Generates a randomized password for the user and insert it on the relevant entry box.
    :returns None:
    """
    label_title.config(fg="dark blue")
    entry_password.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)

# ---------------------------- ENCRYPTION AND DECRYPTION ------------------------------- #


def cipher(text, shift, method="encode"):
    """
    Function applies a simple Caesar cipher on the argument text.
    :param text: Expects a text from the user to process. (English alphabet based)
    :param shift: Expects an integer to decide the shift amount of the text.
    :param method: Expects a specific string `encode` or `decode` to decide sign of the shift integer
    :returns the last, encrypted version of the text:
    """

    encrypted_text = ""

    if method == "decode":
        shift *= -1

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index = letters.index(char)
            new_index = (index + shift) % 26
            new_char = letters[new_index]
            if is_upper:
                new_char = new_char.upper()
            encrypted_text += new_char
        elif char.isdigit():
            index = numbers.index(char)
            new_index = (index + shift) % 10
            new_char = numbers[new_index]
            encrypted_text += new_char
        elif char in symbols:
            index = symbols.index(char)
            new_index = (index + shift) % len(symbols)
            new_char = symbols[new_index]
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Takes the entries, applies cipher function on the email and password string and then save them in a txt file
    named as `data`
    :returns None:
    """
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"""These are the details entered:
    Email: {email}
    Password: {password}
    Is it ok to save?
    Note: Your password and mail will be encrypted.
    """)

    try:
        if is_ok:
            encrypted_email = cipher(email.strip(), (len(website)+letters.index(website[0])))
            encrypted_password = cipher(password.strip(), len(website)+letters.index(website[0]))
            label_info.config(text="Password saved.", fg="dark blue")
            with open("data.txt", "a", encoding="UTF-8") as file:
                file.write(f"{website} | {encrypted_email} | {encrypted_password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)
    except Exception as e:
        messagebox.showwarning(title="Error!", message=f"{e}")

# ---------------------------- LOAD PASSWORD ------------------------------- #


def load():
    """
    Expects the encrypted version of the entries (excluding website entry) and calls cipher function with `decode`
    parameter to decrypt the entries  for the user.
    :returns None:
    """
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"""These are the details entered:
    Email: {email}
    Password: {password}
    Is it ok to load?
    Note: Your password and mail will be decrypted.
    """)

    if is_ok:
        decrypted_email = cipher(email.strip(), (len(website)+letters.index(website[0])), method="decode")
        decrypted_password = cipher(password.strip(), (len(website)+letters.index(website[0])), method="decode")
        label_info.config(text="Password loaded.", fg="dark green")
        entry_email.delete(0, END)
        entry_password.delete(0, END)
        entry_email.insert(0, decrypted_email)
        entry_password.insert(0, decrypted_password)

# ---------------------------- UI SETUP ------------------------------- #


# main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
window.resizable(False, False)
window.iconbitmap("icon.ico")

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="main_logo1.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=1, columnspan=2)

# labels
label_title = Label(text="My Password", bg="white", fg="dark blue", font=("Courier", 35, "bold"))
label_title.grid(row=0, column=1, columnspan=2)
label_info = Label(text="", bg="white", fg="dark blue", font=("Courier", 12, "bold"))
label_info.grid(row=2, column=1, columnspan=2)
label_website = Label(text="Website: ", bg="white")
label_website.grid(row=3, column=0, sticky="e")
label_email = Label(text="Email/Username: ", bg="white")
label_email.grid(row=4, column=0, sticky="e")
label_password = Label(text="Password: ", bg="white")
label_password.grid(row=5, column=0, sticky="e")

# entries
entry_website = ttk.Entry(window, width=63)
entry_website.grid(row=3, column=1, columnspan=2, sticky="w")
entry_email = ttk.Entry(window, width=63)
entry_email.grid(row=4, column=1, columnspan=2, sticky="w")
entry_password = ttk.Entry(window, width=50)
entry_password.grid(row=5, column=1, columnspan=2, sticky="w")

# buttons
button_password = ttk.Button(window, text="Generate Password", command=generate_password)
button_password.grid(row=5, column=2, sticky="e")
button_add = ttk.Button(window, text="Save & Encrypt", width=30, command=save)
button_add.grid(row=6, column=1, sticky="w")
button_load = ttk.Button(window, text="Load & Decrypt", width=30, command=load)
button_load.grid(row=6, column=2, sticky="w")

window.mainloop()
