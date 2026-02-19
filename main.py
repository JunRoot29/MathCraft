from tkinter import *
from tkinter import ttk

from App import chaine_de_caractere as ch
from App import conversion as conv
from App import equation_numerique as eq_num
from App import explorateur_concepts as exp_concepts
from App import integration_numerique as int_num
from App import interpolation_lineaire as int_lin
from App import operation_de_base as op
from App import polynome as poly
from App import theorie_des_nombres as theorie
from App.interface_historique import InterfaceHistorique
from App.responsive_ui import ResponsiveUIManager
from App.soutient_manager import afficher_soutien
from App.styles import ensure_styles_configured

PALETTE = {
    "fond_principal": "#F4F7FB",
    "fond_secondaire": "#FFFFFF",
    "fond_contraste": "#EAF1F8",
    "primaire": "#0F4C81",
    "secondaire": "#1767AA",
    "accent": "#F59E0B",
    "texte_fonce": "#102A43",
    "texte_clair": "#5B7083",
    "bordure": "#D9E2EC",
    "erreur": "#C0392B",
}


def afficher_guides():
    from tkinter import messagebox

    messagebox.showinfo(
        "Guides d'utilisation",
        "📚 Guides MathCraft\n\n"
        "1. Opérations de base : Addition, soustraction, multiplication, division\n"
        "2. Théorie des nombres : PGCD, PPCM, nombres premiers\n"
        "3. Conversion : Bases numériques, unités de mesure\n"
        "4. Explorateur de concepts : Jeu éducatif mathématique\n"
        "5. Polynômes : Résolution d'équations polynomiales\n"
        "6. Chaînes de caractères : Manipulation de texte\n"
        "7. Intégration numérique : Calculs d'intégrales\n\n"
        "Chaque module contient ses instructions détaillées."
    )


def afficher_a_propos():
    from tkinter import messagebox

    messagebox.showinfo(
        "À propos de MathCraft",
        "🧮 MathCraft v1.0\n\n"
        "Un espace malin pour calculer, apprendre et jouer avec les maths.\n\n"
        "Développé par Junior Kossivi\n"
        "© 2026 - Tous droits réservés\n\n"
        "Modules disponibles :\n"
        "- Opérations de base\n"
        "- Théorie des nombres\n"
        "- Conversion\n"
        "- Explorateur de concepts\n"
        "- Polynômes et équations\n"
        "- Chaînes de caractères\n"
        "- Intégration numérique\n"
        "- Résolution d'équations numériques\n"
        "- Interpolation linéaire"
    )


fenetre = Tk()
fenetre.title("MathCraft")
window_width, window_height = ResponsiveUIManager.get_safe_window_geometry(base_width=1240, base_height=820)
ResponsiveUIManager.center_window(fenetre, window_width, window_height)
fenetre.minsize(980, 680)
fenetre.configure(bg=PALETTE["fond_principal"])

ensure_styles_configured(PALETTE)
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure(
    "Custom.TButton",
    foreground=PALETTE["fond_secondaire"],
    background=PALETTE["primaire"],
    font=("Century Gothic", 12, "bold"),
    padding=14,
    relief="flat",
    borderwidth=0,
)
style.map(
    "Custom.TButton",
    background=[("active", PALETTE["secondaire"]), ("pressed", "#0B3C66")],
    foreground=[("active", PALETTE["fond_secondaire"])],
)
style.configure(
    "Quit.TButton",
    foreground=PALETTE["fond_secondaire"],
    background=PALETTE["erreur"],
    font=("Century Gothic", 12, "bold"),
    padding=14,
    relief="flat",
    borderwidth=0,
)
style.map(
    "Quit.TButton",
    background=[("active", "#A93226"), ("pressed", "#922B21")],
    foreground=[("active", PALETTE["fond_secondaire"])],
)


def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()


def show_module(func):
    clear_content()
    try:
        func(parent=content_frame)
    except TypeError:
        func()


def _bind_sidebar_scroll():
    def _on_sidebar_wheel(event):
        sidebar_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    def _enable_scroll(_event):
        sidebar_canvas.bind_all("<MouseWheel>", _on_sidebar_wheel)

    def _disable_scroll(_event):
        sidebar_canvas.unbind_all("<MouseWheel>")

    sidebar_canvas.bind("<Enter>", _enable_scroll)
    sidebar_canvas.bind("<Leave>", _disable_scroll)


