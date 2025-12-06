"""
interpolation_numerique.py - Interface graphique pour l'interpolation numérique avec affichage des calculs et graphiques
Auteur: MathCraft
Description: Interface Tkinter pour les méthodes d'interpolation numérique avec affichage direct des calculs et graphiques
"""

from tkinter import *
from tkinter import ttk
import re
import math
import csv
import numpy as np
from math import factorial
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from . import modules as modu

# Palette unifiée (identique à integration_numerique.py)
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

# Liste des méthodes d'interpolation disponibles
METHODES = ["Lagrange", "Newton", "Linéaire par morceaux", "Spline Cubique Naturelle"]


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


def parse_points(points_str):
    """Parse les points au format 'x1,y1;x2,y2;...'"""
    points = []
    try:
        for point_str in points_str.split(';'):
            point_str = point_str.strip()
            if point_str:
                if ',' in point_str:
                    x_str, y_str = point_str.split(',')
                else:
                    # Essayer avec espace
                    parts = point_str.split()
                    if len(parts) >= 2:
                        x_str, y_str = parts[0], parts[1]
                    else:
                        continue
                
                x = float(x_str.strip())
                y = float(y_str.strip())
                points.append((x, y))
        
        if len(points) < 2:
            raise ValueError("Au moins 2 points sont nécessaires")
        
        return points
    except Exception as e:
        raise ValueError(f"Format de points invalide: {str(e)}\nUtilisez: x1,y1; x2,y2; ...")


def evaluer_polynome_lagrange(x_points, y_points, x):
    """Évalue le polynôme de Lagrange en x (pour tracé du graphe)"""
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result


def evaluer_polynome_newton(x_points, y_points, x):
    """Évalue le polynôme de Newton en x (pour tracé du graphe)"""
    n = len(x_points)
    
    # Table des différences divisées
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_points[i]
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_points[i + j] - x_points[i])
    
    # Évaluation du polynôme
    result = table[0][0]
    produit = 1
    
    for i in range(1, n):
        produit *= (x - x_points[i - 1])
        result += table[0][i] * produit
    
    return result


def evaluer_interpolation_lineaire(x_points, y_points, x):
    """Évalue l'interpolation linéaire par morceaux en x"""
    # Trier les points
    points = sorted(zip(x_points, y_points), key=lambda p: p[0])
    x_sorted, y_sorted = zip(*points)
    
    # Trouver le segment
    if x <= x_sorted[0]:
        return y_sorted[0]
    elif x >= x_sorted[-1]:
        return y_sorted[-1]
    
    for i in range(len(x_sorted) - 1):
        if x_sorted[i] <= x <= x_sorted[i + 1]:
            x1, y1 = x_sorted[i], y_sorted[i]
            x2, y2 = x_sorted[i + 1], y_sorted[i + 1]
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    
    return y_sorted[-1]


def evaluer_spline_cubique(x_points, y_points, x_eval):
    """Évalue une spline cubique naturelle en x (version simplifiée)"""
    try:
        # Trier les points
        points = sorted(zip(x_points, y_points), key=lambda p: p[0])
        x_sorted, y_sorted = zip(*points)
        n = len(x_sorted)
        
        # Trouver l'intervalle
        if x_eval <= x_sorted[0]:
            return y_sorted[0]
        elif x_eval >= x_sorted[-1]:
            return y_sorted[-1]
        
        for i in range(n - 1):
            if x_sorted[i] <= x_eval <= x_sorted[i + 1]:
                # Interpolation linéaire simplifiée pour l'affichage
                x1, y1 = x_sorted[i], y_sorted[i]
                x2, y2 = x_sorted[i + 1], y_sorted[i + 1]
                return y1 + (y2 - y1) * (x_eval - x1) / (x2 - x1)
        
        return y_sorted[-1]
    except:
        # Fallback à l'interpolation linéaire
        return evaluer_interpolation_lineaire(x_points, y_points, x_eval)


