# Joël Smith-Gravel  | Compétance 6, Développement d'une application utilitaire  | 2023-04-17 | Générateur de mots de passe | V1.0

# générateur de mots de passe moderne avec ttkbootstrap.

# importation des modules.
import os # Importation de os pour les fonctions du système d'exploitation.
import sys # Importation de sys pour les fonctions du système.
from tkinter import * # Importation de tkinter comme gestionnaire de fenêtres.
import ttkbootstrap as ttk # Importation de ttkbootstrap pour le thème.
from ttkbootstrap import Style # Importation de tkinter.Style pour le thème.
from ttkbootstrap.tooltip import ToolTip # Importation de tkinter.Tooltip pour les infobulles.
from ttkbootstrap.dialogs import Messagebox # Importation de tkinter.dialogs pour les messages d'erreur.
import secrets # Importation de secrets pour la génération des caractères aléatoires.
import pyperclip # Importation de pyperclip pour copier le mot de passe généré dans le presse-papiers.

# Déclaration des variables.
password = "" # Le mot de passe généré est stocké dans cette variable.
password_assembly = "" # La variable qui contient les caractères à utiliser pour générer le mot de passe.
theme_inverse = "light" # Le thème inverse de l'application est stocké dans cette variable.

# Déclaration des fonctions.

# Fonction pour générer le mot de passe.
def generate_password(): # Définition de la fonction generate_password.
    capital_checked = capital_letters_var.get() # On récupère la valeur de la case à cocher des lettres majuscules.
    small_checked = small_letters_var.get() # On récupère la valeur de la case à cocher des lettres minuscules.
    numbers_checked = numbers_var.get() # On récupère la valeur de la case à cocher des nombres.
    symbols_checked = symbols_var.get() # On récupère la valeur de la case à cocher des symboles.
    
    if not (capital_checked or small_checked or numbers_checked or symbols_checked): # Si aucune case n'est cochée, alors on affiche une erreur et on arrête la fonction.
        Messagebox.show_error("Vous devez sélectionner au moins une case !", "Erreur") # Affichage d'une erreur si aucune case n'est cochée.
        return False # Arrêt de la fonction.
    else: 
        
        # Appel la variable globale password_assembly.
        global password_assembly # Appel la variable globale password_assembly.

        # Réinitialisation de la variable password_assembly.
        password_assembly = "" # Réinitialisation de la variable password_assembly.
        
        # définir les caractères à utiliser.
        CAPITAL_LETTRES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Les lettres majuscules.
        SMALL_LETTRES = "abcdefghijklmnopqrstuvwxyz" # Les lettres minuscules.
        NUMBERS = "0123456789" # Les nombres.
        symboles= "!@#$%^&*()_+-=[]{};:,.‘/<>?|"+'''"''' # Les symboles.
        SAFE_SYMBOLS = "!@#$%^*()_+-[]{};:,." # Mode sur : Les symboles qui peuvent poser des problèmes dans les URL sont retirés tels que : ? & = / \ < > et `.
        
        # Définir les caractères à utiliser en fonction des cases cochées.
        
        capital_checked = capital_letters_var.get() # On récupère la valeur de la case à cocher des lettres majuscules.
        small_checked = small_letters_var.get() # On récupère la valeur de la case à cocher des lettres minuscules.
        numbers_checked = numbers_var.get() # On récupère la valeur de la case à cocher des nombres.
        symbols_checked = symbols_var.get() # On récupère la valeur de la case à cocher des symboles.
        safe_mode_checked = safe_mode_var.get() # On récupère la valeur de la case à cocher "Safe mode".
        
        # Définir la longueur du mot de passe.
        password_lenght = length_password_scale.get() # On récupère la longueur du mot de passe en fonction de la valeur de la barre de longueur.
        password_lenght = int(password_lenght) # On convertit la longueur du mot de passe en entier.
        
        # vérifier si la condition "Safe mode" est activée.
        if safe_mode_var.get() == 1: # Si la condition "Safe mode" est activée, alors on utilise les caractères sans les symboles qui peuvent poser des problèmes dans les URL.
            symboles = SAFE_SYMBOLS # On change la variable "symboles" pour utiliser les caractères sans les symboles qui peuvent poser des problèmes dans les URL.
        
        # Définir les caractères à utiliser pour le mot de passe en fonction de la longueur du mot de passe et des cases cochées.
        if capital_checked: # Si la case à cocher des lettres majuscules est cochée, alors on ajoute les "lettres majuscules" à "password_assembly".
            password_assembly += CAPITAL_LETTRES # On ajoute les lettres majuscules à la variable password_assembly
            
        if small_checked: # Si la case à cocher des lettres minuscules est cochée, alors on ajoute les lettres minuscules à "password_assembly".
            password_assembly += SMALL_LETTRES # On ajoute les lettres minuscules à la variable "password_assembly".
        
        if numbers_checked: # Si la case à cocher des nombres est cochée, alors on ajoute les nombres à "password_assembly".
            #numbers_used = True # On change la valeur de la variable "numbers_used" à True.
            password_assembly += NUMBERS # On ajoute les nombres à la variable "password_assembly",
            
        # Si la case à cocher des symboles est cochée, alors on ajoute les symboles à "password_assembly". mais Si la case à cocher "Safe mode" est cochée alors on ajoute les symboles sans les symboles qui peuvent poser problème dans les URL à "password_assembly".
        if safe_mode_checked and symbols_checked:
            password_assembly += SAFE_SYMBOLS # On ajoute les symboles sans les symboles qui peuvent poser problème dans les URL à la variable password_assembly
        elif symbols_checked:
            password_assembly += symboles # On ajoute les symboles à la variable password_assembly
            
        # Update password fin.
        
        # On réinitialise la variable "password" et "password_lenght".
        password = "" # On réinitialise la variable password.
        password_lenght = length_password_scale.get() # On récupère la longueur du mot de passe en fonction de la valeur de la barre de longueur.
        password_lenght = int(password_lenght) # On convertit la longueur du mot de passe en entier.
        
        # On récupère les caractères à utiliser.
        password = "" # On réinitialise la variable "password".
        password_lenght = length_password_scale.get() # On récupère la longueur du mot de passe en fonction de la valeur de la barre de longueur.
        password_lenght = int(password_lenght) # On convertit la longueur du mot de passe en entier.
        
        # On récupère les caractères à utiliser pour le mot de passe en fonction de la longueur du mot de passe et des cases cochées.
        for i in range(password_lenght): # On répète la boucle autant de fois que la longueur du mot de passe en utilisant la variable i pour compter le nombre de répétitions.
            password += secrets.choice(password_assembly) # On ajoute un caractère aléatoire à la variable password.
            password_var.set(password)  # On met à jour la variable de mot de passe pour l'affichage.

