"""
Module central pour tous les jeux mathématiques de MathCraft
"""
import random
import time
import math
from tkinter import *
from tkinter import ttk, messagebox
import json
import os

# =============================================================================
# GUIDES ET EXEMPLES POUR TOUS LES JEUX
# =============================================================================

GUIDES_JEUX = {
    "math_quizz": {
        "titre": "🎯 Guide du Math Quizz Challenge",
        "contenu": [
            "📝 **Comment jouer :**",
            "• Répondez aux questions mathématiques dans le temps imparti",
            "• Plus vous répondez vite, plus vous gagnez de points bonus",
            "• Les questions deviennent plus difficiles avec votre score",
            "",
            "🎮 **Types de questions :**",
            "• Arithmétique : additions, soustractions, multiplications",
            "• Algèbre : équations simples, expressions",
            "• Géométrie : calculs d'aires, périmètres", 
            "• Trigonométrie : sin, cos, tan des angles courants",
            "• Racines et puissances : √, ², ³",
            "",
            "🏆 **Système de points :**",
            "• Débutant : 10 points par question",
            "• Intermédiaire : 20 points par question", 
            "• Expert : 30 points par question",
            "• Bonus rapidité : +2 à +5 points selon le temps restant",
            "",
            "💡 **Conseils stratégiques :**",
            "• Entraînez-vous sur les tables de multiplication",
            "• Mémorisez les carrés parfaits (1-20)",
            "• Connaissez les valeurs trigonométriques des angles courants",
            "• Gérez votre temps - ne restez pas bloqué sur une question"
        ],
        "exemples": [
            "🧮 **Exemples de questions :**",
            "",
            "Débutant :",
            "• 7 × 8 = ? → 56",
            "• 45 ÷ 9 = ? → 5", 
            "• 15 + 23 = ? → 38",
            "",
            "Intermédiaire :",
            "• 3² + 4² = ? → 25",
            "• √144 = ? → 12",
            "• 2x + 5 = 17 → x = ? → 6",
            "",
            "Expert :",
            "• sin(π/2) = ? → 1",
            "• log₁₀(100) = ? → 2",
            "• (3 + 4i)(3 - 4i) = ? → 25"
        ]
    },
    
    "course_nombres": {
        "titre": "🏆 Guide de la Course aux Nombres", 
        "contenu": [
            "🎯 **Objectif du jeu :**",
            "Atteindre exactement la cible en utilisant les nombres donnés",
            "avec les opérations +, -, ×, ÷ et des parenthèses.",
            "",
            "📝 **Comment jouer :**",
            "• Utilisez TOUS les nombres donnés (ou une partie)",
            "• Chaque nombre ne peut être utilisé qu'UNE fois",
            "• Les opérations autorisées : + - × ÷ ( )",
            "• Vous avez 2 minutes par défi",
            "",
            "🎮 **Niveaux de difficulté :**",
            "• Facile : 4 nombres, cible 10-50",
            "• Moyen : 5 nombres, cible 20-100", 
            "• Difficile : 6 nombres, cible 50-200",
            "",
            "🏅 **Système de points :**",
            "• Points de base : 10 points",
            "• Bonus parenthèses : +5 points",
            "• Bonus opérations multiples : +5 points",
            "• Bonus divisions : +3 points",
            "• Multiplicateur niveau : Facile×1, Moyen×2, Difficile×3",
            "",
            "💡 **Stratégies gagnantes :**",
            "• Cherchez d'abord les multiplications/divisions",
            "• Utilisez les parenthèses pour changer l'ordre des opérations",
            "• Essayez différentes combinaisons",
            "• Pensez aux fractions et nombres décimaux"
        ],
        "exemples": [
            "🧮 **Exemples de solutions :**",
            "",
            "Cible : 24, Nombres : [4, 8, 3, 6]",
            "• 8 × 3 = 24 → +10 points (simple)",
            "• (8 - 6) × 4 × 3 = 24 → +20 points (avec parenthèses)",
            "• 4 × (8 - 6 ÷ 3) = 24 → +23 points (complexe)",
            "",
            "Cible : 100, Nombres : [5, 5, 10, 15]",
            "• (15 + 5) × 5 = 100 → +15 points",
            "• 10 × (5 + 5) = 100 → +15 points", 
            "",
            "Cible : 50, Nombres : [2, 3, 7, 8, 10]",
            "• (10 + 8 - 3) × (7 - 2) = 50 → +25 points"
        ]
    },
    
    "math_emoji": {
        "titre": "🍎 Guide du Math Emoji",
        "contenu": [
            "🎯 **Concept du jeu :**",
            "Résoudre des systèmes d'équations où les inconnues sont des emojis!",
            "Chaque emoji représente un nombre à découvrir.",
            "",
            "📝 **Comment jouer :**",
            "• Deux équations sont données avec des emojis",
            "• Trouvez la valeur numérique de chaque emoji",
            "• Entrez vos réponses dans les champs correspondants", 
            "",
            "🎮 **Types d'équations :**",
            "• Systèmes linéaires : 🍎 + 🍌 = X, 🍎 - 🍌 = Y",
            "• Avec multiplication : 🍎 × 🍌 = X, 🍎 + 🍌 = Y",
            "• Équations complexes : 🍎 + 🍌 + 🍎 = X, etc.",
            "",
            "🏅 **Système de points :**",
            "• Points de base : 10 points",
            "• Bonus système : +5 points",
            "• Bonus trois emojis : +8 points", 
            "• Multiplicateur niveau : Facile×1, Moyen×2, Difficile×3",
            "",
            "💡 **Méthodes de résolution :**",
            "• Méthode par substitution",
            "• Méthode par élimination",
            "• Méthode par comparaison",
            "• Pensez aux nombres entiers uniquement!"
        ],
        "exemples": [
            "🧮 **Exemples résolus :**",
            "",
            "Exemple 1 :",
            "🍎 + 🍌 = 12",
            "🍎 - 🍌 = 4",
            "Solution :",
            "• Additionnez les équations : 2🍎 = 16 → 🍎 = 8",
            "• Substituer : 8 + 🍌 = 12 → 🍌 = 4",
            "",
            "Exemple 2 :", 
            "🚗 × 🚕 = 24",
            "🚗 + 🚕 = 10", 
            "Solution :",
            "• Facteurs de 24 : (1,24), (2,12), (3,8), (4,6)",
            "• Paire dont la somme est 10 : (4,6)",
            "• Donc 🚗 = 4, 🚕 = 6 ou inversement",
            "",
            "Exemple 3 :",
            "⚽ + 🏀 = 15",
            "⚽ + 🏀 + ⚽ = 23", 
            "Solution :",
            "• De la 2ème : 2⚽ + 🏀 = 23",
            "• Soustraire la 1ère : ⚽ = 8",
            "• Substituer : 8 + 🏀 = 15 → 🏀 = 7"
        ]
    }
}

# =============================================================================
# FONCTIONS POUR AFFICHER LES GUIDES
# =============================================================================

