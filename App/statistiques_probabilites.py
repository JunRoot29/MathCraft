"""
statistiques_probabilites.py - Module Statistiques & Probabilites
Presentation orientee "une operation a la fois".
"""

from tkinter import *
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

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

OPS_STATS = [
    "Statistiques descriptives",
    "Coefficient de Pearson",
    "Regression lineaire simple",
]

OPS_PROBA = [
    "Permutations P(n)",
    "Arrangements A(n,k)",
    "Combinaisons C(n,k)",
    "Loi binomiale B(n,p)",
    "Loi normale - PDF",
    "Loi normale - CDF",
    "Loi normale - Quantile",
]


def _is_toplevel_parent(parent):
    import tkinter as tk
    return parent is None or isinstance(parent, (tk.Tk, tk.Toplevel))


def _parse_liste_nombres(texte):
    texte = texte.replace(";", ",").replace("\n", ",")
    valeurs = [v.strip() for v in texte.split(",") if v.strip()]
    if not valeurs:
        raise ValueError("Veuillez saisir au moins une valeur numerique")
    return [float(v) for v in valeurs]


def _format_resultat(value):
    if isinstance(value, float):
        return f"{value:.8f}"
    if isinstance(value, list):
        return "\n".join(str(v) for v in value)
    if isinstance(value, dict):
        return "\n".join([f"- {k}: {v}" for k, v in value.items()])
    return str(value)


