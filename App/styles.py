"""Module centralisé pour la configuration des styles et polices de l'application MathCraft.
Fournit ensure_styles_configured(palette) qui est idempotent et peut être appelé depuis n'importe quel module
au moment où une interface graphique doit être construite.
"""
from tkinter import ttk

_styles_configured = False

# Police par défaut
DEFAULT_FONT = ("Century Gothic", 12)
HEADER_FONT = ("Century Gothic", 18, "bold")
SMALL_FONT = ("Century Gothic", 10)


def ensure_styles_configured(palette: dict):
    """Configure les styles ttk de façon idempotente.
    palette: dictionnaire contenant les couleurs attendues par les modules
    """
    global _styles_configured
    if _styles_configured:
        return

    try:
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass

        # Bouton principal
        try:
            style.configure("Custom.TButton",
                            foreground=palette.get("fond_secondaire", "#FFFFFF"),
                            background=palette.get("primaire", "#1E40AF"),
                            font=("Century Gothic", 12, "bold"),
                            padding=15,
                            relief="flat")
        except Exception:
            pass

        # Bouton Quitter
        try:
            style.configure("Quit.TButton",
                            foreground=palette.get("fond_secondaire", "#FFFFFF"),
                            background=palette.get("erreur", "#DC2626"),
                            font=("Century Gothic", 12, "bold"),
                            padding=12,
                            relief="flat")
        except Exception:
            pass

        # Bouton Retour (header, top-left)
        try:
            style.configure("Return.Header.TButton",
                            foreground=palette.get("fond_secondaire", "#FFFFFF"),
                            background=palette.get("primaire", "#1E40AF"),
                            font=("Century Gothic", 10, "bold"),
                            padding=6,
                            relief="flat")
            style.map("Return.Header.TButton",
                      background=[('active', palette.get("secondaire", '#3B82F6')), ('pressed', '#1E3A8A')])
        except Exception:
            pass

        # Styles complémentaires usuels
        try:
            style.configure("Historique.TButton", padding=10, font=("Century Gothic", 10))
            style.configure("Jeu.TButton", font=("Century Gothic", 12), padding=15, relief="flat")
            style.configure("Guide.TButton", font=("Century Gothic", 10), padding=8)
        except Exception:
            pass

    except Exception:
        # En cas d'échec silencieux, ne pas arrêter l'exécution
        pass
    else:
        # Marquer comme configuré uniquement si la configuration s'est déroulée sans erreur
        _styles_configured = True


def make_scrollable_frame(parent, bg=None):
    """Crée une zone scrollable (frame intérieure) dans `parent` et retourne `inner_frame`.
    Utilise un Canvas + Scrollbar et bind le scroll de la molette lorsque le curseur est au-dessus."""
    import tkinter as tk
    from tkinter import ttk

    canvas = tk.Canvas(parent, bg=bg or "#FFFFFF", highlightthickness=0)
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg=bg or "#FFFFFF")

    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Bind la molette seulement quand le curseur est sur le canvas (évite les conflits globaux)
    def _on_enter(e):
        canvas.bind_all("<MouseWheel>", lambda evt: canvas.yview_scroll(int(-1*(evt.delta/120)), "units"))
    def _on_leave(e):
        canvas.unbind_all("<MouseWheel>")

    canvas.bind("<Enter>", _on_enter)
    canvas.bind("<Leave>", _on_leave)

    return inner
