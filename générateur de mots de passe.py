import tkinter as tk
import secrets
import os
import pyperclip
from tkinter import messagebox

# Vérification qu'il y à au moins une case à cocher de sélectionnée
def check_case():
    capital_checked = capital_letters_var.get()
    small_checked = small_letters_var.get()
    numbers_checked = numbers_var.get()
    special_characters_checked = special_characters_var.get()

    if not (capital_checked or small_checked or numbers_checked or special_characters_checked):
        messagebox.showerror("Erreur", "Vous devez sélectionner au moins une case à cocher")
        return False
    else:
        generate_password()


# Fonction pour changer la couleur du bouton de copie du mot de passe généré
def on_enter(event):
    copy_button.configure(bg=color_button_hover)
def on_leave(event):
    copy_button.configure(bg=color_button_default)
def on_click(event):
    copy_button.configure(bg=color_button_click)

# Fonction pour changer la couleur du bouton de génération du mot de passe
def on_enter_generate(event):
    generate_button.configure(bg=color_button_hover)
def on_leave_generate(event):
    generate_button.configure(bg=color_button_default)
def on_click_generate(event):
    generate_button.configure(bg=color_button_click)

# Fonction pour changer la couleur du bouton de réinitialisation des options de génération du mot de passe
def on_enter_reset(event):
    reset_button.configure(bg=color_button_hover)
def on_leave_reset(event):
    reset_button.configure(bg=color_button_default)
def on_click_reset(event):
    reset_button.configure(bg=color_button_click)

# Fonction pour copier le mot de passe généré dans le presse-papier
def copy_password():
    pyperclip.copy(password_var.get())

# Fonction pour générer le mot de passe
def update_password(val):
    global password
    global password_capital_letters_var
    global password_small_letters_var
    global password_numbers_var
    global password_special_characters_var
    global password_length_var
    global password_characters
    global length_password_scale
    
    # Vérification de la valeur de la scale
    try:
        val = int(val)
    except ValueError:
        print("Erreur : La valeur de la scale n'est pas un nombre")
        return


    password_capital_letters_var = ""
    password_small_letters_var = ""
    password_numbers_var = ""
    password_special_characters_var = ""
    password_length_var = 0
    password_characters = ""

    # Définition des variables pour les caractères à utiliser
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()_+-=[]{};':,./<>?"
    safe_special_characters = "!@#$%^*()_+-=;:,.<>?" # Caractères spéciaux sans les caractères qui peuvent poser problème dans certains navigateurs

    # Définition des variables pour les caractères à utiliser
    capital_letters_used = False
    small_letters_used = False
    numbers_used = False
    special_characters_used = False

    capital_letters_checked = capital_letters_var.get()
    small_letters_checked = small_letters_var.get()
    numbers_checked = numbers_var.get()
    special_characters_checked = special_characters_var.get()

    # Définition de la longueur du mot de passe
    password_length = length_password_scale.get()
    password_length = int(val)

    # Vérification si la condition "safe_mode" est activée
    if safe_mode_var.get() == 1:
        special_characters = safe_special_characters

    # Définition des caractères à utiliser
    if capital_letters_checked:
        capital_letters_used = True
        password_capital_letters_var = capital_letters
    if small_letters_checked:
        small_letters_used = True
        password_small_letters_var = small_letters
    if numbers_checked:
        numbers_used = True
        password_numbers_var = numbers
    if special_characters_checked:
        special_characters_used = True
        password_special_characters_var = special_characters

    if capital_letters_used:
        password_characters += password_capital_letters_var
    if small_letters_used:
        password_characters += password_small_letters_var
    if numbers_used:
        password_characters += password_numbers_var
    if special_characters_used:
        password_characters += password_special_characters_var

def reset_password_generator(): # (remais la scale à 8, les cases à cocher par defaut, et la zone de texte vide)
    global password
    global password_capital_letters_var
    global password_small_letters_var
    global password_numbers_var
    global password_special_characters_var
    global password_length_var
    global password_characters
    global length_password_scale

    password = ""
    password_capital_letters_var = ""
    password_small_letters_var = ""
    password_numbers_var = ""
    password_special_characters_var = ""
    password_length_var = 25
    password_characters = ""
    safe_mode_checkbox.deselect()

    capital_letters_var.set(1)
    small_letters_var.set(1)
    numbers_var.set(1)
    special_characters_var.set(1)
    length_password_scale.set(25)
    password_var.set(password)
    


def generate_password():
    update_password(length_password_scale.get())

    global password
    global password_capital_letters_var
    global password_small_letters_var
    global password_numbers_var
    global password_special_characters_var
    global password_length_var
    global password_characters
    #global length_password_scale

    password = ""
    password_length = length_password_scale.get()
    password_length = int(password_length)
    for i in range(password_length):
        password += secrets.choice(password_characters)
    password_var.set(password)