def lancer_statistiques_probabilites(parent=None):
    is_toplevel = _is_toplevel_parent(parent)
    if is_toplevel:
        fenetre = create_responsive_window(parent, "Statistiques et Probabilites", base_width=1000, base_height=760)
        fenetre.configure(bg=PALETTE["fond_principal"])
    else:
        fenetre = parent
        for w in list(fenetre.winfo_children()):
            w.destroy()
        fenetre.configure(bg=PALETTE["fond_principal"])

    create_header_bar(fenetre, "Module 10 - Statistiques et Probabilites")
    scrollable = ScrollableFrame(fenetre, bg=PALETTE["fond_principal"])
    scrollable.pack(fill=BOTH, expand=True)
    root = scrollable.scrollable_frame

    style = ttk.Style()
    style.configure("Stats.Custom.TButton", font=("Century Gothic", 10, "bold"), padding=6)

    notebook = ttk.Notebook(root)
    notebook.pack(fill=BOTH, expand=True, padx=12, pady=12)

    tab_stats = Frame(notebook, bg=PALETTE["fond_principal"])
    tab_proba = Frame(notebook, bg=PALETTE["fond_principal"])
    notebook.add(tab_stats, text="Statistiques")
    notebook.add(tab_proba, text="Probabilites")

    # --------------------
    # Onglet statistiques
    # --------------------
    Label(tab_stats, text="Choisir une operation", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 11, "bold")).pack(anchor="w", padx=20, pady=(16, 4))
    combo_stats = ttk.Combobox(tab_stats, values=OPS_STATS, state="readonly", width=40)
    combo_stats.pack(fill=X, padx=20)
    combo_stats.set(OPS_STATS[0])

    frame_data = Frame(tab_stats, bg=PALETTE["fond_principal"])
    frame_xy = Frame(tab_stats, bg=PALETTE["fond_principal"])
    frame_data.pack(fill=X, padx=20, pady=(12, 4))
    frame_xy.pack(fill=X, padx=20, pady=(12, 4))

    Label(frame_data, text="Serie (ex: 10,12,12,14)", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 10)).pack(anchor="w")
    txt_data = Text(frame_data, height=4, font=("Consolas", 10))
    txt_data.pack(fill=X, pady=4)
    txt_data.insert("1.0", "10, 12, 12, 14, 18, 21, 21, 25")

    Label(frame_xy, text="Serie X", bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
          font=("Century Gothic", 10)).pack(anchor="w")
    entry_x = Entry(frame_xy, font=("Consolas", 10))
    entry_x.pack(fill=X, pady=(2, 8))
    entry_x.insert(0, "1,2,3,4,5")
    Label(frame_xy, text="Serie Y", bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"],
          font=("Century Gothic", 10)).pack(anchor="w")
    entry_y = Entry(frame_xy, font=("Consolas", 10))
    entry_y.pack(fill=X, pady=(2, 4))
    entry_y.insert(0, "2,4,5,4,6")

    Label(tab_stats, text="Resultat", bg=PALETTE["fond_principal"], fg=PALETTE["primaire"],
          font=("Century Gothic", 11, "bold")).pack(anchor="w", padx=20, pady=(10, 4))
    out_stats = Text(tab_stats, height=16, font=("Consolas", 10))
    out_stats.pack(fill=BOTH, expand=True, padx=20, pady=(0, 8))

    def _refresh_stats_fields(_evt=None):
        op = combo_stats.get()
        if op == "Statistiques descriptives":
            frame_data.pack(fill=X, padx=20, pady=(12, 4))
            frame_xy.pack_forget()
        else:
            frame_data.pack_forget()
            frame_xy.pack(fill=X, padx=20, pady=(12, 4))

    def _calc_stats():
        op = combo_stats.get()
        try:
            if op == "Statistiques descriptives":
                data = _parse_liste_nombres(txt_data.get("1.0", END))
                result = modu.statistiques_descriptives(data)
                entree = {"data": data}
            elif op == "Coefficient de Pearson":
                x = _parse_liste_nombres(entry_x.get())
                y = _parse_liste_nombres(entry_y.get())
                result = {"pearson_r": modu.coefficient_pearson(x, y)}
                entree = {"x": x, "y": y}
            else:
                x = _parse_liste_nombres(entry_x.get())
                y = _parse_liste_nombres(entry_y.get())
                result = modu.regression_lineaire_simple(x, y)
                entree = {"x": x, "y": y}

            out_stats.delete("1.0", END)
            out_stats.insert(END, f"Operation: {op}\n")
            out_stats.insert(END, "============================\n")
            out_stats.insert(END, _format_resultat(result))

            historique_manager.ajouter_calcul(
                module="Statistiques & Probabilites",
                operation=op,
                entree=entree,
                resultat=result
            )
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def _graph_stats():
        op = combo_stats.get()
        try:
            if op == "Statistiques descriptives":
                data = _parse_liste_nombres(txt_data.get("1.0", END))
                arr = np.array(data, dtype=float)
                mu = float(np.mean(arr))
                sigma = float(np.std(arr, ddof=0))

                fig, axes = plt.subplots(1, 3, figsize=(14, 4))

                # Histogramme
                axes[0].hist(arr, bins="auto", color="#1767AA", edgecolor="white", alpha=0.85)
                axes[0].set_title("Histogramme")
                axes[0].set_xlabel("Valeurs")
                axes[0].set_ylabel("Frequence")
                axes[0].grid(alpha=0.25)

                # Boxplot
                axes[1].boxplot(arr, vert=True, patch_artist=True, boxprops=dict(facecolor="#A7C5EB"))
                axes[1].set_title("Boxplot")
                axes[1].set_ylabel("Valeurs")
                axes[1].grid(alpha=0.25)

                # Densite gaussienne approx (si sigma > 0)
                if sigma > 0:
                    x = np.linspace(np.min(arr) - sigma, np.max(arr) + sigma, 200)
                    y = (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
                    axes[2].plot(x, y, color="#0F4C81", linewidth=2, label=f"mu={mu:.2f}, sigma={sigma:.2f}")
                    axes[2].set_title("Densite (approx normale)")
                    axes[2].set_xlabel("x")
                    axes[2].set_ylabel("densite")
                    axes[2].grid(alpha=0.25)
                    axes[2].legend()
                else:
                    axes[2].axvline(mu, color="#0F4C81", linewidth=2)
                    axes[2].set_title("Densite non definie (sigma=0)")
                    axes[2].grid(alpha=0.25)

                fig.suptitle("Visualisation statistique", fontsize=12, fontweight="bold")
                fig.tight_layout()
                plt.show()
            else:
                x = _parse_liste_nombres(entry_x.get())
                y = _parse_liste_nombres(entry_y.get())
                if len(x) != len(y):
                    raise ValueError("X et Y doivent avoir la meme longueur")

                reg = modu.regression_lineaire_simple(x, y)
                a = reg["pente"]
                b = reg["ordonnee_origine"]
                x_arr = np.array(x, dtype=float)
                y_arr = np.array(y, dtype=float)
                x_line = np.linspace(np.min(x_arr), np.max(x_arr), 200)
                y_line = a * x_line + b
                r = modu.coefficient_pearson(x, y)

                plt.figure(figsize=(8, 5))
                plt.scatter(x_arr, y_arr, color="#1767AA", s=60, alpha=0.9, label="Nuage de points")
                plt.plot(x_line, y_line, color="#C0392B", linewidth=2.2, label=f"Droite: y={a:.3f}x+{b:.3f}")
                plt.title(f"Nuage de points et regression (r={r:.4f})")
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.grid(alpha=0.25)
                plt.legend()
                plt.tight_layout()
                plt.show()
        except Exception as e:
            messagebox.showerror("Erreur graphique", str(e))

    combo_stats.bind("<<ComboboxSelected>>", _refresh_stats_fields)
    _refresh_stats_fields()

    row_btn_stats = Frame(tab_stats, bg=PALETTE["fond_principal"])
    row_btn_stats.pack(fill=X, padx=20, pady=(0, 16))
    ttk.Button(row_btn_stats, text="Calculer", style="Stats.Custom.TButton", command=_calc_stats).pack(side=LEFT)
    ttk.Button(row_btn_stats, text="Afficher graphique", style="Stats.Custom.TButton", command=_graph_stats).pack(side=LEFT, padx=8)
    ttk.Button(row_btn_stats, text="Effacer resultat", style="Stats.Custom.TButton",
               command=lambda: out_stats.delete("1.0", END)).pack(side=LEFT, padx=8)

    # --------------------
    # Onglet probabilites
    # --------------------
    Label(tab_proba, text="Choisir une operation", bg=PALETTE["fond_principal"],
          fg=PALETTE["texte_fonce"], font=("Century Gothic", 11, "bold")).pack(anchor="w", padx=20, pady=(16, 4))
    combo_proba = ttk.Combobox(tab_proba, values=OPS_PROBA, state="readonly", width=40)
    combo_proba.pack(fill=X, padx=20)
    combo_proba.set(OPS_PROBA[0])

    form = Frame(tab_proba, bg=PALETTE["fond_principal"])
    form.pack(fill=X, padx=20, pady=(10, 6))

    fields = {}
    for key, label_text, default in [
        ("n", "n", "5"),
        ("k", "k", "2"),
        ("p", "p", "0.4"),
        ("mu", "mu", "0"),
        ("sigma", "sigma", "1"),
        ("x", "x", "1.96"),
        ("q", "q (0<q<1)", "0.975"),
    ]:
        row = Frame(form, bg=PALETTE["fond_principal"])
        lbl = Label(row, text=label_text, width=12, anchor="w", bg=PALETTE["fond_principal"], fg=PALETTE["texte_fonce"])
        ent = Entry(row, font=("Consolas", 10))
        ent.insert(0, default)
        lbl.pack(side=LEFT)
        ent.pack(side=LEFT, fill=X, expand=True)
        fields[key] = {"row": row, "entry": ent}

    def _show_proba_fields(wanted):
        for k, cfg in fields.items():
            cfg["row"].pack_forget()
            if k in wanted:
                cfg["row"].pack(fill=X, pady=3)

    def _refresh_proba_fields(_evt=None):
        op = combo_proba.get()
        mapping = {
            "Permutations P(n)": ["n"],
            "Arrangements A(n,k)": ["n", "k"],
            "Combinaisons C(n,k)": ["n", "k"],
            "Loi binomiale B(n,p)": ["n", "p"],
            "Loi normale - PDF": ["mu", "sigma", "x"],
            "Loi normale - CDF": ["mu", "sigma", "x"],
            "Loi normale - Quantile": ["mu", "sigma", "q"],
        }
        _show_proba_fields(mapping.get(op, ["n"]))

    Label(tab_proba, text="Resultat", bg=PALETTE["fond_principal"], fg=PALETTE["primaire"],
          font=("Century Gothic", 11, "bold")).pack(anchor="w", padx=20, pady=(10, 4))
    out_proba = Text(tab_proba, height=18, font=("Consolas", 10))
    out_proba.pack(fill=BOTH, expand=True, padx=20, pady=(0, 8))

    def _calc_proba():
        op = combo_proba.get()
        try:
            getf = lambda name: fields[name]["entry"].get().strip()
            entree = {}

            if op == "Permutations P(n)":
                n = int(getf("n"))
                entree = {"n": n}
                result = {"P(n)": modu.permutations(n)}
            elif op == "Arrangements A(n,k)":
                n = int(getf("n"))
                k = int(getf("k"))
                entree = {"n": n, "k": k}
                result = {"A(n,k)": modu.arrangements(n, k)}
            elif op == "Combinaisons C(n,k)":
                n = int(getf("n"))
                k = int(getf("k"))
                entree = {"n": n, "k": k}
                result = {"C(n,k)": modu.combinaisons(n, k)}
            elif op == "Loi binomiale B(n,p)":
                n = int(getf("n"))
                p = float(getf("p"))
                entree = {"n": n, "p": p}
                result = modu.distribution_binomiale(n, p)
            elif op == "Loi normale - PDF":
                mu = float(getf("mu"))
                sigma = float(getf("sigma"))
                x = float(getf("x"))
                entree = {"mu": mu, "sigma": sigma, "x": x}
                result = {"pdf": modu.loi_normale_pdf(x, mu, sigma)}
            elif op == "Loi normale - CDF":
                mu = float(getf("mu"))
                sigma = float(getf("sigma"))
                x = float(getf("x"))
                entree = {"mu": mu, "sigma": sigma, "x": x}
                result = {"cdf": modu.loi_normale_cdf(x, mu, sigma)}
            else:
                mu = float(getf("mu"))
                sigma = float(getf("sigma"))
                q = float(getf("q"))
                entree = {"mu": mu, "sigma": sigma, "q": q}
                result = {"quantile": modu.loi_normale_quantile(q, mu, sigma)}

            out_proba.delete("1.0", END)
            out_proba.insert(END, f"Operation: {op}\n")
            out_proba.insert(END, "============================\n")
            out_proba.insert(END, _format_resultat(result))

            historique_manager.ajouter_calcul(
                module="Statistiques & Probabilites",
                operation=op,
                entree=entree,
                resultat=result
            )
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    combo_proba.bind("<<ComboboxSelected>>", _refresh_proba_fields)
    _refresh_proba_fields()

    row_btn_proba = Frame(tab_proba, bg=PALETTE["fond_principal"])
    row_btn_proba.pack(fill=X, padx=20, pady=(0, 16))
    ttk.Button(row_btn_proba, text="Calculer", style="Stats.Custom.TButton", command=_calc_proba).pack(side=LEFT)
    ttk.Button(row_btn_proba, text="Effacer resultat", style="Stats.Custom.TButton",
               command=lambda: out_proba.delete("1.0", END)).pack(side=LEFT, padx=8)

    def _close_local():
        if is_toplevel:
            fenetre.destroy()
        else:
            for w in list(fenetre.winfo_children()):
                w.destroy()

    ttk.Button(root, text="Fermer", style="Stats.Custom.TButton", command=_close_local).pack(pady=(0, 12))

    return fenetre
