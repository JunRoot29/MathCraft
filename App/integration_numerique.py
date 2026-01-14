"""
integration_numerique.py - Interface graphique pour l'intégration numérique avec affichage des itérations
Auteur: Junior Kossivi
Description: Interface Tkinter pour les méthodes d'intégration numérique avec affichage direct des itérations
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

# Liste des méthodes d'intégration disponibles
donnees = ["Rectangle Retrograde", "Rectangle progressif", "Rectangle Centré",
           "Trapèzes Composite", "Trapèzes Simples", "Simpson Simple", "Simpson Composite"]


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


# ======================================================================================
# Fonctions utilitaires pour l'interface
# ======================================================================================

def inserer_texte(texte, widget):
    """Insère du texte à la position actuelle du curseur"""
    position = widget.index(INSERT)
    widget.insert(position, texte)
    widget.focus_set()


def supprimer_caractere(widget):
    """Supprime le caractère précédent le curseur"""
    position = widget.index(INSERT)
    if position > 0:
        widget.delete(position - 1, position)
    widget.focus_set()


def valider_et_convertir_donnees(a, b, n, fonction_text):
    """Valide et convertit toutes les données d'entrée"""
    # Validation des champs vides
    if not a or str(a).strip() == "":
        raise ValueError("La borne inférieure (a) est requise")
    if not b or str(b).strip() == "":
        raise ValueError("La borne supérieure (b) est requise")
    if not n or str(n).strip() == "":
        raise ValueError("Le nombre de subdivisions (n) est requis")
    if not fonction_text or str(fonction_text).strip() == "":
        raise ValueError("La fonction est requise")
    
    # Conversion des nombres
    try:
        a_val = float(str(a).strip())
        b_val = float(str(b).strip())
        n_val = int(str(n).strip())
    except ValueError:
        raise ValueError("Les valeurs a, b doivent être des nombres et n un entier positif")
    
    # Validation des valeurs
    if n_val <= 0:
        raise ValueError("n doit être un entier positif")
    if a_val >= b_val:
        raise ValueError("La borne a doit être inférieure à b")
    
    return a_val, b_val, n_val


def preparer_fonction(fonction_text):
    """Prépare et nettoie la fonction mathématique"""
    try:
        intermediaire = prepare_expression(str(fonction_text))
        arrange_parenthese = equilibrer_parentheses(intermediaire)
        
        def ma_fonction(x):
            try:
                env = {
                    "sin": math.sin, "cos": math.cos, "tan": math.tan,
                    "sqrt": math.sqrt, "log": math.log, "exp": math.exp,
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


def executer_methode(choix, a, b, n, fonction):
    """Exécute la méthode d'intégration sélectionnée"""
    methodes = {
        "Rectangle Retrograde": modu.intRectangleRetro,
        "Rectangle progressif": modu.intRectanglePro,
        "Rectangle Centré": modu.intRectangleCentre,
        "Trapèzes Composite": modu.intTrapezeC,
        "Trapèzes Simples": modu.intTrapezeS,
        "Simpson Simple": modu.intSimpsonS,
        "Simpson Composite": modu.intSimpsonC,
    }
    
    if choix not in methodes:
        raise ValueError(f"Méthode inconnue : {choix}")
    
    # Appel de la méthode qui retourne maintenant (resultat, iterations)
    return methodes[choix](fonction, a, b, n)


# Helper pour savoir si on doit créer une Toplevel ou utiliser un Frame parent
def _is_toplevel_parent(parent):
    import tkinter as tk
    return parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))