def _animate_fade_in(root, step=0.06):
    try:
        root.attributes("-alpha", 0.0)
    except Exception:
        return

    alpha_state = {"value": 0.0}

    def _tick():
        alpha_state["value"] = min(1.0, alpha_state["value"] + step)
        try:
            root.attributes("-alpha", alpha_state["value"])
        except Exception:
            return
        if alpha_state["value"] < 1.0:
            root.after(18, _tick)

    root.after(20, _tick)


def _stagger_buttons(buttons):
    for index, button in enumerate(buttons):
        fenetre.after(
            70 * index,
            lambda b=button: b.pack(pady=7, fill=X, padx=16),
        )


def creer_menu_burger():
    header_wrap = Frame(fenetre, bg=PALETTE["fond_principal"])
    header_wrap.pack(fill=X, padx=18, pady=(12, 8))

    header_card = Frame(
        header_wrap,
        bg=PALETTE["fond_secondaire"],
        highlightbackground=PALETTE["bordure"],
        highlightthickness=1,
    )
    header_card.pack(fill=X)

    burger_btn = Menubutton(
        header_card,
        text="☰",
        font=("Century Gothic", 16, "bold"),
        fg=PALETTE["primaire"],
        bg=PALETTE["fond_secondaire"],
        relief="flat",
        bd=0,
        cursor="hand2",
        width=3,
        activebackground=PALETTE["fond_contraste"],
        activeforeground=PALETTE["primaire"],
    )
    burger_btn.pack(side=LEFT, padx=(12, 8), pady=10)

    title_block = Frame(header_card, bg=PALETTE["fond_secondaire"])
    title_block.pack(side=LEFT, pady=8)
    Label(
        title_block,
        text="MathCraft",
        font=("Century Gothic", 21, "bold"),
        fg=PALETTE["texte_fonce"],
        bg=PALETTE["fond_secondaire"],
    ).pack(anchor="w")
    Label(
        title_block,
        text="Calculer, apprendre, explorer",
        font=("Century Gothic", 10),
        fg=PALETTE["texte_clair"],
        bg=PALETTE["fond_secondaire"],
    ).pack(anchor="w")

    status = Label(
        header_card,
        text="● 9 modules actifs",
        font=("Century Gothic", 10, "bold"),
        fg=PALETTE["accent"],
        bg=PALETTE["fond_secondaire"],
    )
    status.pack(side=RIGHT, padx=14)

    menu = Menu(
        burger_btn,
        tearoff=0,
        bg=PALETTE["fond_secondaire"],
        fg=PALETTE["texte_fonce"],
        font=("Century Gothic", 10),
        activebackground=PALETTE["fond_contraste"],
        activeforeground=PALETTE["texte_fonce"],
    )
    menu.add_command(label="📚 Guides", command=afficher_guides)
    menu.add_command(label="❤️ Soutenir", command=lambda: afficher_soutien(fenetre))
    menu.add_separator()
    menu.add_command(label="ℹ️ À propos", command=afficher_a_propos)
    burger_btn.config(menu=menu)


creer_menu_burger()

main_area = Frame(fenetre, bg=PALETTE["fond_principal"])
main_area.pack(pady=(4, 14), padx=18, fill=BOTH, expand=True)

sidebar_shell = Frame(
    main_area,
    bg=PALETTE["fond_secondaire"],
    width=420,
    highlightbackground=PALETTE["bordure"],
    highlightthickness=1,
)
sidebar_shell.pack(side=LEFT, fill=Y, expand=False)
sidebar_shell.pack_propagate(False)

sidebar_canvas = Canvas(sidebar_shell, bg=PALETTE["fond_secondaire"], highlightthickness=0)
sidebar_scrollbar = ttk.Scrollbar(sidebar_shell, orient="vertical", command=sidebar_canvas.yview)
sidebar_inner = Frame(sidebar_canvas, bg=PALETTE["fond_secondaire"])
sidebar_inner.bind("<Configure>", lambda event: sidebar_canvas.configure(scrollregion=sidebar_canvas.bbox("all")))
sidebar_canvas.create_window((0, 0), window=sidebar_inner, anchor="nw")
sidebar_canvas.configure(yscrollcommand=sidebar_scrollbar.set)
sidebar_canvas.pack(side=LEFT, fill=BOTH, expand=True)
sidebar_scrollbar.pack(side=RIGHT, fill=Y)
_bind_sidebar_scroll()

