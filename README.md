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
* Historique des calculs (supporte des résultats structurés pour les méthodes complexes)

### 🔢 2. Théorie des Nombres
* Test de primalité avec vérification optimisée
* Nombres parfaits
* PGCD / PPCM (algorithme euclidien)
* Nombres de Fibonacci et Catalan
* Vérification de chiffres distincts

### 🔄 3. Conversion d'Unités
* Longueur, température, masse
* Vitesse, angles, pression
* Interface avec prévisualisation en temps réel

### 📐 4. Polynômes & Équations
* Équations du 1er degré
* Équations du 2ème degré (réelles & complexes)
* Affichage graphique des racines
* Factorisation et analyse des polynômes

### 📝 5. Chaînes de Caractères
* Analyse textuelle complète
* Compter voyelles, consonnes, mots
* Test de palindrome
* Statistiques détaillées et fréquences

### ∫ 6. Intégration Numérique
* **7 méthodes** : Rectangles (gauche/droit/centre), Trapèzes, Simpson
* **Affichage des itérations** en temps réel
* **Export CSV** des résultats détaillés
* **Précision ajustable**
* Interface avec onglets pour chaque méthode
* Comparaison visuelle des méthodes

### 🔬 7. Équations Numériques
* **9 méthodes avancées** : Dichotomie, Newton-Raphson, Point Fixe, Sécante, Regula Falsi, Müller, Steffensen, Brent, Ridders
* **Suivi détaillé** de chaque itération avec convergence
* **Comparaison des performances** entre les méthodes
* **Convergence garantie** avec algorithmes robustes
* Guide complet et interactif de chaque méthode
* Export des résultats en CSV

### 📈 8. Interpolation Numérique
* **5 méthodes** : Lagrange, Newton, Linéaire par morceaux, Spline Cubique Naturelle, Hermite
* **Visualisation graphique** des courbes interpolées
* **Calculs détaillés** étape par étape avec étapes intermédiaires
* **Export des résultats** en CSV et images PNG
* **Zoom interactif** et navigation sur les graphiques
* Tableau comparatif des erreurs d'interpolation

### 🎮 9. Jeux & Concepts
* Défis mathématiques interactifs (Fibonacci, Nombres premiers)
* Explorateur de concepts visuels avec démonstrations
* Mini-jeux logiques et énigmes mathématiques
* Battle mathématique avec système de points
* Questions adaptatives avec progression

---

## 🛠️ Technologies utilisées

* **Python 3.x** - Langage principal
* **Tkinter / ttk** - Interface graphique moderne
* **NumPy** - Calculs scientifiques et algèbre linéaire
* **Matplotlib** - Visualisation graphique et graphiques interactifs
* **JSON** - Stockage persistant des données et sauvegardes
* Modules standards : `math`, `re`, `csv`, `json`, `os`

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
# 1. Cloner le projet
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft

# 2. Installer les dépendances
pip install numpy matplotlib

# 3. Vérifier Tkinter
python -m tkinter

# 4. Lancer l'application
python main.py
```

**✅ Requis :** Python 3.8+, pip  
**⏱️ Temps de démarrage :** ~2 secondes  
**💾 Taille :** ~50 MB avec dépendances

---

## 📂 Structure du projet

```
MathCraft/
├── main.py                          # Point d'entrée principal
├── test.py                          # Fichier de test
├── README.md                        # Documentation
├── LICENSE                          # Licence Creative Commons BY-NC-SA 4.0
├── App/
│   ├── __init__.py
│   ├── modules.py                   # Bibliothèque mathématique principale
│   ├── styles.py                    # Styles et thèmes unifiés
│   ├── operation_de_base.py         # Calculatrice scientifique (interface)
│   ├── theorie_des_nombres.py       # Théorie des nombres (interface)
│   ├── conversion.py                # Conversion d'unités (interface)
│   ├── polynome.py                  # Équations polynomiales (interface)
│   ├── chaine_de_caractere.py       # Analyse textuelle (interface)
│   ├── integration_numerique.py     # Intégration numérique (interface) - 7 méthodes
│   ├── equation_numerique.py        # Résolution d'équations (interface) - 9 méthodes
│   ├── interpolation_lineaire.py    # Interpolation numérique (interface) - 5 méthodes
│   ├── jeux_math.py                 # Jeux mathématiques et énigmes
│   ├── explorateur_concepts.py      # Explorateur de concepts (interface)
│   ├── historique_manager.py        # Gestionnaire d'historique persistant
│   ├── soutient_manager.py          # Gestionnaire de support et aide
│   └── interface_historique.py      # Interface de visualisation de l'historique
├── data/
│   ├── historique_calculs.json      # Historique des calculs persistant
│   ├── defis_fibonacci.json         # Défis de la série Fibonacci
│   ├── math_battle.json             # Questions pour la battle mathématique
│   ├── question_enigme.json         # Énigmes et puzzles
│   └── question_premier.json        # Questions sur les nombres premiers
├── sauvegardes/
│   └── historique_calculs.json      # Backups automatiques
├── Image/                           # Dossier pour les ressources visuelles
└── __pycache__/                     # Cache Python (généré automatiquement)
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

