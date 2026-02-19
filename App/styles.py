"""Styles centraux et helpers UI pour MathCraft."""

from tkinter import ttk

DEFAULT_FONT = ("Century Gothic", 12)
HEADER_FONT = ("Century Gothic", 18, "bold")
SMALL_FONT = ("Century Gothic", 10)

DEFAULT_PALETTE = {
    "fond_principal": "#F4F7FB",
    "fond_secondaire": "#FFFFFF",
    "fond_contraste": "#EAF1F8",
    "primaire": "#0F4C81",
    "secondaire": "#1767AA",
    "accent": "#F59E0B",
    "texte_fonce": "#102A43",
    "texte_clair": "#5B7083",
    "erreur": "#C0392B",
    "bordure": "#D9E2EC",
}

_styles_configured = False
_last_palette_signature = None


def _build_palette(palette: dict | None = None) -> dict:
    result = DEFAULT_PALETTE.copy()
    if palette:
        result.update(palette)
    return result


def ensure_styles_configured(palette: dict | None = None):
    """Configure ou met à jour les styles ttk de façon idempotente."""
    global _styles_configured, _last_palette_signature

    final_palette = _build_palette(palette)
    signature = tuple(sorted(final_palette.items()))

    if _styles_configured and signature == _last_palette_signature:
        return

    style = ttk.Style()
    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure(
        "Custom.TButton",
        foreground=final_palette["fond_secondaire"],
        background=final_palette["primaire"],
        font=("Century Gothic", 12, "bold"),
        padding=12,
        relief="flat",
        borderwidth=0,
    )
    style.map(
        "Custom.TButton",
        background=[("active", final_palette["secondaire"]), ("pressed", "#0B3C66")],
        foreground=[("active", final_palette["fond_secondaire"])],
    )

    style.configure(
        "Quit.TButton",
        foreground=final_palette["fond_secondaire"],
        background=final_palette["erreur"],
        font=("Century Gothic", 12, "bold"),
        padding=12,
        relief="flat",
        borderwidth=0,
    )
    style.map(
        "Quit.TButton",
        background=[("active", "#A93226"), ("pressed", "#922B21")],
        foreground=[("active", final_palette["fond_secondaire"])],
    )

    style.configure(
        "Return.Header.TButton",
        foreground=final_palette["fond_secondaire"],
        background=final_palette["primaire"],
        font=("Century Gothic", 10, "bold"),
        padding=6,
        relief="flat",
    )
    style.map(
        "Return.Header.TButton",
        background=[("active", final_palette["secondaire"]), ("pressed", "#0B3C66")],
        foreground=[("active", final_palette["fond_secondaire"])],
    )

    style.configure("Historique.TButton", padding=10, font=("Century Gothic", 10))
    style.configure("Jeu.TButton", font=("Century Gothic", 12), padding=12, relief="flat")
    style.configure("Guide.TButton", font=("Century Gothic", 10), padding=8)

    _styles_configured = True
    _last_palette_signature = signature


def make_scrollable_frame(parent, bg=None):
    """Crée une zone scrollable et retourne le frame interne."""
    import tkinter as tk
    from tkinter import ttk

    canvas = tk.Canvas(parent, bg=bg or DEFAULT_PALETTE["fond_secondaire"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg=bg or DEFAULT_PALETTE["fond_secondaire"])

    inner.bind("<Configure>", lambda _e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    def _on_enter(_event):
        canvas.bind_all("<MouseWheel>", _on_wheel)

    def _on_leave(_event):
        canvas.unbind_all("<MouseWheel>")

    canvas.bind("<Enter>", _on_enter)
    canvas.bind("<Leave>", _on_leave)

    return inner