# Définition de la fenêtre
window = tk.Tk()
windows_width = 790
windows_height = 390
window.title("Générateur de mot de passe")
window.geometry(f"{windows_width}x{windows_height}")
window.minsize(windows_width, windows_height)
window.maxsize(windows_width, windows_height)
window.attributes("-fullscreen", False)
window.resizable(False, False)
window.config(background="#2f3138")

# Définition des variables
color_button_default = "#afb5d0"
color_button_hover = "#c3c3dd"
color_button_click = "#808091"
password = ""
password_var = tk.StringVar()
password_var.set(password)
password_capital_letters_var = ""
password_small_letters_var = ""
password_numbers_var = ""
password_special_characters_var = ""
password_length_var = 25
password_characters = ""

# Définition du frame contenant les options de génération du mot de passe
title_frame = tk.Frame(window, bg="#2f3138")
title_frame.pack(anchor=tk.CENTER, padx=10, pady=10)

# Définition du frame contenant le label
label = tk.Label(title_frame, text="Générateur de mot de passe", font=("Lucida Console", 20), bg="#2f3138", fg="#ffffff")
label.pack(anchor=tk.CENTER, expand=True)

# Définition du frame contenant le bouton de copie du mot de passe généré
password_and_copy_button_frame = tk.Frame(window, bg="#2f3138")
password_and_copy_button_frame.pack(anchor=tk.CENTER, padx=10, pady=10)
# Définition du frame contenant le mot de passe généré
password_frame = tk.Frame(password_and_copy_button_frame, bg="#2f3138")
password_frame.grid (row=0, column=0)
# Définition des widgets du frame contenant le mot de passe généré
#entry = tk.Entry(password_frame,  ,font=("Lucida Console", 20), bg="#afb5d0", fg="#43454f", width=20, borderwidth=0)
entry = tk.Entry(password_frame, textvariable=password_var, font=("Lucida Console", 20), bg="#afb5d0", fg="#43454f", width=40, borderwidth=0, state="readonly")
entry.pack(anchor=tk.W, expand=True)

# Définition d'un bouton pour copier le mot de passe généré à droite du mot de passe généré dans le meme frame
copy_button = tk.Button(password_and_copy_button_frame, text="Copier", font=("Lucida Console", 15), bg="#afb5d0", fg="#43454f", borderwidth=1, command=copy_password)
copy_button.grid(row=0, column=1, padx=10)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)
copy_button.bind("<Button-1>", on_click)

# Définition du frame contenant les options de génération du mot de passe
options_frame = tk.Frame(window, bg="#2f3138")
options_frame.pack(anchor=tk.CENTER, padx=10, pady=10)

# Définition du frame contenant les options de génération du mot de passe (Les case à cocher)
options_checkboxes_frame = tk.Frame(options_frame, bg="#2f3138", bd=0, highlightthickness=0,)
options_checkboxes_frame.grid(row=0, column=0)

# texte pour les case à cocher (personalisation du mon de passe)
personalisation_label = tk.Label(options_checkboxes_frame, text="Personnalisation", font=("Lucida Console", 11), bg="#2f3138", fg="#ffffff", width=20)
personalisation_label.pack(anchor=tk.W, expand=True, padx=40, pady=10)

# Les case à cocher
capital_letters_var = tk.BooleanVar()
capital_letters_var.set(True)

# Définition des widgets des case à cocher
capital_letters_checkbox = tk.Checkbutton(options_checkboxes_frame, text="Lettres majuscules", font=("Lucida Console", 15), bg="#2f3138", fg="#ffffff", activebackground="#2f3138", activeforeground="#ffffff", selectcolor="#2f3138", highlightthickness=0, bd=0, variable=capital_letters_var)
capital_letters_checkbox.pack(anchor=tk.W, expand=True)

# Définition du frame contenant les options de génération du mot de passe (Les spinbox)
small_letters_var = tk.BooleanVar()
small_letters_var.set(True)
small_letters_checkbox = tk.Checkbutton(options_checkboxes_frame, text="Lettres minuscules", font=("Lucida Console", 15), bg="#2f3138", fg="#ffffff", activebackground="#2f3138", activeforeground="#ffffff", selectcolor="#2f3138", highlightthickness=0, bd=0, variable=small_letters_var)
small_letters_checkbox.pack(anchor=tk.W, expand=True)

