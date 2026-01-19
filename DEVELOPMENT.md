# Développement Technique - MathCraft

Documentation technique pour les développeurs souhaitant contribuer ou comprendre l'architecture.

---

## 📋 Table des Matières

1. [Architecture](#-architecture)
2. [Stack Technique](#-stack-technique)
3. [Structure des Modules](#-structure-des-modules)
4. [Guide du Code](#-guide-du-code)
5. [Performance](#-performance)
6. [Tests](#-tests)
7. [Debugging](#-debugging)

---

## 🏗️ Architecture

### Vue d'ensemble

```
┌─────────────────────────────────────────┐
│         Interface Utilisateur            │
│      (Tkinter/ttk - Modules 1-9)        │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Couche de Présentation            │
│  - operation_de_base.py                 │
│  - theorie_des_nombres.py               │
│  - equation_numerique.py                │
│  - ... (autres interfaces)              │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Couche Métier/Services             │
│  - modules.py (Bibliothèque mathém.)   │
│  - historique_manager.py                │
│  - styles.py                            │
│  - soutient_manager.py                  │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Couche de Persistance              │
│  - data/*.json (Historique, défis)      │
│  - sauvegardes/ (Backups)               │
└─────────────────────────────────────────┘
```

### Flux de Données

```
Entrée Utilisateur
        ↓
Validation (Interface)
        ↓
Appel Module Mathématique
        ↓
Calcul + Itérations
        ↓
Formatage Résultats
        ↓
Affichage Interface
        ↓
Sauvegarde Historique (JSON)
```

---

## 🛠️ Stack Technique

### Langage et Versions

- **Python** : 3.8+ (Minimum 3.8, Recommandé 3.10+)
- **Encodage** : UTF-8 (fichiers source)
- **Shebang** : `#!/usr/bin/env python3` (Unix-like)

### Dépendances

```
Obligatoires :
├── tkinter       (Interface GUI - inclus Python)
├── numpy         (Calcul numérique)
└── matplotlib    (Visualisation)

Optionnels :
├── scipy         (Optimisation avancée)
├── sympy         (Calcul symbolique)
├── pytest        (Tests)
└── pyperclip     (Copie presse-papiers)
```

### Versions Testées

- **OS** :
  - Windows 10/11 ✅
  - Ubuntu 20.04/22.04 ✅
  - macOS 11+ ✅
  - Raspberry Pi OS ✅ (limité)

- **Python**:
  - 3.8.x ✅
  - 3.9.x ✅
  - 3.10.x ✅ (Recommandé)
  - 3.11.x ✅

---

## 📂 Structure des Modules

### Point d'entrée

```python
# main.py (335 lignes)
├── Importations des modules
├── Fonctions de menu (guide, à propos)
├── Initialisation Tkinter
├── Boucle principale (root.mainloop())
└── Gestion des fenêtres Toplevel
```

### Modules mathématiques

```python
# App/modules.py (~500+ lignes)
├── Intégration numérique (7 méthodes)
├── Résolution d'équations (9 méthodes)
├── Interpolation (5 méthodes)
├── Théorie des nombres
├── Utilitaires mathématiques
└── Préparation expressions
```

### Interfaces utilisateur (Pattern Adapter)

Chaque module suit le même pattern :

```python
# App/operation_de_base.py (440+ lignes)
def launch_operation(parent=None):
    """Lancer le module en Toplevel ou Frame"""
    is_toplevel = parent is None or isinstance(parent, tk.Tk)
    
    if is_toplevel:
        window = Toplevel(parent)
    else:
        window = ttk.Frame(parent)
    
    # UI components
    # Event handlers
    # Business logic calls to modules.py
```

### Gestion persistance

```python
# App/historique_manager.py (~200 lignes)
├── Classe HistoriqueManager
├── load_historique() - Charger depuis JSON
├── add_to_historique() - Ajouter entrée
├── save_historique() - Sauvegarder
├── export_csv() - Exporter données
└── clear_historique() - Vider
```

### Styles et Thèmes

```python
# App/styles.py (~100+ lignes)
├── PALETTE unifiée (couleurs)
├── ensure_styles_configured() - Appliquer styles
├── Custom TButton styles
├── Custom TEntry styles
└── Thème cohérent
```

---

## 💻 Guide du Code

### Conventions de Nommage

```python
# Variables
x_points          # Snake case
my_var            # Lowercase
MY_CONSTANT       # UPPERCASE

# Fonctions
def calculate_integral():          # Verbe + complément
def validate_input():
def prepare_expression():

# Classes
class IntegrationMethod:           # PascalCase
class HistoriqueManager:
class NumericSolver:

# Constantes Module
PALETTE = {...}
METHODES = [...]
MAX_ITERATIONS = 1000
```

### Structure Fonction Mathématique

```python
def racineBrent(f, a, b, epsilon=1e-10, max_iterations=1000):
    """
    [Docstring NumPy style]
    
    Args:
        f (callable): Fonction f(x)
        a, b (float): Intervalle [a, b]
        epsilon (float): Tolérance
        max_iterations (int): Limite itérations
    
    Returns:
        tuple: (racine, nb_iterations, details_list)
        - racine (float): Solution trouvée
        - nb_iterations (int): Nombre d'itérations effectuées
        - details_list (list): [
            {'iteration': 1, 'a': ..., 'b': ..., 'erreur': ...},
            ...
          ]
    """
    iterations = []
    
    for i in range(max_iterations):
        # Calcul
        iterations.append({
            'iteration': i + 1,
            'valeur': current_x,
            'erreur': current_error
        })
        
        if condition_convergence:
            break
    
    return racine, len(iterations), iterations
```

### Structure Interface Tkinter

```python
def launch_module(parent=None):
    """Lancer l'interface du module"""
    # 1. Déterminer type parent
    is_toplevel = parent is None or isinstance(parent, tk.Tk)
    
    # 2. Créer fenêtre
    if is_toplevel:
        window = Toplevel(parent)
        window.title("Module Title")
        window.geometry("800x600")
    else:
        window = ttk.Frame(parent)
    
    # 3. Configurer styles
    configurer_style()
    
    # 4. Créer widgets
    # - Labels
    # - Entries
    # - Buttons
    # - Canvases (graphiques)
    
    # 5. Layout (grid, pack, place)
    
    # 6. Binding événements
    def on_button_click():
        # Récupérer entrées
        # Valider
        # Appeler module.py
        # Afficher résultats
        # Sauvegarder historique
    
    button.bind('<Button-1>', lambda e: on_button_click())
    
    # 7. Retourner window pour Toplevel
    if is_toplevel:
        return window
```

### Validation Entrées

```python
def valider_input(value_str: str, type_expected: str) -> bool:
    """Valider avant appel module mathématique"""
    try:
        if type_expected == 'float':
            float(value_str)
        elif type_expected == 'int':
            int(value_str)
        elif type_expected == 'expr':
            compile(value_str, '<string>', 'eval')
        return True
    except (ValueError, SyntaxError):
        return False
```

### Export CSV

```python
import csv

def exporter_csv(filename: str, data: list, headers: list):
    """Exporter données en CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
```

### Graphiques Matplotlib

```python
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def afficher_graphique(parent_frame):
    """Intégrer graphique dans Tkinter"""
    fig = Figure(figsize=(8, 6), dpi=100)
    ax = fig.add_subplot(111)
    
    # Tracer
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    ax.plot(x, y, 'b-', label='sin(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    # Intégrer dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
```

---

## 🚀 Performance

### Optimisations Actuelles

1. **NumPy** pour calcul vectorisé
2. **Éviter boucles Python** pur
3. **Cache des résultats** partiels
4. **Graphiques Matplotlib** optimisés

### Points d'Amélioration

```python
# ❌ Lent (boucle Python)
result = 0
for i in range(len(x)):
    result += x[i] * y[i]

# ✅ Rapide (NumPy vectorisé)
result = np.dot(x, y)
```

### Benchmarking

```bash
# Mesurer temps
import time
start = time.time()
result = ma_fonction()
elapsed = time.time() - start
print(f"Temps: {elapsed:.4f}s")

# Profiler
import cProfile
cProfile.run('ma_fonction()', sort='cumtime')
```

### Memory Profiling

```bash
# Installer
pip install memory-profiler

# Utiliser
python -m memory_profiler mon_script.py
```

---

## 🧪 Tests

### Structure Tests

```python
# tests/test_modules.py
import pytest
from App.modules import intSimpsonC, racineNewton

class TestIntegration:
    def test_simpson_simple(self):
        f = lambda x: x**2
        result, iters = intSimpsonC(f, 0, 1, 10)
        assert abs(result - 1/3) < 1e-6
    
    def test_simpson_edges(self):
        # Test cas limites

class TestEquations:
    def test_newton_convergence(self):
        # Tester convergence Newton
```

### Exécuter Tests

```bash
# Tous les tests
pytest tests/

# Test spécifique
pytest tests/test_modules.py::TestIntegration::test_simpson_simple

# Avec output détaillé
pytest tests/ -v

# Avec couverture
pytest tests/ --cov=App --cov-report=html
```

### Coverage

```bash
# Générer rapport coverage
coverage run -m pytest tests/
coverage report
coverage html  # Générer HTML

# Voir couverture spécifique
coverage report -m  # Par ligne
```

---

## 🐛 Debugging

### Logs

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Utiliser
logger.debug("Message debug")
logger.info("Info")
logger.warning("Avertissement")
logger.error("Erreur")
```

### Points d'Arrêt

```python
# breakpoint() - Python 3.7+
def ma_fonction():
    x = 10
    breakpoint()  # Pdb lance ici
    y = x * 2
```

### Commandes PDB

```
(Pdb) n              # Next line
(Pdb) s              # Step in
(Pdb) c              # Continue
(Pdb) p variable     # Print variable
(Pdb) w              # Where (stack)
(Pdb) l              # List (code)
(Pdb) h              # Help
```

### Debugging Tkinter

```python
# Tracer callbacks
def on_button_click(event):
    print(f"Click: {event}")  # Debug
    # Code

# Voir state widgets
print(button.cget('state'))  # État du widget
print(entry.get())  # Valeur entry
```

### Erreurs Courantes

```python
# ❌ AttributeError: 'NoneType' object
window = Toplevel(parent)
# ...
return None  # Ne pas retourner window

# ✅ Retourner l'objet
return window

# ❌ ImportError: relative import
from .modules import fonction  # Non trouvé

# ✅ Chemin correct
from App.modules import fonction
```

---

## 📊 Métriques du Code

### Statistiques (v1.0.0)

| Fichier | Lignes | Fonctions | Complexité |
|---------|--------|-----------|-----------|
| modules.py | 2000+ | 50+ | Haute |
| operation_de_base.py | 440 | 20+ | Moyenne |
| equation_numerique.py | 981 | 40+ | Haute |
| interpolation_lineaire.py | 1361 | 50+ | Très haute |
| jeux_math.py | 8229 | 100+ | Très haute |
| **Total** | **~13,000+** | **250+** | **-** |

### Code Coverage Cible

- **Modules mathématiques** : 90%+
- **Interfaces** : 70%
- **Utilitaires** : 85%
- **Global** : 80%

---

## 🔧 Outils de Développement

### IDE Recommandé

- **VS Code** : Recommandé (Python Extension)
- **PyCharm** : Community Edition gratuite
- **Vim/NeoVim** : Pour expert terminal

### Extensions VS Code

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "charliermarsh.ruff",
    "ms-python.debugpy"
  ]
}
```

### Pre-commit Hooks

```bash
# Installer
pip install pre-commit

# Créer .pre-commit-config.yaml
# Installer hooks
pre-commit install

# Tester
pre-commit run --all-files
```

---

## 🚀 CI/CD (Futur)

### GitHub Actions (À implémenter)

```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.8', '3.9', '3.10']
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

---

## 📚 Ressources et Références

### Documentation

- [Python Docs](https://docs.python.org/3/)
- [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [NumPy Docs](https://numpy.org/doc/)
- [Matplotlib Docs](https://matplotlib.org/stable/contents.html)

### Tutoriels

- [Real Python](https://realpython.com/)
- [DataCamp](https://www.datacamp.com/)
- [Coursera](https://www.coursera.org/)

### Books

- "Fluent Python" - Luciano Ramalho
- "Clean Code" - Robert C. Martin
- "Design Patterns" - Gang of Four

---

## 🎯 Checklist Développeur

Avant de commit :

- [ ] Code testé localement
- [ ] Tests passent (`pytest tests/`)
- [ ] Pas d'erreurs linter (`pylint`)
- [ ] Style PEP 8 respecté (`black`)
- [ ] Docstrings complètes
- [ ] Commentaires clairs
- [ ] Pas d'imports inutiles
- [ ] README/docs à jour
- [ ] Pas de fichiers temporaires
- [ ] Messages commit clairs

---

## 🔗 Liens Utiles

- [GitHub Repository](https://github.com/JunRoot29/MathCraft)
- [Issues](https://github.com/JunRoot29/MathCraft/issues)
- [Pull Requests](https://github.com/JunRoot29/MathCraft/pulls)
- [Discussions](https://github.com/JunRoot29/MathCraft/discussions)

---

*Mise à jour : Janvier 2026*

**Questions ?** Ouvrir une issue ou contacter : junioragbenonzan31@gmail.com