# Fonction pour réinitialiser le générateur de mot de passe.
def reset_password_generator():
    global password_assembly # Appelle la variable globale "password_assembly".
    global password_var # Appelle la variable globale "password_var".
    global capital_letters_var # Appelle la variable globale "capital_letters_var".
    global small_letters_var # Appelle la variable globale "small_letters_var".
    global numbers_var # Appelle la variable globale "numbers_va"r.
    global symbols_var # Appelle la variable globale "symbols_var".
    global safe_mode_var # Appelle la variable globale "safe_mode_var".
    password_assembly = "" # On réinitialise la variable "password_assembly".
    password_var.set("") # On réinitialise la variable de mot de passe pour l'affichage.
    capital_letters_var.set(True) # On réinitialise la variable "capital_letters_var".
    small_letters_var.set(True) # On réinitialise la variable "small_letters_var".
    numbers_var.set(True) # On réinitialise la variable "numbers_var".
    symbols_var.set(True) # On réinitialise la variable "symbols_var".
    safe_mode_var.set(False) # On réinitialise la variable "safe_mode_var".
    length_password_scale.set(25) # On réinitialise la valeur de la barre de longueur à "25".
    
# Fonction pour changer le thème.
def change_theme():
    global style # Appelle la variable globale "style".
    global theme_inverse # Appelle la variable globale "theme_inverse".
    global theme_button # Appelle la variable globale "theme_button".
    global theme_button_frame # Appelle la variable globale "theme_button_frame".
    global button_frame # Appelle la variable globale "button_frame".
    if style.theme_use() == "darkly": # Si le thème utilisé est "darkly", alors on change le thème pour "lightly".
        theme_button.pack_forget() # On supprime le bouton de changement de thème.
        style_config_fonction() # On configure le style.
        style.theme_use("lumen") # On change le thème pour "lumen".
        style.configure(".", font=("Lucida Console", 10)) # On change la police de caractère pour "lumen".
        theme_inverse = "dark" # On change la valeur de la variable "theme_inverse" à dark
        theme_button = ttk.Button(theme_button_frame, text=theme_inverse, command=change_theme, style="costum.TButton.dark") # On crée le bouton de changement de thème.
        theme_button_frame.grid_propagate(0) # Empêche le frame de se redimensionner.
        theme_button_frame.grid(row=2, column=2, padx=(50, 0), pady=10, sticky="e") # On place le frame du bouton de changement de thème.
        theme_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2) # On place le bouton de changement de thème.
        theme_button_frame.columnconfigure(0, weight=1) # Empêche le frame de se redimensionner en largeur.
        theme_button_frame.rowconfigure(0, weight=1) # Empêche le frame de se redimensionner en hauteur.
    else: # Sinon on change le thème pour "darkly".
        theme_button.pack_forget() # On supprime le bouton de changement de thème.
        style_config_fonction() # On configure le style.
        style.theme_use("darkly") # On change le thème pour "darkly".
        theme_inverse = "light" # On change la valeur de la variable "theme_inverse" à "light"
        theme_button = ttk.Button(theme_button_frame, text=theme_inverse, command=change_theme, style="costum.TButton.light") # On crée le bouton de changement de thème.
        theme_button_frame.grid_propagate(0) # Empêche le frame de se redimensionner.
        theme_button_frame.grid(row=2, column=2, padx=(50, 0), pady=10, sticky="e") # On place le frame du bouton de changement de thème.
        theme_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2) # On place le bouton de changement de thème.
        theme_button_frame.columnconfigure(0, weight=1) # Empêche le frame de se redimensionner en largeur.
        theme_button_frame.rowconfigure(0, weight=1) # Empêche le frame de se redimensionner en hauteur.
    
