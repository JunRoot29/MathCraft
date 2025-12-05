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


def lancer_equation_Numerique ():
    page_equation_num = Toplevel()
    page_equation_num.title("Equation Numérique")
    page_equation_num.geometry("600x300")
    page_equation_num.configure(bg=PALETTE["fond_principal"])

    
    style = ttk.Style(page_equation_num)
    style.theme_use('clam')

    style.configure("Quit.TButton",
                foreground="#FFFFFF",
                background="#DC2626",
                font=("Century Gothic", 14),
                relief="flat")

    Label(page_equation_num, text= "😥Oups, l'Equation Numérique est en Dévelopement...\n\nEt sera bientôt Disponible✨😊",font=("Century Gothic",16,),bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()
    Label(page_equation_num, text= "A bientot👋😊",font=("Century Gothic",16),bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack()

    bouton_quit = ttk.Button(
    page_equation_num,
    text="Quitter",
    style="Quit.TButton",
    compound=LEFT,
    command=page_equation_num.destroy
)
    bouton_quit.pack(pady=10, fill=X, padx=60)
    
    # === PIED DE PAGE ===
    footer = Label(
        page_equation_num,
        text="©MathsCraft - Interface Equation Numérique",
        font=("Century Gothic", 9),
        fg="#94A3B8",
        bg="#F0F4F8"
    )
    footer.pack(pady=(30, 20))
    