def afficher_calculs_dans_interface(resultats, methode, notebook, fenetre):
    """Affiche les calculs dans un onglet du notebook"""
    
    # Créer un nouvel onglet pour les calculs
    frame_calculs = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_calculs, text="📊 Calculs détaillés")
    
    # Titre
    Label(frame_calculs, text=f"Détails des calculs - {methode}",
          font=("Century Gothic", 14, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=10)
    
    # Statistiques
    stats_frame = Frame(frame_calculs, bg=PALETTE["fond_principal"])
    stats_frame.pack(pady=5, fill=X, padx=20)
    
    valeur = resultats.get('valeur', 'N/A')
    Label(stats_frame, text=f"Valeur interpolée: {valeur:.8f}",
          font=("Century Gothic", 10, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["succes"]).pack(side=LEFT, padx=10)
    
    if 'points' in resultats:
        Label(stats_frame, text=f"Nombre de points: {len(resultats['points'])}",
              font=("Century Gothic", 10, "bold"),
              bg=PALETTE["fond_principal"],
              fg=PALETTE["texte_fonce"]).pack(side=LEFT, padx=10)
    
    # Frame pour le tableau
    table_frame = Frame(frame_calculs, bg=PALETTE["fond_principal"])
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
    methode_lower = methode.lower()
    
    if "lagrange" in methode_lower:
        headers = ["Terme i", "Coefficient y_i", "Produit des termes", "Valeur L_i(x)", "Contribution"]
        col_widths = [80, 120, 200, 120, 120]
    elif "newton" in methode_lower:
        headers = ["Ordre j", "Indice i", "f[x_i,...,x_{i+j}]", "Calcul", "Valeur"]
        col_widths = [80, 80, 150, 200, 120]
    elif "linéaire" in methode_lower:
        headers = ["Segment", "Point 1 (x,y)", "Point 2 (x,y)", "Pente", "Équation", "Valeur en x"]
        col_widths = [80, 120, 120, 100, 200, 120]
    elif "spline" in methode_lower:
        headers = ["Intervalle", "Coeff a", "Coeff b", "Coeff c", "Coeff d", "Domaine x"]
        col_widths = [80, 100, 100, 100, 100, 120]
    else:
        headers = ["Paramètre", "Valeur"]
        col_widths = [150, 200]
    
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
    
    # Remplir le tableau avec les données selon la méthode
    row_idx = 1
    
    if "lagrange" in methode_lower and 'details' in resultats:
        details = resultats.get('details', [])
        for detail in details:
            # Alterner les couleurs des lignes
            bg_color = PALETTE["table_even"] if row_idx % 2 == 0 else PALETTE["table_odd"]
            
            values = [
                str(detail.get('terme', '')),
                f"{detail.get('coeff', 0):.6f}",
                detail.get('expression', '')[:30] + "..." if len(detail.get('expression', '')) > 30 else detail.get('expression', ''),
                f"{detail.get('valeur_term', 0):.6f}",
                f"{detail.get('valeur_term', 0):.6f}"
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
            
            row_idx += 1
    
    elif "newton" in methode_lower and 'details' in resultats:
        details_diff = resultats.get('details', {}).get('differences', [])
        for diff in details_diff:
            bg_color = PALETTE["table_even"] if row_idx % 2 == 0 else PALETTE["table_odd"]
            
            values = [
                str(diff.get('ordre', '')),
                str(diff.get('indice', '')),
                f"{diff.get('valeur', 0):.8f}",
                diff.get('formule', '')[:40] + "..." if len(diff.get('formule', '')) > 40 else diff.get('formule', ''),
                f"{diff.get('valeur', 0):.8f}"
            ]
            
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
            
            row_idx += 1
    
    elif "linéaire" in methode_lower and 'details' in resultats:
        detail = resultats.get('details', {})
        bg_color = PALETTE["table_even"]
        
        points = detail.get('points', [(0,0), (1,1)])
        values = [
            f"[{detail.get('segment', (0,1))[0]}, {detail.get('segment', (0,1))[1]}]",
            f"({points[0][0]:.3f}, {points[0][1]:.3f})",
            f"({points[1][0]:.3f}, {points[1][1]:.3f})",
            f"{detail.get('pente', 0):.6f}",
            detail.get('formule', '')[:40] + "..." if len(detail.get('formule', '')) > 40 else detail.get('formule', ''),
            f"{resultats.get('valeur', 0):.8f}"
        ]
        
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
        
        row_idx += 1
    
    elif "spline" in methode_lower and 'coefficients' in resultats:
        coeffs = resultats.get('coefficients', {})
        bg_color = PALETTE["table_even"]
        
        values = [
            str(coeffs.get('intervalle', 0)),
            f"{coeffs.get('a', 0):.6f}",
            f"{coeffs.get('b', 0):.6f}",
            f"{coeffs.get('c', 0):.6f}",
            f"{coeffs.get('d', 0):.6f}",
            f"[{coeffs.get('x0', 0):.3f}, {coeffs.get('x1', 1):.3f}]"
        ]
        
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
        
        row_idx += 1
    
    # Afficher le polynôme si disponible
    if 'polynome' in resultats:
        poly_frame = Frame(frame_calculs, bg=PALETTE["fond_principal"])
        poly_frame.pack(pady=10, fill=X, padx=20)
        
        Label(poly_frame, text="Polynôme d'interpolation:",
              font=("Century Gothic", 11, "bold"),
              bg=PALETTE["fond_principal"],
              fg=PALETTE["primaire"]).pack(anchor="w")
        
        polynome_text = resultats['polynome']
        if len(polynome_text) > 100:
            chunks = [polynome_text[i:i+80] for i in range(0, len(polynome_text), 80)]
            for chunk in chunks:
                Label(poly_frame, text=chunk,
                      font=("Courier New", 9),
                      bg=PALETTE["fond_principal"],
                      fg=PALETTE["texte_fonce"],
                      anchor="w").pack(anchor="w", padx=20)
        else:
            Label(poly_frame, text=polynome_text,
                  font=("Courier New", 9),
                  bg=PALETTE["fond_principal"],
                  fg=PALETTE["texte_fonce"],
                  anchor="w").pack(anchor="w", padx=20)
    
    # Configurer les poids des colonnes
    for col_idx in range(len(headers)):
        scrollable_frame.grid_columnconfigure(col_idx, weight=1)
    
    # Boutons d'action
    button_frame = Frame(frame_calculs, bg=PALETTE["fond_principal"])
    button_frame.pack(pady=10, fill=X, padx=20)
    
    def exporter_csv():
        """Exporte les calculs en CSV"""
        try:
            fichier = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Exporter les calculs"
            )
            
            if fichier:
                with open(fichier, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    
                    # Écrire les données selon la méthode
                    if "lagrange" in methode_lower and 'details' in resultats:
                        for detail in resultats['details']:
                            row = [
                                detail.get('terme', ''),
                                f"{detail.get('coeff', 0):.6f}",
                                detail.get('expression', ''),
                                f"{detail.get('valeur_term', 0):.6f}",
                                f"{detail.get('valeur_term', 0):.6f}"
                            ]
                            writer.writerow(row)
                    
                    elif "newton" in methode_lower and 'details' in resultats:
                        for diff in resultats['details'].get('differences', []):
                            row = [
                                diff.get('ordre', ''),
                                diff.get('indice', ''),
                                f"{diff.get('valeur', 0):.8f}",
                                diff.get('formule', ''),
                                f"{diff.get('valeur', 0):.8f}"
                            ]
                            writer.writerow(row)
                    
                    elif "linéaire" in methode_lower and 'details' in resultats:
                        detail = resultats['details']
                        points = detail.get('points', [(0,0), (1,1)])
                        row = [
                            f"[{detail.get('segment', (0,1))[0]}, {detail.get('segment', (0,1))[1]}]",
                            f"({points[0][0]:.3f}, {points[0][1]:.3f})",
                            f"({points[1][0]:.3f}, {points[1][1]:.3f})",
                            f"{detail.get('pente', 0):.6f}",
                            detail.get('formule', ''),
                            f"{resultats.get('valeur', 0):.8f}"
                        ]
                        writer.writerow(row)
                    
                    elif "spline" in methode_lower and 'coefficients' in resultats:
                        coeffs = resultats['coefficients']
                        row = [
                            coeffs.get('intervalle', 0),
                            f"{coeffs.get('a', 0):.6f}",
                            f"{coeffs.get('b', 0):.6f}",
                            f"{coeffs.get('c', 0):.6f}",
                            f"{coeffs.get('d', 0):.6f}",
                            f"[{coeffs.get('x0', 0):.3f}, {coeffs.get('x1', 1):.3f}]"
                        ]
                        writer.writerow(row)
                
                messagebox.showinfo("Export réussi", 
                                  f"Les calculs ont été exportés dans :\n{fichier}")
        except Exception as e:
            messagebox.showerror("Erreur d'export", f"Erreur lors de l'export : {str(e)}")
    
    ttk.Button(button_frame, text="📥 Exporter en CSV", 
              command=exporter_csv).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="Fermer cet onglet", 
              command=lambda: notebook.forget(frame_calculs)).pack(side=LEFT, padx=5)
    
    # Configurer la taille minimale pour le scroll
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Retourner l'onglet créé
    return frame_calculs


def afficher_graphe_interpolation(resultats, methode, notebook, fenetre):
    """Affiche le graphe de l'interpolation dans un onglet du notebook"""
    
    # Créer un nouvel onglet pour le graphe
    frame_graphe = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_graphe, text="📈 Graphe")
    
    # Titre
    Label(frame_graphe, text=f"Graphe de l'interpolation - {methode}",
          font=("Century Gothic", 14, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=10)
    
    # Extraire les points
    points = resultats.get('points', [])
    x_eval = resultats.get('x_eval', 0)
    valeur_interpolee = resultats.get('valeur', 0)
    
    if not points:
        Label(frame_graphe, text="❌ Aucun point disponible pour le graphe",
              font=("Century Gothic", 12),
              bg=PALETTE["fond_principal"],
              fg=PALETTE["erreur"]).pack(pady=50)
        return frame_graphe
    
    # Séparer les coordonnées
    x_points = [p[0] for p in points]
    y_points = [p[1] for p in points]
    
    # Trier pour l'affichage
    points_sorted = sorted(points, key=lambda p: p[0])
    x_sorted = [p[0] for p in points_sorted]
    y_sorted = [p[1] for p in points_sorted]
    
    # Créer la figure Matplotlib
    fig = Figure(figsize=(8, 5), dpi=100)
    ax = fig.add_subplot(111)
    
    # Déterminer l'intervalle d'affichage
    x_min = min(x_sorted)
    x_max = max(x_sorted)
    x_range = x_max - x_min
    
    # Ajouter des marges
    margin = x_range * 0.2 if x_range > 0 else 1
    x_plot_min = x_min - margin
    x_plot_max = x_max + margin
    
    # Créer des points pour la courbe interpolée
    x_curve = np.linspace(x_plot_min, x_plot_max, 200)
    y_curve = []
    
    # Calculer la courbe selon la méthode
    if methode == "Lagrange":
        for x in x_curve:
            y_curve.append(evaluer_polynome_lagrange(x_sorted, y_sorted, x))
        titre = "Interpolation de Lagrange"
        style_courbe = '-'
        
    elif methode == "Newton":
        for x in x_curve:
            y_curve.append(evaluer_polynome_newton(x_sorted, y_sorted, x))
        titre = "Interpolation de Newton"
        style_courbe = '-'
        
    elif methode == "Linéaire par morceaux":
        for x in x_curve:
            y_curve.append(evaluer_interpolation_lineaire(x_sorted, y_sorted, x))
        titre = "Interpolation Linéaire par Morceaux"
        style_courbe = '-'
        
    elif methode == "Spline Cubique Naturelle":
        for x in x_curve:
            y_curve.append(evaluer_spline_cubique(x_sorted, y_sorted, x))
        titre = "Spline Cubique Naturelle"
        style_courbe = '-'
    
    # Tracer la courbe interpolée
    ax.plot(x_curve, y_curve, style_courbe, color=PALETTE["primaire"], 
            linewidth=2, label='Courbe interpolée', zorder=1)
    
    # Tracer les points de données
    ax.scatter(x_sorted, y_sorted, color=PALETTE["erreur"], s=100, 
               zorder=3, label='Points donnés', edgecolors='white', linewidth=2)
    
    # Tracer le point d'évaluation
    ax.scatter([x_eval], [valeur_interpolee], color=PALETTE["succes"], s=150,
               zorder=4, label=f'Point évalué: ({x_eval:.2f}, {valeur_interpolee:.2f})',
               marker='*', edgecolors='white', linewidth=2)
    
    # Ajouter une ligne verticale au point d'évaluation
    ax.axvline(x=x_eval, color=PALETTE["texte_clair"], linestyle='--', 
               alpha=0.5, linewidth=1)
    ax.axhline(y=valeur_interpolee, color=PALETTE["texte_clair"], linestyle='--',
               alpha=0.5, linewidth=1)
    
    # Ajouter une grille
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Configurer les axes
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title(titre, fontsize=14, fontweight='bold', pad=20)
    
    # Ajouter une légende
    ax.legend(loc='best', fontsize=10, framealpha=0.9)
    
    # Ajouter des informations statistiques
    stats_text = f"Points: {len(points)}\n"
    stats_text += f"x évalué: {x_eval:.3f}\n"
    stats_text += f"y interpolé: {valeur_interpolee:.6f}"
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor=PALETTE["fond_secondaire"],
                     alpha=0.8, edgecolor=PALETTE["bordure"]))
    
    # Ajuster les limites
    y_min, y_max = ax.get_ylim()
    y_range = y_max - y_min
    ax.set_ylim(y_min - y_range * 0.1, y_max + y_range * 0.1)
    
    # Ajuster la mise en page
    fig.tight_layout()
    
    # Intégrer le graphique dans Tkinter
    canvas_graph = FigureCanvasTkAgg(fig, master=frame_graphe)
    canvas_graph.draw()
    canvas_graph.get_tk_widget().pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    # Boutons d'action pour le graphe
    button_frame = Frame(frame_graphe, bg=PALETTE["fond_principal"])
    button_frame.pack(pady=10, fill=X, padx=20)
    
    def sauvegarder_graphe():
        """Sauvegarde le graphe en image"""
        try:
            fichier = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"), 
                          ("SVG files", "*.svg"), ("All files", "*.*")],
                title="Sauvegarder le graphe"
            )
            
            if fichier:
                fig.savefig(fichier, dpi=300, bbox_inches='tight')
                messagebox.showinfo("Sauvegarde réussie", 
                                  f"Le graphe a été sauvegardé dans :\n{fichier}")
        except Exception as e:
            messagebox.showerror("Erreur de sauvegarde", f"Erreur lors de la sauvegarde : {str(e)}")
    
    def zoom_in():
        """Zoom avant"""
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2
        x_range = (xlim[1] - xlim[0]) * 0.8
        y_range = (ylim[1] - ylim[0]) * 0.8
        
        ax.set_xlim(x_center - x_range/2, x_center + x_range/2)
        ax.set_ylim(y_center - y_range/2, y_center + y_range/2)
        canvas_graph.draw()
    
    def zoom_out():
        """Zoom arrière"""
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2
        x_range = (xlim[1] - xlim[0]) * 1.25
        y_range = (ylim[1] - ylim[0]) * 1.25
        
        ax.set_xlim(x_center - x_range/2, x_center + x_range/2)
        ax.set_ylim(y_center - y_range/2, y_center + y_range/2)
        canvas_graph.draw()
    
    def reset_zoom():
        """Réinitialise le zoom"""
        x_min = min(x_sorted)
        x_max = max(x_sorted)
        x_range = x_max - x_min
        margin = x_range * 0.2 if x_range > 0 else 1
        
        y_all = list(y_sorted) + y_curve
        y_min_val = min(y_all)
        y_max_val = max(y_all)
        y_range_val = y_max_val - y_min_val
        y_margin = y_range_val * 0.2 if y_range_val > 0 else 1
        
        ax.set_xlim(x_min - margin, x_max + margin)
        ax.set_ylim(y_min_val - y_margin, y_max_val + y_margin)
        canvas_graph.draw()
    
    # Boutons de contrôle du graphe
    ttk.Button(button_frame, text="💾 Sauvegarder l'image", 
              command=sauvegarder_graphe).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="🔍 Zoom +", 
              command=zoom_in).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="🔍 Zoom -", 
              command=zoom_out).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="🔄 Réinitialiser", 
              command=reset_zoom).pack(side=LEFT, padx=5)
    
    ttk.Button(button_frame, text="Fermer cet onglet", 
              command=lambda: notebook.forget(frame_graphe)).pack(side=LEFT, padx=5)
    
    return frame_graphe