def style_config_fonction(): # Fonction pour configurer le style.
    global style # Appelle la variable globale style.
    global theme_inverse # Appelle la variable globale theme_inverse.
    global theme_button # Appelle la variable globale theme_button.
    global theme_button_frame # Appelle la variable globale theme_button_frame.
    global button_frame # Appelle la variable globale button_frame.
    # Style de la fenêtre
    style.configure("costum.TLabel", font=("Lucida Console", 12)) # On définit la police pour les labels.
    style.configure("costum.TButton", font=("Lucida Console", 12)) # On définit la police pour les boutons.
    #style.configure("costum.TCheckbutton", font=("Lucida Console", 10)) # On définit la police pour les cases à cocher.
    style.configure(".", font=("Lucida Console", 10)) # On définit la police pour les autres widgets.
    style.configure("costum.TLabelframe", font=("Lucida Console", 20)) # On définit la police pour les frames.


# Définitions des fonctions pour metre à jour la "scale" avec le "spinbox".

# Fonction pour mettre à jour la valeur de la "spinbox" quand on change la valeur de la "scale".
def on_scale_value_changed(val): # val est la valeur de la scale.
    lenght_password_var.set(int(float(val))) # On met à jour la valeur de la spinbox avec la valeur de la scale.
    
# Fonction pour mettre à jour la valeur de la scale quand on change la valeur de la spinbox.
def on_spinbox_value_changed(*args): # *args permet de prendre en compte les arguments de la fonction pour le gestionnaire d'événements grphique.
    if length_password_spinbox.get() != "": # Si la valeur de la spinbox n'est pas vide.
        value = lenght_password_var.get() # On récupère la valeur de la spinbox et on la met dans la variable value.
        length_password_scale.set(value) # On met à jour la valeur de la scale avec la valeur de la spinbox.
        
# Fonction pour vérifier si la valeur entrée dans le spinbox est un nombre entier
def is_integer(value_if_allowed): # value_if_allowed est la valeur entrée dans le spinbox
    if value_if_allowed == "": # Si la valeur entrée dans le spinbox est vide alors on arrete la fonction.
        return True # On retourne True
    try:    # Sinon on
        int(value_if_allowed) # On essaie de convertir la valeur entrée dans le spinbox en nombre entier
        return True # Si la conversion est possible alors on retourne "True".
    except ValueError: # Sinon on...
        return False # On retourne False