# Définition du frame contenant les options de génération du mot de passe (Les spinbox)
numbers_var = tk.BooleanVar()
numbers_var.set(True)
numbers_checkbox = tk.Checkbutton(options_checkboxes_frame, text="Chiffres", font=("Lucida Console", 15), bg="#2f3138", fg="#ffffff", activebackground="#2f3138", activeforeground="#ffffff", selectcolor="#2f3138", highlightthickness=0, bd=0, variable=numbers_var)
numbers_checkbox.pack(anchor=tk.W, expand=True)

# Définition du frame contenant les options de génération du mot de passe (Les spinbox)
special_characters_var = tk.BooleanVar()
special_characters_var.set(True)
special_characters_checkbox = tk.Checkbutton(options_checkboxes_frame, text="Caractères spéciaux", font=("Lucida Console", 15), bg="#2f3138", fg="#ffffff", activebackground="#2f3138", activeforeground="#ffffff", selectcolor="#2f3138", highlightthickness=0, bd=0, variable=special_characters_var)
special_characters_checkbox.pack(anchor=tk.W, expand=True, padx=(0, 80))

# Définition du frame contenant la case à cocher "mode sûr"
safe_mode_var = tk.BooleanVar()
safe_mode_var.set(False)
safe_mode_checkbox = tk.Checkbutton(options_checkboxes_frame, text="Mode sûr", font=("Lucida Console", 15), bg="#2f3138", fg="#ffffff", activebackground="#2f3138", activeforeground="#ffffff", selectcolor="#2f3138", highlightthickness=0, bd=0, variable=safe_mode_var)
safe_mode_checkbox.pack(anchor=tk.W, expand=True)

# Les case à cocher (Fin)

# Définition du frame contenant les options de génération du mot de passe (La longueur du mot de passe, À DROITE des case à cocher)
options_length_frame = tk.Frame(options_frame, bg="#2f3138")
options_length_frame.grid(row=0, column=1)

# Définition du frame contenant la longueur du mot de passe
options_length_password_frame = tk.Frame(options_length_frame, bg="#2f3138")
options_length_password_frame.grid(row=0, column=0)

# Définition des widgets (curceur) du frame contenant la longueur du mot de passe
length_password_label = tk.Label(options_length_password_frame, text="Longueur du mot de passe", font=("Lucida Console", 15), bg="#2f3138", fg="#ffffff")
length_password_label.pack(anchor=tk.CENTER, expand=True)

# Définition du frame contenant la longueur du mot de passe
length_password_scale = tk.Scale(options_length_password_frame, from_=1, to=64, orient=tk.HORIZONTAL, bg="#2f3138", fg="#ffffff", activebackground="#2f3138", highlightthickness=0, bd=0, length=200, sliderlength=20, command=update_password)
length_password_scale.pack(anchor=tk.CENTER, expand=True)
length_password_scale.set(25)

# Définition du frame contenant le bouton de génération du mot de passe et de réinitialisation des options (en dessous du frame contenant la longueur du mot de passe et les case à cocher)
options_generate_and_reset_frame = tk.Frame(options_frame, bg="#2f3138" )
options_generate_and_reset_frame.grid(row=1, column=0, columnspan=2, pady=(20, 0))

# Définition du frame contenant le bouton de génération du mot de passe (centre du frame contenant le bouton de génération du mot de passe et de réinitialisation des options)
options_generate_frame = tk.Frame(options_generate_and_reset_frame, bg="#2f3138")
options_generate_frame.grid(row=0, column=0)

# Définition du bouton de génération du mot de passe
generate_button = tk.Button(options_generate_frame, text="Générer", font=("Lucida Console", 15), bg="#afb5d0", fg="#43454f", borderwidth=1, command=check_case, anchor=tk.CENTER)
generate_button.pack(anchor=tk.CENTER, expand=True)
generate_button.bind("<Enter>", on_enter_generate)
generate_button.bind("<Leave>", on_leave_generate)
generate_button.bind("<Button-1>", on_click_generate)

# Définition du frame contenant le bouton de réinitialisation des options (en dessous du bouton de génération du mot de passe)
options_reset_frame = tk.Frame(options_generate_and_reset_frame, bg="#2f3138", pady=10)
options_reset_frame.grid(row=1, column=0)

# Définition du bouton de réinitialisation des options
reset_button = tk.Button(options_reset_frame, text="Réinitialiser", font=("Lucida Console", 15), bg="#afb5d0", fg="#43454f", borderwidth=1, command=reset_password_generator, anchor=tk.CENTER,)
reset_button.pack(anchor=tk.CENTER, expand=True)
reset_button.bind("<Enter>", on_enter_reset)
reset_button.bind("<Leave>", on_leave_reset)
reset_button.bind("<Button-1>", on_click_generate)

window.mainloop()

