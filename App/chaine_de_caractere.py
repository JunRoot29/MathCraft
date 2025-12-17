"""
chaine_de_caractere.py - Interface pour le Traitement des chaine de caratère
Auteur: Junior Kossivi
Description: Interface Tkinter pour les méthodes de résolution d'opération sur les chaine de caractère
"""
from tkinter import *
from tkinter import ttk
import pyperclip  # Pour copier dans le presse-papier
from .modules import compterVoyelles, compterlettre, compter_occurrences, palindrome_amelioré
from .modules import inverser_chaine, compter_mots, majuscules, minuscules, nettoyer_espaces, est_anagramme, generer_mot_de_passe, encoder_base64, decoder_base64, compter_consonnes, extraire_chiffres, rot13
from .modules import titre

# Palette unifiée
PALETTE = {
    "fond_principal": "#F0F4F8",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6", 
    "erreur": "#DC2626",
    "succes": "#10B981",
    "texte_fonce": "#1E40AF",
    "texte_clair": "#1E40AF"
}

def configurer_style():
    style = ttk.Style()
    style.configure("Custom.TButton",
                    foreground="#FFFFFF",
                    background=PALETTE["secondaire"],
                    font=("Century Gothic", 12),
                    relief="flat",
                    padding=10)
    
    style.configure("Copier.TButton",
                    foreground="#FFFFFF",
                    background="#6B7280",
                    font=("Century Gothic", 10),
                    relief="flat",
                    padding=6)
    
    style.configure("Quit.TButton",
                    foreground="#FFFFFF",
                    background=PALETTE["erreur"],
                    font=("Century Gothic", 12),
                    relief="flat",
                    padding=10)
    
    style.configure("Petit.TButton",
                    foreground="#FFFFFF",
                    background=PALETTE["secondaire"],
                    font=("Century Gothic", 10),
                    relief="flat",
                    padding=6)
    return style