# Fonction pour obtenir le chemin absolu pour l'icône du programme.
def resource_path(): # Fonction pour récupérer le chemin absolu du fichier.
    if getattr(sys, 'frozen', False): # Si le programme est exécuté en tant qu'application.
        current_dir = sys._MEIPASS # On récupère le chemin absolu du fichier.
    else: # Sinon, le programme est exécuté en tant que script Python.
        current_dir = os.path.dirname(os.path.abspath(__file__)) # On récupère le chemin absolu du fichier.
    icon_path = os.path.join(current_dir, "icon.ico") # On récupère le chemin absolu de l'icône et on assemble le chemin absolu du fichier avec le chemin absolu de l'icône.
    return icon_path # On retourne le chemin absolu de l'icône pour qu'il soit stocké dans la variable "icon_path".
        
# création de la fenêtre principale.

window = Tk() # On crée une fenêtre avec le thème personnalisé.
style = ttk.Style() # On crée un style pour la fenêtre avec le thème personnalisé.
style.theme_use('darkly') # On définit le thème de la fenêtre à darkly (par défaut).
window.title("Générateur de mot de passe") # On définit le titre de la fenêtre.
WINDOW_WIDTH = 800 # On définit la largeur de la fenêtre.
WINDOW_HEIGHT = 505 # On définit la hauteur de la fenêtre.
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}") # On définit la taille de la fenêtre en fonction des variables "WINDOW_WIDTH" et "WINDOW_HEIGHT"
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT) # On définit la taille minimum de la fenêtre en fonction des variables "WINDOW_WIDTH" et "WINDOW_HEIGHT"
window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)   # On définit la taille maximum de la fenêtre en fonction des variables "WINDOW_WIDTH" et "WINDOW_HEIGHT"
window.attributes("-fullscreen", False) # On interdit le plein écran.
window.resizable(False, False) # On interdit le redimensionnement de la fenêtre.
style_config_fonction() # On configure le style.

# Application de l'icône de la fenêtre.
icon_path = resource_path() # On récupère le chemin du fichier de l'icône. On utilise la fonction "resource_path()" pour que le programme fonctionne dans un fichier .exe.
window.iconbitmap(icon_path) # On applique l'icône à la fenêtre. On utilise iconbitmap() car le fichier est au format .ico.

# Définition des variables tkinter.
lenght_password_var = ttk.IntVar() # On crée une variable pour la longueur du mot de passe
validate_integer = window.register(is_integer) # On crée une variable pour valider si la valeur entrée dans le spinbox est un entier

# création de la variable de mot de passe.
password_var = ttk.StringVar() # La variable du mot de passe est stockée dans cette variable pour l'affichage.
password_var.set(password) # La variable du mot de passe est initialisée avec la valeur de la variable du mot de passe.

# création du GUI.
# création du frame principal.
main_frame = ttk.Frame(window, padding=10) # On crée un frame principal pour pouvoir placer les autres frames.
main_frame.pack(anchor="n", expand=True) # On place le frame principal en haut de la fenêtre.

# Définition du frame du label.
title_frame = ttk.Frame(main_frame, padding=10) # On crée un frame pour le label.
title_frame.pack(anchor="n", expand=True) # On place le frame en haut de la fenêtre.

# Définition du frame contenant le label.
label = ttk.Label(title_frame, text="Générateur de mot de passe", font=("Lucida Console", 20, "bold"))  # On crée un label pour le titre.
label.pack(anchor="center", expand=True) # On place le label au centre du frame "main_frame".

# Définition du frame contenant le mot de passe et le bouton de copie.
password_and_copy_frame = ttk.Frame(main_frame, padding=10) # On crée un frame pour le mot de passe et le bouton de copie.
password_and_copy_frame.pack(anchor="n", expand=True) # On place le frame en haut de la fenêtre en dessous du label.

# Définition du frame contenant le mot de passe.
password_frame = ttk.Frame(password_and_copy_frame, padding=10) # On crée un frame pour le mot de passe.
password_frame.grid(row=0, column=0) # On place le frame à gauche du frame contenant le bouton de copie.

# Définition du widget contenant le mot de passe.
entry = ttk.Entry(password_frame, textvariable=password_var, font=("Lucida Console", 18), width=40, state="normal") # On crée un entry pour le mot de passe.
entry.pack(anchor="w", expand=True) # On place le entry à gauche du frame.

# Définition du frame contenant le bouton de copie.
copy_frame = ttk.Frame(password_and_copy_frame, padding=10) # On crée un frame pour le bouton de copie.
copy_frame.grid(row=0, column=1) # On place le frame à droite du frame contenant le mot de passe.


# Définition du widget contenant le bouton de copie.

