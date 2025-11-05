# 🧮 MathCraft
> *Un espace malin pour calculer et s'amuser avec les maths. 🧠✨*


## 📝 Description
MathCraft est une application éducative interactive développée en Python avec Tkinter, offrant une plateforme complète pour explorer et pratiquer différents concepts mathématiques de manière ludique et intuitive. L'application propose 7 modules couvrant un large éventail de domaines mathématiques.


## ✨ Fonctionnalités

### 📊 Module 1 : Opérations de Base
- Calculatrice scientifique avec opérations arithmétiques, trigonométrie, logarithmes, puissances, racines, constantes (π, e), conversion degré/radian

### 🔢 Module 2 : Théorie des Nombres
- Test de primalité, nombres parfaits, PGCD, PPCM, nombres Catalans, chiffres distincts

### 🔄 Module 3 : Conversion
- Longueur, température, masse, vitesse, angles

### 📐 Module 5 : Polynômes & Équations
- Résolution d'équations du 1er et 2ème degré (réelles et complexes)

### 📝 Module 6 : Chaînes de Caractères
- Comptage de voyelles, lettres, mots, test de palindrome

### ∫ Module 7 : Intégration Numérique
- Méthodes : rectangles (gauche/droite/centre), trapèzes (simple/composite), Simpson (simple/composite)

## 🛠️ Technologies utilisées
- Python 3.x
- Tkinter / ttk
- NumPy
- Matplotlib
- Modules standards : math, re

## 📋 Prérequis
```bash
pip install numpy matplotlib
python -m tkinter  # pour tester l'installation
```

## ⚡ Démarrage rapide
```bash
# Cloner et lancer en 3 commandes
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft && pip install -r requirements.txt
python main.py
```

## 🚀 Installation
```bash
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft
pip install -r requirements.txt
python main.py
```

## 📂 Structure du projet
```
MathCraft/
├── main.py
├── README.md
├── requirements.txt
├── App/
│   ├── modules.py
│   ├── operation_de_base.py
│   ├── theorie_des_nombres.py
│   ├── conversion.py
│   ├── polynome.py
│   ├── chaine_de_caractere.py
│   └── integration_numerique.py
└── Image/
    └── screenshot.png
```

## 💡 Exemples d'utilisation

### Calculer un PGCD
1. Lancez l'application
2. Sélectionnez "Théorie des Nombres"
3. Entrez deux nombres
4. Cliquez sur "PGCD"

### Résoudre une équation du 2nd degré
Module Polynômes → ax² + bx + c = 0 → Solutions réelles/complexes

### Intégration numérique
Module Intégration → Choisir la méthode → Entrer la fonction et les bornes → Résultat instantané

## 🎨 Interface
- Design moderne : `#F5F0E6` / `#2C3E50`
- Police : Century Gothic
- Navigation fluide, boutons uniformes, feedback visuel clair

## 🔬 Bibliothèque `modules.py`
- Fonctions : arithmétique, trigonométrie, tableaux, matrices, équations, intégration
- Méthodes : dichotomie, Newton, point fixe, Fibonacci, Catalans, PGCD, PPCM

## 🗺️ Feuille de route

- [x] Modules 1-3, 5-7
- [ ] Module 4 : Explorateur de Concepts
- [ ] Graphiques interactifs (Matplotlib)
- [ ] Export PDF/CSV des résultats
- [ ] Mode sombre
- [ ] Tests unitaires
- [ ] Version mobile

## 🤝 Contribution
```bash
git checkout -b feature/NouvelleFonction
git commit -m "Ajout d'une nouvelle fonctionnalité"
git push origin feature/NouvelleFonction
```

**Guidelines :**
- Commentez votre code en français
- Respectez le style de code existant
- Testez vos modifications avant de soumettre
- Ouvrez une Pull Request avec une description détaillée

## ❓ FAQ

**Q : L'application ne se lance pas ?**  
R : Vérifiez que Python 3.x et tkinter sont installés : `python -m tkinter`

**Q : Puis-je ajouter mes propres formules ?**  
R : Oui ! Consultez `modules.py` et suivez le guide de contribution

**Q : Quels OS sont supportés ?**  
R : Windows, Linux, macOS (avec Python 3.x et tkinter)

**Q : Comment signaler un bug ?**  
R : Ouvrez une issue sur GitHub avec les détails et captures d'écran

## 🐛 Signaler un bug
1. Vérifiez que toutes les dépendances sont installées
2. Ouvrez une issue sur GitHub avec :
   - Description du problème
   - Étapes pour reproduire
   - Captures d'écran si possible
   - Version de Python utilisée

## 📝 Crédits
- **Développeur** : Junior Kossivi
- **Date** : Mai 2024
- **Lieu** : Port-Bouët, Abidjan, Côte d'Ivoire
- **Institution** : Université Félix Houphouët-Boigny

## 🙏 Remerciements
Merci à l'Université Félix Houphouët-Boigny pour son soutien académique.  
Projet inspiré par la passion de rendre les mathématiques accessibles à tous.

## 📄 Licence
**Projet éducatif open source**

- ✅ Usage éducatif et non commercial autorisé
- ✅ Modifications autorisées avec attribution
- ✅ Partage encouragé dans un cadre pédagogique
- ❌ Usage commercial interdit sans permission explicite

Pour toute utilisation commerciale, veuillez contacter l'auteur.

## 📦 Fichier `requirements`



```txt
numpy>=1.20.0
matplotlib>=3.3.0
```


