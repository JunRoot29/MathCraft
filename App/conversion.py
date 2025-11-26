import math
from tkinter import *
from tkinter import ttk
import sys
import os
sys.path.append(os.path.dirname(__file__))

# Palette unifiée (identique à polynome.py)
PALETTE = {
    "fond_principal": "#F0F4F8",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6", 
    "erreur": "#DC2626",
    "texte_fonce": "#1E40AF",
    "texte_clair": "#1E40AF"
}

"""================================Dictionnaire des conversions====================================="""

# Dictionnaire de conversion des unités de longueur
unit_to_meter = {
    "Kilomètre": 1000,
    "Mètre": 1,
    "Centimètre": 0.01,
    "Décamètre": 0.1,
    "Millimètre": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Pieds": 0.3048,
    "Pouces": 0.0254
}

# Dictionnaire de conversion des unités de Température
unit_to_temperature = {
    "Dégrés (°C)": "celsius",
    "Fahrenheit (°F)": "fahrenheit", 
    "Kelvin (°K)": "kelvin",
    "Rankine (°R)": "rankine"
}

## Dictionnaire de conversion des unités de masse et poids
unit_to_masse_et_poids = {
    "Tonne": 1000000,
    "Quintal": 100000,
    "Kilogramme": 1000,
    "Gramme": 1,
    "Milligramme": 0.001,
    "Microgramme": 0.000001,
    "Livre": 453.6,
    "Once": 28.3495,
    "Stone": 6350.29,
    "Carat": 0.2
}

## Dictionnaire de conversion des unités de vitesse
unit_to_vitesse = {
    "Mètre par seconde": 1,
    "Kilomètre par heure": 0.2778,
    "Kilomètre par seconde": 1000,
    "Centimètre par seconde": 0.01,
    "Millimètre par seconde": 0.001,
    "Mile par heure": 0.44704,
    "Mile par seconde": 1609.34,
    "Noeud (nautique )": 0.5144,
    "Mach (vitesse du son à 20°C)": 343,  # à 20°C dans l'air
    "Pied par seconde": 0.3048,
    "Pouce par seconde": 0.0254
}

# Dictionnaire de conversion des angles
unit_to_angles = {
    "Radian": 1,
    "Degré": 0.0174533,         # π / 180
    "Grade (Gon)": 0.0157079,   # π / 200
    "Minute d'arc": 0.0002909,  # π / (180 × 60)
    "Seconde d'arc": 0.00000485,# π / (180 × 3600)
    "Milliradian": 0.001,
    "Microradian": 0.000001
}

"""=========================Les fonctions de Conversion============================="""

# Fonction de conversion de Longueur
def convertir_longueur(valeur, unite_depart, unite_arrivee):
    try:
        valeur = float(valeur)
        en_metre = valeur * unit_to_meter[unite_depart]
        resultat = en_metre / unit_to_meter[unite_arrivee]
        return f"✅{round(resultat, 4)}"
    except Exception as e:
        return f"❌Erreur, Vérifiez la saisie avant conversion"
    
# Fonction de conversion de Température
def convertir_temperature(valeur, unite_depart, unite_arrivee):
    try:
        valeur = float(valeur)
        
        # Conversion vers Celsius d'abord
        if unite_depart == "Dégrés (°C)":
            celsius = valeur
        elif unite_depart == "Fahrenheit (°F)":
            celsius = (valeur - 32) * 5/9
        elif unite_depart == "Kelvin (°K)":
            celsius = valeur - 273.15
        elif unite_depart == "Rankine (°R)":
            celsius = (valeur - 491.67) * 5/9
        else:
            return "❌Unité de départ non supportée"
        
        # Conversion de Celsius vers l'unité d'arrivée
        if unite_arrivee == "Dégrés (°C)":
            resultat = celsius
        elif unite_arrivee == "Fahrenheit (°F)":
            resultat = (celsius * 9/5) + 32
        elif unite_arrivee == "Kelvin (°K)":
            resultat = celsius + 273.15
        elif unite_arrivee == "Rankine (°R)":
            resultat = (celsius + 273.15) * 9/5
        else:
            return "❌Unité d'arrivée non supportée"
        
        return f"✅{round(resultat, 4)}"
        
    except Exception as e:
        return f"❌Erreur, Vérifiez la saisie avant conversion"

