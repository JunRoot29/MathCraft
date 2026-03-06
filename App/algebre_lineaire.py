"""
algebre_lineaire.py - Module Algebre Lineaire
Presentation orientee operation selectionnee.
"""

from tkinter import *
from tkinter import ttk, messagebox

from . import modules as modu
from .historique_manager import historique_manager
from .responsive_ui import create_responsive_window, create_header_bar
from .scrollable_ui import ScrollableFrame


PALETTE = {
    "fond_principal": "#F4F7FB",
    "fond_secondaire": "#FFFFFF",
    "primaire": "#0F4C81",
    "secondaire": "#1767AA",
    "texte_fonce": "#102A43",
    "texte_clair": "#5B7083",
    "succes": "#10B981",
    "erreur": "#C0392B",
    "bordure": "#D9E2EC",
}

OPERATIONS = [
    "A + B",
    "A - B",
    "A x B",
    "Transposee(A)",
    "Trace(A)",
    "Determinant(A)",
    "Rang(A)",
    "Inverse(A)",
    "Resoudre Ax=b (Gauss)",
    "Resoudre Ax=b (Gauss-Jordan)",
    "Decomposition LU(A)",
    "Resoudre Ax=b (LU)",
    "Valeurs/vecteurs propres(A)",
    "Diagonalisation(A)",
    "Trigonalisation(A)",
]


def _is_toplevel_parent(parent):
    import tkinter as tk
    return parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))


def _parse_matrix(text):
    lignes = [l.strip() for l in text.replace("\n", ";").split(";") if l.strip()]
    if not lignes:
        raise ValueError("La matrice est vide")
    matrice = []
    for ligne in lignes:
        elements = [e.strip() for e in ligne.replace(",", " ").split() if e.strip()]
        matrice.append([float(e) for e in elements])
    nb_cols = len(matrice[0])
    if any(len(l) != nb_cols for l in matrice):
        raise ValueError("Toutes les lignes de la matrice doivent avoir la meme longueur")
    return matrice


def _parse_vector(text):
    values = [v.strip() for v in text.replace(";", ",").split(",") if v.strip()]
    if not values:
        raise ValueError("Le vecteur b est vide")
    return [float(v) for v in values]


def _format_value(value):
    def _fmt(v, indent=0):
        pad = " " * indent
        if isinstance(v, float):
            return f"{v:.8f}"
        if isinstance(v, list):
            if v and isinstance(v[0], list):
                return "\n".join([pad + str([round(x, 8) if isinstance(x, float) else x for x in row]) for row in v])
            return pad + str(v)
        if isinstance(v, dict):
            lignes = []
            for k, subv in v.items():
                if isinstance(subv, (list, dict)):
                    lignes.append(f"{pad}{k}:")
                    lignes.append(_fmt(subv, indent + 2))
                else:
                    lignes.append(f"{pad}{k}: {subv}")
            return "\n".join(lignes)
        return pad + str(v)

    return _fmt(value)