## 📧 Contact
📧 **Email** : junioragbenonzan31@gmail.com  
🐙 **GitHub** : [@JunRoot29](https://github.com/JunRoot29)

---

<div align="center">
Fait avec ❤️ et ☕ à Abidjan | © 2025 Junior Kossivi
</div>

---

<div align="center">
====================================================================================================================

====================================================================================================================
</div>

# 🧮 MathCraft
> *A smart space to calculate and enjoy math. 🧠✨*

## 📝 Description
MathCraft is an interactive educational application built with Python and Tkinter. It offers a complete platform to explore and practice various mathematical concepts in a fun and intuitive way. The app includes 7 modules covering a wide range of mathematical topics.

## ✨ Features

### 📊 Module 1: Basic Operations
- Scientific calculator with arithmetic operations, trigonometry, logarithms, powers, roots, constants (π, e), degree/radian conversion

### 🔢 Module 2: Number Theory
- Primality test, perfect numbers, GCD, LCM, Catalan numbers, digit uniqueness

### 🔄 Module 3: Unit Conversion
- Length, temperature, mass, speed, angles

### 📐 Module 5: Polynomials & Equations
- Solve first and second-degree equations (real and complex solutions)

### 📝 Module 6: String Operations
- Count vowels, letters, words, palindrome check

### ∫ Module 7: Numerical Integration
- Methods: rectangles (left/right/midpoint), trapezoids (simple/composite), Simpson (simple/composite)

## 🛠️ Technologies Used
- Python 3.x
- Tkinter / ttk
- NumPy
- Matplotlib
- Standard libraries: math, re

## 📋 Requirements
```bash
pip install numpy matplotlib
python -m tkinter  # to test Tkinter installation
```

## ⚡ Quick Start
```bash
# Clone and launch in 3 commands
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft && pip install -r requirements.txt
python main.py
```

## 🚀 Installation
```bash
git clone https://github.com/JunRoot29/MathCraft.git
cd MathCraft
pip install -r requirements.txt
python main.py
```

## 📂 Project Structure
```
MathCraft/
├── main.py
├── README.md
├── requirements.txt
├── App/
│   ├── modules.py
│   ├── operation_de_base.py
│   ├── theorie_des_nombres.py
│   ├── conversion.py
│   ├── polynome.py
│   ├── chaine_de_caractere.py
│   └── integration_numerique.py
└── Image/
    └── screenshot.png
```

## 💡 Usage Examples

### Calculate GCD
1. Launch the app
2. Select "Number Theory"
3. Enter two numbers
4. Click "GCD"

### Solve a quadratic equation
Polynomials Module → ax² + bx + c = 0 → Real/complex solutions

### Numerical integration
Integration Module → Choose method → Enter function and bounds → Instant result

## 🎨 Interface
- Modern design: `#F5F0E6` / `#2C3E50`
- Font: Century Gothic
- Smooth navigation, uniform buttons, clear visual feedback

## 🔬 `modules.py` Library
- Functions: arithmetic, trigonometry, arrays, matrices, equations, integration
- Methods: bisection, Newton, fixed-point, Fibonacci, Catalan, GCD, LCM

## 🗺️ Roadmap

- [x] Modules 1–3, 5–7
- [ ] Module 4: Concept Explorer
- [ ] Interactive graphs (Matplotlib)
- [ ] Export results to PDF/CSV
- [ ] Dark mode
- [ ] Unit tests
- [ ] Mobile version

## 🤝 Contributing
```bash
git checkout -b feature/NewFeature
git commit -m "Add a new feature"
git push origin feature/NewFeature
```

**Guidelines:**
- Comment your code in French
- Follow existing code style
- Test your changes before submitting
- Open a Pull Request with a detailed description

## ❓ FAQ

**Q: The app won’t launch?**  
A: Make sure Python 3.x and Tkinter are installed: `python -m tkinter`

**Q: Can I add my own formulas?**  
A: Yes! Check `modules.py` and follow the contribution guide

**Q: Which OS are supported?**  
A: Windows, Linux, macOS (with Python 3.x and Tkinter)

**Q: How do I report a bug?**  
A: Open a GitHub issue with details and screenshots

## 🐛 Bug Reporting
1. Ensure all dependencies are installed
2. Open a GitHub issue with:
   - Problem description
   - Steps to reproduce
   - Screenshots if possible
   - Python version used

## 📝 Credits
- **Developer**: Junior Kossivi
- **Date**: May 2024
- **Location**: Port-Bouët, Abidjan, Côte d'Ivoire
- **Institution**: Université Félix Houphouët-Boigny

## 🙏 Acknowledgments
Thanks to Université Félix Houphouët-Boigny for academic support.  
This project is inspired by the passion to make mathematics accessible to all.

## 📄 License
**Open-source educational project**

- ✅ Educational and non-commercial use allowed
- ✅ Modifications allowed with attribution
- ✅ Sharing encouraged in academic settings
- ❌ Commercial use prohibited without explicit permission

For commercial use, please contact the author.

## 📦 `requirements.txt`
```txt
numpy>=1.20.0
matplotlib>=3.3.0
```

## 📧 Contact
📧 **Email**: junioragbenonzan31@gmail.com  
🐙 **GitHub**: [@JunRoot29](https://github.com/JunRoot29)

---

<div align="center">
Made with ❤️ and ☕ in Abidjan | © 2025 Junior Kossivi
</div>
```

---