Cœur du projet contenant les algorithmes mathématiques optimisés avec support des itérations détaillées.

### 📊 Méthodes d'intégration numérique (7 total) :
| Méthode | Fonction | Précision | Convergence |
|---------|----------|-----------|------------|
| Rectangles à gauche | `intRectangleRetro()` | Faible | Linéaire |
| Rectangles à droite | `intRectanglePro()` | Faible | Linéaire |
| Rectangles centrés | `intRectangleCentre()` | Moyenne | Quadratique |
| Trapèzes | `intTrapezeC()` | Bonne | Quadratique |
| Simpson (1/3) | `intSimpsonC()` | Excellente | 4ème ordre |

### 🔬 Résolution d'équations (9 méthodes) :
| Méthode | Fonction | Avantages | Usages |
|---------|----------|-----------|--------|
| Dichotomie | `racineDichotomie()` | Garantie convergence | Démarrage fiable |
| Newton-Raphson | `racineNewton()` | Convergence très rapide | Équations générales |
| Point Fixe | `racinePointFixe()` | Formule simple | Réarrangements g(x)=x |
| Sécante | `racineSecante()` | Sans dérivée | Dérivée difficile |
| Regula Falsi | `racineRegulaFalsi()` | Hybride robuste | Cas généraux |
| Müller | `racineMuller()` | Interpolation quadratique | Racines complexes |
| Steffensen | `racineSteffensen()` | Accélération rapide | Convergence lente |
| Brent | `racineBrent()` | Algorithme industriel | Production |
| Ridders | `racineRidders()` | Extrapolation exponentielle | Haute précision |

### 📈 Interpolation numérique (5 méthodes) :
* `interpolation_lagrange()` - Polynôme exact, basis polynomiale directe
* `interpolation_newton()` - Différences divisées, plus stable numériquement
* `interpolation_lineaire()` - Segments droits, plus rapide
* `spline_cubique_naturelle()` - Courbes lisses C², minimale courbure
* `interpolation_hermite()` - Avec dérivées, C¹ continuité

### 🎯 Fonctions utilitaires :
* `prepare_expression()` - Évaluation sécurisée d'expressions mathématiques
* `equilibrer_parentheses()` - Validation et gestion des parentheses
* `ngcd()` - PGCD récursif
* `lcm()` - PPCM optimisé
* Fonctions arithmétiques avancées avec optimisations

---

## 💡 Exemples d'utilisation

### ➤ Intégration numérique
```bash
1. Ouvrir "Intégration Numérique"
2. Choisir une méthode (ex: Simpson)
3. Entrer : f(x) = sin(x), a=0, b=π, n=100
4. Observer les 100 itérations en tableau
5. Exporter les résultats en CSV
```

### ➤ Résolution d'équation
```bash
1. Ouvrir "Équations Numériques"
2. Choisir "Méthode de Brent"
3. Entrer : f(x) = x³ - 2x - 5, a=2, b=3, ε=1e-6
4. Voir toutes les itérations avec convergence
5. Comparer avec Newton-Raphson
```

