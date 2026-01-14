"""
Module central pour tous les jeux mathématiques de MathCraft
Auteur: Junior Kossivi
"""
import random
import time
import math
from tkinter import *
from tkinter import ttk, messagebox
import json, time
import os
from enum import Enum

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

# Helper pour bouton de retour uniforme (placement top-left)
def _ensure_return_style():
    try:
        from .styles import ensure_styles_configured
        ensure_styles_configured(PALETTE)
    except Exception:
        try:
            style = ttk.Style()
            style.configure("Return.Header.TButton",
                            foreground=PALETTE["fond_principal"],
                            background=PALETTE["primaire"],
                            font=("Century Gothic", 10, "bold"),
                            padding=6,
                            relief="flat")
        except Exception:
            pass


def _ajouter_bouton_retour_to_window(window, is_toplevel, on_return):
    """Ajoute un bouton Retour en haut à gauche (placement absolu)"""
    _ensure_return_style()
    try:
        btn = ttk.Button(window, text="🔙 Retour", style="Return.Header.TButton", command=on_return)
        # Place en haut à gauche, devant les autres widgets sans casser le layout
        btn.place(x=12, y=12)
    except Exception:
        try:
            ttk.Button(window, text="🔙 Retour", style="Jeu.TButton", command=on_return).place(x=12, y=12)
        except Exception:
            pass


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
    }, 
    "mystere_math": {
        "titre": "🕵️ Guide du Mystère Mathématique",
        "contenu": [
            "🎯 **Concept du jeu :**",
            "Jeu d'énigmes mathématiques mystérieuses !",
            "Résous des problèmes logiques, des casse-têtes et des mystères numériques.",
            "",
            "📝 **Comment jouer :**",
            "• Une énigme mathématique s'affiche",
            "• Tu as 5 essais pour trouver la réponse",
            "• Tu peux acheter des indices avec tes points",
            "• Plus tu résous vite, plus tu gagnes de points",
            "• Un journal garde trace de ta progression",
            "",
            "🎮 **Types d'énigmes :**",
            "• Logique numérique : nombres mystères",
            "• Proportions : problèmes de comparaison",
            "• Suites : trouver le motif",
            "• Systèmes d'équations : problèmes à plusieurs inconnues",
            "• Géométrie : calculs de formes",
            "• Probabilités : chances et statistiques",
            "• Équations complexes : transformations multiples",
            "",
            "🏅 **Système de points :**",
            "• Points de base : 50 points × multiplicateur niveau",
            "• Bonus essais : +5 points par essai restant",
            "• Malus indices : -10 points par indice utilisé",
            "• Pénalité solution : -50 points pour voir la solution",
            "• Pénalité échec : -20 points si énigme échouée",
            "• Multiplicateurs : Facile×1, Moyen×2, Difficile×3",
            "",
            "💡 **Stratégies gagnantes :**",
            "• Prends le temps de bien comprendre l'énigme",
            "• Écris les informations importantes",
            "• Utilise le journal pour noter tes réflexions",
            "• Achète des indices stratégiquement",
            "• Vérifie tes calculs avant de soumettre"
        ],
        "exemples": [
            "🧩 **Exemples d'énigmes :**",
            "",
            "Facile :",
            "« Je suis un nombre pair à deux chiffres. La somme de mes chiffres est 10. Mon chiffre des dizaines est le double de mon chiffre des unités. Qui suis-je ? »",
            "→ Réponse : 82 (8+2=10, 8=2×4)",
            "",
            "Moyen :", 
            "« Un train de 150m traverse un tunnel de 450m en 30s. Quelle est sa vitesse en km/h ? »",
            "→ Distance totale = 600m, temps = 30s → 20 m/s → 72 km/h",
            "",
            "Difficile :",
            "« Trouvez tous les nombres entiers x tels que x² + 3x - 10 < 0 »",
            "→ Factoriser : (x+5)(x-2) < 0 → -5 < x < 2 → x = -4,-3,-2,-1,0,1",
            "",
            "⚡ **Conseils de résolution :**",
            "1. Identifie le type d'énigme",
            "2. Écris toutes les données",
            "3. Cherche des relations entre les éléments",
            "4. Teste des valeurs si besoin",
            "5. Vérifie ta réponse avant de soumettre",
            "",
            "📊 **Statistiques idéales :**",
            "• Utiliser 0-1 indice par énigme",
            "• Résoudre en 2-3 essais maximum",
            "• Garder 2-3 essais en réserve",
            "• Avoir une précision > 70%"
        ]
    },"chasse_premiers": {
        "titre": "🔢 Guide de la Chasse aux Nombres Premiers",
        "contenu": [
            "🎯 **Objectif du jeu :**",
            "• Déterminer si le nombre affiché est PREMIER ou COMPOSITE",
            "• Un nombre premier n'a que 2 diviseurs : 1 et lui-même",
            "• Un nombre composite a plus de 2 diviseurs",
            "",
            "🎮 **Comment jouer :**",
            "• Vous avez 3 essais par nombre mystère",
            "• Cliquez sur '✅ OUI' si vous pensez que c'est un nombre PREMIER",
            "• Cliquez sur '❌ NON' si vous pensez que c'est un nombre COMPOSITE",
            "• Gagnez des points pour chaque bonne réponse",
            "",
            "📊 **Niveaux de difficulté :**",
            "• **Débutant** : Nombres entre 2 et 30",
            "• **Intermédiaire** : Nombres entre 30 et 200",
            "• **Avancé** : Nombres entre 200 et 1000",
            "• Le niveau augmente automatiquement avec votre score",
            "",
            "💰 **Système de points :**",
            "• **Points de base** : 20 points × multiplicateur de niveau",
            "• **Multiplicateurs** : Débutant×1, Intermédiaire×2, Avancé×3",
            "• **Bonus d'essais** : +5 points par essai restant",
            "• **Malus d'indices** : -5 points par indice utilisé",
            "• **Bonus streak** : +20 points après 5 réponses correctes consécutives",
            "",
            "💡 **Système d'indices :**",
            "• Chaque indice révélé coûte 5 points",
            "• Les indices deviennent plus précis à chaque utilisation",
            "• Le dernier indice donne souvent la réponse",
            "• Utilisez les indices stratégiquement pour économiser des points",
            "",
            "🔥 **Système de streak :**",
            "• Maintenez un enchaînement de bonnes réponses",
            "• Après 5 bonnes réponses d'affilée : bonus de 20 points",
            "• Le streak se réinitialise après une mauvaise réponse",
            "• Le meilleur streak est enregistré dans vos statistiques",
            "",
            "📈 **Statistiques suivies :**",
            "• Score total et streak actuel",
            "• Parties gagnées / parties jouées",
            "• Taux de réussite global",
            "• Nombres premiers identifiés",
            "• Nombres composites identifiés",
            "• Bonus streak cumulés",
            "",
            "🔍 **Stratégies de jeu :**",
            "1. **Vérifiez d'abord les critères évidents :**",
            "   - Si n < 2 → COMPOSITE",
            "   - Si n = 2 → PREMIER (seul premier pair)",
            "   - Si n est pair et > 2 → COMPOSITE",
            "",
            "2. **Testez les petits diviseurs :**",
            "   - Testez la divisibilité par 2, 3, 5, 7, 11",
            "   - Pour les grands nombres, testez jusqu'à √n",
            "",
            "3. **Astuces de reconnaissance :**",
            "   - Les nombres terminés par 0, 2, 4, 5, 6, 8 sont composites (sauf 2 et 5)",
            "   - Si la somme des chiffres est divisible par 3 → COMPOSITE",
            "   - Carrés parfaits sont toujours composites (sauf 1 qui n'est pas premier)",
            "",
            "❓ **Exemples de réflexion :**",
            "• 17 → Impair, pas divisible par 3, 5, 7 → PREMIER",
            "• 21 → Impair, mais 21 ÷ 3 = 7 → COMPOSITE",
            "• 29 → Impair, pas divisible par 3, 5, 7 → PREMIER (car √29≈5.4)",
            "",
            "⚠️ **Erreurs courantes à éviter :**",
            "• 1 n'est PAS un nombre premier (trop peu de diviseurs)",
            "• 2 EST un nombre premier (le seul pair)",
            "• Un nombre peut être impair mais composite (ex: 9, 15, 21)",
            "• Ne pas oublier de tester tous les diviseurs jusqu'à √n",
            "",
            "🎲 **Conseils avancés :**",
            "• Mémorisez les 25 premiers nombres premiers (jusqu'à 97)",
            "• Connaissez les critères de divisibilité (par 2, 3, 5, 7, 11)",
            "• Pour les grands nombres, cherchez un petit diviseur d'abord",
            "• Utilisez le bouton 'Explication' seulement en cas d'échec (pénalité: 10 points)"
        ],
        "exemples": [
            "🔢 **Exemples de nombres :**",
            "",
            "**NOMBRES PREMIERS (réponse : OUI)** :",
            "• 7 → OUI (diviseurs: 1, 7)",
            "• 13 → OUI (diviseurs: 1, 13)",
            "• 29 → OUI (pas divisible par 2, 3, 5, 7)",
            "• 97 → OUI (dernier premier à 2 chiffres)",
            "",
            "**NOMBRES COMPOSITES (réponse : NON)** :",
            "• 4 → NON (diviseurs: 1, 2, 4)",
            "• 15 → NON (divisible par 3 et 5)",
            "• 21 → NON (21 ÷ 3 = 7)",
            "• 49 → NON (7 × 7 = 49)",
            "",
            "**CAS PARTICULIERS :**",
            "• 1 → NON (n'est pas premier)",
            "• 2 → OUI (seul nombre premier pair)",
            "• 9 → NON (3 × 3 = 9)",
            "• 57 → NON (divisible par 3 et 19)"
        ],
        "astuces": [
            "⚡ **Astuces rapides :**",
            "• Tous les nombres pairs > 2 sont composites",
            "• Tous les nombres terminés par 5 > 5 sont composites",
            "• Si la somme des chiffres est 3, 6, ou 9 → divisible par 3",
            "• Carrés de nombres premiers sont composites (ex: 25 = 5²)",
            "",
            "🎯 **Pour les grands nombres :**",
            "• Vérifiez d'abord les petits nombres premiers (2, 3, 5, 7, 11)",
            "• Calculez √n pour savoir jusqu'où tester",
            "• Un nombre impair n'est pas forcément premier !",
            "",
            "🏆 **Objectifs à atteindre :**",
            "• Bronze : Score de 100 points",
            "• Argent : Score de 300 points avec streak de 5",
            "• Or : Score de 500 points avec 80% de réussite",
            "• Diamant : Score de 1000 points et identification de 50 nombres"
        ]
    },"math_battle": {
    "titre": "⚔️ Math Battle – Ultimate Challenge",
    "contenu": [
        "📝 **Comment jouer :**",
        "• Choisissez votre niveau (Débutant, Intermédiaire, Expert)",
        "• Répondez aux énigmes mathématiques avant la fin du chrono",
        "• Plus vous répondez vite, plus vous gagnez de points bonus",
        "• Les énigmes deviennent plus difficiles au fur et à mesure",
        "",
        "🎮 **Types de questions :**",
        "• Arithmétique : additions, soustractions, multiplications, divisions",
        "• Algèbre : équations simples, systèmes, polynômes",
        "• Géométrie : aires, périmètres, théorème de Pythagore",
        "• Suites et logique : arithmétiques, géométriques, Fibonacci, look-and-say",
        "• Racines et puissances : √, ², ³, puissances entières",
        "• Nombres spéciaux : premiers, parfaits, palindromes",
        "",
        "🏆 **Système de points :**",
        "• Débutant : 10 points par énigme",
        "• Intermédiaire : 20 points par énigme",
        "• Expert : 30 points par énigme",
        "• Bonus rapidité : +2 à +10 points selon le temps restant",
        "",
        "💡 **Conseils stratégiques :**",
        "• Entraînez-vous sur les tables de multiplication et les carrés parfaits",
        "• Mémorisez les valeurs trigonométriques des angles courants (30°, 45°, 60°, 90°)",
        "• Gérez votre temps – ne restez pas bloqué sur une énigme",
        "• Utilisez la logique pour éliminer les mauvaises réponses"
    ],
    "exemples": [
        "🧮 **Exemples d’énigmes :**",
        "Débutant : 12 ÷ 3 = ? → 4",
        "Intermédiaire : √225 = ? → 15",
        "Expert : log₂(32) = ? → 5"
    ],
    "interface": [
        "📊 **Affichage :**",
        "• Barre de progression du chrono",
        "• Score en temps réel",
        "• Niveau actuel et nombre d’énigmes restantes",
        "",
        "🎨 **Design :**",
        "• Couleurs dynamiques selon le niveau (Vert = Débutant, Orange = Intermédiaire, Rouge = Expert)",
        "• Effets visuels quand une réponse est correcte (+ points)",
        "• Animation spéciale quand un niveau est terminé"
    ]
},"defis_fibonacci": {
    "titre": "🌟 Guide du Défi Fibonacci",
    "contenu": [
        "📝 **Comment jouer :**",
        "• Complétez les suites de Fibonacci ou résolvez des énigmes liées",
        "• Plus vous répondez vite, plus vous gagnez de points bonus",
        "• Les suites deviennent plus longues et complexes avec votre score",
        "",
        "🎮 **Types de questions :**",
        "• Suites simples : trouver le prochain terme",
        "• Positions : identifier Fn pour un n donné",
        "• Calculs : sommes, différences, produits de termes",
        "• Logique : retrouver des termes manquants",
        "• Théorie : propriétés avancées (nombre d’or, formule de Binet)",
        "",
        "🏆 **Système de points :**",
        "• Débutant : 10 points par question",
        "• Intermédiaire : 20 points par question",
        "• Expert : 30 points par question",
        "• Bonus rapidité : +2 à +10 points selon le temps restant",
        "",
        "💡 **Conseils stratégiques :**",
        "• Mémorisez les premiers termes de la suite (jusqu’à F20)",
        "• Comprenez la relation Fn+2 = Fn+1 + Fn",
        "• Utilisez la formule de Binet pour les grands n",
        "• Gérez votre temps - ne restez pas bloqué sur une énigme"
    ],
    "exemples": [
        "🧮 **Exemples de questions :**",
        "Débutant : 0, 1, 1, 2, 3, ? → 5",
        "Intermédiaire : Fn = 34, trouver n → 9",
        "Expert : Limite Fn+1/Fn quand n → ∞ → φ ≈ 1.618"
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
              style="Jeu.TButton", command=fenetre_guide.destroy).pack(pady=20)
    
    # Espace final
    Label(scrollable_frame, text="", bg=PALETTE["fond_principal"], height=2).pack()

# =============================================================================
# INTERFACE DE SÉLECTION DES JEUX AVEC SCROLLBAR
# =============================================================================

def creer_interface_jeux(parent=None):
    """Crée l'interface de sélection des jeux avec scrollbar"""
    if parent:
        fenetre_jeux = parent
        for child in list(fenetre_jeux.winfo_children()):
            child.destroy()
        try:
            fenetre_jeux.title("🎮 MathCraft - Sélection des Jeux")
            fenetre_jeux.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass
    else:
        fenetre_jeux = Tk()
        fenetre_jeux.title("🎮 MathCraft - Sélection des Jeux")
        fenetre_jeux.geometry("900x800")
        fenetre_jeux.configure(bg=PALETTE["fond_principal"])
    
    # Style
    try:
        from .styles import ensure_styles_configured
        ensure_styles_configured(PALETTE)
    except Exception:
        pass
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
                                  command=lambda f=jeu["fonction"]: f(fenetre_jeux))
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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🎯 Math Quizz Challenge Pro")
            self.fenetre_jeu.geometry("700x800")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface_avance()
        self._prochaine_question()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface_avance(self):
        """Crée l'interface avancée avec timer et progression"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🎯 MATH QUIZZ CHALLENGE PRO", 
              font=("Century Gothic", 20, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Cadre scrollable pour le contenu du jeu (garde l'en-tête fixe)
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Frame des statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
        progress_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
        self.badges_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        self.badges_frame.pack(fill=X, padx=20, pady=10) 
        
        self.badges_label = Label(self.badges_frame, text="🎖️ Badges: Aucun pour le moment",
                                 font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.badges_label.pack(anchor=W)

        # Bouton guide
        guide_button = ttk.Button(self.badges_frame, text="📚 Guide du jeu", 
                                 command=lambda: afficher_guide_jeu("math_quizz", self.fenetre_jeu), style="Guide.TButton")
        guide_button.pack(side=RIGHT, padx=10)

        # Séparateur
        ttk.Separator(content_frame, orient='horizontal').pack(fill=X, padx=20, pady=10)

        # Question
        question_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        question_frame.pack(fill=BOTH, expand=True, padx=20, pady=20) 
        
        self.question_label = Label(question_frame, text="", font=("Century Gothic", 18, "bold"),
                                   bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], wraplength=600, justify="center")
        self.question_label.pack(pady=30)

        # Réponse
        reponse_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
        buttons_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=20, pady=20) 
        
        ttk.Button(buttons_frame, text="✅ Vérifier la réponse", style="Jeu.TButton", 
                  command=self._verifier_reponse).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="➡️ Question suivante", style="Jeu.TButton", 
                  command=self._prochaine_question).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="📊 Voir les badges", style="Jeu.TButton", 
                  command=self._afficher_badges).pack(side=RIGHT, padx=10)

        # Feedback
        self.feedback_label = Label(content_frame, text="", font=("Century Gothic", 13), 
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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🏆 Course aux Nombres")
            self.fenetre_jeu.geometry("800x700")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            self.fenetre_jeu.protocol("WM_DELETE_WINDOW", self._fermer_jeu)
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouveau_defi()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🏆 COURSE AUX NOMBRES", 
              font=("Century Gothic", 20, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                                 style="Jeu.TButton", command=lambda: afficher_guide_jeu("course_nombres", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Cible
        cible_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        cible_frame.pack(fill=X, padx=20, pady=20)
        
        Label(cible_frame, text="🎯 CIBLE À ATTEINDRE:", 
              font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.cible_label = Label(cible_frame, text="", 
                                font=("Century Gothic", 40, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["erreur"])
        self.cible_label.pack(pady=10)

        # Nombres disponibles
        nombres_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        nombres_frame.pack(fill=X, padx=20, pady=15)
        
        Label(nombres_frame, text="🔢 NOMBRES DISPONIBLES:", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=5)
        
        self.nombres_frame = Frame(nombres_frame, bg=PALETTE["fond_principal"])
        self.nombres_frame.pack(pady=10)

        # Zone de saisie
        saisie_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
        buttons_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=20, pady=15)
        
        ttk.Button(buttons_frame, text="✅ Vérifier le calcul", 
                  style="Jeu.TButton", command=self._verifier_calcul).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouveau défi", 
                  style="Jeu.TButton", command=self._nouveau_defi).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Voir solutions", 
                  style="Jeu.TButton", command=self._afficher_solutions).pack(side=RIGHT, padx=10)

        # Solutions trouvées
        solutions_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
        self.feedback_label = Label(content_frame, text="", 
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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🎯 Le Jeu des 24")
            self.fenetre_jeu.geometry("700x600")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouveau_defi()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🎯 LE JEU DES 24", 
              font=("Century Gothic", 20, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        self.score_label = Label(stats_frame, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 14, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        self.niveau_label = Label(stats_frame, text=f"📊 Niveau: {self.niveau}",
                                 font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
        self.niveau_label.pack(side=LEFT, padx=20)

        # Cible fixe (toujours 24)
        cible_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                  style="Jeu.TButton", command=self._verifier_calcul).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouveau défi", 
                  style="Jeu.TButton", command=self._nouveau_defi).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Voir solutions", 
                  style="Jeu.TButton", command=self._afficher_solutions).pack(side=RIGHT, padx=10)

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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🍎 Math Emoji")
            self.fenetre_jeu.geometry("700x600")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_equation()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 20))
        
        Label(header_frame, text="🍎 MATH EMOJI 🍌", 
              font=("Comic Sans MS", 22, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=15)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                                 command=lambda: afficher_guide_jeu("math_emoji", self.fenetre_jeu), style="Guide.TButton")
        guide_button.pack(side=RIGHT, padx=10)

        # Équations
        equations_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        equations_frame.pack(fill=X, padx=30, pady=20)
        
        Label(equations_frame, text="🧮 RÉSOUS CES ÉQUATIONS :", 
              font=("Arial", 14, "bold"), bg=PALETTE["fond_principal"]).pack(pady=10)
        
        self.equations_text = Text(equations_frame, height=4, font=("Arial", 16),
                                  bg="#FFF9C4", fg=PALETTE["texte_fonce"], wrap=WORD, 
                                  relief="solid", borderwidth=1)
        self.equations_text.pack(fill=X, pady=10)
        self.equations_text.config(state=DISABLED)

        # Zone de réponses
        reponses_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        reponses_frame.pack(fill=X, padx=30, pady=15)
        
        Label(reponses_frame, text="✏️ TES RÉPONSES :", 
              font=("Arial", 12, "bold"), bg=PALETTE["fond_principal"]).pack(pady=10)
        
        self.reponses_frame = Frame(reponses_frame, bg=PALETTE["fond_principal"])
        self.reponses_frame.pack(pady=10)

        # Boutons
        buttons_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=30, pady=20)
        
        ttk.Button(buttons_frame, text="✅ Vérifier les réponses", style="Jeu.TButton", 
                  command=self._verifier_reponses).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="🔄 Nouvelle équation", style="Jeu.TButton", 
                  command=self._nouvelle_equation).pack(side=LEFT, padx=10)
        
        ttk.Button(buttons_frame, text="💡 Indice", 
                  style="Jeu.TButton", command=self._donner_indice).pack(side=RIGHT, padx=10)

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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🌀 Calcul Mental Express")
            self.fenetre_jeu.geometry("600x500")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_question()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🌀 CALCUL MENTAL EXPRESS", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques en temps réel
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
        self.progress_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        self.progress_frame.pack(fill=X, padx=50, pady=5)
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient=HORIZONTAL, 
                                          length=400, mode='determinate', maximum=self.temps_limite)
        self.progress_bar.pack(fill=X)
        self.progress_bar['value'] = self.temps_limite

        # Zone de question
        question_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        question_frame.pack(fill=BOTH, expand=True, padx=40, pady=20)
        
        Label(question_frame, text="CALCULE RAPIDEMENT :", 
              font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack(pady=(10, 20))
        
        self.question_label = Label(question_frame, text="", 
                                   font=("Century Gothic", 28, "bold"), 
                                   bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
        self.question_label.pack(pady=20)

        # Zone de réponse
        reponse_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        reponse_frame.pack(fill=X, padx=40, pady=15)
        
        self.reponse_entry = Entry(reponse_frame, font=("Century Gothic", 18), 
                                  width=15, justify="center")
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse())
        self.reponse_entry.focus()

        # Boutons
        buttons_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
        buttons_frame.pack(fill=X, padx=40, pady=15)
        
        ttk.Button(buttons_frame, text="✅ Vérifier", 
                  style="Jeu.TButton", command=self._verifier_reponse).pack(side=LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="➡️ Passer", 
                  style="Jeu.TButton", command=self._nouvelle_question).pack(side=LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="📚 Guide", 
                  style="Jeu.TButton", command=lambda: afficher_guide_jeu("calcul_mental_express", self.fenetre_jeu)).pack(side=RIGHT, padx=5)

        # Feedback
        self.feedback_label = Label(content_frame, text="", 
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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🧩 Sudoku Mathématique")
            self.fenetre_jeu.geometry("800x700")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_grille()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🧩 SUDOKU MATHÉMATIQUE", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                                 style="Jeu.TButton", command=lambda: afficher_guide_jeu("sudoku_math", self.fenetre_jeu))
        guide_button.pack(side=RIGHT, padx=10)

        # Cadre principal pour la grille
        main_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                           style="Jeu.TButton", command=lambda num=i: self._inserer_chiffre(num))
            btn.grid(row=(i-1)//3, column=(i-1)%3, padx=2, pady=2)

        # Boutons d'action
        action_frame = Frame(saisie_frame, bg=PALETTE["fond_principal"])
        action_frame.pack(pady=10)

        ttk.Button(action_frame, text="🔍 Vérifier la grille", 
                  style="Jeu.TButton", command=self._verifier_grille).pack(side=LEFT, padx=5)
        
        ttk.Button(action_frame, text="🧹 Effacer la case", 
                  style="Jeu.TButton", command=self._effacer_case).pack(side=LEFT, padx=5)
        
        ttk.Button(action_frame, text="🔄 Nouvelle grille", 
                  style="Jeu.TButton", command=self._nouvelle_grille).pack(side=LEFT, padx=5)
        
        ttk.Button(action_frame, text="💡 Indice", 
                  style="Jeu.TButton", command=self._donner_indice).pack(side=RIGHT, padx=5)

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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🎲 Bataille des Fractions")
            self.fenetre_jeu.geometry("800x700")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_partie()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🎲 BATAILLE DES FRACTIONS", 
              font=("Century Gothic", 18, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                                 command=lambda: afficher_guide_jeu("bataille_fractions", self.fenetre_jeu), style="Guide.TButton")
        guide_button.pack(side=RIGHT, padx=10)

        # Zone de jeu principale
        jeu_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                  style="Jeu.TButton", command=self._nouvelle_partie).pack(side=LEFT, padx=5)
        
        ttk.Button(actions_frame, text="💡 Aide Comparaison", 
                  style="Jeu.TButton", command=self._afficher_aide_comparaison).pack(side=LEFT, padx=5)
        
        ttk.Button(actions_frame, text="🎯 Stratégie", 
                  style="Jeu.TButton", command=self._afficher_strategie).pack(side=RIGHT, padx=5)

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
                           style="Jeu.TButton", command=lambda c=carte: self._jouer_carte(c))
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
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("📈 Dessine-moi une Fonction - Version Enrichie")
            self.fenetre_jeu.geometry("900x750")
            self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_fonction()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Construire l'interface Tkinter pour le jeu."""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="📈 DESSINE-MOI UNE FONCTION - BIBLIOTHÈQUE ÉTENDUE", 
              font=("Century Gothic", 16, "bold"), bg=PALETTE["primaire"], fg="white").pack(pady=12)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                                 command=lambda: afficher_guide_jeu("dessine_fonction", self.fenetre_jeu), style="Guide.TButton")
        guide_button.pack(side=RIGHT, padx=10)

        # Cadre principal
        main_frame = Frame(content_frame, bg=PALETTE["fond_principal"])
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
                  style="Jeu.TButton", command=self._effacer_dessin).pack(side=LEFT, padx=5)
        
        ttk.Button(gauche_frame, text="✅ Vérifier", 
                  style="Jeu.TButton", command=self._verifier_dessin).pack(side=LEFT, padx=5)
        
        ttk.Button(gauche_frame, text="🔄 Nouvelle Fonction", 
                  style="Jeu.TButton", command=self._nouvelle_fonction).pack(side=LEFT, padx=5)

        # Boutons droite
        droite_frame = Frame(controles_frame, bg=PALETTE["fond_principal"])
        droite_frame.pack(side=RIGHT)
        
        ttk.Button(droite_frame, text="📐 Afficher Grille", 
                  style="Jeu.TButton", command=self._basculer_grille).pack(side=LEFT, padx=5)
        
        ttk.Button(droite_frame, text="💡 Indice", 
                  style="Jeu.TButton", command=self._donner_indice).pack(side=LEFT, padx=5)
        
        ttk.Button(droite_frame, text="🎯 Types de Fonctions", 
                  style="Jeu.TButton", command=self._afficher_types_fonctions).pack(side=LEFT, padx=5)

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
# MYSTÈRE MATHÉMATIQUE
# =============================================================================

