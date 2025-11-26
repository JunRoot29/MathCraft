"""
Interface pour la gestion de l'historique des calculs
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from .historique_manager import historique_manager

# Palette unifiée (identique aux autres fichiers)
PALETTE = {
    "fond_principal": "#F0F4F8",
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6", 
    "erreur": "#DC2626",
    "texte_fonce": "#1E40AF",
    "texte_clair": "#1E40AF"
}

class InterfaceHistorique:
    def __init__(self, parent=None):
        self.parent = parent
        self.fenetre = None
    
    def afficher_historique(self):
        """Affiche la fenêtre de gestion de l'historique"""
        if self.fenetre and self.fenetre.winfo_exists():
            self.fenetre.lift()
            return
        
        self.fenetre = tk.Toplevel(self.parent)
        self.fenetre.title("📊 Historique des Calculs - MathCraft")
        self.fenetre.geometry("1000x700")
        self.fenetre.configure(bg=PALETTE["fond_principal"])
        self.fenetre.minsize(800, 600)
        
        # Style
        style = ttk.Style()
        style.configure("Historique.TButton", padding=10, font=("Century Gothic", 10))
        style.configure("Historique.Treeview", font=("Century Gothic", 9))
        
        self._creer_interface()
        self._actualiser_affichage()
    
    def _creer_interface(self):
        """Crée l'interface de l'historique"""
        # Frame principal
        main_frame = ttk.Frame(self.fenetre)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # En-tête
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_frame, text="📊 Historique des Calculs", 
                font=("Century Gothic", 18, "bold"), bg=PALETTE["fond_principal"], fg=PALETTE["primaire"]).pack(side=tk.LEFT)
        
        # Barre d'outils
        toolbar_frame = ttk.Frame(main_frame)
        toolbar_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Recherche
        search_frame = ttk.Frame(toolbar_frame)
        search_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(search_frame, text="Rechercher:", font=("Century Gothic", 10), 
                bg=PALETTE["fond_principal"]).pack(side=tk.LEFT, padx=(0, 5))
        
        self.recherche_var = tk.StringVar()
        recherche_entry = ttk.Entry(search_frame, textvariable=self.recherche_var, width=30)
        recherche_entry.pack(side=tk.LEFT, padx=(0, 10))
        recherche_entry.bind("<KeyRelease>", self._rechercher)
        
        # Filtres
        filter_frame = ttk.Frame(toolbar_frame)
        filter_frame.pack(side=tk.RIGHT)
        
        tk.Label(filter_frame, text="Module:", font=("Century Gothic", 10), 
                bg=PALETTE["fond_principal"]).pack(side=tk.LEFT, padx=(0, 5))
        
        self.filtre_module = ttk.Combobox(filter_frame, values=[
            "Tous", "Opérations de Base", "Théorie des Nombres", "Conversion", 
            "Polynômes", "Chaînes de Caractères", "Intégration Numérique"
        ], state="readonly", width=20)
        self.filtre_module.set("Tous")
        self.filtre_module.pack(side=tk.LEFT, padx=(0, 10))
        self.filtre_module.bind("<<ComboboxSelected>>", self._filtrer)
        
        # Treeview pour l'historique
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tree_frame)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        h_scrollbar = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview
        columns = ("id", "date", "module", "operation", "entree", "resultat")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings",
                               yscrollcommand=v_scrollbar.set,
                               xscrollcommand=h_scrollbar.set)
        
        # Configuration des colonnes
        self.tree.heading("id", text="ID")
        self.tree.heading("date", text="Date/Heure")
        self.tree.heading("module", text="Module")
        self.tree.heading("operation", text="Opération")
        self.tree.heading("entree", text="Entrée")
        self.tree.heading("resultat", text="Résultat")
        
        self.tree.column("id", width=50)
        self.tree.column("date", width=150)
        self.tree.column("module", width=120)
        self.tree.column("operation", width=150)
        self.tree.column("entree", width=200)
        self.tree.column("resultat", width=250)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        v_scrollbar.config(command=self.tree.yview)
        h_scrollbar.config(command=self.tree.xview)
        
        # Barre d'outils basse
        bottom_toolbar = ttk.Frame(main_frame)
        bottom_toolbar.pack(fill=tk.X)
        
        # Boutons de gauche
        left_buttons = ttk.Frame(bottom_toolbar)
        left_buttons.pack(side=tk.LEFT)
        
        ttk.Button(left_buttons, text="🔄 Actualiser", 
                  command=self._actualiser_affichage, style="Historique.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(left_buttons, text="📤 Exporter JSON", 
                  command=self._exporter_json, style="Historique.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(left_buttons, text="📤 Exporter CSV", 
                  command=self._exporter_csv, style="Historique.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(left_buttons, text="📥 Importer", 
                  command=self._importer_json, style="Historique.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        # Boutons de droite
        right_buttons = ttk.Frame(bottom_toolbar)
        right_buttons.pack(side=tk.RIGHT)
        
        ttk.Button(right_buttons, text="🗑️ Supprimer sélection", 
                  command=self._supprimer_selection, style="Historique.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(right_buttons, text="🧹 Vider historique", 
                  command=self._vider_historique, style="Historique.TButton").pack(side=tk.LEFT)
        
        # Statistiques
        self.stats_label = tk.Label(main_frame, text="", font=("Century Gothic", 9), 
                                   bg=PALETTE["fond_principal"], fg=PALETTE["primaire"])
        self.stats_label.pack(pady=(10, 0))
    
    def _actualiser_affichage(self):
        """Actualise l'affichage de l'historique"""
        # Vider le treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obtenir et afficher l'historique
        historique = historique_manager.obtenir_historique_complet()
        
        for calcul in reversed(historique):  # Plus récents en premier
            entree_str = ", ".join([f"{k}: {v}" for k, v in calcul["entree"].items()])
            
            self.tree.insert("", 0, values=(
                calcul["id"],
                calcul["date_affichage"],
                calcul["module"],
                calcul["operation"],
                entree_str[:100] + "..." if len(entree_str) > 100 else entree_str,
                str(calcul["resultat"])[:100] + "..." if len(str(calcul["resultat"])) > 100 else calcul["resultat"]
            ))
        
        # Mettre à jour les statistiques
        stats = historique_manager.obtenir_statistiques()
        self.stats_label.config(
            text=f"📈 Total: {stats['total_calculs']} calculs | "
                 f"Session: {stats['session_actuelle']} | "
                 f"Premier: {stats['premier_calcul']}"
        )
    
    def _rechercher(self, event=None):
        """Recherche dans l'historique"""
        terme = self.recherche_var.get().strip()
        if not terme:
            self._actualiser_affichage()
            return
        
        resultats = historique_manager.rechercher_calculs(terme)
        
        # Vider et réafficher les résultats
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for calcul in reversed(resultats):
            entree_str = ", ".join([f"{k}: {v}" for k, v in calcul["entree"].items()])
            
            self.tree.insert("", 0, values=(
                calcul["id"],
                calcul["date_affichage"],
                calcul["module"],
                calcul["operation"],
                entree_str,
                calcul["resultat"]
            ))
    
    def _filtrer(self, event=None):
        """Filtre l'historique par module"""
        module = self.filtre_module.get()
        if module == "Tous":
            self._actualiser_affichage()
            return
        
        historique_filtre = historique_manager.filtrer_par_module(module)
        
        # Vider et réafficher
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for calcul in reversed(historique_filtre):
            entree_str = ", ".join([f"{k}: {v}" for k, v in calcul["entree"].items()])
            
            self.tree.insert("", 0, values=(
                calcul["id"],
                calcul["date_affichage"],
                calcul["module"],
                calcul["operation"],
                entree_str,
                calcul["resultat"]
            ))
    
    def _exporter_json(self):
        """Exporte l'historique en JSON"""
        fichier = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")],
            title="Exporter l'historique en JSON"
        )
        
        if fichier:
            resultat = historique_manager.exporter_json(fichier)
            messagebox.showinfo("Export JSON", resultat)
    
    def _exporter_csv(self):
        """Exporte l'historique en CSV"""
        fichier = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Fichiers CSV", "*.csv"), ("Tous les fichiers", "*.*")],
            title="Exporter l'historique en CSV"
        )
        
        if fichier:
            resultat = historique_manager.exporter_csv(fichier)
            messagebox.showinfo("Export CSV", resultat)
    
    def _importer_json(self):
        """Importe un historique depuis JSON"""
        fichier = filedialog.askopenfilename(
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")],
            title="Importer un historique JSON"
        )
        
        if fichier:
            if messagebox.askyesno("Importer", "Voulez-vous importer cet historique ?"):
                resultat = historique_manager.importer_json(fichier)
                messagebox.showinfo("Import", resultat)
                self._actualiser_affichage()
    
    def _supprimer_selection(self):
        """Supprime le calcul sélectionné"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Supprimer", "Veuillez sélectionner un calcul à supprimer.")
            return
        
        if messagebox.askyesno("Supprimer", "Voulez-vous vraiment supprimer ce calcul ?"):
            for item in selection:
                values = self.tree.item(item)["values"]
                if values:
                    calcul_id = values[0]
                    historique_manager.supprimer_calcul(calcul_id)
            
            self._actualiser_affichage()
    
    def _vider_historique(self):
        """Vide complètement l'historique"""
        if messagebox.askyesno("Vider historique", 
                              "Voulez-vous vraiment vider tout l'historique ?\nCette action est irréversible."):
            resultat = historique_manager.vider_historique()
            messagebox.showinfo("Historique vidé", resultat)
            self._actualiser_affichage()

# Instance globale
interface_historique = InterfaceHistorique()