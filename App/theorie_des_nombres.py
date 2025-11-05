from tkinter import *
from tkinter import ttk
from .modules import nbr_distinct
from .modules import nbr_parfait
from .modules import nb_premier
from .modules import catalan
from .modules import pgcdrec
from .modules import ppcm

# Définition du style global pour les boutons arrondis
def configurer_style():
    style = ttk.Style()
    style.configure("Rounded.TButton",
                    foreground="#3C3C3C",  
                    background="#C7C3BB",  
                    font=("Century Gothic", 14),  
                    padding=(20, 10),
                    relief="flat",
                    width=60)
    return style

# Fonction pour ajouter les conseils dans chaque fenêtre
def ajouter_conseils(fenetre, conseils):
    frame_conseils = Frame(fenetre, bg="#F5F0E6")
    frame_conseils.pack(pady=15, fill=X, padx=20)
    
    Label(frame_conseils, text="💡 Informations :",
          font=("Century Gothic", 11, "bold"), bg="#F5F0E6").pack(pady=(0,8))
    
    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 9),
              bg="#F5F0E6", fg="#555555", anchor="w", justify="left").pack(fill="x", padx=15, pady=1)

# Fonction pour lancer la fenêtre "Nombre parfait"
def lancer_nombre_parfait():
    nbr = Toplevel() 
    nbr.title("Nombre Parfait") 
    nbr.configure(bg="#F5F0E6")
    nbr.geometry("600x550")

    label = Label(nbr, text="VERIFICATION NOMBRE PARFAIT", font=("Century Gothic", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre.pack(pady=10)

    def test_parfait():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nbr_parfait(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Tester", command=test_parfait)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
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
def lancer_nombre_distinct():
    nbr = Toplevel() 
    nbr.title("Nombre distinct") 
    nbr.configure(bg="#F5F0E6")
    nbr.geometry("600x550")
    
    label = Label(nbr, text="VERIFICATION NOMBRE DISTINCT", font=("Century Gothic", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre.pack(pady=10)

    def test_distinct():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nbr_distinct(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Tester", command=test_distinct)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
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
def lancer_nombre_premier():
    nbr = Toplevel() 
    nbr.title("Nombre Premier") 
    nbr.configure(bg="#F5F0E6")
    nbr.geometry("600x700")
    
    label = Label(nbr, text="TEST DE PRIMALITÉ", font=("Century Gothic", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre.pack(pady=10)

    def test_premier():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nb_premier(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Tester", command=test_premier)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
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
def lancer_pgcd():
    nbr = Toplevel() 
    nbr.title("PGCD") 
    nbr.configure(bg="#F5F0E6")
    nbr.geometry("600x600")

    label = Label(nbr, text="CALCUL PGCD", font=("Century Gothic", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le premier nombre", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)
    
    entre1 = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre1.pack(pady=10)

    label2 = Label(nbr, text="Entrez le deuxième nombre", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)
    
    entre2 = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre2.pack(pady=10)

    def test_pgcd():
        try:
            valeur1 = int(entre1.get("1.0", "end").strip())
            valeur2 = int(entre2.get("1.0", "end").strip())
            resultat = pgcdrec(valeur1, valeur2)
            label_resultat.config(text=f"Résultat : {resultat}")
        except:
            label_resultat.config(text="Réessayer : Opération Impossible")

    def remise_a_blanc():
        label_resultat.configure(text="Résultat : ")
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Calculer", command=test_pgcd)
    bouton1.pack(pady=10) 
    
    label_resultat = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg="#F5F0E6")
    label_resultat.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
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
def lancer_ppcm():
    nbr = Toplevel() 
    nbr.title("PPCM") 
    nbr.configure(bg="#F5F0E6")
    nbr.geometry("600x700")

    label = Label(nbr, text="CALCUL PPCM", font=("Century Gothic", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le premier nombre", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)
    
    entre1 = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre1.pack(pady=10)

    label2 = Label(nbr, text="Entrez le deuxième nombre", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)
    
    entre2 = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre2.pack(pady=10)

    def test_ppcm():
        try:
            valeur1 = int(entre1.get("1.0", "end").strip())
            valeur2 = int(entre2.get("1.0", "end").strip())
            resultat = ppcm(valeur1, valeur2)
            label_resultat.config(text=f"Résultat : {resultat}")
        except:
            label_resultat.config(text="Réessayer : Opération Impossible")

    def remise_a_blanc():
        label_resultat.configure(text="Résultat : ")
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Calculer", command=test_ppcm)
    bouton1.pack(pady=10) 
    
    label_resultat = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg="#F5F0E6")
    label_resultat.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
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
def lancer_nombre_catalan():
    nbr = Toplevel() 
    nbr.title("Nombres Catalans") 
    nbr.configure(bg="#F5F0E6")
    nbr.geometry("600x550")

    label = Label(nbr, text="CALCUL DU NOMBRE CATALAN", font=("Century Gothic", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)
    
    entre = Text(nbr, height=2, width=40, font=("Century Gothic", 12))
    entre.pack(pady=10)

    def test_catalan():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = catalan(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    style = configurer_style()
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Calculer", command=test_catalan)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
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
    th = Toplevel(parent)
    th.title("Théorie des nombres")
    th.configure(bg="#F5F0E6")
    th.geometry("500x900")

    # Présentation du module
    frame_presentation = Frame(th, bg="#F5F0E6")
    frame_presentation.pack(pady=20, padx=20, fill=X)
    
    Label(frame_presentation, text="🧮 THÉORIE DES NOMBRES", 
          font=("Century Gothic", 18, "bold"), bg="#F5F0E6").pack(pady=10)
    
    Label(frame_presentation, text="Explorez les propriétés fascinantes des nombres", 
          font=("Century Gothic", 12), bg="#F5F0E6", fg="#666666").pack(pady=5)

    # Conseils généraux
    frame_info = Frame(th, bg="#F5F0E6")
    frame_info.pack(pady=10, padx=20, fill=X)
    
    Label(frame_info, text="📚 Fonctions disponibles :",
          font=("Century Gothic", 12, "bold"), bg="#F5F0E6").pack(anchor="w")
    
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
              bg="#F5F0E6", fg="#555555", anchor="w").pack(fill="x", padx=10, pady=1)

    # Cadre pour les boutons
    frame_boutons = Frame(th, bg="#F5F0E6")
    frame_boutons.pack(pady=20, padx=20, fill=BOTH, expand=True)

    # Boutons pour chaque test
    boutons_config = [
        ("Nombre parfait", lancer_nombre_parfait),
        ("Nombre distinct", lancer_nombre_distinct),
        ("Nombre premier", lancer_nombre_premier),
        ("PGCD", lancer_pgcd),
        ("PPCM", lancer_ppcm),
        ("Nombres Catalans", lancer_nombre_catalan)
    ]

    style = configurer_style()
    for texte, commande in boutons_config:
        bouton = ttk.Button(frame_boutons, text=texte, style="Rounded.TButton", command=commande)
        bouton.pack(pady=8, fill=X, padx=50)