copy_button = ttk.Button(copy_frame, text="Copier", command=lambda: pyperclip.copy(password_var.get()), style="costum.TButton") # On crée un bouton pour copier le mot de passe.
copy_button.pack(anchor="center", expand=True) # On place le bouton au centre du frame.

# Définition du frame contenant les options de génération de mot de passe.
option_frame = ttk.Labelframe(main_frame, text="Personnalisation", padding=10) # On crée un frame pour les options de génération du mot de passe.
option_frame.pack(anchor="n", expand=True) # On place le frame en haut de la fenêtre en dessous du frame contenant le mot de passe et le bouton de copie.

# Définition du frame contenant les options de génération de mot de passe (case à cocher).
option_check_frame = ttk.Frame(option_frame, padding=10) # On crée un frame pour les options de génération de mot de passe (case à cocher).
option_check_frame.grid(row=0, column=0, sticky="w", padx=(40, 150)) # On place le frame à gauche du frame contenant le spinbox et la scale.

# les cases à cocher.
# case à cocher pour les majuscules.
capital_letters_var = BooleanVar() # On crée une variable pour la case à cocher des majuscules.
capital_letters_var.set(True) # On initialise la variable à "True" (par défaut).
capital_letters_checkbox = ttk.Checkbutton(option_check_frame, text="Lettres majuscules", variable=capital_letters_var, style="round-toggle") # On crée une case à cocher pour les majuscules.
capital_letters_checkbox.pack(anchor="w", expand=True, pady=5) # On place la case à cocher à gauche dans le frame. 

# case à cocher pour les minuscules.
small_letters_var = BooleanVar() # On crée une variable pour la case à cocher des minuscules.
small_letters_var.set(True) # On initialise la variable à True (par défaut).
small_letters_checkbox = ttk.Checkbutton(option_check_frame, text="Lettres minuscules", variable=small_letters_var, style="round-toggle") # On crée une case à cocher pour les minuscules.
small_letters_checkbox.pack(anchor="w", expand=True, pady=5) # On place la case à cocher à gauche dans le frame.

# case à cocher pour les chiffres.
numbers_var = BooleanVar() # On crée une variable pour la case à cocher des chiffres.
numbers_var.set(True) # On initialise la variable à ""True" (par défaut).
numbers_checkbox = ttk.Checkbutton(option_check_frame, text="Chiffres", variable=numbers_var, style="round-toggle") # On crée une case à cocher pour les chiffres.
numbers_checkbox.pack(anchor="w", expand=True, pady=5) # On place la case à cocher à gauche dans le frame.

# case à cocher pour les symboles.
symbols_var = BooleanVar() # On crée une variable pour la case à cocher des symboles.
symbols_var.set(True) # On initialise la variable à "True" (par défaut).
symbols_checkbox = ttk.Checkbutton(option_check_frame, text="Symboles", variable=symbols_var, style="round-toggle") # On crée une case à cocher pour les symboles.
symbols_checkbox.pack(anchor="w", expand=True, pady=5) # On place la case à cocher à gauche dans le frame.

# case à cocher pour le mode sécurisé.
safe_mode_var = BooleanVar() # On crée une variable pour la case à cocher du mode sécurisé.
safe_mode_var.set(False) # On initialise la variable à "False" (par défaut)
safe_mode_checkbox = ttk.Checkbutton(option_check_frame, text="Mode sécurisé", variable=safe_mode_var, style="warning-round-toggle") # On crée une case à cocher pour le mode sécurisé avec un style différent "warning-round-toggle".
safe_mode_checkbox.pack(anchor="w", expand=True, pady=15) # On place la case à cocher à gauche dans le frame.
tooltip = ToolTip(safe_mode_checkbox, "Le mode sécurisé permet de générer un mot de passe sans symboles pouvant poser problème dans certains cas (par exemple, dans un terminal ou dans un navigateur web).", bootstyle="warning.costum.TToolTip") # On crée un tooltip pour la case à cocher du mode sécurisé. ce qui permet d'expliquer ce que fait le mode sécurisé.

# les cases à cocher fin.
# Définition du frame contenant les options de génération de mot de passe (barre de longueur à droite des cases à cocher).
option_length_frame = ttk.Frame(option_frame) # On crée un frame pour les options de génération de mot de passe (scale et spinbox).
option_length_frame.grid(row=0, column=1) # On place le frame à droite du frame contenant les cases à cocher.