def centrer_fenetre(fenetre):
    """Centre une fenêtre sur l'écran"""
    fenetre.update_idletasks()
    width = fenetre.winfo_width()
    height = fenetre.winfo_height()
    x = (fenetre.winfo_screenwidth() // 2) - (width // 2)
    y = (fenetre.winfo_screenheight() // 2) - (height // 2)
    fenetre.geometry(f'{width}x{height}+{x}+{y}')

def creer_zone_resultat_copiable(parent, hauteur=6):
    """Crée une zone de résultat avec bouton copier"""
    # Frame pour l'affichage du résultat
    result_frame = Frame(parent, bg=PALETTE["fond_principal"])
    
    # Label du résultat
    result_label = Label(result_frame, text="Résultat :", 
                        font=("Century Gothic", 12, "bold"),
                        bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    result_label.pack(anchor="w", pady=(0, 5))

    # Frame pour l'affichage du texte + bouton copier
    display_frame = Frame(result_frame, bg=PALETTE["fond_principal"])
    display_frame.pack(fill=X)

    # Zone de texte pour le résultat (scrollable)
    result_text = Text(display_frame, height=hauteur, width=50, font=("Consolas", 11),
                      wrap=WORD, relief=SUNKEN, borderwidth=2, state=DISABLED,
                      bg="#F8FAFC", fg=PALETTE["texte_fonce"])
    result_text.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))
    
    # Scrollbar pour le résultat
    result_scrollbar = Scrollbar(display_frame, command=result_text.yview)
    result_scrollbar.pack(side=RIGHT, fill=Y)
    result_text.config(yscrollcommand=result_scrollbar.set)

    # Bouton Copier
    copier_frame = Frame(result_frame, bg=PALETTE["fond_principal"])
    copier_frame.pack(fill=X, pady=(10, 0))
    
    copier_button = ttk.Button(copier_frame, text="📋 Copier le résultat", 
                              style="Copier.TButton")
    copier_button.pack(anchor="e")
    copier_button.pack_forget()  # Caché au début

    def afficher_resultat(texte, couleur=PALETTE["primaire"], montrer_copier=True):
        """Affiche le résultat dans la zone de texte"""
        result_text.config(state=NORMAL)
        result_text.delete("1.0", "end")
        result_text.insert("1.0", texte)
        result_text.config(fg=couleur, state=DISABLED)
        
        # Afficher ou cacher le bouton copier
        if montrer_copier and texte and "❌" not in texte:
            copier_button.pack(anchor="e")
        else:
            copier_button.pack_forget()

    def copier_contenu():
        """Copie le contenu dans le presse-papier"""
        result_text.config(state=NORMAL)
        contenu = result_text.get("1.0", "end-1c")
        result_text.config(state=DISABLED)
        
        if contenu:
            try:
                pyperclip.copy(contenu)
                # Feedback visuel
                original_text = copier_button.cget("text")
                copier_button.config(text="✅ Copié !")
                parent.after(2000, lambda: copier_button.config(text=original_text))
            except Exception as e:
                copier_button.config(text="❌ Erreur")
                parent.after(2000, lambda: copier_button.config(text="📋 Copier le résultat"))

    # Configurer le bouton copier
    copier_button.config(command=copier_contenu)

    def effacer_resultat():
        """Efface le contenu de la zone de résultat"""
        result_text.config(state=NORMAL)
        result_text.delete("1.0", "end")
        result_text.config(state=DISABLED)
        copier_button.pack_forget()

    return result_frame, result_label, result_text, afficher_resultat, effacer_resultat

def lancer_compt_voy(parent):
    page = Toplevel(parent)
    page.configure(bg=PALETTE["fond_principal"])
    page.geometry("700x600")
    page.title("Compteur de voyelles")
    centrer_fenetre(page)
    
    style = configurer_style()

    main_frame = Frame(page, bg=PALETTE["fond_principal"], padx=30, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Titre
    label1 = Label(main_frame, text="Compteur de voyelles", 
                  font=("Century Gothic", 18, "bold"),
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label1.pack(pady=(0, 10))

    label2 = Label(main_frame, text="Entrez votre texte :", 
                  font=("Century Gothic", 12, "bold"),
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label2.pack(anchor="w", pady=(10, 5))

    # Zone de saisie
    entre1 = Text(main_frame, height=8, width=60, font=("Century Gothic", 11),
                 wrap=WORD, relief=SOLID, borderwidth=1)
    entre1.pack(fill=X, pady=(0, 15))
    entre1.focus_set()

    # Zone de résultat avec copier
    result_frame, result_label, result_text, afficher_resultat, effacer_result = creer_zone_resultat_copiable(main_frame)
    result_frame.pack(fill=X, pady=(10, 0))

    def test_voyelle():
        texte = entre1.get("1.0", "end").strip()
        if texte:
            try:
                resultat = compterVoyelles(texte)
                afficher_resultat(resultat, PALETTE["primaire"])
            except Exception as e:
                afficher_resultat(f"❌ Erreur : {str(e)}", PALETTE["erreur"], False)
        else:
            afficher_resultat("❌ Veuillez entrer du texte.", PALETTE["erreur"], False)

    def effacer_saisie():
        entre1.delete("1.0", "end")
        effacer_result()

    # Frame boutons
    bouton_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    bouton_frame.pack(pady=15)

    button_test = ttk.Button(bouton_frame, text="🔢 Compter les voyelles", 
                            style="Custom.TButton", command=test_voyelle)
    button_test.pack(side=LEFT, padx=5)

    button_effacer = ttk.Button(bouton_frame, text="🗑️ Effacer tout", 
                               style="Custom.TButton", command=effacer_saisie)
    button_effacer.pack(side=LEFT, padx=5)

    # Bouton Quitter
    quit_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    quit_frame.pack(pady=(20, 0), fill=X)
    
    button_quitter = ttk.Button(quit_frame, text="🚪 Quitter", 
                               style="Quit.TButton", command=page.destroy)
    button_quitter.pack(fill=X)

def lancer_compt_lettre():
    page = Toplevel()
    page.configure(bg=PALETTE["fond_principal"])
    page.geometry("750x650")
    page.title("Compteur de lettres")
    centrer_fenetre(page)
    
    style = configurer_style()

    main_frame = Frame(page, bg=PALETTE["fond_principal"], padx=30, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Titre
    label1 = Label(main_frame, text="Compteur de lettres", 
                  font=("Century Gothic", 18, "bold"),
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label1.pack(pady=(0, 10))

    # Zone de saisie du texte
    texte_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    texte_frame.pack(fill=X, pady=(10, 0))
    
    label_texte = Label(texte_frame, text="Entrez votre texte :", 
                       font=("Century Gothic", 12, "bold"),
                       bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_texte.pack(anchor="w", pady=(0, 5))

    entre_texte = Text(texte_frame, height=6, width=60, font=("Century Gothic", 11),
                      wrap=WORD, relief=SOLID, borderwidth=1)
    entre_texte.pack(fill=X)
    entre_texte.focus_set()

    # Zone de saisie de la lettre
    lettre_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    lettre_frame.pack(fill=X, pady=(15, 0))
    
    label_lettre = Label(lettre_frame, text="Entrez la lettre à compter :", 
                        font=("Century Gothic", 12, "bold"),
                        bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_lettre.pack(anchor="w", pady=(0, 5))

    entre_lettre = Entry(lettre_frame, font=("Century Gothic", 12),
                        relief=SOLID, borderwidth=1, justify=CENTER)
    entre_lettre.pack(fill=X)

    # Zone de résultat avec copier
    result_frame, result_label, result_text, afficher_resultat, effacer_result = creer_zone_resultat_copiable(main_frame)
    result_frame.pack(fill=X, pady=(15, 0))

    def test_lettre():
        texte = entre_texte.get("1.0", "end").strip()
        lettre = entre_lettre.get().strip()
        
        if not texte:
            afficher_resultat("❌ Veuillez entrer du texte.", PALETTE["erreur"], False)
            return
        
        if not lettre:
            afficher_resultat("❌ Veuillez entrer une lettre.", PALETTE["erreur"], False)
            return
        
        if len(lettre) != 1:
            afficher_resultat("❌ Veuillez entrer une seule lettre.", PALETTE["erreur"], False)
            return
        
        try:
            resultat = compterlettre(texte, lettre)
            afficher_resultat(resultat, PALETTE["primaire"])
        except Exception as e:
            afficher_resultat(f"❌ Erreur : {str(e)}", PALETTE["erreur"], False)

    def effacer_saisie():
        entre_texte.delete("1.0", "end")
        entre_lettre.delete(0, END)
        effacer_result()

    # Frame boutons
    bouton_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    bouton_frame.pack(pady=15)

    button_test = ttk.Button(bouton_frame, text="🔍 Compter la lettre", 
                            style="Custom.TButton", command=test_lettre)
    button_test.pack(side=LEFT, padx=5)

    button_effacer = ttk.Button(bouton_frame, text="🗑️ Effacer tout", 
                               style="Custom.TButton", command=effacer_saisie)
    button_effacer.pack(side=LEFT, padx=5)

    # Bouton Quitter
    quit_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    quit_frame.pack(pady=(20, 0), fill=X)
    
    button_quitter = ttk.Button(quit_frame, text="🚪 Quitter", 
                               style="Quit.TButton", command=page.destroy)
    button_quitter.pack(fill=X)

def lancer_rech_mot():
    page = Toplevel()
    page.configure(bg=PALETTE["fond_principal"])
    page.geometry("750x650")
    page.title("Recherche de mot")
    centrer_fenetre(page)
    
    style = configurer_style()

    main_frame = Frame(page, bg=PALETTE["fond_principal"], padx=30, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Titre
    label1 = Label(main_frame, text="Recherche de mot", 
                  font=("Century Gothic", 18, "bold"),
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label1.pack(pady=(0, 10))

    # Zone de saisie du texte
    texte_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    texte_frame.pack(fill=X, pady=(10, 0))
    
    label_texte = Label(texte_frame, text="Entrez votre texte :", 
                       font=("Century Gothic", 12, "bold"),
                       bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_texte.pack(anchor="w", pady=(0, 5))

    entre_texte = Text(texte_frame, height=6, width=60, font=("Century Gothic", 11),
                      wrap=WORD, relief=SOLID, borderwidth=1)
    entre_texte.pack(fill=X)
    entre_texte.focus_set()

    # Zone de saisie du mot
    mot_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    mot_frame.pack(fill=X, pady=(15, 0))
    
    label_mot = Label(mot_frame, text="Entrez le mot à rechercher :", 
                     font=("Century Gothic", 12, "bold"),
                     bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_mot.pack(anchor="w", pady=(0, 5))

    entre_mot = Entry(mot_frame, font=("Century Gothic", 12),
                     relief=SOLID, borderwidth=1)
    entre_mot.pack(fill=X)

    # Zone de résultat avec copier
    result_frame, result_label, result_text, afficher_resultat, effacer_result = creer_zone_resultat_copiable(main_frame)
    result_frame.pack(fill=X, pady=(15, 0))

    def test_mot():
        texte = entre_texte.get("1.0", "end").strip()
        mot = entre_mot.get().strip()
        
        if not texte:
            afficher_resultat("❌ Veuillez entrer du texte.", PALETTE["erreur"], False)
            return
        
        if not mot:
            afficher_resultat("❌ Veuillez entrer un mot.", PALETTE["erreur"], False)
            return
        
        try:
            resultat = compter_occurrences(texte, mot)
            afficher_resultat(resultat, PALETTE["primaire"])
        except Exception as e:
            afficher_resultat(f"❌ Erreur : {str(e)}", PALETTE["erreur"], False)

    def effacer_saisie():
        entre_texte.delete("1.0", "end")
        entre_mot.delete(0, END)
        effacer_result()

    # Frame boutons
    bouton_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    bouton_frame.pack(pady=15)

    button_test = ttk.Button(bouton_frame, text="🔍 Rechercher le mot", 
                            style="Custom.TButton", command=test_mot)
    button_test.pack(side=LEFT, padx=5)

    button_effacer = ttk.Button(bouton_frame, text="🗑️ Effacer tout", 
                               style="Custom.TButton", command=effacer_saisie)
    button_effacer.pack(side=LEFT, padx=5)

    # Bouton Quitter
    quit_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    quit_frame.pack(pady=(20, 0), fill=X)
    
    button_quitter = ttk.Button(quit_frame, text="🚪 Quitter", 
                               style="Quit.TButton", command=page.destroy)
    button_quitter.pack(fill=X)

def lancer_palindrome():
    page = Toplevel()
    page.configure(bg=PALETTE["fond_principal"])
    page.geometry("700x700")
    page.title("Détecteur de Palindromes")
    centrer_fenetre(page)
    
    style = configurer_style()

    main_frame = Frame(page, bg=PALETTE["fond_principal"], padx=30, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Titre
    titre_label = Label(main_frame, text="Détecteur de Palindromes", 
                       font=("Century Gothic", 18, "bold"),
                       bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    titre_label.pack(pady=(0, 10))

    # Description
    description = Label(main_frame, 
                       text="Un palindrome est un mot, une phrase ou un nombre\nqui se lit de la même manière de gauche à droite et de droite à gauche.",
                       font=("Century Gothic", 11),
                       bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    description.pack(pady=(0, 10))

    # Exemples
    exemples_label = Label(main_frame,
                          text="Exemples: 'radar', 'kayak', 'Ésope reste ici et se repose'",
                          font=("Century Gothic", 10, "italic"),
                          bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
    exemples_label.pack(pady=(0, 20))

    # Zone de saisie
    saisie_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    saisie_frame.pack(fill=X, pady=(10, 0))
    
    label_saisie = Label(saisie_frame, text="Entrez votre texte :", 
                         font=("Century Gothic", 12, "bold"),
                         bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_saisie.pack(anchor="w", pady=(0, 5))

    entre1 = Text(saisie_frame, height=6, width=60, font=("Century Gothic", 11),
                 wrap=WORD, relief=SOLID, borderwidth=1)
    entre1.pack(fill=X)
    entre1.focus_set()

    # Zone de résultat avec copier
    result_frame, result_label, result_text, afficher_resultat, effacer_result = creer_zone_resultat_copiable(main_frame)
    result_frame.pack(fill=X, pady=(15, 0))

    def test_palindrome():
        texte = entre1.get("1.0", "end").strip()
        if texte:
            try:
                resultat = palindrome_amelioré(texte)
                if "✅" in resultat:
                    afficher_resultat(resultat, PALETTE["succes"])
                else:
                    afficher_resultat(resultat, PALETTE["primaire"])
            except Exception as e:
                afficher_resultat(f"❌ Erreur : {str(e)}", PALETTE["erreur"], False)
        else:
            afficher_resultat("❌ Veuillez entrer du texte.", PALETTE["erreur"], False)

    def effacer_saisie():
        entre1.delete("1.0", "end")
        effacer_result()

    def inserer_exemple():
        exemples = [
            "Ésope reste ici et se repose",
            "Engage le jeu que je le gagne",
            "radar",
            "kayak",
            "été",
            "12321",
            "A man, a plan, a canal: Panama"
        ]
        entre1.delete("1.0", "end")
        import random
        exemple = random.choice(exemples)
        entre1.insert("1.0", exemple)

    # Frame pour les boutons
    bouton_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    bouton_frame.pack(pady=15)

    button_test = ttk.Button(bouton_frame, text="🔄 Tester", 
                            style="Custom.TButton", 
                            command=test_palindrome)
    button_test.pack(side=LEFT, padx=5)

    button_effacer = ttk.Button(bouton_frame, text="🗑️ Effacer", 
                               style="Custom.TButton", 
                               command=effacer_saisie)
    button_effacer.pack(side=LEFT, padx=5)

    button_exemple = ttk.Button(bouton_frame, text="📋 Exemple", 
                               style="Custom.TButton", 
                               command=inserer_exemple)
    button_exemple.pack(side=LEFT, padx=5)

    # Info supplémentaire
    info_label = Label(main_frame,
                      text="✓ Ignore les majuscules/minuscules\n✓ Ignore les espaces et la ponctuation\n✓ Gère les accents français",
                      font=("Century Gothic", 10),
                      bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
    info_label.pack(pady=(10, 0))

    # Bouton Quitter
    quit_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    quit_frame.pack(pady=(20, 0), fill=X)
    
    button_quitter = ttk.Button(quit_frame, text="🚪 Quitter", 
                               style="Quit.TButton", 
                               command=page.destroy)
    button_quitter.pack(fill=X)

def lancer_operation_texte(operation, titre_text="Opération Texte", description=""):
    """
    Interface générique pour les opérations sur le texte avec bouton copier
    """
    page = Toplevel()
    page.configure(bg=PALETTE["fond_principal"])
    page.geometry("750x700")
    page.title(titre_text)
    centrer_fenetre(page)
    
    style = configurer_style()

    # Frame principal
    main_frame = Frame(page, bg=PALETTE["fond_principal"], padx=30, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Titre
    label_titre = Label(main_frame, text=titre_text, 
                       font=("Century Gothic", 18, "bold"),
                       bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_titre.pack(pady=(0, 10))

    # Description
    if description:
        label_desc = Label(main_frame, text=description, 
                          font=("Century Gothic", 11),
                          bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
                          wraplength=600)
        label_desc.pack(pady=(0, 15))

    # Zone de saisie 1
    saisie_frame1 = Frame(main_frame, bg=PALETTE["fond_principal"])
    saisie_frame1.pack(fill=X, pady=5)
    
    label_saisie1 = Label(saisie_frame1, text="Texte à traiter :", 
                         font=("Century Gothic", 12, "bold"),
                         bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label_saisie1.pack(anchor="w", pady=(0, 5))

    entre1 = Text(saisie_frame1, height=6, width=60, font=("Century Gothic", 11),
                 wrap=WORD, relief=SOLID, borderwidth=1)
    entre1.pack(fill=X)
    entre1.focus_set()

    # Zone de saisie 2 (si nécessaire)
    entre2_frame = None
    entre2 = None
    if operation in ["anagramme"]:
        entre2_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
        entre2_frame.pack(fill=X, pady=(10, 5))
        
        label_saisie2 = Label(entre2_frame, text="Deuxième texte (pour comparaison) :", 
                             font=("Century Gothic", 12, "bold"),
                             bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        label_saisie2.pack(anchor="w", pady=(0, 5))

        entre2 = Text(entre2_frame, height=4, width=60, font=("Century Gothic", 11),
                     wrap=WORD, relief=SOLID, borderwidth=1)
        entre2.pack(fill=X)

    # Zone de résultat avec copier
    result_frame, result_label, result_text, afficher_resultat, effacer_result = creer_zone_resultat_copiable(main_frame, hauteur=8)
    result_frame.pack(fill=X, pady=(15, 0))

    def executer_operation():
        texte1 = entre1.get("1.0", "end").strip()
        
        if not texte1 and operation != "mdp":
            afficher_resultat("❌ Veuillez entrer du texte.", PALETTE["erreur"], False)
            return

        try:
            if operation == "inverser":
                resultat = inverser_chaine(texte1)
                titre_operation = "Texte inversé"
                
            elif operation == "compter_mots":
                nb_mots = compter_mots(texte1)
                resultat = f"Nombre de mots : {nb_mots}"
                titre_operation = "Comptage des mots"
                
            elif operation == "convertir_case":
                maj = majuscules(texte1)
                minu = minuscules(texte1)
                tit = titre(texte1)
                resultat = f"MAJUSCULES :\n{maj}\n\nminuscules :\n{minu}\n\nTitre :\n{tit}"
                titre_operation = "Conversion de casse"
                
            elif operation == "nettoyer":
                resultat = nettoyer_espaces(texte1)
                titre_operation = "Texte nettoyé"
                
            elif operation == "anagramme":
                texte2 = entre2.get("1.0", "end").strip() if entre2 else ""
                if not texte2:
                    afficher_resultat("❌ Veuillez entrer le deuxième texte.", PALETTE["erreur"], False)
                    return
                
                if est_anagramme(texte1, texte2):
                    resultat = "✅ Ce sont des anagrammes !"
                else:
                    resultat = "❌ Ce ne sont pas des anagrammes"
                titre_operation = "Vérification d'anagramme"
                
            elif operation == "mdp":
                resultat = generer_mot_de_passe(12)
                titre_operation = "Mot de passe généré"
                
            elif operation == "encoder":
                resultat = encoder_base64(texte1)
                titre_operation = "Texte encodé (Base64)"
                
            elif operation == "decoder":
                resultat = decoder_base64(texte1)
                titre_operation = "Texte décodé (Base64)"
                
            elif operation == "consonnes":
                nb_consonnes = compter_consonnes(texte1)
                resultat = f"Nombre de consonnes : {nb_consonnes}"
                titre_operation = "Comptage des consonnes"
                
            elif operation == "chiffres":
                chiffres = extraire_chiffres(texte1)
                resultat = f"Chiffres extraits : {chiffres}"
                titre_operation = "Extraction de chiffres"
                
            elif operation == "rot13":
                resultat = rot13(texte1)
                titre_operation = "Texte chiffré (ROT13)"
                
            else:
                resultat = "Opération non reconnue"
                titre_operation = "Erreur"

            # Mettre à jour le label du résultat
            result_label.config(text=f"{titre_operation} :")
            
            # Afficher le résultat
            afficher_resultat(resultat, PALETTE["primaire"])
            
        except Exception as e:
            afficher_resultat(f"❌ Erreur : {str(e)}", PALETTE["erreur"], False)

    def effacer_saisie():
        entre1.delete("1.0", "end")
        if entre2:
            entre2.delete("1.0", "end")
        effacer_result()
        result_label.config(text="Résultat :")

    def inserer_exemple():
        exemples = {
            "inverser": "Bonjour tout le monde",
            "compter_mots": "Voici une phrase d'exemple pour le comptage.",
            "convertir_case": "texte Exemple À Convertir",
            "nettoyer": "   Texte   avec   trop   d'espaces    ",
            "encoder": "Texte à encoder en Base64",
            "decoder": "VGV4dGUgw6AgZGVjb2RlciBlbiBCYXNlNjQ=",
            "rot13": "Texte secret",
            "chiffres": "Mon numéro est le 06 12 34 56 78"
        }
        
        exemple = exemples.get(operation, "Exemple de texte")
        entre1.delete("1.0", "end")
        entre1.insert("1.0", exemple)

    # Frame pour les boutons
    bouton_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    bouton_frame.pack(pady=15)

    button_executer = ttk.Button(bouton_frame, text="▶️ Exécuter", 
                                style="Custom.TButton", 
                                command=executer_operation)
    button_executer.pack(side=LEFT, padx=5)

    button_effacer = ttk.Button(bouton_frame, text="🗑️ Effacer", 
                               style="Custom.TButton", 
                               command=effacer_saisie)
    button_effacer.pack(side=LEFT, padx=5)

    if operation in ["inverser", "compter_mots", "convertir_case", "nettoyer", 
                    "encoder", "decoder", "rot13", "chiffres"]:
        button_exemple = ttk.Button(bouton_frame, text="📋 Exemple", 
                                   style="Custom.TButton", 
                                   command=inserer_exemple)
        button_exemple.pack(side=LEFT, padx=5)

    # Bouton Quitter
    quit_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    quit_frame.pack(pady=(20, 0), fill=X)
    
    button_quitter = ttk.Button(quit_frame, text="🚪 Quitter", 
                               style="Quit.TButton", 
                               command=page.destroy)
    button_quitter.pack(fill=X)

def lancer_operation(operation_type):
    """
    Fonction wrapper pour lancer les différentes opérations
    """
    descriptions = {
        "inverser": ("Inverser une chaîne", "Inverse l'ordre des caractères dans le texte"),
        "compter_mots": ("Compter les mots", "Compte le nombre de mots dans le texte"),
        "convertir_case": ("Convertir majuscules/minuscules", "Convertit le texte en majuscules, minuscules ou format titre"),
        "nettoyer": ("Nettoyer les espaces", "Supprime les espaces superflus (début, fin et multiples)"),
        "anagramme": ("Vérifier anagramme", "Vérifie si deux textes sont des anagrammes"),
        "mdp": ("Générer mot de passe", "Génère un mot de passe aléatoire sécurisé"),
        "encoder": ("Encoder Base64", "Encode le texte en format Base64"),
        "decoder": ("Décoder Base64", "Décode le texte depuis le format Base64"),
        "consonnes": ("Compter les consonnes", "Compte le nombre de consonnes dans le texte"),
        "chiffres": ("Extraire les chiffres", "Extrait tous les chiffres du texte"),
        "rot13": ("Chiffrement ROT13", "Applique le chiffrement ROT13 au texte")
    }
    
    titre_text, description = descriptions.get(operation_type, (f"Opération {operation_type}", ""))
    lancer_operation_texte(operation_type, titre_text, description)

def lancer_chaine(parent=None):
    is_toplevel = False
    try:
        is_toplevel = (parent is None) or isinstance(parent, (Tk, Toplevel))
    except Exception:
        is_toplevel = True

    if is_toplevel:
        chaine = Toplevel(parent)
        chaine.configure(bg=PALETTE["fond_principal"])
        chaine.geometry("600x750")
        chaine.title("Opérations sur les chaînes de caractères")
        centrer_fenetre(chaine)
    else:
        chaine = parent
        for w in list(chaine.winfo_children()):
            w.destroy()
        try:
            chaine.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    # Frame principal avec padding
    main_frame = Frame(chaine, bg=PALETTE["fond_principal"], padx=20, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Titre
    label1 = Label(main_frame, text="Opérations sur les chaînes", 
                  font=("Century Gothic", 18, "bold"), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
    label1.pack(pady=(0, 10))

    label2 = Label(main_frame, text="Choisissez une opération :", 
                  font=("Century Gothic", 12), 
                  bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
    label2.pack(pady=(0, 15))

    # Canvas avec scrollbar pour les boutons
    canvas_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    canvas_frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(canvas_frame, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    
    # Frame intérieur pour les boutons
    button_container = Frame(canvas, bg=PALETTE["fond_principal"])
    
    # Configuration du canvas
    canvas_window = canvas.create_window((0, 0), window=button_container, anchor="nw", width=540)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack du canvas et scrollbar
    canvas.pack(side="left", fill="both", expand=True, padx=(0, 5))
    scrollbar.pack(side="right", fill="y")

    # Configuration du redimensionnement
    def configure_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_window, width=canvas.winfo_width() - 20)
    
    button_container.bind("<Configure>", configure_scrollregion)
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=canvas.winfo_width() - 20))

    style = configurer_style()
    
    # Liste des boutons avec leurs commandes et emojis
    boutons = [
        ("🔤 Comptage de voyelles", lambda: lancer_compt_voy(chaine)),
        ("🔡 Comptage d'une lettre", lancer_compt_lettre),
        ("📝 Comptage d'un mot", lancer_rech_mot),
        ("🔄 Test Palindrome", lancer_palindrome),
        ("⬅️➡️ Inverser une chaîne", lambda: lancer_operation("inverser")),
        ("🔢 Compter les mots", lambda: lancer_operation("compter_mots")),
        ("🅰️ Convertir majuscules/minuscules", lambda: lancer_operation("convertir_case")),
        ("🧹 Nettoyer les espaces", lambda: lancer_operation("nettoyer")),
        ("🔀 Vérifier anagramme", lambda: lancer_operation("anagramme")),
        ("🔐 Générer mot de passe", lambda: lancer_operation("mdp")),
        ("🔒 Encoder Base64", lambda: lancer_operation("encoder")),
        ("🔓 Décoder Base64", lambda: lancer_operation("decoder")),
        ("🗣️ Compter les consonnes", lambda: lancer_operation("consonnes")),
        ("🔢 Extraire les chiffres", lambda: lancer_operation("chiffres")),
        ("🌀 Chiffrement ROT13", lambda: lancer_operation("rot13"))
    ]

    # Ajouter les boutons avec un espacement régulier
    for texte, commande in boutons:
        btn = ttk.Button(button_container, text=texte, 
                        style="Custom.TButton", 
                        command=commande)
        btn.pack(pady=6, fill=X, padx=10)
    
    # Ajouter un peu d'espace à la fin
    Label(button_container, height=1, bg=PALETTE["fond_principal"]).pack()

    # Bouton Quitter en bas du frame principal
    quit_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    quit_frame.pack(pady=(15, 0), fill=X)
    
    def _quit_local():
        if is_toplevel:
            chaine.destroy()
        else:
            for w in list(chaine.winfo_children()):
                w.destroy()
    quit_button = ttk.Button(quit_frame, text="🚪 Quitter", style="Quit.TButton", 
                           command=_quit_local)
    quit_button.pack(pady=10, fill=X, padx=10)

    # Activer le défilement avec la molette de la souris
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    def on_close():
        canvas.unbind_all("<MouseWheel>")
        chaine.destroy()
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    chaine.protocol("WM_DELETE_WINDOW", on_close)