"""Classe Repertoriant les difficulté"""
class Difficulty(Enum):
    DEBUTANT = "Débutant"
    INTERMEDIAIRE = "Intermédiaire"
    EXPERT = "Expert"

class EnigmeManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.enigmes_data = self._load_enigmes()
    
    def _load_enigmes(self):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Erreur : Fichier {self.json_file_path} non trouvé.")
            return {}
        except json.JSONDecodeError:
            print(f"Erreur : Fichier {self.json_file_path} mal formaté.")
            return {}
    
    def get_enigmes_by_difficulty(self, difficulty):
        if difficulty.value in self.enigmes_data:
            return self.enigmes_data[difficulty.value]
        return []
    
    def get_random_enigme(self, difficulty=None):
        if difficulty:
            enigmes = self.get_enigmes_by_difficulty(difficulty)
        else:
            enigmes = []
            for diff in self.enigmes_data.values():
                enigmes.extend(diff)
        
        if not enigmes:
            return None
        
        return random.choice(enigmes)
    
    def get_enigmes_by_type(self, difficulty, enigme_type):
        enigmes = self.get_enigmes_by_difficulty(difficulty)
        return [enigme for enigme in enigmes if enigme.get('type') == enigme_type]
    
    def add_enigme(self, difficulty, question, reponse, indices, enigme_type):
        if difficulty.value not in self.enigmes_data:
            self.enigmes_data[difficulty.value] = []
        
        new_enigme = {
            "question": question,
            "reponse": reponse,
            "indices": indices,
            "type": enigme_type
        }
        
        self.enigmes_data[difficulty.value].append(new_enigme)
        self._save_enigmes()
    
    def _save_enigmes(self):
        try:
            with open(self.json_file_path, 'w', encoding='utf-8') as f:
                json.dump(self.enigmes_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")
    
    def get_all_enigmes_count(self):
        total = 0
        for difficulty, enigmes in self.enigmes_data.items():
            total += len(enigmes)
        return total
    
    def get_difficulty_stats(self):
        stats = {}
        for difficulty, enigmes in self.enigmes_data.items():
            stats[difficulty] = len(enigmes)
        return stats


import os

class MystereMathematique:
    def __init__(self, parent, json_file_path=None):
        self.parent = parent
        self.score = 0
        self.niveau = Difficulty.DEBUTANT
        self.mystere_actuel = None
        self.indices_decouverts = 0
        self.essais_restants = 5
        self.parties_gagnees = 0
        self.parties_jouees = 0
        
        # Utiliser EnigmeManager pour charger les énigmes
        if json_file_path is None:
            # Chercher dans le dossier data
            if os.path.exists("data/question_enigme.json"):
                json_file_path = "data/question_enigme.json"
            elif os.path.exists("../data/question_enigme.json"):
                json_file_path = "../data/question_enigme.json"
            else:
                # Créer le chemin si le dossier existe
                if os.path.exists("data"):
                    json_file_path = "data/question_enigme.json"
                else:
                    json_file_path = "question_enigme.json"
        
        self.enigme_manager = EnigmeManager(json_file_path)
        
        # Palette de couleurs par défaut
        self.PALETTE = {
            "fond_principal": "#FFFFFF",
            "primaire": "#2563EB",
            "secondaire": "#7C3AED",
            "succes": "#10B981",
            "erreur": "#EF4444",
            "avertissement": "#F59E0B",
            "texte_fonce": "#1F2937",
            "texte_clair": "#6B7280",
            "fond_clair": "#F3F4F6"
        }
    
    def lancer_jeu(self):
        """Lance le Mystère Mathématique"""
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🕵️ Mystère Mathématique")
            self.fenetre_jeu.geometry("800x700")
            self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_enigme()

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass

    def _creer_interface(self):
        """Crée l'interface du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=self.PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 15))
        
        Label(header_frame, text="🕵️ MYSTÈRE MATHÉMATIQUE", 
              font=("Century Gothic", 18, "bold"), bg=self.PALETTE["primaire"], fg="white").pack(pady=12)

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=self.PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, self.PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=self.PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques
        stats_frame = Frame(content_frame, bg=self.PALETTE["fond_principal"])
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Score et niveau
        left_stats = Frame(stats_frame, bg=self.PALETTE["fond_principal"])
        left_stats.pack(side=LEFT)
        
        self.score_label = Label(left_stats, text=f"🏆 Score: {self.score}",
                                font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["primaire"])
        self.score_label.pack(anchor=W)
        
        self.niveau_label = Label(left_stats, text=f"📊 Niveau: {self.niveau.value}",
                                 font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_clair"])
        self.niveau_label.pack(anchor=W)
        
        # Essais restants
        center_stats = Frame(stats_frame, bg=self.PALETTE["fond_principal"])
        center_stats.pack(side=LEFT, expand=True)
        
        self.essais_label = Label(center_stats, text=f"🎯 Essais restants: {self.essais_restants}",
                                 font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["primaire"])
        self.essais_label.pack()
        
        self.resultats_label = Label(center_stats, text=f"📈 Parties: {self.parties_gagnees}/{self.parties_jouees}",
                                    font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_clair"])
        self.resultats_label.pack()

        # Type d'énigme
        right_stats = Frame(stats_frame, bg=self.PALETTE["fond_principal"])
        right_stats.pack(side=RIGHT)
        
        self.type_label = Label(right_stats, text=f"🔍 Type: ?",
                              font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_clair"])
        self.type_label.pack(anchor=E)

        # Cadre principal
        main_frame = Frame(content_frame, bg=self.PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Énigme
        enigme_frame = Frame(main_frame, bg="#FEF3C7", relief="solid", borderwidth=2)
        enigme_frame.pack(fill=X, pady=15, padx=10)
        
        Label(enigme_frame, text="🧩 ÉNIGME MYSTÈRE :", 
              font=("Century Gothic", 12, "bold"), bg="#FEF3C7", fg="#92400E").pack(pady=10)
        
        self.enigme_text = Text(enigme_frame, height=6, font=("Century Gothic", 11),
                               bg="#FEF3C7", fg="#92400E", wrap=WORD, relief="flat")
        self.enigme_text.pack(fill=X, padx=15, pady=10)
        self.enigme_text.config(state=DISABLED)

        # Indices
        indices_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        indices_frame.pack(fill=X, pady=15)
        
        Label(indices_frame, text="💡 INDICES DISPONIBLES :", 
              font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        self.indices_frame = Frame(indices_frame, bg=self.PALETTE["fond_principal"])
        self.indices_frame.pack(pady=10)

        # Saisie de réponse
        reponse_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        reponse_frame.pack(fill=X, pady=15)
        
        Label(reponse_frame, text="✏️ TA RÉPONSE :", 
              font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        self.reponse_entry = Entry(reponse_frame, font=("Century Gothic", 14), 
                                  width=30, justify="center")
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse())
        
        Label(reponse_frame, text="(Tu peux entrer plusieurs réponses séparées par des virgules si besoin)", 
              font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_clair"]).pack()

        # Boutons
        boutons_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        boutons_frame.pack(fill=X, pady=15)
        
        ttk.Button(boutons_frame, text="🔍 Obtenir un indice", 
                  style="Jeu.TButton", command=self._obtenir_indice).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="✅ Vérifier la réponse", 
                  style="Jeu.TButton", command=self._verifier_reponse).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="🔄 Nouvelle énigme", 
                  style="Jeu.TButton", command=self._nouvelle_enigme).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="💡 Solution complète", 
                  style="Jeu.TButton", command=self._afficher_solution).pack(side=RIGHT, padx=5)

        # Feedback
        self.feedback_label = Label(main_frame, text="", 
                                   font=("Century Gothic", 12), bg=self.PALETTE["fond_principal"], wraplength=600)
        self.feedback_label.pack(pady=10)

        # Zone de log
        log_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        log_frame.pack(fill=BOTH, expand=True, pady=10)
        
        Label(log_frame, text="📝 JOURNAL DE RÉSOLUTION :", 
              font=("Century Gothic", 10, "bold"), bg=self.PALETTE["fond_principal"]).pack(anchor=W)
        
        self.log_text = Text(log_frame, height=6, font=("Century Gothic", 9),
                            bg="#F8FAFC", fg=self.PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)
        self.log_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.log_text.config(state=DISABLED)

    def _nouvelle_enigme(self):
        """Prépare une nouvelle énigme"""
        # Mettre à jour le niveau selon le score
        if self.score < 200:
            self.niveau = Difficulty.DEBUTANT
        elif self.score < 500:
            self.niveau = Difficulty.INTERMEDIAIRE
        else:
            self.niveau = Difficulty.EXPERT
        
        # Obtenir une énigme aléatoire
        self.mystere_actuel = self.enigme_manager.get_random_enigme(self.niveau)
        
        if not self.mystere_actuel:
            self.feedback_label.config(text="❌ Aucune énigme disponible pour ce niveau", fg=self.PALETTE["erreur"])
            return
        
        # Réinitialiser les compteurs
        self.indices_decouverts = 0
        self.essais_restants = 5
        
        # Mettre à jour l'interface
        self._afficher_enigme()
        self._afficher_indices()
        self.reponse_entry.delete(0, END)
        self.feedback_label.config(text="🎯 Résous le mystère ! Tu as 5 essais.", fg=self.PALETTE["primaire"])
        self._effacer_log()
        self._ajouter_log("🕵️ Nouvelle énigme chargée !")
        
        # Mettre à jour les labels
        self.niveau_label.config(text=f"📊 Niveau: {self.niveau.value}")
        self.type_label.config(text=f"🔍 Type: {self.mystere_actuel.get('type', 'Inconnu')}")
        
        self._mettre_a_jour_affichage()

    def _afficher_enigme(self):
        """Affiche l'énigme dans la zone de texte"""
        self.enigme_text.config(state=NORMAL)
        self.enigme_text.delete(1.0, END)
        self.enigme_text.insert(END, self.mystere_actuel["question"])
        self.enigme_text.config(state=DISABLED)

    def _afficher_indices(self):
        """Affiche les indices disponibles"""
        # Nettoyer le frame
        for widget in self.indices_frame.winfo_children():
            widget.destroy()
        
        indices = self.mystere_actuel.get("indices", [])
        
        # Afficher les indices déjà découverts
        for i in range(len(indices)):
            if i < self.indices_decouverts:
                # Indice révélé
                Label(self.indices_frame, text=f"💡 {indices[i]}", 
                      font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], fg="#10B981", 
                      wraplength=600, justify="left").pack(anchor=W, pady=2)
            else:
                # Indice caché
                Label(self.indices_frame, text=f"🔒 Indice {i+1} (coût: 10 points)", 
                      font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_clair"], 
                      wraplength=600, justify="left").pack(anchor=W, pady=2)

    def _obtenir_indice(self):
        """Donne un indice au joueur"""
        indices = self.mystere_actuel.get("indices", [])
        
        if self.indices_decouverts >= len(indices):
            self.feedback_label.config(text="❌ Plus d'indices disponibles", fg=self.PALETTE["erreur"])
            return
        
        # Pénalité de points
        penalite = 10
        if self.score >= penalite:
            self.score -= penalite
            self.indices_decouverts += 1
            
            self._ajouter_log(f"📉 Achat d'indice: -{penalite} points")
            self.feedback_label.config(text=f"💡 Indice {self.indices_decouverts} révélé ! (-{penalite} points)", 
                                     fg="#F59E0B")
            
            self._afficher_indices()
            self._mettre_a_jour_affichage()
        else:
            self.feedback_label.config(text="❌ Pas assez de points pour un indice", fg=self.PALETTE["erreur"])

    def _verifier_reponse(self):
        """Vérifie la réponse du joueur"""
        reponse_joueur = self.reponse_entry.get().strip()
        
        if not reponse_joueur:
            self.feedback_label.config(text="❌ Entre une réponse", fg=self.PALETTE["erreur"])
            return
        
        self.essais_restants -= 1
        self.essais_label.config(text=f"🎯 Essais restants: {self.essais_restants}")
        self.parties_jouees += 1
        
        reponse_correcte = self.mystere_actuel.get("reponse")
        
        # Gestion des réponses multiples (listes)
        if isinstance(reponse_correcte, list):
            # Convertir la réponse du joueur en liste
            try:
                reponses_joueur = [self._convertir_reponse(r.strip()) for r in reponse_joueur.split(',')]
                reponses_joueur.sort()
                reponses_correctes = sorted(reponse_correcte)
                
                if reponses_joueur == reponses_correctes:
                    self._reussite_enigme()
                else:
                    self._echec_essai(reponse_joueur)
            except:
                self._echec_essai(reponse_joueur)
        else:
            # Réponse unique
            try:
                reponse_joueur_num = self._convertir_reponse(reponse_joueur)
                reponse_correcte_num = self._convertir_reponse(reponse_correcte)
                
                if reponse_joueur_num == reponse_correcte_num:
                    self._reussite_enigme()
                else:
                    self._echec_essai(reponse_joueur)
            except ValueError:
                # Vérification textuelle
                if str(reponse_joueur).lower() == str(reponse_correcte).lower():
                    self._reussite_enigme()
                else:
                    self._echec_essai(reponse_joueur)
        
        # Vérifier si plus d'essais
        if self.essais_restants <= 0:
            self._enigme_echouee()

    def _convertir_reponse(self, reponse):
        """Convertit une réponse en nombre si possible"""
        try:
            # Essayer de convertir en float
            return float(reponse)
        except ValueError:
            try:
                # Essayer de convertir en int
                return int(reponse)
            except ValueError:
                # Retourner la réponse telle quelle
                return reponse

    def _reussite_enigme(self):
        """Quand l'énigme est résolue"""
        points = self._calculer_points()
        self.score += points
        self.parties_gagnees += 1
        
        reponse = self.mystere_actuel.get("reponse")
        reponse_text = str(reponse)
        if isinstance(reponse, list):
            reponse_text = ", ".join(str(x) for x in reponse)
        
        self.feedback_label.config(
            text=f"🎉 BRAVO ! Réponse correcte : {reponse_text} (+{points} points)", 
            fg="#10B981"
        )
        
        self._ajouter_log(f"✅ ENIGME RÉSOLUE ! +{points} points")
        self._mettre_a_jour_affichage()
        
        # Nouvelle énigme après délai
        self.fenetre_jeu.after(3000, self._nouvelle_enigme)

    def _echec_essai(self, reponse_joueur):
        """Quand un essai échoue"""
        self.feedback_label.config(
            text=f"❌ Réponse incorrecte : {reponse_joueur}", 
            fg=self.PALETTE["erreur"]
        )
        
        self._ajouter_log(f"❌ Essai incorrect: {reponse_joueur}")
        
        if self.essais_restants > 0:
            self.feedback_label.config(
                text=f"❌ Réponse incorrecte. Il te reste {self.essais_restants} essai{'s' if self.essais_restants > 1 else ''}.", 
                fg=self.PALETTE["erreur"]
            )

    def _enigme_echouee(self):
        """Quand l'énigme n'est pas résolue à temps"""
        reponse = self.mystere_actuel.get("reponse")
        reponse_text = str(reponse)
        if isinstance(reponse, list):
            reponse_text = ", ".join(str(x) for x in reponse)
        
        self.feedback_label.config(
            text=f"💥 Énigme échouée ! La réponse était : {reponse_text}", 
            fg=self.PALETTE["erreur"]
        )
        
        self._ajouter_log(f"💥 ÉCHEC - Réponse: {reponse_text}")
        
        # Pénalité pour échec
        penalite = 20
        self.score = max(0, self.score - penalite)
        
        self._ajouter_log(f"📉 Pénalité d'échec: -{penalite} points")
        self._mettre_a_jour_affichage()
        
        # Nouvelle énigme après délai
        self.fenetre_jeu.after(4000, self._nouvelle_enigme)

    def _calculer_points(self):
        """Calcule les points gagnés pour une énigme résolue"""
        points_base = 50
        niveau_multiplier = {
            Difficulty.DEBUTANT: 1, 
            Difficulty.INTERMEDIAIRE: 2, 
            Difficulty.EXPERT: 3
        }
        
        # Bonus pour rapidité (beaucoup d'essais restants)
        bonus_essais = self.essais_restants * 5
        
        # Malus pour indices utilisés
        malus_indices = self.indices_decouverts * 10
        
        points = (points_base + bonus_essais - malus_indices) * niveau_multiplier.get(self.niveau, 1)
        
        # Minimum de 10 points
        return max(10, points)

    def _afficher_solution(self):
        """Affiche la solution complète"""
        # Pénalité importante
        penalite = 50
        self.score = max(0, self.score - penalite)
        
        solution_window = Toplevel(self.fenetre_jeu)
        solution_window.title("💡 Solution Complète")
        solution_window.geometry("600x400")
        solution_window.configure(bg=self.PALETTE["fond_principal"])
        
        Label(solution_window, text="💡 SOLUTION COMPLÈTE", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["primaire"]).pack(pady=20)
        
        # Énigme
        Label(solution_window, text="Énigme:", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        Label(solution_window, text=self.mystere_actuel.get("question", ""), 
              font=("Century Gothic", 11), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_fonce"], 
              wraplength=500, justify="center").pack(pady=5)
        
        # Réponse
        Label(solution_window, text="\nRéponse:", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        reponse = self.mystere_actuel.get("reponse")
        reponse_text = str(reponse)
        if isinstance(reponse, list):
            reponse_text = ", ".join(str(x) for x in reponse)
        
        Label(solution_window, text=reponse_text, 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["fond_principal"], fg="#10B981").pack(pady=5)
        
        # Explication
        Label(solution_window, text="\nExplication:", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        indices = self.mystere_actuel.get("indices", [])
        explication_text = "\n".join(indices)
        Label(solution_window, text=explication_text, 
              font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_clair"], 
              wraplength=500, justify="left").pack(pady=5)
        
        Label(solution_window, text=f"\n(–{penalite} points)", 
              font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_principal"], fg=self.PALETTE["erreur"]).pack(pady=10)
        
        ttk.Button(solution_window, text="Fermer", style="Jeu.TButton", 
                  command=solution_window.destroy).pack(pady=10)
        
        self._ajouter_log(f"📉 Solution achetée: -{penalite} points")
        self._mettre_a_jour_affichage()

    def _ajouter_log(self, message):
        """Ajoute un message au journal"""
        self.log_text.config(state=NORMAL)
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(END, f"[{timestamp}] {message}\n")
        self.log_text.see(END)
        self.log_text.config(state=DISABLED)

    def _effacer_log(self):
        """Efface le journal"""
        self.log_text.config(state=NORMAL)
        self.log_text.delete(1.0, END)
        self.log_text.config(state=DISABLED)

    def _mettre_a_jour_affichage(self):
        """Met à jour tous les affichages"""
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.resultats_label.config(text=f"📈 Parties: {self.parties_gagnees}/{self.parties_jouees}")
        self.essais_label.config(text=f"🎯 Essais restants: {self.essais_restants}")


# =============================================================================
# CHASSE AUX NOMBRES PREMIERS
# =============================================================================
class Difficulty(Enum):
    DEBUTANT = "Débutant"
    INTERMEDIAIRE = "Intermédiaire"
    AVANCE = "Avancé"

class ChasseNombresPremiers:
    def __init__(self, parent, json_file_path="data/question_premier.json"):
        self.parent = parent
        self.score = 0
        self.niveau = Difficulty.DEBUTANT
        self.question_actuelle = None
        self.indices_decouverts = 0
        self.essais_restants = 3
        self.parties_gagnees = 0
        self.parties_jouees = 0
        self.streak = 0
        self.bonus_streak = 0
        self.meilleur_streak = 0
        self.verification_en_cours = False
        
        # Palette de couleurs
        self.PALETTE = {
            "fond_principal": "#FFFFFF",
            "primaire": "#2563EB",
            "secondaire": "#7C3AED",
            "succes": "#10B981",
            "erreur": "#EF4444",
            "avertissement": "#F59E0B",
            "info": "#3B82F6",
            "texte_fonce": "#1F2937",
            "texte_clair": "#6B7280",
            "fond_clair": "#F3F4F6",
            "fond_carte": "#F8FAFC"
        }
        
        # Charger les questions depuis le JSON
        self.questions_data = self._charger_questions(json_file_path)
        
        # Statistiques
        self.nombres_premiers_trouves = []
        self.nombres_composites_trouves = []
        
        # Types de questions supportés
        self.types_questions = {
            "premier": "Est-ce premier ? (Oui/Non)",
            "decomposition": "Décomposition en facteurs premiers",
            "diviseurs": "Liste des diviseurs",
            "nombre_mystere": "Trouver le nombre",
            "vrai_faux": "Vrai ou Faux",
            "multiple": "Choix multiple"
        }

    def _charger_questions(self, json_path):
        """Charge les questions depuis le fichier JSON"""
        try:
            # Vérifier si le fichier existe
            if not os.path.exists(json_path):
                # Créer un fichier par défaut si inexistant
                default_data = {
                    "Débutant": [],
                    "Intermédiaire": [],
                    "Avancé": []
                }
                os.makedirs(os.path.dirname(json_path), exist_ok=True)
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(default_data, f, ensure_ascii=False, indent=2)
                return default_data
            
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur chargement questions: {e}")
            return {"Débutant": [], "Intermédiaire": [], "Avancé": []}
    
    def lancer_jeu(self):
        """Lance la fenêtre du jeu"""
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🔢 Chasse aux Nombres Premiers")
            self.fenetre_jeu.geometry("900x800")
            self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_question()

        # Centrer la fenêtre si Toplevel
        if is_toplevel:
            self.fenetre_jeu.update_idletasks()
            width = self.fenetre_jeu.winfo_width()
            height = self.fenetre_jeu.winfo_height()
            x = (self.fenetre_jeu.winfo_screenwidth() // 2) - (width // 2)
            y = (self.fenetre_jeu.winfo_screenheight() // 2) - (height // 2)
            self.fenetre_jeu.geometry(f'{width}x{height}+{x}+{y}')

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass
    
    def _creer_interface(self):
        """Crée l'interface graphique du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=self.PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 10))
        
        Label(header_frame, text="🔢 CHASSE AUX NOMBRES PREMIERS", 
              font=("Century Gothic", 20, "bold"), bg=self.PALETTE["primaire"], fg="white").pack(pady=15)
        
        Label(header_frame, text="Testez vos connaissances sur les nombres premiers !", 
              font=("Century Gothic", 11), bg=self.PALETTE["primaire"], fg="white", 
              wraplength=700).pack(pady=(0, 10))

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=self.PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, self.PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=self.PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques principales
        stats_frame = Frame(content_frame, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=1)
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Première ligne de stats
        stats_line1 = Frame(stats_frame, bg=self.PALETTE["fond_clair"])
        stats_line1.pack(fill=X, padx=15, pady=10)
        
        # Score
        self.score_label = Label(stats_line1, text=f"🏆 SCORE: {self.score}", 
                                font=("Century Gothic", 13, "bold"), bg=self.PALETTE["fond_clair"], 
                                fg=self.PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        # Streak
        self.streak_label = Label(stats_line1, text=f"🔥 STREAK: {self.streak}", 
                                 font=("Century Gothic", 13, "bold"), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["avertissement"])
        self.streak_label.pack(side=LEFT, padx=20)
        
        # Niveau
        self.niveau_label = Label(stats_line1, text=f"📊 NIVEAU: {self.niveau.value}", 
                                 font=("Century Gothic", 13, "bold"), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["secondaire"])
        self.niveau_label.pack(side=LEFT, padx=20)
        
        # Deuxième ligne de stats
        stats_line2 = Frame(stats_frame, bg=self.PALETTE["fond_clair"])
        stats_line2.pack(fill=X, padx=15, pady=(0, 10))
        
        # Essais
        self.essais_label = Label(stats_line2, text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}", 
                                 font=("Century Gothic", 11), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["texte_fonce"])
        self.essais_label.pack(side=LEFT, padx=20)
        
        # Partie
        self.parties_label = Label(stats_line2, text=f"📈 PARTIES: {self.parties_gagnees}/{self.parties_jouees}", 
                                  font=("Century Gothic", 11), bg=self.PALETTE["fond_clair"], 
                                  fg=self.PALETTE["texte_fonce"])
        self.parties_label.pack(side=LEFT, padx=20)
        
        # Cadre principal
        main_frame = Frame(content_frame, bg=self.PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Boutons d'action (Explication, Guide)
        boutons_action_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        boutons_action_frame.pack(fill=X, pady=5)
        ttk.Button(boutons_action_frame, text="❓ Explication", 
                  style="Jeu.TButton", command=self._afficher_explication).pack(side=RIGHT, padx=5)
        ttk.Button(boutons_action_frame, text="📚 Guide", 
                  style="Jeu.TButton", command=lambda: afficher_guide_jeu("chasse_premiers", self.fenetre_jeu)).pack(side=RIGHT, padx=5)
        
        # Zone de log
        log_frame = Frame(main_frame, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=1)
        log_frame.pack(fill=BOTH, expand=True, pady=10)
        
        Label(log_frame, text="📝 HISTORIQUE DES QUESTIONS :", 
              font=("Century Gothic", 10, "bold"), bg=self.PALETTE["fond_clair"]).pack(anchor=W, padx=10, pady=5)
        
        self.log_text = Text(log_frame, height=5, font=("Century Gothic", 9),
                            bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)
        self.log_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.log_text.config(state=DISABLED)

    def _nouvelle_question(self):
        """Prépare une nouvelle question"""
        self.verification_en_cours = False
        
        # Mettre à jour le niveau selon le score
        if self.score < 100:
            self.niveau = Difficulty.DEBUTANT
        elif self.score < 300:
            self.niveau = Difficulty.INTERMEDIAIRE
        else:
            self.niveau = Difficulty.AVANCE
        
        # Récupérer une question aléatoire du niveau
        questions_niveau = self.questions_data.get(self.niveau.value, [])
        if not questions_niveau:
            self._creer_question_auto()
        else:
            self.question_actuelle = random.choice(questions_niveau)
        
        # Réinitialiser les compteurs
        self.indices_decouverts = 0
        self.essais_restants = 3
        
        # Mettre à jour l'interface
        self._afficher_question()
        self._creer_controles_reponse()  # Créer les contrôles appropriés
        self._afficher_indices()
        self._effacer_feedback()
        
        # Mettre à jour les labels
        self.niveau_label.config(text=f"📊 NIVEAU: {self.niveau.value}")
        self.essais_label.config(text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}")
        
        # Afficher le type de question
        type_question = self.question_actuelle.get("type", "premier")
        type_desc = self.types_questions.get(type_question, "Question sur les nombres premiers")
        self.type_label.config(text=f"🔍 TYPE: {type_desc}")
        
        self._ajouter_log(f"🔢 Nouvelle question: {type_desc}")
        self._mettre_a_jour_stats()

    def _creer_question_auto(self):
        """Crée une question automatiquement si le fichier est vide"""
        # Définir les plages selon le niveau
        if self.niveau == Difficulty.DEBUTANT:
            # Mélanger nombres premiers et composites
            nombres_possibles = list(range(2, 31))
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            nombres_possibles = list(range(30, 201))
        else:  # Avancé
            nombres_possibles = list(range(200, 1001))
        
        # Éviter les nombres trop évidents pour les niveaux supérieurs
        if self.niveau != Difficulty.DEBUTANT:
            nombres_possibles = [n for n in nombres_possibles if n not in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]]
        
        nombre = random.choice(nombres_possibles)
        
        # Déterminer si le nombre est premier
        est_premier = self._est_premier(nombre)
        
        # Créer la question
        self.question_actuelle = {
            "question": f"Le nombre {nombre} est-il premier ?",
            "reponse": "Oui" if est_premier else "Non",
            "indices": self._generer_indices(nombre, est_premier),
            "type": "premier"
        }

    def _est_premier(self, n):
        """Vérifie si un nombre est premier"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def _generer_indices(self, nombre, est_premier):
        """Génère des indices pour un nombre"""
        indices = []
        
        # Indice 1 : Critères basiques
        if nombre < 2:
            indices.append(f"❌ {nombre} < 2, donc il n'est PAS premier")
        elif nombre == 2:
            indices.append("✅ 2 est le SEUL nombre premier pair")
        elif nombre % 2 == 0:
            indices.append(f"❌ {nombre} est pair (sauf 2), donc il est COMPOSITE")
        else:
            indices.append(f"ℹ️  {nombre} est impair, vérifions ses diviseurs...")
        
        # Indice 2 : Diviseurs évidents
        if nombre > 2:
            if nombre % 3 == 0:
                indices.append(f"❌ {nombre} ÷ 3 = {nombre // 3} → divisible par 3")
            elif nombre % 5 == 0:
                indices.append(f"❌ {nombre} ÷ 5 = {nombre // 5} → divisible par 5")
            elif nombre % 7 == 0:
                indices.append(f"❌ {nombre} ÷ 7 = {nombre // 7} → divisible par 7")
            elif nombre > 10 and nombre % 11 == 0:
                indices.append(f"❌ {nombre} ÷ 11 = {nombre // 11} → divisible par 11")
            else:
                indices.append(f"ℹ️  Pas divisible par 2, 3, 5, 7, 11...")
        
        # Indice 3 : Limite de test
        if nombre > 2 and nombre % 2 != 0:
            limite = int(nombre**0.5)
            indices.append(f"ℹ️  Testez les diviseurs jusqu'à √{nombre} ≈ {limite}")
            
            # Chercher un diviseur si composite
            if not est_premier and nombre > 10:
                diviseur = None
                for i in range(3, limite + 1, 2):
                    if nombre % i == 0:
                        diviseur = i
                        break
                if diviseur:
                    indices.append(f"❌ {nombre} ÷ {diviseur} = {nombre // diviseur}")
        
        # Indice 4 : Conclusion
        if est_premier:
            indices.append(f"✅ Aucun diviseur trouvé → {nombre} est PREMIER !")
        else:
            indices.append(f"❌ Trouvé un diviseur → {nombre} est COMPOSITE")
        
        return indices

    def _afficher_question(self):
        """Affiche la question actuelle"""
        # Nettoyer le frame
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        
        # Afficher le nombre mystère
        Label(self.question_frame, text="🎲 QUESTION :", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        # Extraire le nombre de la question
        question_text = self.question_actuelle["question"]
        Label(self.question_frame, text=question_text, 
              font=("Century Gothic", 18, "bold"), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["texte_fonce"], wraplength=700).pack(pady=10, padx=20)
        
        # Afficher l'instruction selon le type
        type_question = self.question_actuelle.get("type", "premier")
        instruction = ""
        
        if type_question == "premier":
            instruction = "Est-ce un nombre premier ?"
        elif type_question == "decomposition":
            instruction = "Donnez la décomposition en facteurs premiers"
        elif type_question == "diviseurs":
            instruction = "Listez tous les diviseurs"
        elif type_question == "vrai_faux":
            instruction = "Cette affirmation est-elle vraie ou fausse ?"
        elif type_question == "nombre_mystere":
            instruction = "Quel est ce nombre ?"
        
        if instruction:
            Label(self.question_frame, text=instruction, 
                  font=("Century Gothic", 14), bg=self.PALETTE["fond_carte"], 
                  fg=self.PALETTE["texte_clair"]).pack(pady=10)

    def _creer_controles_reponse(self):
        """Crée les contrôles de réponse adaptés au type de question"""
        # Nettoyer le frame
        for widget in self.controles_reponse_frame.winfo_children():
            widget.destroy()
        
        type_question = self.question_actuelle.get("type", "premier")
        
        if type_question == "premier":
            # Boutons Oui/Non pour les questions "est-ce premier ?"
            boutons_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            boutons_frame.pack()
            
            self.btn_oui = ttk.Button(boutons_frame, text="✅ OUI, c'est PREMIER", 
                                     style="Jeu.TButton", command=lambda: self._verifier_reponse("Oui"), width=20)
            self.btn_oui.pack(side=LEFT, padx=10)
            
            self.btn_non = ttk.Button(boutons_frame, text="❌ NON, c'est COMPOSITE", 
                                     style="Jeu.TButton", command=lambda: self._verifier_reponse("Non"), width=20)
            self.btn_non.pack(side=LEFT, padx=10)
            
        elif type_question == "vrai_faux":
            # Boutons Vrai/Faux
            boutons_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            boutons_frame.pack()
            
            self.btn_vrai = ttk.Button(boutons_frame, text="✅ VRAI", 
                                      style="Jeu.TButton", command=lambda: self._verifier_reponse("Vrai"), width=15)
            self.btn_vrai.pack(side=LEFT, padx=10)
            
            self.btn_faux = ttk.Button(boutons_frame, text="❌ FAUX", 
                                      style="Jeu.TButton", command=lambda: self._verifier_reponse("Faux"), width=15)
            self.btn_faux.pack(side=LEFT, padx=10)
            
        elif type_question in ["decomposition", "diviseurs", "nombre_mystere"]:
            # Champ de saisie pour les réponses textuelles
            saisie_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            saisie_frame.pack()
            
            Label(saisie_frame, text="Entrez votre réponse :", 
                  font=("Century Gothic", 11), bg=self.PALETTE["fond_principal"]).pack(pady=5)
            
            self.reponse_entry = Entry(saisie_frame, font=("Century Gothic", 14), 
                                      width=30, justify="center")
            self.reponse_entry.pack(pady=5)
            self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse_texte())
            
            # Exemples de format selon le type
            exemples = {
                "decomposition": "Ex: 2×2×3×5 ou 2²×3×5",
                "diviseurs": "Ex: 1,2,3,6 (séparés par des virgules)",
                "nombre_mystere": "Ex: 42"
            }
            
            if type_question in exemples:
                Label(saisie_frame, text=exemples[type_question], 
                      font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], 
                      fg=self.PALETTE["texte_clair"]).pack(pady=2)
            
            ttk.Button(saisie_frame, text="✅ Valider la réponse", 
                      style="Jeu.TButton", command=self._verifier_reponse_texte).pack(pady=10)
        
        else:
            # Par défaut, champ de saisie générique
            saisie_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            saisie_frame.pack()
            
            self.reponse_entry = Entry(saisie_frame, font=("Century Gothic", 14), 
                                      width=30, justify="center")
            self.reponse_entry.pack(pady=5)
            self.reponse_entry.bind("<Return>", lambda e: self._verifier_reponse_texte())
            
            ttk.Button(saisie_frame, text="✅ Valider", 
                      style="Jeu.TButton", command=self._verifier_reponse_texte).pack(pady=5)

    def _verifier_reponse(self, reponse_joueur):
        """Vérifie la réponse pour les questions à choix (Oui/Non, Vrai/Faux)"""
        if self.verification_en_cours:
            return
            
        if self.essais_restants <= 0:
            return
        
        # Désactiver les contrôles
        self._desactiver_controles()
        self.verification_en_cours = True
        
        self.parties_jouees += 1
        self.essais_restants -= 1
        self.essais_label.config(text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}")
        
        reponse_correcte = self.question_actuelle["reponse"]
        
        # Normaliser les réponses
        reponse_joueur_norm = reponse_joueur.strip().lower()
        reponse_correcte_norm = str(reponse_correcte).strip().lower()
        
        if reponse_joueur_norm == reponse_correcte_norm:
            self._reussite_question()
        else:
            self._echec_essai()
        
        if self.essais_restants <= 0:
            self.fenetre_jeu.after(1000, self._question_echouee)

    def _verifier_reponse_texte(self):
        """Vérifie la réponse pour les questions à saisie textuelle"""
        if self.verification_en_cours:
            return
            
        if self.essais_restants <= 0:
            return
        
        # Récupérer la réponse
        try:
            reponse_joueur = self.reponse_entry.get().strip()
        except:
            # Si pas de champ entry (boutons uniquement)
            self._afficher_feedback("❌ Veuillez entrer une réponse", self.PALETTE["erreur"])
            return
        
        if not reponse_joueur:
            self._afficher_feedback("❌ Veuillez entrer une réponse", self.PALETTE["erreur"])
            return
        
        # Désactiver les contrôles
        self._desactiver_controles()
        self.verification_en_cours = True
        
        self.parties_jouees += 1
        self.essais_restants -= 1
        self.essais_label.config(text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}")
        
        reponse_correcte = self.question_actuelle["reponse"]
        type_question = self.question_actuelle.get("type", "premier")
        
        # Vérification selon le type de question
        if self._valider_reponse_texte(reponse_joueur, reponse_correcte, type_question):
            self._reussite_question()
        else:
            self._echec_essai()
        
        if self.essais_restants <= 0:
            self.fenetre_jeu.after(1000, self._question_echouee)

    def _valider_reponse_texte(self, reponse_joueur, reponse_correcte, type_question):
        """Valide une réponse textuelle selon le type de question"""
        try:
            if type_question == "decomposition":
                # Validation de la décomposition en facteurs premiers
                return self._valider_decomposition(reponse_joueur, reponse_correcte)
            
            elif type_question == "diviseurs":
                # Validation de la liste de diviseurs
                return self._valider_diviseurs(reponse_joueur, reponse_correcte)
            
            elif type_question == "nombre_mystere":
                # Validation d'un nombre
                return self._valider_nombre(reponse_joueur, reponse_correcte)
            
            else:
                # Validation textuelle simple
                return str(reponse_joueur).strip().lower() == str(reponse_correcte).strip().lower()
                
        except:
            return False

    def _valider_decomposition(self, reponse_joueur, reponse_correcte):
        """Valide une décomposition en facteurs premiers"""
        # Nettoyer les espaces
        reponse_joueur = reponse_joueur.replace(" ", "").lower()
        reponse_correcte = str(reponse_correcte).replace(" ", "").lower()
        
        # Formater la réponse correcte si c'est une liste
        if isinstance(reponse_correcte, list):
            reponse_correcte = "×".join(str(x) for x in reponse_correcte)
        
        # Supprimer les × en trop
        reponse_joueur = reponse_joueur.strip("×")
        reponse_correcte = reponse_correcte.strip("×")
        
        # Trier les facteurs pour comparer
        def trier_facteurs(expression):
            facteurs = expression.split("×")
            facteurs_tries = sorted(facteurs, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else 0)
            return "×".join(facteurs_tries)
        
        try:
            return trier_facteurs(reponse_joueur) == trier_facteurs(reponse_correcte)
        except:
            return reponse_joueur == reponse_correcte

    def _valider_diviseurs(self, reponse_joueur, reponse_correcte):
        """Valide une liste de diviseurs"""
        # Nettoyer et trier
        try:
            # Extraire les nombres de la réponse du joueur
            nombres_joueur = [int(x.strip()) for x in reponse_joueur.replace(",", " ").split()]
            nombres_joueur.sort()
            
            # Formater la réponse correcte
            if isinstance(reponse_correcte, list):
                nombres_corrects = sorted(reponse_correcte)
            else:
                nombres_corrects = sorted([int(x.strip()) for x in str(reponse_correcte).replace(",", " ").split()])
            
            return nombres_joueur == nombres_corrects
        except:
            return False

    def _valider_nombre(self, reponse_joueur, reponse_correcte):
        """Valide un nombre"""
        try:
            return int(reponse_joueur) == int(reponse_correcte)
        except:
            return reponse_joueur == str(reponse_correcte)

    def _afficher_indices(self):
        """Affiche les indices disponibles"""
        # Nettoyer le frame
        for widget in self.indices_frame.winfo_children():
            widget.destroy()
        
        indices = self.question_actuelle.get("indices", [])
        
        if not indices:
            Label(self.indices_frame, text="Aucun indice disponible", 
                  font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], 
                  fg=self.PALETTE["texte_clair"]).pack(pady=5)
            return
        
        # Afficher les indices déjà découverts
        for i in range(len(indices)):
            if i < self.indices_decouverts:
                # Indice révélé
                Label(self.indices_frame, text=f"💡 {indices[i]}", 
                      font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], 
                      fg="#10B981", wraplength=700, justify="left").pack(anchor=W, pady=3)
            else:
                # Indice caché
                Label(self.indices_frame, text=f"🔒 Indice {i+1} (coût: 5 points)", 
                      font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], 
                      fg=self.PALETTE["texte_clair"], wraplength=700, 
                      justify="left").pack(anchor=W, pady=3)

    def _obtenir_indice(self):
        """Donne un indice au joueur"""
        indices = self.question_actuelle.get("indices", [])
        
        if not indices:
            self._afficher_feedback("❌ Aucun indice disponible pour cette question", self.PALETTE["erreur"])
            return
        
        if self.indices_decouverts >= len(indices):
            self._afficher_feedback("❌ Plus d'indices disponibles !", self.PALETTE["erreur"])
            return
        
        # Pénalité de points
        penalite = 5
        if self.score >= penalite:
            self.score -= penalite
            self.indices_decouverts += 1
            
            self._ajouter_log(f"📉 Indice acheté: -{penalite} points")
            self._afficher_feedback(f"💡 Indice {self.indices_decouverts} révélé ! (-{penalite} points)", 
                                  "#F59E0B")
            
            self._afficher_indices()
            self._mettre_a_jour_stats()
        else:
            self._afficher_feedback("❌ Pas assez de points pour un indice !", self.PALETTE["erreur"])

    def _desactiver_controles(self):
        """Désactive tous les contrôles de réponse"""
        for widget in self.controles_reponse_frame.winfo_children():
            if isinstance(widget, ttk.Button, style="Jeu.TButton"):
                widget.config(state="disabled")
            elif isinstance(widget, Frame):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Button, style="Jeu.TButton"):
                        child.config(state="disabled")
                    elif isinstance(child, Entry):
                        child.config(state="disabled")

    def _reactiver_controles(self):
        """Réactive les contrôles de réponse"""
        type_question = self.question_actuelle.get("type", "premier")
        
        if type_question in ["premier", "vrai_faux"]:
            # Réactiver les boutons
            for widget in self.controles_reponse_frame.winfo_children():
                if isinstance(widget, ttk.Button, style="Jeu.TButton"):
                    widget.config(state="normal")
                elif isinstance(widget, Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, ttk.Button, style="Jeu.TButton"):
                            child.config(state="normal")
        else:
            # Réactiver le champ de saisie
            for widget in self.controles_reponse_frame.winfo_children():
                if isinstance(widget, Entry):
                    widget.config(state="normal")
                elif isinstance(widget, Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, Entry):
                            child.config(state="normal")
                        elif isinstance(child, ttk.Button, style="Jeu.TButton"):
                            child.config(state="normal")

    def _reussite_question(self):
        """Quand la question est résolue correctement"""
        try:
            points = self._calculer_points()
            self.score += points
            self.streak += 1
            self.parties_gagnees += 1
            
            if self.streak > self.meilleur_streak:
                self.meilleur_streak = self.streak
            
            # Bonus de streak
            bonus_streak = 0
            if self.streak >= 5:
                bonus_streak = 20
                self.score += bonus_streak
                self.bonus_streak += bonus_streak
            
            # Extraire des infos pour le feedback
            question_text = self.question_actuelle["question"]
            nombre = self._extraire_nombre(question_text) if "nombre" in question_text.lower() else ""
            
            message = f"✅ CORRECT ! (+{points} points"
            if nombre:
                message += f" pour {nombre}"
            if bonus_streak:
                message += f" + {bonus_streak} bonus streak"
            message += ")"
            
            self._afficher_feedback(message, self.PALETTE["succes"])
            self._ajouter_log(f"✅ Réponse correcte ! +{points} points")
            self._mettre_a_jour_stats()
            
            # Nouvelle question après délai
            self.fenetre_jeu.after(2500, self._nouvelle_question)
            
        except Exception as e:
            print(f"Erreur dans _reussite_question: {e}")
            self._afficher_feedback(f"❌ Erreur: {str(e)}", self.PALETTE["erreur"])
            self.verification_en_cours = False

    def _echec_essai(self):
        """Quand un essai échoue"""
        try:
            self.streak = 0
            self.bonus_streak = 0
            
            if self.essais_restants > 0:
                # Réactiver les contrôles pour un nouvel essai
                self._reactiver_controles()
                self.verification_en_cours = False
                
                self._afficher_feedback(f"❌ Réponse incorrecte. Il te reste {self.essais_restants} essai{'s' if self.essais_restants > 1 else ''}.", 
                                      self.PALETTE["erreur"])
            else:
                self._afficher_feedback(f"❌ Réponse incorrecte.", self.PALETTE["erreur"])
            
            self._ajouter_log(f"❌ Essai incorrect")
            self._mettre_a_jour_stats()
            
        except Exception as e:
            print(f"Erreur dans _echec_essai: {e}")
            self.verification_en_cours = False

    def _question_echouee(self):
        """Quand la question n'est pas résolue à temps"""
        try:
            self.streak = 0
            self.bonus_streak = 0
            
            # Extraire le nombre
            question_text = self.question_actuelle["question"]
            reponse = self.question_actuelle["reponse"]
            
            # Pénalité
            penalite = 15
            self.score = max(0, self.score - penalite)
            
            self._afficher_feedback(f"💥 ÉCHEC ! La réponse était: {reponse} (-{penalite} points)", 
                                  self.PALETTE["erreur"])
            
            self._ajouter_log(f"💥 ÉCHEC - Réponse: {reponse}. -{penalite} points")
            self._mettre_a_jour_stats()
            
            # Nouvelle question après délai
            self.fenetre_jeu.after(3000, self._nouvelle_question)
            
        except Exception as e:
            print(f"Erreur dans _question_echouee: {e}")
            # Passer à la question suivante même en cas d'erreur
            self.fenetre_jeu.after(1000, self._nouvelle_question)

    def _calculer_points(self):
        """Calcule les points gagnés"""
        points_base = 20
        niveau_multiplier = {
            Difficulty.DEBUTANT: 1,
            Difficulty.INTERMEDIAIRE: 2,
            Difficulty.AVANCE: 3
        }
        
        # Bonus pour rapidité (beaucoup d'essais restants)
        bonus_essais = self.essais_restants * 5
        
        # Malus pour indices utilisés
        malus_indices = self.indices_decouverts * 5
        
        # Vérifier que le niveau existe dans le dictionnaire
        multiplicateur = niveau_multiplier.get(self.niveau, 1)
        
        points = (points_base + bonus_essais - malus_indices) * multiplicateur
        
        # Minimum de 10 points
        return max(10, points)

    def _extraire_nombre(self, question):
        """Extrait le nombre d'une question"""
        import re
        nombres = re.findall(r'\d+', question)
        return int(nombres[0]) if nombres else 0
    
    def _afficher_feedback(self, message, couleur):
        """Affiche un message de feedback"""
        self.feedback_label.config(text=message, fg=couleur)
    
    def _effacer_feedback(self):
        """Efface le feedback"""
        self.feedback_label.config(text="")
    
    def _ajouter_log(self, message):
        """Ajoute un message au log"""
        self.log_text.config(state=NORMAL)
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(END, f"[{timestamp}] {message}\n")
        self.log_text.see(END)
        self.log_text.config(state=DISABLED)
    
    def _mettre_a_jour_stats(self):
        """Met à jour toutes les statistiques"""
        self.score_label.config(text=f"🏆 SCORE: {self.score}")
        self.streak_label.config(text=f"🔥 STREAK: {self.streak}")
        self.parties_label.config(text=f"📈 PARTIES: {self.parties_gagnees}/{self.parties_jouees}")
        
        # Mettre à jour le niveau affiché
        if self.score < 100:
            niveau_text = "Débutant"
        elif self.score < 300:
            niveau_text = "Intermédiaire"
        else:
            niveau_text = "Avancé"
        self.niveau_label.config(text=f"📊 NIVEAU: {niveau_text}")

    def _afficher_statistiques(self):
        """Affiche une fenêtre de statistiques"""
        stats_window = Toplevel(self.fenetre_jeu)
        stats_window.title("📊 Statistiques Détaillées")
        stats_window.geometry("500x500")
        stats_window.configure(bg=self.PALETTE["fond_principal"])
        
        # Titre
        Label(stats_window, text="📊 STATISTIQUES DÉTAILLÉES", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        # Cadre des stats avec scrollbar
        stats_container = Frame(stats_window, bg=self.PALETTE["fond_principal"])
        stats_container.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        canvas = Canvas(stats_container, bg=self.PALETTE["fond_clair"])
        scrollbar = Scrollbar(stats_container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.PALETTE["fond_clair"])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        stats_content = [
            ("🎯 Score total", f"{self.score} points"),
            ("🔥 Streak actuel", f"{self.streak} réponses consécutives"),
            ("⭐ Meilleur streak", f"{self.meilleur_streak} réponses"),
            ("✅ Réponses correctes", f"{self.parties_gagnees}"),
            ("📊 Parties jouées", f"{self.parties_jouees}"),
            ("📈 Taux de réussite", f"{(self.parties_gagnees/self.parties_jouees*100 if self.parties_jouees > 0 else 0):.1f}%"),
            ("🔢 Nombres premiers", f"{len(self.nombres_premiers_trouves)}"),
            ("🔣 Nombres composites", f"{len(self.nombres_composites_trouves)}"),
            ("🔍 Indices utilisés", f"{self.indices_decouverts}"),
            ("💰 Coût indices", f"{self.indices_decouverts * 5} points"),
            ("⭐ Bonus streak", f"{self.bonus_streak} points"),
            ("📊 Niveau actuel", f"{self.niveau.value}")
        ]
        
        for label, value in stats_content:
            line_frame = Frame(scrollable_frame, bg=self.PALETTE["fond_clair"])
            line_frame.pack(fill=X, padx=15, pady=8)
            
            Label(line_frame, text=label, font=("Century Gothic", 11), 
                  bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"]).pack(side=LEFT)
            
            Label(line_frame, text=value, font=("Century Gothic", 11, "bold"), 
                  bg=self.PALETTE["fond_clair"], fg=self.PALETTE["primaire"]).pack(side=RIGHT)
        
        # Listes des nombres trouvés (si disponibles)
        if self.nombres_premiers_trouves or self.nombres_composites_trouves:
            separator = Frame(scrollable_frame, bg=self.PALETTE["fond_clair"], height=2, relief="sunken")
            separator.pack(fill=X, padx=15, pady=10)
            
            premiers_text = ", ".join(str(n) for n in sorted(self.nombres_premiers_trouves[-10:]))  # 10 derniers
            composites_text = ", ".join(str(n) for n in sorted(self.nombres_composites_trouves[-10:]))
            
            Label(scrollable_frame, text="📋 10 derniers nombres premiers:", 
                  font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_clair"]).pack(anchor=W, padx=15, pady=5)
            Label(scrollable_frame, text=premiers_text if premiers_text else "Aucun", 
                  font=("Century Gothic", 10), bg=self.PALETTE["fond_clair"], 
                  fg=self.PALETTE["succes"], wraplength=400).pack(anchor=W, padx=15, pady=2)
            
            Label(scrollable_frame, text="📋 10 derniers nombres composites:", 
                  font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_clair"]).pack(anchor=W, padx=15, pady=5)
            Label(scrollable_frame, text=composites_text if composites_text else "Aucun", 
                  font=("Century Gothic", 10), bg=self.PALETTE["fond_clair"], 
                  fg=self.PALETTE["erreur"], wraplength=400).pack(anchor=W, padx=15, pady=2)
        
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Bouton fermer
        btn_frame = Frame(stats_window, bg=self.PALETTE["fond_principal"])
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="Fermer", command=stats_window.destroy, style="Jeu.TButton").pack()
    
    def _afficher_explication(self):
        """Affiche l'explication complète"""
        # Pénalité pour voir la solution
        penalite = 10
        self.score = max(0, self.score - penalite)
        
        explication_window = Toplevel(self.fenetre_jeu)
        explication_window.title("📚 Explication Complète")
        explication_window.geometry("600x500")
        explication_window.configure(bg=self.PALETTE["fond_principal"])
        
        # Titre
        Label(explication_window, text="📚 EXPLICATION COMPLÈTE", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        # Question
        Label(explication_window, text="Question:", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        Label(explication_window, text=self.question_actuelle["question"], 
              font=("Century Gothic", 14), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["texte_fonce"], wraplength=500).pack(pady=5)
        
        # Réponse
        Label(explication_window, text="Réponse:", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=10)
        
        reponse = self.question_actuelle["reponse"]
        couleur = self.PALETTE["succes"] if reponse == "Oui" or reponse == "Vrai" else self.PALETTE["erreur"]
        
        Label(explication_window, text=reponse, 
              font=("Century Gothic", 18, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=couleur).pack(pady=5)
        
        # Explication détaillée
        Label(explication_window, text="Explication détaillée:", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=10)
        
        explication_text = Text(explication_window, height=12, font=("Century Gothic", 10),
                               bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"], 
                               wrap=WORD)
        scrollbar = Scrollbar(explication_window, command=explication_text.yview)
        explication_text.config(yscrollcommand=scrollbar.set)
        
        # Ajouter tous les indices
        indices = self.question_actuelle.get("indices", [])
        if indices:
            for indice in indices:
                explication_text.insert(END, f"• {indice}\n\n")
        else:
            explication_text.insert(END, "Aucune explication disponible.\n")
        
        explication_text.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=5)
        scrollbar.pack(side=RIGHT, fill=Y)
        explication_text.config(state=DISABLED)
        
        # Pénalité
        Label(explication_window, text=f"(-{penalite} points pour voir l'explication)", 
              font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["texte_clair"]).pack(pady=10)
        
        # Bouton fermer
        ttk.Button(explication_window, text="Fermer", 
                  command=explication_window.destroy, style="Jeu.TButton").pack(pady=10)
        
        self._ajouter_log(f"📚 Explication achetée: -{penalite} points")
        self._mettre_a_jour_stats()

# =============================================================================
# MATH BATTLE
# =============================================================================

class MathBattle:
    def __init__(self, parent, json_file_path="data/math_battle.json"):
        self.parent = parent
        self.score_joueur = 0
        self.score_ordi = 0
        self.manche_actuelle = 1
        self.questions_jouees = 0
        self.questions_total = 10
        self.temps_restant = 30
        self.timer_actif = False
        self.question_actuelle = None
        self.derniere_reponse = None
        self.gagnant_manche = None
        self.streak = 0
        self.bonus_streak = 0
        
        # Palette de couleurs
        self.PALETTE = {
            "fond_principal": "#FFFFFF",
            "primaire": "#2563EB",
            "secondaire": "#7C3AED",
            "succes": "#10B981",
            "erreur": "#EF4444",
            "avertissement": "#F59E0B",
            "info": "#3B82F6",
            "texte_fonce": "#1F2937",
            "texte_clair": "#6B7280",
            "fond_clair": "#F3F4F6",
            "fond_carte": "#F8FAFC",
            "joueur": "#3B82F6",  # Bleu pour le joueur
            "ordi": "#EF4444"     # Rouge pour l'ordinateur
        }
        
        # Charger les questions depuis le JSON
        self.questions_data = self._charger_questions(json_file_path)
        
        # Types d'opérations disponibles
        self.operations = ["addition", "soustraction", "multiplication", "division", "mélange"]
        
        # Difficulté progressive
        self.difficulte = "facile"
        
        # Historique des manches
        self.historique_manches = []
    
    def _charger_questions(self, json_path):
        """Charge les questions depuis le fichier JSON"""
        try:
            # Vérifier si le fichier existe
            if not os.path.exists(json_path):
                # Créer un fichier par défaut si inexistant
                default_data = {
                    "facile": [],
                    "moyen": [],
                    "difficile": []
                }
                os.makedirs(os.path.dirname(json_path), exist_ok=True)
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(default_data, f, ensure_ascii=False, indent=2)
                return default_data
            
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur chargement questions Math Battle: {e}")
            return {"facile": [], "moyen": [], "difficile": []}
    
    def lancer_jeu(self):
        """Lance la fenêtre du jeu"""
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("⚔️ Math Battle")
            self.fenetre_jeu.geometry("1000x800")
            self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
            # Empêcher la fermeture accidentelle
            self.fenetre_jeu.protocol("WM_DELETE_WINDOW", self._quitter_jeu)
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouvelle_manche()

        # Centrer la fenêtre si Toplevel
        if is_toplevel:
            self.fenetre_jeu.update_idletasks()
            width = self.fenetre_jeu.winfo_width()
            height = self.fenetre_jeu.winfo_height()
            x = (self.fenetre_jeu.winfo_screenwidth() // 2) - (width // 2)
            y = (self.fenetre_jeu.winfo_screenheight() // 2) - (height // 2)
            self.fenetre_jeu.geometry(f'{width}x{height}+{x}+{y}')

        def _retour():
            if is_toplevel:
                try:
                    self.fenetre_jeu.destroy()
                except Exception:
                    pass
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass
    
    def _quitter_jeu(self):
        """Demande confirmation avant de quitter"""
        if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter le Math Battle ?\nVotre progression sera perdue."):
            self.fenetre_jeu.destroy()
    
    def _creer_interface(self):
        """Crée l'interface graphique du jeu"""
        # En-tête
        header_frame = Frame(self.fenetre_jeu, bg=self.PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 10))
        
        Label(header_frame, text="⚔️ MATH BATTLE", 
              font=("Century Gothic", 22, "bold"), bg=self.PALETTE["primaire"], fg="white").pack(pady=15)
        
        Label(header_frame, text="Affrontez l'ordinateur en calcul mental rapide !", 
              font=("Century Gothic", 12), bg=self.PALETTE["primaire"], fg="white", 
              wraplength=800).pack(pady=(0, 10))

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=self.PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, self.PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=self.PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)
        
        # Score et manches
        score_frame = Frame(self.fenetre_jeu, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=2)
        score_frame.pack(fill=X, padx=20, pady=10)
        
        # Score du joueur (à gauche)
        joueur_frame = Frame(score_frame, bg=self.PALETTE["joueur"])
        joueur_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=2)
        
        Label(joueur_frame, text="🧑 VOUS", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["joueur"], fg="white").pack(pady=5)
        
        self.score_joueur_label = Label(joueur_frame, text=f"{self.score_joueur}", 
                                        font=("Century Gothic", 28, "bold"), bg=self.PALETTE["joueur"], fg="white")
        self.score_joueur_label.pack(pady=10)
        
        # Informations centrales
        centre_frame = Frame(score_frame, bg=self.PALETTE["fond_clair"])
        centre_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10)
        
        # Manche
        self.manche_label = Label(centre_frame, text=f"MANCHE {self.manche_actuelle}/{self.questions_total}", 
                                 font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["primaire"])
        self.manche_label.pack(pady=10)
        
        # Difficulté
        self.difficulte_label = Label(centre_frame, text=f"📊 Difficulté: {self.difficulte.capitalize()}", 
                                     font=("Century Gothic", 12), bg=self.PALETTE["fond_clair"], 
                                     fg=self.PALETTE["texte_fonce"])
        self.difficulte_label.pack(pady=5)
        
        # Timer
        self.timer_frame = Frame(centre_frame, bg=self.PALETTE["fond_clair"])
        self.timer_frame.pack(pady=10)
        
        Label(self.timer_frame, text="⏱️ TEMPS RESTANT:", 
              font=("Century Gothic", 12), bg=self.PALETTE["fond_clair"]).pack()
        
        self.timer_label = Label(self.timer_frame, text=f"{self.temps_restant}s", 
                                font=("Century Gothic", 24, "bold"), bg=self.PALETTE["fond_clair"], 
                                fg=self.PALETTE["avertissement"])
        self.timer_label.pack()
        
        # Score de l'ordinateur (à droite)
        ordi_frame = Frame(score_frame, bg=self.PALETTE["ordi"])
        ordi_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=2, pady=2)
        
        Label(ordi_frame, text="🤖 ORDINATEUR", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["ordi"], fg="white").pack(pady=5)
        
        self.score_ordi_label = Label(ordi_frame, text=f"{self.score_ordi}", 
                                      font=("Century Gothic", 28, "bold"), bg=self.PALETTE["ordi"], fg="white")
        self.score_ordi_label.pack(pady=10)
        
        # Cadre principal
        main_frame = Frame(content_frame, bg=self.PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # Carte de la question
        self.question_frame = Frame(main_frame, bg=self.PALETTE["fond_carte"], 
                                   relief="solid", borderwidth=2)
        self.question_frame.pack(fill=BOTH, expand=True, pady=10)
        
        # Zone de réponse
        reponse_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        reponse_frame.pack(fill=X, pady=15)
        
        Label(reponse_frame, text="🎯 VOTRE RÉPONSE :", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        # Saisie de réponse avec vérification en temps réel
        self.reponse_var = StringVar()
        self.reponse_var.trace("w", self._verifier_saisie)
        
        self.reponse_entry = Entry(reponse_frame, textvariable=self.reponse_var, 
                                  font=("Century Gothic", 18), width=20, justify="center")
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.focus_set()
        
        # Boutons numériques pour aide à la saisie
        self._creer_clavier_numerique(reponse_frame)
        
        # Boutons d'action
        boutons_frame = Frame(reponse_frame, bg=self.PALETTE["fond_principal"])
        boutons_frame.pack(pady=15)
        
        self.btn_valider = ttk.Button(boutons_frame, text="✅ VALIDER (ENTRER)", 
                                     style="Jeu.TButton", command=self._valider_reponse, width=20)
        self.btn_valider.pack(side=LEFT, padx=5)
        
        self.btn_passer = ttk.Button(boutons_frame, text="⏭️ PASSER", 
                                    style="Jeu.TButton", command=self._passer_question, width=15)
        self.btn_passer.pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="📚 Guide", 
                  style="Jeu.TButton", command=lambda: afficher_guide_jeu("math_battle", self.fenetre_jeu)).pack(side=RIGHT, padx=5)
        
        # Zone de résultat de la manche
        self.resultat_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        self.resultat_frame.pack(fill=X, pady=10)
        
        self.resultat_label = Label(self.resultat_frame, text="", 
                                   font=("Century Gothic", 14), bg=self.PALETTE["fond_principal"], 
                                   wraplength=800)
        self.resultat_label.pack()
        
        # Zone d'historique des manches
        historique_frame = Frame(main_frame, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=1)
        historique_frame.pack(fill=BOTH, expand=True, pady=10)
        
        Label(historique_frame, text="📝 HISTORIQUE DES MANCHES :", 
              font=("Century Gothic", 11, "bold"), bg=self.PALETTE["fond_clair"]).pack(anchor=W, padx=10, pady=5)
        
        self.historique_text = Text(historique_frame, height=6, font=("Century Gothic", 9),
                                   bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(historique_frame, command=self.historique_text.yview)
        self.historique_text.config(yscrollcommand=scrollbar.set)
        self.historique_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.historique_text.config(state=DISABLED)
        
        # Boutons de fin
        boutons_fin_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        boutons_fin_frame.pack(fill=X, pady=5)
        
        ttk.Button(boutons_fin_frame, text="📊 Statistiques", 
                  style="Jeu.TButton", command=self._afficher_statistiques).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_fin_frame, text="🔄 Recommencer", 
                  style="Jeu.TButton", command=self._recommencer_jeu).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_fin_frame, text="🏆 Classement", 
                  style="Jeu.TButton", command=self._afficher_classement).pack(side=RIGHT, padx=5)
        
        ttk.Button(boutons_fin_frame, text="❌ Quitter", 
                  style="Jeu.TButton", command=self._quitter_jeu).pack(side=RIGHT, padx=5)

    def _creer_clavier_numerique(self, parent):
        """Crée un clavier numérique pour aider à la saisie"""
        clavier_frame = Frame(parent, bg=self.PALETTE["fond_principal"])
        clavier_frame.pack(pady=10)
        
        # Configuration des boutons
        boutons = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '.', '⌫']
        ]
        
        for ligne in boutons:
            ligne_frame = Frame(clavier_frame, bg=self.PALETTE["fond_principal"])
            ligne_frame.pack()
            
            for texte in ligne:
                if texte == '⌫':
                    commande = self._effacer_caractere
                    width = 8
                else:
                    commande = lambda t=texte: self._ajouter_caractere(t)
                    width = 5
                
                btn = ttk.Button(ligne_frame, text=texte, style="Jeu.TButton", command=commande, width=width)
                btn.pack(side=LEFT, padx=2, pady=2)

    def _ajouter_caractere(self, caractere):
        """Ajoute un caractère à la réponse"""
        current = self.reponse_var.get()
        self.reponse_var.set(current + caractere)
        self.reponse_entry.focus_set()

    def _effacer_caractere(self):
        """Efface le dernier caractère"""
        current = self.reponse_var.get()
        if current:
            self.reponse_var.set(current[:-1])
        self.reponse_entry.focus_set()

    def _verifier_saisie(self, *args):
        """Vérifie la saisie en temps réel"""
        saisie = self.reponse_var.get()
        # Nettoyer la saisie (uniquement chiffres, point, signe moins)
        nettoyee = ''.join(c for c in saisie if c.isdigit() or c in '.-')
        if nettoyee != saisie:
            self.reponse_var.set(nettoyee)
        
        # Mettre à jour le curseur
        self.reponse_entry.icursor(END)

    def _nouvelle_manche(self):
        """Prépare une nouvelle manche"""
        self.questions_jouees += 1
        
        # Mettre à jour la difficulté
        if self.questions_jouees <= 3:
            self.difficulte = "facile"
        elif self.questions_jouees <= 7:
            self.difficulte = "moyen"
        else:
            self.difficulte = "difficile"
        
        # Générer une question
        self.question_actuelle = self._generer_question()
        
        # Réinitialiser l'interface
        self._afficher_question()
        self.reponse_var.set("")
        self.resultat_label.config(text="")
        self.derniere_reponse = None
        self.gagnant_manche = None
        
        # Mettre à jour les labels
        self.manche_label.config(text=f"MANCHE {self.questions_jouees}/{self.questions_total}")
        self.difficulte_label.config(text=f"📊 Difficulté: {self.difficulte.capitalize()}")
        
        # Réinitialiser le timer
        self.temps_restant = 30
        self.timer_label.config(text=f"{self.temps_restant}s", fg=self.PALETTE["avertissement"])
        
        # Activer les boutons
        self.btn_valider.config(state="normal")
        self.btn_passer.config(state="normal")
        self.reponse_entry.config(state="normal")
        self.reponse_entry.focus_set()
        
        # Démarrer le timer
        self.timer_actif = True
        self._demarrer_timer()
        
        # Ajouter à l'historique
        self._ajouter_historique(f"🔔 Manche {self.questions_jouees} - {self.difficulte.capitalize()}")

    def _generer_question(self):
        """Génère une question mathématique aléatoire"""
        if self.difficulte == "facile":
            operation = random.choice(["addition", "soustraction", "multiplication"])
            
            if operation == "addition":
                a = random.randint(1, 50)
                b = random.randint(1, 50)
                question = f"{a} + {b}"
                reponse = a + b
                
            elif operation == "soustraction":
                a = random.randint(1, 100)
                b = random.randint(1, a)
                question = f"{a} - {b}"
                reponse = a - b
                
            else:  # multiplication
                a = random.randint(1, 12)
                b = random.randint(1, 10)
                question = f"{a} × {b}"
                reponse = a * b
                
        elif self.difficulte == "moyen":
            operation = random.choice(["addition", "soustraction", "multiplication", "division"])
            
            if operation == "addition":
                a = random.randint(10, 200)
                b = random.randint(10, 200)
                question = f"{a} + {b}"
                reponse = a + b
                
            elif operation == "soustraction":
                a = random.randint(50, 300)
                b = random.randint(10, a-10)
                question = f"{a} - {b}"
                reponse = a - b
                
            elif operation == "multiplication":
                a = random.randint(2, 15)
                b = random.randint(2, 15)
                question = f"{a} × {b}"
                reponse = a * b
                
            else:  # division
                b = random.randint(2, 12)
                reponse = random.randint(2, 12)
                a = b * reponse
                question = f"{a} ÷ {b}"
                
        else:  # difficile
            operation = random.choice(["addition", "soustraction", "multiplication", "division", "mélange"])
            
            if operation == "addition":
                a = random.randint(100, 500)
                b = random.randint(100, 500)
                question = f"{a} + {b}"
                reponse = a + b
                
            elif operation == "soustraction":
                a = random.randint(200, 1000)
                b = random.randint(100, a-100)
                question = f"{a} - {b}"
                reponse = a - b
                
            elif operation == "multiplication":
                a = random.randint(10, 25)
                b = random.randint(5, 20)
                question = f"{a} × {b}"
                reponse = a * b
                
            elif operation == "division":
                b = random.randint(3, 15)
                reponse = random.randint(5, 20)
                a = b * reponse
                question = f"{a} ÷ {b}"
                
            else:  # mélange
                # Opération à trois termes
                op1 = random.choice(["+", "-", "×"])
                op2 = random.choice(["+", "-", "×"])
                
                if op1 == "×" or op2 == "×":
                    # Éviter les nombres trop grands
                    nums = [random.randint(1, 12) for _ in range(3)]
                else:
                    nums = [random.randint(10, 100) for _ in range(3)]
                
                question = f"{nums[0]} {op1} {nums[1]} {op2} {nums[2]}"
                
                # Calculer la réponse
                if op1 == "×":
                    temp = nums[0] * nums[1]
                elif op1 == "+":
                    temp = nums[0] + nums[1]
                else:  # "-"
                    temp = nums[0] - nums[1]
                
                if op2 == "×":
                    reponse = temp * nums[2]
                elif op2 == "+":
                    reponse = temp + nums[2]
                else:  # "-"
                    reponse = temp - nums[2]
        
        return {
            "question": question,
            "reponse": reponse,
            "operation": operation,
            "difficulte": self.difficulte
        }

    def _afficher_question(self):
        """Affiche la question actuelle"""
        # Nettoyer le frame
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        
        # Afficher la question
        Label(self.question_frame, text="🧮 QUESTION :", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        question_text = self.question_actuelle["question"]
        Label(self.question_frame, text=question_text, 
              font=("Century Gothic", 36, "bold"), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["texte_fonce"]).pack(pady=10)
        
        # Afficher l'opération
        operation = self.question_actuelle["operation"]
        operation_text = {
            "addition": "Addition",
            "soustraction": "Soustraction", 
            "multiplication": "Multiplication",
            "division": "Division",
            "mélange": "Opération mixte"
        }.get(operation, "Calcul")
        
        Label(self.question_frame, text=f"📝 {operation_text.capitalize()}", 
              font=("Century Gothic", 14), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["texte_clair"]).pack(pady=10)
        
        # Barre de progression du temps
        self.progress_frame = Frame(self.question_frame, bg=self.PALETTE["fond_carte"])
        self.progress_frame.pack(pady=20)
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, length=300, mode='determinate')
        self.progress_bar.pack()
        self.progress_bar['value'] = 100  # Commence à 100%

    def _demarrer_timer(self):
        """Démarre le compte à rebours"""
        if not self.timer_actif:
            return
        
        if self.temps_restant > 0:
            self.temps_restant -= 1
            self.timer_label.config(text=f"{self.temps_restant}s")
            
            # Mettre à jour la barre de progression
            progression = (self.temps_restant / 30) * 100
            self.progress_bar['value'] = progression
            
            # Changer la couleur selon le temps restant
            if self.temps_restant <= 10:
                self.timer_label.config(fg=self.PALETTE["erreur"])
                self.progress_bar.configure(style="red.Horizontal.TProgressbar")
            elif self.temps_restant <= 20:
                self.timer_label.config(fg=self.PALETTE["avertissement"])
                self.progress_bar.configure(style="orange.Horizontal.TProgressbar")
            
            # Appeler à nouveau après 1 seconde
            self.fenetre_jeu.after(1000, self._demarrer_timer)
        else:
            # Temps écoulé
            self._temps_ecoule()

    def _temps_ecoule(self):
        """Quand le temps est écoulé"""
        self.timer_actif = False
        self._verifier_manche(gagnant="ordi", raison="temps écoulé")

    def _valider_reponse(self):
        """Valide la réponse du joueur"""
        if not self.timer_actif:
            return
        
        reponse_joueur = self.reponse_var.get().strip()
        
        if not reponse_joueur:
            self.resultat_label.config(text="❌ Veuillez entrer une réponse !", fg=self.PALETTE["erreur"])
            return
        
        try:
            # Convertir en float pour la comparaison
            reponse_joueur_num = float(reponse_joueur)
            reponse_correcte = float(self.question_actuelle["reponse"])
            
            # Tolérance pour les calculs flottants
            if abs(reponse_joueur_num - reponse_correcte) < 0.001:
                self._verifier_manche(gagnant="joueur", raison="bonne réponse")
            else:
                self._verifier_manche(gagnant="ordi", raison="mauvaise réponse")
                
        except ValueError:
            self.resultat_label.config(text="❌ Réponse invalide ! Entrez un nombre.", fg=self.PALETTE["erreur"])

    def _passer_question(self):
        """Passe la question actuelle"""
        if not self.timer_actif:
            return
        
        self._verifier_manche(gagnant="ordi", raison="question passée")

    def _verifier_manche(self, gagnant, raison):
        """Vérifie le résultat de la manche"""
        if not self.timer_actif and gagnant != "temps écoulé":
            return
        
        self.timer_actif = False
        
        # Enregistrer la réponse du joueur
        reponse_joueur = self.reponse_var.get()
        self.derniere_reponse = reponse_joueur
        self.gagnant_manche = gagnant
        
        # Mettre à jour les scores
        if gagnant == "joueur":
            self.score_joueur += 1
            self.streak += 1
            
            # Bonus de streak
            if self.streak >= 3:
                bonus = min(5, self.streak - 2)  # +1 point par streak au-delà de 3
                self.bonus_streak += bonus
                message = f"✅ BONNE RÉPONSE ! (+1 point"
                if bonus > 0:
                    message += f" +{bonus} bonus streak"
                message += ")"
            else:
                message = "✅ BONNE RÉPONSE ! (+1 point)"
                
            couleur = self.PALETTE["succes"]
            
        else:  # ordi gagne
            self.score_ordi += 1
            self.streak = 0
            
            if raison == "temps écoulé":
                message = "⏱️ TEMPS ÉCOULÉ ! L'ordinateur marque 1 point."
            elif raison == "mauvaise réponse":
                reponse_correcte = self.question_actuelle["reponse"]
                message = f"❌ MAUVAISE RÉPONSE ! La réponse était: {reponse_correcte}"
            else:  # question passée
                message = "⏭️ QUESTION PASSÉE ! L'ordinateur marque 1 point."
            
            couleur = self.PALETTE["erreur"]
        
        # Afficher le résultat
        self.resultat_label.config(text=message, fg=couleur)
        
        # Désactiver les boutons
        self.btn_valider.config(state="disabled")
        self.btn_passer.config(state="disabled")
        self.reponse_entry.config(state="disabled")
        
        # Mettre à jour les scores affichés
        self.score_joueur_label.config(text=f"{self.score_joueur}")
        self.score_ordi_label.config(text=f"{self.score_ordi}")
        
        # Ajouter à l'historique
        historique_msg = f"Manche {self.questions_jouees}: "
        if gagnant == "joueur":
            historique_msg += f"✅ Vous gagnez ({raison})"
        else:
            historique_msg += f"❌ Ordinateur gagne ({raison})"
        
        self._ajouter_historique(historique_msg)
        
        # Passer à la suite
        if self.questions_jouees < self.questions_total:
            self.fenetre_jeu.after(2500, self._nouvelle_manche)
        else:
            self.fenetre_jeu.after(3000, self._afficher_resultat_final)

    def _ajouter_historique(self, message):
        """Ajoute un message à l'historique"""
        self.historique_text.config(state=NORMAL)
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.historique_text.insert(END, f"[{timestamp}] {message}\n")
        self.historique_text.see(END)
        self.historique_text.config(state=DISABLED)
        
        # Ajouter à la liste d'historique
        self.historique_manches.append({
            "temps": timestamp,
            "message": message,
            "manche": self.questions_jouees,
            "score_joueur": self.score_joueur,
            "score_ordi": self.score_ordi
        })

    def _afficher_resultat_final(self):
        """Affiche le résultat final du match"""
        resultat_window = Toplevel(self.fenetre_jeu)
        resultat_window.title("🏆 RÉSULTAT FINAL")
        resultat_window.geometry("600x500")
        resultat_window.configure(bg=self.PALETTE["fond_principal"])
        
        # Empêcher la fermeture
        resultat_window.transient(self.fenetre_jeu)
        resultat_window.grab_set()
        
        # Déterminer le gagnant
        if self.score_joueur > self.score_ordi:
            titre = "🎉 VICTOIRE !"
            message = f"Vous avez battu l'ordinateur {self.score_joueur} à {self.score_ordi} !"
            couleur_titre = self.PALETTE["succes"]
            emoji = "🏆"
        elif self.score_joueur < self.score_ordi:
            titre = "💥 DÉFAITE !"
            message = f"L'ordinateur vous a battu {self.score_ordi} à {self.score_joueur} !"
            couleur_titre = self.PALETTE["erreur"]
            emoji = "😢"
        else:
            titre = "🤝 MATCH NUL !"
            message = f"Égalité parfaite {self.score_joueur} à {self.score_ordi} !"
            couleur_titre = self.PALETTE["avertissement"]
            emoji = "⚖️"
        
        # Titre
        Label(resultat_window, text=emoji, 
              font=("Century Gothic", 48), bg=self.PALETTE["fond_principal"], 
              fg=couleur_titre).pack(pady=20)
        
        Label(resultat_window, text=titre, 
              font=("Century Gothic", 24, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=couleur_titre).pack(pady=10)
        
        # Score final
        score_frame = Frame(resultat_window, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=2)
        score_frame.pack(pady=20, padx=50, fill=X)
        
        Label(score_frame, text="SCORE FINAL", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_clair"]).pack(pady=10)
        
        scores_frame = Frame(score_frame, bg=self.PALETTE["fond_clair"])
        scores_frame.pack(pady=10)
        
        Label(scores_frame, text="VOUS", font=("Century Gothic", 14), 
              bg=self.PALETTE["fond_clair"], fg=self.PALETTE["joueur"]).pack(side=LEFT, padx=30)
        
        Label(scores_frame, text=f"{self.score_joueur} - {self.score_ordi}", 
              font=("Century Gothic", 24, "bold"), bg=self.PALETTE["fond_clair"]).pack(side=LEFT, padx=20)
        
        Label(scores_frame, text="ORDI", font=("Century Gothic", 14), 
              bg=self.PALETTE["fond_clair"], fg=self.PALETTE["ordi"]).pack(side=LEFT, padx=30)
        
        # Détails
        details_frame = Frame(resultat_window, bg=self.PALETTE["fond_principal"])
        details_frame.pack(pady=20, padx=30, fill=X)
        
        details = [
            ("📊 Manches jouées", f"{self.questions_total}"),
            ("🔥 Meilleur streak", f"{self.streak} manches"),
            ("⭐ Bonus streak total", f"{self.bonus_streak} points"),
            ("🎯 Taux de réussite", f"{(self.score_joueur/self.questions_total*100):.1f}%"),
            ("⚡ Temps moyen par question", f"{(30 - self.temps_restant/self.questions_total):.1f}s")
        ]
        
        for label, value in details:
            line_frame = Frame(details_frame, bg=self.PALETTE["fond_principal"])
            line_frame.pack(fill=X, pady=5)
            
            Label(line_frame, text=label, font=("Century Gothic", 11), 
                  bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_fonce"]).pack(side=LEFT)
            
            Label(line_frame, text=value, font=("Century Gothic", 11, "bold"), 
                  bg=self.PALETTE["fond_principal"], fg=self.PALETTE["primaire"]).pack(side=RIGHT)
        
        # Boutons
        boutons_frame = Frame(resultat_window, bg=self.PALETTE["fond_principal"])
        boutons_frame.pack(pady=30)
        
        ttk.Button(boutons_frame, text="🔄 Rejouer", 
                  style="Jeu.TButton", command=lambda: [resultat_window.destroy(), self._recommencer_jeu()]).pack(side=LEFT, padx=10)
        
        ttk.Button(boutons_frame, text="📊 Statistiques détaillées", 
                  style="Jeu.TButton", command=lambda: [resultat_window.destroy(), self._afficher_statistiques()]).pack(side=LEFT, padx=10)
        
        ttk.Button(boutons_frame, text="❌ Quitter", 
                  style="Jeu.TButton", command=lambda: [resultat_window.destroy(), self.fenetre_jeu.destroy()]).pack(side=RIGHT, padx=10)

    def _afficher_statistiques(self):
        """Affiche les statistiques détaillées"""
        stats_window = Toplevel(self.fenetre_jeu)
        stats_window.title("📊 Statistiques Détaillées")
        stats_window.geometry("700x600")
        stats_window.configure(bg=self.PALETTE["fond_principal"])
        
        # Titre
        Label(stats_window, text="📊 STATISTIQUES DÉTAILLÉES", 
              font=("Century Gothic", 20, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        # Cadre avec scrollbar
        stats_container = Frame(stats_window, bg=self.PALETTE["fond_principal"])
        stats_container.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        canvas = Canvas(stats_container, bg=self.PALETTE["fond_clair"])
        scrollbar = Scrollbar(stats_container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.PALETTE["fond_clair"])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Statistiques générales
        Label(scrollable_frame, text="📈 PERFORMANCE GÉNÉRALE", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_clair"]).pack(pady=15)
        
        stats_generales = [
            ("🎯 Score final", f"{self.score_joueur} - {self.score_ordi}"),
            ("📊 Manches totales", f"{self.questions_total}"),
            ("✅ Manches gagnées", f"{self.score_joueur}"),
            ("❌ Manches perdues", f"{self.score_ordi}"),
            ("⚖️ Matchs nuls", f"{self.questions_total - self.score_joueur - self.score_ordi}"),
            ("📈 Taux de victoire", f"{(self.score_joueur/self.questions_total*100):.1f}%"),
            ("🔥 Meilleur streak", f"{self.streak} manches"),
            ("⭐ Bonus streak", f"{self.bonus_streak} points"),
            ("⚡ Temps moyen/réponse", f"{(30 - self.temps_restant/self.questions_total):.1f}s"),
            ("🎮 Difficulté maximale", f"{self.difficulte.capitalize()}")
        ]
        
        for label, value in stats_generales:
            line_frame = Frame(scrollable_frame, bg=self.PALETTE["fond_clair"])
            line_frame.pack(fill=X, padx=20, pady=8)
            
            Label(line_frame, text=label, font=("Century Gothic", 11), 
                  bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"]).pack(side=LEFT)
            
            Label(line_frame, text=value, font=("Century Gothic", 11, "bold"), 
                  bg=self.PALETTE["fond_clair"], fg=self.PALETTE["primaire"]).pack(side=RIGHT)
        
        # Historique détaillé
        if self.historique_manches:
            Label(scrollable_frame, text="📝 HISTORIQUE DES MANCHES", 
                  font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_clair"]).pack(pady=20)
            
            for manche in self.historique_manches[-10:]:  # 10 dernières manches
                manche_frame = Frame(scrollable_frame, bg=self.PALETTE["fond_clair"])
                manche_frame.pack(fill=X, padx=20, pady=5)
                
                Label(manche_frame, text=f"[{manche['temps']}] {manche['message']}", 
                      font=("Century Gothic", 9), bg=self.PALETTE["fond_clair"], 
                      fg=self.PALETTE["texte_clair"], wraplength=600, justify="left").pack(anchor=W)
        
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Bouton fermer
        btn_frame = Frame(stats_window, bg=self.PALETTE["fond_principal"])
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="Fermer", command=stats_window.destroy, style="Jeu.TButton").pack()

    def _afficher_classement(self):
        """Affiche le classement (simulé pour l'instant)"""
        classement_window = Toplevel(self.fenetre_jeu)
        classement_window.title("🏆 CLASSEMENT")
        classement_window.geometry("500x400")
        classement_window.configure(bg=self.PALETTE["fond_principal"])
        
        # Titre
        Label(classement_window, text="🏆 CLASSEMENT MATH BATTLE", 
              font=("Century Gothic", 18, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        # Message d'information
        info_frame = Frame(classement_window, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=1)
        info_frame.pack(fill=X, padx=30, pady=10)
        
        Label(info_frame, text="📢 Le classement en ligne sera disponible\nprochainement avec la version 2.0 !", 
              font=("Century Gothic", 11), bg=self.PALETTE["fond_clair"], 
              fg=self.PALETTE["texte_fonce"], justify="center").pack(pady=15)
        
        # Classement simulé
        classement_frame = Frame(classement_window, bg=self.PALETTE["fond_principal"])
        classement_frame.pack(pady=20, padx=30, fill=X)
        
        Label(classement_frame, text="🏅 MEILLEURS SCORES LOCAUX", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=10)
        
        # Scores locaux simulés (à remplacer par un vrai système de sauvegarde)
        scores_locaux = [
            ("🥇 Vous", f"{self.score_joueur} points"),
            ("🥈 MathMaster42", "18 points"),
            ("🥉 CalculPro", "15 points"),
            ("4. Numero1", "12 points"),
            ("5. Einstein Jr", "10 points")
        ]
        
        for rang, (nom, score) in enumerate(scores_locaux, 1):
            score_frame = Frame(classement_frame, bg=self.PALETTE["fond_clair"])
            score_frame.pack(fill=X, pady=5)
            
            Label(score_frame, text=nom, font=("Century Gothic", 11), 
                  bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"]).pack(side=LEFT, padx=10)
            
            Label(score_frame, text=score, font=("Century Gothic", 11, "bold"), 
                  bg=self.PALETTE["fond_clair"], fg=self.PALETTE["primaire"]).pack(side=RIGHT, padx=10)
        
        # Bouton
        btn_frame = Frame(classement_window, bg=self.PALETTE["fond_principal"])
        btn_frame.pack(pady=20)
        ttk.Button(btn_frame, text="Fermer", command=classement_window.destroy, style="Jeu.TButton").pack()

    def _recommencer_jeu(self):
        """Recommence le jeu depuis le début"""
        # Réinitialiser toutes les variables
        self.score_joueur = 0
        self.score_ordi = 0
        self.manche_actuelle = 1
        self.questions_jouees = 0
        self.temps_restant = 30
        self.timer_actif = False
        self.question_actuelle = None
        self.derniere_reponse = None
        self.gagnant_manche = None
        self.streak = 0
        self.bonus_streak = 0
        self.difficulte = "facile"
        self.historique_manches = []
        
        # Réinitialiser l'historique
        self.historique_text.config(state=NORMAL)
        self.historique_text.delete(1.0, END)
        self.historique_text.config(state=DISABLED)
        
        # Recommencer
        self._nouvelle_manche()


# =============================================================================
# DEFI FIBONACCI
# =============================================================================
class DefisFibonacci:
    def __init__(self, parent, json_file_path="data/defis_fibonacci.json"):
        self.parent = parent
        self.score = 0
        self.niveau = Difficulty.DEBUTANT
        self.defi_actuel = None
        self.indices_decouverts = 0
        self.essais_restants = 3
        self.defis_reussis = 0
        self.defis_joues = 0
        self.streak = 0
        self.bonus_streak = 0
        self.meilleur_streak = 0
        self.verification_en_cours = False
        
        # Suite de Fibonacci pré-calculée
        self.fibonacci_sequence = self._generer_fibonacci(100)  # 100 premiers termes
        
        # Palette de couleurs
        self.PALETTE = {
            "fond_principal": "#FFFFFF",
            "primaire": "#8B5CF6",  # Violet Fibonacci
            "secondaire": "#7C3AED",
            "succes": "#10B981",
            "erreur": "#EF4444",
            "avertissement": "#F59E0B",
            "info": "#3B82F6",
            "texte_fonce": "#1F2937",
            "texte_clair": "#6B7280",
            "fond_clair": "#F3F4F6",
            "fond_carte": "#F8FAFC",
            "fibonacci": "#8B5CF6",  # Couleur spécifique Fibonacci
            "spirale": "#F472B6"      # Rose pour la spirale
        }
        
        # Charger les défis depuis le JSON
        self.defis_data = self._charger_defis(json_file_path)
        
        # Types de défis disponibles
        self.types_defis = {
            "terme_manquant": "Trouver le terme manquant",
            "suite_fibonacci": "Continuer la suite",
            "est_fibonacci": "Vérifier si un nombre est Fibonacci",
            "position_fibonacci": "Trouver la position d'un nombre",
            "somme_fibonacci": "Calculer une somme de Fibonacci",
            "ratio_fibonacci": "Calculer le ratio d'or",
            "spirale_fibonacci": "Dessiner la spirale",
            "nature_fibonacci": "Découvrir dans la nature"
        }
        
        # Historique des réponses
        self.historique_reponses = []
    
    def _generer_fibonacci(self, n):
        """Génère les n premiers nombres de Fibonacci"""
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def _charger_defis(self, json_path):
        """Charge les défis depuis le fichier JSON"""
        try:
            # Vérifier si le fichier existe
            if not os.path.exists(json_path):
                # Créer un fichier par défaut si inexistant
                default_data = {
                    "Débutant": [],
                    "Intermédiaire": [],
                    "Avancé": []
                }
                os.makedirs(os.path.dirname(json_path), exist_ok=True)
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(default_data, f, ensure_ascii=False, indent=2)
                return default_data
            
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur chargement défis Fibonacci: {e}")
            return {"Débutant": [], "Intermédiaire": [], "Avancé": []}
    
    def lancer_jeu(self):
        """Lance la fenêtre du jeu"""
        is_toplevel = self.parent is None or isinstance(self.parent, (Tk, Toplevel))
        if is_toplevel:
            self.fenetre_jeu = Toplevel(self.parent)
            self.fenetre_jeu.title("🌟 Défis Fibonacci")
            self.fenetre_jeu.geometry("950x850")
            self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
        else:
            self.fenetre_jeu = self.parent
            for child in list(self.fenetre_jeu.winfo_children()):
                child.destroy()
            try:
                self.fenetre_jeu.configure(bg=self.PALETTE["fond_principal"])
            except Exception:
                pass

        self._creer_interface()
        self._nouveau_defi()

        # Centrer la fenêtre si Toplevel
        if is_toplevel:
            self.fenetre_jeu.update_idletasks()
            width = self.fenetre_jeu.winfo_width()
            height = self.fenetre_jeu.winfo_height()
            x = (self.fenetre_jeu.winfo_screenwidth() // 2) - (width // 2)
            y = (self.fenetre_jeu.winfo_screenheight() // 2) - (height // 2)
            self.fenetre_jeu.geometry(f'{width}x{height}+{x}+{y}')

        def _retour():
            if is_toplevel:
                self.fenetre_jeu.destroy()
            else:
                try:
                    creer_interface_jeux(self.fenetre_jeu)
                except Exception:
                    pass

        try:
            _ajouter_bouton_retour_to_window(self.fenetre_jeu, is_toplevel, _retour)
        except Exception:
            pass
    
    def _creer_interface(self):
        """Crée l'interface graphique du jeu"""
        # En-tête avec motif Fibonacci
        header_frame = Frame(self.fenetre_jeu, bg=self.PALETTE["primaire"])
        header_frame.pack(fill=X, pady=(0, 10))
        
        # Titre avec emojis Fibonacci
        title_frame = Frame(header_frame, bg=self.PALETTE["primaire"])
        title_frame.pack(pady=15)
        
        Label(title_frame, text="🌟 ", 
              font=("Century Gothic", 28), bg=self.PALETTE["primaire"], fg="white").pack(side=LEFT)
        Label(title_frame, text="DÉFIS FIBONACCI", 
              font=("Century Gothic", 22, "bold"), bg=self.PALETTE["primaire"], fg="white").pack(side=LEFT)
        Label(title_frame, text=" 🌟", 
              font=("Century Gothic", 28), bg=self.PALETTE["primaire"], fg="white").pack(side=LEFT)
        
        Label(header_frame, text="Découvrez la magie de la suite de Fibonacci !", 
              font=("Century Gothic", 12), bg=self.PALETTE["primaire"], fg="white", 
              wraplength=800).pack(pady=(0, 10))

        # Cadre scrollable pour le contenu
        content_container = Frame(self.fenetre_jeu, bg=self.PALETTE["fond_principal"]) 
        content_container.pack(fill=BOTH, expand=True, padx=10, pady=0)
        try:
            from .styles import make_scrollable_frame
            content_frame = make_scrollable_frame(content_container, self.PALETTE["fond_principal"])
        except Exception:
            content_frame = Frame(content_container, bg=self.PALETTE["fond_principal"]) 
            content_frame.pack(fill=BOTH, expand=True)

        # Statistiques principales
        stats_frame = Frame(content_frame, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=1)
        stats_frame.pack(fill=X, padx=20, pady=10)
        
        # Première ligne de stats
        stats_line1 = Frame(stats_frame, bg=self.PALETTE["fond_clair"])
        stats_line1.pack(fill=X, padx=15, pady=10)
        
        # Score
        self.score_label = Label(stats_line1, text=f"🏆 SCORE: {self.score}", 
                                font=("Century Gothic", 13, "bold"), bg=self.PALETTE["fond_clair"], 
                                fg=self.PALETTE["primaire"])
        self.score_label.pack(side=LEFT, padx=20)
        
        # Streak
        self.streak_label = Label(stats_line1, text=f"🔥 STREAK: {self.streak}", 
                                 font=("Century Gothic", 13, "bold"), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["avertissement"])
        self.streak_label.pack(side=LEFT, padx=20)
        
        # Niveau
        self.niveau_label = Label(stats_line1, text=f"📊 NIVEAU: {self.niveau.value}", 
                                 font=("Century Gothic", 13, "bold"), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["secondaire"])
        self.niveau_label.pack(side=LEFT, padx=20)
        
        # Deuxième ligne de stats
        stats_line2 = Frame(stats_frame, bg=self.PALETTE["fond_clair"])
        stats_line2.pack(fill=X, padx=15, pady=(0, 10))
        
        # Essais
        self.essais_label = Label(stats_line2, text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}", 
                                 font=("Century Gothic", 11), bg=self.PALETTE["fond_clair"], 
                                 fg=self.PALETTE["texte_fonce"])
        self.essais_label.pack(side=LEFT, padx=20)
        
        # Défis
        self.defis_label = Label(stats_line2, text=f"✅ DÉFIS: {self.defis_reussis}/{self.defis_joues}", 
                                font=("Century Gothic", 11), bg=self.PALETTE["fond_clair"], 
                                fg=self.PALETTE["texte_fonce"])
        self.defis_label.pack(side=LEFT, padx=20)
        
        # Type de défi
        self.type_label = Label(stats_line2, text=f"🔍 TYPE: ?", 
                               font=("Century Gothic", 11), bg=self.PALETTE["fond_clair"], 
                               fg=self.PALETTE["texte_clair"])
        self.type_label.pack(side=RIGHT, padx=20)
        
        # Cadre principal
        main_frame = Frame(content_frame, bg=self.PALETTE["fond_principal"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # Section supérieure : Défi et spirale
        top_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        top_frame.pack(fill=BOTH, expand=True, pady=10)
        
        # Carte du défi (gauche)
        self.defi_frame = Frame(top_frame, bg=self.PALETTE["fond_carte"], 
                               relief="solid", borderwidth=2)
        self.defi_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        
        # Spirale Fibonacci (droite) - CORRECTION ICI : width dans Frame, pas dans pack()
        self.spirale_frame = Frame(top_frame, bg="#FFFFFF", relief="solid", borderwidth=1, width=250)
        self.spirale_frame.pack(side=RIGHT, fill=BOTH, expand=False)
        self.spirale_frame.pack_propagate(False)  # Empêche le frame de changer de taille
        
        Label(self.spirale_frame, text="🌀 SPIRALE FIBONACCI", 
              font=("Century Gothic", 10, "bold"), bg="#FFFFFF", 
              fg=self.PALETTE["spirale"]).pack(pady=10)
        
        # CORRECTION ICI : width dans Canvas, pas dans pack()
        self.spirale_canvas = Canvas(self.spirale_frame, bg="#FFFFFF", height=200, width=230)
        self.spirale_canvas.pack(pady=5, padx=10)
        
        # Zone de réponse
        reponse_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        reponse_frame.pack(fill=X, pady=15)
        
        Label(reponse_frame, text="🎯 VOTRE RÉPONSE :", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        # Frame pour les contrôles de réponse
        self.controles_reponse_frame = Frame(reponse_frame, bg=self.PALETTE["fond_principal"])
        self.controles_reponse_frame.pack(pady=10)
        
        # Indices
        indices_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        indices_frame.pack(fill=X, pady=10)
        
        Label(indices_frame, text="💡 INDICES DISPONIBLES :", 
              font=("Century Gothic", 12, "bold"), bg=self.PALETTE["fond_principal"]).pack(pady=5)
        
        self.indices_frame = Frame(indices_frame, bg=self.PALETTE["fond_principal"])
        self.indices_frame.pack(pady=10)
        
        # Zone de feedback
        self.feedback_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        self.feedback_frame.pack(fill=X, pady=15)
        
        self.feedback_label = Label(self.feedback_frame, text="", 
                                   font=("Century Gothic", 12), bg=self.PALETTE["fond_principal"], 
                                   wraplength=800)
        self.feedback_label.pack()
        
        # Boutons d'action
        boutons_frame = Frame(main_frame, bg=self.PALETTE["fond_principal"])
        boutons_frame.pack(fill=X, pady=10)
        
        ttk.Button(boutons_frame, text="🔍 Obtenir un indice", 
                  style="Jeu.TButton", command=self._obtenir_indice).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="✅ Valider", 
                  style="Jeu.TButton", command=self._valider_reponse).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="🔄 Nouveau défi", 
                  style="Jeu.TButton", command=self._nouveau_defi).pack(side=LEFT, padx=5)
        
        ttk.Button(boutons_frame, text="📊 Statistiques", 
                  style="Jeu.TButton", command=self._afficher_statistiques).pack(side=RIGHT, padx=5)
        
        ttk.Button(boutons_frame, text="❓ Explication", 
                  style="Jeu.TButton", command=self._afficher_explication).pack(side=RIGHT, padx=5)
        
        ttk.Button(boutons_frame, text="📚 Guide", 
                  style="Jeu.TButton", command=lambda: afficher_guide_jeu("defis_fibonacci", self.fenetre_jeu)).pack(side=RIGHT, padx=5)
        
        # Zone d'historique et faits Fibonacci
        historique_frame = Frame(main_frame, bg=self.PALETTE["fond_clair"], relief="solid", borderwidth=1)
        historique_frame.pack(fill=BOTH, expand=True, pady=10)
        
        # Notebook pour séparer historique et faits
        self.notebook = ttk.Notebook(historique_frame)
        self.notebook.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        # Onglet Historique
        historique_tab = Frame(self.notebook, bg=self.PALETTE["fond_clair"])
        self.notebook.add(historique_tab, text="📝 Historique")
        
        Label(historique_tab, text="HISTORIQUE DES DÉFIS :", 
              font=("Century Gothic", 10, "bold"), bg=self.PALETTE["fond_clair"]).pack(anchor=W, padx=10, pady=5)
        
        self.historique_text = Text(historique_tab, height=6, font=("Century Gothic", 9),
                                   bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"], wrap=WORD)
        scrollbar = Scrollbar(historique_tab, command=self.historique_text.yview)
        self.historique_text.config(yscrollcommand=scrollbar.set)
        self.historique_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.historique_text.config(state=DISABLED)
        
        # Onglet Faits Fibonacci
        faits_tab = Frame(self.notebook, bg=self.PALETTE["fond_clair"])
        self.notebook.add(faits_tab, text="✨ Faits Fibonacci")
        
        faits_content = """
🌟 FAITS SUR LA SUITE DE FIBONACCI :

🌀 LA SPIRALE D'OR
• Chaque carré a pour côté un nombre de Fibonacci
• Le rapport entre termes consécutifs tend vers Φ ≈ 1.618
• C'est le nombre d'or !

🌿 DANS LA NATURE
• Pétales de fleurs (3, 5, 8, 13, 21...)
• Pomme de pin (spirales dans 2 sens)
• Ananas (écailles en spirales)
• Coquillages (nautilus)

🎨 DANS L'ART
• Utilisée par Léonard de Vinci
• Architecture grecque (Parthénon)
• Peintures de la Renaissance

📐 EN MATHÉMATIQUES
• F(n) = F(n-1) + F(n-2)
• F(0) = 0, F(1) = 1
• Liée au triangle de Pascal
"""
        
        faits_text = Text(faits_tab, height=8, font=("Century Gothic", 9),
                         bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"], wrap=WORD)
        faits_text.insert(1.0, faits_content)
        faits_text.config(state=DISABLED)
        faits_text.pack(fill=BOTH, expand=True, padx=10, pady=5)

    def _nouveau_defi(self):
        """Prépare un nouveau défi Fibonacci"""
        self.verification_en_cours = False
        
        # Mettre à jour le niveau selon le score
        if self.score < 150:
            self.niveau = Difficulty.DEBUTANT
        elif self.score < 400:
            self.niveau = Difficulty.INTERMEDIAIRE
        else:
            self.niveau = Difficulty.AVANCE
        
        # Récupérer un défi aléatoire du niveau
        defis_niveau = self.defis_data.get(self.niveau.value, [])
        if not defis_niveau:
            self._creer_defi_auto()
        else:
            self.defi_actuel = random.choice(defis_niveau)
        
        # Réinitialiser les compteurs
        self.indices_decouverts = 0
        self.essais_restants = 3
        
        # Mettre à jour l'interface
        self._afficher_defi()
        self._creer_controles_reponse()
        self._afficher_indices()
        self._effacer_feedback()
        self._dessiner_spirale()
        
        # Mettre à jour les labels
        self.niveau_label.config(text=f"📊 NIVEAU: {self.niveau.value}")
        self.essais_label.config(text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}")
        
        # Afficher le type de défi
        type_defi = self.defi_actuel.get("type", "terme_manquant")
        type_desc = self.types_defis.get(type_defi, "Défi Fibonacci")
        self.type_label.config(text=f"🔍 TYPE: {type_desc}")
        
        self._ajouter_historique(f"🌟 Nouveau défi: {type_desc}")
        self._mettre_a_jour_stats()
        
        # Incrémenter le compteur de défis joués
        self.defis_joues += 1
        self.defis_label.config(text=f"✅ DÉFIS: {self.defis_reussis}/{self.defis_joues}")

    def _creer_defi_auto(self):
        """Crée un défi automatiquement si le fichier est vide"""
        type_defi = random.choice(list(self.types_defis.keys()))
        
        if type_defi == "terme_manquant":
            defi = self._creer_defi_terme_manquant()
        elif type_defi == "suite_fibonacci":
            defi = self._creer_defi_suite()
        elif type_defi == "est_fibonacci":
            defi = self._creer_defi_est_fibonacci()
        elif type_defi == "position_fibonacci":
            defi = self._creer_defi_position()
        elif type_defi == "somme_fibonacci":
            defi = self._creer_defi_somme()
        elif type_defi == "ratio_fibonacci":
            defi = self._creer_defi_ratio()
        else:
            defi = self._creer_defi_terme_manquant()  # Par défaut
        
        self.defi_actuel = defi

    def _creer_defi_terme_manquant(self):
        """Crée un défi 'trouver le terme manquant'"""
        # Choisir une position dans la suite
        if self.niveau == Difficulty.DEBUTANT:
            position = random.randint(2, 8)
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            position = random.randint(5, 15)
        else:
            position = random.randint(10, 25)
        
        # Créer la suite avec un trou
        suite = []
        for i in range(max(0, position-3), position+4):
            if 0 <= i < len(self.fibonacci_sequence):
                if i == position:
                    suite.append("?")
                else:
                    suite.append(str(self.fibonacci_sequence[i]))
        
        question = f"Trouvez le terme manquant dans la suite:\n{', '.join(suite)}"
        reponse = self.fibonacci_sequence[position]
        
        indices = [
            "La suite de Fibonacci commence par 0, 1, 1, 2, 3, 5, 8...",
            "Chaque terme est la somme des deux précédents: F(n) = F(n-1) + F(n-2)",
            f"Le terme avant '?' est {self.fibonacci_sequence[position-1]}",
            f"Le terme après '?' est {self.fibonacci_sequence[position+1]}",
            f"Donc ? = {self.fibonacci_sequence[position-1]} + {self.fibonacci_sequence[position-2]} = {reponse}"
        ]
        
        return {
            "question": question,
            "reponse": reponse,
            "indices": indices,
            "type": "terme_manquant",
            "difficulte": self.niveau.value
        }

    def _creer_defi_suite(self):
        """Crée un défi 'continuer la suite'"""
        if self.niveau == Difficulty.DEBUTANT:
            debut = random.randint(0, 5)
            longueur = 4
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            debut = random.randint(5, 10)
            longueur = 5
        else:
            debut = random.randint(10, 20)
            longueur = 6
        
        # Afficher les premiers termes
        termes = [str(self.fibonacci_sequence[i]) for i in range(debut, debut + longueur)]
        question = f"Continuez la suite de Fibonacci:\n{', '.join(termes)}, ..."
        
        # Demander les 3 termes suivants
        reponse = [
            self.fibonacci_sequence[debut + longueur],
            self.fibonacci_sequence[debut + longueur + 1],
            self.fibonacci_sequence[debut + longueur + 2]
        ]
        
        indices = [
            "Rappel: F(n) = F(n-1) + F(n-2)",
            f"Les deux derniers termes sont: {termes[-2]} et {termes[-1]}",
            f"Le prochain terme est: {termes[-2]} + {termes[-1]} = {reponse[0]}",
            f"Puis: {termes[-1]} + {reponse[0]} = {reponse[1]}",
            f"Ensuite: {reponse[0]} + {reponse[1]} = {reponse[2]}"
        ]
        
        return {
            "question": question,
            "reponse": reponse,
            "indices": indices,
            "type": "suite_fibonacci",
            "difficulte": self.niveau.value
        }

    def _creer_defi_est_fibonacci(self):
        """Crée un défi 'vérifier si un nombre est Fibonacci'"""
        # 50% de chance que ce soit un nombre Fibonacci
        if random.random() < 0.5:
            nombre = random.choice(self.fibonacci_sequence[5:20])  # Éviter les trop petits
            est_fibonacci = True
        else:
            # Choisir un nombre non-Fibonacci
            while True:
                nombre = random.randint(10, 200)
                if nombre not in self.fibonacci_sequence:
                    est_fibonacci = False
                    break
        
        question = f"Le nombre {nombre} fait-il partie de la suite de Fibonacci ?"
        reponse = "Oui" if est_fibonacci else "Non"
        
        if est_fibonacci:
            position = self.fibonacci_sequence.index(nombre)
            indices = [
                "Un nombre est Fibonacci s'il vérifie: 5n² ± 4 est un carré parfait",
                f"Les nombres Fibonacci autour de {nombre}: ...",
                f"On vérifie: 5×{nombre}² + 4 = {5*nombre*nombre + 4}",
                f"Ou: 5×{nombre}² - 4 = {5*nombre*nombre - 4}",
                f"{nombre} est le F({position}) de la suite"
            ]
        else:
            # Trouver les Fibonacci les plus proches
            plus_petit = max([f for f in self.fibonacci_sequence if f < nombre])
            plus_grand = min([f for f in self.fibonacci_sequence if f > nombre])
            indices = [
                f"Les nombres Fibonacci proches: {plus_petit} et {plus_grand}",
                f"Pour être Fibonacci, {nombre} devrait être entre F(k) et F(k+1)",
                f"Mais {nombre} n'est pas égal à {plus_petit} + {self.fibonacci_sequence[self.fibonacci_sequence.index(plus_petit)-1]}",
                f"Donc {nombre} n'est pas un nombre Fibonacci"
            ]
        
        return {
            "question": question,
            "reponse": reponse,
            "indices": indices,
            "type": "est_fibonacci",
            "difficulte": self.niveau.value
        }

    def _creer_defi_position(self):
        """Crée un défi 'trouver la position d'un nombre Fibonacci'"""
        if self.niveau == Difficulty.DEBUTANT:
            position = random.randint(3, 10)
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            position = random.randint(8, 20)
        else:
            position = random.randint(15, 30)
        
        nombre = self.fibonacci_sequence[position]
        question = f"À quelle position se trouve le nombre {nombre} dans la suite de Fibonacci ?\n(Rappel: F(0)=0, F(1)=1)"
        
        indices = [
            "Les premiers termes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...",
            f"Cherchez où se trouve {nombre} dans cette liste",
            f"Le terme F({position-1}) = {self.fibonacci_sequence[position-1]}",
            f"Le terme F({position+1}) = {self.fibonacci_sequence[position+1]}",
            f"Donc {nombre} est le F({position})"
        ]
        
        return {
            "question": question,
            "reponse": position,
            "indices": indices,
            "type": "position_fibonacci",
            "difficulte": self.niveau.value
        }

    def _creer_defi_somme(self):
        """Crée un défi 'calculer une somme de Fibonacci'"""
        if self.niveau == Difficulty.DEBUTANT:
            n = random.randint(3, 6)
            question = f"Calculez la somme des {n} premiers nombres de Fibonacci (F(0) à F({n-1}))"
            reponse = sum(self.fibonacci_sequence[:n])
            
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            a = random.randint(2, 8)
            b = random.randint(a+1, a+5)
            question = f"Calculez F({a}) + F({a+1}) + ... + F({b})"
            reponse = sum(self.fibonacci_sequence[a:b+1])
            
        else:  # Avancé
            # Somme des carrés ou autre propriété
            n = random.randint(4, 8)
            question = f"Calculez F(1)² + F(2)² + ... + F({n})²"
            reponse = sum([f*f for f in self.fibonacci_sequence[1:n+1]])
        
        indices = [
            "Propriété: F(0)+F(1)+...+F(n) = F(n+2) - 1",
            "Pour les sommes partielles: F(a)+...+F(b) = F(b+2) - F(a+1)",
            "Pour les carrés: F(1)²+...+F(n)² = F(n)×F(n+1)",
            "Calculez terme par terme si nécessaire"
        ]
        
        return {
            "question": question,
            "reponse": reponse,
            "indices": indices,
            "type": "somme_fibonacci",
            "difficulte": self.niveau.value
        }

    def _creer_defi_ratio(self):
        """Crée un défi sur le ratio d'or"""
        if self.niveau == Difficulty.DEBUTANT:
            n = random.randint(5, 10)
            question = f"Calculez F({n+1}) / F({n}) (arrondi à 3 décimales)"
            reponse = round(self.fibonacci_sequence[n+1] / self.fibonacci_sequence[n], 3)
            
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            question = "Quelle est la valeur du nombre d'or Φ (phi) ?\n(arrondi à 5 décimales)"
            reponse = 1.61803
            
        else:  # Avancé
            question = "Résolvez: Φ² = Φ + 1\nQuelle est la valeur positive de Φ ?"
            reponse = (1 + math.sqrt(5)) / 2
        
        indices = [
            "Le ratio F(n+1)/F(n) tend vers Φ quand n→∞",
            "Φ ≈ 1.618033988749895...",
            "Φ est solution de Φ² = Φ + 1",
            "Formule: Φ = (1 + √5) / 2",
            "Pour n grand, le ratio est très proche de Φ"
        ]
        
        return {
            "question": question,
            "reponse": reponse,
            "indices": indices,
            "type": "ratio_fibonacci",
            "difficulte": self.niveau.value
        }

    def _afficher_defi(self):
        """Affiche le défi actuel"""
        # Nettoyer le frame
        for widget in self.defi_frame.winfo_children():
            widget.destroy()
        
        # Afficher le défi
        Label(self.defi_frame, text="🧩 DÉFI FIBONACCI", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        question_text = self.defi_actuel["question"]
        Label(self.defi_frame, text=question_text, 
              font=("Century Gothic", 14), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["texte_fonce"], wraplength=550, justify="center").pack(pady=10, padx=20)
        
        # Afficher des informations sur Fibonacci selon le niveau
        info_frame = Frame(self.defi_frame, bg=self.PALETTE["fond_carte"])
        info_frame.pack(pady=20)
        
        if self.niveau == Difficulty.DEBUTANT:
            info_text = "Rappel: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)"
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            info_text = "Suite: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144..."
        else:
            info_text = "Φ ≈ 1.618 | F(n) ≈ Φⁿ/√5"
        
        Label(info_frame, text=info_text, 
              font=("Century Gothic", 11, "italic"), bg=self.PALETTE["fond_carte"], 
              fg=self.PALETTE["texte_clair"]).pack()

    def _dessiner_spirale(self):
        """Dessine une spirale de Fibonacci"""
        self.spirale_canvas.delete("all")
        
        # Dimensions
        width = 230
        height = 200
        x_center = width // 2
        y_center = height // 2
        
        # Taille des carrés (adaptée à l'espace)
        taille_base = 10
        if self.niveau == Difficulty.DEBUTANT:
            n_carres = 6
        elif self.niveau == Difficulty.INTERMEDIAIRE:
            n_carres = 7
        else:
            n_carres = 8
        
        # Calculer les tailles des carrés
        tailles = [taille_base * self.fibonacci_sequence[i] for i in range(1, n_carres+1)]
        
        # Position initiale
        x, y = x_center, y_center
        angle = 0
        
        # Couleurs alternées
        couleurs = ["#FEE2E2", "#FEF3C7", "#D1FAE5", "#DBEAFE", "#EDE9FE"]
        
        for i in range(n_carres):
            taille = tailles[i]
            couleur = couleurs[i % len(couleurs)]
            
            # Dessiner le carré
            self.spirale_canvas.create_rectangle(
                x, y, x + taille, y + taille,
                fill=couleur, outline=self.PALETTE["spirale"], width=1
            )
            
            # Dessiner le quart de cercle pour la spirale
            start_angle = angle
            end_angle = angle + 90
            
            if i % 4 == 0:  # En bas à droite
                self.spirale_canvas.create_arc(
                    x, y, x + 2*taille, y + 2*taille,
                    start=start_angle, extent=90,
                    outline=self.PALETTE["spirale"], width=2, style="arc"
                )
                x += taille
            elif i % 4 == 1:  # En haut à droite
                self.spirale_canvas.create_arc(
                    x - taille, y, x + taille, y + 2*taille,
                    start=start_angle, extent=90,
                    outline=self.PALETTE["spirale"], width=2, style="arc"
                )
                y -= taille
            elif i % 4 == 2:  # En haut à gauche
                self.spirale_canvas.create_arc(
                    x - 2*taille, y - taille, x, y + taille,
                    start=start_angle, extent=90,
                    outline=self.PALETTE["spirale"], width=2, style="arc"
                )
                x -= taille
            else:  # En bas à gauche
                self.spirale_canvas.create_arc(
                    x, y - 2*taille, x + 2*taille, y,
                    start=start_angle, extent=90,
                    outline=self.PALETTE["spirale"], width=2, style="arc"
                )
                y += taille
            
            angle = (angle + 90) % 360
        
        # Ajouter le texte "Spirale d'or"
        self.spirale_canvas.create_text(
            width // 2, height - 15,
            text="Spirale d'or 🌟",
            font=("Century Gothic", 8, "bold"),
            fill=self.PALETTE["spirale"]
        )

    def _creer_controles_reponse(self):
        """Crée les contrôles de réponse adaptés au type de défi"""
        # Nettoyer le frame
        for widget in self.controles_reponse_frame.winfo_children():
            widget.destroy()
        
        type_defi = self.defi_actuel.get("type", "terme_manquant")
        
        if type_defi in ["est_fibonacci"]:
            # Boutons Oui/Non
            boutons_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            boutons_frame.pack()
            
            self.btn_oui = ttk.Button(boutons_frame, text="✅ OUI", 
                                     style="Jeu.TButton", command=lambda: self._valider_reponse_choix("Oui"), width=15)
            self.btn_oui.pack(side=LEFT, padx=10)
            
            self.btn_non = ttk.Button(boutons_frame, text="❌ NON", 
                                     style="Jeu.TButton", command=lambda: self._valider_reponse_choix("Non"), width=15)
            self.btn_non.pack(side=LEFT, padx=10)
            
        elif type_defi in ["suite_fibonacci"]:
            # Plusieurs champs pour une suite
            saisie_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            saisie_frame.pack()
            
            Label(saisie_frame, text="Prochains termes (séparés par des virgules):", 
                  font=("Century Gothic", 11), bg=self.PALETTE["fond_principal"]).pack(pady=5)
            
            self.reponse_entry = Entry(saisie_frame, font=("Century Gothic", 14), 
                                      width=30, justify="center")  # width dans Entry, pas dans pack
            self.reponse_entry.pack(pady=5)
            self.reponse_entry.bind("<Return>", lambda e: self._valider_reponse())
            
            Label(saisie_frame, text="Ex: 13, 21, 34", 
                  font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], 
                  fg=self.PALETTE["texte_clair"]).pack(pady=2)
            
            ttk.Button(saisie_frame, text="✅ Valider", 
                      style="Jeu.TButton", command=self._valider_reponse).pack(pady=10)
            
        else:
            # Champ de saisie unique
            saisie_frame = Frame(self.controles_reponse_frame, bg=self.PALETTE["fond_principal"])
            saisie_frame.pack()
            
            Label(saisie_frame, text="Entrez votre réponse :", 
                  font=("Century Gothic", 11), bg=self.PALETTE["fond_principal"]).pack(pady=5)
            
            self.reponse_entry = Entry(saisie_frame, font=("Century Gothic", 14), 
                                      width=20, justify="center")  # width dans Entry, pas dans pack
            self.reponse_entry.pack(pady=5)
            self.reponse_entry.bind("<Return>", lambda e: self._valider_reponse())
            
            # Indication selon le type
            if type_defi == "ratio_fibonacci":
                Label(saisie_frame, text="(nombre décimal si nécessaire)", 
                      font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], 
                      fg=self.PALETTE["texte_clair"]).pack(pady=2)
            
            ttk.Button(saisie_frame, text="✅ Valider", 
                      style="Jeu.TButton", command=self._valider_reponse).pack(pady=10)
    
    def _valider_reponse(self):
        """Méthode principale de validation qui redirige vers la bonne méthode"""
        type_defi = self.defi_actuel.get("type", "terme_manquant")
        
        if type_defi in ["est_fibonacci"]:
            # Pour ce type, les boutons Oui/Non appellent directement _valider_reponse_choix
            # Cette méthode ne devrait pas être appelée directement pour ce type
            return
        else:
            # Pour les autres types, appeler la méthode de validation textuelle
            self._valider_reponse_texte()

    def _valider_reponse_choix(self, reponse_joueur):
        """Valide une réponse à choix (Oui/Non)"""
        if self.verification_en_cours:
            return
            
        if self.essais_restants <= 0:
            return
        
        # Désactiver les contrôles
        self._desactiver_controles()
        self.verification_en_cours = True
        
        self.essais_restants -= 1
        self.essais_label.config(text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}")
        
        reponse_correcte = self.defi_actuel["reponse"]
        
        if reponse_joueur == reponse_correcte:
            self._reussite_defi()
        else:
            self._echec_essai()
        
        if self.essais_restants <= 0:
            self.fenetre_jeu.after(1000, self._defi_echoue)

    def _valider_reponse_texte(self):
        """Valide une réponse textuelle"""
        if self.verification_en_cours:
            return
            
        if self.essais_restants <= 0:
            return
        
        # Récupérer la réponse
        try:
            reponse_joueur = self.reponse_entry.get().strip()
        except:
            self._afficher_feedback("❌ Veuillez entrer une réponse", self.PALETTE["erreur"])
            return
        
        if not reponse_joueur:
            self._afficher_feedback("❌ Veuillez entrer une réponse", self.PALETTE["erreur"])
            return
        
        # Désactiver les contrôles
        self._desactiver_controles()
        self.verification_en_cours = True
        
        self.essais_restants -= 1
        self.essais_label.config(text=f"🎯 ESSAIS RESTANTS: {self.essais_restants}")
        
        reponse_correcte = self.defi_actuel["reponse"]
        type_defi = self.defi_actuel.get("type", "terme_manquant")
        
        # Vérification selon le type
        if self._valider_reponse_selon_type(reponse_joueur, reponse_correcte, type_defi):
            self._reussite_defi()
        else:
            self._echec_essai()
        
        if self.essais_restants <= 0:
            self.fenetre_jeu.after(1000, self._defi_echoue)

    def _valider_reponse_selon_type(self, reponse_joueur, reponse_correcte, type_defi):
        """Valide une réponse selon le type de défi"""
        try:
            if type_defi == "suite_fibonacci":
                # Valider une liste de nombres
                nombres_joueur = [int(x.strip()) for x in reponse_joueur.replace(",", " ").split()]
                if isinstance(reponse_correcte, list):
                    return nombres_joueur == reponse_correcte
                else:
                    return False
                
            elif type_defi == "ratio_fibonacci":
                # Valider un nombre décimal avec tolérance
                try:
                    val_joueur = float(reponse_joueur)
                    val_correcte = float(reponse_correcte)
                    return abs(val_joueur - val_correcte) < 0.001
                except:
                    return False
                
            else:
                # Validation numérique simple
                try:
                    return int(reponse_joueur) == int(reponse_correcte)
                except:
                    return reponse_joueur == str(reponse_correcte)
                    
        except:
            return False

    def _afficher_indices(self):
        """Affiche les indices disponibles"""
        # Nettoyer le frame
        for widget in self.indices_frame.winfo_children():
            widget.destroy()
        
        indices = self.defi_actuel.get("indices", [])
        
        if not indices:
            Label(self.indices_frame, text="Aucun indice disponible", 
                  font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], 
                  fg=self.PALETTE["texte_clair"]).pack(pady=5)
            return
        
        for i in range(len(indices)):
            if i < self.indices_decouverts:
                Label(self.indices_frame, text=f"💡 {indices[i]}", 
                      font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], 
                      fg="#10B981", wraplength=700, justify="left").pack(anchor=W, pady=3)
            else:
                Label(self.indices_frame, text=f"🔒 Indice {i+1} (coût: 5 points)", 
                      font=("Century Gothic", 9), bg=self.PALETTE["fond_principal"], 
                      fg=self.PALETTE["texte_clair"], wraplength=700, 
                      justify="left").pack(anchor=W, pady=3)

    def _obtenir_indice(self):
        """Donne un indice au joueur"""
        indices = self.defi_actuel.get("indices", [])
        
        if not indices:
            self._afficher_feedback("❌ Aucun indice disponible", self.PALETTE["erreur"])
            return
        
        if self.indices_decouverts >= len(indices):
            self._afficher_feedback("❌ Plus d'indices disponibles !", self.PALETTE["erreur"])
            return
        
        penalite = 5
        if self.score >= penalite:
            self.score -= penalite
            self.indices_decouverts += 1
            
            self._ajouter_historique(f"📉 Indice acheté: -{penalite} points")
            self._afficher_feedback(f"💡 Indice {self.indices_decouverts} révélé ! (-{penalite} points)", 
                                  "#F59E0B")
            
            self._afficher_indices()
            self._mettre_a_jour_stats()
        else:
            self._afficher_feedback("❌ Pas assez de points pour un indice !", self.PALETTE["erreur"])

    def _desactiver_controles(self):
        """Désactive tous les contrôles de réponse"""
        for widget in self.controles_reponse_frame.winfo_children():
            if isinstance(widget, ttk.Button, style="Jeu.TButton"):
                widget.config(state="disabled")
            elif isinstance(widget, Frame):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Button, style="Jeu.TButton"):
                        child.config(state="disabled")
                    elif isinstance(child, Entry):
                        child.config(state="disabled")

    def _reactiver_controles(self):
        """Réactive les contrôles de réponse"""
        type_defi = self.defi_actuel.get("type", "terme_manquant")
        
        if type_defi in ["est_fibonacci"]:
            for widget in self.controles_reponse_frame.winfo_children():
                if isinstance(widget, ttk.Button, style="Jeu.TButton"):
                    widget.config(state="normal")
                elif isinstance(widget, Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, ttk.Button, style="Jeu.TButton"):
                            child.config(state="normal")
        else:
            for widget in self.controles_reponse_frame.winfo_children():
                if isinstance(widget, Entry):
                    widget.config(state="normal")
                elif isinstance(widget, Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, Entry):
                            child.config(state="normal")
                        elif isinstance(child, ttk.Button, style="Jeu.TButton"):
                            child.config(state="normal")

    def _reussite_defi(self):
        """Quand le défi est réussi"""
        try:
            points = self._calculer_points()
            self.score += points
            self.streak += 1
            self.defis_reussis += 1
            
            if self.streak > self.meilleur_streak:
                self.meilleur_streak = self.streak
            
            # Bonus de streak
            bonus_streak = 0
            if self.streak >= 3:
                bonus_streak = min(10, self.streak * 2)
                self.score += bonus_streak
                self.bonus_streak += bonus_streak
            
            reponse_correcte = self.defi_actuel["reponse"]
            message = f"✅ DÉFI RÉUSSI ! (+{points} points"
            if bonus_streak:
                message += f" +{bonus_streak} bonus streak"
            message += f")\nRéponse: {reponse_correcte}"
            
            self._afficher_feedback(message, self.PALETTE["succes"])
            self._ajouter_historique(f"✅ Défi réussi ! +{points} points")
            self._mettre_a_jour_stats()
            
            # Nouveau défi après délai
            self.fenetre_jeu.after(3000, self._nouveau_defi)
            
        except Exception as e:
            print(f"Erreur dans _reussite_defi: {e}")
            self._afficher_feedback(f"❌ Erreur: {str(e)}", self.PALETTE["erreur"])
            self.verification_en_cours = False

    def _echec_essai(self):
        """Quand un essai échoue"""
        try:
            if self.essais_restants > 0:
                self._reactiver_controles()
                self.verification_en_cours = False
                
                self._afficher_feedback(f"❌ Réponse incorrecte. Essais restants: {self.essais_restants}", 
                                      self.PALETTE["erreur"])
            else:
                self._afficher_feedback("❌ Réponse incorrecte.", self.PALETTE["erreur"])
            
            self._ajouter_historique(f"❌ Essai incorrect")
            self._mettre_a_jour_stats()
            
        except Exception as e:
            print(f"Erreur dans _echec_essai: {e}")
            self.verification_en_cours = False

    def _defi_echoue(self):
        """Quand le défi échoue"""
        try:
            self.streak = 0
            self.bonus_streak = 0
            
            reponse_correcte = self.defi_actuel["reponse"]
            penalite = 10
            self.score = max(0, self.score - penalite)
            
            self._afficher_feedback(f"💥 DÉFI ÉCHOUÉ ! Réponse: {reponse_correcte} (-{penalite} points)", 
                                  self.PALETTE["erreur"])
            
            self._ajouter_historique(f"💥 Défi échoué. -{penalite} points")
            self._mettre_a_jour_stats()
            
            self.fenetre_jeu.after(3000, self._nouveau_defi)
            
        except Exception as e:
            print(f"Erreur dans _defi_echoue: {e}")
            self.fenetre_jeu.after(1000, self._nouveau_defi)

    def _calculer_points(self):
        """Calcule les points gagnés"""
        points_base = 25
        niveau_multiplier = {
            Difficulty.DEBUTANT: 1,
            Difficulty.INTERMEDIAIRE: 1.5,
            Difficulty.AVANCE: 2
        }
        
        bonus_essais = self.essais_restants * 3
        malus_indices = self.indices_decouverts * 3
        
        multiplicateur = niveau_multiplier.get(self.niveau, 1)
        points = (points_base + bonus_essais - malus_indices) * multiplicateur
        
        return max(15, round(points))

    def _ajouter_historique(self, message):
        """Ajoute un message à l'historique"""
        self.historique_text.config(state=NORMAL)
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.historique_text.insert(END, f"[{timestamp}] {message}\n")
        self.historique_text.see(END)
        self.historique_text.config(state=DISABLED)
        
        self.historique_reponses.append({
            "temps": timestamp,
            "message": message,
            "defi": self.defis_joues,
            "score": self.score
        })

    def _effacer_feedback(self):
        """Efface le feedback"""
        self.feedback_label.config(text="")

    def _afficher_feedback(self, message, couleur):
        """Affiche un message de feedback"""
        self.feedback_label.config(text=message, fg=couleur)

    def _mettre_a_jour_stats(self):
        """Met à jour toutes les statistiques"""
        self.score_label.config(text=f"🏆 SCORE: {self.score}")
        self.streak_label.config(text=f"🔥 STREAK: {self.streak}")
        self.defis_label.config(text=f"✅ DÉFIS: {self.defis_reussis}/{self.defis_joues}")
        
        if self.score < 150:
            niveau_text = "Débutant"
        elif self.score < 400:
            niveau_text = "Intermédiaire"
        else:
            niveau_text = "Avancé"
        self.niveau_label.config(text=f"📊 NIVEAU: {niveau_text}")

    def _afficher_statistiques(self):
        """Affiche les statistiques détaillées"""
        stats_window = Toplevel(self.fenetre_jeu)
        stats_window.title("📊 Statistiques Fibonacci")
        stats_window.geometry("600x500")
        stats_window.configure(bg=self.PALETTE["fond_principal"])
        
        Label(stats_window, text="📊 STATISTIQUES FIBONACCI", 
              font=("Century Gothic", 18, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        stats_content = [
            ("🌟 Score total", f"{self.score} points"),
            ("🔥 Meilleur streak", f"{self.meilleur_streak} défis"),
            ("✅ Défis réussis", f"{self.defis_reussis}"),
            ("📊 Défis joués", f"{self.defis_joues}"),
            ("📈 Taux de réussite", f"{(self.defis_reussis/self.defis_joues*100 if self.defis_joues > 0 else 0):.1f}%"),
            ("🔍 Indices utilisés", f"{self.indices_decouverts}"),
            ("⭐ Bonus streak total", f"{self.bonus_streak} points"),
            ("🎯 Niveau actuel", f"{self.niveau.value}")
        ]
        
        for label, value in stats_content:
            line_frame = Frame(stats_window, bg=self.PALETTE["fond_principal"])
            line_frame.pack(fill=X, padx=50, pady=8)
            
            Label(line_frame, text=label, font=("Century Gothic", 11), 
                  bg=self.PALETTE["fond_principal"], fg=self.PALETTE["texte_fonce"]).pack(side=LEFT)
            
            Label(line_frame, text=value, font=("Century Gothic", 11, "bold"), 
                  bg=self.PALETTE["fond_principal"], fg=self.PALETTE["primaire"]).pack(side=RIGHT)
        
        ttk.Button(stats_window, text="Fermer", command=stats_window.destroy, style="Jeu.TButton").pack(pady=20)

    def _afficher_explication(self):
        """Affiche l'explication complète"""
        penalite = 10
        self.score = max(0, self.score - penalite)
        
        explication_window = Toplevel(self.fenetre_jeu)
        explication_window.title("📚 Explication Fibonacci")
        explication_window.geometry("500x400")
        explication_window.configure(bg=self.PALETTE["fond_principal"])
        
        Label(explication_window, text="📚 EXPLICATION COMPLÈTE", 
              font=("Century Gothic", 16, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["primaire"]).pack(pady=20)
        
        Label(explication_window, text=self.defi_actuel["question"], 
              font=("Century Gothic", 12), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["texte_fonce"], wraplength=450).pack(pady=10)
        
        reponse = self.defi_actuel["reponse"]
        Label(explication_window, text=f"Réponse: {reponse}", 
              font=("Century Gothic", 14, "bold"), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["succes"]).pack(pady=10)
        
        explication_text = Text(explication_window, height=10, font=("Century Gothic", 10),
                               bg=self.PALETTE["fond_clair"], fg=self.PALETTE["texte_fonce"], 
                               wrap=WORD)
        scrollbar = Scrollbar(explication_window, command=explication_text.yview)
        explication_text.config(yscrollcommand=scrollbar.set)
        
        indices = self.defi_actuel.get("indices", [])
        for indice in indices:
            explication_text.insert(END, f"• {indice}\n\n")
        
        explication_text.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=5)
        scrollbar.pack(side=RIGHT, fill=Y)
        explication_text.config(state=DISABLED)
        
        Label(explication_window, text=f"(-{penalite} points)", 
              font=("Century Gothic", 10), bg=self.PALETTE["fond_principal"], 
              fg=self.PALETTE["texte_clair"]).pack(pady=10)
        
        ttk.Button(explication_window, text="Fermer", 
                  command=explication_window.destroy, style="Jeu.TButton").pack(pady=10)
        
        self._ajouter_historique(f"📚 Explication achetée: -{penalite} points")
        self._mettre_a_jour_stats()
# =============================================================================
# FONCTIONS D'ACCÈS UNIFIÉES
# =============================================================================
def lancer_jeu_des_24(parent=None):
    """Lance le Jeu des 24"""
    jeu = JeuDes24(parent)
    jeu.lancer_jeu()

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

def lancer_mystere_math(parent=None):
    """Lance le Mystère Mathématique"""
    jeu = MystereMathematique(parent)
    jeu.lancer_jeu()

def lancer_chasse_premiers(parent=None):
    """Lancer le Jeu Chasse aux Nombres Premiers"""
    jeu = ChasseNombresPremiers(parent)
    jeu.lancer_jeu()

def lancer_math_battle(parent=None):
    """Lancer le Jeu Chasse aux Nombres Premiers"""
    jeu = MathBattle(parent)
    jeu.lancer_jeu()

def lancer_defis_fibonacci(parent):
    """Lance le jeu Défis Fibonacci"""
    try:
        jeu = DefisFibonacci(parent, "data/defis_fibonacci.json")
        jeu.lancer_jeu()
    except Exception as e:
        print(f"Erreur lancement Défis Fibonacci: {e}")
        messagebox.showerror("Erreur", f"Impossible de lancer le jeu:\n{str(e)}")

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
    },{
        "nom": "🕵️ Mystère Mathématique",
        "description": "Énigmes et casse-têtes mathématiques\n• Développe la pensée critique\n• Système d'indices stratégiques\n• Journal de résolution",
        "fonction": lancer_mystere_math,
        "disponible": True,
        "guide": lambda parent: afficher_guide_jeu("mystere_math", parent)
    },
    {
    "nom": "🔢 Chasse aux Nombres Premiers",
    "description": "Testez votre instinct mathématique !\n• Identifiez les nombres premiers vs composites\n• 3 niveaux de difficulté progressive\n• Système de streak et bonus de performance\n• Indices stratégiques et explications détaillées",
    "fonction": lancer_chasse_premiers,
    "disponible": True,
    "guide": lambda parent: afficher_guide_jeu("chasse_premiers", parent)
    },{
    "nom": "⚔️ Math Battle",
    "description": "Affrontez l'ordinateur en calcul mental rapide !\n• 10 manches avec timer de 30 secondes\n• Difficulté progressive (facile → difficile)\n• Système de streak avec bonus de points\n• Différentes opérations : +, -, ×, ÷, mélange",
    "fonction": lancer_math_battle,
    "disponible": True,
    "guide": lambda parent: afficher_guide_jeu("math_battle", parent)
},
{
    "nom": "🌟 Défis Fibonacci",
    "description": "Explorez la célèbre suite mathématique !\n• 8 types de défis variés\n• Spirale Fibonacci interactive\n• Faits sur le nombre d'or et la nature\n• Apprenez les propriétés mathématiques",
    "fonction": lancer_defis_fibonacci,
    "disponible": True,
    "guide": lambda parent: afficher_guide_jeu("defis_fibonacci", parent)
}
]
