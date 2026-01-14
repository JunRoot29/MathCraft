# 🧮 MathCraft

> *Un espace malin pour calculer, apprendre et s'amuser avec les maths. 🧠✨*

---

## 📝 Description

**MathCraft** est une application éducative interactive développée en Python (Tkinter) qui offre une plateforme moderne et intuitive pour explorer et pratiquer des concepts mathématiques à travers **9 modules complets**, allant des opérations de base à l'interpolation numérique avancée.

L'objectif est simple : rendre les mathématiques **accessibles, visuelles et amusantes** grâce à des interfaces interactives avec visualisation graphique.

---

## ✨ Fonctionnalités principales

### 📊 1. Opérations de Base
* Calculatrice scientifique complète
* Trigonométrie, logarithmes, puissances, racines
* Constantes (π, e)
* Conversion degrés ↔ radians
* Historique des calculs (supporte désormais des résultats structurés pour les méthodes renvoyant des détails, ex. intégration)

### 🔢 2. Théorie des Nombres
* Test de primalité
* Nombres parfaits
* PGCD / PPCM
* Nombres de Fibonacci et Catalan
* Vérification de chiffres distincts

### 🔄 3. Conversion d'Unités
* Longueur, température, masse
* Vitesse, angles, pression
* Interface avec prévisualisation

### 📐 4. Polynômes & Équations
* Équations du 1er degré
* Équations du 2ème degré (réelles & complexes)
* Affichage graphique des racines

### 📝 5. Chaînes de Caractères
* Analyse textuelle complète
* Compter voyelles, consonnes, mots
* Test de palindrome
* Statistiques détaillées

### ∫ 6. Intégration Numérique **🆕**
* **7 méthodes** : Rectangles (gauche/droit/centre), Trapèzes, Simpson
* **Affichage des itérations** en temps réel
* **Export CSV** des résultats
* **Précision ajustable**
* Interface avec onglets détaillés

> **Note technique :** Les fonctions d'intégration retournent désormais un tuple `(resultat, iterations)` —
> `resultat` est un float et `iterations` est une liste de dictionnaires décrivant chaque étape (utile pour l'interface et l'export).

### 🔬 7. Équations Numériques **🆕**
* **9 méthodes avancées** : Dichotomie, Newton-Raphson, Point Fixe, Sécante, Regula Falsi, Müller, Steffensen, Brent, Ridders
* **Suivi détaillé** de chaque itération
* **Comparaison des performances**
* **Convergence garantie** avec algorithmes robustes
* Guide complet des méthodes

### 📈 8. Interpolation Numérique **🆕**
* **4 méthodes** : Lagrange, Newton, Linéaire par morceaux, Spline Cubique
* **Visualisation graphique** des courbes interpolées
* **Calculs détaillés** étape par étape
* **Export des résultats** en CSV et images
* **Zoom interactif** sur les graphiques

### 🎮 9. Jeux & Concepts
* Défis mathématiques interactifs
* Explorateur de concepts visuels
* Mini-jeux logiques
* Battle mathématique

---

## 🛠️ Technologies utilisées

* **Python 3.x** - Langage principal
* **Tkinter / ttk** - Interface graphique
* **NumPy** - Calculs scientifiques
* **Matplotlib** - Visualisation graphique
* **JSON** - Stockage des données
* Modules standards : `math`, `re`, `csv`, `json`

---

## 📋 Prérequis

```bash
pip install numpy matplotlib
python -m tkinter   # Vérifier l'installation de Tkinter
pip install pyperclip 
```

---

## ⚡ Démarrage rapide

```bash
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft
pip install -r requirements.txt
python main.py
```

---

## 📂 Structure du projet

