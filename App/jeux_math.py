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

# Palette unifiée (identique aux autres fichiers)
PALETTE = {
    "fond_principal": "#F0F4F8",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6", 
    "erreur": "#DC2626",
    "texte_fonce": "#1E40AF",
    "texte_clair": "#1E40AF"
}

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
            "Débutant : 7 × 8 = ? → 56",
            "Intermédiaire : √144 = ? → 12",
            "Expert : sin(π/2) = ? → 1"
        ]
    },
     "bataille_fractions": {
        "titre": "🎲 Guide de la Bataille des Fractions",
        "contenu": [
            "🎯 **Concept du jeu :**",
            "Jeu de bataille classique adapté aux fractions !",
            "Affronte l'ordinateur en comparant des fractions.",
            "La plus grande fraction remporte la manche.",
            "",
            "📝 **Comment jouer :**",
            "• Chaque joueur reçoit 10 cartes fractions",
            "• À chaque tour, choisis une carte de ta main", 
            "• L'ordinateur joue une carte au hasard",
            "• La plus grande fraction gagne la manche",
            "• La partie se termine quand un joueur n'a plus de cartes",
            "",
            "🎮 **Niveaux de difficulté :**",
            "• Facile : Fractions simples (dénominateurs 2,3,4,6,8)",
            "• Moyen : Fractions variées (dénominateurs jusqu'à 12)",
            "• Difficile : Fractions complexes et impropres",
            "",
            "🏅 **Système de points :**",
            "• Victoire simple : 10 points × multiplicateur niveau",
            "• Bonus fraction simplifiée : +5 points",
            "• Bonus choix stratégique (petite différence) : +8 points",
            "• Bonus victoire partie : +50 points",
            "• Multiplicateurs : Facile×1, Moyen×2, Difficile×3",
            "",
            "💡 **Stratégies gagnantes :**",
            "• Apprenez les équivalences de fractions courantes",
            "• Gardez les grosses fractions pour les manches cruciales",
            "• Utilisez la multiplication en croix pour comparer vite",
            "• Mémorisez les valeurs décimales des fractions usuelles",
            "• Simplifiez mentalement les fractions complexes"
        ],
        "exemples": [
            "🧮 **Exemples de comparaisons :**",
            "",
            "Facile :",
            "• 1/2 vs 1/3 → 0.5 > 0.33 → 1/2 gagne",
            "• 2/3 vs 3/4 → 0.66 < 0.75 → 3/4 gagne", 
            "• 3/4 vs 5/8 → 0.75 > 0.625 → 3/4 gagne",
            "",
            "Moyen :",
            "• 4/5 vs 7/10 → 0.8 > 0.7 → 4/5 gagne",
            "• 5/6 vs 8/12 → 0.83 > 0.66 → 5/6 gagne",
            "• 3/8 vs 2/5 → 0.375 < 0.4 → 2/5 gagne",
            "",
            "Difficile :",
            "• 7/8 vs 11/12 → 0.875 < 0.916 → 11/12 gagne",
            "• 5/4 vs 6/5 → 1.25 > 1.2 → 5/4 gagne",
            "• 9/16 vs 3/5 → 0.5625 < 0.6 → 3/5 gagne",
            "",
            "⚔️ **Techniques de comparaison :**",
            "Multiplication en croix :",
            "2/3 vs 3/4 → 2×4=8 vs 3×3=9 → 3/4 gagne",
            "5/6 vs 7/8 → 5×8=40 vs 7×6=42 → 7/8 gagne"
        ]
    },
    "dessine_fonction": {
        "titre": "📈 Guide de Dessine-moi une Fonction",
        "contenu": [
            "🎯 **Concept du jeu :**",
            "Jeu de reconnaissance visuelle de fonctions mathématiques !",
            "Observe les points de référence et trace la fonction correspondante.",
            "",
            "📝 **Comment jouer :**",
            "• Une fonction mathématique est donnée",
            "• Des points rouges indiquent des valeurs correctes", 
            "• Clique et glisse pour tracer la fonction",
            "• Plus ton tracé est proche des points, plus tu gagnes de points",
            "• Utilise la grille pour plus de précision",
            "",
            "🎮 **Niveaux de difficulté :**",
            "• Débutant : Fonctions linéaires, constantes, valeur absolue",
            "• Intermédiaire : + fonctions quadratiques, racines carrées",
            "• Avancé : + fonctions cubiques, sinus, formes complexes",
            "",
            "🏅 **Système de points :**",
            "• Points de base : 20 points × multiplicateur niveau",
            "• Bonus précision : Jusqu'à +30 points pour >70% de précision",
            "• Seuil de réussite : 70% de précision minimum",
            "• Multiplicateurs : Débutant×1, Intermédiaire×2, Avancé×3",
            "",
            "💡 **Stratégies gagnantes :**",
            "• Commence par les points évidents (intersections avec les axes)",
            "• Observe la forme générale (droite, courbe, V, etc.)",
            "• Utilise la grille pour estimer les valeurs",
            "• Pour les droites, trouve 2 points et trace la ligne",
            "• Pour les paraboles, trouve le sommet et l'ouverture"
        ],
        "exemples": [
            "📊 **Reconnaître les formes :**",
            "",
            "Fonctions linéaires :",
            "• f(x) = 2x + 1 → Droite qui monte, intersection Y à 1",
            "• f(x) = -x + 3 → Droite qui descend, intersection Y à 3",
            "",
            "Fonctions constantes :", 
            "• f(x) = 4 → Ligne horizontale à y=4",
            "• f(x) = -2 → Ligne horizontale à y=-2",
            "",
            "Valeur absolue :",
            "• f(x) = |x| → Forme en V, minimum à (0,0)",
            "",
            "Fonctions quadratiques :",
            "• f(x) = x² - 2 → Parabole qui ouvre vers le haut, sommet à (0,-2)",
            "• f(x) = -x² + 3 → Parabole qui ouvre vers le bas, sommet à (0,3)",
            "",
            "Fonctions racines :",
            "• f(x) = √(x + 4) → Courbe qui commence à x=-4, croissance lente",
            "",
            "⚠️ **Conseils de précision :**",
            "• Utilise la grille pour mieux estimer les positions",
            "• Trace doucement pour plus de précision",
            "• Vérifie les points de référence régulièrement",
            "• N'hésite pas à effacer et recommencer"
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
            "• Vous avez 2 minutes par défi"
        ],
        "exemples": [
            "🧮 **Exemple :**",
            "Cible : 24, Nombres : [4, 8, 3, 6] → 8 × 3 = 24"
        ]
    },

    "math_emoji": {
        "titre": "🍎 Guide du Math Emoji",
        "contenu": [
            "🎯 **Concept du jeu :**",
            "Résoudre des systèmes d'équations où les inconnues sont des emojis!",
            "Chaque emoji représente un nombre à découvrir."
        ],
        "exemples": [
            "🧮 **Exemple :**",
            "🍎 + 🍌 = 12 ; 🍎 - 🍌 = 4 → 🍎 = 8, 🍌 = 4"
        ]
    },

    "jeu_des_24": {
        "titre": "🎯 Guide du Jeu des 24",
        "contenu": [
            "🎯 **Objectif du jeu :**",
            "Atteindre exactement 24 en utilisant les 4 nombres donnés",
            "avec les opérations +, -, ×, ÷ et des parenthèses.",
            "",
            "📝 **Règles principales :**",
            "• Utilisez les 4 nombres donnés UNE SEULE FOIS chacun",
            "• Les opérations autorisées : + - × ÷ ( )",
            "• Le résultat final doit être EXACTEMENT 24",
            "• Plusieurs solutions possibles pour chaque défi",
            "",
            "🎮 **Niveaux de difficulté :**",
            "• Facile : Nombres de 1 à 10",
            "• Moyen : Nombres de 1 à 13", 
            "• Difficile : Nombres de 1 à 20",
            "",
            "🏅 **Système de points :**",
            "• Points de base : 15 points",
            "• Bonus parenthèses : +5 points",
            "• Bonus opérations multiples : +5 points",
            "• Bonus divisions : +3 points",
            "• Multiplicateur niveau : Facile×1, Moyen×2, Difficile×3"
        ],
        "exemples": [
            "🧮 **Exemples de solutions :**",
            "Avec [3, 3, 8, 8] → 8 ÷ (3 - 8 ÷ 3) = 24",
            "Avec [2, 3, 5, 12] → 12 × (5 - 3) ÷ 2 = 24"
        ]
    },
    "calcul_mental_express": {
        "titre": "🌀 Guide du Calcul Mental Express",
        "contenu": [
            "🎯 **Objectif du jeu :**",
            "Résoudre un maximum de calculs mentalement le plus vite possible !",
            "Développez votre agilité mentale et votre rapidité de calcul.",
            "",
            "📝 **Comment jouer :**",
            "• Une question de calcul s'affiche avec un timer",
            "• Entrez votre réponse et validez avec Entrée ou le bouton",
            "• Plus vous répondez vite, plus vous gagnez de points bonus",
            "• Les streaks rapportent des bonus supplémentaires",
            "",
            "🎮 **Niveaux de difficulté :**",
            "• Débutant : Additions/soustractions (15 secondes)",
            "• Intermédiaire : + multiplications (12 secondes)", 
            "• Expert : + divisions entières (10 secondes)",
            "",
            "🏅 **Système de points :**",
            "• Débutant : 5 points + bonus rapidité",
            "• Intermédiaire : 8 points + bonus rapidité",
            "• Expert : 12 points + bonus rapidité",
            "• Bonus rapidité : Jusqu'à +5 points",
            "• Streak bonus : Points supplémentaires à partir de 5 réponses consécutives",
            "",
            "💡 **Stratégies gagnantes :**",
            "• Entraînez-vous aux tables de multiplication",
            "• Apprenez les astuces de calcul mental",
            "• Ne paniquez pas sous la pression du temps",
            "• Concentrez-vous sur la précision d'abord, la vitesse viendra après"
        ],
        "exemples": [
            "🧮 **Exemples d'entraînement :**",
            "",
            "Pour les additions :",
            "• 17 + 25 = ? → Pensez 17 + 20 = 37, puis 37 + 5 = 42",
            "• 48 + 36 = ? → Pensez 50 + 36 = 86, puis 86 - 2 = 84",
            "",
            "Pour les multiplications :",
            "• 7 × 8 = ? → Table de multiplication classique → 56",
            "• 13 × 5 = ? → Pensez 10×5=50 et 3×5=15, donc 50+15=65",
            "• 16 × 25 = ? → Pensez 4×4×25 = 4×100 = 400",
            "",
            "Pour les divisions :",
            "• 48 ÷ 6 = ? → Table de 6 → 8",
            "• 81 ÷ 9 = ? → Table de 9 → 9",
            "• 144 ÷ 12 = ? → Pensez 12×12=144 donc réponse=12"
        ]
    },
    "sudoku_math": {
        "titre": "🧩 Guide du Sudoku Mathématique",
        "contenu": [
            "🎯 **Concept du jeu :**",
            "Combinaison classique du Sudoku avec des opérations mathématiques !",
            "Résolvez la grille en respectant les règles du Sudoku traditionnel.",
            "",
            "📝 **Règles du Sudoku :**",
            "• Chaque ligne doit contenir les chiffres de 1 à 9 sans répétition",
            "• Chaque colonne doit contenir les chiffres de 1 à 9 sans répétition", 
            "• Chaque région 3x3 doit contenir les chiffres de 1 à 9 sans répétition",
            "• Les cases grisées montrent des opérations à résoudre mentalement",
            "",
            "🎮 **Niveaux de difficulté :**",
            "• Facile : 40 cases vides, opérations simples",
            "• Moyen : 50 cases vides, mélange d'opérations",
            "• Difficile : 60 cases vides, opérations complexes",
            "",
            "🏅 **Système de points :**",
            "• Points de base : 100 points par grille",
            "• Bonus rapidité : Jusqu'à +300 points pour moins de 5 minutes",
            "• Pénalité erreurs : -10 points par erreur",
            "• Multiplicateur niveau : Facile×1, Moyen×2, Difficile×3",
            "• Score minimum garanti : 50 points",
            "",
            "💡 **Stratégies gagnantes :**",
            "• Commencez par les lignes/colonnes/régions les plus remplies",
            "• Utilisez la technique du 'candidat unique'",
            "• Cherchez les paires et triplets cachés",
            "• Résolvez d'abord les opérations simples mentalement",
            "• Vérifiez régulièrement avec le bouton de vérification"
        ],
        "exemples": [
            "🧮 **Exemples d'opérations :**",
            "",
            "Additions :",
            "• '3+5' → 8",
            "• '12+7' → 19 → 1+9=10 → 1+0=1 (chiffre unique)",
            "",
            "Soustractions :", 
            "• '9-4' → 5",
            "• '15-8' → 7",
            "",
            "Multiplications :",
            "• '3×4' → 12 → 1+2=3",
            "• '6×7' → 42 → 4+2=6",
            "",
            "Divisions :",
            "• '20÷5' → 4",
            "• '36÷6' → 6",
            "",
            "⚠️ **Attention :**",
            "Tous les résultats sont réduits à un chiffre de 1 à 9",
            "comme dans le Sudoku traditionnel !"
        ]
    }
}

