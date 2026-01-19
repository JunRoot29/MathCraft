"""
scrollable_ui.py - Module pour gérer les scrollbars dans les interfaces complexes
Auteur: Junior Kossivi
Description: Utilitaires pour rendre les interfaces scrollables
"""

import tkinter as tk
from tkinter import ttk


class ScrollableNotebook(ttk.Notebook):
    """
    Notebook avec support de scrollbar pour les onglets
    Utile quand il y a beaucoup d'onglets
    """
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Binding pour gérer l'espace et la molette
        self.bind("<MouseWheel>", self._on_scroll)
        self.bind("<Button-4>", self._on_scroll)   # Linux scroll up
        self.bind("<Button-5>", self._on_scroll)   # Linux scroll down
    
    def _on_scroll(self, event):
        """Gérer le scroll sur les onglets"""
        # Déterminer la direction
        if event.num == 5 or event.delta < 0:
            direction = 1  # Scroll down
        elif event.num == 4 or event.delta > 0:
            direction = -1  # Scroll up
        else:
            return
        
        # Trouver l'onglet courant et aller au suivant
        try:
            tabs = self.tabs()
            current = self.index(self.select())
            next_tab = (current + direction) % len(tabs)
            self.select(next_tab)
        except:
            pass


class ScrollableTextWidget(ttk.Frame):
    """
    Widget Text avec scrollbar intégrée
    Parfait pour afficher du texte long
    """
    
    def __init__(self, parent, height=10, width=50, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget
        self.text = tk.Text(self, height=height, width=width, 
                           yscrollcommand=scrollbar.set, wrap=tk.WORD)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.text.yview)
        
        # Binding molette souris
        self.text.bind("<MouseWheel>", self._on_mousewheel)
        self.text.bind("<Button-4>", self._on_mousewheel)
        self.text.bind("<Button-5>", self._on_mousewheel)
    
    def _on_mousewheel(self, event):
        """Gérer le scroll à la molette"""
        if event.num == 5 or event.delta < 0:
            self.text.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            self.text.yview_scroll(-1, "units")
        return "break"
    
    def get(self, *args):
        """Obtenir le texte"""
        return self.text.get(*args)
    
    def insert(self, *args):
        """Insérer du texte"""
        return self.text.insert(*args)
    
    def delete(self, *args):
        """Supprimer du texte"""
        return self.text.delete(*args)
    
    def config(self, **kwargs):
        """Configurer le widget"""
        self.text.config(**kwargs)


class ScrollableFrame(ttk.Frame):
    """
    Frame avec scrollbar automatique et responsive
    Parfait pour les formulaires longs
    """
    
    def __init__(self, parent, bg=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Déterminer la couleur de fond
        if bg is None:
            bg = '#F0F4F8'
        
        # Canvas principal
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        # Frame scrollable
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Créer la fenêtre dans le canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Support du redimensionnement du canvas
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        # Support de la molette souris
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind("<Button-4>", self._on_mousewheel)
        self.scrollable_frame.bind("<Button-5>", self._on_mousewheel)
        
        # Binding pour tous les enfants
        self._bind_mousewheel_recursively(self.scrollable_frame)
        
        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _on_canvas_configure(self, event):
        """Adapter la largeur du frame scrollable à celle du canvas"""
        self.canvas.itemconfig(self.canvas_window, width=event.width)
    
    def _on_mousewheel(self, event):
        """Gérer le défilement à la molette"""
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(3, "units")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-3, "units")
        return "break"
    
    def _bind_mousewheel_recursively(self, widget):
        """Binder la molette souris à tous les enfants"""
        widget.bind("<MouseWheel>", self._on_mousewheel)
        widget.bind("<Button-4>", self._on_mousewheel)
        widget.bind("<Button-5>", self._on_mousewheel)
        
        for child in widget.winfo_children():
            self._bind_mousewheel_recursively(child)


