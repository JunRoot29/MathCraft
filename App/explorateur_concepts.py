"""Interface pour l'Explorateur de Concepts - Module 4"""
"""
explorateur_concepts.py - Interface pour la découverte
Auteur: Junior Kossivi
Description: Interface Tkinter pour la présentations de jeu mathématiques
"""
from tkinter import *
from tkinter import ttk
from .jeux_math import JEUX_DISPONIBLES

# Palette de couleurs améliorée
PALETTE = {
    "fond_principal": "#F4F7FB",
    "fond_secondaire": "#FFFFFF",
    "primaire": "#0F4C81",      # Bleu plus foncé pour meilleur contraste
    "secondaire": "#1767AA",    # Bleu original pour accents
    "texte_fonce": "#102A43",   # Texte très visible
    "texte_clair": "#5B7083",   # Texte secondaire
    "succes": "#10B981",        # Vert
    "erreur": "#C0392B",        # Rouge
    "bordure": "#D9E2EC",       # Bordure légère
}

def configurer_styles():
    """Configure les styles ttk pour l'explorateur de concepts"""
    try:
        from .styles import ensure_styles_configured
        ensure_styles_configured(PALETTE)
    except Exception:
        pass


# Helper pour savoir si on doit créer une Toplevel ou utiliser un Frame parent
def _is_toplevel_parent(parent):
    import tkinter as tk
    # Only create a new Toplevel when no parent is provided or when parent is the root Tk.
    # If parent is a Toplevel, reuse that window instead of opening a new one.
    return parent is None or isinstance(parent, tk.Tk)

def lancer_explorateur_concepts(parent=None):
    """Lance l'explorateur de concepts en réutilisant l'interface de sélection des jeux"""
    # Configurer les styles puis déléguer à `creer_interface_jeux` pour garder l'interface identique
    configurer_styles()
    try:
        from .jeux_math import creer_interface_jeux
        return creer_interface_jeux(parent)
    except Exception:
        # Fallback minimal : si pour une raison quelconque l'import échoue, retourner None
        return None