# Installation Guide pour MathCraft

## Prerequisites

- **Python** 3.8 ou supérieur
- **pip** (gestionnaire de paquets Python)
- **Tkinter** (généralement inclus avec Python)

## Installation Rapide

### Windows 10/11

```bash
# 1. Cloner le dépôt
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft

# 2. Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Vérifier que Tkinter est disponible
python -m tkinter

# 5. Lancer l'application
python main.py
```

### Linux (Ubuntu/Debian)

```bash
# 1. Installer les dépendances système
sudo apt-get update
sudo apt-get install python3 python3-pip python3-tk

# 2. Cloner et configurer
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft

python3 -m venv venv
source venv/bin/activate

# 3. Installer les paquets Python
pip install -r requirements.txt

# 4. Lancer
python3 main.py
```

### macOS

```bash
# 1. Installer Python (via Homebrew)
brew install python@3.10

# 2. Cloner le dépôt
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft

# 3. Créer l'environnement
python3 -m venv venv
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer
python3 main.py
```

## Dépannage

### ❌ Erreur : "No module named 'tkinter'"

**Windows :**
```bash
# Réinstaller Python avec Tkinter
# Aller à https://www.python.org/downloads/
# Cocher "tcl/tk and IDLE" lors de l'installation
```

**Linux :**
```bash
sudo apt-get install python3-tk
```

**macOS :**
```bash
brew install python-tk@3.10
```

### ❌ Erreur : "No module named 'numpy'" ou 'matplotlib'

```bash
# Réinstaller les dépendances
pip install --upgrade -r requirements.txt
```

### ❌ Erreur lors du démarrage

```bash
# Vérifier la version Python
python --version  # Doit être 3.8+

# Vérifier les dépendances
python -c "import tkinter; import numpy; import matplotlib; print('OK')"

# Vérifier l'installation
python test.py
```

## Configuration Optimale

Pour les meilleures performances :

### GPU Acceleration (Optionnel)
```bash
# Pour utiliser GPU avec NumPy
pip install cupy-cuda11x  # Adapter xx à votre version CUDA
```

### Installation Développeur
```bash
# Cloner avec développement
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft

# Environnement avec outils de dev
pip install -r requirements.txt
pip install pytest pytest-cov pylint black  # Optionnel

# Tester
python -m pytest tests/
```

## Variables d'Environnement

Optionnel pour customiser le comportement :

```bash
# Activer le mode debug
set MATHCRAFT_DEBUG=1  # Windows
export MATHCRAFT_DEBUG=1  # Linux/macOS

# Définir le répertoire de sauvegarde
set MATHCRAFT_DATA_DIR=./data  # Windows
export MATHCRAFT_DATA_DIR=./data  # Linux/macOS
```

## Vérification de l'Installation

```bash
python -c "
import sys
print(f'Python {sys.version}')
import tkinter as tk
print('✓ Tkinter disponible')
import numpy as np
print(f'✓ NumPy {np.__version__}')
import matplotlib
print(f'✓ Matplotlib {matplotlib.__version__}')
print('Installation OK!')
"
```

## Performance Tips

1. **Utiliser un environnement virtuel** : Évite les conflits de dépendances
2. **SSD recommandé** : Pour l'export graphique rapide
3. **Résolution min 1024x768** : Pour interface complète
4. **Au moins 1GB RAM** : Pour graphiques complexes

## Support

En cas de problème :
- Vérifier les [issues GitHub](https://github.com/JunRoot29/MathCraft/issues)
- Consulter le [README](README.md) principal
- Contacter : junioragbenonzan31@gmail.com

---

*Mise à jour : Janvier 2026*