content_frame = Frame(
    main_area,
    bg=PALETTE["fond_secondaire"],
    highlightbackground=PALETTE["bordure"],
    highlightthickness=1,
)
content_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(16, 0))

historique_interface = InterfaceHistorique(parent=fenetre)

hero = Frame(content_frame, bg=PALETTE["fond_secondaire"])
hero.pack(fill=X, padx=24, pady=(20, 8))
Label(
    hero,
    text="🧠 Bienvenue dans votre atelier mathématique",
    font=("Century Gothic", 17, "bold"),
    fg=PALETTE["texte_fonce"],
    bg=PALETTE["fond_secondaire"],
).pack(anchor="w")

subtitle = Label(
    hero,
    text="Choisissez un module à gauche pour lancer vos exercices et calculs.",
    font=("Century Gothic", 11),
    fg=PALETTE["texte_clair"],
    bg=PALETTE["fond_secondaire"],
)
subtitle.pack(anchor="w", pady=(4, 10))

ttk.Separator(content_frame, orient="horizontal").pack(fill="x", padx=24, pady=(0, 12))

Label(
    sidebar_inner,
    text="Modules",
    fg=PALETTE["texte_fonce"],
    bg=PALETTE["fond_secondaire"],
    font=("Century Gothic", 15, "bold"),
    justify="left",
).pack(pady=(16, 4), padx=16, anchor="w")

Label(
    sidebar_inner,
    text="Accès rapide à tous les outils",
    fg=PALETTE["texte_clair"],
    bg=PALETTE["fond_secondaire"],
    font=("Century Gothic", 10),
).pack(pady=(0, 12), padx=16, anchor="w")

module_buttons = []
module_defs = [
    ("Module 1  |  Opérations de base 🧮", lambda: show_module(op.launch_operation)),
    ("Module 2  |  Théorie des nombres ➕", lambda: show_module(theorie.lancer_theorie)),
    ("Module 3  |  Conversion ⚖️", lambda: show_module(conv.launch_conversion)),
    ("Module 4  |  Explorateur de concepts 🎯", lambda: show_module(exp_concepts.lancer_explorateur_concepts)),
    ("Module 5  |  Polynômes et équations 📈", lambda: show_module(poly.lancer_polynome)),
    ("Module 6  |  Chaînes de caractères 🔠", lambda: show_module(ch.lancer_chaine)),
    ("Module 7  |  Intégration numérique 📊", lambda: show_module(int_num.lancer_integration_numerique)),
    ("Module 8  |  Équations numériques 🟰", lambda: show_module(eq_num.lancer_equation_Numerique)),
    ("Module 9  |  Interpolation linéaire 📉", lambda: show_module(int_lin.lancer_interpolation_numerique)),
    ("📚 Historique des calculs", lambda: historique_interface.afficher_historique(parent=content_frame)),
]
for text, command in module_defs:
    module_buttons.append(ttk.Button(sidebar_inner, text=text, style="Custom.TButton", command=command))
_stagger_buttons(module_buttons)

ttk.Separator(sidebar_inner, orient="horizontal").pack(fill="x", padx=14, pady=18)
ttk.Button(
    sidebar_inner,
    text="Quitter l'application",
    style="Quit.TButton",
    command=fenetre.destroy,
).pack(pady=(0, 16), fill=X, padx=16)

footer = Label(
    content_frame,
    text="© 2026 MathCraft - Développé par Junior Kossivi",
    font=("Century Gothic", 9),
    fg="#8795A1",
    bg=PALETTE["fond_secondaire"],
)
footer.pack(pady=(22, 16), padx=20, anchor="center", side=BOTTOM)


def animate_subtitle():
    colors = [PALETTE["texte_clair"], "#4A637A", PALETTE["texte_clair"]]
    state = {"idx": 0}

    def _tick():
        subtitle.configure(fg=colors[state["idx"]])
        state["idx"] = (state["idx"] + 1) % len(colors)
        fenetre.after(850, _tick)

    _tick()


_animate_fade_in(fenetre)
animate_subtitle()
fenetre.mainloop()
