
"""Interface pour Polynome - Module 5"""
"""
polynome.py - Interface graphique pour la résolution d'équation du 1er, 2nd et 3ème dégrés avec affichage des calculs et graphiques
Auteur: Junior Kossivi
Description: Interface Tkinter pour les méthodes d'équation avec affichage direct des calculs et graphiques
"""
# ruff: noqa: E402,F405
import tkinter as tk
from tkinter import ttk
from .modules import polynome1, polynome2, polynome3, voir_graphe1, voir_graphe2, voir_graphe3
try:
    from .historique_manager import historique_manager
except ImportError:
    # Solution de secours
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from App.historique_manager import historique_manager
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

# Palette unifiée (même que main.py)
PALETTE = {
    "fond_principal": "#F0F4F8",
    "fond_secondaire": "#FFFFFF",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6",
    "texte_fonce": "#1E293B",
    "texte_clair": "#64748B",
    "succes": "#10B981",
    "erreur": "#DC2626",
    "bordure": "#E2E8F0",
}


def enregistrer_calcul(module, operation, entree, resultat):
    """Fonction wrapper pour l'historique"""
    return historique_manager.ajouter_calcul(module, operation, entree, resultat)


def configurer_style():
    """Compat wrapper: délègue à App.style_manager.ensure_style()."""
    return ensure_style()




# Helper pour savoir si on doit créer une Toplevel ou utiliser un Frame parent
def _is_toplevel_parent(parent):
    import tkinter as tk
    return parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))

def ajouter_conseils(fenetre, conseils, titre="💡 Conseils :"):
    """Fonction pour ajouter des conseils avec style unifié"""
    frame_conseils = Frame(fenetre, bg=PALETTE["fond_principal"])
    frame_conseils.pack(pady=15, fill=X, padx=20)
    
    Label(frame_conseils, text=titre,
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0,8))
    
    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 9),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w", justify="left").pack(fill="x", padx=15, pady=1)

