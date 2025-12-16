"""
equation_numerique.py - Interface pour la résolution d'équations numériques
Auteur: MathCraft
Description: Interface Tkinter pour les méthodes de résolution d'équations
"""

from tkinter import *
from tkinter import ttk
import re
import math
import csv
from math import factorial
from tkinter import filedialog, messagebox
from . import modules as modu

# Palette unifiée
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
    "table_header": "#E2E8F0",
    "table_odd": "#F8FAFC",
    "table_even": "#FFFFFF"
}

# Liste des méthodes disponibles
METHODES = [
    "Dichotomie",
    "Newton-Raphson",
    "Point Fixe",
    "Sécante",
    "Regula Falsi",
    "Müller",
    "Steffensen",
    "Brent",
    "Ridders"
]

# Description des méthodes
DESCRIPTION_METHODES = {
    "Dichotomie": {
        "description": "Méthode de dichotomie (bissection)",
        "convergence": "Linéaire (1/2^n)",
        "precision": "Bonne",
        "robustesse": "Très robuste",
        "prerequis": "f(a)*f(b) < 0"
    },
    "Newton-Raphson": {
        "description": "Méthode de Newton-Raphson",
        "convergence": "Quadratique",
        "precision": "Excellente",
        "robustesse": "Moyenne (nécessite dérivée)",
        "prerequis": "Dérivée f'(x)"
    },
    "Point Fixe": {
        "description": "Méthode du point fixe",
        "convergence": "Linéaire",
        "precision": "Variable",
        "robustesse": "Moyenne",
        "prerequis": "Fonction g(x) = x"
    },
    "Sécante": {
        "description": "Méthode de la sécante",
        "convergence": "Super-linéaire (≈1.618)",
        "precision": "Très bonne",
        "robustesse": "Bonne",
        "prerequis": "Deux points initiaux"
    },
    "Regula Falsi": {
        "description": "Méthode de la fausse position",
        "convergence": "Super-linéaire",
        "precision": "Bonne",
        "robustesse": "Très robuste",
        "prerequis": "f(a)*f(b) < 0"
    },
    "Müller": {
        "description": "Méthode de Müller",
        "convergence": "Super-linéaire",
        "precision": "Excellente",
        "robustesse": "Bonne",
        "prerequis": "Trois points initiaux"
    },
    "Steffensen": {
        "description": "Méthode de Steffensen",
        "convergence": "Quadratique",
        "precision": "Excellente",
        "robustesse": "Moyenne",
        "prerequis": "Fonction de point fixe"
    },
    "Brent": {
        "description": "Algorithme de Brent",
        "convergence": "Super-linéaire",
        "precision": "Excellente",
        "robustesse": "Très robuste",
        "prerequis": "f(a)*f(b) < 0"
    },
    "Ridders": {
        "description": "Méthode de Ridders",
        "convergence": "Quadratique",
        "precision": "Excellente",
        "robustesse": "Très robuste",
        "prerequis": "f(a)*f(b) < 0"
    }
}


def prepare_expression(expr: str) -> str:
    """Prépare l'expression mathématique pour évaluation"""
    expr = expr.replace(" ", "")
    
    # Valeur absolue
    while "|" in expr:
        debut = expr.find("|")
        fin = expr.find("|", debut + 1)
        if fin == -1:
            expr = expr.replace("|", "", 1)
        else:
            contenu = expr[debut + 1:fin]
            expr = expr[:debut] + f"abs({contenu})" + expr[fin + 1:]
    
    # Multiplication implicite
    expr = re.sub(r"(\d)(π)", r"\1*π", expr)
    expr = re.sub(r"(\d)(√)", r"\1*√", expr)
    expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)
    
    # Remplacements
    expr = expr.replace("π", "pi")
    expr = expr.replace("√", "sqrt")
    expr = expr.replace("^", "**")
    expr = expr.replace("%", "/100")
    expr = re.sub(r"(\d+)!", r"factorial(\1)", expr)
    
    return expr


def equilibrer_parentheses(expr: str) -> str:
    """Équilibre les parenthèses"""
    ouvert = expr.count("(")
    ferme = expr.count(")")
    manque = ouvert - ferme
    if manque > 0:
        expr += ")" * manque
    return expr