class TableWithScrollbar(ttk.Frame):
    """
    Treeview (tableau) avec scrollbar horizontal et vertical
    Parfait pour afficher des données tabulaires
    """
    
    def __init__(self, parent, columns, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Frame pour les scrollbars
        scroll_frame = ttk.Frame(self)
        scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar vertical
        vscrollbar = ttk.Scrollbar(scroll_frame, orient=tk.VERTICAL)
        vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Scrollbar horizontal
        hscrollbar = ttk.Scrollbar(scroll_frame, orient=tk.HORIZONTAL)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview
        self.tree = ttk.Treeview(scroll_frame, columns=columns, 
                                 yscrollcommand=vscrollbar.set,
                                 xscrollcommand=hscrollbar.set)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Configurer scrollbars
        vscrollbar.config(command=self.tree.yview)
        hscrollbar.config(command=self.tree.xview)
        
        # Binding molette
        self.tree.bind("<MouseWheel>", self._on_mousewheel)
        self.tree.bind("<Button-4>", self._on_mousewheel)
        self.tree.bind("<Button-5>", self._on_mousewheel)
    
    def _on_mousewheel(self, event):
        """Gérer le scroll"""
        if event.num == 5 or event.delta < 0:
            self.tree.yview_scroll(3, "units")
        elif event.num == 4 or event.delta > 0:
            self.tree.yview_scroll(-3, "units")
        return "break"


class ExpandableFrame(ttk.Frame):
    """
    Frame qui peut être étendu/réduit pour révéler/cacher du contenu
    Util pour les interfaces complexes avec beaucoup d'options
    """
    
    def __init__(self, parent, title="Options", **kwargs):
        super().__init__(parent, **kwargs)
        
        # Header clickable
        self.header = ttk.Frame(self)
        self.header.pack(fill=tk.X, padx=5, pady=5)
        
        # Arrow indicator et titre
        self.arrow = tk.Label(self.header, text="▶ " + title, cursor="hand2")
        self.arrow.pack(side=tk.LEFT)
        
        # Separator
        ttk.Separator(self).pack(fill=tk.X, padx=5, pady=5)
        
        # Content frame (scrollable)
        self.content_frame = ScrollableFrame(self, bg=self.cget('bg'))
        
        # Variables
        self.is_expanded = True
        
        # Binding
        self.arrow.bind("<Button-1>", self._toggle)
        
    def _toggle(self, event=None):
        """Basculer entre étendu et réduit"""
        if self.is_expanded:
            self.content_frame.pack_forget()
            self.arrow.config(text="▼ " + self.arrow.cget("text")[2:])
            self.is_expanded = False
        else:
            self.content_frame.pack(fill=tk.BOTH, expand=True)
            self.arrow.config(text="▶ " + self.arrow.cget("text")[2:])
            self.is_expanded = True


class HorizontalScrolledFrame(ttk.Frame):
    """
    Frame avec scrollbar horizontal
    Utile pour les contenus larges
    """
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Configure grid weight
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Canvas
        self.canvas = tk.Canvas(self, highlightthickness=0, bg="white", height=100)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar horizontal
        scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Frame scrollable
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        # Créer la window dans le canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Bind configure pour update scrollregion
        def on_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            # Stretch frame to canvas height if needed
            if self.scrollable_frame.winfo_reqheight() < event.height:
                self.canvas.itemconfig(self.canvas_window, height=event.height)
        
        self.scrollable_frame.bind("<Configure>", on_configure)
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width))
        
        # Configure canvas scroll
        self.canvas.configure(xscrollcommand=scrollbar.set)
        
        # Bind mouse wheel
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel_h)
        self.scrollable_frame.bind("<Button-4>", self._on_mousewheel_h)
        self.scrollable_frame.bind("<Button-5>", self._on_mousewheel_h)
    
    def _on_mousewheel_h(self, event):
        """Handle horizontal mouse wheel scroll"""
        if event.num == 5 or event.delta < 0:
            self.canvas.xview_scroll(3, "units")
        elif event.num == 4 or event.delta > 0:
            self.canvas.xview_scroll(-3, "units")


def create_scrollable_container(parent, bg='#F0F4F8'):
    """Créer rapidement un conteneur scrollable"""
    return ScrollableFrame(parent, bg=bg)


def add_horizontal_scrollbar_to_widget(widget):
    """Ajouter une scrollbar horizontale à un widget existant"""
    parent = widget.master
    
    # Créer les scrollbars
    hscrollbar = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, command=widget.xview)
    
    if hasattr(widget, 'config'):
        widget.config(xscrollcommand=hscrollbar.set)
    
    return hscrollbar