```
MathCraft/
├── main.py                          # Point d'entrée principal
├── README.md                        # Documentation
├── requirements.txt                 # Dépendances
├── App/
│   ├── __init__.py
│   ├── modules.py                   # Bibliothèque mathématique principale
│   ├── operation_de_base.py         # Calculatrice scientifique(interface)
│   ├── theorie_des_nombres.py       # Théorie des nombres(interface)
│   ├── conversion.py                # Conversion d'unités(interface)
│   ├── polynome.py                  # Équations polynomiales(interface)
│   ├── chaine_de_caractere.py       # Analyse textuelle(interface)
│   ├── integration_numerique.py     # Intégration numérique (interface)
│   ├── equation_numerique.py        # Résolution d'équations (interface) 🆕
│   ├── interpolation_numerique.py   # Interpolation numérique (interface) 🆕
│   ├── jeux_math.py                 # Jeux mathématiques
│   ├── soutieng_manager.py          # Gestionnaire de support
│   ├── interface_historique.py      # Historique des calculs(interface)
│   └── explorateur_concepts.py      # Explorateur de concepts(interface)
├── data/
│   ├── historique_calculs.json      # Historique des calculs
│   ├── defis_fibonacci.json         # Défis Fibonacci
│   ├── math_battle.json             # Questions battle mathématique
│   ├── question_enigme.json         # Énigmes
│   └── questions.json               # Questions générales
└── Image/
    ├── icon.png                     # Icône principale
    ├── Calc.png                     # Calculatrice
    ├── integral.png                 # Intégration
    ├── poly.png                     # Polynômes
    └── ... (autres images)
```

---

## 🎨 Design de l'interface

### Palette de couleurs unifiée :
```python
PALETTE = {
    "fond_principal": "#F0F4F8",
    "fond_secondaire": "#FFFFFF", 
    "primaire": "#1E40AF",
    "secondaire": "#3B82F6",
    "texte_fonce": "#1E293B",
    "texte_clair": "#64748B",
    "succes": "#10B981",
    "erreur": "#DC2626",
    "bordure": "#E2E8F0"
}
```

### Caractéristiques :
* **Police** : Century Gothic
* **Navigation par onglets** pour modules complexes
* **Feedback visuel** en temps réel
* **Messages d'erreur/succès** contextualisés
* **Scrollbars** pour contenu long
* **Export des données** (CSV, images)

---

## 🔬 Bibliothèque mathématique : `modules.py`

### Méthodes d'intégration numérique :
* `intRectangleRetro()` - Rectangles rétrogrades
* `intRectanglePro()` - Rectangles progressifs  
* `intRectangleCentre()` - Rectangles centrés
* `intTrapezeC()` - Trapèzes composites
* `intTrapezeS()` - Trapèzes simples
* `intSimpsonC()` - Simpson composite
* `intSimpsonS()` - Simpson simple

### Résolution d'équations (9 méthodes) :
* `racineDichotomie()` - Méthode robuste
* `racineNewton()` - Convergence rapide
* `racinePointFixe()` - Pour g(x)=x
* `racineSecante()` - Sans dérivée
* `racineRegulaFalsi()` - Combinaison optimale
* `racineMuller()` - Interpolation quadratique
* `racineSteffensen()` - Accélération
* `racineBrent()` - Algorithme industriel
* `racineRidders()` - Extrapolation exponentielle

### Interpolation numérique :
* `interpolation_lagrange()` - Polynôme exact
* `interpolation_newton()` - Différences divisées
* `interpolation_lineaire()` - Segments droits
* `spline_cubique_naturelle()` - Courbes lisses

### Fonctions utilitaires :
* `prepare_expression()` - Préparation des expressions
* `equilibrer_parentheses()` - Gestion des parenthèses
* Fonctions arithmétiques avancées

---

## 💡 Exemples d'utilisation

### ➤ Intégration numérique
1. Ouvrir **Intégration Numérique**
2. Choisir une méthode (ex: Simpson Composite)
3. Entrer : `f(x) = sin(x)`, `a=0`, `b=π`, `n=100`
4. Obtenir résultat avec **affichage des 100 itérations**
5. **Exporter** les données en CSV

