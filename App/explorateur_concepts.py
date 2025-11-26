"""Interface pour l'Explorateur de Concepts - Module 4"""
from tkinter import *
from tkinter import ttk
from .jeux_math import JEUX_DISPONIBLES

# Palette de couleurs améliorée
PALETTE = {
    "fond_principal": "#F0F4F8",
    "fond_secondaire": "#FFFFFF",
    "primaire": "#1E40AF",      # Bleu plus foncé pour meilleur contraste
    "secondaire": "#3B82F6",    # Bleu original pour accents
    "texte_fonce": "#1E293B",   # Texte très visible
    "texte_clair": "#64748B",   # Texte secondaire
    "succes": "#10B981",        # Vert
    "erreur": "#DC2626",        # Rouge
    "bordure": "#E2E8F0",       # Bordure légère
}

def configurer_styles():
    """Configure les styles ttk pour l'explorateur de concepts"""
    style = ttk.Style()
    style.theme_use("clam")
    
    # Style bouton jeu actif
    style.configure("JeuActif.TButton",
                   foreground=PALETTE["fond_secondaire"],
                   background=PALETTE["primaire"],
                   font=("Century Gothic", 11, "bold"),
                   padding=15,
                   relief="flat",
                   focuscolor="none")
    
    # Style bouton jeu inactif
    style.configure("JeuInactif.TButton",
                   foreground=PALETTE["texte_clair"],
                   background=PALETTE["bordure"],
                   font=("Century Gothic", 11),
                   padding=15,
                   relief="flat",
                   focuscolor="none")
    
    # Style bouton retour
    style.configure("Retour.TButton",
                   foreground=PALETTE["fond_secondaire"],
                   background=PALETTE["erreur"],
                   font=("Century Gothic", 11, "bold"),
                   padding=12,
                   relief="flat",
                   focuscolor="none")
    
    # Effets au survol
    style.map("JeuActif.TButton",
             background=[('active', PALETTE["secondaire"]),
                        ('pressed', '#1E3A8A')],
             foreground=[('active', PALETTE["fond_secondaire"])])
    
    style.map("JeuInactif.TButton",
             background=[('active', '#D1D5DB'),
                        ('pressed', '#9CA3AF')],
             foreground=[('active', PALETTE["texte_clair"])])
    
    style.map("Retour.TButton",
             background=[('active', '#B91C1C'),
                        ('pressed', '#991B1B')],
             foreground=[('active', PALETTE["fond_secondaire"])])

def lancer_explorateur_concepts(parent=None):
    """Lance le menu principal des jeux mathématiques"""
    # Configurer les styles d'abord
    configurer_styles()
    
    explorateur = Toplevel(parent)
    explorateur.title("🎮 Explorateur de Concepts - Jeux Mathématiques")
    explorateur.geometry("550x650")
    explorateur.configure(bg=PALETTE["fond_principal"])
    explorateur.resizable(False, False)

    # Centrer la fenêtre
    explorateur.transient(parent)
    explorateur.grab_set()

    # Cadre principal avec défilement
    main_frame = Frame(explorateur, bg=PALETTE["fond_principal"])
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)

    # Canvas et scrollbar pour le défilement
    canvas = Canvas(main_frame, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=PALETTE["fond_principal"])

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Défilement avec molette
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

    # En-tête
    header_frame = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    header_frame.pack(fill=X, pady=(0, 10))

    Label(header_frame, 
          text="🎮 EXPLORATEUR DE CONCEPTS", 
          font=("Century Gothic", 18, "bold"), 
          bg=PALETTE["fond_principal"], 
          fg=PALETTE["primaire"]).pack(pady=(10, 5))

    Label(header_frame, 
          text="Choisis ton jeu mathématique !", 
          font=("Century Gothic", 12), 
          bg=PALETTE["fond_principal"], 
          fg=PALETTE["texte_clair"]).pack(pady=(0, 10))

    # Séparateur
    separator = ttk.Separator(scrollable_frame, orient='horizontal')
    separator.pack(fill='x', pady=10)

    # Frame pour les boutons des jeux
    jeux_frame = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    jeux_frame.pack(fill=BOTH, expand=True, pady=10)

    # Créer un bouton pour chaque jeu
    for jeu in JEUX_DISPONIBLES:
        if jeu["disponible"]:
            btn = ttk.Button(jeux_frame, 
                            text=f"🎯 {jeu['nom']}\n{jeu['description']}",
                            style="JeuActif.TButton",
                            command=lambda f=jeu['fonction']: f(explorateur))
        else:
            btn = ttk.Button(jeux_frame,
                            text=f"🔒 {jeu['nom']}\n{jeu['description']}\n⏳ Prochainement",
                            style="JeuInactif.TButton",
                            state="disabled")
        btn.pack(pady=8, fill=X, padx=5)

    # Séparateur avant le bouton retour
    separator2 = ttk.Separator(scrollable_frame, orient='horizontal')
    separator2.pack(fill='x', pady=20)

    # Bouton retour
    ttk.Button(scrollable_frame, 
              text="🚪 Retour au Menu Principal",
              style="Retour.TButton",
              command=explorateur.destroy).pack(pady=10, fill=X, padx=5)

    # Pied de page
    footer = Label(scrollable_frame,
                  text="🎮 Explorateur de Concepts - MathsCraft",
                  font=("Century Gothic", 9),
                  fg=PALETTE["texte_clair"],
                  bg=PALETTE["fond_principal"])
    footer.pack(pady=15)

    # Ajuster la zone de défilement
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    return explorateur