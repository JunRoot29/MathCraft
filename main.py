from tkinter import *
from tkinter import ttk
from App import polynome as poly
from App import operation_de_base as op
from App import theorie_des_nombres as theorie
from App import conversion as conv
from App import chaine_de_caractere as ch
from App import integration_numerique as int_num
from App.interface_historique import InterfaceHistorique  
from App import explorateur_concepts as exp_concepts
from App.soutient_manager import afficher_soutien

# Fonctions pour le menu Aide
def afficher_guides():
    """Afficher les guides d'utilisation"""
    from tkinter import messagebox
    messagebox.showinfo(
        "Guides d'utilisation", 
        "📚 Guides MathsCraft\n\n"
        "1. Opérations de base : Addition, soustraction, multiplication, division\n"
        "2. Théorie des nombres : PGCD, PPCM, nombres premiers\n"
        "3. Conversion : Bases numériques, unités de mesure\n"
        "4. Explorateur de Concepts : Jeu éducatif mathématique\n"
        "5. Polynômes : Résolution d'équations polynomiales\n"
        "6. Chaînes de caractères : Manipulation de texte\n"
        "7. Intégration numérique : Calculs d'intégrales\n\n"
        "Chaque module contient des instructions détaillées !"
    )

def afficher_a_propos():
    """Afficher la boîte À propos"""
    from tkinter import messagebox
    messagebox.showinfo(
        "À propos de MathsCraft", 
        "🧮 MathsCraft v1.0\n\n"
        "Un espace malin pour calculer et s'amuser avec les maths.\n\n"
        "Développé par Junior Kossivi\n"
        "© 2025 - Tous droits réservés\n\n"
        "Modules disponibles :\n"
        "- Opérations de base\n"
        "- Théorie des nombres\n" 
        "- Conversion\n"
        "- Explorateur de concepts\n"
        "- Polynômes & équations\n"
        "- Chaînes de caractères\n"
        "- Intégration numérique"
    )

# Initialiser l'interface historique
historique_interface = InterfaceHistorique(parent=None)  

# Fenetre principal
fenetre = Tk()
fenetre.title("MathsCraft")
fenetre.geometry("900x700")
fenetre.configure(bg="#F0F4F8")

# === MENU BURGER SIMPLIFIÉ ET FONCTIONNEL ===
def creer_menu_burger():
    """Crée un menu burger simple et fonctionnel"""
    # Cadre pour le header
    header_frame = Frame(fenetre, bg="#F0F4F8", height=60)
    header_frame.pack(fill=X, padx=20, pady=10)
    header_frame.pack_propagate(False)
    
    # Bouton menu burger à gauche
    burger_btn = Menubutton(
        header_frame,
        text="☰",
        font=("Arial", 16, "bold"),
        fg="#1E40AF",
        bg="#F0F4F8",
        relief="flat",
        bd=0,
        cursor="hand2",
        width=3
    )
    burger_btn.pack(side=LEFT, padx=(0, 15))
    
    # Titre à côté du bouton burger
    title_label = Label(
        header_frame,
        text="MathCrafts",
        font=("Century Gothic", 20, "bold"),
        fg="#1E40AF",
        bg="#F0F4F8"
    )
    title_label.pack(side=LEFT)
    
    # Créer le menu déroulant
    menu = Menu(burger_btn, tearoff=0, bg="white", fg="#1E293B", font=("Century Gothic", 10))
    
    # Ajouter les options au menu
    menu.add_command(label="📚 Guides", command=afficher_guides)
    menu.add_command(label="❤️ Soutenir", command=lambda: afficher_soutien(fenetre))
    menu.add_separator()
    menu.add_command(label="ℹ️ À propos", command=afficher_a_propos)
    
    # Associer le menu au bouton burger
    burger_btn.config(menu=menu)
    
    return header_frame

# Créer le menu burger
creer_menu_burger()

# Configuration du style pour les boutons
style = ttk.Style(fenetre)
style.theme_use('clam')

# Style pour les boutons principaux
style.configure("Custom.TButton",
                foreground="#FFFFFF",
                background="#3B82F6",
                font=("Century Gothic", 13, "bold"),
                padding=18,
                relief="flat",
                borderwidth=0,
                width=40)

style.configure("Quit.TButton",
                foreground="#FFFFFF",
                background="#DC2626",
                font=("Century Gothic", 14),
                relief="flat")

style.map("Custom.TButton",
          background=[('active', '#2563EB'), ('pressed', '#1D4ED8')],
          foreground=[('active', '#FFFFFF')])