def afficher_guide_jeu(nom_jeu, parent=None):
    """Affiche le guide détaillé pour un jeu spécifique"""
    if nom_jeu not in GUIDES_JEUX:
        messagebox.showinfo("Guide", "Guide non disponible pour ce jeu.")
        return
        
    guide = GUIDES_JEUX[nom_jeu]
    
    fenetre_guide = Toplevel(parent)
    fenetre_guide.title(guide["titre"])
    fenetre_guide.geometry("800x700")
    fenetre_guide.configure(bg="#F0F4F8")
    
    # Cadre principal avec scrollbar
    main_frame = Frame(fenetre_guide, bg="#F0F4F8")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    canvas = Canvas(main_frame, bg="#F0F4F8", highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#F0F4F8")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    # Contenu du guide
    Label(scrollable_frame, text=guide["titre"], 
          font=("Century Gothic", 20, "bold"), bg="#F0F4F8", fg="#1E40AF").pack(pady=20)
    
    # Partie guide
    guide_frame = Frame(scrollable_frame, bg="#F0F4F8")
    guide_frame.pack(fill=X, pady=10)
    
    for ligne in guide["contenu"]:
        if ligne.startswith("•"):
            Label(guide_frame, text=ligne, font=("Century Gothic", 11), 
                  bg="#F0F4F8", fg="#374151", justify="left", anchor="w").pack(fill=X, padx=20, pady=1)
        elif ligne.startswith("📝") or ligne.startswith("🎮") or ligne.startswith("🏆") or ligne.startswith("💡"):
            Label(guide_frame, text=ligne, font=("Century Gothic", 12, "bold"), 
                  bg="#F0F4F8", fg="#1E40AF", justify="left", anchor="w").pack(fill=X, padx=10, pady=(15,5))
        else:
            Label(guide_frame, text=ligne, font=("Century Gothic", 11), 
                  bg="#F0F4F8", fg="#64748B", justify="left", anchor="w").pack(fill=X, padx=20, pady=2)
    
    # Séparateur
    ttk.Separator(scrollable_frame, orient='horizontal').pack(fill=X, pady=20)
    
    # Partie exemples
    exemples_frame = Frame(scrollable_frame, bg="#F0F4F8")
    exemples_frame.pack(fill=X, pady=10)
    
    for ligne in guide["exemples"]:
        if ligne.startswith("🧮"):
            Label(exemples_frame, text=ligne, font=("Century Gothic", 14, "bold"), 
                  bg="#F0F4F8", fg="#8B5CF6", justify="left", anchor="w").pack(fill=X, padx=10, pady=(10,5))
        elif ligne.startswith("•"):
            Label(exemples_frame, text=ligne, font=("Century Gothic", 11), 
                  bg="#F0F4F8", fg="#7C3AED", justify="left", anchor="w").pack(fill=X, padx=25, pady=1)
        elif ligne == "":
            Label(exemples_frame, text=" ", font=("Century Gothic", 4), 
                  bg="#F0F4F8").pack(fill=X, pady=2)
        else:
            Label(exemples_frame, text=ligne, font=("Century Gothic", 11, "italic"), 
                  bg="#F0F4F8", fg="#6D28D9", justify="left", anchor="w").pack(fill=X, padx=20, pady=2)
    
    # Bouton fermer
    ttk.Button(scrollable_frame, text="Fermer le guide", 
              command=fenetre_guide.destroy).pack(pady=20)
    
    # Espace final
    Label(scrollable_frame, text="", bg="#F0F4F8", height=2).pack()

# =============================================================================
# INTERFACE DE SÉLECTION DES JEUX AVEC SCROLLBAR
# =============================================================================

def creer_interface_jeux(parent=None):
    """Crée l'interface de sélection des jeux avec scrollbar"""
    fenetre_jeux = Toplevel(parent) if parent else Tk()
    fenetre_jeux.title("🎮 MathCraft - Sélection des Jeux")
    fenetre_jeux.geometry("900x800")
    fenetre_jeux.configure(bg="#F0F4F8")
    
    # Style
    style = ttk.Style()
    style.configure("Jeu.TButton", 
                   font=("Century Gothic", 12),
                   padding=15,
                   relief="flat")
    
    style.configure("Guide.TButton",
                   font=("Century Gothic", 10),
                   padding=8)
    
    # En-tête fixe
    header_frame = Frame(fenetre_jeux, bg="#1E40AF")
    header_frame.pack(fill=X, pady=(0, 10))
    
    Label(header_frame, text="🎮 MATHCRAFT - ESPACE JEUX", 
          font=("Century Gothic", 24, "bold"), bg="#1E40AF", fg="white").pack(pady=20)
    
    Label(header_frame, text="Choisis ton aventure mathématique !", 
          font=("Century Gothic", 14), bg="#1E40AF", fg="#E0F2FE").pack(pady=(0, 15))
    
    # Cadre principal avec scrollbar
    main_frame = Frame(fenetre_jeux, bg="#F0F4F8")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    canvas = Canvas(main_frame, bg="#F0F4F8", highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#F0F4F8")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    # Contenu des jeux
    content_frame = scrollable_frame
    
    # Section jeux disponibles
    Label(content_frame, text="🎯 JEUX DISPONIBLES", 
          font=("Century Gothic", 18, "bold"), bg="#F0F4F8", fg="#1E40AF").pack(pady=20)
    
    # Création des cartes de jeux
    for i, jeu in enumerate(JEUX_DISPONIBLES):
        # Carte du jeu
        carte_frame = Frame(content_frame, bg="white", relief="raised", borderwidth=2)
        carte_frame.pack(fill=X, padx=10, pady=12, ipady=10)
        
        # Contenu de la carte
        top_frame = Frame(carte_frame, bg="white")
        top_frame.pack(fill=X, padx=20, pady=15)
        
        # Titre et description
        text_frame = Frame(top_frame, bg="white")
        text_frame.pack(side=LEFT, fill=X, expand=True)
        
        titre_label = Label(text_frame, text=jeu["nom"], 
                           font=("Century Gothic", 16, "bold"), 
                           bg="white", fg="#1E40AF", anchor="w")
        titre_label.pack(fill=X)
        
        desc_label = Label(text_frame, text=jeu["description"],
                          font=("Century Gothic", 11),
                          bg="white", fg="#64748B", justify="left", anchor="w")
        desc_label.pack(fill=X, pady=(5, 0))
        
        # Boutons
        buttons_frame = Frame(top_frame, bg="white")
        buttons_frame.pack(side=RIGHT, padx=(20, 0))
        
        if jeu["disponible"]:
            # Bouton jouer
            jouer_btn = ttk.Button(buttons_frame, text="🎮 Jouer", 
                                  style="Jeu.TButton",
                                  command=jeu["fonction"])
            jouer_btn.pack(pady=5)
            
            # Bouton guide si disponible
            if "guide" in jeu:
                guide_btn = ttk.Button(buttons_frame, text="📚 Guide", 
                                      style="Guide.TButton",
                                      command=lambda g=jeu["guide"]: g(fenetre_jeux))
                guide_btn.pack(pady=5)
        else:
            # Bouton bientôt disponible
            soon_btn = ttk.Button(buttons_frame, text="🔜 Bientôt", 
                                 style="Guide.TButton",
                                 state="disabled")
            soon_btn.pack(pady=5)
        
        # Indicateur de statut
        status_frame = Frame(carte_frame, bg="white")
        status_frame.pack(fill=X, padx=20, pady=(0, 10))
        
        if jeu["disponible"]:
            status_label = Label(status_frame, text="✅ Disponible", 
                               font=("Century Gothic", 9, "bold"),
                               bg="white", fg="#10B981")
        else:
            status_label = Label(status_frame, text="⏳ En développement", 
                               font=("Century Gothic", 9),
                               bg="white", fg="#F59E0B")
        status_label.pack(side=LEFT)
    
    # Section informations
    info_frame = Frame(content_frame, bg="#E0F2FE", relief="solid", borderwidth=1)
    info_frame.pack(fill=X, padx=10, pady=30, ipady=15)
    
    Label(info_frame, text="💡 Informations importantes", 
          font=("Century Gothic", 14, "bold"), bg="#E0F2FE", fg="#1E40AF").pack(pady=(0, 10))
    
    infos = [
        "• Chaque jeu propose des défis adaptés à ton niveau",
        "• Consulte les guides pour apprendre les stratégies gagnantes", 
        "• Plus tu joues, plus tu débloques de badges et récompenses",
        "• N'hésite pas à essayer différents jeux pour varier les plaisirs !"
    ]
    
    for info in infos:
        Label(info_frame, text=info, font=("Century Gothic", 10), 
              bg="#E0F2FE", fg="#1E40AF", justify="left", anchor="w").pack(fill=X, padx=20, pady=2)
    
    # Bouton fermer
    ttk.Button(content_frame, text="🚪 Fermer", 
              command=fenetre_jeux.destroy,
              style="Jeu.TButton").pack(pady=30)
    
    # Espace final pour le défilement
    Label(content_frame, text="", bg="#F0F4F8", height=2).pack()
    
    return fenetre_jeux

# =============================================================================
# MATH QUIZZ CHALLENGE AMÉLIORÉ
# =============================================================================

class MathQuizzChallenge:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau_actuel = "Débutant"
        self.question_actuelle = None
        self.temps_debut = None
        self.temps_limite = 30
        self.questions_repondus = 0
        self.questions_total = 0
        self.badges_gagnes = []
        
        # Charger les questions depuis JSON
        self.questions = self._charger_questions_avance()
        self.questions_total = sum(len(q) for q in self.questions.values())
        
        # Timer
        self.timer_actif = False
        self.temps_restant = self.temps_limite

    def _charger_questions_avance(self):
        """Charge les questions depuis le JSON inclus"""
        try:
            with open("data/questions.json", "r", encoding="utf-8") as f:
                questions_data = json.load(f)
                total_questions = sum(len(q) for q in questions_data.values())
                print(f"✅ {total_questions} questions chargées depuis data/questions.json")
                return questions_data
        except Exception as e:
            print(f"❌ Erreur chargement questions: {e}")
            print("🔄 Utilisation des questions de secours...")
            return self._questions_par_defaut()

    def _questions_par_defaut(self):
        """Questions par défaut si le JSON n'est pas trouvé"""
        return {
            "Débutant": [
                {"question": "2 + 3 = ?", "reponse": 5, "type": "arithmetique", "points": 10},
                {"question": "5 × 4 = ?", "reponse": 20, "type": "arithmetique", "points": 10},
            ],
            "Intermédiaire": [
                {"question": "√16 = ?", "reponse": 4, "type": "racine", "points": 20},
                {"question": "3² + 4² = ?", "reponse": 25, "type": "puissance", "points": 20},
            ],
            "Expert": [
                {"question": "2x + 5 = 15 → x = ?", "reponse": 5, "type": "equation", "points": 30},
                {"question": "sin(π/2) = ?", "reponse": 1, "type": "trigonometrie", "points": 30},
            ]
        }

    def lancer_jeu(self):
        """Lance l'interface du jeu améliorée"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🎯 Math Quizz Challenge Pro")
        self.fenetre_jeu.geometry("700x800")
        self.fenetre_jeu.configure(bg="#F0F4F8")
        
        self._creer_interface_avance()
        self._prochaine_question()

    def _creer_interface_avance(self):
        """Crée l'interface avancée avec timer et progression"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg="#1E40AF")
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🎯 MATH QUIZZ CHALLENGE PRO", 
              font=("Century Gothic", 20, "bold"), bg="#1E40AF", fg="white").pack(pady=15)

        # Frame des statistiques
        stats_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Score
        self.score_label = Label(stats_frame, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 14, "bold"), bg="#F0F4F8", fg="#1E40AF")
        self.score_label.pack(side=LEFT, padx=20)
        
        # Niveau
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau_actuel}",
                                 font=("Century Gothic", 12), bg="#F0F4F8", fg="#64748B")
        self.niveau_label.pack(side=LEFT, padx=20)
        
        # Timer
        self.timer_label = Label(stats_frame, text=f"⏱️ Temps: {self.temps_restant}s",
                                font=("Century Gothic", 12, "bold"), bg="#F0F4F8", fg="#DC2626")
        self.timer_label.pack(side=RIGHT, padx=20)

        # Barre de progression
        progress_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        progress_frame.pack(fill=X, padx=20, pady=10)
        
        Label(progress_frame, text="Progression:", 
              font=("Century Gothic", 10), bg="#F0F4F8").pack(anchor=W)
        
        self.progress_bar = ttk.Progressbar(progress_frame, orient=HORIZONTAL, 
                                           length=600, mode='determinate')
        self.progress_bar.pack(fill=X, pady=5)
        
        self.progress_label = Label(progress_frame, text="0/0 questions",
                                   font=("Century Gothic", 9), bg="#F0F4F8", fg="#64748B")
        self.progress_label.pack(anchor=W)

        # Badges
        self.badges_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        self.badges_frame.pack(fill=X, padx=20, pady=10)
        
        self.badges_label = Label(self.badges_frame, text="🎖️ Badges: Aucun pour le moment",
                                 font=("Century Gothic", 10), bg="#F0F4F8", fg="#64748B")
        self.badges_label.pack(anchor=W)

        # Bouton guide
        guide_button = ttk.Button(self.badges_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("math_quizz", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Séparateur
        ttk.Separator(self.fenetre_jeu, orient='horizontal').pack(fill=X, padx=20, pady=10)

        # Question
        question_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        question_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        self.question_label = Label(question_frame, text="", font=("Century Gothic", 18, "bold"),
                                   bg="#F0F4F8", fg="#1E293B", wraplength=600, justify="center")
        self.question_label.pack(pady=30)

        # Réponse
        reponse_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        reponse_frame.pack(fill=X, padx=20, pady=10)
        
        Label(reponse_frame, text="Ta réponse:", 
              font=("Century Gothic", 12), bg="#F0F4F8").pack(pady=5)
        
        self.reponse_entry = Entry(reponse_frame, font=("Century Gothic", 16), 
                                  width=20, justify="center")
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse())

        # Points de la question
        self.points_label = Label(reponse_frame, text="", 
                                 font=("Century Gothic", 11), bg="#F0F4F8", fg="#8B5CF6")
        self.points_label.pack()

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        buttons_frame.pack(fill=X, padx=20, pady=20)
        
        ttk.Button(buttons_frame, text="✅ Vérifier la réponse", 
                  command=self._verifier_reponse).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="➡️ Question suivante", 
                  command=self._prochaine_question).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="📊 Voir les badges", 
                  command=self._afficher_badges).pack(side=RIGHT, padx=10)

        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", font=("Century Gothic", 13), 
                                   bg="#F0F4F8", wraplength=500)
        self.feedback_label.pack(pady=10)

    def _demarrer_timer(self):
        """Démarre le compte à rebours"""
        self.temps_restant = self.temps_limite
        self.timer_actif = True
        self._mettre_a_jour_timer()

    def _arreter_timer(self):
        """Arrête le timer"""
        self.timer_actif = False

    def _mettre_a_jour_timer(self):
        """Met à jour le timer chaque seconde - version corrigée"""
        if not self.timer_actif or self.temps_restant <= 0:
            return
            
        try:
            # Vérifier si la fenêtre existe encore
            if not self.fenetre_jeu.winfo_exists():
                self.timer_actif = False
                return
                
            self.temps_restant -= 1
            self.timer_label.config(text=f"⏱️ Temps: {self.temps_restant}s")
            
            # Changement de couleur selon le temps restant
            if self.temps_restant <= 10:
                self.timer_label.config(fg="#DC2626")  # Rouge
            elif self.temps_restant <= 20:
                self.timer_label.config(fg="#F59E0B")  # Orange
            
            if self.temps_restant > 0:
                self.fenetre_jeu.after(1000, self._mettre_a_jour_timer)
            else:
                self._temps_ecoule()
                
        except Exception as e:
            # Si la fenêtre est fermée, arrêter le timer
            self.timer_actif = False

    def _temps_ecoule(self):
        """Quand le temps est écoulé"""
        self.timer_actif = False
        self.feedback_label.config(text="⏰ Temps écoulé ! Passage à la question suivante...", 
                                 fg="#DC2626")
        self.fenetre_jeu.after(2000, self._prochaine_question)

    def _mettre_a_jour_progression(self):
        """Met à jour la barre de progression"""
        progression = (self.questions_repondus / self.questions_total) * 100
        self.progress_bar['value'] = progression
        self.progress_label.config(text=f"{self.questions_repondus}/{self.questions_total} questions")

    def _verifier_et_attribuer_badges(self):
        """Vérifie et attribue les badges selon la progression"""
        nouveaux_badges = []
        
        # Badge Débutant
        if self.score >= 100 and "Débutant" not in self.badges_gagnes:
            nouveaux_badges.append("🥉 Mathématicien Débutant")
            self.badges_gagnes.append("Débutant")
        
        # Badge Intermédiaire
        if self.score >= 500 and "Intermédiaire" not in self.badges_gagnes:
            nouveaux_badges.append("🥈 Mathématicien Confirmé")
            self.badges_gagnes.append("Intermédiaire")
        
        # Badge Expert
        if self.score >= 1000 and "Expert" not in self.badges_gagnes:
            nouveaux_badges.append("🥇 Mathématicien Expert")
            self.badges_gagnes.append("Expert")
        
        # Badge Rapidité
        if self.questions_repondus >= 10 and "Rapidité" not in self.badges_gagnes:
            nouveaux_badges.append("⚡ Maître du Timing")
            self.badges_gagnes.append("Rapidité")
        
        # Badge Persévérance
        if self.questions_repondus >= 50 and "Persévérance" not in self.badges_gagnes:
            nouveaux_badges.append("💪 Persévérant Incorruptible")
            self.badges_gagnes.append("Persévérance")
        
        # Mettre à jour l'affichage des badges
        if self.badges_gagnes:
            badges_text = "🎖️ Badges: " + ", ".join(self.badges_gagnes)
            self.badges_label.config(text=badges_text, fg="#10B981")
        
        # Afficher notification pour nouveaux badges
        for badge in nouveaux_badges:
            messagebox.showinfo("🎉 Nouveau Badge Débloqué !", 
                              f"Félicitations ! Tu as débloqué le badge:\n{badge}")

    def _afficher_badges(self):
        """Affiche une fenêtre avec tous les badges"""
        badges_window = Toplevel(self.fenetre_jeu)
        badges_window.title("🎖️ Mes Badges")
        badges_window.geometry("400x300")
        badges_window.configure(bg="#F0F4F8")
        
        Label(badges_window, text="🎖️ MES BADGES", 
              font=("Century Gothic", 18, "bold"), bg="#F0F4F8", fg="#1E40AF").pack(pady=20)
        
        badges_frame = Frame(badges_window, bg="#F0F4F8")
        badges_frame.pack(fill=BOTH, expand=True, padx=20)
        
        # Liste des badges possibles
        tous_badges = [
            ("🥉 Mathématicien Débutant", "Score ≥ 100 points", "Débutant" in self.badges_gagnes),
            ("🥈 Mathématicien Confirmé", "Score ≥ 500 points", "Intermédiaire" in self.badges_gagnes),
            ("🥇 Mathématicien Expert", "Score ≥ 1000 points", "Expert" in self.badges_gagnes),
            ("⚡ Maître du Timing", "Répondre 10 questions", "Rapidité" in self.badges_gagnes),
            ("💪 Persévérant Incorruptible", "Répondre 50 questions", "Persévérance" in self.badges_gagnes),
        ]
        
        for badge, description, obtenu in tous_badges:
            color = "#10B981" if obtenu else "#94A3B8"
            emoji = "✅" if obtenu else "❌"
            
            Label(badges_frame, text=f"{emoji} {badge}", 
                  font=("Century Gothic", 11, "bold" if obtenu else "normal"),
                  bg="#F0F4F8", fg=color).pack(anchor=W, pady=2)
            
            Label(badges_frame, text=f"   {description}", 
                  font=("Century Gothic", 9), bg="#F0F4F8", fg="#64748B").pack(anchor=W, pady=(0, 8))

    def _prochaine_question(self):
        """Passe à la question suivante - version corrigée"""
        self._arreter_timer()
        
        # Vérifier si la fenêtre existe encore
        if not hasattr(self, 'fenetre_jeu') or not self.fenetre_jeu.winfo_exists():
            return
            
        self.feedback_label.config(text="")
        self.reponse_entry.delete(0, END)
        
        # Déterminer le niveau selon le score
        if self.score < 200:
            self.niveau_actuel = "Débutant"
        elif self.score < 600:
            self.niveau_actuel = "Intermédiaire"
        else:
            self.niveau_actuel = "Expert"
        
        questions_niveau = self.questions[self.niveau_actuel]
        
        if questions_niveau:  # Vérifier qu'il y a des questions
            self.question_actuelle = random.choice(questions_niveau)
            
            # Mettre à jour l'interface
            self.question_label.config(text=self.question_actuelle["question"])
            self.niveau_label.config(text=f"📊 Niveau: {self.niveau_actuel}")
            self.points_label.config(text=f"🎯 {self.question_actuelle['points']} points")
            
            # Démarrer le timer
            self._demarrer_timer()
            self.reponse_entry.focus()
            
            # Mettre à jour la progression
            self.questions_repondus += 1
            self._mettre_a_jour_progression()

    def _verifier_reponse(self):
        """Vérifie la réponse avec gestion des types spéciaux"""
        if not self.question_actuelle or not self.timer_actif:
            return

        self._arreter_timer()
        reponse_joueur = self.reponse_entry.get().strip().lower()
        reponse_correcte = self.question_actuelle["reponse"]

        try:
            # Gestion des réponses spéciales
            if reponse_correcte == "indéfini":
                correct = reponse_joueur in ["indéfini", "undefined", "infini", "infinity"]
            elif isinstance(reponse_correcte, str) and '/' in reponse_correcte:
                # Gestion des fractions
                try:
                    reponse_joueur_eval = eval(reponse_joueur)
                    reponse_correcte_eval = eval(reponse_correcte)
                    correct = abs(reponse_joueur_eval - reponse_correcte_eval) < 0.001
                except:
                    correct = False
            else:
                # Réponses numériques normales
                reponse_joueur_num = float(reponse_joueur)
                correct = abs(reponse_joueur_num - reponse_correcte) < 0.001

            if correct:
                points = self.question_actuelle["points"]
                # Bonus de rapidité
                if self.temps_restant > 20:
                    points += 5
                    bonus_text = " (+5 bonus rapidité!)"
                elif self.temps_restant > 10:
                    points += 2
                    bonus_text = " (+2 bonus rapidité!)"
                else:
                    bonus_text = ""
                
                self.score += points
                self.score_label.config(text=f"🏆 Score: {self.score}")
                self.feedback_label.config(text=f"✅ Correct ! +{points} points{bonus_text}", fg="#10B981")
            else:
                self.feedback_label.config(text=f"❌ Incorrect. Réponse: {reponse_correcte}", fg="#DC2626")

            # Vérifier les badges
            self._verifier_et_attribuer_badges()

            # Question suivante après délai
            self.fenetre_jeu.after(2500, self._prochaine_question)

        except ValueError:
            self.feedback_label.config(text="❌ Entrez une réponse valide", fg="#DC2626")
            self.fenetre_jeu.after(1500, self._prochaine_question)