def preparer_fonction(fonction_text):
    """Prépare et nettoie la fonction mathématique"""
    try:
        intermediaire = prepare_expression(str(fonction_text))
        arrange_parenthese = equilibrer_parentheses(intermediaire)
        
        def ma_fonction(x):
            try:
                env = {
                    "sin": math.sin, "cos": math.cos, "tan": math.tan,
                    "asin": math.asin, "acos": math.acos, "atan": math.atan,
                    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
                    "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
                    "exp": math.exp, "pow": math.pow,
                    "pi": math.pi, "e": math.e, "abs": abs,
                    "factorial": factorial
                }
                namespace = {"x": x}
                namespace.update(env)
                return eval(arrange_parenthese, {"__builtins__": {}}, namespace)
            except Exception as e:
                raise ValueError(f"Erreur lors de l'évaluation: {str(e)}")
        
        return ma_fonction
    except Exception as e:
        raise ValueError(f"Erreur dans la fonction : {str(e)}")


def calculer_derivee_numerique(f, x, h=1e-5):
    """Calcule la dérivée numérique de f en x"""
    return (f(x + h) - f(x - h)) / (2 * h)


def executer_methode(methode, params):
    """Exécute la méthode de résolution sélectionnée"""
    methodes_fonctions = {
        "Dichotomie": lambda: modu.racineDichotomie(
            params['a'], params['b'], params['epsilon'], params['f']
        ),
        "Newton-Raphson": lambda: modu.racineNewton(
            params['f'], params['df'], params['x0'], params['epsilon']
        ),
        "Point Fixe": lambda: modu.racinePointFixe(
            params['g'], params['x0'], params['epsilon']
        ),
        "Sécante": lambda: modu.racineSecante(
            params['f'], params['x0'], params['x1'], params['epsilon']
        ),
        "Regula Falsi": lambda: modu.racineRegulaFalsi(
            params['f'], params['a'], params['b'], params['epsilon']
        ),
        "Müller": lambda: modu.racineMuller(
            params['f'], params['x0'], params['x1'], params['x2'], params['epsilon']
        ),
        "Steffensen": lambda: modu.racineSteffensen(
            params['g'], params['x0'], params['epsilon']
        ),
        "Brent": lambda: modu.racineBrent(
            params['f'], params['a'], params['b'], params['epsilon']
        ),
        "Ridders": lambda: modu.racineRidders(
            params['f'], params['a'], params['b'], params['epsilon']
        )
    }
    
    if methode not in methodes_fonctions:
        raise ValueError(f"Méthode inconnue : {methode}")
    
    return methodes_fonctions[methode]()


