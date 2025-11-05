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
Fait avec ❤️ et ☕ à Abidjan | © 2024 Junior Kossivi
</div>

---