### ➤ Interpolation avec graphique
```bash
1. Ouvrir "Interpolation Numérique"
2. Choisir "Spline Cubique"
3. Entrer points : (0,0), (1,1), (2,4), (3,9)
4. Visualiser la courbe interpolée
5. Évaluer en x=1.5 et voir le graphique zoomer
6. Sauvegarder l'image PNG
```

### ➤ Théorie des nombres
```python
# Vérifier si 17 est premier
Théorie des nombres → Test primalité → Entrer 17 → Résultat : OUI

# Trouver PGCD et PPCM
PGCD(48, 18) → Résultat : 6
PPCM(48, 18) → Résultat : 144
```

### ➤ Jeux mathématiques
```bash
- Défis Fibonacci : Complétez la suite
- Battle Math : Questions à choix multiples avec classement
- Énigmes : Puzzles logiques progressifs
- Concepts : Démonstrations interactives
```

### ➤ Export des résultats
```python
# Toutes les interfaces supportent :
- Export CSV des itérations
- Export PNG des graphiques
- Copie directe des résultats
- Historique persistant en JSON
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

### ✅ Réalisé (v1.0)
- [x] Module 1 : Opérations de base - Calculatrice scientifique
- [x] Module 2 : Théorie des nombres - PGCD, PPCM, primalité, Fibonacci, Catalan
- [x] Module 3 : Conversion d'unités - Longueur, température, masse, vitesse, angles, pression
- [x] Module 4 : Polynômes et équations - Équations du 1er et 2ème degré
- [x] Module 5 : Chaînes de caractères - Analyse textuelle complète
- [x] Module 6 : Intégration numérique - 7 méthodes avec export CSV
- [x] Module 7 : Équations numériques - 9 méthodes avancées avec comparaison
- [x] Module 8 : Interpolation numérique - 5 méthodes avec visualisation graphique
- [x] Module 9 : Jeux et concepts - Défis, Battle Math, Énigmes, Explorateur
- [x] Interface unifiée avec palette de couleurs cohérente
- [x] Historique persistant avec gestionnaire JSON
- [x] Export CSV et PNG pour tous les modules complexes
- [x] Visualisation graphique interactive avec Matplotlib
- [x] Validation en temps réel et messages contextuels
- [x] Support clavier et molette souris pour navigation
- [x] Barres de défilement pour interfaces longues

### 🔄 En développement
- [ ] Module 10 : Calcul différentiel numérique (dérivation)
- [ ] Mode sombre/clair avec thème personnalisable
- [ ] Export PDF des rapports complets
- [ ] Internationalisation (English/Français)
- [ ] Base de données SQLite pour historique avancé
- [ ] Système de thèmes extensible

### 📋 Planifié (v2.0+)
- [ ] Transformées de Fourier
- [ ] Algèbre linéaire avancée (matrices, déterminants)
- [ ] Statistiques et probabilités
- [ ] Calcul symbolique (SymPy)
- [ ] Version web (Streamlit ou Flask)
- [ ] Applications mobiles (Kivy)
- [ ] Plugins et extensions utilisateur
- [ ] Système de tutoriels vidéo

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
Méthode              n=100    n=1000   n=10000   Précision Asymptotique
Rectangles à gauche  0.2ms    2.0ms    20ms      O(1/n)
Trapèzes             0.3ms    3.0ms    30ms      O(1/n²)
Simpson              0.4ms    4.0ms    40ms      O(1/n⁴)
```

### Convergence des équations (x³ - 2x - 5 = 0 sur [2,3]) :
```
Méthode          Itérations   Erreur finale   Temps(ms)
Dichotomie       20           1.0e-6          5
Newton           5            1.0e-14         2
Brent            8            1.0e-15         3
Point Fixe       45           1.0e-6          12
```

### Interpolation (4 points, 1000 évaluations) :
```
Méthode              Construction   Évaluation   Erreur max
Lagrange             1ms            0.2ms/1000   1.0e-10
Newton               0.8ms          0.2ms/1000   1.0e-11
Spline Cubique       2ms            0.3ms/1000   1.0e-14
```

