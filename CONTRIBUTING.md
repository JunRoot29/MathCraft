# Guide de Contribution - MathCraft

Merci de votre intérêt pour contribuer à **MathCraft** ! Ce document guide explique comment participer au projet.

## 🤝 Code de Conduite

- Respecter tous les contributeurs
- Communiquer de manière constructive
- Accepter les critiques et les retours
- Se concentrer sur ce qui est meilleur pour la communauté

## 📋 Comment Contribuer

### 1. Signaler un Bug

**Avant de signaler :**
- Vérifier que le bug n'existe pas déjà dans les [Issues](https://github.com/JunRoot29/MathCraft/issues)
- Tester avec la dernière version
- Vérifier tous les prérequis

**Pour signaler :**
```bash
Titre : [BUG] Description courte

Description :
- Étapes pour reproduire
- Comportement attendu
- Comportement observé
- Environnement (OS, Python version, dépendances)
- Capture d'écran/Logs
```

### 2. Proposer une Amélioration

```bash
Titre : [FEATURE] Description courte

Motivation : Pourquoi cette fonctionnalité ?
Implémentation proposée : Comment l'ajouter ?
Cas d'usage : Quand l'utiliser ?
```

### 3. Soumettre du Code

#### Étape 1 : Fork et Clone

```bash
# 1. Fork sur GitHub (bouton Fork)
# 2. Cloner votre fork
git clone https://github.com/VOTRE_USERNAME/MathCraft.git
cd MathCraft

# 3. Ajouter le dépôt original
git remote add upstream https://github.com/JunRoot29/MathCraft.git

# 4. Créer une branche
git checkout -b feature/description-claire
```

#### Étape 2 : Développer

**Style de code :**
- **Language** : Python 3.8+
- **Format** : PEP 8
- **Docstrings** : Format NumPy/Google
- **Langue** : Commentaires en français

**Exemple de fonction :**
```python
def interpolation_lagrange(x_points, y_points, x):
    """
    Interpolation polynomiale par la méthode de Lagrange.
    
    Cette méthode construit un polynôme de degré n-1 passant par
    n points donnés en utilisant les polynômes de base de Lagrange.
    
    Args:
        x_points (list or np.ndarray): Abscisses des points de contrôle [n]
        y_points (list or np.ndarray): Ordonnées des points [n]
        x (float or np.ndarray): Point(s) d'évaluation
        
    Returns:
        float or np.ndarray: Valeur interpolée en x
        
    Exemple:
        >>> x = [0, 1, 2]
        >>> y = [0, 1, 4]
        >>> interpolation_lagrange(x, y, 1.5)
        2.25
    """
    # Implémentation...
```

**Tester votre code :**
```bash
# Tester une fonction
python -c "from App.modules import votre_fonction; print(votre_fonction(...))"

# Tester le module complet
python -m pytest tests/test_votre_module.py

# Vérifier le style
pylint App/votre_fichier.py
```

#### Étape 3 : Commit et Push

```bash
# Commits clairs et logiques
git add .
git commit -m "Feat: Ajouter interpolation Hermite"
git commit -m "Fix: Corriger bug convergence Newton"
git commit -m "Docs: Mettre à jour README pour module 7"

# Push vers votre fork
git push origin feature/description-claire
```

**Messages de commit :**
- `Feat:` - Nouvelle fonctionnalité
- `Fix:` - Correction de bug
- `Docs:` - Documentation
- `Style:` - Formatage, style
- `Refactor:` - Restructuration
- `Test:` - Tests et coverage
- `Perf:` - Optimisations

#### Étape 4 : Pull Request

1. Aller sur GitHub
2. Cliquer "New Pull Request"
3. Comparer votre branche avec `main`
4. Remplir le template PR

**Template Pull Request :**
```markdown
## Description
Brève description des changements

## Type de PR
- [ ] Bug fix
- [ ] Feature
- [ ] Documentation
- [ ] Refactor

## Lié à
Ferme #123

## Checklist
- [ ] J'ai testé les changements
- [ ] J'ai mis à jour la documentation
- [ ] Pas de dépendances nouvelles (ou justifiées)
- [ ] Code commenté en français
- [ ] Tests passent ✓
```

## 📂 Structure du Projet

