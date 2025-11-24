import math
from tkinter import *
from tkinter import ttk
from .modules import polynome1, polynome2, polynome3, voir_graphe1, voir_graphe2, voir_graphe3

# Import simplifié
try:
    from .historique_manager import historique_manager
except ImportError:
    # Solution de secours
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from App.historique_manager import historique_manager

def enregistrer_calcul(module, operation, entree, resultat):
    """Fonction wrapper pour l'historique"""
    return historique_manager.ajouter_calcul(module, operation, entree, resultat)

def configurer_style():
    style = ttk.Style()
    style.configure("Custom.TButton",
                    foreground="#FFFFFF",
                    background="#3B82F6",  # Bleu moderne comme main.py
                    font=("Century Gothic", 14),
                    relief="flat")
    
    # Style spécial pour le bouton Quitter
    style.configure("Quit.TButton",
                    foreground="#FFFFFF",
                    background="#DC2626",  # Rouge
                    font=("Century Gothic", 14),
                    relief="flat")
    return style

style = configurer_style()

# ------------------ Polynôme de degré 1 ------------------
def lancer_polynome1():
    fenetre_polynome1 = Toplevel()
    fenetre_polynome1.configure(bg="#F0F4F8")  # Même fond que main.py
    fenetre_polynome1.title("Polynome dégré 1")
    fenetre_polynome1.geometry("500x700")

    def lancer_graphe1():
        # Récupération et conversion des valeurs
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        
        if nombre1 and nombre2:
            try:
                # Conversion en float
                a = float(nombre1)
                b = float(nombre2)
                voir_graphe1(a, b)  # Maintenant on passe des nombres !
            except ValueError:
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg="#DC2626")
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg="#DC2626")

    def recherche_resultat():
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        
        if nombre1 and nombre2:
            try:
                resultat = polynome1(nombre1, nombre2)
                
                # === SAUVEGARDE DU CALCUL ===
                entree_data = {
                    "a": nombre1,
                    "b": nombre2
                }
                historique_manager.ajouter_calcul(
                    module="Polynômes",
                    operation="Équation degré 1",
                    entree=entree_data,
                    resultat=resultat
                )
                # ============================
                
                if "✅" in resultat:
                    result_label.config(text=f"Résultat : {resultat}", fg="#1E40AF")
                else:
                    result_label.config(text=f"Résultat : {resultat}", fg="#DC2626")
            except Exception as e:
                result_label.config(text=f"Erreur : {e}", fg="#DC2626")
        else:
            result_label.config(text="Entrez des valeurs correctes", fg="#DC2626")

    label1 = Label(fenetre_polynome1, text="RESOLUTION DES POLYNOMES DE DEGRE 1",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label1.pack(pady=10)

    label2 = Label(fenetre_polynome1, text="Entrez la valeur de a",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome1, height=1, width=40, font=("Century Gothic", 14))
    entre1.pack()

    label3 = Label(fenetre_polynome1, text="Entrez la valeur de b",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome1, height=1, width=40, font=("Century Gothic", 14))
    entre2.pack()

    result_label = Label(fenetre_polynome1, text="Résultat :", font=("Century Gothic", 14), bg="#F0F4F8", fg="#1E40AF")
    result_label.pack(pady=10)

    button = ttk.Button(fenetre_polynome1, style="Custom.TButton", text="Calculez", command=recherche_resultat)
    button.pack(pady=20)

    button2 = ttk.Button(fenetre_polynome1, style="Custom.TButton", text="Voir le Graphe", command=lancer_graphe1)
    button2.pack(pady=20)

    # Bouton Quitter
    button_quitter = ttk.Button(fenetre_polynome1, style="Quit.TButton", text="Quitter", 
                               command=fenetre_polynome1.destroy)
    button_quitter.pack(pady=10)

# ------------------ Polynôme de degré 2 ------------------
def lancer_polynome2():
    fenetre_polynome2 = Toplevel()
    fenetre_polynome2.configure(bg="#F0F4F8")  # Même fond que main.py
    fenetre_polynome2.title("Polynome degré 2")
    fenetre_polynome2.geometry("500x1000")

    # === Fonction pour afficher le graphe ===
    def lancer_graphe2():
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        nombre3 = entre3.get("1.0", "end").strip()
        
        if nombre1 and nombre2 and nombre3:
            try:
                a = float(nombre1)
                b = float(nombre2)
                c = float(nombre3)
                voir_graphe2(a, b, c)  # Fonction externe
            except ValueError:
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg="#DC2626")
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg="#DC2626")

    # === Fonction pour calculer le résultat ===
    def recherche_resultat():
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        nombre3 = entre3.get("1.0", "end").strip()
        
        if nombre1 and nombre2 and nombre3:
            try:
                resultat = polynome2(nombre1, nombre2, nombre3)
                
                # Sauvegarde du calcul
                entree_data = {
                    "a": nombre1,
                    "b": nombre2,
                    "c": nombre3
                }
                historique_manager.ajouter_calcul(
                    module="Polynômes",
                    operation="Équation degré 2",
                    entree=entree_data,
                    resultat=resultat
                )
                
                if "✅" in resultat:
                    result_label.config(text=f"Résultat : {resultat}", fg="#1E40AF")
                else:
                    result_label.config(text=f"Résultat : {resultat}", fg="#DC2626")
            except Exception as e:
                result_label.config(text=f"Erreur : {e}", fg="#DC2626")
        else:
            result_label.config(text="Entrez des valeurs correctes", fg="#DC2626")

    # === Widgets ===
    label1 = Label(fenetre_polynome2, text="RESOLUTION DES POLYNOMES DE DEGRE 2",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label1.pack(pady=10)

    label2 = Label(fenetre_polynome2, text="Entrez la valeur de a",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome2, height=1, width=40, font=("Century Gothic", 14))
    entre1.pack()

    label3 = Label(fenetre_polynome2, text="Entrez la valeur de b",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome2, height=1, width=40, font=("Century Gothic", 14))
    entre2.pack()

    label4 = Label(fenetre_polynome2, text="Entrez la valeur de c",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label4.pack(pady=10)

    entre3 = Text(fenetre_polynome2, height=1, width=40, font=("Century Gothic", 14))
    entre3.pack()

    result_label = Label(fenetre_polynome2, text="Résultat :", font=("Century Gothic", 14),
                         bg="#F0F4F8", fg="#1E40AF")
    result_label.pack(pady=10)

    # Boutons
    button = ttk.Button(fenetre_polynome2, style="Custom.TButton", text="Calculez", command=recherche_resultat)
    button.pack(pady=20)

    button2 = ttk.Button(fenetre_polynome2, style="Custom.TButton", text="Voir le Graphe", command=lancer_graphe2)
    button2.pack(pady=20)

    # Conseils
    frame_conseils = Frame(fenetre_polynome2, bg="#F0F4F8")
    frame_conseils.pack(pady=15)

    Label(frame_conseils, text="💡 Conseils pour les polynômes degré 2 :",
          font=("Century Gothic", 11, "bold"), bg="#F0F4F8", fg="#1E40AF").pack(pady=(0,8))

    conseils = [
        "• Équation de la forme ax² + bx + c = 0",
        "• Solution unique : x = -b/a (si a ≠ 0)",
        "• a = 0 et b ≠ 0 : aucune solution",
        "• a = 0 et b = 0 : infinité de solutions",
        "• La droite coupe l'axe des x en un seul point",
        "• Exemple simple : 2, -6 donne la racine x = 3"
    ]

    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 9),
              bg="#F0F4F8", fg="#1E40AF", anchor="w", justify="left").pack(fill="x", padx=15, pady=1)

    Label(fenetre_polynome2, text="", bg="#F0F4F8", height=1).pack()

    # Effacer les champs
    def effacer_champs():
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")
        entre3.delete("1.0", "end")
        result_label.config(text="Résultat :", fg="#1E40AF")

    button_effacer = ttk.Button(fenetre_polynome2, style="Custom.TButton", text="Effacer", command=effacer_champs)
    button_effacer.pack(pady=10)

    # Quitter
    button_quitter = ttk.Button(fenetre_polynome2, style="Quit.TButton", text="Quitter", command=fenetre_polynome2.destroy)
    button_quitter.pack(pady=10)


