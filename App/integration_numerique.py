from tkinter import *
from tkinter import ttk
import re
import math
from math import factorial
from . import modules as modu


def prepare_expression(expr: str) -> str:
    """Prépare l'expression mathématique pour évaluation"""
    expr = expr.replace(" ", "")
    
    # Valeur absolue
    while "|" in expr:
        debut = expr.find("|")
        fin = expr.find("|", debut + 1)
        if fin == -1:
            expr = expr.replace("|", "", 1)
        else:
            contenu = expr[debut + 1:fin]
            expr = expr[:debut] + f"abs({contenu})" + expr[fin + 1:]
    
    # Multiplication implicite
    expr = re.sub(r"(\d)(π)", r"\1*π", expr)
    expr = re.sub(r"(\d)(√)", r"\1*√", expr)
    expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)
    
    # Remplacements
    expr = expr.replace("π", "pi")
    expr = expr.replace("√", "sqrt")
    expr = expr.replace("^", "**")
    expr = expr.replace("%", "/100")
    expr = re.sub(r"(\d+)!", r"factorial(\1)", expr)
    
    return expr

def equilibrer_parentheses(expr: str) -> str:
    """Équilibre les parenthèses"""
    ouvert = expr.count("(")
    ferme = expr.count(")")
    manque = ouvert - ferme
    if manque > 0:
        expr += ")" * manque
    return expr

# ================================================================================================
# INTERFACE GRAPHIQUE
# ================================================================================================

# Liste des méthodes d'intégration disponibles
donnees = ["Rectangle Retrograde", "Rectangle progressif", "Rectangle Centré",
           "Trapèzes Composite", "Trapèzes Simples", "Simpson Simple", "Simpson Composite"]

