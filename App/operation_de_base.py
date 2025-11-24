import math
from tkinter import *
from tkinter import ttk
import re
from .historique_manager import historique_manager


def launch_operation(parent=None):
    operation = Toplevel(parent)
    operation.title("Calculatrice de base")
    operation.geometry("500x550")
    operation.configure(bg="#F0F4F8")  # Même fond que main.py
    label3 = Label(operation,font=("Century Gothic",14), bg="#F0F4F8", fg="#1E40AF")

    def configurer_style():
        style = ttk.Style()
        style.configure("Custom.TButton",
                        foreground="#000000",
                        background="#3B82F6",  # Bleu moderne comme main.py
                        font=("Century Gothic", 10),
                        padding=(2, 2))
        
        # Style spécial pour le bouton Quitter
        style.configure("Quit.TButton",
                        foreground="#000000",
                        background="#DC2626",  # Rouge
                        font=("Century Gothic", 10),
                        padding=(2, 2))
        return style

    style = configurer_style()
    label1 = Label(operation, text="Calculatrice de base", bg="#F0F4F8", font=("Century Gothic", 14), fg="#1E40AF")
    label1.pack(pady=5)

    # Création du champ verrouillé
    entree = Text(operation, height=2, width=40, font=("Century Gothic", 10), state=DISABLED)
    entree.pack(pady=10)
    label3.pack(pady=10)
    
    # Blocage total des interactions utilisateur
    def bloquer_interaction(event):
        return "break"

    entree.bind("<Key>", bloquer_interaction)
    entree.bind("<Button-1>", bloquer_interaction)
    entree.bind("<Control-v>", bloquer_interaction)
    entree.bind("<Button-3>", bloquer_interaction)
    entree.config(insertontime=0)
    
    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(operation, bg="#F0F4F8")
    main_frame.pack(pady=5)

    # Ligne 1 : Fonctions générales
    ligne1_frame = Frame(main_frame, bg="#F0F4F8")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="esc", style="Custom.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="(", style="Custom.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text=")", style="Custom.TButton", width=5)
    btn4 = ttk.Button(ligne1_frame, text="%", style="Custom.TButton", width=5)
    btn33 = ttk.Button(ligne1_frame, text="|  |", style="Custom.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)
    btn4.pack(side="left", padx=2)
    btn33.pack(side="left", padx=2)

    # Ligne 2 : Chiffres 7–9 et multiplication
    ligne2_frame = Frame(main_frame, bg="#F0F4F8")
    ligne2_frame.pack(pady=2)

    btn5 = ttk.Button(ligne2_frame, text="cos", style="Custom.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="sin", style="Custom.TButton", width=5)
    btn7 = ttk.Button(ligne2_frame, text="tan", style="Custom.TButton", width=5)
    btn8 = ttk.Button(ligne2_frame, text="+/-", style="Custom.TButton", width=5)
    btn34 = ttk.Button(ligne2_frame, text="Deg°", style="Custom.TButton", width=5)

    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)
    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn34.pack(side="left", padx=2)

    # Ligne 3 : Chiffres 4–6 et addition
    ligne3_frame = Frame(main_frame, bg="#F0F4F8")
    ligne3_frame.pack(pady=2)

    btn9 = ttk.Button(ligne3_frame, text="√", style="Custom.TButton", width=5)
    btn10 = ttk.Button(ligne3_frame, text="ln", style="Custom.TButton", width=5)
    btn11 = ttk.Button(ligne3_frame, text="1/x", style="Custom.TButton", width=5)
    btn12 = ttk.Button(ligne3_frame, text="π", style="Custom.TButton", width=5)
    btn35 = ttk.Button(ligne3_frame, text="<-", style="Custom.TButton", width=5)

    btn9.pack(side="left", padx=2)
    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)
    btn35.pack(side="left", padx=2)

    # Ligne 4 : Chiffres 1–3 et soustraction
    ligne4_frame = Frame(main_frame, bg="#F0F4F8")
    ligne4_frame.pack(pady=2)

    btn13 = ttk.Button(ligne4_frame, text="!", style="Custom.TButton", width=5)
    btn14 = ttk.Button(ligne4_frame, text="log", style="Custom.TButton", width=5)
    btn15 = ttk.Button(ligne4_frame, text="x²", style="Custom.TButton", width=5)
    btn16 = ttk.Button(ligne4_frame, text="x^(n)", style="Custom.TButton", width=5)

    btn13.pack(side="left", padx=2)
    btn14.pack(side="left", padx=2)
    btn15.pack(side="left", padx=2)
    btn16.pack(side="left", padx=2)

    # Ligne 5 : +/- , 0 , . , =
    ligne5_frame = Frame(main_frame, bg="#F0F4F8")
    ligne5_frame.pack(pady=2)

    btn17 = ttk.Button(ligne5_frame, text="7", style="Custom.TButton", width=5)
    btn18 = ttk.Button(ligne5_frame, text="8", style="Custom.TButton", width=5)
    btn19 = ttk.Button(ligne5_frame, text="9", style="Custom.TButton", width=5)
    btn20 = ttk.Button(ligne5_frame, text="+", style="Custom.TButton", width=5)

    btn17.pack(side="left", padx=2)
    btn18.pack(side="left", padx=2)
    btn19.pack(side="left", padx=2)
    btn20.pack(side="left", padx=2)

    # Ligne 6 : Fonctions racine et trigonométrie
    ligne6_frame = Frame(main_frame, bg="#F0F4F8")
    ligne6_frame.pack(pady=2)

    btn21 = ttk.Button(ligne6_frame, text="4", style="Custom.TButton", width=5)
    btn22 = ttk.Button(ligne6_frame, text="5", style="Custom.TButton", width=5)
    btn23 = ttk.Button(ligne6_frame, text="6", style="Custom.TButton", width=5)
    btn24 = ttk.Button(ligne6_frame, text="-", style="Custom.TButton", width=5)

    btn21.pack(side="left", padx=2)
    btn22.pack(side="left", padx=2)
    btn23.pack(side="left", padx=2)
    btn24.pack(side="left", padx=2)

    # Ligne 7 : Fonctions logarithmiques et puissances
    ligne7_frame = Frame(main_frame, bg="#F0F4F8")
    ligne7_frame.pack(pady=2)

    btn25 = ttk.Button(ligne7_frame, text="1", style="Custom.TButton", width=5)
    btn26 = ttk.Button(ligne7_frame, text="2", style="Custom.TButton", width=5)
    btn27 = ttk.Button(ligne7_frame, text="3", style="Custom.TButton", width=5)
    btn28 = ttk.Button(ligne7_frame, text="/", style="Custom.TButton", width=5)

    btn25.pack(side="left", padx=2)
    btn26.pack(side="left", padx=2)
    btn27.pack(side="left", padx=2)
    btn28.pack(side="left", padx=2)

    # Ligne 8 : Constantes et fonctions inverses
    ligne8_frame = Frame(main_frame, bg="#F0F4F8")
    ligne8_frame.pack(pady=2)

    btn29 = ttk.Button(ligne8_frame, text="0", style="Custom.TButton", width=5)
    btn30 = ttk.Button(ligne8_frame, text=".", style="Custom.TButton", width=5)
    btn31 = ttk.Button(ligne8_frame, text="X", style="Custom.TButton", width=5)
    btn32 = ttk.Button(ligne8_frame, text="=", style="Custom.TButton", width=5)

    btn29.pack(side="left", padx=2)
    btn30.pack(side="left", padx=2)
    btn31.pack(side="left", padx=2)
    btn32.pack(side="left", padx=2)

    # Variables pour gérer la valeur absolue
    valeur_absolue_ouverte = False
    derniere_position_absolue = 0

    # Fonctions pour l'entrée de texte
    def inserer_text(texte):
        nonlocal valeur_absolue_ouverte, derniere_position_absolue
        
        entree.config(state=NORMAL)
        
        if texte == "|":
            if valeur_absolue_ouverte:
                # Fermer la valeur absolue
                entree.insert(END, "|")
                valeur_absolue_ouverte = False
            else:
                # Ouvrir la valeur absolue
                entree.insert(END, "|")
                valeur_absolue_ouverte = True
                derniere_position_absolue = entree.index(INSERT)
        else:
            entree.insert(END, texte)
            
        entree.config(state=DISABLED)


    import re

    def prepare_expression(expr: str) -> str:
        # Nettoyage des espaces
        expr = expr.replace(" ", "")

        # Valeur absolue : transformer |x| en abs(x)
        while "|" in expr:
            debut = expr.find("|")
            fin = expr.find("|", debut + 1)
            if fin == -1:
                expr = expr.replace("|", "", 1)
            else:
                contenu = expr[debut+1:fin]
                expr = expr[:debut] + f"abs({contenu})" + expr[fin+1:]

        # Insertion de multiplication implicite : 3π → 3*math.pi, 2cos → 2*math.cos
        expr = re.sub(r"(\d)(π)", r"\1*π", expr)
        expr = re.sub(r"(\d)(√)", r"\1*√", expr)
        expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)


        # Remplacements simples
        expr = expr.replace("π", "math.pi")
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("^", "**")
        expr = expr.replace("%", "/100")
        expr = re.sub(r"(\d+)!", r"math.factorial(\1)", expr)

        # Fonctions mathématiques
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("ln", "math.log")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("rad", "math.radians")

        return expr

    
    def equilibrer_parentheses(expr: str) -> str:
        """
        Ajoute des parenthèses fermantes si besoin pour équilibrer l'expression.
        """
        ouvert = expr.count("(")
        ferme = expr.count(")")
        manque = ouvert - ferme
        if manque > 0:
            expr += ")" * manque
        return expr
    
    def evaluer_expression(expr: str) -> str:
        expr = equilibrer_parentheses(expr)
        expr = prepare_expression(expr)
        return str(eval(expr, {"__builtins__": None}, {"math": math, "abs": abs}))



    def recherche_du_resultat():
        nonlocal valeur_absolue_ouverte
        expression = entree.get("1.0", END).strip()

        # Fermer automatiquement les valeurs absolues non fermées
        if valeur_absolue_ouverte:
            inserer_text("|")
            expression = entree.get("1.0", END).strip()

        try:
            resultat = evaluer_expression(expression)
            entree.config(state=NORMAL)
            entree.delete("1.0", END)
            entree.insert(END, resultat)
            entree.config(state=DISABLED)
            
            # === SAUVEGARDE DU CALCUL ===
            entree_data = {"expression": expression}
            historique_manager.ajouter_calcul(
                module="Opérations de Base",
                operation="Calculatrice",
                entree=entree_data,
                resultat=resultat
            )
            # ============================
            
            label3.config(text="", fg="#1E40AF")  # Effacer le message d'erreur
        except Exception as e:
            label3.config(text=f"❌ Erreur : {e}", fg="#DC2626")
            entree.config(state=NORMAL)
            entree.delete("1.0", END)
            entree.config(state=DISABLED)

    def remise_a_blanc():
        nonlocal valeur_absolue_ouverte
        entree.config(state=NORMAL)
        entree.delete("1.0", END)
        entree.config(state=DISABLED)
        valeur_absolue_ouverte = False
        label3.config(text="", fg="#1E40AF")

    def suppr():
        nonlocal valeur_absolue_ouverte, derniere_position_absolue
        
        entree.config(state=NORMAL)
        contenu = entree.get("1.0", END).strip()
        
        if contenu:
            # Supprimer le dernier caractère
            entree.delete("end-2c", "end-1c")
            
            # Vérifier si on a supprimé un | de valeur absolue
            if valeur_absolue_ouverte and len(contenu) > 0 and contenu[-1] == "|":
                valeur_absolue_ouverte = False
        
        entree.config(state=DISABLED)

    # Actions derrière les boutons
    btn1.config(command=remise_a_blanc)
    btn2.config(command=lambda: inserer_text("("))
    btn3.config(command=lambda: inserer_text(")"))
    btn4.config(command=lambda: inserer_text("%"))
    btn33.config(command=lambda: inserer_text("|"))

    btn5.config(command=lambda: inserer_text("cos("))
    btn6.config(command=lambda: inserer_text("sin("))
    btn7.config(command=lambda: inserer_text("tan("))
    btn8.config(command=lambda: inserer_text("-"))
    btn34.config(command=lambda: inserer_text("rad("))
    btn35.config(command=suppr)

    btn9.config(command=lambda: inserer_text("√("))
    btn10.config(command=lambda: inserer_text("ln("))
    btn11.config(command=lambda: inserer_text("1/("))
    btn12.config(command=lambda: inserer_text("π"))

    btn13.config(command=lambda: inserer_text("!"))
    btn14.config(command=lambda: inserer_text("log("))
    btn15.config(command=lambda: inserer_text("**2"))
    btn16.config(command=lambda: inserer_text("**"))

    btn17.config(command=lambda: inserer_text("7"))
    btn18.config(command=lambda: inserer_text("8"))
    btn19.config(command=lambda: inserer_text("9"))
    btn20.config(command=lambda: inserer_text("+"))

    btn21.config(command=lambda: inserer_text("4"))
    btn22.config(command=lambda: inserer_text("5"))
    btn23.config(command=lambda: inserer_text("6"))
    btn24.config(command=lambda: inserer_text("-"))

    btn25.config(command=lambda: inserer_text("1"))
    btn26.config(command=lambda: inserer_text("2"))
    btn27.config(command=lambda: inserer_text("3"))
    btn28.config(command=lambda: inserer_text("/"))

    btn29.config(command=lambda: inserer_text("0"))
    btn30.config(command=lambda: inserer_text("."))
    btn31.config(command=lambda: inserer_text("*"))
    btn32.config(command=recherche_du_resultat)

    # Ajout du bouton Quitter en bas
    frame_quitter = Frame(operation, bg="#F0F4F8")
    frame_quitter.pack(pady=10)
    
    btn_quitter = ttk.Button(frame_quitter, text="Quitter", style="Quit.TButton", 
                           width=20, command=operation.destroy)
    btn_quitter.pack()