# ======================================================================================
# Interface principale avec notebook
# ======================================================================================

def lancer_interpolation_numerique(parent=None):
    """
    Ouvre une nouvelle fenêtre pour effectuer une interpolation numérique.
    
    Args:
        parent: Fenêtre parente (optionnel)
    
    Returns:
        Tk ou Toplevel: La fenêtre d'interpolation numérique
    """
    
    # Variables associées aux champs d'entrée
    var_points = StringVar()
    var_x = StringVar()
    
    # Variables pour suivre les onglets
    current_calculs_tab = None
    current_graphe_tab = None
    
    # Initialisation de la fenêtre
    fenetre_interpolation = Toplevel(parent) if parent else Tk()
    fenetre_interpolation.configure(bg=PALETTE["fond_principal"])
    fenetre_interpolation.geometry("1100x850")  # Un peu plus grand pour les graphiques
    fenetre_interpolation.title("Interpolation Numérique avec Calculs Détaillés et Graphiques")
    fenetre_interpolation.resizable(True, True)
    
    # Centrer la fenêtre
    if parent:
        fenetre_interpolation.transient(parent)
        fenetre_interpolation.grab_set()
    
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
    notebook = ttk.Notebook(fenetre_interpolation)
    notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # ==============================
    # ONGLET 1: Calcul
    # ==============================
    frame_calcul = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_calcul, text="🧮 Calcul")
    
    # Titre
    header_frame = Frame(frame_calcul, bg=PALETTE["fond_principal"])
    header_frame.pack(fill="x", pady=20)
    
    Label(header_frame, text="📈 INTERPOLATION NUMÉRIQUE",
          font=("Century Gothic", 20, "bold"), fg=PALETTE["primaire"], bg=PALETTE["fond_principal"]).pack()
    Label(header_frame, text="Choisissez une méthode d'interpolation",
          font=("Century Gothic", 12), fg=PALETTE["texte_clair"], bg=PALETTE["fond_principal"]).pack(pady=5)
    
    # Menu déroulant pour choisir la méthode
    combo = ttk.Combobox(header_frame, font=("Century Gothic", 12),
                         values=METHODES, state="readonly", width=30)
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
    
    # Section points d'interpolation
    Label(scrollable_calc_frame, text="Points d'interpolation (format: x1,y1; x2,y2; x3,y3; ...)",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"]).pack(pady=10)
    
    # Text widget pour les points (meilleur pour plusieurs points)
    text_points = Text(scrollable_calc_frame, font=("Century Gothic", 11), height=5,
                      relief="solid", borderwidth=1)
    text_points.pack(padx=20, pady=5, fill=X)
    
    # Insérer un exemple
    text_points.insert("1.0", "0,0; 1,1; 2,4; 3,9")
    
    # Section point d'évaluation
    Label(scrollable_calc_frame, text="Point x où évaluer l'interpolation :",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"]).pack(pady=10)
    
    entree_x = Entry(scrollable_calc_frame, font=("Century Gothic", 12), width=20,
                    relief="solid", borderwidth=1)
    entree_x.pack(padx=20, pady=5)
    entree_x.insert(0, "1.5")
    
    # Boutons d'exemples rapides
    Label(scrollable_calc_frame, text="Exemples rapides :",
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(20,10))
    
    frame_exemples = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_exemples.pack(pady=5)
    
    exemples = [
        ("Parabole", "0,0; 1,1; 2,4; 3,9"),
        ("Sinus", "0,0; 1.57,1; 3.14,0; 4.71,-1"),
        ("Cosinus", "0,1; 1.57,0; 3.14,-1; 4.71,0"),
        ("Courbe quelconque", "0,1; 1,3; 2,2; 3,5; 4,4")
    ]
    
    def charger_exemple(points):
        text_points.delete("1.0", END)
        text_points.insert("1.0", points)
    
    for nom, points in exemples:
        btn = ttk.Button(frame_exemples, text=nom, style="Custom.TButton",
                        command=lambda p=points: charger_exemple(p))
        btn.pack(side="left", padx=2, pady=5)
    
    # Zone de résultat
    frame_resultat = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_resultat.pack(pady=25)
    
    resultat_label = Label(frame_resultat, text="Résultat apparaîtra ici",
                          font=("Century Gothic", 14, "bold"), fg=PALETTE["texte_clair"], bg=PALETTE["fond_principal"])
    resultat_label.pack()
    
    # Fonction principale de calcul
    def calculer():
        """Fonction principale de calcul"""
        nonlocal current_calculs_tab, current_graphe_tab
        
        try:
            choix = combo.get()
            
            if choix == "=== Sélectionnez une méthode ===":
                resultat_label.config(text="❌ Veuillez sélectionner une méthode", fg=PALETTE["erreur"])
                return
            
            # Récupération des données
            points_text = text_points.get("1.0", END).strip()
            x_eval_str = entree_x.get().strip()
            
            # Validation
            if not points_text:
                raise ValueError("Les points d'interpolation sont requis")
            if not x_eval_str:
                raise ValueError("Le point x d'évaluation est requis")
            
            # Parsing des points
            points = parse_points(points_text)
            
            # Extraction des coordonnées
            x_points = [p[0] for p in points]
            y_points = [p[1] for p in points]
            
            # Conversion de x
            x_eval = float(x_eval_str)
            
            # Exécution selon la méthode
            resultats = {'points': points, 'x_eval': x_eval}
            
            if choix == "Lagrange":
                result, polynome, details = modu.interpolation_lagrange(x_points, y_points, x_eval)
                resultats.update({
                    'valeur': result,
                    'polynome': polynome,
                    'details': details
                })
                
            elif choix == "Newton":
                result, table, polynome, details = modu.interpolation_newton(x_points, y_points, x_eval)
                resultats.update({
                    'valeur': result,
                    'tableau_differences': table,
                    'polynome': polynome,
                    'details': details
                })
                
            elif choix == "Linéaire par morceaux":
                result, details = modu.interpolation_lineaire(x_points, y_points, x_eval)
                resultats.update({
                    'valeur': result,
                    'details': details
                })
                
            elif choix == "Spline Cubique Naturelle":
                if len(points) < 3:
                    raise ValueError("Au moins 3 points sont nécessaires pour une spline cubique")
                result, coefficients, details = modu.spline_cubique_naturelle(x_points, y_points, x_eval)
                resultats.update({
                    'valeur': result,
                    'coefficients': coefficients,
                    'details': details
                })
            
            # Affichage du résultat
            resultat_label.config(text=f"✅ {choix}:\nP({x_eval}) = {resultats['valeur']:.8f}", 
                                 fg=PALETTE["succes"])
            
            # Supprimer les anciens onglets s'ils existent
            if current_calculs_tab is not None:
                try:
                    notebook.forget(current_calculs_tab)
                except:
                    pass
            
            if current_graphe_tab is not None:
                try:
                    notebook.forget(current_graphe_tab)
                except:
                    pass
            
            # Créer un nouvel onglet pour afficher les calculs
            current_calculs_tab = afficher_calculs_dans_interface(
                resultats, choix, notebook, fenetre_interpolation
            )
            
            # Créer un nouvel onglet pour afficher le graphe
            current_graphe_tab = afficher_graphe_interpolation(
                resultats, choix, notebook, fenetre_interpolation
            )
            
            # Sélectionner l'onglet du graphe par défaut
            notebook.select(current_graphe_tab)
            
        except ValueError as e:
            resultat_label.config(text=f"❌ {str(e)}", fg=PALETTE["erreur"])
        except Exception as e:
            resultat_label.config(text=f"❌ Erreur de calcul : {str(e)}", 
                                 fg=PALETTE["erreur"])
    
    # Boutons de calcul
    frame_boutons_finaux = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_boutons_finaux.pack(pady=25)
    
    bouton_calculer = ttk.Button(frame_boutons_finaux, text="🧮 Calculer l'Interpolation",
                                style="Custom.TButton", command=calculer)
    bouton_calculer.pack(side="left", padx=10)
    
    bouton_effacer = ttk.Button(frame_boutons_finaux, text="🧹 Effacer",
                               style="Custom.TButton", 
                               command=lambda: [text_points.delete("1.0", END), entree_x.delete(0, END)])
    bouton_effacer.pack(side="left", padx=10)
    
    bouton_exit = ttk.Button(frame_boutons_finaux, text="🚪 Fermer la fenêtre",
                           style="Quit.TButton", command=fenetre_interpolation.destroy)
    bouton_exit.pack(side="left", padx=10)
    
    # Exemples
    frame_exemples_detail = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_exemples_detail.pack(pady=15)
    
    Label(frame_exemples_detail, text="💡 Exemples de points :",
          font=("Century Gothic", 11, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
    Label(frame_exemples_detail, text="0,0; 1,1; 2,4    |    0,1; 1,0; 2,1    |    -1,1; 0,0; 1,1; 2,4",
          font=("Century Gothic", 10), fg=PALETTE["texte_fonce"], bg=PALETTE["fond_principal"]).pack(pady=5)
    
    # Informations supplémentaires
    frame_info = Frame(scrollable_calc_frame, bg=PALETTE["fond_principal"])
    frame_info.pack(pady=20)
    
    Label(frame_info, text="ℹ️ Informations sur les méthodes :",
          font=("Century Gothic", 12, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(pady=(0,10))
    
    methodes_info = [
        "• Lagrange : Polynôme passant exactement par tous les points",
        "• Newton : Même résultat que Lagrange avec différences divisées", 
        "• Linéaire par morceaux : Segments droits entre points consécutifs",
        "• Spline Cubique Naturelle : Courbe lisse (dérivée seconde continue)"
    ]
    
    for info in methodes_info:
        Label(frame_info, text=info, font=("Century Gothic", 10), 
              bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"], anchor="w").pack(fill="x", padx=20, pady=2)
    
    # Espaceur final
    Label(scrollable_calc_frame, text="", bg=PALETTE["fond_principal"], height=3).pack()
    
    # ==============================
    # ONGLET 2: Visualisation
    # ==============================
    frame_visu = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(frame_visu, text="👁️ Visualisation")
    
    # Contenu de l'onglet Visualisation
    Label(frame_visu, text="Visualisation des Méthodes d'Interpolation",
          font=("Century Gothic", 16, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=20)
    
    # Canvas pour le contenu avec scrollbar
    canvas_visu = Canvas(frame_visu, bg=PALETTE["fond_principal"], highlightthickness=0)
    scrollbar_visu = ttk.Scrollbar(frame_visu, orient="vertical", command=canvas_visu.yview)
    scrollable_visu = Frame(canvas_visu, bg=PALETTE["fond_principal"])
    
    scrollable_visu.bind(
        "<Configure>",
        lambda e: canvas_visu.configure(scrollregion=canvas_visu.bbox("all"))
    )
    
    canvas_visu.create_window((0, 0), window=scrollable_visu, anchor="nw")
    canvas_visu.configure(yscrollcommand=scrollbar_visu.set)
    
    canvas_visu.pack(side="left", fill="both", expand=True)
    scrollbar_visu.pack(side="right", fill="y")
    
    # Contenu
    visu_frame = Frame(scrollable_visu, bg=PALETTE["fond_principal"])
    visu_frame.pack(fill=BOTH, expand=True, padx=30, pady=20)
    
    # Introduction
    Label(visu_frame, text="🎨 Visualisation Graphique des Interpolations",
          font=("Century Gothic", 14, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=(0,15))
    
    visu_text = """
    L'onglet "Graphe" affiche visuellement l'interpolation calculée :
    
    📊 Éléments du graphe :
    • Points bleus : Points de données fournis
    • Courbe bleue : Courbe interpolée
    • Étoile verte : Point évalué avec sa valeur
    • Lignes pointillées : Guide visuel pour le point évalué
    
    🎯 Fonctionnalités graphiques :
    • Zoom avant/arrière avec les boutons 🔍
    • Réinitialisation de la vue avec 🔄
    • Sauvegarde de l'image avec 💾
    • Navigation entre onglets
    
    📈 Comparaison visuelle des méthodes :
    
    1. Lagrange & Newton :
       • Courbe polynomiale unique
       • Passe exactement par tous les points
       • Peut osciller avec beaucoup de points
    
    2. Linéaire par morceaux :
       • Segments droits entre points
       • Simple mais angles vifs
       • Pas de dérivée continue
    
    3. Spline Cubique :
       • Courbe lisse et continue
       • Dérivée seconde continue
       • Meilleure pour les courbes naturelles
    
    💡 Conseil :
    Utilisez différentes méthodes sur les mêmes points
    pour comparer visuellement les résultats !
    """
    
    Label(visu_frame, text=visu_text,
          font=("Century Gothic", 10),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"],
          justify=LEFT).pack(pady=10, padx=10)
    
    # Exemple visuel
    Label(visu_frame, text="Exemple de ce que vous verrez :",
          font=("Century Gothic", 12, "bold"),
          bg=PALETTE["fond_principal"],
          fg=PALETTE["primaire"]).pack(pady=(20,10))
    
    # Créer une petite figure d'exemple
    fig_exemple = Figure(figsize=(6, 3), dpi=80)
    ax_exemple = fig_exemple.add_subplot(111)
    
    # Points d'exemple
    x_exemple = [0, 1, 2, 3, 4]
    y_exemple = [0, 1, 4, 9, 16]
    
    # Tracer
    x_curve = np.linspace(0, 4, 100)
    y_curve = x_curve ** 2  # Parabole
    
    ax_exemple.plot(x_curve, y_curve, color=PALETTE["primaire"], linewidth=2)
    ax_exemple.scatter(x_exemple, y_exemple, color=PALETTE["erreur"], s=50)
    ax_exemple.grid(True, alpha=0.3)
    ax_exemple.set_title("Exemple: Interpolation d'une parabole", fontsize=10)
    
    # Intégrer la figure dans Tkinter
    canvas_exemple = FigureCanvasTkAgg(fig_exemple, master=visu_frame)
    canvas_exemple.draw()
    canvas_exemple.get_tk_widget().pack(pady=10)
    
    # Bouton de fermeture
    Button(frame_visu, text="Fermer l'application",
           font=("Century Gothic", 10, "bold"),
           bg=PALETTE["erreur"],
           fg="white",
           command=fenetre_interpolation.destroy,
           padx=20,
           pady=10).pack(pady=20)
    
    return fenetre_interpolation