### ➤ Résolution d'équation
1. Ouvrir **Équations Numériques**
2. Choisir **Méthode de Brent** (robuste)
3. Entrer : `f(x) = x³ - 2x - 5`, `a=2`, `b=3`, `ε=1e-6`
4. Visualiser **chaque itération** avec précision
5. Comparer avec d'autres méthodes

### ➤ Interpolation avec graphique
1. Ouvrir **Interpolation Numérique**
2. Choisir **Spline Cubique**
3. Entrer points : `0,0; 1,1; 2,4; 3,9`
4. Évaluer en `x=1.5`
5. **Visualiser la courbe** dans l'onglet Graphique
6. **Zoomer** et **sauvegarder** l'image

### ➤ Export des résultats
```python
# Toutes les interfaces proposent :
- Export CSV des itérations
- Export PNG des graphiques
- Copie des résultats
- Historique des calculs
```

---

## 🚀 Fonctionnalités avancées

### 📊 Visualisation graphique
* **Graphiques interactifs** avec Matplotlib
* **Zoom et pan** dynamiques
* **Légendes détaillées**
* **Points mis en évidence**
* **Sauvegarde haute résolution**

### 📈 Analyse des résultats
* **Tableaux détaillés** étape par étape
* **Erreurs de convergence**
* **Comparaison des méthodes**
* **Statistiques d'exécution**
* **Précision configurable**

### 🎯 Interface utilisateur
* **Onglets multiples** pour navigation
* **Raccourcis mathématiques**
* **Exemples préconfigurés**
* **Validation en temps réel**
* **Messages d'aide contextuels**

---

## 🗺️ Feuille de route

### ✅ Réalisé
- [x] Modules 1-6 : Opérations de base à intégration
- [x] Module 7 : Équations numériques (9 méthodes)
- [x] Module 8 : Interpolation numérique avec graphiques
- [x] Interface unifiée avec palette cohérente
- [x] Export CSV et images
- [x] Visualisation graphique interactive
- [x] Ajout de barres de défilement verticales aux interfaces des jeux (en-têtes fixes, support de la molette de la souris)

### 🔄 En développement
- [ ] Module 9 : Jeux mathématiques avancés
- [ ] Export PDF des rapports
- [ ] Mode sombre/clair
- [ ] Internationalisation (anglais/français)
- [ ] Base de données des calculs

### 📋 Planifié
- [ ] Calcul différentiel numérique
- [ ] Transformées de Fourier
- [ ] Algèbre linéaire avancée
- [ ] Statistiques et probabilités
- [ ] Version web (Streamlit/Dash)
- [ ] Applications mobiles

---

## 🤝 Contribution

```bash
# 1. Fork le projet
# 2. Créer une branche
git checkout -b feature/NouvelleFonction

# 3. Commiter les changements
git commit -m "Ajout: Description claire"

# 4. Pousser vers GitHub
git push origin feature/NouvelleFonction

# 5. Ouvrir une Pull Request
```

### Guidelines de contribution :
* **Commentaires en français** avec docstrings
* **Tests unitaires** pour nouvelles fonctions
* **Respect du style** de code existant
* **Validation** sur différents cas d'usage
* **Documentation** mise à jour

---

## 🧪 Tests

```bash
# Tester les fonctions mathématiques
python -m pytest tests/test_modules.py

# Tester l'interface
python -m pytest tests/test_interface.py

# Lancer tous les tests
python -m pytest tests/
```

---

## ❓ FAQ

### ❔ L'application ne démarre pas ?
```bash
# Vérifier Tkinter
python -m tkinter

# Vérifier les dépendances
pip install -r requirements.txt

# Vérifier Python 3.8+
python --version
```

### ❔ Comment ajouter une nouvelle méthode ?
1. Ajouter la fonction dans `modules.py`
2. Implémenter le suivi des itérations
3. Ajouter à l'interface correspondante
4. Tester avec différents cas
5. Documenter dans le README

### ❔ Puis-je utiliser l'API mathématique seule ?
```python
from App.modules import intSimpsonC, racineNewton

# Utiliser directement
resultat, iterations = intSimpsonC(f, a, b, n)
racine, nb_iter, details = racineNewton(f, df, x0, epsilon)
```

