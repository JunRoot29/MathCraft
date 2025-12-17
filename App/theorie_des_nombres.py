"""Interface pour Théorie des nombres - Module 2"""
"""
theorie_des_nombres.py - Interface graphique pour l'exploration de concepts Math accéssibles
Auteur: Junior Kossivi
Description: Interface Tkinter pour les méthodes de théories des nombres (Nombres Parfait, nombres premier, pgcd, ppcmn...)
"""

from tkinter import *
from tkinter import ttk
from .modules import nbr_distinct, nbr_parfait, nb_premier, catalan, pgcdrec, ppcm
from .historique_manager import historique_manager

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

# Définition du style global pour les boutons arrondis
def configurer_style():
    style = ttk.Style()
    style.theme_use("clam")  # ✅ Ajout du thème clam
    
    # Style bouton principal
    style.configure("Custom.TButton",
                    foreground=PALETTE["fond_secondaire"],
                    background=PALETTE["primaire"],
                    font=("Century Gothic", 12, "bold"),
                    padding=15,
                    relief="flat",
                    focuscolor="none")
    
    # Style spécial pour le bouton Quitter
    style.configure("Quit.TButton",
                    foreground=PALETTE["fond_secondaire"],
                    background=PALETTE["erreur"],
                    font=("Century Gothic", 12, "bold"),
                    padding=12,
                    relief="flat",
                    focuscolor="none")
    
    # Effets de survol
    style.map("Custom.TButton",
             background=[('active', PALETTE["secondaire"]),
                        ('pressed', '#1E3A8A')],
             foreground=[('active', PALETTE["fond_secondaire"])])
    
    style.map("Quit.TButton",
             background=[('active', '#B91C1C'),
                        ('pressed', '#991B1B')],
             foreground=[('active', PALETTE["fond_secondaire"])])
    
    return style


# Helper pour savoir si on doit créer une Toplevel ou utiliser un Frame parent
def _is_toplevel_parent(parent):
    import tkinter as tk
    return parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))

# Fonction pour ajouter les conseils dans chaque fenêtre
def ajouter_conseils(fenetre, conseils):
    frame_conseils = Frame(fenetre, bg=PALETTE["fond_principal"])
    frame_conseils.pack(pady=15, fill=X, padx=20)
    
    Label(frame_conseils, text="💡 Informations :",
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0,8))
    
    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 9),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w", justify="left").pack(fill="x", padx=15, pady=1)

