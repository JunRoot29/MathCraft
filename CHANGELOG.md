# Changelog - MathCraft

Toutes les modifications notables du projet MathCraft sont documentées dans ce fichier.

Format basé sur [Keep a Changelog](https://keepachangelog.com/) et [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - Janvier 2026 - Version Officielle

### ✨ Ajouté

#### Module 1 : Opérations de Base
- Calculatrice scientifique complète
- Trigonométrie (sin, cos, tan, asin, acos, atan, sinh, cosh, tanh)
- Logarithmes et exponentielles (log, log10, ln, exp)
- Puissances, racines et valeurs absolues
- Constantes (π, e)
- Conversion degrés ↔ radians
- Historique des calculs avec copie rapide

#### Module 2 : Théorie des Nombres
- Test de primalité optimisé
- Nombres parfaits (détection)
- PGCD / PPCM (algorithme euclidien)
- Nombres de Fibonacci (jusqu'à F(1000))
- Nombres de Catalan
- Vérification de chiffres distincts
- Factorisation basique

#### Module 3 : Conversion d'Unités
- **Longueur** : mm, cm, m, km, pouces, pieds, miles
- **Masse** : mg, g, kg, tonnes, onces, livres
- **Température** : Celsius ↔ Fahrenheit ↔ Kelvin
- **Vitesse** : m/s, km/h, nœuds, mph
- **Angles** : degrés, radians, gradians
- **Pression** : Pa, kPa, bar, atm, psi
- Prévisualisation en temps réel

#### Module 4 : Polynômes & Équations
- Équations du 1er degré (ax + b = 0)
- Équations du 2ème degré (solutions réelles et complexes)
- Affichage graphique des racines
- Discriminant et analyse
- Support des nombres complexes

#### Module 5 : Chaînes de Caractères
- Comptage de voyelles et consonnes
- Comptage de mots et caractères
- Test de palindrome
- Fréquence des caractères
- Statistiques détaillées
- Conversion casse (maj/min)
- Inversion de chaîne

#### Module 6 : Intégration Numérique
- 7 méthodes d'intégration :
  * Rectangles à gauche
  * Rectangles à droite
  * Rectangles au centre
  * Trapèzes
  * Simpson (1/3)
- **Affichage en temps réel** des itérations
- **Tableau détaillé** de chaque étape
- **Comparaison des méthodes**
- **Export CSV** des résultats
- Précision configurable (jusqu'à 1e-15)

#### Module 7 : Équations Numériques
- 9 méthodes de résolution :
  * Dichotomie (robuste)
  * Newton-Raphson (converge rapide)
  * Point Fixe (pour g(x)=x)
  * Sécante (sans dérivée)
  * Regula Falsi (hybride)
  * Müller (racines complexes)
  * Steffensen (accélération)
  * Brent (industriel)
  * Ridders (extrapolation)
- **Suivi détaillé** de chaque itération
- **Convergence visualisée**
- **Comparaison des performances**
- **Export CSV** détaillé
- Gestion des cas complexes

#### Module 8 : Interpolation Numérique
- 5 méthodes d'interpolation :
  * Lagrange (polynôme exact)
  * Newton (différences divisées)
  * Linéaire par morceaux (segments)
  * Spline Cubique Naturelle (courbes lisses)
  * Hermite (avec dérivées)
- **Visualisation graphique** interactive
- **Calculs étape par étape** affichés
- **Tableau d'itérations** complet
- **Export PNG** haute résolution
- **Export CSV** des résultats
- **Zoom interactif** et navigation
- Évaluation multiple en x

#### Module 9 : Jeux & Concepts
- **Défis Fibonacci** : Compléter les suites en temps limité
- **Battle Mathématique** : Quiz à choix multiples avec classement
- **Énigmes mathématiques** : Puzzles progressifs
- **Explorateur de concepts** : Démonstrations visuelles
- Système de points et progression
- Stockage des scores

#### Infrastructure
- **Interface unifiée** avec palette de couleurs cohérente
- **Historique persistant** en JSON
- **Gestionnaire d'historique** complet
- **Styles thématiques** (Century Gothic, couleurs harmonieuses)
- **Messages contextuels** et feedback utilisateur
- **Validation en temps réel** des entrées
- **Copie rapide** des résultats
- **Support clavier** (raccourcis)
- **Barres de défilement** pour interfaces longues
- **Support de la molette souris** pour navigation

### 📚 Documentation

- [x] README complet avec exemples
- [x] INSTALLATION.md avec guide pas à pas
- [x] CONTRIBUTING.md pour contributeurs
- [x] FAQ.md avec 50+ questions
- [x] Commentaires détaillés en code (français)
- [x] Docstrings complets (NumPy style)
- [x] Guide d'aide intégré dans chaque module

### 🔧 Technique

- **Langage** : Python 3.8+
- **Interface** : Tkinter/ttk
- **Numériques** : NumPy, Matplotlib
- **Données** : JSON persistant
- **Code** : ~8000 lignes, bien structuré
- **Tests** : Coverage de base, test.py
- **Performance** : Optimisé pour temps réel

---

## [0.9.0] - Décembre 2025 - Pre-Release

### ✨ Ajouté

- Modules 1-7 avec fonctionnalités complètes
- Interface graphique de base
- Export CSV pour modules numériques
- Historique persistant basique
- Support graphique Matplotlib

### 🐛 Corrigé

- Bugs de stabilité Tkinter
- Validations d'entrées renforcées
- Gestion des cas limites mathématiques

### ⚠️ Limitations

- Module 9 en développement
- Mode sombre non implémenté
- Pas de support multi-langue complet
- Export PDF non disponible

---

## [0.8.0] - Octobre 2025 - Beta

### ✨ Ajouté

- Modules 1-6 complets
- Intégration numérique (7 méthodes)
- Interface Tkinter basique
- Système d'historique JSON

---

## [0.1.0] - Septembre 2025 - Alpha

### ✨ Ajouté

- Modules mathématiques de base (modules.py)
- Calculatrice simple (operation_de_base.py)
- Théorie des nombres (theorie_des_nombres.py)

---

## Plan Futur

### v1.1.0 (Q1 2026)
- [ ] Optimisations performance
- [ ] Bugs corrections
- [ ] Tests unitaires améliorés
- [ ] Nouveaux exemples

### v1.2.0 (Q2 2026)
- [ ] Mode sombre/clair
- [ ] Export PDF
- [ ] Interface thématisable
- [ ] Raccourcis clavier complètement mappés

### v2.0.0 (H2 2026)
- [ ] Calcul différentiel numérique
- [ ] Transformées de Fourier
- [ ] Algèbre linéaire avancée
- [ ] Statistiques et probabilités
- [ ] Version web (Streamlit)
- [ ] Internationalisation complète

### v2.5.0 (2027)
- [ ] Application mobile (Kivy)
- [ ] Calcul symbolique (SymPy)
- [ ] Base de données avancée
- [ ] Système de plugins

---

## 📊 Statistiques de Version

### v1.0.0
- **Fichiers** : 15+ modules Python
- **Lignes de code** : ~8000+
- **Tests** : Coverage de base
- **Documentation** : 5 fichiers (README, INSTALLATION, CONTRIBUTING, FAQ, CHANGELOG)
- **Modules mathématiques** : 50+
- **Interfaces utilisateur** : 9
- **Jeux inclus** : 4
- **Formats d'export** : CSV, PNG, JSON

---

## 🙏 Remerciements

Merci à :
- Équipe pédagogique UFR-MI
- Utilisateurs pour les retours
- Communauté Python Francophone
- Contributors (actuels et futurs)

---

## 📝 Notes de Publication

### v1.0.0 - Stable

MathCraft atteint sa v1.0 avec :
✅ 9 modules complets et testés  
✅ Interface utilisateur professionnelle  
✅ Tous les algorithmes mathématiques clés  
✅ Support d'export complet  
✅ Documentation exhaustive  
✅ Prêt pour usage éducatif en production  

**Recommandations** :
- Tester sur votre système avant déploiement en classe
- Avoir Python 3.8+ et dépendances installées
- Pour Raspberry Pi : limiter n des itérations
- Sauvegarder régulièrement les données utilisateur

---

## 🐛 Historique des Corrections

### Problèmes résolus en v1.0.0

| Date | Issue | Statut |
|------|-------|--------|
| Jan 2026 | Stabilité Tkinter | ✅ Corrigé |
| Jan 2026 | Export CSV avec caractères spéciaux | ✅ Corrigé |
| Dec 2025 | Graphiques non affichés | ✅ Corrigé |
| Dec 2025 | Historique corrompu | ✅ Corrigé |
| Oct 2025 | Interface lente avec beaucoup d'itérations | ✅ Optimisé |

---

## 📖 Comment Lire ce Changelog

- **✨ Ajouté** : Nouvelles fonctionnalités
- **🔧 Modifié** : Changements d'API ou comportement
- **🐛 Corrigé** : Bug fixes
- **⚠️ Dépréciée** : Fonctionnalités en fin de vie
- **❌ Supprimée** : Fonctionnalités retirées
- **🔒 Sécurité** : Correctifs de sécurité

---

## 🔗 Liens Utiles

- [Versions GitHub](https://github.com/JunRoot29/MathCraft/releases)
- [Commits](https://github.com/JunRoot29/MathCraft/commits/main)
- [Issues](https://github.com/JunRoot29/MathCraft/issues)
- [Pull Requests](https://github.com/JunRoot29/MathCraft/pulls)

---

*Pour plus de détails, consultez les [commits](https://github.com/JunRoot29/MathCraft/commits/main)*

*Dernière mise à jour : Janvier 2026*
