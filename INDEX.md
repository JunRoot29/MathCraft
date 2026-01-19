# 📖 Index Documentation - MathCraft

Guide complet de la documentation du projet MathCraft.

---

## 🎯 Démarrage Rapide

Pour commencer rapidement, lire dans cet ordre :

1. **[README.md](README.md)** - Vue d'ensemble générale (15 min)
2. **[INSTALLATION.md](INSTALLATION.md)** - Installation sur votre système (5 min)
3. **Lancer `python main.py`** (2 sec)

✅ **Vous êtes prêt !** Explorez les 9 modules.

---

## 📚 Documentation par Rôle

### 👨‍🎓 Utilisateur Final

**Je veux utiliser l'application :**
1. [INSTALLATION.md](INSTALLATION.md) - Installer
2. [README.md](README.md#-exemples-dutilisation) - Exemples d'usage
3. [FAQ.md](FAQ.md) - Questions fréquentes
4. Modules → Aide (?) - Aide contextuelle

**Je veux comprendre les mathématiques :**
- Voir les docstrings dans [App/modules.py](App/modules.py)
- Lire les guides d'aide dans chaque module
- Consulter les références externes

**J'ai un problème :**
1. Voir [FAQ.md](FAQ.md) → Dépannage
2. Ouvrir une [Issue](https://github.com/JunRoot29/MathCraft/issues)
3. Contacter : junioragbenonzan31@gmail.com

---

### 👨‍💻 Développeur

**Je veux contribuer :**
1. [CONTRIBUTING.md](CONTRIBUTING.md) - Guide complet
2. [DEVELOPMENT.md](DEVELOPMENT.md) - Architecture technique
3. Fork → Branche → Code → PR

**Je veux comprendre le code :**
1. [DEVELOPMENT.md](DEVELOPMENT.md#-guide-du-code) - Conventions
2. [Lire le code source](App/)
3. [DEVELOPMENT.md](DEVELOPMENT.md#-debugging) - Debugging

**Je veux ajouter une méthode mathématique :**
1. [DEVELOPMENT.md](DEVELOPMENT.md#-ajouter-une-nouvelle-méthode-mathématique)
2. Éditer [App/modules.py](App/modules.py)
3. Tester et documenter

---

### 👨‍🏫 Enseignant

**Je veux utiliser MathCraft en classe :**
1. [README.md](README.md) - Fonctionnalités
2. [INSTALLATION.md](INSTALLATION.md) - Installation classe
3. [FAQ.md](FAQ.md#-autres-questions) - Intégration pédagogique

**Je veux personnaliser pour mes cours :**
1. [DEVELOPMENT.md](DEVELOPMENT.md) - Architecture
2. Modifier [data/](data/) fichiers JSON
3. Ajouter vos propres défis/questions

**Je veux des ressources pédagogiques :**
- Exemples dans [README.md](README.md#-exemples-dutilisation)
- Guides intégrés dans chaque module
- Contacter : junioragbenonzan31@gmail.com

---

### 🔬 Chercheur

**Je veux utiliser MathCraft en recherche :**
1. [README.md](README.md#-bibliothèque-mathématique--modulespy) - API disponible
2. Importer depuis [App/modules.py](App/modules.py)
3. [DEVELOPMENT.md](DEVELOPMENT.md) - API techniques

**Je veux intégrer dans mes scripts :**
```python
from App.modules import interpolation_lagrange, racineNewton
# Utiliser directement les fonctions
```

**Je veux citer MathCraft :**
Voir [README.md](README.md#-citation-académique) pour format BibTeX

---

## 📂 Structure Fichiers Documentation

```
MathCraft/
├── README.md           # 🌍 Vue d'ensemble complète
├── INSTALLATION.md     # 📦 Guide installation par OS
├── CONTRIBUTING.md     # 🤝 Guide contribution code
├── DEVELOPMENT.md      # 💻 Architecture technique
├── FAQ.md              # ❓ 50+ questions réponses
├── CHANGELOG.md        # 📋 Historique versions
├── SUMMARY.md          # 📊 Résumé exécutif
├── INDEX.md            # 📖 Ce fichier
├── LICENSE             # ⚖️ Creative Commons BY-NC-SA
├── requirements.txt    # 📦 Dépendances
├── .gitignore          # 🚫 Git exclusions
└── main.py             # 🚀 Point d'entrée
```

---

## 📑 Fichiers Importants du Projet

### Code Source

| Fichier | Lignes | Rôle |
|---------|--------|------|
| [App/modules.py](App/modules.py) | 2000+ | Bibliothèque mathématique |
| [App/operation_de_base.py](App/operation_de_base.py) | 440 | Interface calculatrice |
| [App/equation_numerique.py](App/equation_numerique.py) | 981 | Interface équations |
| [App/interpolation_lineaire.py](App/interpolation_lineaire.py) | 1361 | Interface interpolation |
| [App/jeux_math.py](App/jeux_math.py) | 8229 | Jeux et défis |

### Données

| Fichier | Contenu |
|---------|---------|
| [data/historique_calculs.json](data/historique_calculs.json) | Historique persistant |
| [data/defis_fibonacci.json](data/defis_fibonacci.json) | Défis Fibonacci |
| [data/math_battle.json](data/math_battle.json) | Questions Battle |
| [data/question_enigme.json](data/question_enigme.json) | Énigmes |

---

## 🔍 Navigation par Sujet

### Mathématiques

**Théorie**
- Méthodes d'intégration : [README.md](README.md#-intégration-numérique)
- Solveurs d'équations : [README.md](README.md#-équations-numériques)
- Interpolation : [README.md](README.md#-interpolation-numérique)
- Implémentation : [App/modules.py](App/modules.py)

**Exemples d'usage**
- Intégration : [README.md](README.md#-intégration-numérique)
- Équations : [README.md](README.md#-résolution-déquation)
- Interpolation : [README.md](README.md#-interpolation-avec-graphique)

---

### Installation et Configuration

**Installation**
- Guide détaillé : [INSTALLATION.md](INSTALLATION.md)
- Dépendances : [requirements.txt](requirements.txt)
- Dépannage : [FAQ.md](FAQ.md#-questions-fréquemment-posées)

**Configuration**
- Variables env : [INSTALLATION.md](INSTALLATION.md#variables-denvironnement)
- Optimisation : [INSTALLATION.md](INSTALLATION.md#performance-tips)

---

### Utilisation de l'Application

**Interface**
- Fonctionnalités : [README.md](README.md#-fonctionnalités-principales)
- Modules : [README.md](README.md#-fonctionnalités-principales)
- Exemples : [README.md](README.md#-exemples-dutilisation)

**Jeux**
- Vue générale : [README.md](README.md#-jeux--concepts)
- Utilisation : [FAQ.md](FAQ.md#-jeux-et-défis)
- Données : [data/](data/) fichiers JSON

**Export**
- Formats : [README.md](README.md#-export-des-résultats)
- Comment faire : [FAQ.md](FAQ.md#-comment-exporter-les-résultats)

---

### Développement et Contribution

**Pour débuter**
1. [CONTRIBUTING.md](CONTRIBUTING.md) - Voir comment contribuer
2. [DEVELOPMENT.md](DEVELOPMENT.md) - Architecture technique
3. Fork et commencer

**Code**
- Conventions : [DEVELOPMENT.md](DEVELOPMENT.md#-guide-du-code)
- Architecture : [DEVELOPMENT.md](DEVELOPMENT.md#-architecture)
- Tests : [DEVELOPMENT.md](DEVELOPMENT.md#-tests)

**Bug fixes et features**
1. Ouvrir une Issue
2. [CONTRIBUTING.md](CONTRIBUTING.md) - Processus
3. PR et review

---

### Maintenance

**Mises à jour**
- Historique : [CHANGELOG.md](CHANGELOG.md)
- Nouveautés : [README.md](README.md#-feuille-de-route)
- Planification : [DEVELOPMENT.md](DEVELOPMENT.md#-ci-cd-futur)

**Support**
- FAQ : [FAQ.md](FAQ.md)
- Dépannage : [INSTALLATION.md](INSTALLATION.md#dépannage)
- Issues : [GitHub Issues](https://github.com/JunRoot29/MathCraft/issues)

---

## 🎓 Tutoriels et Guides

### Pour Débutants

**Premier lancement (5 min)**
```
1. Installer : python main.py
2. Explorer : Cliquer sur Opérations de Base
3. Essayer : Calculer sin(π/2)
4. Exporter : Bouton "Copier"
```

**Premiers calculs (15 min)**
1. Module 1 : Calculatrice simple
2. Module 2 : Tester la primalité
3. Module 3 : Convertir des unités

### Pour Intermédiaires

**Mathématiques numériques (30 min)**
1. Module 6 : Intégration (choisir Simpson)
2. Module 7 : Équations (essayer Newton)
3. Module 8 : Interpolation avec graphique

**Jeux et concepts (20 min)**
1. Module 9 : Défis Fibonacci
2. Module 9 : Battle Mathématique
3. Module 9 : Énigmes

### Pour Avancés

**Intégration dans scripts (1h)**
- Lire [DEVELOPMENT.md](DEVELOPMENT.md#-guide-du-code)
- Importer modules.py
- Utiliser l'API mathématique

**Contribution au code (variable)**
- Voir [CONTRIBUTING.md](CONTRIBUTING.md)
- Comprendre [DEVELOPMENT.md](DEVELOPMENT.md)
- Soumettre une PR

---

## 🆘 Aide et Support

### Questions Fréquentes

**Installation**
- Voir [FAQ.md](FAQ.md#-installation-et-configuration)
- Ou [INSTALLATION.md](INSTALLATION.md)

**Utilisation**
- Voir [FAQ.md](FAQ.md#-utilisation-de-lapplication)
- Ou [README.md](README.md#-exemples-dutilisation)

**Problèmes**
- Voir [FAQ.md](FAQ.md#-dépannage)
- Ou [INSTALLATION.md](INSTALLATION.md#dépannage)

**Développement**
- Voir [FAQ.md](FAQ.md#-développement-et-contribution)
- Ou [DEVELOPMENT.md](DEVELOPMENT.md)

### Contacter l'Auteur

- 📧 Email : junioragbenonzan31@gmail.com
- 🐙 GitHub : [@JunRoot29](https://github.com/JunRoot29)
- ☕ Ko-fi : [Soutenir](https://ko-fi.com/juniorkossivi)

### Signaler un Bug

1. Voir [FAQ.md](FAQ.md#-comment-signaler-un-bug)
2. Ouvrir une [Issue GitHub](https://github.com/JunRoot29/MathCraft/issues)
3. Décrire clairement le problème

### Proposer une Amélioration

1. Voir [FAQ.md](FAQ.md#-comment-proposer-une-nouvelle-fonctionnalité)
2. Ouvrir une [Issue GitHub](https://github.com/JunRoot29/MathCraft/issues) avec label "enhancement"
3. Décrire votre idée

---

## 🔗 Liens Rapides

### Documentation
- 📖 [README.md](README.md)
- 📦 [INSTALLATION.md](INSTALLATION.md)
- 🤝 [CONTRIBUTING.md](CONTRIBUTING.md)
- ❓ [FAQ.md](FAQ.md)
- 📋 [CHANGELOG.md](CHANGELOG.md)
- 💻 [DEVELOPMENT.md](DEVELOPMENT.md)
- 📊 [SUMMARY.md](SUMMARY.md)

### Projet
- 🐙 [GitHub](https://github.com/JunRoot29/MathCraft)
- 📁 [Code source](App/)
- 📊 [Données](data/)
- ⚖️ [Licence](LICENSE)

### Contact
- 📧 [Email](mailto:junioragbenonzan31@gmail.com)
- 💬 [Issues](https://github.com/JunRoot29/MathCraft/issues)
- ☕ [Ko-fi](https://ko-fi.com/juniorkossivi)

---

## 🗺️ Parcours Recommandé

### Pour Utilisateur Régulier
```
README.md → INSTALLATION.md → Modules 1-9 → FAQ.md
```

### Pour Enseignant
```
README.md → INSTALLATION.md → Modules (démo) → CONTRIBUTING.md (personnalisation)
```

### Pour Développeur
```
README.md → DEVELOPMENT.md → Code source → CONTRIBUTING.md → Coding
```

### Pour Chercheur
```
README.md → modules.py → API utilisation → Scripts
```

---

## 📅 Mise à Jour Documentation

| Fichier | Dernière MAJ | Statut |
|---------|--------------|--------|
| README.md | Jan 2026 | ✅ À jour |
| INSTALLATION.md | Jan 2026 | ✅ À jour |
| CONTRIBUTING.md | Jan 2026 | ✅ À jour |
| DEVELOPMENT.md | Jan 2026 | ✅ À jour |
| FAQ.md | Jan 2026 | ✅ À jour |
| CHANGELOG.md | Jan 2026 | ✅ À jour |

---

<div align="center">

## 🎯 Bienvenue dans MathCraft !

**Trouvez rapidement ce que vous cherchez en utilisant ce guide d'index.**

**Questions ?** → Voir [FAQ.md](FAQ.md)  
**Problème ?** → Voir [Dépannage](#-aide-et-support)  
**Contribuer ?** → Voir [CONTRIBUTING.md](CONTRIBUTING.md)

---

*Dernière mise à jour : Janvier 2026*

</div>