# Définition du frame contenant la barre de longueur.
options_length_bar_frame = ttk.Frame(option_length_frame) # On crée un frame pour la barre de longueur.
options_length_bar_frame.grid(row=0, column=0, sticky="e", padx=(0, 50)) # On place le frame à droite du frame contenant les cases à cocher.

# Définition du label de la barre de longueur.
lenght_password_label = ttk.Label(options_length_bar_frame, text="Longueur du mot de passe", style="costum.TLabel") # On crée un label pour la barre de longueur.
lenght_password_label.pack(anchor="n", expand=True, pady=10) # On place le label en haut du frame contenant la barre de longueur et le spinbox.

# frame pour la barre de longueur et le label de la valeur.
length_password_frame = ttk.Frame(options_length_bar_frame) # On crée un frame pour la barre de longueur et le spinbox de façon à pouvoir les placer cote à cote.
length_password_frame.pack(anchor="n", expand=True, pady=10) # On place le frame juste en dessous du label.

# Définition de la barre de longueur.
length_password_scale = ttk.IntVar() # On crée une variable pour la barre de longueur.
length_password_scale = ttk.Scale(length_password_frame, from_=1, to=64, orient=HORIZONTAL, command=on_scale_value_changed, length=200) # On crée la barre de longueur.
length_password_scale.grid(row=1, column=1, pady=10) # On place la barre de longueur à droite du spinbox.
length_password_scale.set(25) # On initialise la barre de longueur à 25 (par défaut).

# Définition du spinbox de la barre de longueur.
length_password_spinbox = Spinbox(length_password_frame, from_=1, to=64, textvariable=lenght_password_var, width=3, validate="key", validatecommand=(validate_integer, "%P")) # On crée le spinbox lié à la barre de longueur (scale).
length_password_spinbox.grid(row=1, column=0, pady=10, padx=(0, 10)) # On place le spinbox à gauche de la barre de longueur.
lenght_password_var.trace_add("write", on_spinbox_value_changed) # trace la variable pour mettre à jour la barre de longueur quand la valeur est modifiée comme dans le cas ou l'utilisateur saisit une valeur dans le spinbox.

# Définition du frame contenant le bouton de génération, le bouton de réinitialisation et le bouton permettant de changer le thème.
button_frame = ttk.Frame(main_frame, padding=10) # On crée un frame pour les boutons.
button_frame.pack(anchor="n", expand=True) # On place le frame en bas du frame de personnalisation dans la fenêtre principale.

# frame padding.
button_frame_padding = ttk.Frame(button_frame, padding=166) # On crée un frame pour le padding du frame contenant les boutons.
button_frame_padding.grid(row=0, column=0, sticky="w", padx=(266, 0)) # On place le frame à gauche du frame contenant les boutons.

# Définition du bouton de génération.
generate_button = ttk.Button(button_frame, text="Générer", command=generate_password) # On crée un bouton pour générer un mot de passe.
generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew") # On place le bouton en haut au centre dans le frame contenant les boutons.

# Définition du bouton de réinitialisation.
reset_button = ttk.Button(button_frame, text="Réinitialiser", command=reset_password_generator) # On crée un bouton pour réinitialiser les options de génération de mot de passe.
reset_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew") # On place le bouton en bas au centre dans le frame contenant les boutons.

# Créez un frame pour le bouton avec une taille fixe.
theme_button_frame = ttk.Labelframe(button_frame, width=217, height=40, text="Changer de thème : ", style="costum.TLabelframe") # On crée un frame pour le bouton de changement de thème.
theme_button_frame.grid_propagate(0) # Empêche le frame de se redimensionner.
theme_button_frame.grid(row=2, column=2, padx=(50, 0), pady=10, sticky="e") # On place le frame à droite du frame contenant les boutons.

# Définition du bouton de changement de thème.
theme_button = ttk.Button(theme_button_frame, text= theme_inverse, command=change_theme, style="costum.TButton.light") # On crée un bouton pour changer de thème.
theme_button.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)  # On place le bouton dans le frame contenant le bouton de changement de thème.
theme_button_frame.columnconfigure(0, weight=1) # Empêche le bouton de se redimensionner en largeur.
theme_button_frame.rowconfigure(0, weight=1) # Empêche le bouton de se redimensionner en hauteur.


# démarage de la boucle principale pour la fenêtre tkinter.
window.mainloop() # On lance la boucle principale de la fenêtre tkinter.