# Fonction pour lancer la fenêtre "Nombre parfait"
def lancer_nombre_parfait(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        nbr = Toplevel(parent)
        nbr.title("Nombre Parfait")
        nbr.configure(bg=PALETTE["fond_principal"])
        nbr.geometry("600x550")
        nbr.resizable(False, False)
    else:
        nbr = parent
        for child in list(nbr.winfo_children()):
            child.destroy()
        try:
            nbr.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    label = Label(nbr, text="VERIFICATION NOMBRE PARFAIT", font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre.pack(pady=10)

    def test_parfait():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nbr_parfait(valeur)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"nombre": valeur}
            historique_manager.ajouter_calcul(
                module="Théorie des Nombres",
                operation="Test nombre parfait",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label2.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
        except:
            label2.config(text="Réessayer : Opération Impossible", fg=PALETTE["erreur"])

    def remise_a_blanc():
        label2.configure(text="Résultat : ", fg=PALETTE["texte_fonce"])
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Custom.TButton", text="Tester", command=test_parfait)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Custom.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

    # Conseils pour les nombres parfaits
    conseils_parfaits = [
        "• Un nombre parfait est égal à la somme de ses diviseurs propres",
        "• Exemples : 6 = 1+2+3, 28 = 1+2+4+7+14",
        "• Les nombres parfaits connus sont tous pairs",
        "• Très rares : seulement 51 connus à ce jour",
        "• Testez avec : 6, 28, 496, 8128"
    ]
    ajouter_conseils(nbr, conseils_parfaits)

# Fonction pour lancer la fenêtre "Nombre distinct"
def lancer_nombre_distinct(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        nbr = Toplevel(parent)
        nbr.title("Nombre distinct")
        nbr.configure(bg=PALETTE["fond_principal"])
        nbr.geometry("600x550")
        nbr.resizable(False, False)
    else:
        nbr = parent
        for child in list(nbr.winfo_children()):
            child.destroy()
        try:
            nbr.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass
    
    label = Label(nbr, text="VERIFICATION NOMBRE DISTINCT", font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre.pack(pady=10)

    def test_distinct():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nbr_distinct(valeur)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"nombre": valeur}
            historique_manager.ajouter_calcul(
                module="Théorie des Nombres",
                operation="Test nombre distinct",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label2.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
        except:
            label2.config(text="Réessayer : Opération Impossible", fg=PALETTE["erreur"])

    def remise_a_blanc():
        label2.configure(text="Résultat : ", fg=PALETTE["texte_fonce"])
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Custom.TButton", text="Tester", command=test_distinct)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Custom.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

    # Conseils pour les nombres distincts
    conseils_distincts = [
        "• Un nombre distinct a tous ses chiffres différents",
        "• Exemples : 1234 (distinct), 1123 (non distinct)",
        "• Les nombres à un chiffre sont toujours distincts",
        "• Utile pour les codes PIN, mots de passe, etc.",
        "• Testez avec : 123, 4567, 1029"
    ]
    ajouter_conseils(nbr, conseils_distincts)

# Fonction pour lancer la fenêtre "Nombre premier"
def lancer_nombre_premier(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        nbr = Toplevel(parent)
        nbr.title("Nombre Premier")
        nbr.configure(bg=PALETTE["fond_principal"])
        nbr.geometry("600x650")
        nbr.resizable(False, False)
    else:
        nbr = parent
        for child in list(nbr.winfo_children()):
            child.destroy()
        try:
            nbr.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass
    
    label = Label(nbr, text="TEST DE PRIMALITÉ", font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre.pack(pady=10)

    def test_premier():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nb_premier(valeur)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"nombre": valeur}
            historique_manager.ajouter_calcul(
                module="Théorie des Nombres",
                operation="Test nombre premier",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label2.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
        except:
            label2.config(text="Réessayer : Opération Impossible", fg=PALETTE["erreur"])

    def remise_a_blanc():
        label2.configure(text="Résultat : ", fg=PALETTE["texte_fonce"])
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Custom.TButton", text="Tester", command=test_premier)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Custom.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

    # Conseils pour les nombres premiers
    conseils_premiers = [
        "• Un nombre premier n'a que 2 diviseurs : 1 et lui-même",
        "• Exemples : 2, 3, 5, 7, 11, 13, 17...",
        "• 1 n'est pas premier (un seul diviseur)",
        "• 2 est le seul nombre premier pair",
        "• Testez avec : 17, 29, 97, 101"
    ]
    ajouter_conseils(nbr, conseils_premiers)

# Fonction pour lancer le PGCD
def lancer_pgcd(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        nbr = Toplevel(parent)
        nbr.title("PGCD")
        nbr.configure(bg=PALETTE["fond_principal"])
        nbr.geometry("600x600")
        nbr.resizable(False, False)
    else:
        nbr = parent
        for child in list(nbr.winfo_children()):
            child.destroy()
        try:
            nbr.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    label = Label(nbr, text="CALCUL PGCD", font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le premier nombre", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label1.pack(pady=10)
    
    entre1 = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre1.pack(pady=10)

    label2 = Label(nbr, text="Entrez le deuxième nombre", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=10)
    
    entre2 = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre2.pack(pady=10)

    def test_pgcd():
        try:
            valeur1 = int(entre1.get("1.0", "end").strip())
            valeur2 = int(entre2.get("1.0", "end").strip())  # ✅ Correction : entre2 au lieu de entre1
            resultat = pgcdrec(valeur1, valeur2)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"nombre1": valeur1, "nombre2": valeur2}
            historique_manager.ajouter_calcul(
                module="Théorie des Nombres",
                operation="Test pgcd",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label_resultat.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
        except:
            label_resultat.config(text="Réessayer : Opération Impossible", fg=PALETTE["erreur"])

    def remise_a_blanc():
        label_resultat.configure(text="Résultat : ", fg=PALETTE["texte_fonce"])
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Custom.TButton", text="Calculer", command=test_pgcd)
    bouton1.pack(pady=10) 
    
    label_resultat = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label_resultat.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Custom.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

    # Conseils pour le PGCD
    conseils_pgcd = [
        "• PGCD = Plus Grand Commun Diviseur",
        "• Algorithme d'Euclide (méthode récursive)",
        "• Si PGCD(a,b) = 1, les nombres sont premiers entre eux",
        "• Propriété : PGCD(a,b) × PPCM(a,b) = a × b",
        "• Testez avec : (56, 42) → 14, (17, 13) → 1"
    ]
    ajouter_conseils(nbr, conseils_pgcd)

# Fonction pour lancer le PPCM
def lancer_ppcm(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        nbr = Toplevel(parent)
        nbr.title("PPCM")
        nbr.configure(bg=PALETTE["fond_principal"])
        nbr.geometry("600x650")
        nbr.resizable(False, False)
    else:
        nbr = parent
        for child in list(nbr.winfo_children()):
            child.destroy()
        try:
            nbr.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    label = Label(nbr, text="CALCUL PPCM", font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le premier nombre", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label1.pack(pady=10)
    
    entre1 = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre1.pack(pady=10)

    label2 = Label(nbr, text="Entrez le deuxième nombre", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=10)
    
    entre2 = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre2.pack(pady=10)

    def test_ppcm():
        try:
            valeur1 = int(entre1.get("1.0", "end").strip())
            valeur2 = int(entre2.get("1.0", "end").strip())  # ✅ Correction : entre2 au lieu de entre1
            resultat = ppcm(valeur1, valeur2)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"nombre1": valeur1, "nombre2": valeur2}
            historique_manager.ajouter_calcul(
                module="Théorie des Nombres",
                operation="Test ppcm",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label_resultat.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
        except:
            label_resultat.config(text="Réessayer : Opération Impossible", fg=PALETTE["erreur"])

    def remise_a_blanc():
        label_resultat.configure(text="Résultat : ", fg=PALETTE["texte_fonce"])
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Custom.TButton", text="Calculer", command=test_ppcm)
    bouton1.pack(pady=10) 
    
    label_resultat = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label_resultat.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Custom.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

    # Conseils pour le PPCM
    conseils_ppcm = [
        "• PPCM = Plus Petit Commun Multiple",
        "• Utile pour additionner des fractions",
        "• Relation : PGCD(a,b) × PPCM(a,b) = a × b",
        "• Le PPCM est toujours ≥ au plus grand nombre",
        "• Testez avec : (6, 8) → 24, (12, 18) → 36"
    ]
    ajouter_conseils(nbr, conseils_ppcm)

# Fonction pour lancer la fenêtre "Nombre Catalan"
def lancer_nombre_catalan(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        nbr = Toplevel(parent)
        nbr.title("Nombres Catalans")
        nbr.configure(bg=PALETTE["fond_principal"])
        nbr.geometry("600x550")
        nbr.resizable(False, False)
    else:
        nbr = parent
        for child in list(nbr.winfo_children()):
            child.destroy()
        try:
            nbr.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    label = Label(nbr, text="CALCUL DU NOMBRE CATALAN", font=("Century Gothic", 16, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12), relief="solid", borderwidth=1)
    entre.pack(pady=10)

    def test_catalan():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = catalan(valeur)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"nombre": valeur}
            historique_manager.ajouter_calcul(
                module="Théorie des Nombres",
                operation="Test Nombre Catalan",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label2.config(text=f"Résultat : {resultat}", fg=PALETTE["primaire"])
        except:
            label2.config(text="Réessayer : Opération Impossible", fg=PALETTE["erreur"])

    def remise_a_blanc():
        label2.configure(text="Résultat : ", fg=PALETTE["texte_fonce"])
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Custom.TButton", text="Calculer", command=test_catalan)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Custom.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

    # Conseils pour les nombres de Catalan
    conseils_catalan = [
        "• Suite de nombres apparaissant dans de nombreux problèmes",
        "• Applications : arbres binaires, parenthésages, triangulations",
        "• Formule : Cₙ = (2n)! / (n!(n+1)!)",
        "• Premiers termes : 1, 1, 2, 5, 14, 42, 132...",
        "• Testez avec : n=3 → 5, n=4 → 14, n=5 → 42"
    ]
    ajouter_conseils(nbr, conseils_catalan)

# Fonction principale pour lancer le module "Théorie des nombres"
def lancer_theorie(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        th = Toplevel(parent)
        th.title("Théorie des nombres")
        th.configure(bg=PALETTE["fond_principal"])
        th.geometry("500x800")
        th.resizable(False, False)

        # Centrer la fenêtre
        th.transient(parent)
        th.grab_set()
    else:
        th = parent
        for child in list(th.winfo_children()):
            child.destroy()
        try:
            th.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    # Présentation du module
    frame_presentation = Frame(th, bg=PALETTE["fond_principal"])
    frame_presentation.pack(pady=20, padx=20, fill=X)
    
    Label(frame_presentation, text="🧮 THÉORIE DES NOMBRES", 
          font=("Century Gothic", 18, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=10)
    
    Label(frame_presentation, text="Explorez les propriétés fascinantes des nombres", 
          font=("Century Gothic", 12), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"]).pack(pady=5)

    # Conseils généraux
    frame_info = Frame(th, bg=PALETTE["fond_principal"])
    frame_info.pack(pady=10, padx=20, fill=X)
    
    Label(frame_info, text="📚 Fonctions disponibles :",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(anchor="w")
    
    fonctions_info = [
        "• Nombre parfait : somme des diviseurs = nombre",
        "• Nombre distinct : tous chiffres différents", 
        "• Nombre premier : divisible seulement par 1 et lui-même",
        "• PGCD : Plus Grand Commun Diviseur",
        "• PPCM : Plus Petit Commun Multiple",
        "• Nombres de Catalan : suite combinatoire importante"
    ]
    
    for info in fonctions_info:
        Label(frame_info, text=info, font=("Century Gothic", 9),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w").pack(fill="x", padx=10, pady=1)

    # Cadre pour les boutons
    frame_boutons = Frame(th, bg=PALETTE["fond_principal"])
    frame_boutons.pack(pady=20, padx=20, fill=BOTH, expand=True)

    # Boutons pour chaque test
    boutons_config = [
        ("🔢 Nombre parfait", lancer_nombre_parfait),
        ("🔤 Nombre distinct", lancer_nombre_distinct),
        ("⭐ Nombre premier", lancer_nombre_premier),
        ("📐 PGCD", lancer_pgcd),
        ("📊 PPCM", lancer_ppcm),
        ("🎯 Nombres Catalans", lancer_nombre_catalan)
    ]

    style = configurer_style()
    for texte, commande in boutons_config:
        bouton = ttk.Button(frame_boutons, text=texte, style="Custom.TButton", 
                           command=lambda cmd=commande: cmd(th))
        bouton.pack(pady=8, fill=X)

    # Bouton retour
    ttk.Button(th, text="🚪 Retour au Menu Principal", style="Quit.TButton",
              command=th.destroy).pack(pady=20)