def lancer_jeu_des_24(parent=None):
    """Lance le Jeu des 24"""
    jeu = JeuDes24(parent)
    jeu.lancer_jeu()

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
    fenetre_guide.configure(bg=PALETTE["fond_principal"])
    
    # Cadre principal avec scrollbar
    main_frame = Frame(fenetre_guide, bg=PALETTE["fond_principal"])
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
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
    
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    # Contenu du guide
    Label(scrollable_frame, text=guide["titre"], 
          font=("Century Gothic", 20, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=20)
    
    # Partie guide
    guide_frame = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    guide_frame.pack(fill=X, pady=10)
    
    for ligne in guide["contenu"]:
        if ligne.startswith("•"):
            Label(guide_frame, text=ligne, font=("Century Gothic", 11), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], justify="left", anchor="w").pack(fill=X, padx=20, pady=1)
        elif ligne.startswith("📝") or ligne.startswith("🎮") or ligne.startswith("🏆") or ligne.startswith("💡"):
            Label(guide_frame, text=ligne, font=("Century Gothic", 12, "bold"), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"], justify="left", anchor="w").pack(fill=X, padx=10, pady=(15,5))
        else:
            Label(guide_frame, text=ligne, font=("Century Gothic", 11), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"], justify="left", anchor="w").pack(fill=X, padx=20, pady=2)
    
    # Séparateur
    ttk.Separator(scrollable_frame, orient='horizontal').pack(fill=X, pady=20)
    
    # Partie exemples
    exemples_frame = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    exemples_frame.pack(fill=X, pady=10)
    
    for ligne in guide["exemples"]:
        if ligne.startswith("🧮"):
            Label(exemples_frame, text=ligne, font=("Century Gothic", 14, "bold"), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"], justify="left", anchor="w").pack(fill=X, padx=10, pady=(10,5))
        elif ligne.startswith("•"):
            Label(exemples_frame, text=ligne, font=("Century Gothic", 11), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"], justify="left", anchor="w").pack(fill=X, padx=25, pady=1)
        elif ligne == "":
            Label(exemples_frame, text=" ", font=("Century Gothic", 4), 
                  bg=PALETTE["fond_principal"]).pack(fill=X, pady=2)
        else:
            Label(exemples_frame, text=ligne, font=("Century Gothic", 11, "italic"), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"], justify="left", anchor="w").pack(fill=X, padx=20, pady=2)
    
    # Bouton fermer
    ttk.Button(scrollable_frame, text="Fermer le guide", 
              command=fenetre_guide.destroy).pack(pady=20)
    
    # Espace final
    Label(scrollable_frame, text="", bg=PALETTE["fond_principal"], height=2).pack()

# =============================================================================
# INTERFACE DE SÉLECTION DES JEUX AVEC SCROLLBAR
# =============================================================================

def creer_interface_jeux(parent=None):
    """Crée l'interface de sélection des jeux avec scrollbar"""
    fenetre_jeux = Toplevel(parent) if parent else Tk()
    fenetre_jeux.title("🎮 MathCraft - Sélection des Jeux")
    fenetre_jeux.geometry("900x800")
    fenetre_jeux.configure(bg=PALETTE["fond_principal"])
    
    # Style
    style = ttk.Style()
    style.configure("Jeu.TButton", 
                   font=("Century Gothic", 12),
                   padding=15,
                   relief="flat")
    
    style.configure("Guide.TButton",
                   font=("Century Gothic", 10),
                   padding=8)
    
    style.configure("Horizontal.TProgressbar", background=PALETTE["primaire"])
    style.configure("Warning.Horizontal.TProgressbar", background="#F59E0B")
    style.configure("Urgent.Horizontal.TProgressbar", background=PALETTE["erreur"])
    
    # En-tête fixe
    header_frame = Frame(fenetre_jeux, bg=PALETTE["primaire"])
    header_frame.pack(fill=X, pady=(0, 10))
    
    Label(header_frame, text="🎮 MATHCRAFT - ESPACE JEUX", 
          font=("Century Gothic", 24, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=20)
    
    Label(header_frame, text="Choisis ton aventure mathématique !", 
          font=("Century Gothic", 14), bg=PALETTE["primaire"], fg="white").pack(pady=(0, 15))
    
    # Cadre principal avec scrollbar
    main_frame = Frame(fenetre_jeux, bg=PALETTE["fond_principal"])
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
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
    
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    # Contenu des jeux
    content_frame = scrollable_frame
    
    # Section jeux disponibles
    Label(content_frame, text="🎯 JEUX DISPONIBLES", 
          font=("Century Gothic", 18, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=20)
    
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
                           bg="white", fg=PALETTE["primaire"], anchor="w")
        titre_label.pack(fill=X)
        
        desc_label = Label(text_frame, text=jeu["description"],
                          font=("Century Gothic", 11),
                          bg="white", fg=PALETTE["texte_clair"], justify="left", anchor="w")
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
    info_frame = Frame(content_frame, bg=PALETTE["secondaire"], relief="solid", borderwidth=1)
    info_frame.pack(fill=X, padx=10, pady=30, ipady=15)
    
    Label(info_frame, text="💡 Informations importantes", 
          font=("Century Gothic", 14, "bold"), bg=PALETTE["secondaire"], fg="white").pack(pady=(0, 10))
    
    infos = [
        "• Chaque jeu propose des défis adaptés à ton niveau",
        "• Consulte les guides pour apprendre les stratégies gagnantes", 
        "• Plus tu joues, plus tu débloques de badges et récompenses",
        "• N'hésite pas à essayer différents jeux pour varier les plaisirs !"
    ]
    
    for info in infos:
        Label(info_frame, text=info, font=("Century Gothic", 10), 
              bg=PALETTE["secondaire"], fg="white", justify="left", anchor="w").pack(fill=X, padx=20, pady=2)
    
    # Bouton fermer
    ttk.Button(content_frame, text="🚪 Fermer", 
              command=fenetre_jeux.destroy,
              style="Jeu.TButton").pack(pady=30)
    
    # Espace final pour le défilement
    Label(content_frame, text="", bg=PALETTE["fond_principal"], height=2).pack()
    
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
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        
        self._creer_interface_avance()
        self._prochaine_question()

    def _creer_interface_avance(self):
        """Crée l'interface avancée avec timer et progression"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🎯 MATH QUIZZ CHALLENGE PRO", 
              font=("Century Gothic", 20, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Frame des statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Score
        self.score_label = Label(stats_frame, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        # Niveau
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau_actuel}",
                                 font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(side=LEFT, padx=20)
        
        # Timer
        self.timer_label = Label(stats_frame, text=f"⏱️ Temps: {self.temps_restant}s",
                                font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.timer_label.pack(side=RIGHT, padx=20)

        # Barre de progression
        progress_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        progress_frame.pack(fill=X, padx=20, pady=10)
        
        Label(progress_frame, text="Progression:", 
              font=("Century Gothic", 10), bg=PALETTE["fond_principal"]).pack(anchor=W)
        
        self.progress_bar = ttk.Progressbar(progress_frame, orient=HORIZONTAL, 
                                           length=600, mode='determinate')
        self.progress_bar.pack(fill=X, pady=5)
        
        self.progress_label = Label(progress_frame, text="0/0 questions",
                                   font=("Century Gothic", 9), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.progress_label.pack(anchor=W)

        # Badges
        self.badges_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        self.badges_frame.pack(fill=X, padx=20, pady=10)
        
        self.badges_label = Label(self.badges_frame, text="🎖️ Badges: Aucun pour le moment",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.badges_label.pack(anchor=W)

        # Bouton guide
        guide_button = ttk.Button(self.badges_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("math_quizz", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Séparateur
        ttk.Separator(self.fenetre_jeu, orient='horizontal').pack(fill=X, padx=20, pady=10)

        # Question
        question_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        question_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        self.question_label = Label(question_frame, text="", font=("Century Gothic", 18, "bold"),
                                   bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], wraplength=600, justify="center")
        self.question_label.pack(pady=30)

        # Réponse
        reponse_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        reponse_frame.pack(fill=X, padx=20, pady=10)
        
        Label(reponse_frame, text="Ta réponse:", 
              font=("Century Gothic", 12), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.reponse_entry = Entry(reponse_frame, font=("Century Gothic", 16), 
                                  width=20, justify="center")
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse())

        # Points de la question
        self.points_label = Label(reponse_frame, text="", 
                                 font=("Century Gothic", 11), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.points_label.pack()

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=20, pady=20)
        
        ttk.Button(buttons_frame, text="✅ Vérifier la réponse", 
                  command=self._verifier_reponse).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="➡️ Question suivante", 
                  command=self._prochaine_question).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="📊 Voir les badges", 
                  command=self._afficher_badges).pack(side=RIGHT, padx=10)

        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", font=("Century Gothic", 13), 
                                   bg=PALETTE["fond_principal"], wraplength=500)
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
                self.timer_label.config(fg=PALETTE["erreur"])  # Rouge
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
                                 fg=PALETTE["erreur"])
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
        badges_window.configure(bg=PALETTE["fond_principal"])
        
        Label(badges_window, text="🎖️ MES BADGES", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=20)
        
        badges_frame = Frame(badges_window, bg=PALETTE["fond_principal"])
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
                  bg=PALETTE["fond_principal"], fg=color).pack(anchor=W, pady=2)
            
            Label(badges_frame, text=f"   {description}", 
                  font=("Century Gothic", 9), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack(anchor=W, pady=(0, 8))

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
                self.feedback_label.config(text=f"❌ Incorrect. Réponse: {reponse_correcte}", fg=PALETTE["erreur"])

            # Vérifier les badges
            self._verifier_et_attribuer_badges()

            # Question suivante après délai
            self.fenetre_jeu.after(2500, self._prochaine_question)

        except ValueError:
            self.feedback_label.config(text="❌ Entrez une réponse valide", fg=PALETTE["erreur"])
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
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        self.fenetre_jeu.protocol("WM_DELETE_WINDOW", self._fermer_jeu)
        
        self._creer_interface()
        self._nouveau_defi()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🏆 COURSE AUX NOMBRES", 
              font=("Century Gothic", 20, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        self.score_label = Label(stats_frame, text=f"🎯 Score: {self.score}",
                                font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(side=LEFT, padx=20)
        
        self.timer_label = Label(stats_frame, text=f"⏱️ Temps: {self.temps_limite}s",
                                font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.timer_label.pack(side=RIGHT, padx=20)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("course_nombres", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Cible
        cible_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        cible_frame.pack(fill=X, padx=20, pady=20)
        
        Label(cible_frame, text="🎯 CIBLE À ATTEINDRE:", 
              font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.cible_label = Label(cible_frame, text="", 
                                font=("Century Gothic", 40, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.cible_label.pack(pady=10)

        # Nombres disponibles
        nombres_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        nombres_frame.pack(fill=X, padx=20, pady=15)
        
        Label(nombres_frame, text="🔢 NOMBRES DISPONIBLES:", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.nombres_frame = Frame(nombres_frame, bg=PALETTE["fond_principal"])
        self.nombres_frame.pack(pady=10)

        # Zone de saisie
        saisie_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        saisie_frame.pack(fill=X, padx=20, pady=20)
        
        Label(saisie_frame, text="🧮 TON CALCUL:", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.calcul_entry = Entry(saisie_frame, font=("Century Gothic", 16), 
                                 width=30, justify="center")
        self.calcul_entry.pack(pady=10)
        self.calcul_entry.bind("<Return>", lambda e: self._verifier_calcul())
        
        # Exemple
        Label(saisie_frame, text="Exemple: (5 + 3) * 2", 
              font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack()

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=20, pady=15)
        
        ttk.Button(buttons_frame, text="✅ Vérifier le calcul", 
                  command=self._verifier_calcul).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouveau défi", 
                  command=self._nouveau_defi).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Voir solutions", 
                  command=self._afficher_solutions).pack(side=RIGHT, padx=10)

        # Solutions trouvées
        solutions_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        solutions_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)
        
        Label(solutions_frame, text="✅ SOLUTIONS TROUVÉES:", 
              font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"]).pack(anchor=W)
        
        self.solutions_text = Text(solutions_frame, height=6, font=("Century Gothic", 10),
                                  bg="#F8FAFC", fg=PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(solutions_frame, command=self.solutions_text.yview)
        self.solutions_text.config(yscrollcommand=scrollbar.set)
        self.solutions_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", 
                                   font=("Century Gothic", 12), bg=PALETTE["fond_principal"])
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
                  bg=PALETTE["secondaire"], fg="white", 
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
                    self.timer_label.config(fg=PALETTE["erreur"])
                elif self.temps_restant <= 60:
                    self.timer_label.config(fg="#F59E0B")
                    
                self.fenetre_jeu.after(1000, self._mettre_a_jour_timer)
            else:
                self._temps_ecoule()

    def _temps_ecoule(self):
        """Quand le temps est écoulé"""
        self.feedback_label.config(text="⏰ Temps écoulé ! Nouveau défi...", fg=PALETTE["erreur"])
        self.fenetre_jeu.after(2000, self._nouveau_defi)

    def _verifier_calcul(self):
        """Vérifie le calcul du joueur"""
        calcul = self.calcul_entry.get().strip()
        
        if not calcul:
            self.feedback_label.config(text="❌ Entre un calcul", fg=PALETTE["erreur"])
            return
            
        try:
            # Vérifier que seuls les nombres autorisés sont utilisés
            nombres_utilises = self._extraire_nombres(calcul)
            if not self._verifier_nombres_autorises(nombres_utilises):
                self.feedback_label.config(text="❌ Utilise seulement les nombres donnés", fg=PALETTE["erreur"])
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
                self.feedback_label.config(text=f"❌ Résultat: {resultat}, cible: {self.cible_actuelle}", fg=PALETTE["erreur"])
                
        except Exception as e:
            self.feedback_label.config(text="❌ Calcul invalide", fg=PALETTE["erreur"])

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
# JEU DES 24
# =============================================================================

class JeuDes24:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = "Facile"
        self.nombres_actuels = []
        self.solutions_trouvees = []
        
    def lancer_jeu(self):
        """Lance le Jeu des 24"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🎯 Le Jeu des 24")
        self.fenetre_jeu.geometry("700x600")
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        
        self._creer_interface()
        self._nouveau_defi()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🎯 LE JEU DES 24", 
              font=("Century Gothic", 20, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        self.score_label = Label(stats_frame, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(side=LEFT, padx=20)

        # Cible fixe (toujours 24)
        cible_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        cible_frame.pack(fill=X, padx=20, pady=20)
        
        Label(cible_frame, text="🎯 CIBLE À ATTEINDRE:", 
              font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.cible_label = Label(cible_frame, text="24", 
                                font=("Century Gothic", 40, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.cible_label.pack(pady=10)

        # Nombres disponibles
        nombres_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        nombres_frame.pack(fill=X, padx=20, pady=15)
        
        Label(nombres_frame, text="🔢 NOMBRES DISPONIBLES:", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.nombres_frame = Frame(nombres_frame, bg=PALETTE["fond_principal"])
        self.nombres_frame.pack(pady=10)

        # Zone de saisie
        saisie_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        saisie_frame.pack(fill=X, padx=20, pady=20)
        
        Label(saisie_frame, text="🧮 TON CALCUL:", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.calcul_entry = Entry(saisie_frame, font=("Century Gothic", 16), 
                                 width=30, justify="center")
        self.calcul_entry.pack(pady=10)
        self.calcul_entry.bind("<Return>", lambda e: self._verifier_calcul())
        
        # Exemple
        Label(saisie_frame, text="Exemple: (6 - 2) * (4 + 2)", 
              font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack()

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=20, pady=15)
        
        ttk.Button(buttons_frame, text="✅ Vérifier le calcul", 
                  command=self._verifier_calcul).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouveau défi", 
                  command=self._nouveau_defi).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Voir solutions", 
                  command=self._afficher_solutions).pack(side=RIGHT, padx=10)

        # Solutions trouvées
        solutions_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        solutions_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)
        
        Label(solutions_frame, text="✅ SOLUTIONS TROUVÉES:", 
              font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"]).pack(anchor=W)
        
        self.solutions_text = Text(solutions_frame, height=6, font=("Century Gothic", 10),
                                  bg="#F8FAFC", fg=PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(solutions_frame, command=self.solutions_text.yview)
        self.solutions_text.config(yscrollcommand=scrollbar.set)
        self.solutions_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", 
                                   font=("Century Gothic", 12), bg=PALETTE["fond_principal"])
        self.feedback_label.pack(pady=10)

    def _generer_nombres(self):
        """Génère 4 nombres pour le jeu des 24"""
        if self.niveau == "Facile":
            # Nombres de 1 à 10, plus faciles
            self.nombres_actuels = [random.randint(1, 10) for _ in range(4)]
        elif self.niveau == "Moyen":
            # Nombres de 1 à 13, avec quelques plus grands
            self.nombres_actuels = [random.randint(1, 13) for _ in range(4)]
        else:  # Difficile
            # Nombres de 1 à 20, défis plus complexes
            self.nombres_actuels = [random.randint(1, 20) for _ in range(4)]
            
        # Vérifier qu'au moins une solution existe
        if not self._trouver_toutes_solutions():
            # Regénérer si pas de solution
            self._generer_nombres()

    def _afficher_nombres(self):
        """Affiche les nombres disponibles"""
        # Nettoyer le frame
        for widget in self.nombres_frame.winfo_children():
            widget.destroy()
            
        # Afficher chaque nombre
        for i, nombre in enumerate(self.nombres_actuels):
            Label(self.nombres_frame, text=str(nombre), 
                  font=("Century Gothic", 20, "bold"), 
                  bg=PALETTE["secondaire"], fg="white", 
                  width=4, height=2, relief="raised",
                  borderwidth=2).grid(row=0, column=i, padx=10)

    def _nouveau_defi(self):
        """Prépare un nouveau défi"""
        self._generer_nombres()
        self._afficher_nombres()
        self.calcul_entry.delete(0, END)
        self.solutions_text.delete(1.0, END)
        self.solutions_trouvees = []
        self.feedback_label.config(text="")
        
        # Mettre à jour le niveau selon le score
        if self.score < 50:
            self.niveau = "Facile"
        elif self.score < 150:
            self.niveau = "Moyen"
        else:
            self.niveau = "Difficile"
            
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau}")

    def _verifier_calcul(self):
        """Vérifie le calcul du joueur"""
        calcul = self.calcul_entry.get().strip()
        
        if not calcul:
            self.feedback_label.config(text="❌ Entre un calcul", fg=PALETTE["erreur"])
            return
            
        try:
            # Vérifier que seuls les nombres autorisés sont utilisés
            nombres_utilises = self._extraire_nombres(calcul)
            if not self._verifier_nombres_autorises(nombres_utilises):
                self.feedback_label.config(text="❌ Utilise seulement les nombres donnés", fg=PALETTE["erreur"])
                return
            
            # Évaluer le résultat
            resultat = eval(calcul)
            
            if abs(resultat - 24) < 0.001:  # Tolérance pour les floats
                if calcul not in self.solutions_trouvees:
                    # Calculer les points
                    points = self._calculer_points(calcul)
                    self.score += points
                    self.score_label.config(text=f"🏆 Score: {self.score}")
                    
                    self.solutions_trouvees.append(calcul)
                    self._afficher_solution(calcul, points)
                    
                    self.feedback_label.config(text=f"✅ Bravo ! +{points} points", fg="#10B981")
                    self.calcul_entry.delete(0, END)
                    
                    # Nouveau défi après 3 solutions
                    if len(self.solutions_trouvees) >= 3:
                        self.fenetre_jeu.after(2000, self._nouveau_defi)
                else:
                    self.feedback_label.config(text="⚠️ Solution déjà trouvée", fg="#F59E0B")
            else:
                self.feedback_label.config(text=f"❌ Résultat: {resultat}, cible: 24", fg=PALETTE["erreur"])
                
        except Exception as e:
            self.feedback_label.config(text="❌ Calcul invalide", fg=PALETTE["erreur"])

    def _extraire_nombres(self, calcul):
        """Extrait les nombres utilisés dans le calcul"""
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
        return len(nombres_utilises) <= 4  # Maximum 4 nombres

    def _calculer_points(self, calcul):
        """Calcule les points selon la complexité"""
        points_base = 15  # Base plus élevée pour le 24
        
        # Bonus pour complexité
        if '(' in calcul:
            points_base += 5
        if calcul.count('+') + calcul.count('-') + calcul.count('*') + calcul.count('/') >= 3:
            points_base += 5
        if '/' in calcul:
            points_base += 3
            
        # Multiplicateur de niveau
        multiplicateur = {"Facile": 1, "Moyen": 2, "Difficile": 3}
        
        return points_base * multiplicateur[self.niveau]

    def _afficher_solution(self, calcul, points):
        """Affiche une solution trouvée"""
        self.solutions_text.insert(END, f"• {calcul} = 24 (+{points} pts)\n")
        self.solutions_text.see(END)

    def _trouver_toutes_solutions(self):
        """Trouve quelques solutions possibles (version simplifiée)"""
        # Cette fonction vérifie simplement qu'il existe au moins une solution
        # Une implémentation complète vérifierait toutes les combinaisons
        return True  # Pour l'instant, on suppose qu'il y a toujours une solution

    def _afficher_solutions(self):
        """Affiche quelques solutions possibles"""
        solutions = self._trouver_solutions_simples()
        
        if solutions:
            message = "Quelques solutions possibles :\n\n"
            for i, sol in enumerate(solutions[:3], 1):
                message += f"{i}. {sol}\n"
            messagebox.showinfo("💡 Solutions possibles", message)
        else:
            messagebox.showinfo("💡 Astuce", "Essaye différentes combinaisons d'opérations ! Les parenthèses peuvent aider !")

    def _trouver_solutions_simples(self):
        """Trouve quelques solutions simples"""
        solutions = []
        nombres = self.nombres_actuels
        
        # Essaie quelques combinaisons basiques
        operations = ['+', '-', '*', '/']
        
        from itertools import permutations, product
        
        # Teste quelques permutations
        for perm in permutations(nombres):
            for ops in product(operations, repeat=3):
                try:
                    # Essai 1: ((a op b) op c) op d
                    calcul1 = f"(({perm[0]} {ops[0]} {perm[1]}) {ops[1]} {perm[2]}) {ops[2]} {perm[3]}"
                    if abs(eval(calcul1) - 24) < 0.001:
                        solutions.append(calcul1)
                        
                    # Essai 2: (a op b) op (c op d)
                    calcul2 = f"({perm[0]} {ops[0]} {perm[1]}) {ops[1]} ({perm[2]} {ops[2]} {perm[3]})"
                    if abs(eval(calcul2) - 24) < 0.001:
                        solutions.append(calcul2)
                        
                except:
                    pass
                    
        return solutions[:5]  # Retourne max 5 solutions

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
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        
        self._creer_interface()
        self._nouvelle_equation()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🍎 MATH EMOJI 🍌", 
              font=("Comic Sans MS", 22, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        self.score_label = Label(stats_frame, text=f"🏆 Score: {self.score}",
                                font=("Arial", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau}",
                                 font=("Arial", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(side=LEFT, padx=20)

        # Catégorie
        self.categorie_label = Label(stats_frame, text=f"🎨 Catégorie: Fruits",
                                    font=("Arial", 12), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.categorie_label.pack(side=RIGHT, padx=20)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("math_emoji", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Équations
        equations_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        equations_frame.pack(fill=X, padx=30, pady=20)
        
        Label(equations_frame, text="🧮 RÉSOUS CES ÉQUATIONS :", 
              font=("Arial", 14, "bold"), bg=PALETTE["fond_principal"]).pack(pady=10)
        
        self.equations_text = Text(equations_frame, height=4, font=("Arial", 16),
                                  bg="#FFF9C4", fg=PALETTE["texte_fonce"], wrap=WORD, 
                                  relief="solid", borderwidth=1)
        self.equations_text.pack(fill=X, pady=10)
        self.equations_text.config(state=DISABLED)

        # Zone de réponses
        reponses_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        reponses_frame.pack(fill=X, padx=30, pady=15)
        
        Label(reponses_frame, text="✏️ TES RÉPONSES :", 
              font=("Arial", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=10)
        
        self.reponses_frame = Frame(reponses_frame, bg=PALETTE["fond_principal"])
        self.reponses_frame.pack(pady=10)

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=30, pady=20)
        
        ttk.Button(buttons_frame, text="✅ Vérifier les réponses", 
                  command=self._verifier_reponses, style="Accent.TButton").pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouvelle équation", 
                  command=self._nouvelle_equation).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Indice", 
                  command=self._donner_indice).pack(side=RIGHT, padx=10)

        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", 
                                   font=("Arial", 13), bg=PALETTE["fond_principal"], wraplength=500)
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
            ligne_frame = Frame(self.reponses_frame, bg=PALETTE["fond_principal"])
            ligne_frame.grid(row=i, column=0, sticky="w", pady=8)
            
            Label(ligne_frame, text=f"{emoji} = ", 
                  font=("Arial", 16), bg=PALETTE["fond_principal"]).pack(side=LEFT, padx=(0, 10))
            
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
                    fg=PALETTE["erreur"]
                )
                
        except Exception as e:
            self.feedback_label.config(text="❌ Erreur de saisie", fg=PALETTE["erreur"])

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
# CALCUL MENTAL EXPRESS
# =============================================================================

class CalculMentalExpress:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = "Débutant"
        self.question_actuelle = None
        self.reponse_correcte = None
        self.temps_limite = 15  # 15 secondes par question
        self.temps_restant = self.temps_limite
        self.timer_actif = False
        self.questions_repondus = 0
        self.questions_correctes = 0
        self.streak = 0
        self.meilleur_streak = 0
        
    def lancer_jeu(self):
        """Lance le Calcul Mental Express"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🌀 Calcul Mental Express")
        self.fenetre_jeu.geometry("600x500")
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        
        self._creer_interface()
        self._nouvelle_question()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🌀 CALCUL MENTAL EXPRESS", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Statistiques en temps réel
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=8)
        
        # Score et streak
        left_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        left_stats.pack(side=LEFT)
        
        self.score_label = Label(left_stats, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(anchor=W)
        
        self.streak_label = Label(left_stats, text=f"🔥 Streak: {self.streak}",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.streak_label.pack(anchor=W)
        
        # Timer au centre
        center_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        center_stats.pack(side=LEFT, expand=True)
        
        self.timer_label = Label(center_stats, text=f"⏱️ {self.temps_restant}s",
                                font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.timer_label.pack()
        
        # Précision à droite
        right_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        right_stats.pack(side=RIGHT)
        
        self.precision_label = Label(right_stats, text=f"🎯 Précision: 0%",
                                   font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.precision_label.pack(anchor=E)
        
        self.niveau_label = Label(right_stats, text=f"📊 {self.niveau}",
                                font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(anchor=E)

        # Barre de progression du timer
        self.progress_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        self.progress_frame.pack(fill=X, padx=50, pady=5)
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient=HORIZONTAL, 
                                          length=400, mode='determinate', maximum=self.temps_limite)
        self.progress_bar.pack(fill=X)
        self.progress_bar['value'] = self.temps_limite

        # Zone de question
        question_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        question_frame.pack(fill=BOTH, expand=True, padx=40, pady=20)
        
        Label(question_frame, text="CALCULE RAPIDEMENT :", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack(pady=(10, 20))
        
        self.question_label = Label(question_frame, text="", 
                                   font=("Century Gothic", 28, "bold"), 
                                   bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
        self.question_label.pack(pady=20)

        # Zone de réponse
        reponse_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        reponse_frame.pack(fill=X, padx=40, pady=15)
        
        self.reponse_entry = Entry(reponse_frame, font=("Century Gothic", 18), 
                                  width=15, justify="center")
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse())
        self.reponse_entry.focus()

        # Boutons
        buttons_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=40, pady=15)
        
        ttk.Button(buttons_frame, text="✅ Vérifier", 
                  command=self._verifier_reponse).pack(side=LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="➡️ Passer", 
                  command=self._nouvelle_question).pack(side=LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="📚 Guide", 
                  command=lambda: afficher_guide_jeu("calcul_mental_express", self.fenetre_jeu)).pack(side=RIGHT, padx=5)

        # Feedback
        self.feedback_label = Label(self.fenetre_jeu, text="", 
                                   font=("Century Gothic", 12), bg=PALETTE["fond_principal"])
        self.feedback_label.pack(pady=10)

    def _generer_question(self):
        """Génère une question selon le niveau"""
        if self.niveau == "Débutant":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            operations = ['+', '-']
            points = 5
            
        elif self.niveau == "Intermédiaire":
            a = random.randint(10, 50)
            b = random.randint(1, 30)
            operations = ['+', '-', '*']
            points = 8
            
        else:  # Expert
            a = random.randint(20, 100)
            b = random.randint(1, 50)
            operations = ['+', '-', '*', '//']  # Division entière
            points = 12
        
        operation = random.choice(operations)
        
        if operation == '+':
            question = f"{a} + {b}"
            reponse = a + b
        elif operation == '-':
            # Éviter les résultats négatifs
            a, b = max(a, b), min(a, b)
            question = f"{a} - {b}"
            reponse = a - b
        elif operation == '*':
            # Limiter la difficulté
            if self.niveau == "Intermédiaire":
                a = random.randint(2, 12)
                b = random.randint(2, 12)
            else:
                a = random.randint(5, 20)
                b = random.randint(5, 15)
            question = f"{a} × {b}"
            reponse = a * b
        elif operation == '//':
            # Division avec résultat entier
            b = random.randint(2, 12)
            a = b * random.randint(2, 12)
            question = f"{a} ÷ {b}"
            reponse = a // b
        
        return question, reponse, points

    def _nouvelle_question(self):
        """Prépare une nouvelle question"""
        self._arreter_timer()
        
        if hasattr(self, 'fenetre_jeu') and self.fenetre_jeu.winfo_exists():
            self.question_actuelle, self.reponse_correcte, self.points_question = self._generer_question()
            
            # Mettre à jour l'interface
            self.question_label.config(text=self.question_actuelle)
            self.reponse_entry.delete(0, END)
            self.feedback_label.config(text="")
            
            # Réinitialiser le timer
            self.temps_restant = self.temps_limite
            self.timer_label.config(text=f"⏱️ {self.temps_restant}s")
            self.progress_bar['value'] = self.temps_limite
            
            # Démarrer le timer
            self._demarrer_timer()
            self.reponse_entry.focus()

    def _demarrer_timer(self):
        """Démarre le compte à rebours"""
        self.timer_actif = True
        self._mettre_a_jour_timer()

    def _arreter_timer(self):
        """Arrête le timer"""
        self.timer_actif = False

    def _mettre_a_jour_timer(self):
        """Met à jour le timer chaque seconde"""
        if not self.timer_actif or not hasattr(self, 'fenetre_jeu') or not self.fenetre_jeu.winfo_exists():
            return
            
        if self.temps_restant > 0:
            self.temps_restant -= 0.1  # Mise à jour toutes les 100ms pour plus de fluidité
            self.timer_label.config(text=f"⏱️ {self.temps_restant:.1f}s")
            self.progress_bar['value'] = self.temps_restant
            
            # Changement de couleur
            if self.temps_restant <= 5:
                self.timer_label.config(fg=PALETTE["erreur"])
                self.progress_bar.configure(style="Urgent.Horizontal.TProgressbar")
            elif self.temps_restant <= 10:
                self.timer_label.config(fg="#F59E0B")
                self.progress_bar.configure(style="Warning.Horizontal.TProgressbar")
            else:
                self.timer_label.config(fg=PALETTE["primaire"])
                self.progress_bar.configure(style="Horizontal.TProgressbar")
            
            self.fenetre_jeu.after(100, self._mettre_a_jour_timer)
        else:
            self._temps_ecoule()

    def _temps_ecoule(self):
        """Quand le temps est écoulé"""
        self.timer_actif = False
        self.feedback_label.config(text="⏰ Temps écoulé !", fg=PALETTE["erreur"])
        self.streak = 0
        self.streak_label.config(text=f"🔥 Streak: {self.streak}")
        self.questions_repondus += 1
        self._mettre_a_jour_precision()
        self.fenetre_jeu.after(1500, self._nouvelle_question)

    def _verifier_reponse(self):
        """Vérifie la réponse du joueur"""
        if not self.timer_actif or not self.question_actuelle:
            return
            
        self._arreter_timer()
        reponse_joueur = self.reponse_entry.get().strip()
        
        try:
            reponse_joueur_num = int(reponse_joueur)
            temps_utilise = self.temps_limite - self.temps_restant
            
            if reponse_joueur_num == self.reponse_correcte:
                # Calcul des points avec bonus de rapidité
                points_bonus = max(1, int(5 * (self.temps_restant / self.temps_limite)))
                points_totaux = self.points_question + points_bonus
                
                self.score += points_totaux
                self.questions_correctes += 1
                self.streak += 1
                self.meilleur_streak = max(self.meilleur_streak, self.streak)
                
                # Feedback positif
                if temps_utilise < 5:
                    message = f"⚡ Foudroyant ! +{points_totaux} points"
                elif temps_utilise < 10:
                    message = f"✅ Excellent ! +{points_totaux} points"
                else:
                    message = f"👍 Correct ! +{points_totaux} points"
                
                self.feedback_label.config(text=message, fg="#10B981")
                
                # Mettre à jour les statistiques
                self._mettre_a_jour_affichage()
                
                # Bonus visuel pour les streaks
                if self.streak >= 5:
                    self.feedback_label.config(text=f"🎯 STREAK {self.streak} ! +{points_totaux} points", fg="#F59E0B")
                if self.streak >= 10:
                    self.feedback_label.config(text=f"🔥 STREAK {self.streak} ! +{points_totaux} points", fg=PALETTE["erreur"])
                    
            else:
                self.feedback_label.config(text=f"❌ Incorrect. Réponse: {self.reponse_correcte}", fg=PALETTE["erreur"])
                self.streak = 0
                self._mettre_a_jour_affichage()
            
            self.questions_repondus += 1
            self._mettre_a_jour_precision()
            self._mettre_a_jour_niveau()
            
            # Question suivante après délai
            self.fenetre_jeu.after(2000, self._nouvelle_question)
            
        except ValueError:
            self.feedback_label.config(text="❌ Entrez un nombre entier", fg=PALETTE["erreur"])
            self.fenetre_jeu.after(1500, self._nouvelle_question)

    def _mettre_a_jour_affichage(self):
        """Met à jour tous les affichages"""
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.streak_label.config(text=f"🔥 Streak: {self.streak}")

    def _mettre_a_jour_precision(self):
        """Met à jour le pourcentage de précision"""
        if self.questions_repondus > 0:
            precision = (self.questions_correctes / self.questions_repondus) * 100
            self.precision_label.config(text=f"🎯 Précision: {precision:.1f}%")

    def _mettre_a_jour_niveau(self):
        """Met à jour le niveau selon le score"""
        ancien_niveau = self.niveau
        
        if self.score < 100:
            self.niveau = "Débutant"
            self.temps_limite = 15
        elif self.score < 300:
            self.niveau = "Intermédiaire"
            self.temps_limite = 12
        else:
            self.niveau = "Expert"
            self.temps_limite = 10
            
        self.niveau_label.config(text=f"📊 {self.niveau}")
        
        # Notification de changement de niveau
        if ancien_niveau != self.niveau:
            self.feedback_label.config(text=f"🎉 Niveau {self.niveau} débloqué !", fg=PALETTE["primaire"])




# =============================================================================
# SUDOKU MATHÉMATIQUE
# =============================================================================

class SudokuMathematique:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = "Facile"
        self.grille_actuelle = None
        self.grille_solution = None
        self.cases_vides = 0
        self.erreurs = 0
        self.temps_debut = None
        self.temps_ecoule = 0
        self.timer_actif = False
        
    def lancer_jeu(self):
        """Lance le Sudoku Mathématique"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🧩 Sudoku Mathématique")
        self.fenetre_jeu.geometry("800x700")
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        
        self._creer_interface()
        self._nouvelle_grille()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🧩 SUDOKU MATHÉMATIQUE", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Score et niveau
        left_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        left_stats.pack(side=LEFT)
        
        self.score_label = Label(left_stats, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(anchor=W)
        
        self.niveau_label = Label(left_stats, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(anchor=W)
        
        # Timer au centre
        center_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        center_stats.pack(side=LEFT, expand=True)
        
        self.timer_label = Label(center_stats, text="⏱️ 00:00",
                                font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.timer_label.pack()
        
        # Erreurs et progression
        right_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        right_stats.pack(side=RIGHT)
        
        self.erreurs_label = Label(right_stats, text=f"❌ Erreurs: {self.erreurs}",
                                  font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.erreurs_label.pack(anchor=E)
        
        self.progression_label = Label(right_stats, text=f"📈 Progression: 0%",
                                     font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.progression_label.pack(anchor=E)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("sudoku_math", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Cadre principal pour la grille
        main_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Instructions
        Label(main_frame, text="Remplis la grille selon les règles du Sudoku avec des opérations mathématiques !", 
              font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack(pady=5)

        # Cadre de la grille
        grille_frame = Frame(main_frame, bg="black", relief="solid", borderwidth=2)
        grille_frame.pack(pady=15)

        # Créer la grille 9x9
        self.cases = []
        for i in range(9):
            ligne_cases = []
            for j in range(9):
                # Déterminer la couleur de fond selon la région 3x3
                region_i, region_j = i // 3, j // 3
                if (region_i + region_j) % 2 == 0:
                    bg_color = "#E8F4FD"  # Bleu très clair
                else:
                    bg_color = "#FFFFFF"  # Blanc
                
                case_frame = Frame(grille_frame, bg=bg_color, relief="solid", borderwidth=1, width=50, height=50)
                case_frame.grid(row=i, column=j, padx=1, pady=1)
                case_frame.pack_propagate(False)
                
                case_label = Label(case_frame, text="", font=("Arial", 16, "bold"), 
                                  bg=bg_color, fg=PALETTE["texte_fonce"])
                case_label.pack(expand=True, fill=BOTH)
                
                # Stocker les informations de la case
                case_info = {
                    'frame': case_frame,
                    'label': case_label,
                    'valeur': 0,
                    'modifiable': False,
                    'row': i,
                    'col': j
                }
                ligne_cases.append(case_info)
                
                # Bind des événements de clic
                case_frame.bind("<Button-1>", lambda e, row=i, col=j: self._selectionner_case(row, col))
                case_label.bind("<Button-1>", lambda e, row=i, col=j: self._selectionner_case(row, col))
            
            self.cases.append(ligne_cases)

        # Cadre de saisie
        saisie_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        saisie_frame.pack(fill=X, pady=15)

        Label(saisie_frame, text="Case sélectionnée: Aucune", 
              font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.case_selectionnee_label = Label(saisie_frame, text="", 
                                           font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.case_selectionnee_label.pack(pady=2)

        # Boutons numériques
        chiffres_frame = Frame(saisie_frame, bg=PALETTE["fond_principal"])
        chiffres_frame.pack(pady=10)

        for i in range(1, 10):
            btn = ttk.Button(chiffres_frame, text=str(i), width=4,
                           command=lambda num=i: self._inserer_chiffre(num))
            btn.grid(row=(i-1)//3, column=(i-1)%3, padx=2, pady=2)

        # Boutons d'action
        action_frame = Frame(saisie_frame, bg=PALETTE["fond_principal"])
        action_frame.pack(pady=10)

        ttk.Button(action_frame, text="🔍 Vérifier la grille", 
                  command=self._verifier_grille).pack(side=LEFT, padx=5)
        
        ttk.Button(action_frame, text="🧹 Effacer la case", 
                  command=self._effacer_case).pack(side=LEFT, padx=5)
        
        ttk.Button(action_frame, text="🔄 Nouvelle grille", 
                  command=self._nouvelle_grille).pack(side=LEFT, padx=5)
        
        ttk.Button(action_frame, text="💡 Indice", 
                  command=self._donner_indice).pack(side=RIGHT, padx=5)

        # Feedback
        self.feedback_label = Label(main_frame, text="", 
                                   font=("Century Gothic", 12), bg=PALETTE["fond_principal"], wraplength=600)
        self.feedback_label.pack(pady=10)

        # Case sélectionnée
        self.case_selectionnee = None

    def _generer_grille_sudoku(self):
        """Génère une grille de Sudoku selon le niveau"""
        # Pour la démonstration, nous utilisons une grille prédéfinie
        # En production, vous voudriez une vraie génération de Sudoku
        
        if self.niveau == "Facile":
            grille_base = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
            cases_vides = 40
        elif self.niveau == "Moyen":
            grille_base = [
                [0, 0, 0, 6, 0, 0, 4, 0, 0],
                [7, 0, 0, 0, 0, 3, 6, 0, 0],
                [0, 0, 0, 0, 9, 1, 0, 8, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 5, 0, 1, 8, 0, 0, 0, 3],
                [0, 0, 0, 3, 0, 6, 0, 4, 5],
                [0, 4, 0, 2, 0, 0, 0, 6, 0],
                [9, 0, 3, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 1, 0, 0]
            ]
            cases_vides = 50
        else:  # Difficile
            grille_base = [
                [0, 0, 0, 6, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 5, 0, 1],
                [3, 6, 9, 0, 8, 0, 4, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            cases_vides = 60
            
        return grille_base, cases_vides

    def _convertir_en_sudoku_math(self, grille):
        """Convertit une grille classique en Sudoku mathématique"""
        grille_math = []
        operations = ['+', '-', '×', '÷']
        
        for i in range(9):
            ligne_math = []
            for j in range(9):
                if grille[i][j] != 0:
                    # Pour les cases pré-remplies, on ajoute une opération aléatoire
                    operation = random.choice(operations)
                    if operation == '+':
                        a = random.randint(1, grille[i][j]-1)
                        b = grille[i][j] - a
                        texte = f"{a}+{b}"
                    elif operation == '-':
                        a = grille[i][j] + random.randint(1, 5)
                        b = a - grille[i][j]
                        texte = f"{a}-{b}"
                    elif operation == '×':
                        # Trouver des facteurs
                        facteurs = []
                        for k in range(1, grille[i][j]+1):
                            if grille[i][j] % k == 0:
                                facteurs.append(k)
                        if len(facteurs) > 1:
                            a = random.choice(facteurs[:-1])
                            b = grille[i][j] // a
                            texte = f"{a}×{b}"
                        else:
                            texte = str(grille[i][j])
                    else:  # '÷'
                        a = grille[i][j] * random.randint(2, 5)
                        b = a // grille[i][j]
                        texte = f"{a}÷{b}"
                    
                    ligne_math.append(texte)
                else:
                    ligne_math.append("")
            
            grille_math.append(ligne_math)
        
        return grille_math

    def _nouvelle_grille(self):
        """Prépare une nouvelle grille"""
        self._arreter_timer()
        
        # Générer la grille
        grille_base, self.cases_vides = self._generer_grille_sudoku()
        self.grille_solution = [ligne[:] for ligne in grille_base]  # Copie de la solution
        self.grille_actuelle = self._convertir_en_sudoku_math(grille_base)
        
        # Mettre à jour l'affichage
        self._afficher_grille()
        self.erreurs = 0
        self._mettre_a_jour_affichage()
        self.feedback_label.config(text="")
        self.case_selectionnee = None
        self.case_selectionnee_label.config(text="Aucune case sélectionnée")
        
        # Démarrer le timer
        self.temps_debut = time.time()
        self.temps_ecoule = 0
        self._demarrer_timer()

    def _afficher_grille(self):
        """Affiche la grille dans l'interface"""
        for i in range(9):
            for j in range(9):
                case = self.cases[i][j]
                valeur = self.grille_actuelle[i][j]
                
                if valeur:
                    case['label'].config(text=valeur)
                    case['modifiable'] = False
                    case['label'].config(fg=PALETTE["texte_fonce"])  # Noir pour les cases fixes
                else:
                    case['label'].config(text="")
                    case['modifiable'] = True
                    case['label'].config(fg=PALETTE["primaire"])  # Bleu pour les cases modifiables
                
                # Réinitialiser la couleur de fond
                region_i, region_j = i // 3, j // 3
                if (region_i + region_j) % 2 == 0:
                    bg_color = "#E8F4FD"
                else:
                    bg_color = "#FFFFFF"
                
                case['frame'].config(bg=bg_color)
                case['label'].config(bg=bg_color)

    def _selectionner_case(self, row, col):
        """Sélectionne une case de la grille"""
        case = self.cases[row][col]
        
        if not case['modifiable']:
            self.feedback_label.config(text="❌ Cette case ne peut pas être modifiée", fg=PALETTE["erreur"])
            return
        
        # Désélectionner l'ancienne case
        if self.case_selectionnee:
            old_row, old_col = self.case_selectionnee
            old_case = self.cases[old_row][old_col]
            region_i, region_j = old_row // 3, old_col // 3
            if (region_i + region_j) % 2 == 0:
                bg_color = "#E8F4FD"
            else:
                bg_color = "#FFFFFF"
            old_case['frame'].config(bg=bg_color)
            old_case['label'].config(bg=bg_color)
        
        # Sélectionner la nouvelle case
        self.case_selectionnee = (row, col)
        case['frame'].config(bg="#FFF9C4")  #Jaune pour la sélection
        case['label'].config(bg="#FFF9C4")
        
        self.case_selectionnee_label.config(text=f"Ligne {row+1}, Colonne {col+1}")

    def _inserer_chiffre(self, chiffre):
        """Insère un chiffre dans la case sélectionnée"""
        if not self.case_selectionnee:
            self.feedback_label.config(text="❌ Sélectionne d'abord une case", fg=PALETTE["erreur"])
            return
        
        row, col = self.case_selectionnee
        case = self.cases[row][col]
        
        if not case['modifiable']:
            self.feedback_label.config(text="❌ Cette case ne peut pas être modifiée", fg=PALETTE["erreur"])
            return
        
        # Mettre à jour l'affichage
        case['label'].config(text=str(chiffre))
        
        # Vérifier si c'est correct
        if chiffre == self.grille_solution[row][col]:
            self.feedback_label.config(text="✅ Correct !", fg="#10B981")
            self.cases_vides -= 1
            self._mettre_a_jour_progression()
            
            # Vérifier si la grille est complète
            if self.cases_vides == 0:
                self._grille_terminee()
        else:
            self.feedback_label.config(text="❌ Incorrect", fg=PALETTE["erreur"])
            self.erreurs += 1
            self.erreurs_label.config(text=f"❌ Erreurs: {self.erreurs}")

    def _effacer_case(self):
        """Efface la case sélectionnée"""
        if not self.case_selectionnee:
            return
        
        row, col = self.case_selectionnee
        case = self.cases[row][col]
        
        if case['modifiable']:
            case['label'].config(text="")
            # Si on efface une case correcte, on réincrémente cases_vides
            if case['label']['text'] and int(case['label']['text']) == self.grille_solution[row][col]:
                self.cases_vides += 1
                self._mettre_a_jour_progression()

    def _mettre_a_jour_progression(self):
        """Met à jour la progression"""
        total_cases = 81
        cases_remplies = total_cases - self.cases_vides
        progression = (cases_remplies / total_cases) * 100
        self.progression_label.config(text=f"📈 Progression: {progression:.1f}%")

    def _verifier_grille(self):
        """Vérifie l'état actuel de la grille"""
        correct = True
        for i in range(9):
            for j in range(9):
                case = self.cases[i][j]
                if case['modifiable'] and case['label']['text']:
                    try:
                        valeur_joueur = int(case['label']['text'])
                        if valeur_joueur != self.grille_solution[i][j]:
                            correct = False
                            case['frame'].config(bg="#FFCDD2")  # Rouge pour les erreurs
                    except:
                        correct = False
        
        if correct:
            self.feedback_label.config(text="🎉 Toutes les cases remplies sont correctes !", fg="#10B981")
        else:
            self.feedback_label.config(text="❌ Certaines cases sont incorrectes", fg=PALETTE["erreur"])

    def _grille_terminee(self):
        """Quand la grille est terminée"""
        self._arreter_timer()
        
        # Calculer le score
        temps_bonus = max(0, 300 - self.temps_ecoule)  # Bonus jusqu'à 5 minutes
        erreurs_penalite = self.erreurs * 10
        niveau_multiplier = {"Facile": 1, "Moyen": 2, "Difficile": 3}
        
        points = (100 + temps_bonus - erreurs_penalite) * niveau_multiplier[self.niveau]
        points = max(50, points)  # Score minimum de 50
        
        self.score += points
        self.score_label.config(text=f"🏆 Score: {self.score}")
        
        messagebox.showinfo(
            "🎉 Grille Terminée !", 
            f"Félicitations ! Vous avez complété la grille !\n\n"
            f"Temps: {self.temps_ecoule:.0f} secondes\n"
            f"Erreurs: {self.erreurs}\n"
            f"Score: +{points} points\n\n"
            f"Score total: {self.score}"
        )
        
        # Nouvelle grille après délai
        self.fenetre_jeu.after(2000, self._nouvelle_grille)

    def _donner_indice(self):
        """Donne un indice au joueur"""
        if not self.case_selectionnee:
            self.feedback_label.config(text="❌ Sélectionne d'abord une case pour obtenir un indice", fg=PALETTE["erreur"])
            return
        
        row, col = self.case_selectionnee
        solution = self.grille_solution[row][col]
        
        # Pénalité de points pour l'indice
        penalite = 5
        self.score = max(0, self.score - penalite)
        self.score_label.config(text=f"🏆 Score: {self.score}")
        
        messagebox.showinfo(
            "💡 Indice", 
            f"La solution pour cette case est : {solution}\n\n"
            f"(–{penalite} points)"
        )

    def _demarrer_timer(self):
        """Démarre le timer"""
        self.timer_actif = True
        self._mettre_a_jour_timer()

    def _arreter_timer(self):
        """Arrête le timer"""
        self.timer_actif = False

    def _mettre_a_jour_timer(self):
        """Met à jour le timer"""
        if not self.timer_actif or not hasattr(self, 'fenetre_jeu') or not self.fenetre_jeu.winfo_exists():
            return
        
        self.temps_ecoule = time.time() - self.temps_debut
        
        # Formater le temps
        minutes = int(self.temps_ecoule // 60)
        secondes = int(self.temps_ecoule % 60)
        temps_formate = f"{minutes:02d}:{secondes:02d}"
        
        self.timer_label.config(text=f"⏱️ {temps_formate}")
        
        if self.timer_actif:
            self.fenetre_jeu.after(1000, self._mettre_a_jour_timer)

    def _mettre_a_jour_affichage(self):
        """Met à jour tous les affichages"""
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau}")
        self.erreurs_label.config(text=f"❌ Erreurs: {self.erreurs}")
        self._mettre_a_jour_progression()

# =============================================================================
# BATAILLE DES FRACTIONS
# =============================================================================

class BatailleDesFractions:
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = "Facile"
        self.fraction_joueur = None
        self.fraction_ordi = None
        self.victoires = 0
        self.defaites = 0
        self.manches_gagnees = 0
        self.manches_totales = 0
        self.paquet_cartes = []
        self.main_joueur = []
        self.main_ordi = []
        self.carte_actuelle = None
        
    def lancer_jeu(self):
        """Lance la Bataille des Fractions"""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("🎲 Bataille des Fractions")
        self.fenetre_jeu.geometry("800x700")
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        
        self._creer_interface()
        self._nouvelle_partie()

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🎲 BATAILLE DES FRACTIONS", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Score et niveau
        left_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        left_stats.pack(side=LEFT)
        
        self.score_label = Label(left_stats, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(anchor=W)
        
        self.niveau_label = Label(left_stats, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(anchor=W)
        
        # Résultats au centre
        center_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        center_stats.pack(side=LEFT, expand=True)
        
        self.resultats_label = Label(center_stats, text=f"🎯 Manches: {self.manches_gagnees}/{self.manches_totales}",
                                    font=("Century Gothic", 11), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
        self.resultats_label.pack()
        
        self.victoires_label = Label(center_stats, text=f"✅ Victoires: {self.victoires} | ❌ Défaites: {self.defaites}",
                                    font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.victoires_label.pack()
        
        # Cartes restantes à droite
        right_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        right_stats.pack(side=RIGHT)
        
        self.cartes_label = Label(right_stats, text=f"🃏 Cartes: 0/0",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.cartes_label.pack(anchor=E)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("bataille_fractions", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Zone de jeu principale
        jeu_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        jeu_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)

        # Cartes de l'ordinateur
        ordi_frame = Frame(jeu_frame, bg=PALETTE["fond_principal"])
        ordi_frame.pack(fill=X, pady=10)
        
        Label(ordi_frame, text="🤖 ORDINATEUR", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.carte_ordi_frame = Frame(ordi_frame, bg=PALETTE["fond_principal"], height=120)
        self.carte_ordi_frame.pack(fill=X, pady=10)
        self.carte_ordi_frame.pack_propagate(False)

        # Zone de bataille
        bataille_frame = Frame(jeu_frame, bg=PALETTE["fond_principal"])
        bataille_frame.pack(fill=X, pady=20)
        
        self.comparaison_label = Label(bataille_frame, text="⚔️ CHOISIS TA CARTE !", 
                                      font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.comparaison_label.pack(pady=10)

        # Cartes du joueur
        joueur_frame = Frame(jeu_frame, bg=PALETTE["fond_principal"])
        joueur_frame.pack(fill=X, pady=10)
        
        Label(joueur_frame, text="🎮 TON JEU", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.cartes_joueur_frame = Frame(joueur_frame, bg=PALETTE["fond_principal"])
        self.cartes_joueur_frame.pack(fill=X, pady=10)

        # Boutons d'action
        actions_frame = Frame(jeu_frame, bg=PALETTE["fond_principal"])
        actions_frame.pack(fill=X, pady=20)
        
        ttk.Button(actions_frame, text="🔄 Nouvelle Partie", 
                  command=self._nouvelle_partie).pack(side=LEFT, padx=5)
        
        ttk.Button(actions_frame, text="💡 Aide Comparaison", 
                  command=self._afficher_aide_comparaison).pack(side=LEFT, padx=5)
        
        ttk.Button(actions_frame, text="🎯 Stratégie", 
                  command=self._afficher_strategie).pack(side=RIGHT, padx=5)

        # Feedback
        self.feedback_label = Label(jeu_frame, text="", 
                                   font=("Century Gothic", 13, "bold"), bg=PALETTE["fond_principal"], wraplength=600)
        self.feedback_label.pack(pady=15)

        # Historique des manches
        historique_frame = Frame(jeu_frame, bg=PALETTE["fond_principal"])
        historique_frame.pack(fill=BOTH, expand=True, pady=10)
        
        Label(historique_frame, text="📊 DERNIÈRES MANCHES:", 
              font=("Century Gothic", 10, "bold"), bg=PALETTE["fond_principal"]).pack(anchor=W)
        
        self.historique_text = Text(historique_frame, height=4, font=("Century Gothic", 9),
                                   bg="#F8FAFC", fg=PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(historique_frame, command=self.historique_text.yview)
        self.historique_text.config(yscrollcommand=scrollbar.set)
        self.historique_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.historique_text.config(state=DISABLED)

    def _creer_paquet_cartes(self):
        """Crée un paquet de cartes fractions selon le niveau"""
        self.paquet_cartes = []
        
        if self.niveau == "Facile":
            # Fractions simples avec dénominateurs 2, 3, 4, 6, 8
            denominateurs = [2, 3, 4, 6, 8]
            for denom in denominateurs:
                for num in range(1, denom):
                    # Éviter les fractions égales à 1
                    if num != denom:
                        valeur = num / denom
                        self.paquet_cartes.append({
                            'fraction': f"{num}/{denom}",
                            'valeur': valeur,
                            'simplifiee': self._simplifier_fraction(num, denom)
                        })
        elif self.niveau == "Moyen":
            # Fractions avec dénominateurs jusqu'à 12
            denominateurs = [2, 3, 4, 5, 6, 8, 10, 12]
            for denom in denominateurs:
                for num in range(1, denom):
                    valeur = num / denom
                    self.paquet_cartes.append({
                        'fraction': f"{num}/{denom}",
                        'valeur': valeur,
                        'simplifiee': self._simplifier_fraction(num, denom)
                    })
        else:  # Difficile
            # Fractions complexes avec dénominateurs jusqu'à 16
            denominateurs = [3, 4, 5, 6, 7, 8, 9, 10, 12, 16]
            for denom in denominateurs:
                for num in range(1, denom):
                    # Inclure quelques fractions impropres
                    if random.random() < 0.3:  # 30% de fractions > 1
                        num = random.randint(denom + 1, denom * 2)
                    valeur = num / denom
                    self.paquet_cartes.append({
                        'fraction': f"{num}/{denom}",
                        'valeur': valeur,
                        'simplifiee': self._simplifier_fraction(num, denom)
                    })
        
        # Mélanger le paquet
        random.shuffle(self.paquet_cartes)

    def _simplifier_fraction(self, num, denom):
        """Simplifie une fraction"""
        def pgcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        diviseur = pgcd(num, denom)
        num_simple = num // diviseur
        denom_simple = denom // diviseur
        
        if denom_simple == 1:
            return str(num_simple)
        else:
            return f"{num_simple}/{denom_simple}"

    def _distribuer_cartes(self):
        """Distribue les cartes aux joueurs"""
        self.main_joueur = []
        self.main_ordi = []
        
        # Distribuer 10 cartes à chaque joueur
        for i in range(10):
            if self.paquet_cartes:
                self.main_joueur.append(self.paquet_cartes.pop())
            if self.paquet_cartes:
                self.main_ordi.append(self.paquet_cartes.pop())

    def _nouvelle_partie(self):
        """Commence une nouvelle partie"""
        self._creer_paquet_cartes()
        self._distribuer_cartes()
        self.manches_gagnees = 0
        self.manches_totales = 0
        self._mettre_a_jour_affichage()
        self._afficher_cartes_joueur()
        self._cacher_carte_ordi()
        self.feedback_label.config(text="🎮 Choisis une carte ! La plus grande fraction gagne.", fg=PALETTE["primaire"])
        self.historique_text.config(state=NORMAL)
        self.historique_text.delete(1.0, END)
        self.historique_text.config(state=DISABLED)

    def _afficher_cartes_joueur(self):
        """Affiche les cartes du joueur"""
        # Nettoyer le frame
        for widget in self.cartes_joueur_frame.winfo_children():
            widget.destroy()
        
        # Afficher chaque carte
        for i, carte in enumerate(self.main_joueur):
            carte_frame = Frame(self.cartes_joueur_frame, bg="white", relief="raised", borderwidth=2, width=80, height=100)
            carte_frame.grid(row=0, column=i, padx=5, pady=5)
            carte_frame.pack_propagate(False)
            
            # Fraction
            Label(carte_frame, text=carte['fraction'], font=("Arial", 14, "bold"), 
                  bg="white", fg=PALETTE["primaire"]).pack(expand=True)
            
            # Valeur décimale (cachée au début)
            valeur_label = Label(carte_frame, text=f"{carte['valeur']:.2f}", font=("Arial", 10), 
                               bg="white", fg=PALETTE["texte_clair"])
            valeur_label.pack()
            
            # Bouton pour jouer la carte
            btn = ttk.Button(carte_frame, text="Jouer", 
                           command=lambda c=carte: self._jouer_carte(c))
            btn.pack(pady=5)
            
            # Stocker la référence
            carte['frame'] = carte_frame
            carte['valeur_label'] = valeur_label

    def _cacher_carte_ordi(self):
        """Cache la carte de l'ordinateur"""
        for widget in self.carte_ordi_frame.winfo_children():
            widget.destroy()
        
        carte_cachee_frame = Frame(self.carte_ordi_frame, bg="#4B5563", relief="raised", borderwidth=2, width=80, height=100)
        carte_cachee_frame.pack(pady=10)
        carte_cachee_frame.pack_propagate(False)
        
        Label(carte_cachee_frame, text="?", font=("Arial", 20, "bold"), 
              bg="#4B5563", fg="white").pack(expand=True)
        
        Label(carte_cachee_frame, text="Carte cachée", font=("Arial", 8), 
              bg="#4B5563", fg="white").pack()

    def _afficher_carte_ordi(self, carte):
        """Affiche la carte de l'ordinateur"""
        for widget in self.carte_ordi_frame.winfo_children():
            widget.destroy()
        
        carte_frame = Frame(self.carte_ordi_frame, bg="#DC2626", relief="raised", borderwidth=2, width=80, height=100)
        carte_frame.pack(pady=10)
        carte_frame.pack_propagate(False)
        
        Label(carte_frame, text=carte['fraction'], font=("Arial", 14, "bold"), 
              bg="#DC2626", fg="white").pack(expand=True)
        
        Label(carte_frame, text=f"{carte['valeur']:.2f}", font=("Arial", 10), 
              bg="#DC2626", fg="white").pack()

    def _jouer_carte(self, carte_joueur):
        """Le joueur joue une carte"""
        if not self.main_ordi:
            return
        
        # L'ordinateur joue une carte au hasard
        carte_ordi = random.choice(self.main_ordi)
        
        # Afficher la carte de l'ordinateur
        self._afficher_carte_ordi(carte_ordi)
        
        # Retirer les cartes des mains
        self.main_joueur.remove(carte_joueur)
        self.main_ordi.remove(carte_ordi)
        self.manches_totales += 1
        
        # Comparer les fractions
        if carte_joueur['valeur'] > carte_ordi['valeur']:
            # Victoire du joueur
            self.manches_gagnees += 1
            self.victoires += 1
            points = self._calculer_points(carte_joueur, carte_ordi, True)
            self.score += points
            self.feedback_label.config(
                text=f"✅ VICTOIRE ! {carte_joueur['fraction']} > {carte_ordi['fraction']} (+{points} points)", 
                fg="#10B981"
            )
            self._ajouter_historique(f"✅ {carte_joueur['fraction']} > {carte_ordi['fraction']} (+{points})")
            
        elif carte_joueur['valeur'] < carte_ordi['valeur']:
            # Défaite du joueur
            self.defaites += 1
            self.feedback_label.config(
                text=f"❌ DÉFAITE ! {carte_joueur['fraction']} < {carte_ordi['fraction']}", 
                fg=PALETTE["erreur"]
            )
            self._ajouter_historique(f"❌ {carte_joueur['fraction']} < {carte_ordi['fraction']}")
            
        else:
            # Égalité
            self.feedback_label.config(
                text=f"⚖️ ÉGALITÉ ! {carte_joueur['fraction']} = {carte_ordi['fraction']}", 
                fg="#F59E0B"
            )
            self._ajouter_historique(f"⚖️ {carte_joueur['fraction']} = {carte_ordi['fraction']}")
        
        # Mettre à jour l'affichage
        self._mettre_a_jour_affichage()
        self._afficher_cartes_joueur()
        
        # Vérifier si la partie est terminée
        if not self.main_joueur or not self.main_ordi:
            self._partie_terminee()

    def _calculer_points(self, carte_joueur, carte_ordi, victoire):
        """Calcule les points gagnés"""
        if not victoire:
            return 0
            
        points_base = 10
        niveau_multiplier = {"Facile": 1, "Moyen": 2, "Difficile": 3}
        
        # Bonus pour fractions complexes
        if '/' in carte_joueur['simplifiee'] and carte_joueur['simplifiee'] != carte_joueur['fraction']:
            points_base += 5
        
        # Bonus si la différence est petite (choix stratégique)
        difference = abs(carte_joueur['valeur'] - carte_ordi['valeur'])
        if difference < 0.1:
            points_base += 8
        
        return points_base * niveau_multiplier[self.niveau]

    def _partie_terminee(self):
        """Quand la partie est terminée"""
        # Calculer le bonus de victoire
        if self.manches_gagnees > self.manches_totales / 2:
            bonus_victoire = 50
            message = f"🎉 VICTOIRE ! Tu as gagné {self.manches_gagnees}/{self.manches_totales} manches !"
            self.victoires += 1
        else:
            bonus_victoire = 0
            message = f"💪 Bon effort ! Tu as gagné {self.manches_gagnees}/{self.manches_totales} manches."
            self.defaites += 1
        
        self.score += bonus_victoire
        
        messagebox.showinfo(
            "Partie Terminée", 
            f"{message}\n\n"
            f"Bonus victoire: +{bonus_victoire} points\n"
            f"Score total: {self.score}\n\n"
            f"✅ Victoires: {self.victoires} | ❌ Défaites: {self.defaites}"
        )
        
        # Mettre à jour le niveau selon le score
        if self.score < 200:
            self.niveau = "Facile"
        elif self.score < 500:
            self.niveau = "Moyen"
        else:
            self.niveau = "Difficile"
        
        self._mettre_a_jour_affichage()

    def _mettre_a_jour_affichage(self):
        """Met à jour tous les affichages"""
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau}")
        self.resultats_label.config(text=f"🎯 Manches: {self.manches_gagnees}/{self.manches_totales}")
        self.victoires_label.config(text=f"✅ Victoires: {self.victoires} | ❌ Défaites: {self.defaites}")
        
        cartes_restantes = len(self.main_joueur) + len(self.main_ordi)
        self.cartes_label.config(text=f"🃏 Cartes: {cartes_restantes}/20")

    def _ajouter_historique(self, texte):
        """Ajoute une entrée à l'historique"""
        self.historique_text.config(state=NORMAL)
        self.historique_text.insert(END, f"• {texte}\n")
        self.historique_text.see(END)
        self.historique_text.config(state=DISABLED)

    def _afficher_aide_comparaison(self):
        """Affiche l'aide pour comparer les fractions"""
        messagebox.showinfo(
            "💡 Aide Comparaison", 
            "Pour comparer deux fractions :\n\n"
            "1. Même dénominateur : Compare les numérateurs\n"
            "   Ex: 3/4 > 2/4\n\n"
            "2. Même numérateur : Plus petit dénominateur = plus grande fraction\n"
            "   Ex: 2/3 > 2/5\n\n"
            "3. Différents : Trouve un dénominateur commun\n"
            "   Ex: 2/3 vs 3/4 → 8/12 vs 9/12 → 3/4 gagne\n\n"
            "Astuce : Multiplie en croix !\n"
            "2/3 vs 3/4 → 2×4=8 vs 3×3=9 → 3/4 gagne"
        )

    def _afficher_strategie(self):
        """Affiche des conseils stratégiques"""
        messagebox.showinfo(
            "🎯 Stratégie", 
            "Conseils pour gagner :\n\n"
            "• Garde les grosses fractions pour les manches importantes\n"
            "• Utilise les petites fractions quand l'ordi joue une carte faible\n"
            "• Apprends les équivalences : 1/2 = 2/4 = 3/6 = 0.5\n"
            "• Mémorise les fractions courantes :\n"
            "  1/4=0.25, 1/3≈0.33, 1/2=0.5, 2/3≈0.66, 3/4=0.75\n"
            "• Simplifie mentalement les fractions pour mieux comparer"
        )

# =============================================================================
# DESSINE-MOI UNE FONCTION
# =============================================================================

# =============================================================================
# DESSINE-MOI UNE FONCTION - VERSION ENRICHIE
# =============================================================================

class DessineMoiUneFonction:
    """Jeu « Dessine-moi une fonction » - classe refactorisée.

    Structure :
    - initialisation des attributs
    - méthode publique `lancer_jeu`
    - création de l'interface
    - génération / dessin / vérification
    - aides: indices, affichage des types
    """

    def __init__(self, parent):
        self.parent = parent
        # état du jeu
        self.score = 0
        self.niveau = "Débutant"
        self.fonction_actuelle = None
        self.points_joueur = []
        self.points_corrects = []

        # widgets et rendu
        self.canvas = None
        self.fenetre_jeu = None

        # flags et compteurs
        self.dessin_actif = False
        self.manches_gagnees = 0
        self.manches_totales = 0
        self.dernier_point = None
        self.grille_visible = True

        # bibliothèque de fonctions
        self.fonctions_bibliotheque = self._creer_bibliotheque_fonctions()

    def _creer_bibliotheque_fonctions(self):
        """Crée une bibliothèque étendue de fonctions.

        Retourne un dict {niveau: [fonctions]}. Chaque fonction est un dict
        contenant 'type', 'expression' et 'fonction' (callable).
        """
        return {
            "Débutant": [
                # Fonctions linéaires (20 variations)
                {"type": "lineaire", "expression": "f(x) = 2x + 1", "fonction": lambda x: 2*x + 1},
                {"type": "lineaire", "expression": "f(x) = x - 3", "fonction": lambda x: x - 3},
                {"type": "lineaire", "expression": "f(x) = -x + 2", "fonction": lambda x: -x + 2},
                {"type": "lineaire", "expression": "f(x) = -2x - 1", "fonction": lambda x: -2*x - 1},
                {"type": "lineaire", "expression": "f(x) = 3x", "fonction": lambda x: 3*x},
                {"type": "lineaire", "expression": "f(x) = 0.5x + 2", "fonction": lambda x: 0.5*x + 2},
                {"type": "lineaire", "expression": "f(x) = -0.5x - 1", "fonction": lambda x: -0.5*x - 1},
                {"type": "lineaire", "expression": "f(x) = 1.5x + 0.5", "fonction": lambda x: 1.5*x + 0.5},
                {"type": "lineaire", "expression": "f(x) = -1.5x + 2", "fonction": lambda x: -1.5*x + 2},
                {"type": "lineaire", "expression": "f(x) = 2x - 3", "fonction": lambda x: 2*x - 3},
                {"type": "lineaire", "expression": "f(x) = -x - 2", "fonction": lambda x: -x - 2},
                {"type": "lineaire", "expression": "f(x) = 4x + 1", "fonction": lambda x: 4*x + 1},
                {"type": "lineaire", "expression": "f(x) = -3x + 4", "fonction": lambda x: -3*x + 4},
                {"type": "lineaire", "expression": "f(x) = 0.25x + 3", "fonction": lambda x: 0.25*x + 3},
                {"type": "lineaire", "expression": "f(x) = -0.75x - 2", "fonction": lambda x: -0.75*x - 2},
                {"type": "lineaire", "expression": "f(x) = 2.5x - 1", "fonction": lambda x: 2.5*x - 1},
                {"type": "lineaire", "expression": "f(x) = -2x + 5", "fonction": lambda x: -2*x + 5},
                {"type": "lineaire", "expression": "f(x) = x + 4", "fonction": lambda x: x + 4},
                {"type": "lineaire", "expression": "f(x) = -x + 5", "fonction": lambda x: -x + 5},
                {"type": "lineaire", "expression": "f(x) = 3x - 4", "fonction": lambda x: 3*x - 4},
                
                # Fonctions constantes (10 variations)
                {"type": "constante", "expression": "f(x) = 3", "fonction": lambda x: 3},
                {"type": "constante", "expression": "f(x) = -2", "fonction": lambda x: -2},
                {"type": "constante", "expression": "f(x) = 0", "fonction": lambda x: 0},
                {"type": "constante", "expression": "f(x) = 4", "fonction": lambda x: 4},
                {"type": "constante", "expression": "f(x) = -1", "fonction": lambda x: -1},
                {"type": "constante", "expression": "f(x) = 2.5", "fonction": lambda x: 2.5},
                {"type": "constante", "expression": "f(x) = -3.5", "fonction": lambda x: -3.5},
                {"type": "constante", "expression": "f(x) = 1", "fonction": lambda x: 1},
                {"type": "constante", "expression": "f(x) = -4", "fonction": lambda x: -4},
                {"type": "constante", "expression": "f(x) = 0.5", "fonction": lambda x: 0.5},
                
                # Valeur absolue (10 variations)
                {"type": "absolu", "expression": "f(x) = |x|", "fonction": lambda x: abs(x)},
                {"type": "absolu", "expression": "f(x) = |x - 2|", "fonction": lambda x: abs(x - 2)},
                {"type": "absolu", "expression": "f(x) = |x + 1|", "fonction": lambda x: abs(x + 1)},
                {"type": "absolu", "expression": "f(x) = |2x|", "fonction": lambda x: abs(2*x)},
                {"type": "absolu", "expression": "f(x) = |0.5x|", "fonction": lambda x: abs(0.5*x)},
                {"type": "absolu", "expression": "f(x) = |x| + 1", "fonction": lambda x: abs(x) + 1},
                {"type": "absolu", "expression": "f(x) = |x| - 2", "fonction": lambda x: abs(x) - 2},
                {"type": "absolu", "expression": "f(x) = |x - 1| + 2", "fonction": lambda x: abs(x - 1) + 2},
                {"type": "absolu", "expression": "f(x) = |x + 2| - 1", "fonction": lambda x: abs(x + 2) - 1},
                {"type": "absolu", "expression": "f(x) = 2|x|", "fonction": lambda x: 2 * abs(x)},
                ],

            "Intermédiaire": [
                # Fonctions quadratiques simples (20 variations)
                {"type": "quadratique", "expression": "f(x) = x²", "fonction": lambda x: x**2},
                {"type": "quadratique", "expression": "f(x) = x² - 2", "fonction": lambda x: x**2 - 2},
                {"type": "quadratique", "expression": "f(x) = x² + 3", "fonction": lambda x: x**2 + 3},
                {"type": "quadratique", "expression": "f(x) = -x²", "fonction": lambda x: -x**2},
                {"type": "quadratique", "expression": "f(x) = -x² + 4", "fonction": lambda x: -x**2 + 4},
                {"type": "quadratique", "expression": "f(x) = 2x²", "fonction": lambda x: 2*x**2},
                {"type": "quadratique", "expression": "f(x) = 0.5x²", "fonction": lambda x: 0.5*x**2},
                {"type": "quadratique", "expression": "f(x) = -2x²", "fonction": lambda x: -2*x**2},
                {"type": "quadratique", "expression": "f(x) = x² - 4", "fonction": lambda x: x**2 - 4},
                {"type": "quadratique", "expression": "f(x) = -x² - 1", "fonction": lambda x: -x**2 - 1},
                {"type": "quadratique", "expression": "f(x) = 3x² - 2", "fonction": lambda x: 3*x**2 - 2},
                {"type": "quadratique", "expression": "f(x) = -0.5x² + 3", "fonction": lambda x: -0.5*x**2 + 3},
                {"type": "quadratique", "expression": "f(x) = 1.5x² + 1", "fonction": lambda x: 1.5*x**2 + 1},
                {"type": "quadratique", "expression": "f(x) = -1.5x² - 2", "fonction": lambda x: -1.5*x**2 - 2},
                {"type": "quadratique", "expression": "f(x) = 4x²", "fonction": lambda x: 4*x**2},
                {"type": "quadratique", "expression": "f(x) = -3x²", "fonction": lambda x: -3*x**2},
                {"type": "quadratique", "expression": "f(x) = 0.25x²", "fonction": lambda x: 0.25*x**2},
                {"type": "quadratique", "expression": "f(x) = -0.75x²", "fonction": lambda x: -0.75*x**2},
                {"type": "quadratique", "expression": "f(x) = 2.5x² - 3", "fonction": lambda x: 2.5*x**2 - 3},
                {"type": "quadratique", "expression": "f(x) = -2x² + 5", "fonction": lambda x: -2*x**2 + 5},
                
                # Fonctions racines (15 variations)
                {"type": "racine", "expression": "f(x) = √x", "fonction": lambda x: math.sqrt(x) if x >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √(x + 4)", "fonction": lambda x: math.sqrt(x + 4) if x + 4 >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √(x - 1)", "fonction": lambda x: math.sqrt(x - 1) if x - 1 >= 0 else 0},
                {"type": "racine", "expression": "f(x) = 2√x", "fonction": lambda x: 2 * math.sqrt(x) if x >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √x + 1", "fonction": lambda x: math.sqrt(x) + 1 if x >= 0 else 1},
                {"type": "racine", "expression": "f(x) = √x - 2", "fonction": lambda x: math.sqrt(x) - 2 if x >= 0 else -2},
                {"type": "racine", "expression": "f(x) = √(x + 2) + 1", "fonction": lambda x: math.sqrt(x + 2) + 1 if x + 2 >= 0 else 1},
                {"type": "racine", "expression": "f(x) = √(x - 3) - 1", "fonction": lambda x: math.sqrt(x - 3) - 1 if x - 3 >= 0 else -1},
                {"type": "racine", "expression": "f(x) = 0.5√x", "fonction": lambda x: 0.5 * math.sqrt(x) if x >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √(2x)", "fonction": lambda x: math.sqrt(2*x) if 2*x >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √(x + 6)", "fonction": lambda x: math.sqrt(x + 6) if x + 6 >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √(x - 4)", "fonction": lambda x: math.sqrt(x - 4) if x - 4 >= 0 else 0},
                {"type": "racine", "expression": "f(x) = 3√x", "fonction": lambda x: 3 * math.sqrt(x) if x >= 0 else 0},
                {"type": "racine", "expression": "f(x) = √x + 3", "fonction": lambda x: math.sqrt(x) + 3 if x >= 0 else 3},
                {"type": "racine", "expression": "f(x) = √(x + 1) - 2", "fonction": lambda x: math.sqrt(x + 1) - 2 if x + 1 >= 0 else -2},
                
                # Fonctions cubiques simples (15 variations)
                {"type": "cubique", "expression": "f(x) = x³", "fonction": lambda x: x**3 / 8},  # Échelle réduite
                {"type": "cubique", "expression": "f(x) = -x³", "fonction": lambda x: -x**3 / 8},
                {"type": "cubique", "expression": "f(x) = 2x³", "fonction": lambda x: 2*x**3 / 27},
                {"type": "cubique", "expression": "f(x) = -2x³", "fonction": lambda x: -2*x**3 / 27},
                {"type": "cubique", "expression": "f(x) = 0.5x³", "fonction": lambda x: 0.5*x**3 / 8},
                {"type": "cubique", "expression": "f(x) = -0.5x³", "fonction": lambda x: -0.5*x**3 / 8},
                {"type": "cubique", "expression": "f(x) = x³ + 1", "fonction": lambda x: (x**3 / 8) + 1},
                {"type": "cubique", "expression": "f(x) = x³ - 2", "fonction": lambda x: (x**3 / 8) - 2},
                {"type": "cubique", "expression": "f(x) = -x³ + 3", "fonction": lambda x: (-x**3 / 8) + 3},
                {"type": "cubique", "expression": "f(x) = -x³ - 1", "fonction": lambda x: (-x**3 / 8) - 1},
                {"type": "cubique", "expression": "f(x) = 1.5x³", "fonction": lambda x: 1.5*x**3 / 27},
                {"type": "cubique", "expression": "f(x) = -1.5x³", "fonction": lambda x: -1.5*x**3 / 27},
                {"type": "cubique", "expression": "f(x) = 3x³", "fonction": lambda x: 3*x**3 / 64},
                {"type": "cubique", "expression": "f(x) = -3x³", "fonction": lambda x: -3*x**3 / 64},
                {"type": "cubique", "expression": "f(x) = 0.25x³", "fonction": lambda x: 0.25*x**3 / 8},
            ],
            
            "Avancé": [
                # Fonctions quadratiques complexes (20 variations)
                {"type": "quadratique", "expression": "f(x) = (x - 2)²", "fonction": lambda x: (x - 2)**2},
                {"type": "quadratique", "expression": "f(x) = (x + 1)²", "fonction": lambda x: (x + 1)**2},
                {"type": "quadratique", "expression": "f(x) = -(x - 1)²", "fonction": lambda x: -(x - 1)**2},
                {"type": "quadratique", "expression": "f(x) = -(x + 2)²", "fonction": lambda x: -(x + 2)**2},
                {"type": "quadratique", "expression": "f(x) = (x - 2)² + 1", "fonction": lambda x: (x - 2)**2 + 1},
                {"type": "quadratique", "expression": "f(x) = (x + 1)² - 2", "fonction": lambda x: (x + 1)**2 - 2},
                {"type": "quadratique", "expression": "f(x) = -(x - 1)² + 3", "fonction": lambda x: -(x - 1)**2 + 3},
                {"type": "quadratique", "expression": "f(x) = -(x + 2)² - 1", "fonction": lambda x: -(x + 2)**2 - 1},
                {"type": "quadratique", "expression": "f(x) = 2(x - 1)²", "fonction": lambda x: 2*(x - 1)**2},
                {"type": "quadratique", "expression": "f(x) = -2(x + 1)²", "fonction": lambda x: -2*(x + 1)**2},
                {"type": "quadratique", "expression": "f(x) = 0.5(x - 3)²", "fonction": lambda x: 0.5*(x - 3)**2},
                {"type": "quadratique", "expression": "f(x) = -0.5(x + 3)²", "fonction": lambda x: -0.5*(x + 3)**2},
                {"type": "quadratique", "expression": "f(x) = (x - 1)² + 2", "fonction": lambda x: (x - 1)**2 + 2},
                {"type": "quadratique", "expression": "f(x) = (x + 2)² - 3", "fonction": lambda x: (x + 2)**2 - 3},
                {"type": "quadratique", "expression": "f(x) = -(x - 3)² + 1", "fonction": lambda x: -(x - 3)**2 + 1},
                {"type": "quadratique", "expression": "f(x) = -(x + 1)² - 2", "fonction": lambda x: -(x + 1)**2 - 2},
                {"type": "quadratique", "expression": "f(x) = 1.5(x - 2)²", "fonction": lambda x: 1.5*(x - 2)**2},
                {"type": "quadratique", "expression": "f(x) = -1.5(x + 2)²", "fonction": lambda x: -1.5*(x + 2)**2},
                {"type": "quadratique", "expression": "f(x) = 3(x - 1)² - 1", "fonction": lambda x: 3*(x - 1)**2 - 1},
                {"type": "quadratique", "expression": "f(x) = -3(x + 1)² + 2", "fonction": lambda x: -3*(x + 1)**2 + 2},
                
                # Fonctions trigonométriques (20 variations)
                {"type": "trigo", "expression": "f(x) = sin(x)", "fonction": lambda x: 2 * math.sin(x)},
                {"type": "trigo", "expression": "f(x) = cos(x)", "fonction": lambda x: 2 * math.cos(x)},
                {"type": "trigo", "expression": "f(x) = -sin(x)", "fonction": lambda x: -2 * math.sin(x)},
                {"type": "trigo", "expression": "f(x) = -cos(x)", "fonction": lambda x: -2 * math.cos(x)},
                {"type": "trigo", "expression": "f(x) = 2sin(x)", "fonction": lambda x: 3 * math.sin(x)},
                {"type": "trigo", "expression": "f(x) = 2cos(x)", "fonction": lambda x: 3 * math.cos(x)},
                {"type": "trigo", "expression": "f(x) = sin(2x)", "fonction": lambda x: 2 * math.sin(2*x)},
                {"type": "trigo", "expression": "f(x) = cos(2x)", "fonction": lambda x: 2 * math.cos(2*x)},
                {"type": "trigo", "expression": "f(x) = sin(x) + 1", "fonction": lambda x: 2 * math.sin(x) + 1},
                {"type": "trigo", "expression": "f(x) = cos(x) - 1", "fonction": lambda x: 2 * math.cos(x) - 1},
                {"type": "trigo", "expression": "f(x) = sin(x - 1)", "fonction": lambda x: 2 * math.sin(x - 1)},
                {"type": "trigo", "expression": "f(x) = cos(x + 1)", "fonction": lambda x: 2 * math.cos(x + 1)},
                {"type": "trigo", "expression": "f(x) = 0.5sin(x)", "fonction": lambda x: math.sin(x)},
                {"type": "trigo", "expression": "f(x) = 0.5cos(x)", "fonction": lambda x: math.cos(x)},
                {"type": "trigo", "expression": "f(x) = -2sin(x)", "fonction": lambda x: -3 * math.sin(x)},
                {"type": "trigo", "expression": "f(x) = -2cos(x)", "fonction": lambda x: -3 * math.cos(x)},
                {"type": "trigo", "expression": "f(x) = sin(0.5x)", "fonction": lambda x: 2 * math.sin(0.5*x)},
                {"type": "trigo", "expression": "f(x) = cos(0.5x)", "fonction": lambda x: 2 * math.cos(0.5*x)},
                {"type": "trigo", "expression": "f(x) = sin(x) + cos(x)", "fonction": lambda x: math.sin(x) + math.cos(x)},
                {"type": "trigo", "expression": "f(x) = 2sin(x) - cos(x)", "fonction": lambda x: 2*math.sin(x) - math.cos(x)},
                
                # Fonctions exponentielles et logarithmiques (15 variations)
                {"type": "exponentielle", "expression": "f(x) = e^x", "fonction": lambda x: math.exp(x/2) / 3},  # Échelle réduite
                {"type": "exponentielle", "expression": "f(x) = e^{-x}", "fonction": lambda x: math.exp(-x/2) / 3},
                {"type": "exponentielle", "expression": "f(x) = 2^x", "fonction": lambda x: 2**(x/2) / 3},
                {"type": "exponentielle", "expression": "f(x) = 2^{-x}", "fonction": lambda x: 2**(-x/2) / 3},
                {"type": "exponentielle", "expression": "f(x) = e^x + 1", "fonction": lambda x: math.exp(x/2)/3 + 1},
                {"type": "exponentielle", "expression": "f(x) = e^{-x} - 1", "fonction": lambda x: math.exp(-x/2)/3 - 1},
                {"type": "exponentielle", "expression": "f(x) = 2e^x", "fonction": lambda x: 2*math.exp(x/2)/3},
                {"type": "exponentielle", "expression": "f(x) = 0.5e^x", "fonction": lambda x: 0.5*math.exp(x/2)/3},
                {"type": "exponentielle", "expression": "f(x) = e^{2x}", "fonction": lambda x: math.exp(x) / 5},
                {"type": "exponentielle", "expression": "f(x) = e^{-2x}", "fonction": lambda x: math.exp(-x) / 5},
                {"type": "logarithmique", "expression": "f(x) = ln(x+5)", "fonction": lambda x: math.log(x+5) if x+5 > 0 else -3},
                {"type": "logarithmique", "expression": "f(x) = ln(x+3)", "fonction": lambda x: math.log(x+3) if x+3 > 0 else -2},
                {"type": "logarithmique", "expression": "f(x) = ln(x+7)", "fonction": lambda x: math.log(x+7) if x+7 > 0 else -4},
                {"type": "logarithmique", "expression": "f(x) = 2ln(x+5)", "fonction": lambda x: 2*math.log(x+5) if x+5 > 0 else -6},
                {"type": "logarithmique", "expression": "f(x) = ln(x+5) + 1", "fonction": lambda x: math.log(x+5)+1 if x+5 > 0 else -2},
                
                # Fonctions rationnelles (15 variations)
                {"type": "rationnelle", "expression": "f(x) = 1/x", "fonction": lambda x: 1/x if x != 0 else 10},
                {"type": "rationnelle", "expression": "f(x) = 2/x", "fonction": lambda x: 2/x if x != 0 else 10},
                {"type": "rationnelle", "expression": "f(x) = 1/(x+2)", "fonction": lambda x: 1/(x+2) if x != -2 else 10},
                {"type": "rationnelle", "expression": "f(x) = 1/(x-1)", "fonction": lambda x: 1/(x-1) if x != 1 else 10},
                {"type": "rationnelle", "expression": "f(x) = 2/(x+1)", "fonction": lambda x: 2/(x+1) if x != -1 else 10},
                {"type": "rationnelle", "expression": "f(x) = 1/(x²+1)", "fonction": lambda x: 1/(x**2+1)},
                {"type": "rationnelle", "expression": "f(x) = x/(x²+1)", "fonction": lambda x: x/(x**2+1)},
                {"type": "rationnelle", "expression": "f(x) = 1/(x+3)", "fonction": lambda x: 1/(x+3) if x != -3 else 10},
                {"type": "rationnelle", "expression": "f(x) = 1/(x-2)", "fonction": lambda x: 1/(x-2) if x != 2 else 10},
                {"type": "rationnelle", "expression": "f(x) = 3/(x+1)", "fonction": lambda x: 3/(x+1) if x != -1 else 10},
                {"type": "rationnelle", "expression": "f(x) = 1/(2x+1)", "fonction": lambda x: 1/(2*x+1) if x != -0.5 else 10},
                {"type": "rationnelle", "expression": "f(x) = x/(x+2)", "fonction": lambda x: x/(x+2) if x != -2 else 10},
                {"type": "rationnelle", "expression": "f(x) = (x+1)/(x-1)", "fonction": lambda x: (x+1)/(x-1) if x != 1 else 10},
                {"type": "rationnelle", "expression": "f(x) = 1/(x²+4)", "fonction": lambda x: 1/(x**2+4)},
                {"type": "rationnelle", "expression": "f(x) = x/(x²+4)", "fonction": lambda x: x/(x**2+4)},
            ]
        }

    def lancer_jeu(self):
        """Lance l'interface du jeu et initialise une partie."""
        self.fenetre_jeu = Toplevel(self.parent)
        self.fenetre_jeu.title("📈 Dessine-moi une Fonction - Version Enrichie")
        self.fenetre_jeu.geometry("900x750")
        self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])

        self._creer_interface()
        self._nouvelle_fonction()

    def _creer_interface(self):
        """Construire l'interface Tkinter pour le jeu."""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="📈 DESSINE-MOI UNE FONCTION - BIBLIOTHÈQUE ÉTENDUE", 
              font=("Century Gothic", 16, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Statistiques
        stats_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Score et niveau
        left_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        left_stats.pack(side=LEFT)
        
        self.score_label = Label(left_stats, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(anchor=W)
        
        self.niveau_label = Label(left_stats, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(anchor=W)
        
        # Résultats au centre
        center_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        center_stats.pack(side=LEFT, expand=True)
        
        self.resultats_label = Label(center_stats, text=f"🎯 Précision: {self.manches_gagnees}/{self.manches_totales}",
                                    font=("Century Gothic", 11), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
        self.resultats_label.pack()
        
        self.fonction_label = Label(center_stats, text="f(x) = ?",
                                   font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.fonction_label.pack()

        # Info bibliothèque
        right_stats = Frame(stats_frame, bg=PALETTE["fond_principal"])
        right_stats.pack(side=RIGHT)
        
        total_fonctions = sum(len(fonctions) for fonctions in self.fonctions_bibliotheque.values())
        self.info_label = Label(right_stats, text=f"📚 {total_fonctions} fonctions disponibles",
                              font=("Century Gothic", 9), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.info_label.pack(anchor=E)

        # Bouton guide
        guide_button = ttk.Button(stats_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("dessine_fonction", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Cadre principal
        main_frame = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Instructions
        instructions_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        instructions_frame.pack(fill=X, pady=10)
        
        Label(instructions_frame, 
              text="🎯 Trace la fonction en cliquant sur le graphique ! Bibliothèque étendue : 40 linéaires, 20 constantes, 10 absolues, 35 quadratiques, 15 racines, 15 cubiques, 20 trigo, 15 exponentielles, 15 rationnelles",
              font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"], wraplength=800
        ).pack()

        # Canvas pour le graphique
        graph_frame = Frame(main_frame, bg="white", relief="solid", borderwidth=2)
        graph_frame.pack(fill=BOTH, expand=True, pady=10)
        
        # Créer le canvas
        self.canvas = Canvas(graph_frame, bg="white", width=800, height=400)
        self.canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Bind les événements de souris
        self.canvas.bind("<Button-1>", self._ajouter_point)
        self.canvas.bind("<B1-Motion>", self._dessiner_ligne)

        # Contrôles
        controles_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        controles_frame.pack(fill=X, pady=15)
        
        # Boutons gauche
        gauche_frame = Frame(controles_frame, bg=PALETTE["fond_principal"])
        gauche_frame.pack(side=LEFT)
        
        ttk.Button(gauche_frame, text="🧹 Effacer", 
                  command=self._effacer_dessin).pack(side=LEFT, padx=5)
        
        ttk.Button(gauche_frame, text="✅ Vérifier", 
                  command=self._verifier_dessin).pack(side=LEFT, padx=5)
        
        ttk.Button(gauche_frame, text="🔄 Nouvelle Fonction", 
                  command=self._nouvelle_fonction).pack(side=LEFT, padx=5)

        # Boutons droite
        droite_frame = Frame(controles_frame, bg=PALETTE["fond_principal"])
        droite_frame.pack(side=RIGHT)
        
        ttk.Button(droite_frame, text="📐 Afficher Grille", 
                  command=self._basculer_grille).pack(side=LEFT, padx=5)
        
        ttk.Button(droite_frame, text="💡 Indice", 
                  command=self._donner_indice).pack(side=LEFT, padx=5)
        
        ttk.Button(droite_frame, text="🎯 Types de Fonctions", 
                  command=self._afficher_types_fonctions).pack(side=LEFT, padx=5)

        # Feedback
        self.feedback_label = Label(main_frame, text="", 
                                   font=("Century Gothic", 12), bg=PALETTE["fond_principal"], wraplength=600)
        self.feedback_label.pack(pady=10)

        # Variables pour le dessin (état initial)
        self.dessin_actif = True
        self.dernier_point = None
        self.grille_visible = True

    def _nouvelle_fonction(self):
        """Sélectionne une fonction aléatoire et prépare les points de référence."""
        # Choisir une fonction aléatoire dans la bibliothèque du niveau actuel
        fonctions_niveau = self.fonctions_bibliotheque[self.niveau]
        self.fonction_actuelle = random.choice(fonctions_niveau)
        
        # Générer les points de référence
        self.points_corrects = self._generer_points_reference()
        
        self.points_joueur = []
        self._effacer_dessin()
        self._dessiner_graphique()
        self.fonction_label.config(text=self.fonction_actuelle["expression"])
        self.feedback_label.config(text="🎯 Trace la fonction en cliquant sur le graphique !", fg=PALETTE["primaire"])
        
        # Mettre à jour le niveau selon le score
        if self.score < 100:
            self.niveau = "Débutant"
        elif self.score < 300:
            self.niveau = "Intermédiaire"
        else:
            self.niveau = "Avancé"
        
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau}")

    def _generer_points_reference(self):
        """Génère et renvoie la liste de points (x, y) pour la fonction actuelle."""
        points = []
        type_fonction = self.fonction_actuelle["type"]
        
        # Générer plus de points pour les fonctions complexes
        if type_fonction in ["trigo", "exponentielle", "logarithmique", "rationnelle"]:
            x_values = [x * 0.5 for x in range(-8, 9)]  # Pas de 0.5
        else:
            x_values = range(-4, 5)  # Pas de 1
        
        for x in x_values:
            try:
                y = self.fonction_actuelle["fonction"](x)
                # Limiter aux bornes du graphique
                if -5 <= y <= 5:
                    points.append((x, y))
            except (ValueError, ZeroDivisionError):
                # Gérer les points où la fonction n'est pas définie
                continue
                
        return points

    def _dessiner_graphique(self):
        """Dessine le système d'axes, la grille et les points de référence."""
        if not self.canvas:
            return

        self.canvas.delete("all")
        largeur = self.canvas.winfo_width() or 800
        hauteur = self.canvas.winfo_height() or 400

        # Origine au centre et échelle
        self.origine_x = largeur // 2
        self.origine_y = hauteur // 2
        self.echelle = max(1, min(largeur, hauteur) // 10)

        # Grille
        if self.grille_visible:
            for i in range(-5, 6):
                x = self.origine_x + i * self.echelle
                y = self.origine_y + i * self.echelle
                self.canvas.create_line(x, 0, x, hauteur, fill="#E5E7EB", dash=(2, 2))
                self.canvas.create_line(0, y, largeur, y, fill="#E5E7EB", dash=(2, 2))

        # Axes
        self.canvas.create_line(0, self.origine_y, largeur, self.origine_y, fill="black", width=2)
        self.canvas.create_line(self.origine_x, 0, self.origine_x, hauteur, fill="black", width=2)

        # Graduations
        for i in range(-4, 5):
            if i == 0:
                continue
            x = self.origine_x + i * self.echelle
            y = self.origine_y + i * self.echelle
            self.canvas.create_line(x, self.origine_y - 5, x, self.origine_y + 5, fill="black")
            self.canvas.create_text(x, self.origine_y + 15, text=str(i), font=("Arial", 10))
            self.canvas.create_line(self.origine_x - 5, y, self.origine_x + 5, y, fill="black")
            self.canvas.create_text(self.origine_x - 15, y, text=str(-i), font=("Arial", 10))

        # Origine
        self.canvas.create_text(self.origine_x - 15, self.origine_y + 15, text="0", font=("Arial", 10))

        # Points de référence (en rouge)
        for x, y in self.points_corrects:
            canvas_x = self.origine_x + x * self.echelle
            canvas_y = self.origine_y - y * self.echelle
            self.canvas.create_oval(canvas_x - 4, canvas_y - 4, canvas_x + 4, canvas_y + 4, fill="red", outline="red")

    def _ajouter_point(self, event):
        """Ajoute un point au dessin (coordonnées canvas -> coordonnées mathématiques)."""
        if not self.dessin_actif:
            return

        # Conversion canvas -> math
        x_math = (event.x - self.origine_x) / self.echelle
        y_math = (self.origine_y - event.y) / self.echelle

        # Limiter aux bornes du graphique
        if -5 <= x_math <= 5 and -5 <= y_math <= 5:
            self.points_joueur.append((x_math, y_math))

            # Dessiner le point sur le canvas
            self.canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3,
                                    fill=PALETTE["primaire"], outline=PALETTE["primaire"])

            # Relier au point précédent (coordonnées canvas)
            if self.dernier_point:
                self.canvas.create_line(self.dernier_point[0], self.dernier_point[1], event.x, event.y,
                                        fill=PALETTE["primaire"], width=2)

            self.dernier_point = (event.x, event.y)

    def _dessiner_ligne(self, event):
        """Handler pour <B1-Motion> : ajoute un point au tracé continu."""
        self._ajouter_point(event)

    def _effacer_dessin(self):
        """Efface le dessin du joueur sans toucher au score ni aux points de référence."""
        self.points_joueur = []
        self.dernier_point = None
        self._dessiner_graphique()
        if hasattr(self, 'feedback_label'):
            self.feedback_label.config(text="🧹 Dessin effacé ! Trace à nouveau.", fg=PALETTE["texte_clair"])

    def _verifier_dessin(self):
        """Vérifie la précision du dessin du joueur par rapport aux points de référence."""
        if len(self.points_joueur) < 3:
            self.feedback_label.config(text="❌ Trace au moins 3 points pour vérifier", fg=PALETTE["erreur"])
            return

        self.manches_totales += 1
        precision = self._calculer_precision()

        if precision >= 0.7:
            points = self._calculer_points(precision)
            self.score += points
            self.manches_gagnees += 1
            self.feedback_label.config(text=f"✅ Excellent ! Précision: {precision:.1%} (+{points} points)", fg="#10B981")
            self._afficher_fonction_correcte()
            # Nouvelle fonction après petit délai
            if self.fenetre_jeu:
                self.fenetre_jeu.after(3000, self._nouvelle_fonction)
        else:
            self.feedback_label.config(text=f"❌ Pas assez précis ! Précision: {precision:.1%}. Essaie encore !", fg=PALETTE["erreur"])

        self._mettre_a_jour_affichage()

    def _calculer_precision(self):
        """Calcule une métrique de précision basée sur la distance moyenne aux points de référence.

        Retourne une valeur entre 0 et 1 (1 = parfait).
        """
        if not self.points_joueur or not self.points_corrects:
            return 0.0

        erreur_totale = 0.0
        for x_j, y_j in self.points_joueur:
            min_distance = float('inf')
            for x_c, y_c in self.points_corrects:
                d = math.hypot(x_j - x_c, y_j - y_c)
                if d < min_distance:
                    min_distance = d
            erreur_totale += min_distance

        erreur_moyenne = erreur_totale / len(self.points_joueur)
        precision = max(0.0, 1.0 - (erreur_moyenne / 2.0))
        return precision

    def _calculer_points(self, precision: float) -> int:
        """Calcule le score attribué en fonction de la précision et du niveau."""
        points_base = 20
        niveau_multiplier = {"Débutant": 1, "Intermédiaire": 2, "Avancé": 3}
        bonus_precision = max(0, int((precision - 0.7) * 100))
        return (points_base + bonus_precision) * niveau_multiplier.get(self.niveau, 1)

    def _afficher_fonction_correcte(self):
        """Dessine la courbe correcte (approximation par segments) en vert."""
        if not self.points_corrects:
            return
        pts = []
        for x, y in self.points_corrects:
            canvas_x = self.origine_x + x * self.echelle
            canvas_y = self.origine_y - y * self.echelle
            pts.extend([canvas_x, canvas_y])

        if len(pts) >= 4:
            self.canvas.create_line(pts, fill="#10B981", width=2, smooth=True)

    def _basculer_grille(self):
        """Active/désactive la grille et redessine le graphique et le dessin utilisateur."""
        self.grille_visible = not self.grille_visible
        self._dessiner_graphique()
        # Redessiner les points du joueur
        for x_math, y_math in self.points_joueur:
            canvas_x = self.origine_x + x_math * self.echelle
            canvas_y = self.origine_y - y_math * self.echelle
            self.canvas.create_oval(canvas_x - 3, canvas_y - 3, canvas_x + 3, canvas_y + 3, fill=PALETTE["primaire"], outline=PALETTE["primaire"])

    def _donner_indice(self):
        """Affiche un indice selon le type de fonction et applique une petite pénalité."""
        if not self.fonction_actuelle:
            return

        type_fonction = self.fonction_actuelle.get("type")
        indices = {
            "lineaire": "C'est une droite ! Regarde sa pente et son intersection avec l'axe Y.",
            "constante": "C'est une ligne horizontale ! La fonction a la même valeur pour tous les x.",
            "absolu": "Forme en V ! La fonction est toujours positive ou nulle.",
            "quadratique": "C'est une parabole ! Regarde si elle ouvre vers le haut ou le bas.",
            "racine": "Croissance lente ! La fonction n'existe que pour x >= a.",
            "cubique": "Croissance rapide ! Passe de négatif à positif.",
            "trigo": "Ondulations ! La fonction oscille périodiquement.",
            "exponentielle": "Croissance explosive ! Soit très rapide, soit décroissance.",
            "logarithmique": "Croissance très lente ! N'existe que pour x > a.",
            "rationnelle": "Asymptotes ! La fonction a des valeurs interdites."
        }

        indice = indices.get(type_fonction, "Observe bien la forme de la courbe !")
        penalite = 5
        self.score = max(0, self.score - penalite)
        if hasattr(self, 'score_label'):
            self.score_label.config(text=f"🏆 Score: {self.score}")
        messagebox.showinfo("💡 Indice", f"{indice}\n\n(–{penalite} points)")

    def _afficher_types_fonctions(self):
        """Affiche la répartition des types de fonctions de la bibliothèque."""
        types_comptage = {}
        for niveau, fonctions in self.fonctions_bibliotheque.items():
            for fonction in fonctions:
                t = fonction.get("type")
                types_comptage[t] = types_comptage.get(t, 0) + 1

        message = "📊 RÉPARTITION DES FONCTIONS PAR TYPE :\n\n"
        for type_f, count in sorted(types_comptage.items()):
            message += f"• {type_f}: {count} fonctions\n"
        message += f"\n📈 TOTAL: {sum(types_comptage.values())} fonctions disponibles"
        messagebox.showinfo("🎯 Bibliothèque des Fonctions", message)

    def _mettre_a_jour_affichage(self):
        """Actualise les labels de score / résultats."""
        if hasattr(self, 'score_label'):
            self.score_label.config(text=f"🏆 Score: {self.score}")
        if hasattr(self, 'resultats_label'):
            self.resultats_label.config(text=f"🎯 Précision: {self.manches_gagnees}/{self.manches_totales}")
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
    """Lance le Sudoku Mathématique"""
    jeu = SudokuMathematique(parent)
    jeu.lancer_jeu()

def lancer_calcul_mental_express(parent=None):
    """Lance le Calcul Mental Express"""
    jeu = CalculMentalExpress(parent)
    jeu.lancer_jeu()

def lancer_bataille_fractions(parent=None):
    """Lance la Bataille des Fractions"""
    jeu = BatailleDesFractions(parent)
    jeu.lancer_jeu()

def lancer_dessine_fonction(parent=None):
    """Lance Dessine-moi une Fonction"""
    jeu = DessineMoiUneFonction(parent)
    jeu.lancer_jeu()

# =============================================================================
# LISTE DES JEUX DISPONIBLES (pour l'interface)
# =============================================================================

JEUX_DISPONIBLES = [
    {
        "nom": "🌀 Calcul Mental Express", 
        "description": "Défie ta rapidité de calcul mental\n• Timer challengeant\n• Système de streaks et bonus\n• Progression par niveaux",
        "fonction": lancer_calcul_mental_express,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("calcul_mental_express", parent)
    },

    {
        "nom": "🎯 Math Quizz Challenge PRO",
        "description": "300 questions + Timer + Badges + Progression\n• Questions adaptatives selon votre niveau\n• Système de badges et récompenses\n• Timer avec bonus de rapidité",
        "fonction": lancer_math_quizz,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("math_quizz", parent)
    },

     {
        "nom": "🎲 Bataille des Fractions", 
        "description": "Jeu de bataille avec comparaison de fractions\n• Affronte l'ordinateur\n• Apprends les équivalences\n• Stratégie et calcul mental",
        "fonction": lancer_bataille_fractions,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("bataille_fractions", parent)
    },
    
    {
        "nom": "📈 Dessine-moi une Fonction",
        "description": "Reconnaissance visuelle de fonctions mathématiques\n• Développe l'intuition graphique\n• Apprentissage des formes de fonctions\n• Précision et observation",
        "fonction": lancer_dessine_fonction,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("dessine_fonction", parent)
    },

    {
        "nom": "🧩 Sudoku Mathématique",
        "description": "Grille Sudoku avec opérations mathématiques\n• Logique et calcul mental combinés\n• Timer avec bonus de rapidité\n• Système d'indices stratégiques",
        "fonction": lancer_sudoku_math,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("sudoku_math", parent)
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
        "nom": "🎯 Le Jeu des 24",
        "description": "Atteins 24 avec 4 nombres donnés\n• Classique des jeux mathématiques\n• Développe la créativité numérique\n• Plusieurs solutions par défi",
        "fonction": lancer_jeu_des_24,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("jeu_des_24", parent)
    }
]