# ------------------ Polynôme de degré 3 ------------------
def lancer_polynome3():
    fenetre_polynome3 = Toplevel()
    fenetre_polynome3.configure(bg="#F0F4F8")  # Même fond que main.py
    fenetre_polynome3.title("Polynome dégré 3")
    fenetre_polynome3.geometry("500x1000")

    def lancer_graphe3():
        # Récupération et conversion des valeurs
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        nombre3 = entre3.get("1.0", "end").strip()
        nombre4 = entre4.get("1.0", "end").strip()
        
        if nombre1 and nombre2 and nombre3 and nombre4:
            try:
                # Conversion en float
                a = float(nombre1)
                b = float(nombre2)
                c = float(nombre3)
                d = float(nombre4)

                voir_graphe3(a, b, c, d)  # Maintenant on passe des nombres !
            except ValueError:
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg="#DC2626")
            except Exception as e:
                result_label.config(text=f"Erreur graphique : {e}", fg="#DC2626")
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg="#DC2626")

    def recherche_resultat():
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        nombre3 = entre3.get("1.0", "end").strip()
        nombre4 = entre4.get("1.0", "end").strip()

        if nombre1 and nombre2 and nombre3 and nombre4:
            try:
                # Conversion en float pour cohérence
                a = float(nombre1)
                b = float(nombre2)
                c = float(nombre3)
                d = float(nombre4)

                # Calcul du polynôme de degré 3
                resultat = polynome3(a, b, c, d)

                # === SAUVEGARDE DU CALCUL ===
                entree_data = {
                    "a": a,
                    "b": b,
                    "c": c,
                    "d": d
                }
                historique_manager.ajouter_calcul(
                    module="Polynômes",
                    operation="Équation degré 3",
                    entree=entree_data,
                    resultat=resultat
                )
                # ============================

                # Affichage du résultat
                if "✅" in resultat:
                    result_label.config(text=f"Résultat : {resultat}", fg="#1E40AF")
                else:
                    result_label.config(text=f"Résultat : {resultat}", fg="#DC2626")

            except ValueError:
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg="#DC2626")
            except Exception as e:
                result_label.config(text=f"Erreur : {e}", fg="#DC2626")
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg="#DC2626")

    # Titre principal
    label1 = Label(fenetre_polynome3, text="RESOLUTION DES POLYNOMES DE DEGRE 3",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14), justify="center")
    label1.pack(pady=10)

    # Champ pour a
    label2 = Label(fenetre_polynome3, text="Entrez la valeur de a (coefficient x³)",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 12), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12))
    entre1.pack()

    # Champ pour b
    label3 = Label(fenetre_polynome3, text="Entrez la valeur de b (coefficient x²)",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 12), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12))
    entre2.pack()

    # Champ pour c
    label4 = Label(fenetre_polynome3, text="Entrez la valeur de c (coefficient x)",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 12), justify="center")
    label4.pack(pady=10)

    entre3 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12))
    entre3.pack()

    # Champ pour d
    label5 = Label(fenetre_polynome3, text="Entrez la valeur de d (constante)",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 12), justify="center")
    label5.pack(pady=10)

    entre4 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12))
    entre4.pack()

    # Label résultat
    result_label = Label(fenetre_polynome3, text="Résultat : ", 
                         font=("Century Gothic", 12), bg="#F0F4F8", fg="#1E40AF")
    result_label.pack(pady=10)

    # Bouton calcul
    button = ttk.Button(fenetre_polynome3, style="Custom.TButton", text="Calculez", command=recherche_resultat)
    button.pack(pady=20)

    # Bouton graphique
    button2 = ttk.Button(fenetre_polynome3, style="Custom.TButton", text="Voir le Graphique", command=lancer_graphe3)
    button2.pack(pady=20)

    # Ajout d'explications
    # Conseils d'utilisation pour polynôme degré 3 
    frame_conseils = Frame(fenetre_polynome3, bg="#F0F4F8")
    frame_conseils.pack(pady=15)

    Label(frame_conseils, text="💡 Conseils pour les polynômes degré 3 :",
        font=("Century Gothic", 11, "bold"), bg="#F0F4F8", fg="#1E40AF").pack(pady=(0,8))

    conseils = [
        "• Ici nous utilisons la méthodes de Cardan",
        "• Toujours 1 racine réelle minimum, maximum 3 racines réelles",
        "• a > 0 : croissante à l'infini • a < 0 : décroissante à l'infini",
        "• Point d'inflexion à x = -b/(3a) (changement de concavité)",
        "• Racine double quand la courbe est tangente à l'axe des x",
        "• Exemple simple : 1, -6, 11, -6 donne les racines 1, 2, 3"
    ]

    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 9),
            bg="#F0F4F8", fg="#1E40AF", anchor="w", justify="left").pack(fill="x", padx=15, pady=1)

    # Espaceur final
    Label(fenetre_polynome3, text="", bg="#F0F4F8", height=1).pack()

    # Bouton pour effacer les champs
    def effacer_champs():
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")
        entre3.delete("1.0", "end")
        entre4.delete("1.0", "end")
        result_label.config(text="Résultat : ", fg="#1E40AF")

    button_effacer = ttk.Button(fenetre_polynome3, style="Custom.TButton", 
                               text="Effacer", command=effacer_champs)
    button_effacer.pack(pady=10)

    # Bouton Quitter
    button_quitter = ttk.Button(fenetre_polynome3, style="Quit.TButton", text="Quitter", 
                               command=fenetre_polynome3.destroy)
    button_quitter.pack(pady=10)