# ------------------ Polynôme de degré 1 ------------------
def lancer_polynome1(parent=None):
    # Assurer que le style est configuré si une racine existe
    ensure_style()
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre_polynome1 = Toplevel(parent)
        fenetre_polynome1.configure(bg=PALETTE["fond_principal"])
        fenetre_polynome1.title("Polynôme degré 1")
        fenetre_polynome1.geometry("500x650")
        fenetre_polynome1.resizable(False, False)
    else:
        fenetre_polynome1 = parent
        for child in list(fenetre_polynome1.winfo_children()):
            child.destroy()
        try:
            fenetre_polynome1.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

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
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg=PALETTE["erreur"])
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg=PALETTE["erreur"])

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
                    result_label.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
                else:
                    result_label.config(text=f"Résultat : {resultat}", fg=PALETTE["erreur"])
            except Exception as e:
                result_label.config(text=f"Erreur : {e}", fg=PALETTE["erreur"])
        else:
            result_label.config(text="Entrez des valeurs correctes", fg=PALETTE["erreur"])

    def effacer_champs():
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")
        result_label.config(text="Résultat :", fg=PALETTE["texte_fonce"])

    # Interface
    label1 = Label(fenetre_polynome1, text="RÉSOLUTION DES POLYNÔMES DE DEGRÉ 1",
                   fg=PALETTE["primaire"], bg=PALETTE["fond_principal"], font=("Century Gothic", 16, "bold"), justify="center")
    label1.pack(pady=20)

    label2 = Label(fenetre_polynome1, text="Entrez la valeur de a",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome1, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre1.pack()

    label3 = Label(fenetre_polynome1, text="Entrez la valeur de b",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome1, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre2.pack()

    result_label = Label(fenetre_polynome1, text="Résultat :", font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    result_label.pack(pady=10)

    button = ttk.Button(fenetre_polynome1, style="Custom.TButton", text="Calculer", command=recherche_resultat)
    button.pack(pady=10)

    button2 = ttk.Button(fenetre_polynome1, style="Custom.TButton", text="📈 Voir le Graphe", command=lancer_graphe1)
    button2.pack(pady=10)

    button_effacer = ttk.Button(fenetre_polynome1, style="Custom.TButton", text="🧹 Effacer", command=effacer_champs)
    button_effacer.pack(pady=10)

    # Conseils
    conseils_degre1 = [
        "• Équation de la forme ax + b = 0",
        "• Solution unique : x = -b/a (si a ≠ 0)",
        "• a = 0 et b ≠ 0 : aucune solution",
        "• a = 0 et b = 0 : infinité de solutions",
        "• La droite coupe l'axe des x en un seul point",
        "• Exemple simple : 2, -6 donne la racine x = 3"
    ]
    ajouter_conseils(fenetre_polynome1, conseils_degre1, "💡 Conseils pour les polynômes degré 1 :")

    # Bouton Quitter
    def _quit_local_1():
        if is_toplevel:
            fenetre_polynome1.destroy()
        else:
            for w in list(fenetre_polynome1.winfo_children()):
                w.destroy()
    button_quitter = ttk.Button(fenetre_polynome1, style="Quit.TButton", text="🚪 Quitter", 
                               command=_quit_local_1)
    button_quitter.pack(pady=10)

# ------------------ Polynôme de degré 2 ------------------
def lancer_polynome2(parent=None):    # Assurer que le style est configuré si une racine existe
    ensure_style()
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre_polynome2 = Toplevel(parent)
        fenetre_polynome2.configure(bg=PALETTE["fond_principal"])
        fenetre_polynome2.title("Polynôme degré 2")
        fenetre_polynome2.geometry("500x900")
        fenetre_polynome2.resizable(False, False)
    else:
        fenetre_polynome2 = parent
        for child in list(fenetre_polynome2.winfo_children()):
            child.destroy()
        try:
            fenetre_polynome2.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

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
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg=PALETTE["erreur"])
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg=PALETTE["erreur"])

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
                    result_label.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
                else:
                    result_label.config(text=f"Résultat : {resultat}", fg=PALETTE["erreur"])
            except Exception as e:
                result_label.config(text=f"Erreur : {e}", fg=PALETTE["erreur"])
        else:
            result_label.config(text="Entrez des valeurs correctes", fg=PALETTE["erreur"])

    def effacer_champs():
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")
        entre3.delete("1.0", "end")
        result_label.config(text="Résultat :", fg=PALETTE["texte_fonce"])

    # === Widgets ===
    label1 = Label(fenetre_polynome2, text="RÉSOLUTION DES POLYNÔMES DE DEGRÉ 2",
                   fg=PALETTE["primaire"], bg=PALETTE["fond_principal"], font=("Century Gothic", 16, "bold"), justify="center")
    label1.pack(pady=20)

    label2 = Label(fenetre_polynome2, text="Entrez la valeur de a",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome2, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre1.pack()

    label3 = Label(fenetre_polynome2, text="Entrez la valeur de b",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome2, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre2.pack()

    label4 = Label(fenetre_polynome2, text="Entrez la valeur de c",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label4.pack(pady=10)

    entre3 = Text(fenetre_polynome2, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre3.pack()

    result_label = Label(fenetre_polynome2, text="Résultat :", font=("Century Gothic", 12),
                         bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    result_label.pack(pady=10)

    # Boutons
    button = ttk.Button(fenetre_polynome2, style="Custom.TButton", text="Calculer", command=recherche_resultat)
    button.pack(pady=10)

    button2 = ttk.Button(fenetre_polynome2, style="Custom.TButton", text="📈 Voir le Graphe", command=lancer_graphe2)
    button2.pack(pady=10)

    button_effacer = ttk.Button(fenetre_polynome2, style="Custom.TButton", text="🧹 Effacer", command=effacer_champs)
    button_effacer.pack(pady=10)

    # Conseils
    conseils_degre2 = [
        "• Équation de la forme ax² + bx + c = 0",
        "• Discriminant Δ = b² - 4ac",
        "• Δ > 0 : 2 racines réelles distinctes",
        "• Δ = 0 : 1 racine réelle double", 
        "• Δ < 0 : 2 racines complexes conjuguées",
        "• Exemple : 1, -3, 2 donne les racines 1 et 2"
    ]
    ajouter_conseils(fenetre_polynome2, conseils_degre2, "💡 Conseils pour les polynômes degré 2 :")

    # Bouton Quitter
    def _quit_local_2():
        if is_toplevel:
            fenetre_polynome2.destroy()
        else:
            for w in list(fenetre_polynome2.winfo_children()):
                w.destroy()
    button_quitter = ttk.Button(fenetre_polynome2, style="Quit.TButton", text="🚪 Quitter", command=_quit_local_2)
    button_quitter.pack(pady=10)

# ------------------ Polynôme de degré 3 ------------------
def lancer_polynome3(parent=None):    # Assurer que le style est configuré si une racine existe
    ensure_style()
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre_polynome3 = Toplevel(parent)
        fenetre_polynome3.configure(bg=PALETTE["fond_principal"])
        fenetre_polynome3.title("Polynôme degré 3")
        fenetre_polynome3.geometry("500x950")
        fenetre_polynome3.resizable(False, False)
    else:
        fenetre_polynome3 = parent
        for child in list(fenetre_polynome3.winfo_children()):
            child.destroy()
        try:
            fenetre_polynome3.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

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
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg=PALETTE["erreur"])
            except Exception as e:
                result_label.config(text=f"Erreur graphique : {e}", fg=PALETTE["erreur"])
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg=PALETTE["erreur"])

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
                    result_label.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
                else:
                    result_label.config(text=f"Résultat : {resultat}", fg=PALETTE["erreur"])

            except ValueError:
                result_label.config(text="Erreur : Veuillez entrer des nombres valides", fg=PALETTE["erreur"])
            except Exception as e:
                result_label.config(text=f"Erreur : {e}", fg=PALETTE["erreur"])
        else:
            result_label.config(text="Veuillez remplir tous les champs", fg=PALETTE["erreur"])

    def effacer_champs():
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")
        entre3.delete("1.0", "end")
        entre4.delete("1.0", "end")
        result_label.config(text="Résultat : ", fg=PALETTE["texte_fonce"])

    # Titre principal
    label1 = Label(fenetre_polynome3, text="RÉSOLUTION DES POLYNÔMES DE DEGRÉ 3",
                   fg=PALETTE["primaire"], bg=PALETTE["fond_principal"], font=("Century Gothic", 16, "bold"), justify="center")
    label1.pack(pady=20)

    # Champ pour a
    label2 = Label(fenetre_polynome3, text="Entrez la valeur de a (coefficient x³)",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre1.pack()

    # Champ pour b
    label3 = Label(fenetre_polynome3, text="Entrez la valeur de b (coefficient x²)",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre2.pack()

    # Champ pour c
    label4 = Label(fenetre_polynome3, text="Entrez la valeur de c (coefficient x)",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label4.pack(pady=10)

    entre3 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre3.pack()

    # Champ pour d
    label5 = Label(fenetre_polynome3, text="Entrez la valeur de d (constante)",
                   fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label5.pack(pady=10)

    entre4 = Text(fenetre_polynome3, height=1, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre4.pack()

    # Label résultat
    result_label = Label(fenetre_polynome3, text="Résultat : ", 
                         font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    result_label.pack(pady=10)

    # Bouton calcul
    button = ttk.Button(fenetre_polynome3, style="Custom.TButton", text="Calculer", command=recherche_resultat)
    button.pack(pady=10)

    # Bouton graphique
    button2 = ttk.Button(fenetre_polynome3, style="Custom.TButton", text="📈 Voir le Graphique", command=lancer_graphe3)
    button2.pack(pady=10)

    button_effacer = ttk.Button(fenetre_polynome3, style="Custom.TButton", 
                               text="🧹 Effacer", command=effacer_champs)
    button_effacer.pack(pady=10)

    # Conseils
    conseils_degre3 = [
        "• Ici nous utilisons la méthode de Cardan",
        "• Toujours 1 racine réelle minimum, maximum 3 racines réelles",
        "• a > 0 : croissante à l'infini • a < 0 : décroissante à l'infini",
        "• Point d'inflexion à x = -b/(3a) (changement de concavité)",
        "• Racine double quand la courbe est tangente à l'axe des x",
        "• Exemple simple : 1, -6, 11, -6 donne les racines 1, 2, 3"
    ]
    ajouter_conseils(fenetre_polynome3, conseils_degre3, "💡 Conseils pour les polynômes degré 3 :")

    # Bouton Quitter
    def _quit_local_3():
        if is_toplevel:
            fenetre_polynome3.destroy()
        else:
            for w in list(fenetre_polynome3.winfo_children()):
                w.destroy()
    button_quitter = ttk.Button(fenetre_polynome3, style="Quit.TButton", text="🚪 Quitter", 
                               command=_quit_local_3)
    button_quitter.pack(pady=10)

# ------------------ Menu principal ------------------
def lancer_polynome(parent=None):
    # Assurer que le style est configuré si une racine existe
    ensure_style()
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre_polynome = Toplevel(parent)
        fenetre_polynome.configure(bg=PALETTE["fond_principal"])
        fenetre_polynome.title("Polynômes")
        fenetre_polynome.geometry("500x600")
        fenetre_polynome.resizable(False, False)

        # Centrer la fenêtre
        fenetre_polynome.transient(parent)
        fenetre_polynome.grab_set()
    else:
        fenetre_polynome = parent
        for child in list(fenetre_polynome.winfo_children()):
            child.destroy()
        try:
            fenetre_polynome.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    label1 = Label(fenetre_polynome, text="🧮 MODULE POLYNÔMES",
                   fg=PALETTE["primaire"], bg=PALETTE["fond_principal"], font=("Century Gothic", 18, "bold"), justify="center")
    label1.pack(pady=20)

    label2 = Label(fenetre_polynome, text="Choisissez le type de polynôme à résoudre",
                   fg=PALETTE["texte_clair"], bg=PALETTE["fond_principal"], font=("Century Gothic", 12), justify="center")
    label2.pack(pady=10)

    # Boutons avec icônes
    button1 = ttk.Button(fenetre_polynome,
                         text="🔢 Polynôme de degré 1 (ax + b = 0)",
                         style="Custom.TButton",
                         command=lambda: lancer_polynome1(fenetre_polynome))
    
    button2 = ttk.Button(fenetre_polynome,
                         text="📊 Polynôme de degré 2 (ax² + bx + c = 0)",
                         style="Custom.TButton",
                         command=lambda: lancer_polynome2(fenetre_polynome))
    
    button4 = ttk.Button(fenetre_polynome,
                         text="📈 Polynôme de degré 3 (ax³ + bx² + cx + d = 0)",
                         style="Custom.TButton",
                         command=lambda: lancer_polynome3(fenetre_polynome))

    def _quit_local_main():
        if is_toplevel:
            fenetre_polynome.destroy()
        else:
            for w in list(fenetre_polynome.winfo_children()):
                w.destroy()
    button3 = ttk.Button(fenetre_polynome,
                         text="🚪 Retour au Menu Principal",
                         style="Quit.TButton",
                         command=_quit_local_main)

    button1.pack(pady=15, fill=X, padx=50)
    button2.pack(pady=15, fill=X, padx=50)
    button4.pack(pady=15, fill=X, padx=50)
    button3.pack(pady=20, fill=X, padx=50)

    # Informations
    frame_info = Frame(fenetre_polynome, bg=PALETTE["fond_principal"])
    frame_info.pack(pady=20, padx=20, fill=X)
    
    Label(frame_info, text="📚 Types de polynômes disponibles :",
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(anchor="w")
    
    infos = [
        "• Degré 1 : Équation linéaire (droite)",
        "• Degré 2 : Équation quadratique (parabole)", 
        "• Degré 3 : Équation cubique (courbe en S)"
    ]
    
    for info in infos:
        Label(frame_info, text=info, font=("Century Gothic", 9),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w").pack(fill="x", padx=10, pady=1)