# Style pour le bouton Quitter
style.configure("Quit.TButton",
                foreground="#FFFFFF",
                background="#DC2626",
                font=("Century Gothic", 13, "bold"),
                padding=18,
                relief="flat",
                borderwidth=0,
                width=40)

style.map("Quit.TButton",
          background=[('active', '#B91C1C'), ('pressed', '#991B1B')],
          foreground=[('active', "#FF0202")])

# Cadre pour contenir les boutons avec défilement si nécessaire
frame = Frame(fenetre, bg="#F0F4F8")
frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

# Créer un Canvas avec une Scrollbar
canvas = Canvas(frame, bg="#F0F4F8", highlightthickness=0)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#F0F4F8")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Permettre le défilement avec la molette de la souris
def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# === CONTENU PRINCIPAL ===
labels = Label(
    scrollable_frame,
    text="🧮 ✨ Un espace malin, Calculer et s'amuser avec les maths.",
    font=("Century Gothic", 13),
    fg="#64748B",
    bg="#F0F4F8"
)
labels.pack(pady=(0, 20))

# Séparateur
separator1 = ttk.Separator(scrollable_frame, orient='horizontal')
separator1.pack(fill='x', padx=50, pady=15)

# === SECTION BOUTONS ===
label2 = Label(
    scrollable_frame,
    text="Choisis ton opération !",
    fg="#1E293B",
    bg="#F0F4F8",
    font=("Century Gothic", 16, "bold"),
    justify="center"
)
label2.pack(pady=(10, 20))

# Boutons pour les Modules
bouton1 = ttk.Button(
    scrollable_frame,
    text="Module 1 : Opération de Base 🧮",
    style="Custom.TButton",
    compound=LEFT,
    command=op.launch_operation,
)

bouton2 = ttk.Button(
    scrollable_frame,
    text="Module 2 : Théorie des nombres ➕",
    style="Custom.TButton",
    compound=LEFT,
    command=theorie.lancer_theorie,
)

bouton3 = ttk.Button(
    scrollable_frame,
    text="Module 3 : Conversion ⚖️",
    style="Custom.TButton",
    compound=LEFT,
    command=conv.launch_conversion
)

bouton4 = ttk.Button(
    scrollable_frame,
    text="Module 4 : Explorateur de Concepts (Jeu) 🎯",
    style="Custom.TButton", 
    compound=LEFT,
    command=exp_concepts.lancer_explorateur_concepts
)

bouton6 = ttk.Button(
    scrollable_frame,
    text="Module 5 : Polynomes & Equations 📈",
    style="Custom.TButton",
    compound=LEFT,
    command=poly.lancer_polynome)

bouton8 = ttk.Button(
    scrollable_frame,
    text="Module 6 : Opération sur les chaines de caractère 🔠",
    style="Custom.TButton",
    compound=LEFT,
    command=ch.lancer_chaine
)

bouton9 = ttk.Button(
    scrollable_frame,
    text="Module 7 : Intégration Numérique 📊",
    style="Custom.TButton",
    compound=LEFT,
    command=int_num.lancer_integration_numerique
)

bouton_historique = ttk.Button(
    scrollable_frame,
    text="📊 Historique des Calculs", 
    style="Custom.TButton",
    compound=LEFT,
    command=lambda: historique_interface.afficher_historique()
)

# Placement des boutons
bouton1.pack(pady=8, fill=X, padx=60)
bouton2.pack(pady=8, fill=X, padx=60)
bouton3.pack(pady=8, fill=X, padx=60)
bouton4.pack(pady=8, fill=X, padx=60)
bouton6.pack(pady=8, fill=X, padx=60)
bouton8.pack(pady=8, fill=X, padx=60)
bouton9.pack(pady=8, fill=X, padx=60)
bouton_historique.pack(pady=8, fill=X, padx=60)

# Séparateur avant le bouton Quitter
separator2 = ttk.Separator(scrollable_frame, orient='horizontal')
separator2.pack(fill='x', padx=50, pady=20)

# Bouton Quitter avec style distinct
bouton10 = ttk.Button(
    scrollable_frame,
    text="Quitter",
    style="Quit.TButton",
    compound=LEFT,
    command=fenetre.destroy
)
bouton10.pack(pady=10, fill=X, padx=60)

# === PIED DE PAGE ===
footer = Label(
    scrollable_frame,
    text="© 2025 MathsCraft - Développé Par Junior Kossivi",
    font=("Century Gothic", 9),
    fg="#94A3B8",
    bg="#F0F4F8"
)
footer.pack(pady=(30, 20))

# Mettre à jour la référence parent de l'historique
historique_interface.parent = fenetre

fenetre.mainloop()