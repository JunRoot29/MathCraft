from tkinter import *
from tkinter import ttk

# Palette unifiée (identique à polynome.py et conversion.py)
PALETTE = {
    "fond_principal": "#F0F4F8",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6", 
    "erreur": "#DC2626",
    "texte_fonce": "#1E40AF",
    "texte_clair": "#1E40AF"
}


def lancer_interpolation_Numerique ():
    page_interpolation = Toplevel()
    page_interpolation.title("Interpolation Numérique")
    page_interpolation.geometry("600x300")
    page_interpolation.configure(bg=PALETTE["fond_principal"])

    
    style = ttk.Style(page_interpolation)
    style.theme_use('clam')

    style.configure("Quit.TButton",
                foreground="#FFFFFF",
                background="#DC2626",
                font=("Century Gothic", 14),
                relief="flat")

    Label(page_interpolation, text= "😥Oups, l'interpolation linéaire est en Dévelopement...\n\nEt sera bientôt Disponible✨😊",font=("Century Gothic",16,),bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
    Label(page_interpolation, text= "A bientot👋😊",font=("Century Gothic",16),bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()

    bouton_quit = ttk.Button(
    page_interpolation,
    text="Quitter",
    style="Quit.TButton",
    compound=LEFT,
    command=page_interpolation.destroy
)
    bouton_quit.pack(pady=10, fill=X, padx=60)
    
    # === PIED DE PAGE ===
    footer = Label(
        page_interpolation,
        text="©MathsCraft - Interface Interpolation Numérique",
        font=("Century Gothic", 9),
        fg="#94A3B8",
        bg="#F0F4F8"
    )
    footer.pack(pady=(30, 20))
    
