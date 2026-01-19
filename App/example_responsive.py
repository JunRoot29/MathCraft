"""
example_responsive_interface.py - Exemples d'utilisation des modules responsive et scrollable
Auteur: Junior Kossivi
Description: Démontre comment utiliser les nouveaux modules d'adaptabilité
"""

import tkinter as tk
from tkinter import ttk
from App.responsive_ui import (
    ResponsiveUIManager, create_responsive_window, 
    ScrollableFrame as ResponsiveScrollableFrame
)
from App.scrollable_ui import (
    ScrollableFrame, ScrollableTextWidget, TableWithScrollbar,
    ExpandableFrame, HorizontalScrolledFrame, ScrollableNotebook
)


def example_1_basic_responsive_window():
    """Exemple 1 : Fenêtre responsive simple"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 1")
    root.geometry("800x600")
    
    def open_responsive():
        # Créer une fenêtre qui s'adapte automatiquement
        window = create_responsive_window(root, "Fenêtre Responsive", base_width=600, base_height=400)
        
        label = tk.Label(window, text="Cette fenêtre s'adapte à votre résolution !", 
                        font=("Century Gothic", 14), pady=20)
        label.pack()
        
        info = tk.Label(window, text=f"Catégorie écran: {ResponsiveUIManager.get_screen_category()}", 
                       font=("Century Gothic", 10))
        info.pack()
        
        screen_size = ResponsiveUIManager.get_screen_size()
        size_info = tk.Label(window, text=f"Résolution écran: {screen_size[0]}x{screen_size[1]}", 
                           font=("Century Gothic", 10))
        size_info.pack()
    
    btn = tk.Button(root, text="Ouvrir Fenêtre Responsive", command=open_responsive)
    btn.pack(pady=20)
    
    root.mainloop()


def example_2_scrollable_form():
    """Exemple 2 : Formulaire scrollable"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 2 : Formulaire Scrollable")
    root.geometry("500x400")
    
    label = tk.Label(root, text="Formulaire avec beaucoup de champs (scrollable)", 
                    font=("Century Gothic", 12, "bold"), pady=10)
    label.pack()
    
    # Créer un frame scrollable
    scrollable = ScrollableFrame(root, bg='#F0F4F8')
    scrollable.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Ajouter beaucoup de champs
    for i in range(20):
        frame = tk.Frame(scrollable.scrollable_frame, bg='#FFFFFF', relief=tk.SUNKEN, bd=1)
        frame.pack(fill=tk.X, pady=5, padx=5)
        
        label = tk.Label(frame, text=f"Champ {i+1}:", bg='#FFFFFF', fg='#1E40AF')
        label.pack(side=tk.LEFT, padx=5, pady=5)
        
        entry = tk.Entry(frame)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
    
    root.mainloop()


def example_3_table_with_scrollbars():
    """Exemple 3 : Tableau avec scrollbars H/V"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 3 : Tableau Scrollable")
    root.geometry("700x400")
    
    label = tk.Label(root, text="Tableau avec Scrollbars Horizontal et Vertical", 
                    font=("Century Gothic", 12, "bold"), pady=10)
    label.pack()
    
    # Créer un tableau
    columns = ['ID', 'Nom', 'Valeur', 'Erreur', 'Statut', 'Détails', 'Actions']
    table = TableWithScrollbar(root, columns)
    table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Configurer les en-têtes
    table.tree.heading('#0', text='')
    for col in columns:
        table.tree.heading(col, text=col)
        table.tree.column(col, width=100)
    
    # Ajouter beaucoup de données
    for i in range(100):
        values = [f'ID{i:03d}', f'Item{i}', f'{i*1.5:.2f}', f'{i*0.01:.4f}', 
                 'OK' if i % 2 == 0 else 'ERREUR', f'Détail long pour item {i}', 'Action']
        table.tree.insert('', 'end', values=values)
    
    root.mainloop()


def example_4_expandable_sections():
    """Exemple 4 : Sections expansibles"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 4 : Sections Expansibles")
    root.geometry("600x400")
    
    label = tk.Label(root, text="Cliquez sur les titres pour développer/réduire", 
                    font=("Century Gothic", 12, "bold"), pady=10)
    label.pack()
    
    # Créer un frame scrollable pour contenir les sections
    main_scroll = ScrollableFrame(root, bg='#F0F4F8')
    main_scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Ajouter plusieurs sections expansibles
    for section_num in range(5):
        section = ExpandableFrame(main_scroll.scrollable_frame, 
                                 title=f"Section {section_num + 1}")
        section.pack(fill=tk.X, pady=5)
        
        # Ajouter du contenu dans la section
        for item_num in range(3):
            label = tk.Label(section.content_frame.scrollable_frame, 
                           text=f"  → Item {item_num + 1}", 
                           bg='#FFFFFF')
            label.pack(fill=tk.X, padx=10, pady=2)
    
    root.mainloop()


