"""
responsive_ui.py - Module pour rendre les interfaces adaptables aux différentes résolutions d'écran
Auteur: Junior Kossivi
Description: Fournit des utilitaires pour adapter dynamiquement les interfaces Tkinter
"""

import tkinter as tk
from tkinter import ttk

class ResponsiveUIManager:
    """Gère les dimensions et l'adaptabilité des interfaces"""
    
    # Résolutions standards
    SCREEN_BREAKPOINTS = {
        'small': 800,      # Écrans < 800px
        'medium': 1366,    # Écrans 800-1366px
        'large': 1920,     # Écrans 1366-1920px
        'xlarge': 2560,    # Écrans > 1920px
    }
    _cached_screen_size = None
    
    @staticmethod
    def get_screen_size():
        """Obtenir la résolution de l'écran"""
        if ResponsiveUIManager._cached_screen_size:
            return ResponsiveUIManager._cached_screen_size

        root = tk._default_root
        created_temp_root = False
        if root is None:
            root = tk.Tk()
            root.withdraw()
            created_temp_root = True

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        if created_temp_root:
            root.destroy()

        ResponsiveUIManager._cached_screen_size = (width, height)
        return width, height
    
    @staticmethod
    def get_screen_category():
        """Catégoriser l'écran selon sa taille"""
        width, _ = ResponsiveUIManager.get_screen_size()
        
        if width < ResponsiveUIManager.SCREEN_BREAKPOINTS['small']:
            return 'small'
        elif width < ResponsiveUIManager.SCREEN_BREAKPOINTS['medium']:
            return 'medium'
        elif width < ResponsiveUIManager.SCREEN_BREAKPOINTS['large']:
            return 'large'
        else:
            return 'xlarge'
    
    @staticmethod
    def calculate_window_size(category, base_width=800, base_height=600):
        """
        Calculer la taille adaptée de la fenêtre selon la catégorie d'écran
        
        Args:
            category: 'small', 'medium', 'large', 'xlarge'
            base_width: largeur de base
            base_height: hauteur de base
            
        Returns:
            tuple: (width, height)
        """
        scaling = {
            'small': 0.7,      # 70% de la base pour petits écrans
            'medium': 0.9,     # 90% de la base pour écrans moyens
            'large': 1.0,      # 100% de la base
            'xlarge': 1.1,     # 110% de la base pour très grands écrans
        }
        
        scale = scaling.get(category, 1.0)
        width = int(base_width * scale)
        height = int(base_height * scale)
        
        return width, height
    
    @staticmethod
    def calculate_max_size_for_screen(margin=100):
        """
        Calculer la taille maximale disponible sur l'écran
        
        Args:
            margin: marge à respecter autour
            
        Returns:
            tuple: (max_width, max_height)
        """
        screen_width, screen_height = ResponsiveUIManager.get_screen_size()
        max_width = screen_width - margin
        max_height = screen_height - margin
        
        return max_width, max_height
    
    @staticmethod
    def get_safe_window_geometry(base_width=800, base_height=600):
        """
        Calculer une géométrie sûre qui s'adapte à l'écran
        
        Args:
            base_width: largeur souhaitée
            base_height: hauteur souhaitée
            
        Returns:
            tuple: (width, height)
        """
        category = ResponsiveUIManager.get_screen_category()
        screen_width, screen_height = ResponsiveUIManager.get_screen_size()
        
        # Calculer la taille adaptée
        width, height = ResponsiveUIManager.calculate_window_size(category, base_width, base_height)
        
        # S'assurer que la fenêtre ne dépasse pas l'écran
        max_width, max_height = ResponsiveUIManager.calculate_max_size_for_screen(margin=50)
        width = min(width, max_width)
        height = min(height, max_height)
        
        return width, height
    
    @staticmethod
    def center_window(window, width, height):
        """Centrer la fenêtre sur l'écran"""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    @staticmethod
    def get_font_size(category, base_size=12):
        """Adapter la taille de police selon la résolution"""
        scaling = {
            'small': 0.8,      # 80% pour petit écran
            'medium': 0.9,     # 90% pour moyen
            'large': 1.0,      # 100% pour grand
            'xlarge': 1.1,     # 110% pour très grand
        }
        
        scale = scaling.get(category, 1.0)
        return int(base_size * scale)