### Utilisation mémoire :
* Interface seule : ~20 MB
* + Historique complet (10k calculs) : ~50 MB
* + Graphiques (20 courbes) : ~80 MB

---

## 📝 Crédits

* **Auteur principal** : Junior Kossivi Agbenonzan
* **Institution** : Université Félix Houphouët-Boigny (UFR-MI)
* **Localisation** : Abidjan, Côte d'Ivoire
* **Année de création** : 2025
* **Dernière mise à jour** : Janvier 2026

### Remerciements :
* Équipe pédagogique UFR-MI pour le support académique
* Communauté Python Francophone
* Contributeurs open source
* Utilisateurs pour les retours et suggestions

---

## 📄 Licence

**Projet éducatif open source**

```
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (BY-NC-SA)
```

✅ **Autorisé :**
* Utilisation éducative gratuite
* Modifications avec attribution
* Partage et distribution
* Recherche académique
* Enseignement en milieu scolaire/universitaire

⚠️ **Sous conditions :**
* Attribution obligatoire
* Licence identique pour les dérivés
* Non-commercial (sauf autorisation)

❌ **Interdit :**
* Revendication de paternité
* Utilisation commerciale directe
* Suppression des crédits

---

## 📧 Contact & Support

### Communication directe :
* 📨 **Email** : [junioragbenonzan31@gmail.com](mailto:junioragbenonzan31@gmail.com)
* 🐙 **GitHub** : [@JunRoot29](https://github.com/JunRoot29)
* ☕ **Ko-fi** : [https://ko-fi.com/juniorkossivi](https://ko-fi.com/juniorkossivi)

### Support du projet :
* 💬 **Issues et Bugs** : [MathCraft Issues](https://github.com/JunRoot29/MathCraft/issues)
* 📋 **Discussions** : GitHub Discussions
* 💡 **Suggestions** : Issues avec label "enhancement"

### Intégration académique :
* **Formations** : Contact pour intégration dans un cours
* **Projets étudiants** : Templates et ressources disponibles
* **Recherche** : Données et API disponibles
* **Conférences** : Disponible pour présenter le projet

### Communauté :
* Labels pour faciliter les contributions
* Accueil des pull requests
* Support actif pour les utilisateurs
* Roadmap participative

---

## 🏆 Citation académique

Si vous utilisez **MathCraft** dans un contexte académique, merci de citer :

```bibtex
@software{mathcraft2025,
  author = {Kossivi, Junior Agbenonzan},
  title = {MathCraft: Plateforme Interactive de Calcul Numérique en Python},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/JunRoot29/MathCraft},
  note = {Application éducative pour l'apprentissage des mathématiques numériques}
}
```

---

## ⭐ Contribuer et soutenir

### Comment contribuer :
```bash
# 1. Fork le projet
# 2. Créer une branche feature
git checkout -b feature/NouvelleFonction

# 3. Commiter avec messages clairs
git commit -m "Feat: Description concise des changements"

# 4. Pousser et ouvrir une Pull Request
git push origin feature/NouvelleFonction
```

### Soutenir le projet :
* **⭐ Mettre une étoile** sur GitHub
* **🔄 Partager** avec vos collègues et étudiants
* **💬 Laisser des retours** dans les issues
* **📝 Contribuer** avec code ou documentation
* **☕ Soutenir via Ko-fi** : [https://ko-fi.com/juniorkossivi](https://ko-fi.com/juniorkossivi)

---

<div align="center">

## 🎯 Vision du projet

MathCraft ambitionne de démocratiser l'accès aux outils de calcul numérique de haute qualité, 
en rendant les mathématiques avancées accessibles, visuelles et amusantes à tous les niveaux.

**"Les mathématiques sont la clé et la porte de toutes les sciences."**  
*– Roger Bacon*

---

Développé avec ❤️ et beaucoup de ☕  
© 2026 **Jacques Junior Kossivi Agbenonzan**  
Université Félix Houphouët-Boigny • Abidjan, Côte d'Ivoire

*Dernière mise à jour : Janvier 2026* 📅

</div>  
*Version : MathCraft 1.0.0 - "Numerical Revolution"*