# Fonction de conversion de Masse et Poids
def convertir_masse_et_poids(valeur, unite_depart, unite_arrivee):
    try:
        valeur = float(valeur)
        en_gramme = valeur * unit_to_masse_et_poids[unite_depart]
        resultat = en_gramme / unit_to_masse_et_poids[unite_arrivee]
        return f"✅{round(resultat, 4)}"
    except Exception as e:
        return f"❌Erreur, Vérifiez la saisie avant conversion"

# Fonction de conversion de Vitesse
def convertir_vitesse(valeur, unite_depart, unite_arrivee):
    try:
        valeur = float(valeur)
        en_gramme = valeur * unit_to_vitesse[unite_depart]
        resultat = en_gramme / unit_to_vitesse[unite_arrivee]
        return f"✅{round(resultat, 4)}"
    except Exception as e:
        return f"❌Erreur, Vérifiez la saisie avant conversion"

# Fonction de conversion des angles
def convertir_angles(valeur, unite_depart, unite_arrivee):
    try:
        valeur = float(valeur)
        en_gramme = valeur * unit_to_angles[unite_depart]
        resultat = en_gramme / unit_to_angles[unite_arrivee]
        return f"✅{round(resultat, 4)}"
    except Exception as e:
        return f"❌Erreur, Vérifiez la saisie avant conversion"

"""===================================================================================="""
# Style global pour les boutons arrondis
def configurer_style():
    style = ttk.Style()
    style.configure("Custom.TButton",
                    foreground="#FFFFFF",
                    background=PALETTE["secondaire"],  # Utilisation de la palette
                    font=("Century Gothic", 14),
                    padding=15,
                    relief="flat",
                    width=40)
    
    # Style spécial pour le bouton Quitter
    style.configure("Quit.TButton",
                    foreground="#FFFFFF",
                    background=PALETTE["erreur"],  # Utilisation de la palette
                    font=("Century Gothic", 14),
                    padding=15,
                    relief="flat",
                    width=40)
    return style