def afficher_iterations(iterations, methode, notebook, fenetre):
    """Affiche les itérations dans un onglet du notebook"""
    
    # Créer un nouvel onglet pour les itérations
    frame_iterations = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_iterations, text="📊 Itérations")
    
    # Titre
    Label(frame_iterations, text=f"Détails des itérations - {methode}",
          font=("Century Gothic", 14, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=10)
    
    # Statistiques
    stats_frame = Frame(frame_iterations, bg=PALETTE["fond_principal"])
    stats_frame.pack(pady=5, fill=X, padx=20)
    
    Label(stats_frame, text=f"Nombre d'itérations: {len(iterations)}",
          font=("Century Gothic", 10, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"]).pack(side=LEFT, padx=10)
    
    if iterations:
        derniere_iter = iterations[-1]
        if 'erreur' in derniere_iter:
            Label(stats_frame, text=f"Erreur finale: {derniere_iter['erreur']:.2e}",
                  font=("Century Gothic", 10, "bold"),
                  bg=PALETTE["fond_principal"],
                  fg=PALETTE["succes"]).pack(side=LEFT, padx=10)
    
    # Frame pour le tableau
    table_frame = Frame(frame_iterations, bg=PALETTE["fond_principal"])
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    # Créer un canvas avec scrollbar
    canvas = Canvas(table_frame, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar_y = Scrollbar(table_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar_x = Scrollbar(table_frame, orient=HORIZONTAL, command=canvas.xview)
    
    scrollable_frame = Frame(canvas, bg=PALETTE["fond_principal"])
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    
    # Pack les éléments de scroll
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    
    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0, weight=1)
    
    # Déterminer les colonnes en fonction de la méthode
    if methode == "Dichotomie":
        headers = ["Itér.", "a", "b", "c", "f(a)", "f(c)", "Intervalle", "Erreur"]
        col_keys = ['iteration', 'a', 'b', 'c', 'f(a)', 'f(c)', 'intervalle', 'erreur']
    elif methode == "Newton-Raphson":
        headers = ["Itér.", "x_n", "f(x_n)", "f'(x_n)", "Erreur"]
        col_keys = ['iteration', 'x_n', 'f(x_n)', "f'(x_n)", 'erreur']
    elif methode == "Sécante":
        headers = ["Itér.", "x_{n-1}", "x_n", "x_{n+1}", "f(x_n)", "Erreur"]
        col_keys = ['iteration', 'x_{n-1}', 'x_n', 'x_{n+1}', 'f(x_n)', 'erreur']
    elif methode == "Regula Falsi":
        headers = ["Itér.", "a", "b", "c", "f(c)", "Intervalle", "Erreur"]
        col_keys = ['iteration', 'a', 'b', 'c', 'f(c)', 'intervalle', 'erreur']
    else:
        # Colonnes génériques
        headers = ["Itération"]
        col_keys = ['iteration']
        if iterations:
            for key in iterations[0].keys():
                if key != 'iteration' and key != 'type':
                    headers.append(key.capitalize())
                    col_keys.append(key)
    
    col_widths = [80] + [120] * (len(headers) - 1)
    
    # Créer les en-têtes
    for col_idx, (header, width) in enumerate(zip(headers, col_widths)):
        header_label = Label(scrollable_frame, text=header, 
                            font=("Century Gothic", 9, "bold"),
                            bg=PALETTE["table_header"],
                            fg=PALETTE["texte_fonce"],
                            relief="solid",
                            borderwidth=1,
                            padx=10,
                            pady=5,
                            width=15)
        header_label.grid(row=0, column=col_idx, sticky="nsew")
    
    # Remplir le tableau avec les données
    for row_idx, iter_data in enumerate(iterations):
        # Alterner les couleurs des lignes
        bg_color = PALETTE["table_even"] if (row_idx + 1) % 2 == 0 else PALETTE["table_odd"]
        
        values = []
        for key in col_keys:
            value = iter_data.get(key, '')
            if isinstance(value, (int, float)):
                if abs(value) < 1e-10:
                    values.append("0.0000")
                elif abs(value) > 1e10:
                    values.append(f"{value:.4e}")
                else:
                    values.append(f"{value:.8f}")
            else:
                values.append(str(value))
        
        # Créer les cellules pour cette ligne
        for col_idx, (value, width) in enumerate(zip(values, col_widths)):
            cell = Label(scrollable_frame, text=value,
                        font=("Century Gothic", 8),
                        bg=bg_color,
                        fg=PALETTE["texte_fonce"],
                        relief="solid",
                        borderwidth=1,
                        padx=10,
                        pady=5,
                        width=15,
                        anchor="center")
            cell.grid(row=row_idx + 1, column=col_idx, sticky="nsew")
    
    # Configurer les poids des colonnes
    for col_idx in range(len(headers)):
        scrollable_frame.grid_columnconfigure(col_idx, weight=1)
    
    # Boutons d'action
    button_frame = Frame(frame_iterations, bg=PALETTE["fond_principal"])
    button_frame.pack(pady=10, fill=X, padx=20)
    
    def exporter_csv():
        """Exporte les itérations en CSV"""
        try:
            fichier = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Exporter les itérations"
            )
            
            if fichier:
                with open(fichier, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    for iter_data in iterations:
                        row = []
                        for key in col_keys:
                            value = iter_data.get(key, '')
                            if isinstance(value, (int, float)):
                                row.append(f"{value:.10f}")
                            else:
                                row.append(str(value))
                        writer.writerow(row)
                
                messagebox.showinfo("Export réussi", 
                                  f"Les itérations ont été exportées dans :\n{fichier}")
        except Exception as e:
            messagebox.showerror("Erreur d'export", f"Erreur lors de l'export : {str(e)}")
    
    ttk.Button(button_frame, text="📥 Exporter en CSV", 
              command=exporter_csv).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="Fermer cet onglet", 
              command=lambda: notebook.forget(frame_iterations)).pack(side=LEFT, padx=5)
    
    # Configurer la taille minimale pour le scroll
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    return frame_iterations


def _is_toplevel_parent(parent):
    import tkinter as tk
    return parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))


def lancer_equation_Numerique(parent=None):
    """
    Ouvre une nouvelle fenêtre pour la résolution d'équations numériques.
    
    Args:
        parent: Fenêtre parente (optionnel)
    
    Returns:
        Tk ou Toplevel: La fenêtre de résolution d'équations
    """
    
    # Variables
    var_f = StringVar()
    var_g = StringVar()
    var_df = StringVar()
    var_a = StringVar()
    var_b = StringVar()
    var_x0 = StringVar()
    var_x1 = StringVar()
    var_x2 = StringVar()
    var_epsilon = StringVar(value="1e-6")
    var_max_iter = StringVar(value="1000")
    
    # Variable pour suivre l'onglet d'itérations
    current_iterations_tab = None
    
    # Initialisation de la fenêtre / zone de contenu
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre = Toplevel(parent) if parent else Tk()
        fenetre.configure(bg=PALETTE["fond_principal"])
        fenetre.geometry("1100x800")
        fenetre.title("Résolution d'Équations Numériques")
        fenetre.resizable(True, True)
        # Centrer la fenêtre
        if parent:
            fenetre.transient(parent)
            fenetre.grab_set()
    else:
        fenetre = parent
        for w in list(fenetre.winfo_children()):
            w.destroy()
        try:
            fenetre.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass
    
    # Configuration du style
    def configurer_style():
        style = ttk.Style()
        style.theme_use("clam")
        
        # Style pour les onglets
        style.configure("TNotebook", background=PALETTE["fond_principal"])
        style.configure("TNotebook.Tab", 
                       font=("Century Gothic", 10),
                       padding=[10, 5])
        
        # Style pour les boutons
        style.configure("Custom.TButton",
                        foreground=PALETTE["fond_secondaire"],
                        background=PALETTE["primaire"],
                        font=("Century Gothic", 10, "bold"),
                        padding=6,
                        relief="flat")
        
        style.configure("Quit.TButton",
                        foreground=PALETTE["fond_secondaire"],
                        background=PALETTE["erreur"],
                        font=("Century Gothic", 10, "bold"),
                        padding=6,
                        relief="flat")
        
        # Effets de survol
        style.map("Custom.TButton",
                 background=[('active', PALETTE["secondaire"]),
                            ('pressed', '#1E3A8A')])
        
        style.map("Quit.TButton",
                 background=[('active', '#B91C1C'),
                            ('pressed', '#991B1B')])
        
        return style
    
    style = configurer_style()
    
    # Créer un notebook (onglets)
    notebook = ttk.Notebook(fenetre)
    notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # ==============================
    # ONGLET 1: Calcul
    # ==============================
    frame_calcul = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_calcul, text="🧮 Calcul")
    
    # Conteneur principal avec scrollbar
    main_container = Frame(frame_calcul, bg=PALETTE["fond_principal"])
    main_container.pack(fill=BOTH, expand=True)
    
    canvas = Canvas(main_container, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=PALETTE["fond_principal"])
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Fonction pour le scroll avec la molette
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    # ========== CONTENU DE L'ONGLET CALCUL ==========
    
    # Titre
    Label(scrollable_frame, text="🔢 RÉSOLUTION D'ÉQUATIONS NUMÉRIQUES",
          font=("Century Gothic", 20, "bold"), fg=PALETTE["primaire"], 
          bg=PALETTE["fond_principal"]).pack(pady=20)
    
    # Sélection de la méthode
    Label(scrollable_frame, text="Choisissez une méthode :",
          font=("Century Gothic", 12, "bold"), fg=PALETTE["texte_fonce"], 
          bg=PALETTE["fond_principal"]).pack(pady=10)
    
    combo_methode = ttk.Combobox(scrollable_frame, font=("Century Gothic", 11),
                                 values=METHODES, state="readonly", width=30)
    combo_methode.pack(pady=5)
    combo_methode.set("=== Sélectionnez une méthode ===")
    
    # Frame pour la description de la méthode
    frame_desc = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_desc.pack(pady=10, fill=X, padx=50)
    
    label_desc = Label(frame_desc, text="", font=("Century Gothic", 10),
                      bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
                      wraplength=600, justify=LEFT)
    label_desc.pack()
    
    def update_description(event):
        methode = combo_methode.get()
        if methode in DESCRIPTION_METHODES:
            desc = DESCRIPTION_METHODES[methode]
            text = f"📖 {desc['description']}\n"
            text += f"📈 Convergence: {desc['convergence']}\n"
            text += f"🎯 Précision: {desc['precision']}\n"
            text += f"🛡️ Robustesse: {desc['robustesse']}\n"
            text += f"⚠️ Prérequis: {desc['prerequis']}"
            label_desc.config(text=text)
        else:
            label_desc.config(text="")
    
    combo_methode.bind("<<ComboboxSelected>>", update_description)
    
    # Section pour les fonctions
    frame_fonctions = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_fonctions.pack(pady=20, fill=X, padx=50)
    
    # Fonction f(x)
    Label(frame_fonctions, text="Fonction f(x) [f(x)=0] :",
          font=("Century Gothic", 11, "bold"), fg=PALETTE["texte_fonce"], 
          bg=PALETTE["fond_principal"]).pack(anchor="w")
    
    entree_f = Entry(frame_fonctions, font=("Century Gothic", 11), 
                    textvariable=var_f, width=50, relief="solid", borderwidth=1)
    entree_f.pack(pady=5, fill=X)
    
    # Frame pour les paramètres
    frame_params = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_params.pack(pady=20, fill=X, padx=50)
    
    # Fonction pour créer un champ de paramètre
    def create_param_row(parent_frame, label, var_name, default=""):
        frame = Frame(parent_frame, bg=PALETTE["fond_principal"])
        frame.pack(pady=5, fill=X)
        
        Label(frame, text=label + " :", font=("Century Gothic", 10),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
              width=15, anchor="w").pack(side=LEFT)
        
        entry = Entry(frame, font=("Century Gothic", 10), 
                     textvariable=var_name, width=30, relief="solid", borderwidth=1)
        entry.pack(side=LEFT, padx=10)
        
        if default:
            var_name.set(default)
        
        return entry
    
    # Créer les champs de paramètres
    entry_a = create_param_row(frame_params, "Borne a", var_a)
    entry_b = create_param_row(frame_params, "Borne b", var_b)
    entry_x0 = create_param_row(frame_params, "Point initial x0", var_x0)
    entry_x1 = create_param_row(frame_params, "Point x1", var_x1)
    entry_x2 = create_param_row(frame_params, "Point x2", var_x2)
    entry_epsilon = create_param_row(frame_params, "Précision ε", var_epsilon, "1e-6")
    entry_max_iter = create_param_row(frame_params, "Max itérations", var_max_iter, "1000")
    
    # Section pour les fonctions supplémentaires
    frame_fonctions_supp = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_fonctions_supp.pack(pady=20, fill=X, padx=50)
    
    # Fonction g(x) pour point fixe
    Label(frame_fonctions_supp, text="Fonction g(x) [pour point fixe] :",
          font=("Century Gothic", 11), fg=PALETTE["texte_fonce"], 
          bg=PALETTE["fond_principal"]).pack(anchor="w")
    
    entree_g = Entry(frame_fonctions_supp, font=("Century Gothic", 11), 
                    textvariable=var_g, width=50, relief="solid", borderwidth=1)
    entree_g.pack(pady=5, fill=X)
    
    # Fonction f'(x) pour Newton
    Label(frame_fonctions_supp, text="Dérivée f'(x) [pour Newton] :",
          font=("Century Gothic", 11), fg=PALETTE["texte_fonce"], 
          bg=PALETTE["fond_principal"]).pack(anchor="w", pady=(10,0))
    
    entree_df = Entry(frame_fonctions_supp, font=("Century Gothic", 11), 
                     textvariable=var_df, width=50, relief="solid", borderwidth=1)
    entree_df.pack(pady=5, fill=X)
    
    # Boutons d'aide mathématique
    Label(scrollable_frame, text="Raccourcis pour fonctions mathématiques",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], 
          fg=PALETTE["primaire"]).pack(pady=(20, 10))
    
    frame_boutons_math = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_boutons_math.pack(pady=10)
    
    # Ligne 1
    ligne1 = Frame(frame_boutons_math, bg=PALETTE["fond_principal"])
    ligne1.pack(pady=2)
    
    boutons_ligne1 = [
        ("x²", "x**2"),
        ("xⁿ", "x**"),
        ("√x", "sqrt(x)"),
        ("eˣ", "exp(x)"),
        ("ln(x)", "log(x)")
    ]
    
    for text, insert_text in boutons_ligne1:
        btn = ttk.Button(ligne1, text=text, style="Custom.TButton",
                        command=lambda t=insert_text: entree_f.insert(END, t))
        btn.pack(side="left", padx=2)
    
    # Ligne 2
    ligne2 = Frame(frame_boutons_math, bg=PALETTE["fond_principal"])
    ligne2.pack(pady=2)
    
    boutons_ligne2 = [
        ("sin(x)", "sin(x)"),
        ("cos(x)", "cos(x)"),
        ("tan(x)", "tan(x)"),
        ("π", "pi"),
        ("|x|", "abs(x)")
    ]
    
    for text, insert_text in boutons_ligne2:
        btn = ttk.Button(ligne2, text=text, style="Custom.TButton",
                        command=lambda t=insert_text: entree_f.insert(END, t))
        btn.pack(side="left", padx=2)
    
    # Zone de résultat
    frame_resultat = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_resultat.pack(pady=25)
    
    resultat_label = Label(frame_resultat, text="Résultat apparaîtra ici",
                          font=("Century Gothic", 14, "bold"), 
                          fg=PALETTE["texte_clair"], bg=PALETTE["fond_principal"])
    resultat_label.pack()
    
    # Fonction principale de calcul
    def calculer():
        nonlocal current_iterations_tab
        
        try:
            methode = combo_methode.get()
            
            if methode == "=== Sélectionnez une méthode ===":
                resultat_label.config(text="❌ Veuillez sélectionner une méthode", 
                                     fg=PALETTE["erreur"])
                return
            
            # Préparation de la fonction f
            if not var_f.get():
                raise ValueError("La fonction f(x) est requise")
            
            f = preparer_fonction(var_f.get())
            
            # Préparation des paramètres selon la méthode
            params = {'f': f, 'epsilon': float(var_epsilon.get())}
            
            # Récupération des paramètres spécifiques
            if methode in ["Dichotomie", "Regula Falsi", "Brent", "Ridders"]:
                if not var_a.get() or not var_b.get():
                    raise ValueError(f"Les bornes a et b sont requises pour {methode}")
                params['a'] = float(var_a.get())
                params['b'] = float(var_b.get())
            
            if methode in ["Newton-Raphson", "Point Fixe", "Steffensen"]:
                if not var_x0.get():
                    raise ValueError(f"Le point initial x0 est requis pour {methode}")
                params['x0'] = float(var_x0.get())
            
            if methode == "Sécante":
                if not var_x0.get() or not var_x1.get():
                    raise ValueError("Les points x0 et x1 sont requis pour la sécante")
                params['x0'] = float(var_x0.get())
                params['x1'] = float(var_x1.get())
            
            if methode == "Müller":
                if not var_x0.get() or not var_x1.get() or not var_x2.get():
                    raise ValueError("Les points x0, x1 et x2 sont requis pour Müller")
                params['x0'] = float(var_x0.get())
                params['x1'] = float(var_x1.get())
                params['x2'] = float(var_x2.get())
            
            if methode == "Newton-Raphson":
                if var_df.get():
                    params['df'] = preparer_fonction(var_df.get())
                else:
                    # Dérivée numérique
                    params['df'] = lambda x: calculer_derivee_numerique(f, x)
            
            if methode in ["Point Fixe", "Steffensen"]:
                if not var_g.get():
                    raise ValueError(f"La fonction g(x) est requise pour {methode}")
                params['g'] = preparer_fonction(var_g.get())
            
            # Exécution de la méthode
            racine, iterations_count, iterations = executer_methode(methode, params)
            
            # Affichage du résultat
            resultat_label.config(text=f"✅ {methode}:\nRacine ≈ {racine:.10f}\n"
                                     f"Itérations: {iterations_count}\n"
                                     f"f(racine) = {f(racine):.2e}",
                                 fg=PALETTE["succes"])
            
            # Supprimer l'ancien onglet d'itérations s'il existe
            if current_iterations_tab is not None:
                try:
                    notebook.forget(current_iterations_tab)
                except:
                    pass
            
            # Créer un nouvel onglet pour afficher les itérations
            current_iterations_tab = afficher_iterations(
                iterations, methode, notebook, fenetre
            )
            
            # Sélectionner l'onglet des itérations
            notebook.select(current_iterations_tab)
            
        except ValueError as e:
            resultat_label.config(text=f"❌ {str(e)}", fg=PALETTE["erreur"])
        except Exception as e:
            resultat_label.config(text=f"❌ Erreur de calcul : {str(e)}", 
                                 fg=PALETTE["erreur"])
    
    # Boutons de contrôle
    frame_boutons = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_boutons.pack(pady=25)
    
    bouton_calculer = ttk.Button(frame_boutons, text="🧮 Résoudre l'équation",
                                style="Custom.TButton", command=calculer)
    bouton_calculer.pack(side="left", padx=10)
    
    bouton_effacer = ttk.Button(frame_boutons, text="🧹 Effacer tout",
                               style="Custom.TButton", 
                               command=lambda: [var.set("") for var in 
                                               [var_f, var_g, var_df, var_a, var_b, 
                                                var_x0, var_x1, var_x2]])
    bouton_effacer.pack(side="left", padx=10)
    
    def _close_local():
        if is_toplevel:
            fenetre.destroy()
        else:
            for w in list(fenetre.winfo_children()):
                w.destroy()
    bouton_quitter = ttk.Button(frame_boutons, text="🚪 Fermer",
                               style="Quit.TButton", command=_close_local)
    bouton_quitter.pack(side="left", padx=10)
    
    # Exemples
    frame_exemples = Frame(scrollable_frame, bg=PALETTE["fond_principal"])
    frame_exemples.pack(pady=20, fill=X, padx=50)
    
    Label(frame_exemples, text="💡 Exemples d'équations :",
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], 
          fg=PALETTE["primaire"]).pack(anchor="w")
    
    exemples = [
        "• x**3 - 2*x - 5 = 0  (Méthode: Dichotomie, a=2, b=3)",
        "• cos(x) - x = 0  (Méthode: Point Fixe, g(x)=cos(x), x0=0.5)",
        "• exp(x) - 3*x = 0  (Méthode: Newton, x0=1)",
        "• x**2 - 2 = 0  (Méthode: Sécante, x0=1, x1=2)"
    ]
    
    for exemple in exemples:
        Label(frame_exemples, text=exemple, font=("Century Gothic", 9),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
              anchor="w").pack(pady=2)
    
    # Espaceur final
    Label(scrollable_frame, text="", bg=PALETTE["fond_principal"], height=3).pack()
    
    # ==============================
    # ONGLET 2: Guide des méthodes
    # ==============================
    frame_guide = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_guide, text="📚 Guide")
    
    # Contenu du guide
    Label(frame_guide, text="Guide des Méthodes Numériques",
          font=("Century Gothic", 16, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=20)
    
    # Canvas pour le guide avec scrollbar
    canvas_guide = Canvas(frame_guide, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar_guide = ttk.Scrollbar(frame_guide, orient="vertical", command=canvas_guide.yview)
    scrollable_guide = Frame(canvas_guide, bg=PALETTE["fond_principal"])
    
    scrollable_guide.bind(
        "<Configure>",
        lambda e: canvas_guide.configure(scrollregion=canvas_guide.bbox("all"))
    )
    
    canvas_guide.create_window((0, 0), window=scrollable_guide, anchor="nw")
    canvas_guide.configure(yscrollcommand=scrollbar_guide.set)
    
    canvas_guide.pack(side="left", fill="both", expand=True)
    scrollbar_guide.pack(side="right", fill="y")
    
    # Contenu du guide
    guide_content = Frame(scrollable_guide, bg=PALETTE["fond_principal"])
    guide_content.pack(fill=BOTH, expand=True, padx=30, pady=20)
    
    # Description détaillée de chaque méthode
    for methode in METHODES:
        desc = DESCRIPTION_METHODES[methode]
        
        # Frame pour chaque méthode
        frame_methode = Frame(guide_content, bg=PALETTE["fond_principal"],
                             relief="solid", borderwidth=1)
        frame_methode.pack(fill=X, pady=10, padx=10)
        
        # Titre de la méthode
        Label(frame_methode, text=f"🔬 {methode}",
              font=("Century Gothic", 12, "bold"),
              bg=PALETTE["fond_principal"],
              fg=PALETTE["primaire"]).pack(anchor="w", pady=(10,5), padx=10)
        
        # Description
        Label(frame_methode, text=desc["description"],
              font=("Century Gothic", 10),
              bg=PALETTE["fond_principal"],
              fg=PALETTE["texte_fonce"],
              wraplength=700,
              justify=LEFT).pack(anchor="w", padx=10)
        
        # Caractéristiques
        caracteristiques = [
            f"📈 Convergence: {desc['convergence']}",
            f"🎯 Précision: {desc['precision']}",
            f"🛡️ Robustesse: {desc['robustesse']}",
            f"⚠️ Prérequis: {desc['prerequis']}"
        ]
        
        for carac in caracteristiques:
            Label(frame_methode, text=carac,
                  font=("Century Gothic", 9),
                  bg=PALETTE["fond_principal"],
                  fg=PALETTE["texte_clair"],
                  anchor="w").pack(anchor="w", padx=20, pady=1)
        
        # Conseils d'utilisation
        if methode == "Dichotomie":
            conseil = "Conseil: Toujours vérifier que f(a)*f(b) < 0"
        elif methode == "Newton-Raphson":
            conseil = "Conseil: La dérivée ne doit pas s'annuler près de la racine"
        elif methode == "Brent":
            conseil = "Conseil: Méthode recommandée pour la robustesse"
        elif methode == "Ridders":
            conseil = "Conseil: Excellente précision et robustesse"
        else:
            conseil = ""
        
        if conseil:
            Label(frame_methode, text=conseil,
                  font=("Century Gothic", 9, "italic"),
                  bg=PALETTE["fond_principal"],
                  fg=PALETTE["secondaire"],
                  anchor="w").pack(anchor="w", padx=20, pady=(5,10))
    
    # ==============================
    # ONGLET 3: À propos
    # ==============================
    frame_apropos = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_apropos, text="ℹ️ À propos")
    
    # Contenu de l'onglet À propos
    Label(frame_apropos, text="Résolution d'Équations Numériques",
          font=("Century Gothic", 16, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=30)
    
    info_text = """
    Cette application permet de résoudre des équations non linéaires
    du type f(x) = 0 à l'aide de différentes méthodes numériques.
    
    📊 Fonctionnalités :
    • 9 méthodes de résolution différentes
    • Affichage détaillé de chaque itération
    • Comparaison des performances
    • Export des résultats en CSV
    • Interface intuitive avec onglets
    
    🎯 Méthodes implémentées :
    1. Dichotomie - Méthode robuste et simple
    2. Newton-Raphson - Convergence rapide (quadratique)
    3. Point Fixe - Pour les équations g(x) = x
    4. Sécante - Alternative à Newton sans dérivée
    5. Regula Falsi - Combinaison dichotomie/sécante
    6. Müller - Méthode par interpolation quadratique
    7. Steffensen - Accélération du point fixe
    8. Brent - Algorithme robuste et efficace
    9. Ridders - Méthode précise avec extrapolation
    
    ⚠️ Conseils généraux :
    • Commencez par Dichotomie ou Brent pour la robustesse
    • Utilisez Newton pour une convergence rapide si la dérivée est disponible
    • Vérifiez toujours les conditions d'application
    • Testez avec différentes valeurs initiales si nécessaire
    
    © MathsCraft - Version 1.0
    """
    
    Label(frame_apropos, text=info_text,
          font=("Century Gothic", 10),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"],
          justify=LEFT).pack(pady=20, padx=50)
    
    # Bouton de fermeture
    def _close_about():
        if is_toplevel:
            fenetre.destroy()
        else:
            for w in list(fenetre.winfo_children()):
                w.destroy()
    ttk.Button(frame_apropos, text="Fermer l'application",
               style="Quit.TButton",
               command=_close_about).pack(pady=20)
    
    return fenetre