def afficher_iterations_dans_interface(iterations, methode, notebook, fenetre):
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
        if 'somme_partielle' in derniere_iter:
            Label(stats_frame, text=f"Valeur finale: {derniere_iter['somme_partielle']:.8f}",
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
    
    # Déterminer les colonnes en fonction du type de méthode
    methode_lower = methode.lower()
    
    if "rectangle" in methode_lower:
        headers = ["Itération", "xi", "f(xi)", "Largeur (h)", "Aire rectangle", "Somme partielle"]
        col_widths = [80, 120, 120, 100, 120, 120]
    elif "trapeze" in methode_lower:
        if "simple" in methode_lower:
            headers = ["Itération", "a", "f(a)", "b", "f(b)", "Largeur", "Aire totale"]
            col_widths = [80, 120, 120, 120, 120, 100, 120]
        else:
            headers = ["Itération", "xi", "f(xi)", "Aire trapèze", "Somme partielle"]
            col_widths = [80, 120, 120, 120, 120]
    elif "simpson" in methode_lower:
        headers = ["Itération", "xi", "f(xi)", "Coefficient", "Contribution", "Somme partielle"]
        col_widths = [80, 120, 120, 100, 120, 120]
    else:
        headers = ["Itération", "xi", "f(xi)", "Somme partielle"]
        col_widths = [80, 120, 120, 120]
    
    # Créer les en-têtes
    for col_idx, (header, width) in enumerate(zip(headers, col_widths)):
        header_label = Label(scrollable_frame, text=header, 
                            font=("Century Gothic", 10, "bold"),
                            bg=PALETTE["table_header"],
                            fg=PALETTE["texte_fonce"],
                            relief="solid",
                            borderwidth=1,
                            padx=10,
                            pady=5,
                            width=width//10)
        header_label.grid(row=0, column=col_idx, sticky="nsew")
    
    # Remplir le tableau avec les données
    for row_idx, iter_data in enumerate(iterations, 1):
        # Alterner les couleurs des lignes
        bg_color = PALETTE["table_even"] if row_idx % 2 == 0 else PALETTE["table_odd"]
        
        if "rectangle" in methode_lower:
            values = [
                str(iter_data['iteration']),
                f"{iter_data['xi']:.6f}",
                f"{iter_data['f(xi)']:.6f}",
                f"{iter_data.get('largeur', 0):.6f}",
                f"{iter_data.get('aire_rectangle', 0):.6f}",
                f"{iter_data.get('somme_partielle', 0):.6f}"
            ]
        elif "trapeze" in methode_lower and "simple" in methode_lower:
            values = [
                str(iter_data['iteration']),
                f"{iter_data.get('a', 0):.6f}",
                f"{iter_data.get('f(a)', 0):.6f}",
                f"{iter_data.get('b', 0):.6f}",
                f"{iter_data.get('f(b)', 0):.6f}",
                f"{iter_data.get('largeur', 0):.6f}",
                f"{iter_data.get('aire', 0):.6f}"
            ]
        elif "trapeze" in methode_lower:
            values = [
                str(iter_data['iteration']),
                f"{iter_data['xi']:.6f}",
                f"{iter_data['f(xi)']:.6f}",
                f"{iter_data.get('aire_trapeze', 0):.6f}",
                f"{iter_data.get('somme_partielle', 0):.6f}"
            ]
        elif "simpson" in methode_lower:
            values = [
                str(iter_data['iteration']),
                f"{iter_data['xi']:.6f}",
                f"{iter_data['f(xi)']:.6f}",
                str(iter_data.get('coefficient', 1)),
                f"{iter_data.get('contribution', 0):.6f}",
                f"{iter_data.get('somme_partielle', 0):.6f}"
            ]
        else:
            values = [
                str(iter_data.get('iteration', '')),
                f"{iter_data.get('xi', 0):.6f}",
                f"{iter_data.get('f(xi)', 0):.6f}",
                f"{iter_data.get('somme_partielle', 0):.6f}"
            ]
        
        # Créer les cellules pour cette ligne
        for col_idx, (value, width) in enumerate(zip(values, col_widths)):
            cell = Label(scrollable_frame, text=value,
                        font=("Century Gothic", 9),
                        bg=bg_color,
                        fg=PALETTE["texte_fonce"],
                        relief="solid",
                        borderwidth=1,
                        padx=10,
                        pady=5,
                        width=width//10,
                        anchor="center")
            cell.grid(row=row_idx, column=col_idx, sticky="nsew")
    
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
                        for header in headers:
                            if header == "Itération":
                                row.append(iter_data.get('iteration', ''))
                            elif header == "xi":
                                row.append(f"{iter_data.get('xi', 0):.6f}")
                            elif header == "f(xi)":
                                row.append(f"{iter_data.get('f(xi)', 0):.6f}")
                            elif header in ["Largeur (h)", "Largeur"]:
                                row.append(f"{iter_data.get('largeur', 0):.6f}")
                            elif header == "Aire rectangle":
                                row.append(f"{iter_data.get('aire_rectangle', 0):.6f}")
                            elif header in ["Aire trapèze", "Aire totale", "Aire"]:
                                row.append(f"{iter_data.get('aire', iter_data.get('aire_trapeze', 0)):.6f}")
                            elif header in ["a", "f(a)", "b", "f(b)"]:
                                row.append(f"{iter_data.get(header.lower(), 0):.6f}")
                            elif header == "Coefficient":
                                row.append(iter_data.get('coefficient', 1))
                            elif header == "Contribution":
                                row.append(f"{iter_data.get('contribution', 0):.6f}")
                            elif header == "Somme partielle":
                                row.append(f"{iter_data.get('somme_partielle', 0):.6f}")
                            else:
                                row.append("")
                        writer.writerow(row)
                
                messagebox.showinfo("Export réussi", 
                                  f"Les itérations ont été exportées dans :\n{fichier}")
        except Exception as e:
            messagebox.showerror("Erreur d'export", f"Erreur lors de l'export : {str(e)}")
    
    ttk.Button(button_frame, text="📥 Exporter en CSV", 
              style="Jeu.TButton", command=exporter_csv).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="Fermer cet onglet", 
              style="Jeu.TButton", command=lambda: notebook.forget(frame_iterations)).pack(side=LEFT, padx=5)
    
    # Configurer la taille minimale pour le scroll
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Retourner l'onglet créé
    return frame_iterations


# ======================================================================================
# Interface principale avec notebook
# ======================================================================================

def lancer_integration_numerique(parent=None):
    """
    Ouvre une nouvelle fenêtre pour effectuer une intégration numérique.
    
    Args:
        parent: Fenêtre parente (optionnel)
    
    Returns:
        Tk ou Toplevel: La fenêtre d'intégration numérique
    """
    
    # Variables associées aux champs d'entrée
    var_a = StringVar()
    var_b = StringVar()
    var_n = StringVar()
    var_f = StringVar()
    
    # Variable pour suivre l'onglet d'itérations actuel
    current_iterations_tab = None
    
    # Initialisation de la fenêtre / zone de contenu
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre_integration = Toplevel(parent) if parent else Tk()
        fenetre_integration.configure(bg=PALETTE["fond_principal"])
        fenetre_integration.geometry("1000x800")  # Plus large pour accommoder le notebook
        fenetre_integration.title("Intégration Numérique avec Itérations")
        fenetre_integration.resizable(True, True)
        # Centrer la fenêtre
        if parent:
            fenetre_integration.transient(parent)
            fenetre_integration.grab_set()
    else:
        fenetre_integration = parent
        for w in list(fenetre_integration.winfo_children()):
            w.destroy()
        try:
            fenetre_integration.configure(bg=PALETTE["fond_principal"])
        except Exception:
            pass
    
    # Configuration du style
    def configurer_style():
        try:
            from .styles import ensure_styles_configured
            ensure_styles_configured(PALETTE)
        except Exception:
            pass
        style = ttk.Style()
        
        # Style pour les onglets
        style.configure("TNotebook", background=PALETTE["fond_principal"])
        style.configure("TNotebook.Tab", 
                       font=("Century Gothic", 10),
                       padding=[10, 5])
        
        # Style pour les boutons (scope local au module)
        style.configure("Integration.Custom.TButton",
                        foreground=PALETTE["fond_secondaire"],
                        background=PALETTE["primaire"],
                        font=("Century Gothic", 9, "bold"),
                        padding=4,
                        relief="flat",
                        width=18)
        
        style.configure("Integration.Quit.TButton",
                        foreground=PALETTE["fond_secondaire"],
                        background=PALETTE["erreur"],
                        font=("Century Gothic", 10, "bold"),
                        padding=6,
                        relief="flat")

        # Style pour petits boutons (raccourcis)
        style.configure("Integration.Small.TButton",
                        foreground=PALETTE["fond_secondaire"],
                        background=PALETTE["primaire"],
                        font=("Century Gothic", 9),
                        padding=2,
                        relief="flat",
                        width=8)
        
        # Effets de survol
        style.map("Integration.Custom.TButton",
                 background=[('active', PALETTE["secondaire"]),
                            ('pressed', '#1E3A8A')])
        style.map("Integration.Small.TButton",
                 background=[('active', PALETTE["secondaire"]),
                            ('pressed', '#1E3A8A')])
        
        style.map("Integration.Quit.TButton",
                 background=[('active', '#B91C1C'),
                            ('pressed', '#991B1B')])
        
        return style
    
    style = configurer_style()
    
    # Créer un notebook (onglets)
    notebook = ttk.Notebook(fenetre_integration)
    notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # ==============================
    # ONGLET 1: Calcul
    # ==============================
    frame_calcul = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_calcul, text="🧮 Calcul")
    
    # Titre
    header_frame = Frame(frame_calcul, bg=PALETTE["fond_principal"])
    header_frame.pack(fill="x", pady=20)
    
    Label(header_frame, text="📈 INTÉGRATION NUMÉRIQUE",
          font=("Century Gothic", 20, "bold"), fg=PALETTE["primaire"], bg=PALETTE["fond_principal"]).pack()
    Label(header_frame, text="Choisissez une méthode d'intégration",
          font=("Century Gothic", 12), fg=PALETTE["texte_clair"], bg=PALETTE["fond_principal"]).pack(pady=5)
    
    # Menu déroulant pour choisir la méthode
    combo = ttk.Combobox(header_frame, font=("Century Gothic", 12),
                         values=donnees, state="readonly", width=30)
    combo.pack(pady=10)
    combo.set("=== Sélectionnez une méthode ===")
    
    # Cadre pour le contenu avec scrollbar
    main_calc_frame = Frame(frame_calcul, bg=PALETTE["fond_principal"])
    main_calc_frame.pack(fill=BOTH, expand=True, padx=20)
    
    canvas_calc = Canvas(main_calc_frame, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar_calc = ttk.Scrollbar(main_calc_frame, orient="vertical", command=canvas_calc.yview)
    scrollable_calc_frame = Frame(canvas_calc, bg=PALETTE["fond_principal"])
    
    scrollable_calc_frame.bind(
        "<Configure>",
        lambda e: canvas_calc.configure(scrollregion=canvas_calc.bbox("all"))
    )
    
    canvas_calc.create_window((0, 0), window=scrollable_calc_frame, anchor="nw")
    canvas_calc.configure(yscrollcommand=scrollbar_calc.set)
    
    canvas_calc.pack(side="left", fill="both", expand=True)
    scrollbar_calc.pack(side="right", fill="y")
    
    def _on_mouse_wheel(event):
        canvas_calc.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas_calc.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    # ========== CONTENU DE L'ONGLET CALCUL ==========
    
    # Section fonction
    Label(scrollable_calc_frame, text="Fonction à intégrer (ex: x**2, sin(x), cos(x)*x)",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"]).pack(pady=10)
    
    entree_f = Entry(scrollable_calc_frame, font=("Century Gothic", 12), textvariable=var_f, width=40, 
                    relief="solid", borderwidth=1)
    entree_f.pack(padx=20, pady=5)
    
    # Section paramètres
    frame_params = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_params.pack(pady=15)
    
    # Paramètre a
    frame_a = Frame(frame_params, bg=PALETTE["fond_principal"])
    frame_a.pack(pady=8)
    Label(frame_a, text="Borne inférieure (a) :", font=("Century Gothic", 11), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"]).pack(side="left")
    entree_a = Entry(frame_a, font=("Century Gothic", 11), textvariable=var_a, width=15, relief="solid", borderwidth=1)
    entree_a.pack(side="left", padx=10)
    
    # Paramètre b
    frame_b = Frame(frame_params, bg=PALETTE["fond_principal"])
    frame_b.pack(pady=8)
    Label(frame_b, text="Borne supérieure (b) :", font=("Century Gothic", 11), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"]).pack(side="left")
    entree_b = Entry(frame_b, font=("Century Gothic", 11), textvariable=var_b, width=15, relief="solid", borderwidth=1)
    entree_b.pack(side="left", padx=10)
    
    # Paramètre n
    frame_n = Frame(frame_params, bg=PALETTE["fond_principal"])
    frame_n.pack(pady=8)
    Label(frame_n, text="Subdivisions (n) :", font=("Century Gothic", 11), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"]).pack(side="left")
    entree_n = Entry(frame_n, font=("Century Gothic", 11), textvariable=var_n, width=15, relief="solid", borderwidth=1)
    entree_n.pack(side="left", padx=10)
    
    # Boutons d'aide mathématique
    Label(scrollable_calc_frame, text="Raccourcis pour fonctions mathématiques",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(20, 10))
    
    frame_boutons = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_boutons.pack(pady=10)
    
    # Ligne 1
    ligne1 = Frame(frame_boutons, bg=PALETTE["fond_principal"])
    ligne1.pack(pady=3)
    
    boutons_ligne1 = [
        ("x²", "x**2"),
        ("xⁿ", "x**"),
        ("√x", "sqrt(x)"),
        ("(", "("),
        (")", ")")
    ]
    
    for text, insert_text in boutons_ligne1:
        btn = ttk.Button(ligne1, text=text, style="Integration.Small.TButton",
                        command=lambda t=insert_text: inserer_texte(t, entree_f))
        btn.pack(side="left", padx=2)
    
    # Ligne 2
    ligne2 = Frame(frame_boutons, bg=PALETTE["fond_principal"])
    ligne2.pack(pady=3)
    
    boutons_ligne2 = [
        ("sin(x)", "sin(x)"),
        ("cos(x)", "cos(x)"),
        ("tan(x)", "tan(x)"),
        ("π", "pi"),
        ("e", "e")
    ]
    
    for text, insert_text in boutons_ligne2:
        btn = ttk.Button(ligne2, text=text, style="Integration.Small.TButton",
                        command=lambda t=insert_text: inserer_texte(t, entree_f))
        btn.pack(side="left", padx=2)
    
    # Ligne 3
    ligne3 = Frame(frame_boutons, bg=PALETTE["fond_principal"])
    ligne3.pack(pady=3)
    
    boutons_ligne3 = [
        ("log(x)", "log(x)"),
        ("exp(x)", "exp(x)"),
        ("|x|", "|x|"),
        ("🧹 Effacer", "clear"),
        ("← Retour", "backspace")
    ]
    
    for text, action in boutons_ligne3:
        if action == "clear":
            btn = ttk.Button(ligne3, text=text, style="Integration.Small.TButton",
                            command=lambda: var_f.set(""))
        elif action == "backspace":
            btn = ttk.Button(ligne3, text=text, style="Integration.Small.TButton",
                            command=lambda: supprimer_caractere(entree_f))
        else:
            btn = ttk.Button(ligne3, text=text, style="Integration.Small.TButton",
                            command=lambda t=action: inserer_texte(t, entree_f))
        btn.pack(side="left", padx=2)
    
    # Zone de résultat
    frame_resultat = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_resultat.pack(pady=25)
    
    resultat_label = Label(frame_resultat, text="Résultat apparaîtra ici",
                          font=("Century Gothic", 14, "bold"), fg=PALETTE["texte_clair"], bg=PALETTE["fond_principal"])
    resultat_label.pack()
    
    # Fonction principale de calcul
    def calculer():
        """Fonction principale de calcul"""
        nonlocal current_iterations_tab
        
        try:
            choix = combo.get()
            
            if choix == "=== Sélectionnez une méthode ===":
                resultat_label.config(text="❌ Veuillez sélectionner une méthode", fg=PALETTE["erreur"])
                return
            
            # Récupération des valeurs
            nombre_a = entree_a.get()
            nombre_b = entree_b.get()
            nombre_n = entree_n.get()
            fonction_text = entree_f.get()
            
            # Validation et conversion
            a, b, n = valider_et_convertir_donnees(nombre_a, nombre_b, nombre_n, fonction_text)
            
            # Préparation de la fonction
            fonction_propre = preparer_fonction(fonction_text)
            
            # Test de la fonction
            try:
                fonction_propre(a)
                fonction_propre(b)
                fonction_propre((a + b) / 2)
            except Exception as e:
                resultat_label.config(text=f"❌ Erreur dans la fonction : {str(e)}", fg=PALETTE["erreur"])
                return
            
            # Calcul - ON RECUPERE AUSSI LES ITERATIONS
            resultat, iterations = executer_methode(choix, a, b, n, fonction_propre)
            
            # Affichage du résultat
            resultat_label.config(text=f"✅ Résultat : {resultat:.8f}", fg=PALETTE["succes"])
            
            # Supprimer l'ancien onglet d'itérations s'il existe
            if current_iterations_tab is not None:
                try:
                    notebook.forget(current_iterations_tab)
                except:
                    pass
            
            # Créer un nouvel onglet pour afficher les itérations
            current_iterations_tab = afficher_iterations_dans_interface(
                iterations, choix, notebook, fenetre_integration
            )
            
            # Sélectionner l'onglet des itérations
            notebook.select(current_iterations_tab)
            
        except ValueError as e:
            resultat_label.config(text=f"❌ {str(e)}", fg=PALETTE["erreur"])
        except Exception as e:
            resultat_label.config(text=f"❌ Erreur de calcul : {str(e)}", fg=PALETTE["erreur"])
    
    # Boutons de calcul
    frame_boutons_finaux = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_boutons_finaux.pack(pady=25)
    
    bouton_calculer = ttk.Button(frame_boutons_finaux, text="🧮 Calculer l'Intégrale",
                                style="Custom.TButton", command=calculer)
    bouton_calculer.pack(side="left", padx=10)
    
    def _quit_local():
        if is_toplevel:
            fenetre_integration.destroy()
        else:
            for w in list(fenetre_integration.winfo_children()):
                w.destroy()

    bouton_exit = ttk.Button(frame_boutons_finaux, text="🚪 Fermer la fenêtre",
                           style="Quit.TButton", command=_quit_local)
    bouton_exit.pack(side="left", padx=10)
    
    # Exemples
    frame_exemples = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_exemples.pack(pady=15)
    
    Label(frame_exemples, text="💡 Exemples de fonctions :",
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
    Label(frame_exemples, text="x**2 + 3*x + 1    |    sin(x)    |    cos(x)*exp(x)    |    sqrt(x)",
          font=("Century Gothic", 10), fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"]).pack(pady=5)
    
    # Informations supplémentaires
    frame_info = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_info.pack(pady=20)
    
    Label(frame_info, text="ℹ️ Informations sur les méthodes :",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0,10))
    
    methodes_info = [
        "• Rectangle Rétrograde : Utilise le côté gauche de chaque intervalle",
        "• Rectangle Progressif : Utilise le côté droit de chaque intervalle", 
        "• Rectangle Centré : Utilise le point milieu de chaque intervalle",
        "• Trapèzes Simple : Approximation linéaire entre deux points",
        "• Trapèzes Composite : Division en plusieurs trapèzes",
        "• Simpson Simple : Approximation parabolique sur 3 points",
        "• Simpson Composite : Multiple approximations paraboliques"
    ]
    
    for info in methodes_info:
        Label(frame_info, text=info, font=("Century Gothic", 10), 
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w").pack(fill="x", padx=20, pady=2)
    
    # Conseils d'utilisation
    frame_conseils = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_conseils.pack(pady=20)
    
    Label(frame_conseils, text="💡 Conseils d'utilisation :",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0,10))
    
    conseils = [
        "• Augmentez n pour plus de précision",
        "• Simpson nécessite un nombre pair de subdivisions",
        "• Testez avec des fonctions simples d'abord",
        "• Vérifiez que votre fonction est continue sur [a,b]",
        "• Utilisez des parenthèses pour les expressions complexes"
    ]
    
    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 10),
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w").pack(fill="x", padx=20, pady=2)
    
    # Espaceur final
    Label(scrollable_calc_frame, text="", bg=PALETTE["fond_principal"], height=3).pack()
    
    # ==============================
    # ONGLET 2: Aide
    # ==============================
    frame_aide = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_aide, text="❓ Aide")
    
    # Contenu de l'onglet Aide
    Label(frame_aide, text="📚 Aide sur l'intégration numérique",
          font=("Century Gothic", 16, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=20)
    
    aide_content = [
        ("Fonctionnalités principales:", [
            "• Calcul d'intégrales par différentes méthodes",
            "• Affichage détaillé de chaque itération",
            "• Interface intuitive avec onglets",
            "• Export des résultats en CSV",
            "• Raccourcis pour fonctions mathématiques"
        ]),
        
        ("Syntaxe des fonctions:", [
            "• x**2 pour x au carré",
            "• sin(x), cos(x), tan(x) pour les fonctions trigonométriques",
            "• sqrt(x) pour la racine carrée",
            "• log(x) pour le logarithme népérien",
            "• exp(x) pour l'exponentielle",
            "• pi pour π (3.14159...)",
            "• e pour la constante d'Euler (2.71828...)"
        ]),
        
        ("Paramètres:", [
            "• a: borne inférieure de l'intégrale",
            "• b: borne supérieure de l'intégrale",
            "• n: nombre de subdivisions (doit être > 0)",
            "• Pour Simpson: n doit être pair"
        ]),
        
        ("Conseils:", [
            "• Commencez avec n=10 pour tester",
            "• Augmentez n pour plus de précision",
            "• Vérifiez la continuité de la fonction",
            "• Utilisez l'export CSV pour sauvegarder les résultats"
        ])
    ]
    
    aide_frame = Frame(frame_aide, bg=PALETTE["fond_principal"])
    aide_frame.pack(fill=BOTH, expand=True, padx=30)
    
    for titre, points in aide_content:
        Label(aide_frame, text=titre,
              font=("Century Gothic", 12, "bold"),
              bg=PALETTE["fond_principal"],
              fg=PALETTE["texte_fonce"],
              anchor="w").pack(fill=X, pady=(15,5))
        
        for point in points:
            Label(aide_frame, text=point,
                  font=("Century Gothic", 10),
                  bg=PALETTE["fond_principal"],
                  fg=PALETTE["texte_clair"],
                  anchor="w",
                  justify=LEFT).pack(fill=X, padx=20, pady=2)
    
    # Bouton de fermeture dans l'onglet aide
    Button(frame_aide, text="Fermer l'application",
           font=("Century Gothic", 10, "bold"),
           bg=PALETTE["erreur"],
           fg="white",
           command=_quit_local,
           padx=20,
           pady=10).pack(pady=20)
    
    return fenetre_integration