def launch_conversion(parent=None):
    conversion = Toplevel(parent)
    conversion.title("Conversion")
    conversion.geometry("600x700")
    conversion.configure(bg=PALETTE["fond_principal"])  # Utilisation de la palette

    Label(conversion, text="Conversion", font=("Century Gothic", 24, "bold"), 
          bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
    Label(conversion, text="Et si on s'amusait à convertir ? \n Choisi ton Opération!", 
          font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()

    options = ["Longueur 📏", "Masse et Poids 🏋️", "Température🌡️", "Vitesse 🏃🏾", "Angles 📐", "Données 🖲️"]
    combo = ttk.Combobox(conversion, values=options, font=("Century Gothic", 14), state="readonly")
    combo.set("Longueur 📏")
    combo.pack()

    champ_valeur_var = StringVar()

    def ajouter_texte(valeur):
        champ_valeur_var.set(champ_valeur_var.get() + valeur)

    def selection(event):
        choix = combo.get()
        try:
            if choix == "Longueur 📏":
                lancer_longueur()
            elif choix == "Température🌡️":
                lancer_temperature()
            elif choix == "Vitesse 🏃🏾":
                lancer_vitesse()
            elif choix == "Angles 📐":
                lancer_angles()
            elif choix == "Données 🖲️":
                lancer_donnees()
            elif choix == "Masse et Poids 🏋️":
                lancer_masse_poids()
            else:
                raise ValueError(f"Option inconnue : {choix}")
        except Exception as e:
            print(f"Erreur lors de la sélection : {e}")

    combo.bind("<<ComboboxSelected>>", selection)

    def lancer_longueur():
        for widget in conversion.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()

        cadre_longueur = Frame(conversion, bg=PALETTE["fond_principal"])
        cadre_longueur.pack(pady=10)

        Label(cadre_longueur, text="Valeur à convertir :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        champ_valeur = Entry(cadre_longueur, font=("Century Gothic", 14), textvariable=champ_valeur_var)
        champ_valeur.pack()

        Label(cadre_longueur, text="De :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_depart = ttk.Combobox(cadre_longueur, values=list(unit_to_meter.keys()), 
                                   font=("Century Gothic", 12), state="readonly")
        unite_depart.set("Mètre")
        unite_depart.pack()

        Label(cadre_longueur, text="Vers :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_arrivee = ttk.Combobox(cadre_longueur, values=list(unit_to_meter.keys()), 
                                    font=("Century Gothic", 12), state="readonly")
        unite_arrivee.set("Kilomètre")
        unite_arrivee.pack()

        champ_resultat = Label(cadre_longueur, text="", font=("Century Gothic", 14), 
                              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        champ_resultat.pack(pady=10)

        def calculer():
            val = champ_valeur.get()
            u1 = unite_depart.get()
            u2 = unite_arrivee.get()
            res = convertir_longueur(val, u1, u2)
            if "✅" in res:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["primaire"])
            else:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["erreur"])

        bouton_convertir = ttk.Button(cadre_longueur, text="Convertir", style="Custom.TButton", command=calculer)
        bouton_convertir.pack(pady=5)

        # Bouton Quitter
        bouton_quitter = ttk.Button(cadre_longueur, text="Quitter", style="Quit.TButton", command=conversion.destroy)
        bouton_quitter.pack(pady=10)

    def lancer_vitesse():
        for widget in conversion.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()

        cadre_vitesse = Frame(conversion, bg=PALETTE["fond_principal"])
        cadre_vitesse.pack(pady=10)

        Label(cadre_vitesse, text="Valeur à convertir :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        champ_valeur = Entry(cadre_vitesse, font=("Century Gothic", 14), textvariable=champ_valeur_var)
        champ_valeur.pack()

        Label(cadre_vitesse, text="De :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_depart = ttk.Combobox(cadre_vitesse, values=list(unit_to_vitesse.keys()), 
                                   font=("Century Gothic", 12), state="readonly")
        unite_depart.set("Kilomètre par heure")
        unite_depart.pack()

        Label(cadre_vitesse, text="Vers :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_arrivee = ttk.Combobox(cadre_vitesse, values=list(unit_to_vitesse.keys()), 
                                    font=("Century Gothic", 12), state="readonly")
        unite_arrivee.set("Kilomètre par seconde")
        unite_arrivee.pack()

        champ_resultat = Label(cadre_vitesse, text="", font=("Century Gothic", 14), 
                              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        champ_resultat.pack(pady=10)

        def calculer():
            val = champ_valeur.get()
            u1 = unite_depart.get()
            u2 = unite_arrivee.get()
            res = convertir_vitesse(val, u1, u2)
            if "✅" in res:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["primaire"])
            else:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["erreur"])

        bouton_convertir = ttk.Button(cadre_vitesse, text="Convertir", style="Custom.TButton", command=calculer)
        bouton_convertir.pack(pady=5)

        # Bouton Quitter
        bouton_quitter = ttk.Button(cadre_vitesse, text="Quitter", style="Quit.TButton", command=conversion.destroy)
        bouton_quitter.pack(pady=10)

    def lancer_donnees():
        for widget in conversion.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()

        cadre_donnees = Frame(conversion, bg=PALETTE["fond_principal"])
        cadre_donnees.pack(pady=10)

        Label(cadre_donnees, text="Module Données - En développement", 
              font=("Century Gothic", 16), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=20)
        Label(cadre_donnees, text="Cette fonctionnalité sera disponible prochainement", 
              font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=10)

        # Bouton Quitter
        bouton_quitter = ttk.Button(cadre_donnees, text="Quitter", style="Quit.TButton", command=conversion.destroy)
        bouton_quitter.pack(pady=20)

    def lancer_masse_poids():
        for widget in conversion.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()

        cadre_masse = Frame(conversion, bg=PALETTE["fond_principal"])
        cadre_masse.pack(pady=10)

        Label(cadre_masse, text="Valeur à convertir :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        champ_valeur = Entry(cadre_masse, font=("Century Gothic", 14), textvariable=champ_valeur_var)
        champ_valeur.pack()

        Label(cadre_masse, text="De :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_depart = ttk.Combobox(cadre_masse, values=list(unit_to_masse_et_poids.keys()), 
                                   font=("Century Gothic", 12), state="readonly")
        unite_depart.set("Gramme")
        unite_depart.pack()

        Label(cadre_masse, text="Vers :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_arrivee = ttk.Combobox(cadre_masse, values=list(unit_to_masse_et_poids.keys()), 
                                    font=("Century Gothic", 12), state="readonly")
        unite_arrivee.set("Kilogramme")
        unite_arrivee.pack()

        champ_resultat = Label(cadre_masse, text="", font=("Century Gothic", 14), 
                              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        champ_resultat.pack(pady=10)

        def calculer():
            val = champ_valeur.get()
            u1 = unite_depart.get()
            u2 = unite_arrivee.get()
            res = convertir_masse_et_poids(val, u1, u2)
            if "✅" in res:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["primaire"])
            else:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["erreur"])

        bouton_convertir = ttk.Button(cadre_masse, text="Convertir", style="Custom.TButton", command=calculer)
        bouton_convertir.pack(pady=5)

        # Bouton Quitter
        bouton_quitter = ttk.Button(cadre_masse, text="Quitter", style="Quit.TButton", command=conversion.destroy)
        bouton_quitter.pack(pady=10)

    def lancer_temperature():
        for widget in conversion.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()
        
        cadre_temperature = Frame(conversion, bg=PALETTE["fond_principal"])
        cadre_temperature.pack(pady=10)

        Label(cadre_temperature, text="Valeur à convertir :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        champ_valeur = Entry(cadre_temperature, font=("Century Gothic", 14), textvariable=champ_valeur_var)
        champ_valeur.pack()

        Label(cadre_temperature, text="De :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_depart = ttk.Combobox(cadre_temperature, values=list(unit_to_temperature.keys()), 
                                   font=("Century Gothic", 12), state="readonly")
        unite_depart.set("Dégrés (°C)")
        unite_depart.pack()

        Label(cadre_temperature, text="Vers :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_arrivee = ttk.Combobox(cadre_temperature, values=list(unit_to_temperature.keys()), 
                                    font=("Century Gothic", 12), state="readonly")
        unite_arrivee.set("Fahrenheit (°F)")
        unite_arrivee.pack()

        champ_resultat = Label(cadre_temperature, text="", font=("Century Gothic", 14), 
                              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        champ_resultat.pack(pady=10)

        def calculer():
            val = champ_valeur.get()
            u1 = unite_depart.get()
            u2 = unite_arrivee.get()
            res = convertir_temperature(val, u1, u2)
            if "✅" in res:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["primaire"])
            else:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["erreur"])

        bouton_convertir = ttk.Button(cadre_temperature, text="Convertir", style="Custom.TButton", command=calculer)
        bouton_convertir.pack(pady=5)

        # Bouton Quitter
        bouton_quitter = ttk.Button(cadre_temperature, text="Quitter", style="Quit.TButton", command=conversion.destroy)
        bouton_quitter.pack(pady=10)

    def lancer_angles():
        for widget in conversion.winfo_children():
            if isinstance(widget, Frame):
                widget.destroy()

        cadre_angles = Frame(conversion, bg=PALETTE["fond_principal"])
        cadre_angles.pack(pady=10)

        Label(cadre_angles, text="Valeur à convertir :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        champ_valeur = Entry(cadre_angles, font=("Century Gothic", 14), textvariable=champ_valeur_var)
        champ_valeur.pack()

        Label(cadre_angles, text="De :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_depart = ttk.Combobox(cadre_angles, values=list(unit_to_angles.keys()), 
                                   font=("Century Gothic", 12), state="readonly")
        unite_depart.set("Radian")
        unite_depart.pack()

        Label(cadre_angles, text="Vers :", font=("Century Gothic", 14), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
        unite_arrivee = ttk.Combobox(cadre_angles, values=list(unit_to_angles.keys()), 
                                    font=("Century Gothic", 12), state="readonly")
        unite_arrivee.set("Degré")
        unite_arrivee.pack()

        champ_resultat = Label(cadre_angles, text="", font=("Century Gothic", 14), 
                              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        champ_resultat.pack(pady=10)

        def calculer():
            val = champ_valeur.get()
            u1 = unite_depart.get()
            u2 = unite_arrivee.get()
            res = convertir_angles(val, u1, u2)
            if "✅" in res:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["primaire"])
            else:
                champ_resultat.config(text=f"Résultat : {res} {u2}", fg=PALETTE["erreur"])

        bouton_convertir = ttk.Button(cadre_angles, text="Convertir", style="Custom.TButton", command=calculer)
        bouton_convertir.pack(pady=5)

        # Bouton Quitter
        bouton_quitter = ttk.Button(cadre_angles, text="Quitter", style="Quit.TButton", command=conversion.destroy)
        bouton_quitter.pack(pady=10)