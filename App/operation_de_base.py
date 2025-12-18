"""
operation_de_base.py - Interface de calcul simple
Auteur: Junior Kossivi
Description: Interface Tkinter pour les calcul simples (Une Calculatrice)
"""
# ruff: noqa: E402,F405

import math
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
import re
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

def launch_operation(parent=None):
    import tkinter as tk

    # Si parent est une fenêtre (Tk ou Toplevel) ou None -> créer Toplevel
    # Sinon on rend le module dans le Frame fourni (mode intégration)
    is_toplevel = parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))
    if is_toplevel:
        operation = Toplevel(parent)
        operation.title("Calculatrice de base")
        operation.geometry("500x750")
        operation.configure(bg=PALETTE["fond_principal"])
        operation.resizable(False, False)
        # Centrer la fenêtre
        operation.transient(parent)
        operation.grab_set()
    else:
        operation = parent
        # nettoyer l'espace de contenu avant d'afficher
        for child in list(operation.winfo_children()):
            child.destroy()
        try:
            operation.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass

    def configurer_style():
        s = ensure_style()
        if s is None:
            s = ttk.Style()
            try:
                s.theme_use("clam")  # ✅ Ajout du thème clam
            except Exception:
                pass
        
        # Style bouton principal
        s.configure("Custom.TButton",
                    foreground=PALETTE["fond_secondaire"],
                    background=PALETTE["primaire"],
                    font=("Century Gothic", 10, "bold"),
                    padding=8,
                    relief="flat",
                    focuscolor="none")
        
        # Style pour boutons de la calculatrice (taille réduite)
        s.configure("Calc.TButton",
                    foreground=PALETTE["fond_secondaire"],
                    background=PALETTE["primaire"],
                    font=("Century Gothic", 10),
                    padding=2,
                    relief="flat",
                    width=6)
        
        # Style spécial pour le bouton Quitter
        s.configure("Quit.TButton",
                    foreground=PALETTE["fond_secondaire"],
                    background=PALETTE["erreur"],
                    font=("Century Gothic", 11, "bold"),
                    padding=10,
                    relief="flat",
                    focuscolor="none")
        
        # Effets de survol
        s.map("Custom.TButton",
             background=[('active', PALETTE["secondaire"]),
                        ('pressed', '#1E3A8A')],
             foreground=[('active', PALETTE["fond_secondaire"])])
        
        s.map("Quit.TButton",
             background=[('active', '#B91C1C'),
                        ('pressed', '#991B1B')],
             foreground=[('active', PALETTE["fond_secondaire"])])
        
        return s

    ensure_style()
    
    # Titre principal
    label1 = Label(operation, text="🧮 CALCULATRICE DE BASE", 
                   bg=PALETTE["fond_principal"], font=("Century Gothic", 16, "bold"), fg=PALETTE["primaire"])
    label1.pack(pady=15)

    # Label pour les messages d'erreur/succès
    label3 = Label(operation, font=("Century Gothic", 10), bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"])
    label3.pack(pady=5)

    # Création du champ verrouillé
    entree = Text(operation, height=2, width=40, font=("Century Gothic", 12), 
                  state=DISABLED, relief="solid", borderwidth=1, bg=PALETTE["fond_secondaire"])
    entree.pack(pady=10)
    
    # Blocage total des interactions utilisateur
    def bloquer_interaction(event):
        return "break"

    entree.bind("<Key>", bloquer_interaction)
    entree.bind("<Button-1>", bloquer_interaction)
    entree.bind("<Control-v>", bloquer_interaction)
    entree.bind("<Button-3>", bloquer_interaction)
    entree.config(insertontime=0)
    
    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(operation, bg=PALETTE["fond_principal"])
    main_frame.pack(pady=10)

    # Ligne 1 : Fonctions générales
    ligne1_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne1_frame.pack(pady=3)

    btn1 = ttk.Button(ligne1_frame, text="ESC", style="Calc.TButton", width=6)
    btn2 = ttk.Button(ligne1_frame, text="(", style="Calc.TButton", width=6)
    btn3 = ttk.Button(ligne1_frame, text=")", style="Calc.TButton", width=6)
    btn4 = ttk.Button(ligne1_frame, text="%", style="Calc.TButton", width=6)
    btn33 = ttk.Button(ligne1_frame, text="|  |", style="Calc.TButton", width=6)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)
    btn4.pack(side="left", padx=2)
    btn33.pack(side="left", padx=2)

    # Ligne 2 : Fonctions trigonométriques
    ligne2_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne2_frame.pack(pady=3)

    btn5 = ttk.Button(ligne2_frame, text="cos", style="Calc.TButton", width=6)
    btn6 = ttk.Button(ligne2_frame, text="sin", style="Calc.TButton", width=6)
    btn7 = ttk.Button(ligne2_frame, text="tan", style="Calc.TButton", width=6)
    btn8 = ttk.Button(ligne2_frame, text="+/-", style="Calc.TButton", width=6)
    btn34 = ttk.Button(ligne2_frame, text="Deg°", style="Calc.TButton", width=6)

    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)
    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn34.pack(side="left", padx=2)

    # Ligne 3 : Fonctions mathématiques avancées
    ligne3_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne3_frame.pack(pady=3)

    btn9 = ttk.Button(ligne3_frame, text="√", style="Calc.TButton", width=6)
    btn10 = ttk.Button(ligne3_frame, text="ln", style="Calc.TButton", width=6)
    btn11 = ttk.Button(ligne3_frame, text="1/x", style="Calc.TButton", width=6)
    btn12 = ttk.Button(ligne3_frame, text="π", style="Calc.TButton", width=6)
    btn35 = ttk.Button(ligne3_frame, text="←", style="Calc.TButton", width=6)

    btn9.pack(side="left", padx=2)
    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)
    btn35.pack(side="left", padx=2)

    # Ligne 4 : Fonctions spéciales
    ligne4_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne4_frame.pack(pady=3)

    btn13 = ttk.Button(ligne4_frame, text="!", style="Calc.TButton", width=6)
    btn14 = ttk.Button(ligne4_frame, text="log", style="Calc.TButton", width=6)
    btn15 = ttk.Button(ligne4_frame, text="x²", style="Calc.TButton", width=6)
    btn16 = ttk.Button(ligne4_frame, text="x^(n)", style="Calc.TButton", width=6)

    btn13.pack(side="left", padx=2)
    btn14.pack(side="left", padx=2)
    btn15.pack(side="left", padx=2)
    btn16.pack(side="left", padx=2)

    # Ligne 5 : Chiffres 7-9 et addition
    ligne5_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne5_frame.pack(pady=3)

    btn17 = ttk.Button(ligne5_frame, text="7", style="Calc.TButton", width=6)
    btn18 = ttk.Button(ligne5_frame, text="8", style="Calc.TButton", width=6)
    btn19 = ttk.Button(ligne5_frame, text="9", style="Calc.TButton", width=6)
    btn20 = ttk.Button(ligne5_frame, text="+", style="Calc.TButton", width=6)

    btn17.pack(side="left", padx=2)
    btn18.pack(side="left", padx=2)
    btn19.pack(side="left", padx=2)
    btn20.pack(side="left", padx=2)

    # Ligne 6 : Chiffres 4-6 et soustraction
    ligne6_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne6_frame.pack(pady=3)

    btn21 = ttk.Button(ligne6_frame, text="4", style="Calc.TButton", width=6)
    btn22 = ttk.Button(ligne6_frame, text="5", style="Calc.TButton", width=6)
    btn23 = ttk.Button(ligne6_frame, text="6", style="Calc.TButton", width=6)
    btn24 = ttk.Button(ligne6_frame, text="-", style="Calc.TButton", width=6)

    btn21.pack(side="left", padx=2)
    btn22.pack(side="left", padx=2)
    btn23.pack(side="left", padx=2)
    btn24.pack(side="left", padx=2)

    # Ligne 7 : Chiffres 1-3 et division
    ligne7_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne7_frame.pack(pady=3)

    btn25 = ttk.Button(ligne7_frame, text="1", style="Calc.TButton", width=6)
    btn26 = ttk.Button(ligne7_frame, text="2", style="Calc.TButton", width=6)
    btn27 = ttk.Button(ligne7_frame, text="3", style="Calc.TButton", width=6)
    btn28 = ttk.Button(ligne7_frame, text="/", style="Calc.TButton", width=6)

    btn25.pack(side="left", padx=2)
    btn26.pack(side="left", padx=2)
    btn27.pack(side="left", padx=2)
    btn28.pack(side="left", padx=2)

    # Ligne 8 : Chiffres 0, décimal et opérations finales
    ligne8_frame = Frame(main_frame, bg=PALETTE["fond_principal"])
    ligne8_frame.pack(pady=3)

    btn29 = ttk.Button(ligne8_frame, text="0", style="Calc.TButton", width=6)
    btn30 = ttk.Button(ligne8_frame, text=".", style="Calc.TButton", width=6)
    btn31 = ttk.Button(ligne8_frame, text="×", style="Calc.TButton", width=6)
    btn32 = ttk.Button(ligne8_frame, text="=", style="Calc.TButton", width=6)

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
            
            label3.config(text="✅ Calcul réussi", fg=PALETTE["succes"])
        except Exception as e:
            label3.config(text=f"❌ Erreur : {str(e)[:30]}...", fg=PALETTE["erreur"])
            entree.config(state=NORMAL)
            entree.delete("1.0", END)
            entree.config(state=DISABLED)

    def remise_a_blanc():
        nonlocal valeur_absolue_ouverte
        entree.config(state=NORMAL)
        entree.delete("1.0", END)
        entree.config(state=DISABLED)
        valeur_absolue_ouverte = False
        label3.config(text="", fg=PALETTE["texte_clair"])

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

    # Informations d'utilisation
    frame_info = Frame(operation, bg=PALETTE["fond_principal"])
    frame_info.pack(pady=10, padx=20, fill=X)
    
    Label(frame_info, text="💡 Calculatrice scientifique complète",
          font=("Century Gothic", 10, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0,5))
    
    infos = [
        "• Supporte les fonctions trigonométriques, logarithmiques, etc.",
        "• Utilisez 'rad()' pour convertir les degrés en radians",
        "• 'ESC' pour effacer • '←' pour supprimer le dernier caractère"
    ]
    
    for info in infos:
        Label(frame_info, text=info, font=("Century Gothic", 8),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w").pack(fill="x", pady=1)

    # Bouton Quitter
    frame_quitter = Frame(operation, bg=PALETTE["fond_principal"])
    frame_quitter.pack(pady=15)
    
    btn_quitter = ttk.Button(frame_quitter, text="🚪 Quitter", style="Quit.TButton", 
                           command=operation.destroy)
    btn_quitter.pack()