def lancer_integration_numerique(parent=None):
    """
    Ouvre une nouvelle fenêtre pour effectuer une intégration numérique.
    """
    
    # Variables associées aux champs d'entrée
    var_a = StringVar()
    var_b = StringVar()
    var_n = StringVar()
    var_f = StringVar()
    
    # Initialisation de la fenêtre secondaire
    fenetre_integration = Toplevel(parent) if parent else Tk()
    fenetre_integration.configure(bg="#F0F4F8")
    fenetre_integration.geometry("700x900")
    fenetre_integration.title("Intégration Numérique")
    
    # Configuration du style
    def configurer_style():
        style = ttk.Style()
        style.configure("Custom.TButton",
                        foreground="#FFFFFF",
                        background="#3B82F6",
                        font=("Century Gothic", 12),
                        padding=8,
                        relief="flat")
        
        style.configure("Quit.TButton",
                        foreground="#FFFFFF",
                        background="#DC2626",
                        font=("Century Gothic", 12),
                        padding=8,
                        relief="flat")
        
        return style
    
    style = configurer_style()
    
    # Titres fixes en haut
    header_frame = Frame(fenetre_integration, bg="#F0F4F8")
    header_frame.pack(fill="x", pady=10)
    
    Label(header_frame, text="Intégration Numérique 📈",
          font=("Century Gothic", 24, "bold"), fg="#1E40AF", bg="#F0F4F8").pack()
    Label(header_frame, text="Choisissez une méthode d'intégration 😊",
          font=("Century Gothic", 14), fg="#1E40AF", bg="#F0F4F8").pack()
    
    # Menu déroulant pour choisir la méthode d'intégration
    combo = ttk.Combobox(header_frame, font=("Century Gothic", 14),
                         values=donnees, state="readonly", width=30)
    combo.pack(pady=10)
    combo.set("=== Sélectionnez une méthode ===")
    
    # Cadre principal avec scrollbar
    main_frame = Frame(fenetre_integration, bg="#F0F4F8")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    canvas = Canvas(main_frame, bg="#F0F4F8", highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#F0F4F8")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    def _on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    
    frame_contenu = scrollable_frame
    
    # Section fonction
    Label(frame_contenu, text="Fonction à intégrer (ex: x**2, sin(x), cos(x)*x)",
          font=("Century Gothic", 14), bg="#F0F4F8", fg="#1E40AF").pack(pady=5)
    
    entree_f = Entry(frame_contenu, font=("Century Gothic", 14), textvariable=var_f, width=40)
    entree_f.pack(padx=20, pady=5)
    
    # Section paramètres
    frame_params = Frame(frame_contenu, bg="#F0F4F8")
    frame_params.pack(pady=10)
    
    # Paramètre a
    frame_a = Frame(frame_params, bg="#F0F4F8")
    frame_a.pack(pady=5)
    Label(frame_a, text="Borne inférieure (a) :", font=("Century Gothic", 12), bg="#F0F4F8", fg="#1E40AF").pack(side="left")
    entree_a = Entry(frame_a, font=("Century Gothic", 12), textvariable=var_a, width=15)
    entree_a.pack(side="left", padx=10)
    
    # Paramètre b
    frame_b = Frame(frame_params, bg="#F0F4F8")
    frame_b.pack(pady=5)
    Label(frame_b, text="Borne supérieure (b) :", font=("Century Gothic", 12), bg="#F0F4F8", fg="#1E40AF").pack(side="left")
    entree_b = Entry(frame_b, font=("Century Gothic", 12), textvariable=var_b, width=15)
    entree_b.pack(side="left", padx=10)
    
    # Paramètre n
    frame_n = Frame(frame_params, bg="#F0F4F8")
    frame_n.pack(pady=5)
    Label(frame_n, text="Subdivisions (n) :", font=("Century Gothic", 12), bg="#F0F4F8", fg="#1E40AF").pack(side="left")
    entree_n = Entry(frame_n, font=("Century Gothic", 12), textvariable=var_n, width=15)
    entree_n.pack(side="left", padx=10)
    
    # Boutons d'aide mathématique
    Label(frame_contenu, text="Raccourcis pour fonctions mathématiques",
          font=("Century Gothic", 12, "bold"), bg="#F0F4F8", fg="#1E40AF").pack(pady=(20, 5))
    
    frame_boutons = Frame(frame_contenu, bg="#F0F4F8")
    frame_boutons.pack(pady=10)
    
    # Ligne 1
    ligne1 = Frame(frame_boutons, bg="#F0F4F8")
    ligne1.pack(pady=2)
    
    boutons_ligne1 = [
        ("x**2", "x**2"),
        ("x**n", "x**"),
        ("sqrt(x)", "sqrt(x)"),
        ("(", "("),
        (")", ")")
    ]
    
    for text, insert_text in boutons_ligne1:
        btn = ttk.Button(ligne1, text=text, style="Custom.TButton",
                        command=lambda t=insert_text: inserer_texte(t, entree_f))
        btn.pack(side="left", padx=2)
    
    # Ligne 2
    ligne2 = Frame(frame_boutons, bg="#F0F4F8")
    ligne2.pack(pady=2)
    
    boutons_ligne2 = [
        ("sin(x)", "sin(x)"),
        ("cos(x)", "cos(x)"),
        ("tan(x)", "tan(x)"),
        ("π", "pi"),
        ("e", "e")
    ]
    
    for text, insert_text in boutons_ligne2:
        btn = ttk.Button(ligne2, text=text, style="Custom.TButton",
                        command=lambda t=insert_text: inserer_texte(t, entree_f))
        btn.pack(side="left", padx=2)
    
    # Ligne 3
    ligne3 = Frame(frame_boutons, bg="#F0F4F8")
    ligne3.pack(pady=2)
    
    boutons_ligne3 = [
        ("log(x)", "log(x)"),
        ("exp(x)", "exp(x)"),
        ("|x|", "|x|"),
        ("Effacer", "clear"),
        ("←", "backspace")
    ]
    
    for text, action in boutons_ligne3:
        if action == "clear":
            btn = ttk.Button(ligne3, text=text, style="Custom.TButton",
                            command=lambda: var_f.set(""))
        elif action == "backspace":
            btn = ttk.Button(ligne3, text=text, style="Custom.TButton",
                            command=lambda: supprimer_caractere(entree_f))
        else:
            btn = ttk.Button(ligne3, text=text, style="Custom.TButton",
                            command=lambda t=action: inserer_texte(t, entree_f))
        btn.pack(side="left", padx=2)
    
    # Zone de résultat
    frame_resultat = Frame(frame_contenu, bg="#F0F4F8")
    frame_resultat.pack(pady=20)
    
    resultat_label = Label(frame_resultat, text="Résultat apparaîtra ici",
                          font=("Century Gothic", 14, "bold"), fg="#1E40AF", bg="#F0F4F8")
    resultat_label.pack()
    
    # Fonctions utilitaires
    def inserer_texte(texte, widget):
        """Insère du texte à la position actuelle du curseur"""
        position = widget.index(INSERT)
        widget.insert(position, texte)
        widget.focus_set()
    
    def supprimer_caractere(widget):
        """Supprime le caractère précédent le curseur"""
        position = widget.index(INSERT)
        if position > 0:
            widget.delete(position - 1, position)
        widget.focus_set()
    
    def valider_et_convertir_donnees(a, b, n, fonction_text):
        """Valide et convertit toutes les données d'entrée"""
        # Validation des champs vides - CORRECTION ICI
        if not a or str(a).strip() == "":
            raise ValueError("La borne inférieure (a) est requise")
        if not b or str(b).strip() == "":
            raise ValueError("La borne supérieure (b) est requise")
        if not n or str(n).strip() == "":
            raise ValueError("Le nombre de subdivisions (n) est requis")
        if not fonction_text or str(fonction_text).strip() == "":
            raise ValueError("La fonction est requise")
        
        # Conversion des nombres
        try:
            a_val = float(str(a).strip())
            b_val = float(str(b).strip())
            n_val = int(str(n).strip())
        except ValueError:
            raise ValueError("Les valeurs a, b doivent être des nombres et n un entier positif")
        
        # Validation des valeurs
        if n_val <= 0:
            raise ValueError("n doit être un entier positif")
        if a_val >= b_val:
            raise ValueError("La borne a doit être inférieure à b")
        
        return a_val, b_val, n_val
    
    def preparer_fonction(fonction_text):
        """Prépare et nettoie la fonction mathématique"""
        try:
            intermediaire = prepare_expression(str(fonction_text))
            arrange_parenthese = equilibrer_parentheses(intermediaire)
            
            def ma_fonction(x):
                try:
                    env = {
                        "sin": math.sin, "cos": math.cos, "tan": math.tan,
                        "sqrt": math.sqrt, "log": math.log, "exp": math.exp,
                        "pi": math.pi, "e": math.e, "abs": abs,
                        "factorial": factorial
                    }
                    namespace = {"x": x}
                    namespace.update(env)
                    return eval(arrange_parenthese, {"__builtins__": {}}, namespace)
                except Exception as e:
                    raise ValueError(f"Erreur lors de l'évaluation: {str(e)}")
            
            return ma_fonction
        except Exception as e:
            raise ValueError(f"Erreur dans la fonction : {str(e)}")
    
    def executer_methode(choix, a, b, n, fonction):
        """Exécute la méthode d'intégration sélectionnée"""
        methodes = {
            "Rectangle Retrograde": modu.intRectangleRetro,
            "Rectangle progressif": modu.intRectanglePro,
            "Rectangle Centré": modu.intRectangleCentre,
            "Trapèzes Composite": modu.intTrapezeC,
            "Trapèzes Simples": modu.intTrapezeS,
            "Simpson Simple": modu.intSimpsonS,
            "Simpson Composite": modu.intSimpsonC,
        }
        
        if choix not in methodes:
            raise ValueError(f"Méthode inconnue : {choix}")
        
        # CORRECTION : Appel avec l'ordre correct des paramètres
        return methodes[choix](fonction, a, b, n)
    
    def calculer():
        """Fonction principale de calcul"""
        try:
            choix = combo.get()
            
            if choix == "=== Sélectionnez une méthode ===":
                resultat_label.config(text="❌ Veuillez sélectionner une méthode", fg="#DC2626")
                return
            
            # CORRECTION : Récupération directe des valeurs
            nombre_a = entree_a.get()
            nombre_b = entree_b.get()
            nombre_n = entree_n.get()
            fonction_text = entree_f.get()
            
            # Debug: afficher les valeurs récupérées
            print(f"Debug - a: '{nombre_a}', b: '{nombre_b}', n: '{nombre_n}', f: '{fonction_text}'")
            
            # Validation et conversion
            a, b, n = valider_et_convertir_donnees(nombre_a, nombre_b, nombre_n, fonction_text)
            
            # Préparation de la fonction
            fonction_propre = preparer_fonction(fonction_text)
            
            # Test de la fonction
            try:
                # Test sur plusieurs points pour vérifier la continuité
                fonction_propre(a)
                fonction_propre(b)
                fonction_propre((a + b) / 2)
            except Exception as e:
                resultat_label.config(text=f"❌ Erreur dans la fonction : {str(e)}", fg="#DC2626")
                return
            
            # Calcul
            resultat = executer_methode(choix, a, b, n, fonction_propre)
            resultat_label.config(text=f"✅ Résultat : {resultat:.8f}", fg="#1E40AF")
            
        except ValueError as e:
            resultat_label.config(text=f"❌ {str(e)}", fg="#DC2626")
        except Exception as e:
            resultat_label.config(text=f"❌ Erreur de calcul : {str(e)}", fg="#DC2626")
    
    # Boutons finaux
    frame_boutons_finaux = Frame(frame_contenu, bg="#F0F4F8")
    frame_boutons_finaux.pack(pady=20)
    
    bouton_calculer = ttk.Button(frame_boutons_finaux, text="🧮 Calculer",
                                style="Custom.TButton", command=calculer)
    bouton_calculer.pack(side="left", padx=10)
    
    bouton_exit = ttk.Button(frame_boutons_finaux, text="❌ Fermer",
                           style="Quit.TButton", command=fenetre_integration.destroy)
    bouton_exit.pack(side="left", padx=10)
    
    # Exemples
    frame_exemples = Frame(frame_contenu, bg="#F0F4F8")
    frame_exemples.pack(pady=10)
    
    Label(frame_exemples, text="💡 Exemples de fonctions :",
          font=("Century Gothic", 12, "bold"), bg="#F0F4F8", fg="#1E40AF").pack()
    Label(frame_exemples, text="x**2 + 3*x + 1    |    sin(x)    |    cos(x)*exp(x)    |    sqrt(x)",
          font=("Century Gothic", 10), fg="#1E40AF", bg="#F0F4F8").pack()
    
    # Informations supplémentaires
    frame_info = Frame(frame_contenu, bg="#F0F4F8")
    frame_info.pack(pady=20)
    
    Label(frame_info, text="ℹ️ Informations sur les méthodes :",
          font=("Century Gothic", 12, "bold"), bg="#F0F4F8", fg="#1E40AF").pack()
    
    methodes_info = [
        "• Rectangle Rétrograde : Utilise le côté gauche de chaque intervalle",
        "• Rectangle Progressif : Utilise le côté droit de chaque intervalle", 
        "• Rectangle Centré : Utilise le point milieu de chaque intervalle",
        "• Trapèzes Simple : Approximation linéaire entre deux points",
        "• Trapèzes Composite : Division en plusieurs trapèzes",
        "• Simpson Simple : Approximation parabolique sur 3 points",
        "• Simpson Composite : Multiple approximations paraboliques"
    ]
    
    for info in methodes_info:
        Label(frame_info, text=info, font=("Century Gothic", 10), 
              bg="#F0F4F8", fg="#1E40AF", anchor="w").pack(fill="x", padx=20, pady=2)
    
    # Conseils d'utilisation
    frame_conseils = Frame(frame_contenu, bg="#F0F4F8")
    frame_conseils.pack(pady=20)
    
    Label(frame_conseils, text="💡 Conseils d'utilisation :",
          font=("Century Gothic", 12, "bold"), bg="#F0F4F8", fg="#1E40AF").pack()
    
    conseils = [
        "• Augmentez n pour plus de précision",
        "• Simpson nécessite un nombre pair de subdivisions",
        "• Testez avec des fonctions simples d'abord",
        "• Vérifiez que votre fonction est continue sur [a,b]",
        "• Utilisez des parenthèses pour les expressions complexes"
    ]
    
    for conseil in conseils:
        Label(frame_conseils, text=conseil, font=("Century Gothic", 10),
              bg="#F0F4F8", fg="#1E40AF", anchor="w").pack(fill="x", padx=20, pady=2)
    
    # Espaceur final pour le défilement
    Label(frame_contenu, text="", bg="#F0F4F8", height=3).pack()

    return fenetre_integration

# Pour tester directement ce fichier
if __name__ == "__main__":
    fenetre = lancer_integration_numerique()
    fenetre.mainloop()