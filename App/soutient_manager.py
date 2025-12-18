"""
Gestionnaire de soutien pour MathCraft
"""
# ruff: noqa: E402,F405
import webbrowser
import tkinter as tk
from tkinter import ttk
from .style_manager import ensure_style

# Alias tkinter (remplacer les star-imports pour satisfaire le linter)
Label = tk.Label
Frame = tk.Frame
Toplevel = tk.Toplevel
Text = tk.Text
Canvas = tk.Canvas
Menu = tk.Menu
Menubutton = tk.Menubutton
Scrollbar = tk.Scrollbar
Entry = tk.Entry
LEFT = tk.LEFT
RIGHT = tk.RIGHT
BOTH = tk.BOTH
X = tk.X
Y = tk.Y
W = tk.W
NW = tk.NW
WORD = tk.WORD
# Constantes et états
DISABLED = tk.DISABLED
NORMAL = tk.NORMAL
END = tk.END
INSERT = tk.INSERT

# Palette unifiée (identique aux autres fichiers)
PALETTE = {
    "fond_principal": "#F0F4F8",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6", 
    "erreur": "#DC2626",
    "texte_fonce": "#1E40AF",
    "texte_clair": "#1E40AF"
}

class SoutienManager:
    def __init__(self):
        self.lien_kofi = "https://ko-fi.com/juniorkossivi"  # Mon lien Ko-fi
        
    def afficher_fenetre_soutien(self, parent=None):
        """Affiche la fenêtre de soutien"""
        fenetre = Toplevel(parent)
        fenetre.title("❤️ Soutenir MathCraft")
        fenetre.geometry("550x650")
        fenetre.configure(bg=PALETTE["fond_principal"])
        fenetre.resizable(False, False)
        
        # Centrer la fenêtre
        fenetre.transient(parent)
        fenetre.grab_set()
        
        self._creer_interface(fenetre)
        
        return fenetre
    
    def _creer_interface(self, fenetre):
        """Crée l'interface de la fenêtre de soutien"""
        
        # ==================== EN-TÊTE ====================
        header_frame = Frame(fenetre, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="❤️ SOUTENIR MATHCRAFT", 
              font=("Century Gothic", 22, "bold"), 
              bg=PALETTE["primaire"], fg="white").pack(pady=25)
        
        Label(header_frame, text="Votre encouragement fait vivre le projet !", 
              font=("Century Gothic", 12), 
              bg=PALETTE["primaire"], fg="#E0F2FE").pack(pady=(0, 20))
        
        # ==================== CONTENU PRINCIPAL ====================
        main_frame = Frame(fenetre, bg=PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=30, pady=20)
        
        # Message principal
        message_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        message_frame.pack(fill=X, pady=(0, 30))
        
        Label(message_frame, 
              text="MathCraft est développé avec passion pour rendre les mathématiques accessibles et amusantes pour tous.",
              font=("Century Gothic", 12), 
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
              wraplength=500, justify="center").pack(pady=10)
        
        Label(message_frame, 
              text="Si l'application vous plaît et que vous souhaitez m'encourager à continuer le développement...",
              font=("Century Gothic", 11), 
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"],
              wraplength=500, justify="center").pack(pady=5)
        
        # ==================== CARTE KO-FI ====================
        plateforme_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        plateforme_frame.pack(fill=X, pady=(0, 30))
        
        Label(plateforme_frame, text="💝 Votre soutien :",
              font=("Century Gothic", 14, "bold"), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0, 20))
        
        # Carte Ko-fi unique
        carte_kofi = Frame(plateforme_frame, bg="white", relief="raised", borderwidth=2)
        carte_kofi.pack(fill=X, pady=10, ipady=10)
        carte_kofi.configure(cursor="hand2")
        
        # Bind des événements de souris
        carte_kofi.bind("<Button-1>", lambda e: self._ouvrir_kofi())
        
        content_frame = Frame(carte_kofi, bg="white")
        content_frame.pack(fill=X, padx=25, pady=20)
        
        # Emoji et texte
        emoji_frame = Frame(content_frame, bg="white")
        emoji_frame.pack(side=LEFT, fill=Y)
        
        Label(emoji_frame, text="☕", font=("Arial", 28), bg="white").pack(side=LEFT, padx=(0, 20))
        
        text_frame = Frame(emoji_frame, bg="white")
        text_frame.pack(side=LEFT, fill=Y)
        
        Label(text_frame, text="Offrez-moi un café symbolique !", 
              font=("Century Gothic", 16, "bold"), 
              bg="white", fg="#FF5E5E").pack(anchor="w")
        
        Label(text_frame, text="Sur Ko-fi - Plateforme simple et intuitive", 
              font=("Century Gothic", 11), 
              bg="white", fg=PALETTE["texte_clair"]).pack(anchor="w", pady=(2, 0))
        
        # Flèche
        Label(content_frame, text="➡️", font=("Arial", 18), 
              bg="white", fg=PALETTE["texte_clair"]).pack(side=RIGHT)
        
        # Message d'explication
        Label(plateforme_frame, 
              text="Cliquez sur la carte ci-dessus pour visiter ma page Ko-fi",
              font=("Century Gothic", 10), 
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"],
              justify="center").pack(pady=10)
        
        # ==================== CONTREPARTIES ====================
        contreparties_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        contreparties_frame.pack(fill=X, pady=(0, 30))
        
        Label(contreparties_frame, text="🎁 En retour de votre soutien :",
              font=("Century Gothic", 14, "bold"), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0, 15))
        
        contreparties = [
            "✅ Ma motivation décuplée pour améliorer MathCraft !",
            "✅ Votre nom dans les crédits des prochaines versions", 
            "✅ Accès anticipé aux nouvelles fonctionnalités",
            "✅ Un immense merci pour votre encouragement ❤️"
        ]
        
        for contrepartie in contreparties:
            Label(contreparties_frame, text=contrepartie,
                  font=("Century Gothic", 11), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
                  anchor="w").pack(fill=X, pady=3)
        
        # ==================== ENGAGEMENT ====================
        engagement_frame = Frame(main_frame, bg="#F0F9FF", relief="solid", borderwidth=1)
        engagement_frame.pack(fill=X, pady=(0, 20), ipady=15)
        
        Label(engagement_frame, text="📜 Mon engagement :",
              font=("Century Gothic", 12, "bold"), 
              bg="#F0F9FF", fg=PALETTE["primaire"]).pack(pady=(0, 10))
        
        Label(engagement_frame, 
              text="MathCraft restera 100% gratuit, sans publicité ni limitations.\nVotre soutien sert uniquement à m'encourager à continuer !",
              font=("Century Gothic", 10), 
              bg="#F0F9FF", fg=PALETTE["primaire"],
              justify="center").pack()
        
        # ==================== BOUTONS ====================
        buttons_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, pady=20)
        
        # Style pour les boutons
        s = ensure_style()
        if s is None:
            s = ttk.Style()
        s.configure("Soutien.TButton", font=("Century Gothic", 10))
        
        # Bouton principal Ko-fi
        ttk.Button(buttons_frame, text="☕ Aller sur Ko-fi", 
                  command=self._ouvrir_kofi,
                  style="Soutien.TButton").pack(side=LEFT, padx=5)
        
        # Bouton Partager
        ttk.Button(buttons_frame, text="📤 Partager l'application", 
                  command=self._partager_application,
                  style="Soutien.TButton").pack(side=LEFT, padx=5)
        
        # Bouton Fermer
        ttk.Button(buttons_frame, text="Fermer", 
                  command=fenetre.destroy,
                  style="Soutien.TButton").pack(side=RIGHT, padx=5)
    
    def _ouvrir_kofi(self):
        """Ouvre la page Ko-fi"""
        webbrowser.open(self.lien_kofi)
    
    def _partager_application(self):
        """Ouvre une fenêtre pour partager l'application"""
        fenetre_partage = Toplevel()
        fenetre_partage.title("📤 Partager MathCraft")
        fenetre_partage.geometry("500x400")
        fenetre_partage.configure(bg=PALETTE["fond_principal"])
        
        Label(fenetre_partage, text="🎉 Partagez MathCraft !", 
              font=("Century Gothic", 18, "bold"), 
              bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=20)
        
        message_frame = Frame(fenetre_partage, bg=PALETTE["fond_principal"])
        message_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        message_text = (
            "Découvrez MathCraft - une application géniale pour apprendre les maths en s'amusant !\n\n"
            "🎮 Des jeux mathématiques passionnants\n"
            "🧮 Des outils de calcul complets\n"
            "📚 Accessible à tous les niveaux\n\n"
            "Téléchargez-la gratuitement !\n"
            "👉 [Lien de téléchargement à ajouter]"
        )
        
        text_widget = Text(message_frame, height=12, width=50, font=("Century Gothic", 11),
                         bg="white", relief="solid", borderwidth=1, wrap=WORD)
        text_widget.pack(fill=BOTH, expand=True)
        text_widget.insert("1.0", message_text)
        text_widget.config(state="disabled")
        
        ttk.Button(fenetre_partage, text="Fermer", 
                  command=fenetre_partage.destroy).pack(pady=10)

# Instance globale
soutien_manager = SoutienManager()

# Fonction d'accès direct
def afficher_soutien(parent=None):
    """Affiche la fenêtre de soutien (fonction principale)"""
    return soutien_manager.afficher_fenetre_soutien(parent)