def lancer_algebre_lineaire(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre = create_responsive_window(parent, "Algebre lineaire", base_width=1000, base_height=780)
        fenetre.configure(bg=PALETTE["fond_principal"])
    else:
        fenetre = parent
        for w in list(fenetre.winfo_children()):
            w.destroy()
        fenetre.configure(bg=PALETTE["fond_principal"])

    create_header_bar(fenetre, "Module 11 - Algebre Lineaire")
    scrollable = ScrollableFrame(fenetre, bg=PALETTE["fond_principal"])
    scrollable.pack(fill=BOTH, expand=True)
    root = scrollable.scrollable_frame

    style = ttk.Style()
    style.configure("Alg.Custom.TButton", font=("Century Gothic", 10, "bold"), padding=6)

    Label(root, text="Choisir une operation", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 11, "bold")).pack(anchor="w", padx=20, pady=(16, 4))
    combo = ttk.Combobox(root, values=OPERATIONS, state="readonly", width=46)
    combo.pack(fill=X, padx=20)
    combo.set(OPERATIONS[0])

    frame_a = Frame(root, bg=PALETTE["fond_principal"])
    frame_b = Frame(root, bg=PALETTE["fond_principal"])
    frame_vec = Frame(root, bg=PALETTE["fond_principal"])
    frame_a.pack(fill=X, padx=20, pady=(10, 4))
    frame_b.pack(fill=X, padx=20, pady=(10, 4))
    frame_vec.pack(fill=X, padx=20, pady=(10, 4))

    Label(frame_a, text="Matrice A (ex: 1 2; 3 4)", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 10)).pack(anchor="w")
    txt_a = Text(frame_a, height=5, font=("Consolas", 10))
    txt_a.pack(fill=X, pady=4)
    txt_a.insert("1.0", "1 2; 3 4")

    Label(frame_b, text="Matrice B", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 10)).pack(anchor="w")
    txt_b = Text(frame_b, height=5, font=("Consolas", 10))
    txt_b.pack(fill=X, pady=4)
    txt_b.insert("1.0", "5 6; 7 8")

    Label(frame_vec, text="Vecteur b (ex: 5,11)", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 10)).pack(anchor="w")
    entry_vec = Entry(frame_vec, font=("Consolas", 10))
    entry_vec.pack(fill=X, pady=4)
    entry_vec.insert(0, "5,11")

    exemple = Label(root, text="", bg=PALETTE["fond_principal"], fg=PALETTE["texte_clair"],
                    font=("Century Gothic", 9), justify=LEFT, anchor="w")
    exemple.pack(fill=X, padx=20, pady=(4, 8))

    Label(root, text="Resultat", bg=PALETTE["fond_principal"], fg=PALETTE["primaire"],
          font=("Century Gothic", 11, "bold")).pack(anchor="w", padx=20, pady=(4, 4))
    out = Text(root, height=18, font=("Consolas", 10))
    out.pack(fill=BOTH, expand=True, padx=20, pady=(0, 8))

    def _refresh_fields(_evt=None):
        op = combo.get()
        needs_b = op in {"A + B", "A - B", "A x B"}
        needs_vec = op in {"Resoudre Ax=b (Gauss)", "Resoudre Ax=b (Gauss-Jordan)", "Resoudre Ax=b (LU)"}

        if needs_b:
            frame_b.pack(fill=X, padx=20, pady=(10, 4))
        else:
            frame_b.pack_forget()

        if needs_vec:
            frame_vec.pack(fill=X, padx=20, pady=(10, 4))
        else:
            frame_vec.pack_forget()

        hints = {
            "A + B": "A et B de meme dimension",
            "A x B": "nb colonnes(A) = nb lignes(B)",
            "Inverse(A)": "A doit etre carree et inversible",
            "Diagonalisation(A)": "A doit etre carree; certaines matrices ne sont pas diagonalisables",
            "Trigonalisation(A)": "Retourne T triangulaire avec A ~= Q*T*Q^-1",
            "Resoudre Ax=b (Gauss)": "A carree, b de taille n",
        }
        exemple.config(text=f"Conseil: {hints.get(op, 'Saisir A puis lancer le calcul.')}")

    def _calculate():
        op = combo.get()
        try:
            a = _parse_matrix(txt_a.get("1.0", END))
            entree = {"A": a}

            if op == "A + B":
                b = _parse_matrix(txt_b.get("1.0", END))
                entree["B"] = b
                result = modu.matrice_addition(a, b)
            elif op == "A - B":
                b = _parse_matrix(txt_b.get("1.0", END))
                entree["B"] = b
                result = modu.matrice_soustraction(a, b)
            elif op == "A x B":
                b = _parse_matrix(txt_b.get("1.0", END))
                entree["B"] = b
                result = modu.matrice_multiplication(a, b)
            elif op == "Transposee(A)":
                result = modu.matrice_transposee(a)
            elif op == "Trace(A)":
                result = {"trace": modu.matrice_trace(a)}
            elif op == "Determinant(A)":
                result = {"determinant": modu.matrice_determinant(a)}
            elif op == "Rang(A)":
                result = {"rang": modu.matrice_rang(a)}
            elif op == "Inverse(A)":
                result = modu.matrice_inverse(a)
            elif op == "Resoudre Ax=b (Gauss)":
                bvec = _parse_vector(entry_vec.get())
                entree["b"] = bvec
                result = {"solution": modu.resoudre_systeme_gauss(a, bvec)}
            elif op == "Resoudre Ax=b (Gauss-Jordan)":
                bvec = _parse_vector(entry_vec.get())
                entree["b"] = bvec
                result = {"solution": modu.resoudre_systeme_gauss_jordan(a, bvec)}
            elif op == "Decomposition LU(A)":
                result = modu.decomposition_lu(a)
            elif op == "Resoudre Ax=b (LU)":
                bvec = _parse_vector(entry_vec.get())
                entree["b"] = bvec
                result = {"solution": modu.resoudre_systeme_lu(a, bvec)}
            elif op == "Valeurs/vecteurs propres(A)":
                result = modu.valeurs_propres_vecteurs_propres(a)
            elif op == "Diagonalisation(A)":
                result = modu.diagonalisation_matrice(a)
            elif op == "Trigonalisation(A)":
                result = modu.trigonalisation_matrice(a)
            else:
                raise ValueError("Operation inconnue")

            out.delete("1.0", END)
            out.insert(END, f"Operation: {op}\n")
            out.insert(END, "============================\n")
            out.insert(END, _format_value(result))

            historique_manager.ajouter_calcul(
                module="Algebre Lineaire",
                operation=op,
                entree=entree,
                resultat=result
            )
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    combo.bind("<<ComboboxSelected>>", _refresh_fields)
    _refresh_fields()

    row_btn = Frame(root, bg=PALETTE["fond_principal"])
    row_btn.pack(fill=X, padx=20, pady=(0, 12))
    ttk.Button(row_btn, text="Calculer", style="Alg.Custom.TButton", command=_calculate).pack(side=LEFT)
    ttk.Button(row_btn, text="Effacer resultat", style="Alg.Custom.TButton",
               command=lambda: out.delete("1.0", END)).pack(side=LEFT, padx=8)

    def _close_local():
        if is_toplevel:
            fenetre.destroy()
        else:
            for w in list(fenetre.winfo_children()):
                w.destroy()

    ttk.Button(row_btn, text="Fermer", style="Alg.Custom.TButton", command=_close_local).pack(side=RIGHT)

    return fenetre
