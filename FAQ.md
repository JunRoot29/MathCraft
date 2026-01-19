# FAQ - MathCraft

## Questions Fréquemment Posées

### 📦 Installation et Configuration

#### Q1: Comment installer MathCraft ?

**R:** Voir le fichier [INSTALLATION.md](INSTALLATION.md) pour les instructions complètes.

Résumé rapide :
```bash
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft
pip install -r requirements.txt
python main.py
```

#### Q2: Quels sont les prérequis système ?

**R:**
- **Python** 3.8 ou supérieur
- **RAM** : Minimum 512 MB, 1 GB recommandé
- **Espace disque** : 100 MB (avec dépendances)
- **OS** : Windows 10+, Linux (Ubuntu 18.04+), macOS 10.15+

#### Q3: Pourquoi Tkinter n'est pas installé ?

**R:** Tkinter est généralement inclus avec Python, mais sur Linux, installez-le séparément :

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS
brew install python-tk@3.10
```

#### Q4: Puis-je utiliser MathCraft sur Raspberry Pi ?

**R:** Oui, mais avec limitations :
- Interface plus lente
- Graphiques simples
- Historique limité
- Installation : `pip install -r requirements-lite.txt`

#### Q5: MathCraft fonctionne-t-il hors ligne ?

**R:** Oui, 100% hors ligne. Aucune connexion internet requise.

---

### 🚀 Utilisation de l'Application

#### Q6: Comment démarrer une nouvelle calculatrice ?

**R:** Cliquez sur l'une des 9 icônes du menu principal :
1. Opérations de base
2. Théorie des nombres
3. Conversion d'unités
4. Polynômes & équations
5. Chaînes de caractères
6. Intégration numérique
7. Équations numériques
8. Interpolation numérique
9. Jeux & concepts

#### Q7: Comment exporter les résultats ?

**R:** Pour chaque module complexe (Intégration, Équations, Interpolation) :
- **CSV** : Tableau → Bouton "Exporter CSV"
- **PNG** : Graphique → Bouton "Sauvegarder image"
- **Copier** : Ctrl+C ou bouton "Copier"

#### Q8: Où sont stockés mes calculs ?

**R:** Historique persistant dans :
- **Fichier** : `data/historique_calculs.json`
- **Accessibilité** : Menu "Historique"
- **Limitation** : Derniers 1000 calculs
- **Sauvegarde** : Automatique tous les calculs

#### Q9: Puis-je supprimer mon historique ?

**R:** Oui :
1. Menu → Historique
2. Bouton "Effacer l'historique"
3. Confirmer

Ou supprimer manuellement : `data/historique_calculs.json`

#### Q10: Comment réinitialiser les paramètres ?

**R:** Supprimer les fichiers de configuration :
```bash
rm data/historique_calculs.json
rm data/*.json  # Réinitialiser tous les jeux
```

---

### 🔢 Mathématiques et Calculs

#### Q11: Quelle est la précision de MathCraft ?

**R:** Dépend de la méthode :
- **Intégration** : Précision adjustable (jusqu'à 1e-15)
- **Équations** : Newton: 1e-14, Dichotomie: 1e-6
- **Interpolation** : Spline cubique: 1e-14

#### Q12: Comment définir la tolérance d'erreur ?

**R:** Dans les modules numériques (Équations, Intégration) :
1. Voir le champ "Epsilon" ou "Tolérance"
2. Entrer une valeur (ex: 1e-6)
3. Plus petit = plus précis mais plus lent

#### Q13: Quelles fonctions mathématiques sont supportées ?

**R:** Dans les expressions mathématiques, supportées :
```
Opérateurs : +, -, *, /, **, % (modulo)
Fonctions  : sin, cos, tan, asin, acos, atan,
             sinh, cosh, tanh, exp, log, log10,
             sqrt, abs, floor, ceil
Constantes : pi, e
```

Exemple valide : `sin(x) + exp(-x) / 2`

#### Q14: Comment entrer des nombres complexes ?

**R:** Format : `a+bj` ou `a-bj`

Exemples :
- `3+4j` (3 + 4i)
- `2-1j` (2 - i)

Supportés dans : Polynômes (degré 2)

#### Q15: L'application peut-elle traiter les domaines d'intégration infinis ?

**R:** Partiellement. Les méthodes classiques ne supportent que des intervalles finis [a, b].

Pour intégrer sur ℝ, utiliser :
- **Change de variable** : u = 1/x
- **Transformation** : ∫₀^∞ f(x)dx → ∫₀^1 f(1/u)/u² du

---

### 🎮 Jeux et Défis

#### Q16: Comment jouer aux défis Fibonacci ?

**R:**
1. Menu → Jeux & Concepts → Défis Fibonacci
2. Compléter la suite en 60 secondes
3. Réponses correctes = +10 points
4. Temps restant = points bonus

#### Q17: Qu'est-ce que la Battle Mathématique ?

**R:** Mini-jeu à choix multiples :
- 10 questions aléatoires
- 4 réponses par question
- Temps limité (30 sec/question)
- Classement automatique

#### Q18: Puis-je modifier les questions des jeux ?

**R:** Oui, en éditant les fichiers JSON :
- `data/defis_fibonacci.json`
- `data/math_battle.json`
- `data/question_enigme.json`

Format JSON simple, facile à modifier.

#### Q19: Comment débloquer les énigmes avancées ?

**R:** Les énigmes se déverrouillent progressivement. Complétez-en plusieurs pour accéder aux niveaux supérieurs.

---

### 🛠️ Dépannage

#### Q20: L'application ne démarre pas

**R:**
1. Vérifier Python 3.8+ : `python --version`
2. Vérifier Tkinter : `python -m tkinter`
3. Installer les dépendances : `pip install -r requirements.txt`
4. Vérifier les logs : `python main.py 2>&1`

#### Q21: Erreur "No module named 'App'"

**R:** Vous n'êtes pas dans le bon répertoire :
```bash
cd MathCraft  # Doit contenir main.py
python main.py
```

#### Q22: Graphiques ne s'affichent pas

**R:** Problème d'affichage Matplotlib :
```bash
# Réinstaller Matplotlib
pip install --upgrade matplotlib

# Ou forcer un backend
pip install PyQt5
```

#### Q23: Application très lente

**R:**
- Réduire le nombre d'itérations (n=100 au lieu de 10000)
- Fermer d'autres applications
- Vérifier RAM disponible (>500MB)
- Utiliser SSD plutôt que HDD

#### Q24: Historique corrompu / fichiers JSON vides

**R:**
```bash
# Supprimer les fichiers
rm data/historique_calculs.json

# Relancer l'application (recréera les fichiers)
python main.py
```

#### Q25: Erreur lors de l'export CSV

**R:**
- Vérifier que le répertoire `data/` existe
- Créer manuellement : `mkdir data`
- Vérifier les permissions d'écriture
- Utiliser un chemin sans caractères spéciaux

---

### 💻 Développement et Contribution

#### Q26: Comment ajouter une nouvelle méthode mathématique ?

**R:** Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour le guide complet.

Résumé :
1. Coder dans `App/modules.py`
2. Ajouter interface dans le module correspondant
3. Tester avec `pytest`
4. Documenter et PR

#### Q27: Où sont les tests unitaires ?

**R:** Actuellement dans le fichier `test.py` à la racine.

Création de tests complets en cours.

#### Q28: Comment configurer un environnement de développement ?

**R:**
```bash
# Fork et clone votre version
git clone https://github.com/VOTRE_USERNAME/MathCraft.git
cd MathCraft

# Environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# Outils de dev
pip install -r requirements.txt
pip install pylint black pytest pytest-cov
```

#### Q29: Puis-je utiliser MathCraft en tant que librairie ?

**R:** Oui, l'API mathématique est accessible :

```python
from App.modules import intSimpsonC, racineNewton

# Intégration
f = lambda x: x**2
resultat, iterations = intSimpsonC(f, 0, 1, 100)

# Équation
f = lambda x: x**3 - 2
df = lambda x: 3*x**2
racine, n_iter, details = racineNewton(f, df, 1.5)
```

#### Q30: Comment contribuer une traduction ?

**R:** Contactez l'auteur pour i18n complet.

Actuellement : Français et interface partiellement en anglais.

---

### 🔐 Sécurité et Confidentialité

#### Q31: MathCraft envoie-t-il des données à distance ?

**R:** Non, l'application est 100% hors ligne.
- Pas de connexion internet
- Pas de télémétrie
- Pas de suivi utilisateur
- Données locales uniquement

#### Q32: Mes calculs sont-ils sauvegardés en toute sécurité ?

**R:** Oui, stockés en JSON dans `data/` :
- Accès local uniquement
- Chiffrage : Non (données locales)
- Sauvegarde : Manuelle ou export
- Suppression : Contrôle total

#### Q33: Comment sauvegarder mes données ?

**R:**
```bash
# Copier les fichiers de données
cp -r data/ backup_mathcraft/

# Ou exporter en CSV depuis chaque module
```

---

### 📊 Performances et Optimisations

#### Q34: Pourquoi certains calculs sont-ils lents ?

**R:** Causes possibles :
- Trop d'itérations (n > 10000)
- Fonction complexe à évaluer
- Graphique avec beaucoup de points
- PC en arrière-plan chargé

Solutions :
- Réduire n
- Augmenter tolérance ε
- Fermer autres applications

#### Q35: Quelle est la limite du nombre d'itérations ?

**R:** Recommandations :
- Intégration : n ≤ 100,000
- Équations : ≤ 10,000 itérations max
- Interpolation : ≤ 10,000 points

Limites hardware varient selon la RAM.

#### Q36: Comment améliorer la vitesse ?

**R:**
1. Utiliser SSD plutôt que HDD
2. Augmenter la RAM disponible
3. Fermer navigateur/éditeur en arrière-plan
4. Réduire n ou augmenter ε

---

### 📚 Documentation et Apprentissage

#### Q37: Existe-t-il un tutoriel vidéo ?

**R:** Pas encore, en développement pour v2.0.

Pour le moment :
- README : Documentation complète
- INSTALLATION.md : Guide détaillé
- CONTRIBUTING.md : Exemples code
- Commentaires : Dans les interfaces

#### Q38: Comment apprendre à utiliser les méthodes ?

**R:** Chaque module a :
- Guide d'aide (bouton ❓)
- Exemples préconfigurés
- Documentation inline
- Commentaires détaillés

#### Q39: Où trouver les explications mathématiques ?

**R:**
- Lire le code dans `App/modules.py`
- Voir les docstrings
- Consulter les ressources externes
- Contacter l'auteur

#### Q40: Le code est-il bien documenté ?

**R:** Oui :
- Docstrings complets (NumPy style)
- Commentaires explicatifs
- Types hints (partiels)
- Exemples dans docstrings

---

### 🤝 Support et Contact

#### Q41: Comment signaler un bug ?

**R:** Ouvrir une [Issue GitHub](https://github.com/JunRoot29/MathCraft/issues) avec :
- Titre descriptif
- Étapes pour reproduire
- Comportement attendu vs observé
- Environnement (OS, Python, dépendances)
- Logs d'erreur
- Capture d'écran

#### Q42: Comment proposer une nouvelle fonctionnalité ?

**R:** Ouvrir une [Issue avec label "enhancement"](https://github.com/JunRoot29/MathCraft/issues) :
- Description claire
- Cas d'usage
- Bénéfices attendus
- Implémentation proposée

#### Q43: Comment obtenir du support ?

**R:** Canaux disponibles :
1. 📧 Email : junioragbenonzan31@gmail.com
2. 🐙 GitHub Issues/Discussions
3. ☕ Ko-fi : https://ko-fi.com/juniorkossivi

#### Q44: Le projet est-il maintenu activement ?

**R:** Oui ! Mis à jour régulièrement avec :
- Corrections de bugs
- Nouvelles fonctionnalités
- Améliorations
- Support utilisateur

#### Q45: Puis-je utiliser MathCraft commercialement ?

**R:** Voir la [Licence](LICENSE) : Creative Commons BY-NC-SA 4.0

- ✅ Usage éducatif libre
- ✅ Modifications avec attribution
- ⚠️ Commercial sur autorisation
- ❌ Pas de revendication de paternité

Pour usage commercial, [contactez l'auteur](mailto:junioragbenonzan31@gmail.com).

---

### ✨ Autres Questions

#### Q46: Est-ce qu'il y a une version mobile ?

**R:** Pas actuellement. Planifié pour v2.0 (Kivy).

#### Q47: Peut-on intégrer MathCraft dans Jupyter Notebook ?

**R:** Partiellement. Les modules mathématiques oui :
```python
from App.modules import intSimpsonC
```

L'interface graphique Tkinter non (utilise UI différente).

#### Q48: Comment mettre à jour vers une nouvelle version ?

**R:**
```bash
cd MathCraft
git pull origin main
pip install -r requirements.txt --upgrade
python main.py
```

#### Q49: Y a-t-il des plans pour un langage non-français ?

**R:** Oui, i18n partiellement en cours.

Langues prévues : Anglais d'abord, puis autres.

#### Q50: Comment puis-je soutenir le projet ?

**R:**
- ⭐ Mettre une étoile sur GitHub
- 🔄 Partager avec vos collègues
- 💬 Laisser un retour
- 💡 Proposer des améliorations
- ☕ Soutenir via Ko-fi : https://ko-fi.com/juniorkossivi

---

## 🔗 Liens Utiles

- 📖 [README Principal](README.md)
- 📦 [Installation](INSTALLATION.md)
- 🤝 [Guide de Contribution](CONTRIBUTING.md)
- 🐙 [GitHub](https://github.com/JunRoot29/MathCraft)
- 💬 [Issues](https://github.com/JunRoot29/MathCraft/issues)
- 📧 [Email Support](mailto:junioragbenonzan31@gmail.com)
- ☕ [Ko-fi](https://ko-fi.com/juniorkossivi)

---

**Vous n'avez pas trouvé votre réponse ?**

Ouvrir une [nouvelle issue](https://github.com/JunRoot29/MathCraft/issues/new) ou [contacter l'auteur](mailto:junioragbenonzan31@gmail.com) ! 😊

*Mise à jour : Janvier 2026*