def example_5_text_with_scrollbar():
    """Exemple 5 : Text widget avec scrollbar"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 5 : Text Widget Scrollable")
    root.geometry("600x400")
    
    label = tk.Label(root, text="Text Widget avec Scrollbar et Support Molette Souris", 
                    font=("Century Gothic", 12, "bold"), pady=10)
    label.pack()
    
    # Créer un text widget scrollable
    text_widget = ScrollableTextWidget(root, height=20, width=60)
    text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Ajouter du texte
    texte_long = """
    Ceci est un texte de démonstration.
    
    Vous pouvez utiliser la molette souris pour défiler.
    """ + "\n".join([f"Ligne {i}" for i in range(1, 50)])
    
    text_widget.insert(1.0, texte_long)
    text_widget.text.config(state=tk.DISABLED)  # Lecture seule
    
    root.mainloop()


def example_6_responsive_fonts():
    """Exemple 6 : Polices adaptatives"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 6 : Polices Adaptatives")
    root.geometry("600x400")
    
    # Obtenir la catégorie d'écran
    category = ResponsiveUIManager.get_screen_category()
    
    label = tk.Label(root, text=f"Votre écran : {category.upper()}", 
                    font=("Century Gothic", 14, "bold"), pady=20)
    label.pack()
    
    # Afficher les tailles de police adaptées
    sizes = [8, 10, 12, 14, 16, 18, 20]
    
    for base_size in sizes:
        adapted_size = ResponsiveUIManager.get_font_size(category, base_size)
        label = tk.Label(root, 
                        text=f"Base: {base_size}px → Adapté: {adapted_size}px", 
                        font=("Century Gothic", adapted_size))
        label.pack(pady=5)
    
    root.mainloop()


def example_7_horizontal_scroll():
    """Exemple 7 : Scroll horizontal"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 7 : Scroll Horizontal")
    root.geometry("500x300")
    
    label = tk.Label(root, text="Tableau Très Large (Scroll Horizontal)", 
                    font=("Century Gothic", 12, "bold"), pady=10)
    label.pack()
    
    # Créer un frame avec scroll horizontal
    h_scroll = HorizontalScrolledFrame(root)
    h_scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Ajouter beaucoup de boutons en ligne
    for i in range(50):
        btn = tk.Button(h_scroll.scrollable_frame, text=f"Btn{i}", width=10, height=3)
        btn.pack(side=tk.LEFT, padx=2, pady=2)
    
    root.mainloop()


def example_8_complete_interface():
    """Exemple 8 : Interface complète avec tous les éléments"""
    root = tk.Tk()
    root.title("MathCraft - Exemple 8 : Interface Complète")
    
    # Utiliser une fenêtre responsive
    window = create_responsive_window(root, "Interface Complète", base_width=800, base_height=600)
    
    # Titre
    title = tk.Label(window, text="Interface Responsive et Scrollable", 
                    font=("Century Gothic", 16, "bold"), bg='#1E40AF', fg='white', pady=10)
    title.pack(fill=tk.X)
    
    # Créer un notebook (onglets) scrollable
    notebook = ScrollableNotebook(window)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Onglet 1 : Formulaire
    frame1 = ttk.Frame(notebook)
    notebook.add(frame1, text="Formulaire")
    
    scroll1 = ScrollableFrame(frame1, bg='#F0F4F8')
    scroll1.pack(fill=tk.BOTH, expand=True)
    
    for i in range(15):
        label = tk.Label(scroll1.scrollable_frame, text=f"Champ {i+1}:")
        label.pack(pady=5)
        entry = tk.Entry(scroll1.scrollable_frame)
        entry.pack(fill=tk.X, padx=5, pady=2)
    
    # Onglet 2 : Tableau
    frame2 = ttk.Frame(notebook)
    notebook.add(frame2, text="Données")
    
    cols = ['Colonne 1', 'Colonne 2', 'Colonne 3']
    table = TableWithScrollbar(frame2, cols)
    table.pack(fill=tk.BOTH, expand=True)
    
    for i in range(50):
        table.tree.insert('', 'end', values=[f'Data{i}', f'{i*2}', f'{i*3}'])
    
    # Onglet 3 : Texte
    frame3 = ttk.Frame(notebook)
    notebook.add(frame3, text="Texte")
    
    text_w = ScrollableTextWidget(frame3, height=15, width=50)
    text_w.pack(fill=tk.BOTH, expand=True)
    text_w.insert(1.0, "Texte exemple.\n" * 30)
    
    window.mainloop()


# Menu principal
if __name__ == "__main__":
    root = tk.Tk()
    root.title("MathCraft - Exemples Responsive & Scrollable")
    root.geometry("500x300")
    
    label = tk.Label(root, text="Choisissez un exemple", 
                    font=("Century Gothic", 14, "bold"), pady=20)
    label.pack()
    
    buttons = [
        ("1. Fenêtre Responsive Simple", example_1_basic_responsive_window),
        ("2. Formulaire Scrollable", example_2_scrollable_form),
        ("3. Tableau avec Scrollbars", example_3_table_with_scrollbars),
        ("4. Sections Expansibles", example_4_expandable_sections),
        ("5. Text Widget Scrollable", example_5_text_with_scrollbar),
        ("6. Polices Adaptatives", example_6_responsive_fonts),
        ("7. Scroll Horizontal", example_7_horizontal_scroll),
        ("8. Interface Complète", example_8_complete_interface),
    ]
    
    for text, command in buttons:
        btn = tk.Button(root, text=text, command=command, width=40, height=2)
        btn.pack(pady=5)
    
    root.mainloop()
