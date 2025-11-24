"""
Interface pour l'Explorateur de Concepts - Module 4
"""
from tkinter import *
from tkinter import ttk
from .jeux_math import JEUX_DISPONIBLES

def lancer_explorateur_concepts(parent=None):
    """Lance le menu principal des jeux mathématiques"""
    explorateur = Toplevel(parent)
    explorateur.title("🎮 Explorateur de Concepts - Jeux Mathématiques")
    explorateur.geometry("500x600")
    explorateur.configure(bg="#F0F4F8")

    # En-tête
    Label(explorateur, text="🎮 EXPLORATEUR DE CONCEPTS", 
          font=("Century Gothic", 18, "bold"), 
          bg="#F0F4F8", fg="#1E40AF").pack(pady=20)

    Label(explorateur, text="Choisis ton jeu mathématique !", 
          font=("Century Gothic", 12), 
          bg="#F0F4F8", fg="#64748B").pack(pady=10)

    # Frame pour les boutons
    jeux_frame = Frame(explorateur, bg="#F0F4F8")
    jeux_frame.pack(pady=30, fill=BOTH, expand=True, padx=50)

    # Style
    style = ttk.Style()
    style.configure("JeuActif.TButton", foreground="#FFFFFF", background="#3B82F6",
                   font=("Century Gothic", 11), padding=12)
    style.configure("JeuInactif.TButton", foreground="#999999", background="#E5E7EB",
                   font=("Century Gothic", 11), padding=12)

    # Créer un bouton pour chaque jeu
    for jeu in JEUX_DISPONIBLES:
        if jeu["disponible"]:
            btn = ttk.Button(jeux_frame, 
                            text=f"{jeu['nom']}\n{jeu['description']}",
                            style="JeuActif.TButton",
                            command=lambda f=jeu['fonction']: f(explorateur))
        else:
            btn = ttk.Button(jeux_frame,
                            text=f"{jeu['nom']}\n{jeu['description']}\n[Prochainement]",
                            style="JeuInactif.TButton",
                            state="disabled")
        btn.pack(pady=8, fill=X)

    # Bouton quitter
    ttk.Button(explorateur, 
              text="🚪 Retour au Menu Principal",
              command=explorateur.destroy).pack(pady=20)

    return explorateur