```
App/
├── modules.py              # Bibliothèque mathématique (CORE)
├── operation_de_base.py    # Interface module 1
├── [autres modules].py     # Interfaces
├── historique_manager.py   # Gestion persistance
├── styles.py              # Thèmes unifiés
└── ...

data/                       # Données JSON
tests/                      # Tests unitaires (à créer)
CONTRIBUTING.md            # Ce fichier
INSTALLATION.md            # Guide d'installation
```

## 🔧 Ajouter une Nouvelle Méthode Mathématique

### 1. Dans `modules.py`

```python
def racineBisection(f, a, b, epsilon=1e-10, max_iterations=1000):
    """
    Résolution par bisection robuste.
    
    Args:
        f: Fonction callable f(x)
        a, b: Intervalle [a, b]
        epsilon: Tolérance
        max_iterations: Limite d'itérations
        
    Returns:
        tuple: (racine, nb_iterations, [détails])
    """
    iterations = []
    
    while abs(b - a) > epsilon and len(iterations) < max_iterations:
        c = (a + b) / 2
        fc = f(c)
        
        iterations.append({
            'iteration': len(iterations) + 1,
            'a': a,
            'b': b,
            'c': c,
            'fc': fc,
            'erreur': abs(b - a) / 2
        })
        
        if fc == 0:
            break
        elif f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return c, len(iterations), iterations
```

### 2. Ajouter à l'Interface

Dans `equation_numerique.py` ou similaire :

```python
# 1. Ajouter à METHODES
METHODES = [
    "...",
    "Bisection"  # Nouvelle
]

# 2. Ajouter le cas dans la sélection
def on_method_selected(event):
    if method_var.get() == "Bisection":
        # Afficher description Bisection
        show_bisection_guide()
```

### 3. Tester

```bash
python -c "
from App.modules import racineBisection
f = lambda x: x**3 - 2*x - 5
root, iterations, details = racineBisection(f, 2, 3)
print(f'Racine: {root}')
print(f'Itérations: {len(details)}')
"
```

## 📝 Documentation

### Mettre à jour le README

1. Ajouter la nouvelle fonctionnalité dans la section appropriée
2. Ajouter un exemple d'utilisation
3. Mettre à jour la feuille de route

### Créer une Documentation Détaillée

```markdown
## Module X : Nouvelle Fonctionnalité

**Fichier** : `App/nouveau_module.py`

### Description
...

### Fonctionnalités
- Feature 1
- Feature 2

### Exemple
```

## 🧪 Tests

### Écrire des Tests

```python
# tests/test_modules.py
import pytest
from App.modules import racineBisection

def test_bisection_simple():
    f = lambda x: x - 2
    root, iters, details = racineBisection(f, 1, 3)
    assert abs(root - 2) < 1e-6
    assert len(details) > 0

def test_bisection_cubic():
    f = lambda x: x**3 - 2*x - 5
    root, iters, details = racineBisection(f, 2, 3)
    assert abs(f(root)) < 1e-6
```

### Exécuter les Tests

```bash
# Tous les tests
pytest tests/

# Test spécifique
pytest tests/test_modules.py::test_bisection_simple

# Avec couverture
pytest --cov=App tests/
```

## 🚀 Process de Revue

1. **Vérification automatique** : CI/CD tests
2. **Revue du code** : Mainteneur vérifie
3. **Retours** : Demandes de changements
4. **Approbation** : 👍 Et merge !

## ✅ Checklist Avant de Commit

- [ ] Code testé localement
- [ ] Tests passent ✓
- [ ] Docstrings complètes
- [ ] Commentaires clairs
- [ ] Pas d'imports inutiles
- [ ] README/docs à jour
- [ ] Pas de fichiers temporaires
- [ ] Messages de commit clairs

## 📚 Ressources Utiles

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [GitHub Markdown](https://guides.github.com/features/mastering-markdown/)

## 🤔 Questions ?

- 📧 Email : junioragbenonzan31@gmail.com
- 💬 GitHub Issues
- 🐙 GitHub Discussions

## 🎯 Priorités de Contribution

**Hautement apprécié :**
- [ ] Corrections de bugs documentés
- [ ] Amélioration des performances
- [ ] Tests supplémentaires
- [ ] Documentation améliorée
- [ ] Traductions (i18n)

**En cours :**
- [ ] Module 9 complet
- [ ] Mode sombre/clair
- [ ] Export PDF

**Planifié v2.0 :**
- [ ] Algèbre linéaire
- [ ] Transformées de Fourier
- [ ] Version web

---

Merci de contribuer à MathCraft ! ❤️

*Dernière mise à jour : Janvier 2026*