# =============================================================================
# COURSE AUX NOMBRES
# =============================================================================

class CourseAuxNombres:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = "Facile"
        self.cible_actuelle = None
        self.nombres_actuels = []
        self.solutions_trouvees = []
        self.temps_debut = None
        self.temps_limite = 120  # 2 minutes par défi
        
    def lancer_jeu(self):
        """Lance le jeu Course aux Nombres"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🏆 Course aux Nombres")
        self.fenetre_jeu.geometry("800x700")
        self.fenetre_jeu.configure(bg="#F0F4F8")
        self.fenetre_jeu.protocol("WM_DELETE_WINDOW", self._fermer_jeu)
        
        self._creer_interface()
        self._nouveau_defi()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg="#1E40AF")
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🏆 COURSE AUX NOMBRES", 
              font=("Century Gothic", 20, "bold"), bg="#1E40AF", fg="white").pack(pady=15)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        self.score_label = Label(stats_frame, text=f"🎯 Score: {self.score}",
                                font=("Century Gothic", 14, "bold"), bg="#F0F4F8", fg="#1E40AF")
        self.score_label.pack(side=LEFT, padx=20)
        
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 12), bg="#F0F4F8", fg="#64748B")
        self.niveau_label.pack(side=LEFT, padx=20)
        
        self.timer_label = Label(stats_frame, text=f"⏱️ Temps: {self.temps_limite}s",
                                font=("Century Gothic", 12, "bold"), bg="#F0F4F8", fg="#DC2626")
        self.timer_label.pack(side=RIGHT, padx=20)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("course_nombres", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Cible
        cible_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        cible_frame.pack(fill=X, padx=20, pady=20)
        
        Label(cible_frame, text="🎯 CIBLE À ATTEINDRE:", 
              font=("Century Gothic", 14, "bold"), bg="#F0F4F8").pack(pady=5)
        
        self.cible_label = Label(cible_frame, text="", 
                                font=("Century Gothic", 40, "bold"), bg="#F0F4F8", fg="#DC2626")
        self.cible_label.pack(pady=10)

        # Nombres disponibles
        nombres_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        nombres_frame.pack(fill=X, padx=20, pady=15)
        
        Label(nombres_frame, text="🔢 NOMBRES DISPONIBLES:", 
              font=("Century Gothic", 12, "bold"), bg="#F0F4F8").pack(pady=5)
        
        self.nombres_frame = Frame(nombres_frame, bg="#F0F4F8")
        self.nombres_frame.pack(pady=10)

        # Zone de saisie
        saisie_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        saisie_frame.pack(fill=X, padx=20, pady=20)
        
        Label(saisie_frame, text="🧮 TON CALCUL:", 
              font=("Century Gothic", 12, "bold"), bg="#F0F4F8").pack(pady=5)
        
        self.calcul_entry = Entry(saisie_frame, font=("Century Gothic", 16), 
                                 width=30, justify="center")
        self.calcul_entry.pack(pady=10)
        self.calcul_entry.bind("<Return>", lambda e: self._verifier_calcul())
        
        # Exemple
        Label(saisie_frame, text="Exemple: (5 + 3) * 2", 
              font=("Century Gothic", 10), bg="#F0F4F8", fg="#64748B").pack()

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        buttons_frame.pack(fill=X, padx=20, pady=15)
        
        ttk.Button(buttons_frame, text="✅ Vérifier le calcul", 
                  command=self._verifier_calcul).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouveau défi", 
                  command=self._nouveau_defi).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Voir solutions", 
                  command=self._afficher_solutions).pack(side=RIGHT, padx=10)

        # Solutions trouvées
        solutions_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        solutions_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)
        
        Label(solutions_frame, text="✅ SOLUTIONS TROUVÉES:", 
              font=("Century Gothic", 11, "bold"), bg="#F0F4F8").pack(anchor=W)
        
        self.solutions_text = Text(solutions_frame, height=6, font=("Century Gothic", 10),
                                  bg="#F8FAFC", fg="#1E293B", wrap=WORD)
        scrollbar = Scrollbar(solutions_frame, command=self.solutions_text.yview)
        self.solutions_text.config(yscrollcommand=scrollbar.set)
        self.solutions_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", 
                                   font=("Century Gothic", 12), bg="#F0F4F8")
        self.feedback_label.pack(pady=10)

    def _generer_defi(self):
        """Génère un nouveau défi selon le niveau"""
        if self.niveau == "Facile":
            self.cible_actuelle = random.randint(10, 50)
            self.nombres_actuels = [random.randint(1, 10) for _ in range(4)]
        elif self.niveau == "Moyen":
            self.cible_actuelle = random.randint(20, 100)
            self.nombres_actuels = [random.randint(1, 15) for _ in range(5)]
        else:  # Difficile
            self.cible_actuelle = random.randint(50, 200)
            self.nombres_actuels = [random.randint(1, 20) for _ in range(6)]
            
        self.solutions_trouvees = []

    def _afficher_nombres(self):
        """Affiche les nombres disponibles"""
        # Nettoyer le frame
        for widget in self.nombres_frame.winfo_children():
            widget.destroy()
            
        # Afficher chaque nombre
        for i, nombre in enumerate(self.nombres_actuels):
            Label(self.nombres_frame, text=str(nombre), 
                  font=("Century Gothic", 20, "bold"), 
                  bg="#3B82F6", fg="white", 
                  width=4, height=2, relief="raised",
                  borderwidth=2).grid(row=0, column=i, padx=10)

    def _nouveau_defi(self):
        """Prépare un nouveau défi"""
        self._generer_defi()
        self.cible_label.config(text=str(self.cible_actuelle))
        self._afficher_nombres()
        self.calcul_entry.delete(0, END)
        self.solutions_text.delete(1.0, END)
        self.feedback_label.config(text="")
        
        # Mettre à jour le niveau selon le score
        if self.score < 100:
            self.niveau = "Facile"
        elif self.score < 300:
            self.niveau = "Moyen"
        else:
            self.niveau = "Difficile"
            
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau}")
        
        # Démarrer le timer
        self._demarrer_timer()

    def _demarrer_timer(self):
        """Démarre le compte à rebours"""
        self.temps_restant = self.temps_limite
        self._mettre_a_jour_timer()

    def _mettre_a_jour_timer(self):
        """Met à jour le timer"""
        if hasattr(self, 'fenetre_jeu') and self.fenetre_jeu.winfo_exists():
            if self.temps_restant > 0:
                self.temps_restant -= 1
                self.timer_label.config(text=f"⏱️ Temps: {self.temps_restant}s")
                
                # Changement de couleur
                if self.temps_restant <= 30:
                    self.timer_label.config(fg="#DC2626")
                elif self.temps_restant <= 60:
                    self.timer_label.config(fg="#F59E0B")
                    
                self.fenetre_jeu.after(1000, self._mettre_a_jour_timer)
            else:
                self._temps_ecoule()

    def _temps_ecoule(self):
        """Quand le temps est écoulé"""
        self.feedback_label.config(text="⏰ Temps écoulé ! Nouveau défi...", fg="#DC2626")
        self.fenetre_jeu.after(2000, self._nouveau_defi)

    def _verifier_calcul(self):
        """Vérifie le calcul du joueur"""
        calcul = self.calcul_entry.get().strip()
        
        if not calcul:
            self.feedback_label.config(text="❌ Entre un calcul", fg="#DC2626")
            return
            
        try:
            # Vérifier que seuls les nombres autorisés sont utilisés
            nombres_utilises = self._extraire_nombres(calcul)
            if not self._verifier_nombres_autorises(nombres_utilises):
                self.feedback_label.config(text="❌ Utilise seulement les nombres donnés", fg="#DC2626")
                return
            
            # Évaluer le résultat
            resultat = eval(calcul)
            
            if abs(resultat - self.cible_actuelle) < 0.001:  # Tolérance pour les floats
                if calcul not in self.solutions_trouvees:
                    # Calculer les points
                    points = self._calculer_points(calcul)
                    self.score += points
                    self.score_label.config(text=f"🎯 Score: {self.score}")
                    
                    self.solutions_trouvees.append(calcul)
                    self._afficher_solution(calcul, points)
                    
                    self.feedback_label.config(text=f"✅ Bravo ! +{points} points", fg="#10B981")
                    self.calcul_entry.delete(0, END)
                    
                    # Nouveau défi après 3 solutions ou 10 secondes
                    if len(self.solutions_trouvees) >= 3:
                        self.fenetre_jeu.after(2000, self._nouveau_defi)
                else:
                    self.feedback_label.config(text="⚠️ Solution déjà trouvée", fg="#F59E0B")
            else:
                self.feedback_label.config(text=f"❌ Résultat: {resultat}, cible: {self.cible_actuelle}", fg="#DC2626")
                
        except Exception as e:
            self.feedback_label.config(text="❌ Calcul invalide", fg="#DC2626")

    def _extraire_nombres(self, calcul):
        """Extrait les nombres utilisés dans le calcul"""
        # Supprimer les opérateurs et parenthèses, puis extraire les nombres
        import re
        nombres = re.findall(r'\d+\.?\d*', calcul)
        return [float(n) if '.' in n else int(n) for n in nombres]

    def _verifier_nombres_autorises(self, nombres_utilises):
        """Vérifie que seuls les nombres autorisés sont utilisés"""
        nombres_disponibles = self.nombres_actuels.copy()
        
        for nombre in nombres_utilises:
            if nombre in nombres_disponibles:
                nombres_disponibles.remove(nombre)
            else:
                return False
        return True

    def _calculer_points(self, calcul):
        """Calcule les points selon la complexité"""
        points_base = 10
        
        # Bonus pour complexité
        if '(' in calcul:
            points_base += 5
        if calcul.count('+') + calcul.count('-') + calcul.count('*') + calcul.count('/') > 2:
            points_base += 5
        if '/' in calcul:
            points_base += 3
            
        # Multiplicateur de niveau
        multiplicateur = {"Facile": 1, "Moyen": 2, "Difficile": 3}
        
        return points_base * multiplicateur[self.niveau]

    def _afficher_solution(self, calcul, points):
        """Affiche une solution trouvée"""
        self.solutions_text.insert(END, f"• {calcul} = {self.cible_actuelle} (+{points} pts)\n")
        self.solutions_text.see(END)

    def _afficher_solutions(self):
        """Affiche quelques solutions possibles"""
        solutions = self._trouver_solutions_simples()
        
        if solutions:
            message = "Quelques solutions possibles :\n\n"
            for i, sol in enumerate(solutions[:3], 1):
                message += f"{i}. {sol}\n"
            messagebox.showinfo("💡 Solutions possibles", message)
        else:
            messagebox.showinfo("💡 Astuce", "Essaye différentes combinaisons d'opérations !")

    def _trouver_solutions_simples(self):
        """Trouve quelques solutions simples (version basique)"""
        solutions = []
        nombres = self.nombres_actuels
        
        # Quelques combinaisons simples
        operations = ['+', '-', '*', '/']
        
        # Essaie quelques combinaisons aléatoires
        for _ in range(50):
            random.shuffle(nombres)
            for op1 in operations:
                for op2 in operations:
                    if len(nombres) >= 3:
                        calcul = f"({nombres[0]} {op1} {nombres[1]}) {op2} {nombres[2]}"
                        try:
                            if abs(eval(calcul) - self.cible_actuelle) < 0.001:
                                solutions.append(calcul)
                        except:
                            pass
        return solutions

    def _fermer_jeu(self):
        """Ferme proprement le jeu"""
        if hasattr(self, 'fenetre_jeu'):
            self.fenetre_jeu.destroy()

# =============================================================================
# MATH EMOJI
# =============================================================================

class MathEmoji:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = "Facile"
        self.equation_actuelle = None
        self.reponses_correctes = {}
        self.emoji_sets = self._preparer_emojis()
        
    def _preparer_emojis(self):
        """Prépare les différents sets d'emojis"""
        return {
            "Fruits": ["🍎", "🍌", "🍒", "🍇", "🍊", "🍋", "🍉", "🍓"],
            "Animaux": ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"],
            "Sports": ["⚽", "🏀", "🏈", "⚾", "🎾", "🏐", "🎯", "🏓"],
            "Transports": ["🚗", "🚕", "🚙", "🚌", "🚎", "🏎️", "🚓", "🚑"],
            "Nourriture": ["🍕", "🍔", "🍟", "🌭", "🍿", "🧁", "🍫", "🍩"]
        }

    def lancer_jeu(self):
        """Lance le jeu Math Emoji"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🍎 Math Emoji")
        self.fenetre_jeu.geometry("700x600")
        self.fenetre_jeu.configure(bg="#F0F4F8")
        
        self._creer_interface()
        self._nouvelle_equation()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg="#FF6B6B")
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🍎 MATH EMOJI 🍌", 
              font=("Comic Sans MS", 22, "bold"), bg="#FF6B6B", fg="white").pack(pady=15)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        self.score_label = Label(stats_frame, text=f"🏆 Score: {self.score}",
                                font=("Arial", 14, "bold"), bg="#F0F4F8", fg="#1E40AF")
        self.score_label.pack(side=LEFT, padx=20)
        
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau}",
                                 font=("Arial", 12), bg="#F0F4F8", fg="#64748B")
        self.niveau_label.pack(side=LEFT, padx=20)

        # Catégorie
        self.categorie_label = Label(stats_frame, text=f"🎨 Catégorie: Fruits",
                                    font=("Arial", 12), bg="#F0F4F8", fg="#8B5CF6")
        self.categorie_label.pack(side=RIGHT, padx=20)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("math_emoji", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Équations
        equations_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        equations_frame.pack(fill=X, padx=30, pady=20)
        
        Label(equations_frame, text="🧮 RÉSOUS CES ÉQUATIONS :", 
              font=("Arial", 14, "bold"), bg="#F0F4F8").pack(pady=10)
        
        self.equations_text = Text(equations_frame, height=4, font=("Arial", 16),
                                  bg="#FFF9C4", fg="#1E293B", wrap=WORD, 
                                  relief="solid", borderwidth=1)
        self.equations_text.pack(fill=X, pady=10)
        self.equations_text.config(state=DISABLED)

        # Zone de réponses
        reponses_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        reponses_frame.pack(fill=X, padx=30, pady=15)
        
        Label(reponses_frame, text="✏️ TES RÉPONSES :", 
              font=("Arial", 12, "bold"), bg="#F0F4F8").pack(pady=10)
        
        self.reponses_frame = Frame(reponses_frame, bg="#F0F4F8")
        self.reponses_frame.pack(pady=10)

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg="#F0F4F8")
        buttons_frame.pack(fill=X, padx=30, pady=20)
        
        ttk.Button(buttons_frame, text="✅ Vérifier les réponses", 
                  command=self._verifier_reponses, style="Accent.TButton").pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouvelle équation", 
                  command=self._nouvelle_equation).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Indice", 
                  command=self._donner_indice).pack(side=RIGHT, padx=10)

        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", 
                                   font=("Arial", 13), bg="#F0F4F8", wraplength=500)
        self.feedback_label.pack(pady=15)

        # Style pour le bouton accent
        style = ttk.Style()
        style.configure("Accent.TButton", foreground="white", background="#4CAF50")

    def _generer_equation(self):
        """Génère une nouvelle équation avec emojis"""
        # Choisir une catégorie aléatoire
        categorie = random.choice(list(self.emoji_sets.keys()))
        emojis = random.sample(self.emoji_sets[categorie], 2)
        
        # Générer des valeurs selon le niveau
        if self.niveau == "Facile":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        elif self.niveau == "Moyen":
            a = random.randint(5, 20)
            b = random.randint(1, 15)
        else:  # Difficile
            a = random.randint(10, 30)
            b = random.randint(5, 25)
        
        # Types d'équations possibles
        types_equations = [
            # Système d'équations
            {
                "type": "systeme",
                "equations": [
                    f"{emojis[0]} + {emojis[1]} = {a + b}",
                    f"{emojis[0]} - {emojis[1]} = {a - b}"
                ],
                "solutions": {emojis[0]: a, emojis[1]: b}
            },
            # Multiplication
            {
                "type": "multiplication", 
                "equations": [
                    f"{emojis[0]} × {emojis[1]} = {a * b}",
                    f"{emojis[0]} + {emojis[1]} = {a + b}"
                ],
                "solutions": {emojis[0]: a, emojis[1]: b}
            },
            # Avec trois emojis
            {
                "type": "trois_emojis",
                "equations": [
                    f"{emojis[0]} + {emojis[1]} = {a + b}",
                    f"{emojis[0]} + {emojis[1]} + {emojis[0]} = {2*a + b}"
                ],
                "solutions": {emojis[0]: a, emojis[1]: b}
            }
        ]
        
        equation_choisie = random.choice(types_equations)
        equation_choisie["categorie"] = categorie
        equation_choisie["emojis"] = emojis
        
        return equation_choisie

    def _nouvelle_equation(self):
        """Prépare une nouvelle équation"""
        self.equation_actuelle = self._generer_equation()
        self.reponses_correctes = self.equation_actuelle["solutions"]
        
        # Mettre à jour l'interface
        self._afficher_equations()
        self._creer_zones_reponse()
        self.feedback_label.config(text="")
        
        # Mettre à jour la catégorie
        self.categorie_label.config(text=f"🎨 Catégorie: {self.equation_actuelle['categorie']}")
        
        # Mettre à jour le niveau selon le score
        if self.score < 50:
            self.niveau = "Facile"
        elif self.score < 150:
            self.niveau = "Moyen"
        else:
            self.niveau = "Difficile"
            
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau}")

    def _afficher_equations(self):
        """Affiche les équations dans la zone de texte"""
        self.equations_text.config(state=NORMAL)
        self.equations_text.delete(1.0, END)
        
        for i, equation in enumerate(self.equation_actuelle["equations"]):
            self.equations_text.insert(END, f"Équation {i+1}: {equation}\n")
        
        self.equations_text.config(state=DISABLED)

    def _creer_zones_reponse(self):
        """Crée les zones de saisie pour chaque emoji"""
        # Nettoyer le frame
        for widget in self.reponses_frame.winfo_children():
            widget.destroy()
        
        emojis = list(self.reponses_correctes.keys())
        
        for i, emoji in enumerate(emojis):
            ligne_frame = Frame(self.reponses_frame, bg="#F0F4F8")
            ligne_frame.grid(row=i, column=0, sticky="w", pady=8)
            
            Label(ligne_frame, text=f"{emoji} = ", 
                  font=("Arial", 16), bg="#F0F4F8").pack(side=LEFT, padx=(0, 10))
            
            entry = Entry(ligne_frame, font=("Arial", 14), width=8, justify="center")
            entry.pack(side=LEFT)
            entry.emoji = emoji  # Stocker l'emoji associé

    def _verifier_reponses(self):
        """Vérifie les réponses du joueur"""
        try:
            toutes_correctes = True
            reponses_obtenues = {}
            
            # Récupérer toutes les réponses
            for widget in self.reponses_frame.winfo_children():
                for child in widget.winfo_children():
                    if isinstance(child, Entry):
                        emoji = getattr(child, 'emoji', None)
                        if emoji:
                            try:
                                reponse = int(child.get().strip())
                                reponses_obtenues[emoji] = reponse
                                
                                # Vérifier si correct
                                if reponse == self.reponses_correctes[emoji]:
                                    child.config(bg="#C8E6C9")  # Vert si correct
                                else:
                                    child.config(bg="#FFCDD2")  # Rouge si incorrect
                                    toutes_correctes = False
                                    
                            except ValueError:
                                child.config(bg="#FFCDD2")
                                toutes_correctes = False
            
            if toutes_correctes and len(reponses_obtenues) == len(self.reponses_correctes):
                # Calculer les points
                points = self._calculer_points()
                self.score += points
                self.score_label.config(text=f"🏆 Score: {self.score}")
                
                self.feedback_label.config(
                    text=f"🎉 Excellent ! Toutes bonnes réponses ! +{points} points", 
                    fg="#10B981"
                )
                
                # Nouvelle équation après délai
                self.fenetre_jeu.after(2000, self._nouvelle_equation)
                
            else:
                self.feedback_label.config(
                    text="❌ Certaines réponses sont incorrectes. Essaie encore !", 
                    fg="#DC2626"
                )
                
        except Exception as e:
            self.feedback_label.config(text="❌ Erreur de saisie", fg="#DC2626")

    def _calculer_points(self):
        """Calcule les points selon la difficulté"""
        points_base = 10
        multiplicateur = {"Facile": 1, "Moyen": 2, "Difficile": 3}
        
        # Bonus pour type d'équation
        if self.equation_actuelle["type"] == "systeme":
            points_base += 5
        elif self.equation_actuelle["type"] == "trois_emojis":
            points_base += 8
            
        return points_base * multiplicateur[self.niveau]

    def _donner_indice(self):
        """Donne un indice au joueur"""
        if not self.equation_actuelle:
            return
            
        emojis = list(self.reponses_correctes.keys())
        emoji_indice = random.choice(emojis)
        valeur = self.reponses_correctes[emoji_indice]
        
        # Pénalité de points pour l'indice
        penalite = 3
        self.score = max(0, self.score - penalite)
        self.score_label.config(text=f"🏆 Score: {self.score}")
        
        messagebox.showinfo(
            "💡 Indice", 
            f"Petit coup de pouce :\n{emoji_indice} = {valeur}\n\n(–{penalite} points)"
        )

# =============================================================================
# FONCTIONS D'ACCÈS UNIFIÉES
# =============================================================================

def lancer_math_emoji(parent=None):
    """Lance le jeu Math Emoji"""
    jeu = MathEmoji(parent)
    jeu.lancer_jeu()

def lancer_math_quizz(parent=None):
    """Lance le Math Quizz Challenge amélioré"""
    jeu = MathQuizzChallenge(parent)
    jeu.lancer_jeu()

def lancer_course_nombres(parent=None):
    """Lance la Course aux Nombres"""
    jeu = CourseAuxNombres(parent)
    jeu.lancer_jeu()

def lancer_sudoku_math(parent=None):
    """Lance le Sudoku Mathématique (placeholder)"""
    messagebox.showinfo("Prochainement", "Sudoku Mathématique - Bientôt disponible!\n\nGuide : Résolvez des grilles où les cases contiennent des opérations mathématiques au lieu de chiffres.")

def lancer_bataille_fractions(parent=None):
    """Lance la Bataille des Fractions (placeholder)"""
    messagebox.showinfo("Prochainement", "Bataille des Fractions - Bientôt disponible!\n\nGuide : Comparez des fractions pour gagner des cartes. Maîtrisez les équivalences et simplifications!")

# =============================================================================
# LISTE DES JEUX DISPONIBLES (pour l'interface)
# =============================================================================

JEUX_DISPONIBLES = [
    {
        "nom": "🎯 Math Quizz Challenge PRO",
        "description": "300 questions + Timer + Badges + Progression\n• Questions adaptatives selon votre niveau\n• Système de badges et récompenses\n• Timer avec bonus de rapidité",
        "fonction": lancer_math_quizz,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("math_quizz", parent)
    },
    {
        "nom": "🏆 Course aux Nombres", 
        "description": "Atteins la cible avec les nombres donnés\n• Utilisez + - × ÷ et parenthèses\n• Plusieurs solutions possibles par défi\n• Points bonus pour solutions complexes",
        "fonction": lancer_course_nombres,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("course_nombres", parent)
    },
    {
        "nom": "🍎 Math Emoji",
        "description": "Résoudre des équations avec des emojis\n• Systèmes d'équations amusants\n• Catégories variées (fruits, animaux, sports)\n• Méthodes algébriques à découvrir",
        "fonction": lancer_math_emoji,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("math_emoji", parent)
    },
    {
        "nom": "🧩 Sudoku Mathématique",
        "description": "Grilles avec opérations au lieu de chiffres\n• Combinaison de logique et calcul\n• Niveaux de difficulté progressifs\n• Perfect pour la réflexion stratégique",
        "fonction": lancer_sudoku_math,
        "disponible": False
    },
    {
        "nom": "⚡ Bataille des Fractions", 
        "description": "Compare et gagne des cartes\n• Maîtrise des fractions et équivalences\n• Jeu compétitif à deux joueurs\n• Apprentissage des comparaisons",
        "fonction": lancer_bataille_fractions,
        "disponible": False
    }
]

# Pour tester directement
if __name__ == "__main__":
    fenetre = creer_interface_jeux()
    fenetre.mainloop()