# ------------------ Menu principal ------------------
def lancer_polynome(parent = None):
    fenetre_polynome = Toplevel(parent)
    fenetre_polynome.configure(bg="#F0F4F8")  # Même fond que main.py
    fenetre_polynome.title("Polynome")
    fenetre_polynome.geometry("500x700")

    label1 = Label(fenetre_polynome, text="Choisi le polynome approprié!",
                   fg="#1E40AF", bg="#F0F4F8", font=("Century Gothic", 14, "bold"), justify="center")
    label1.pack(pady=10)

    button1 = ttk.Button(fenetre_polynome,
                         text="Polynome de dégré 1  (ax+b=0)",
                         style="Custom.TButton",
                         command=lancer_polynome1)

    button2 = ttk.Button(fenetre_polynome,
                         text="Polynome de dégré 2(ax²+bx+c=0)",
                         style="Custom.TButton",
                         command=lancer_polynome2)
    
    button3 = ttk.Button(fenetre_polynome,
                         text="Quitter",
                         style="Quit.TButton",
                         compound=LEFT,
                         command=fenetre_polynome.destroy)
    
    button4= ttk.Button(fenetre_polynome,
                         text="Polynome de dégré 3(ax^3 + bx² + cx +d =0)",
                         style="Custom.TButton",
                         command=lancer_polynome3)

    button1.pack(pady=20, fill=X)
    button2.pack(pady=20, fill=X)
    button4.pack(pady=20, fill=X)
    button3.pack(pady=20, fill=X)