### ❔ OS supportés ?
* **Windows 10/11** ✅
* **Linux** (Ubuntu, Debian) ✅  
* **macOS** 10.15+ ✅
* **Raspberry Pi** (avec interface légère) ⚠️

---

## 🐛 Signaler un bug

1. **Vérifier** les dépendances et version Python
2. **Reproduire** le bug avec étapes claires
3. **Capture d'écran** si applicable
4. **Ouvrir une issue** sur GitHub avec :
   * Description du problème
   * Étapes pour reproduire
   * Version de MathCraft
   * Logs d'erreur

---

## 📊 Performances

### Benchmark d'intégration (sin(x) de 0 à π) :
```
Méthode          n=100     n=1000    Précision
Rectangles       0.002s    0.015s    Moyenne
Trapèzes         0.003s    0.020s    Bonne  
Simpson          0.004s    0.025s    Excellente
```

### Convergence des équations (x³-2x-5=0) :
```
Méthode          Itérations   Erreur finale
Dichotomie       20           1e-6
Newton           5            1e-12
Brent            8            1e-15
```

---

## 📝 Crédits

* **Auteur principal** : Junior Kossivi Agbenonzan
* **Institution** : Université Félix Houphouët-Boigny
* **Localisation** : Abidjan, Côte d'Ivoire
* **Année** : 2025

### Remerciements :
* Équipe pédagogique UFR-MI
* Communauté Python Francophone
* Contributeurs open source

---

## 📄 Licence

**Projet éducatif open source**

* ✅ **Utilisation éducative** - Libre
* ✅ **Modifications** - Avec attribution
* ✅ **Partage** - Autorisé
* ✅ **Recherche académique** - Encouragée
* ⚠️ **Usage commercial** - Sur autorisation
* ❌ **Revendication de paternité** - Interdite

**Licence** : Creative Commons BY-NC-SA 4.0

---

## 📧 Contact & Support

### Communication :
* 📨 **Email** : [junioragbenonzan31@gmail.com](mailto:junioragbenonzan31@gmail.com)
* 🐙 **GitHub** : [@JunRoot29](https://github.com/JunRoot29)* ☕ **Ko-fi** : [https://ko-fi.com/juniorkossivi](https://ko-fi.com/juniorkossivi)* 💬 **Issues** : [MathCraft Issues](https://github.com/JunRoot29/MathCraft/issues)

### Support académique :
* Pour **intégration dans un cours** : Contact par email
* Pour **projets étudiants** : Templates disponibles
* Pour **recherche** : Données d'export disponibles

### Communauté :
* **Discussions** : Section GitHub Discussions
* **Suggestions** : Issues avec label "enhancement"
* **Bugs** : Issues avec label "bug"
* **Questions** : Issues avec label "question"

---

<div align="center">

## 🏆 Citation

Si vous utilisez MathCraft dans un contexte académique :

```
@software{mathcraft2025,
  author = {Kossivi, Junior},
  title = {MathCraft: Plateforme Interactive de Mathématiques Numériques},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/JunRoot29/MathCraft}
}
```

## ⭐ Soutien

Si vous aimez MathCraft, n'hésitez pas à :
- **Mettre une étoile** ⭐ sur GitHub
- **Partager** avec vos collègues
- **Contribuer** au développement
- **Suggérer** des améliorations
- **Soutenir via Ko-fi** ☕ : [https://ko-fi.com/juniorkossivi](https://ko-fi.com/juniorkossivi)

---

Fait avec ❤️ et beaucoup de ☕ à Abidjan

**"Les mathématiques sont la porte et la clé de toutes les sciences."**
*– Roger Bacon*

© 2026 **Jacques Junior Kossivi** • Université Félix Houphouët-Boigny

</div>

---

*Dernière mise à jour : Janvier 2025*  
*Version : MathCraft 1.0.0 - "Numerical Revolution"*
