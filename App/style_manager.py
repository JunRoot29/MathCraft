"""Gestion centralisée du style pour l'interface Tkinter.

Évite la création d'une racine Tk implicite lors de l'import en initialisant
le style uniquement lorsque la racine existe.
"""
from typing import Optional
import tkinter as tk
from tkinter import ttk

# Palette partagée (synchronisée avec le reste du projet)
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
    "table_even": "#FFFFFF",
}

_style: Optional[ttk.Style] = None


def _configure_style() -> ttk.Style:
    """Crée et configure le ttk.Style à utiliser par l'application."""
    s = ttk.Style()
    try:
        s.theme_use("clam")
    except Exception:
        # Certains environnements peuvent ne pas supporter le thème clam
        pass

    # Boutons principaux
    s.configure("Custom.TButton",
                foreground=PALETTE["fond_secondaire"],
                background=PALETTE["primaire"],
                font=("Century Gothic", 12, "bold"),
                padding=15,
                relief="flat")

    s.configure("Quit.TButton",
                foreground=PALETTE["fond_secondaire"],
                background=PALETTE["erreur"],
                font=("Century Gothic", 12, "bold"),
                padding=12,
                relief="flat")

    s.map("Custom.TButton",
          background=[('active', PALETTE["secondaire"]), ('pressed', '#1E3A8A')],
          foreground=[('active', PALETTE["fond_secondaire"])])

    s.map("Quit.TButton",
          background=[('active', '#B91C1C'), ('pressed', '#991B1B')],
          foreground=[('active', PALETTE["fond_secondaire"])])

    # Style pour treeviews / historiques
    s.configure("Historique.TButton", padding=10, font=("Century Gothic", 10))
    s.configure("Historique.Treeview", font=("Century Gothic", 9))

    # Onglets & Notebook
    s.configure("TNotebook", background=PALETTE["fond_principal"])
    s.configure("TNotebook.Tab", font=("Century Gothic", 10), padding=[10, 5])

    return s


def ensure_style() -> Optional[ttk.Style]:
    """Initialise le style si une racine Tk existe.

    Retourne l'objet ttk.Style configuré, ou None si aucune racine Tk n'existe.
    """
    global _style
    if _style is None:
        # Ne pas créer une racine Tk implicite : n'initialiser que si root existe
        if tk._default_root is None:
            return None
        try:
            _style = _configure_style()
        except Exception:
            _style = None
    return _style