class ScrollableFrame(ttk.Frame):
    """
    Frame avec scrollbar automatique et responsive
    Permet de créer des interfaces scrollables facilement
    """
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Canvas pour scrolling
        self.canvas = tk.Canvas(self, bg=parent.cget('bg') if hasattr(parent, 'cget') else '#F0F4F8')
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        # Frame scrollable
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Support de la molette souris
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind("<Button-4>", self._on_mousewheel)  # Linux scroll up
        self.scrollable_frame.bind("<Button-5>", self._on_mousewheel)  # Linux scroll down
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)
        
        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _on_mousewheel(self, event):
        """Gérer le défilement à la molette"""
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")


class ResponsiveLabel(tk.Label):
    """Label avec police adaptable"""
    
    def __init__(self, parent, text="", base_size=12, **kwargs):
        self.base_size = base_size
        category = ResponsiveUIManager.get_screen_category()
        font_size = ResponsiveUIManager.get_font_size(category, base_size)
        
        font = kwargs.pop('font', None)
        if font:
            if isinstance(font, tuple):
                font = (font[0], font_size) + font[2:]
            else:
                font = (font, font_size)
        else:
            font = ("Century Gothic", font_size)
        
        super().__init__(parent, text=text, font=font, **kwargs)


class ResponsiveButton(ttk.Button):
    """Button avec style adaptatif"""
    
    def __init__(self, parent, text="", base_size=12, **kwargs):
        self.base_size = base_size
        super().__init__(parent, text=text, **kwargs)


class ResponsiveEntry(ttk.Entry):
    """Entry avec police adaptable"""
    
    def __init__(self, parent, base_size=12, **kwargs):
        self.base_size = base_size
        super().__init__(parent, **kwargs)
        
        category = ResponsiveUIManager.get_screen_category()
        font_size = ResponsiveUIManager.get_font_size(category, base_size)
        font = ("Century Gothic", font_size)
        self.configure(font=font)


def create_responsive_window(parent=None, title="MathCraft", base_width=800, base_height=600):
    """
    Créer une fenêtre responsive centrée
    
    Args:
        parent: fenêtre parente
        title: titre de la fenêtre
        base_width: largeur de base souhaitée
        base_height: hauteur de base souhaitée
        
    Returns:
        Toplevel: la fenêtre créée
    """
    window = tk.Toplevel(parent)
    window.title(title)
    
    # Calculer les dimensions adaptées
    width, height = ResponsiveUIManager.get_safe_window_geometry(base_width, base_height)
    
    # Centrer et géométrie
    ResponsiveUIManager.center_window(window, width, height)
    
    # Permettre le redimensionnement pour très petits écrans
    window.resizable(True, True)
    
    return window


def add_responsive_padding(widget, category=None):
    """Ajouter du padding adaptatif"""
    if category is None:
        category = ResponsiveUIManager.get_screen_category()
    
    padding = {
        'small': 5,
        'medium': 10,
        'large': 15,
        'xlarge': 20,
    }
    
    pad = padding.get(category, 10)
    return pad


def create_header_bar(parent, title="Module", on_return_callback=None):
    """
    Crée une bande bleue header avec titre et optionnellement bouton retour
    
    Args:
        parent: Frame parent
        title: Titre à afficher
        on_return_callback: Callback pour bouton retour (optionnel)
    
    Returns:
        Frame: Le header frame créé
    """
    from .styles import ensure_styles_configured

    ensure_styles_configured()

    # Header frame bleu
    header = tk.Frame(parent, bg="#1E40AF", height=60)
    header.pack(fill=tk.X, side=tk.TOP)
    header.pack_propagate(False)
    
    # Bouton retour (si callback fourni)
    if on_return_callback:
        btn_return = ttk.Button(
            header,
            text="🔙 Retour",
            style="Return.Header.TButton",
            command=on_return_callback,
        )
        btn_return.pack(side=tk.LEFT, padx=10, pady=10)
    
    # Titre au centre/gauche
    title_label = tk.Label(header, text=title, 
                          font=("Century Gothic", 14, "bold"),
                          fg="white", bg="#1E40AF")
    title_label.pack(side=tk.LEFT, padx=15, pady=10)
    
    return header
