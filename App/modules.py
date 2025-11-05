#Réalisé par: Junior Kossivi le 12/05/2025 à 12:44:23 à Port-Bouet, Abidjan, Côte d'Ivoire, Université Félix Houphouët-Boigny
#Version 2.0
#Description: Ce code contient des fonctions utiles en Python pour effectuer diverses opérations mathématiques, manipuler des tableaux, résoudre des équations, et effectuer des intégrations numériques. 
#Il inclut également des fonctions pour travailler avec des chaînes de caractères et des matrices. 
# Les fonctions sont organisées par catégorie pour une meilleure lisibilité et utilisation.
#En esperant que ce code vous sera utile, n'hésitez pas à l'utiliser et à le modifier selon vos besoins.
#======================================================================================
#Bibliothèque de codes utiles en Python
#======================================================================================
#Importation des bibliothèques nécessaires
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from functools import lru_cache
import re


#Opérations arithmétiques de bases
#======================================================================================


#factoriel recursif
def factorec(n):
    if n == 0 or n==1:
        return 1
    return n*factorec(n-1)

#factoriel itératif
def factoiter(n):
    somme = 1
    for i in range (1,n+1):
        somme *= i
    return somme

#Nombre premier
def nb_premier(n):
    tab=[]
    for i in range(1,n+1):
        if n%i == 0:
            tab.append(i)
    if tab[0] == 1 and tab[1]==n and len(tab)==2:
        return "✅ Ce nombre est Premier"
    else:
        return "❌ Ce nombre est Non premier"

#Calcul du PGCD itératif
def pgcditer(a,b):
    while a!=0:
        a,b = b, a%b
    return a
#Calcul du PGCD récursif
def pgcdrec(a,b):
    if b==0:
        return a
    return pgcdrec(b,a%b)

#Calcul du PPCM
def ppcm(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return (a*b)/pgcdrec(a,b)

#Convertir un nombre décimal en binaire
def decimale_binaire(n):
    if n == 0 :
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimale_binaire(n//2) + str(n%2)

#Somme des carré des n premiers entiers
def sommeCarre(n):
    tab = []
    for i in range(0,n+1):
        tab.append(i**2)
    return tab
        
#Nombre parfait
def nbr_parfait(n):
    par = 0
    for i in range(1,n):
        if n%i == 0 :
            par += i
    if n == par:
        return "✅ Ce nombre est parfait"
    else:
        return "❌ Ce nombre n'est pas parfait"

#Nombre Distinct
def nbr_distinct(n):
    chaine = str(n)
    etat = False
    for lettre in chaine:
        if chaine.count(lettre)>1:
            etat = True
            break
    if etat == True:
        return "✅ Ce nombre n'est pas distinct"
    else:
        return "❌ Ce nombre est distinct"

        
#Calcul de moyenne
def moyenne(n):
    tab = []
    somme =0
    i=0
    while i!=n:
        tab.append(int(input(f"entrez la note {i+1}: ")))
        i+=1
    for j in tab:
        somme +=j
    return somme/n

#Racine de nombre
def racine(a):
    if a>=0:
        return a**(1/2)
    else:
        racine = complex(0, a**(1/2))
        return racine
    
#Calcul de la puissance d'un nombre
def puissance(a,n):
    if n == 0:
        return 1
    elif n>0:
        return a*puissance(a,n-1)
    elif n<0:
        return 1/puissance(a, n)
    

#Calcul de la puissance (puissance rapide)
def puissanceRapide(a,n):
    if n == 0:
        return 1
    if n%2==0:
        return puissanceRapide(a, n//2)**2
    else :
        return a*puissanceRapide(a,n//2)**2
    

#nombre catalans
def catalan(n):
    if n ==0:
        return 1
    else :
        somme= factorec(2*n)//(factorec(n+1)*factorec(n))
        return somme
    

#Combinaison de k dans n
def combinaison(k,n):
    if k>n:
        return "❌ Resultat impossible"
    else:
        return factorec(n)/(factorec(k)*factorec(n-k))
    
#Valeur approché de Pi (Liebniz Gregory)
def liebnizPi(epsilon):
    somme = 0
    i=0
    prec = float('inf')
    while True:
        somme += ((-1)**i)/(2*i+1)
        if abs(prec -somme)<epsilon:
            break
        
        prec = somme
        i+=1
    return 4*somme

#fibonacci
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibo(n-2)+fibo(n-1)

def fibo2(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b  # Mise à jour simultanée
    return b
    

#Fonctions trigonométriques
#======================================================================================
#Cosinus
def cosinus(x,epsilon):
    somme = 0
    i=0
    prec = float('inf')
    while True:
        somme += ((-1)**i)*(x**(2*i))/factorec(2*i)
        if abs(prec -somme)<epsilon:
            break
        
        prec = somme
        i+=1
    return somme

#sinus
def sinus(x,epsilon):
    somme = 0
    i=0
    prec = float('inf')
    while True:
        somme += ((-1)**i)*(x**((2*i)+1))/factorec((2*i)+1)
        if abs(prec -somme)<epsilon:
            break
        
        prec = somme
        i+=1
    return somme


#Opérations sur les tableaux
#======================================================================================

#Générer un tableau de n éléments
def genTab(n):
    tab=[]
    for i in range (0,n):
        print("Entrez l'élément",i+1)
        a=int(input())
        tab.append(a)
    return tab

#Chercher le minimum dans un tableau
def minimumTab(tab):
    mini = tab[0]
    for i in range(0,len(tab)):
        if mini>tab[i]:
            mini = tab[i]
    return mini

#Chercher le maximum dans un tableau
def maximumTab(tab):
    maxi = tab[0]
    for i in range(0,len(tab)):
        if maxi<tab[i]:
            maxi = tab[i]
    return maxi

#Inverser les éléments d'un tableau
def inverseTab(tab):
    return tab[::-1]

#Recherche dichotomique dans un tableau trié
def recherchedicho(a,b,n,tab):
    if a>b:
        return False
    c = int((a+b)/2)
    if n == tab[c]:
        return True
    
    if n>tab[c]:
        return recherchedicho(c+1, b, n, tab)
    else:
        return recherchedicho(a, c-1, n, tab)

#Tri à bulle (Bubble sort) pour trier un tableau
def tribulles(tableau):
    n = len(tableau)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if tableau[j]>tableau[j+1]:
               tableau[j] ,tableau[j+1] = tableau[j+1] , tableau[j]
    return tableau

#Somme des éléments d'un tableau
def sommetab(tab):
    n = len(tab)
    somm = 0
    for i in range(n):
        somm += tab[i]
    return somm


#Moyenne des éléments d'un tableau
def moyennetab(tab):
    n = len(tab)
    return sommetab(tab)/n

#Recherche du plus petit entier absent dans un tab
def plus_ti_n_hors_tab(tab):
    for i in range(minimumTab(tab),maximumTab(tab)+1):
        if i not in tab:
            ok = i
            break
    return ok

#Recherche de Zéro de polynomes
#======================================================================================

#Polnome degré 1
def polynome1(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "⚠️ Les valeurs doivent être numériques"

    if a == 0:
        return "❌ Pas de solution (a ne peut pas être nul)"
    else:
        x = -b / a
        return f"✅ x = {x:.2f}"  # Affiche le résultat avec 2 décimales


#Polnome degré 2
def polynome2(a,b,c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "⚠️ Les valeurs doivent être numériques"
    
    if a == 0:
        if b == 0:
            return "❌ Pas de solution" if c != 0 else "✅ Infinité de solutions"
        else:
            x = -c / b
            return f"✅ Équation de degré 1 : x = {x:.2f}"
    
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b - disc**0.5) / (2*a)
        x2 = (-b + disc**0.5) / (2*a)
        return f"✅ Deux solutions : x₁ = {x1:.2f}, x₂ = {x2:.2f}"
    elif disc == 0:
        x = -b / (2*a)
        return f"✅ Une solution double : x = {x:.2f}"
    else:
            x1 = complex(-b / (2*a), -math.sqrt(-disc) / (2*a))
            x2 = complex(-b / (2*a), +math.sqrt(-disc) / (2*a))
            
            return (
    "❌ Pas de solution réelle (discriminant < 0)\n"
    f"✅ Deux solutions complexes :\n"
    f"x₁ = {x1.real:.2f} {x1.imag:+.2f}i\n"
    f"x₂ = {x2.real:.2f} {x2.imag:+.2f}i"
)

#Polynome3

def polynome3(a, b, c, d):
    """
    Résout l'équation cubique : ax³ + bx² + cx + d = 0
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
    except ValueError:
        return "⚠️ Les valeurs doivent être numériques"
    
    # Cas dégénérés
    if a == 0:
        if b == 0:
            if c == 0:
                return "❌ Pas de solution" if d != 0 else "✅ Infinité de solutions"
            else:
                # Équation de degré 1
                x = -d / c
                return f"✅ Équation de degré 1 : x = {x:.2f}"
        else:
            # Équation de degré 2
            disc = c**2 - 4*b*d
            if disc > 0:
                x1 = (-c - math.sqrt(disc)) / (2*b)
                x2 = (-c + math.sqrt(disc)) / (2*b)
                return f"✅ Équation de degré 2 : x₁ = {x1:.2f}, x₂ = {x2:.2f}"
            elif disc == 0:
                x = -c / (2*b)
                return f"✅ Équation de degré 2 : solution double x = {x:.2f}"
            else:
                x1 = complex(-c / (2*b), -math.sqrt(-disc) / (2*b))
                x2 = complex(-c / (2*b), +math.sqrt(-disc) / (2*b))
                return (
                    "✅ Équation de degré 2 : pas de solution réelle\n"
                    f"Deux solutions complexes :\n"
                    f"x₁ = {x1.real:.2f} {x1.imag:+.2f}i\n"
                    f"x₂ = {x2.real:.2f} {x2.imag:+.2f}i"
                )
    
    # Équation cubique normale
    # Méthode de Cardan
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
    delta = (q/2)**2 + (p/3)**3
    
    if delta > 0:
        # Une racine réelle, deux complexes
        u = (-q/2 + math.sqrt(delta))**(1/3)
        v = (-q/2 - math.sqrt(delta))**(1/3)
        
        x1 = u + v - b/(3*a)
        
        # Racines complexes
        x2 = complex(-(u+v)/2 - b/(3*a), (u-v)*math.sqrt(3)/2)
        x3 = complex(-(u+v)/2 - b/(3*a), -(u-v)*math.sqrt(3)/2)
        
        return (
            f"✅ Une solution réelle et deux complexes :\n"
            f"x₁ = {x1:.2f}\n"
            f"x₂ = {x2.real:.2f} {x2.imag:+.2f}i\n"
            f"x₃ = {x3.real:.2f} {x3.imag:+.2f}i"
        )
    
    elif delta == 0:
        # Trois racines réelles (au moins deux égales)
        if q == 0:
            x = -b/(3*a)
            return f"✅ Trois solutions réelles identiques : x = {x:.2f}"
        else:
            u = (-q/2)**(1/3)
            x1 = 2*u - b/(3*a)
            x2 = -u - b/(3*a)
            return f"✅ Deux solutions réelles : x₁ = {x1:.2f}, x₂ = {x2:.2f} (double)"
    
    else:
        # Trois racines réelles distinctes (cas irréductible)
        r = math.sqrt(-(p/3)**3)
        theta = math.acos(-q/(2*r))
        
        x1 = 2 * math.sqrt(-p/3) * math.cos(theta/3) - b/(3*a)
        x2 = 2 * math.sqrt(-p/3) * math.cos((theta + 2*math.pi)/3) - b/(3*a)
        x3 = 2 * math.sqrt(-p/3) * math.cos((theta + 4*math.pi)/3) - b/(3*a)
        
        # Trier les solutions
        solutions = sorted([x1, x2, x3])
        
        return (
            "✅ Trois solutions réelles distinctes :\n"
            f"x₁ = {solutions[0]:.2f}\n"
            f"x₂ = {solutions[1]:.2f}\n"
            f"x₃ = {solutions[2]:.2f}"
        )


#Opération de base sur les matrices
#======================================================================================

#remplisage une matrice carrée
def remplissagemat(n,m):
    matrice = []
    for i in range (n):
        ligne=[]
        for j in range(m):
            ligne.append(int(input(f"Entrez l'élément de la matrice [{i+1}] [{j+1}]: ")))
        matrice.append(ligne)
    return matrice

#addition de deux matrices carrées
#On suppose que les deux matrices ont la même dimension
def additionmat(matrice1,matrice2,ordre):
    matrice3 = []
    for i in range (ordre):
        ligne=[]
        for j in range(ordre):
            ligne.append(matrice1[i][j]+matrice2[i][j])
        matrice3.append(ligne)
    return matrice3

#Soustraction de deux matrices carrées
#On suppose que les deux matrices ont la même dimension
def soustractionmat(matrice1,matrice2,ordre):
    matrice3 = []
    for i in range (ordre):
        ligne=[]
        for j in range(ordre):
            ligne.append(matrice1[i][j]-matrice2[i][j])
        matrice3.append(ligne)
    return matrice3

#Multiplication de deux matrices carrées

def multiplicationmat(matrice1,matrice2):
    resultat = []

    for _ in range(len(matrice1)):
        ligne = [0] * len(matrice2[0])
        resultat.append(ligne)

    if len(matrice1[0]) != len(matrice2):
        raise ValueError ("Le nombre de ligne doit être égal au nombre de colonne")
    
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            for k in range(len(matrice2)):
                resultat[i][j]+=matrice1[i][k]*matrice2[k][j]
    return resultat
        
        
#Code sur les évenement de la vie
#======================================================================================

#Année bissextile
def bissex(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return "Cette année est une année bissextile"
    else:
        return "Cette année n'est pas une année bissextile"

#Enregistrer une liste de contact (Dictionnaire)
def save_Contact(n) :
    int(input("Entrez le nombre d'éléments de la liste : "))
    contact = []
    for i in range(n):
        index = int(input("l'index : "))
        while index <0 or index>250 :
            index = int(input("l'index doit être entre 0<index<250): "))
            if 0<=index<=250:
                break
        nom = str(input("Nom : "))
        numero = str(input("Numéro : "))
        lonNum = len(numero)
        while lonNum !=8 :
            numero = str(input("Entrez un Numéro à 8 chiffres: "))
            lonNum = len(numero)
            if lonNum == 8:
                break
        contact.append({"Index":index,"Nom": nom, "Numero": numero})
    return contact

#Opération sur les Chaines de caractères
#======================================================================================

#Compter le nombre de voyelles dans une chaine
def compterVoyelles(chaine):
    voyelles = "aeiouyAEIOUY"
    compteur = 0
    for i in chaine:
        if i in voyelles:
           compteur += 1
    return compteur

#Rechercher une lettre dans une chaine
def compterlettre(chaine, lettre):
    i = 0
    for let in chaine:
        if let == lettre:
            i+=1
    return f"Il y'a {i} fois {lettre}"

#Compter le nombre d'apparition d'une lettre dans un mot
def compter_occurrences(chaine, mot):
    # On découpe la chaîne en mots
    mots = chaine.split()
    i = mots.count(mot)
    # On compte le nombre de fois que 'mot' apparaît
    return f"Il y'a {i} fois {mot}"

#Inverser une chaine de caractère
def inversechaine(chaine):
    b = str(chaine)
    return b[::-1]

#Palindrome
def palindrome(chaine):
    # Nettoyage des deux chaînes
    nettoyee = chaine.lower().replace(" ", "").replace(",", "").replace(".", "")
    inverse = nettoyee[::-1]
    
    if inverse == nettoyee:
        return "✅ C'est un palindrome"
    else:
        return "❌ Réessayer, ce n'est pas un palindrome"


#Concatenation
def concachaine(chaine1,chaine2):
    space = " "
    chaine3 = chaine1 + space + chaine2
    return chaine3


#Résolution d'équation non linéaire
#======================================================================================
#Méthode de dichotomie
#On suppose que f est continue sur [a,b] et que f(a)*f(b)<0
#i représente le nombre d'itération1

def racineDichotomie(a,b,epsilon,f):
    i= 0
    if f(a)*f(b)>0:
        raise ValueError(f"❌ pas de racine dans {[a,b]}")
    else :
        while abs(b-a)>epsilon:
            c = (a+b)/2
            if f(a)*f(c)<0:
                i += 1
                b = c
                
            else :
                i += 1
                a = c
        return (c,i)

#Méthode de Newton
#On suppose que f est dérivable sur [a,b]
def racineNewton(f,df,x0,epsilon): 
    i=0
    while abs(f(x0))>epsilon:
        if df(x0) == 0:
            raise ValueError("❌ La dérivée est nulle")
            break
        else:
            x0 = x0 - (f(x0)/df(x0))
            i += 1
    return (x0,i)

#Méthode du point fixe
def racinePointFixe(g,x0,epsilon):
    i = 0

    while abs(g(x0)-x0)>epsilon:
        x0 = g(x0)
        i += 1
    return (x0,i)

def intRectangleRetro(f, a, b, n):
    """Méthode des rectangles rétrograde"""
    h = (b - a) / n
    somme = 0
    for i in range(n):
        somme += f(a + i * h)
    return somme * h

def intRectanglePro(f, a, b, n):
    """Méthode des rectangles progressive"""
    h = (b - a) / n
    somme = 0
    for i in range(1, n + 1):
        somme += f(a + i * h)
    return somme * h

def intRectangleCentre(f, a, b, n):
    """Méthode des rectangles centrée"""
    h = (b - a) / n
    somme = 0
    for i in range(n):
        somme += f(a + i * h + h / 2)
    return somme * h

def intTrapezeC(f, a, b, n):
    """Méthode des trapèzes composite"""
    h = (b - a) / n
    somme = 0
    for i in range(1, n):
        somme += f(a + i * h)
    return (h / 2) * (f(a) + f(b) + 2 * somme)

def intTrapezeS(f, a, b, n):
    """Méthode des trapèzes simple"""
    h = (b - a)
    return (h / 2) * (f(a) + f(b))

def intSimpsonC(f, a, b, n):
    """Méthode de Simpson composite"""
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    somme_pairs = 0
    somme_impairs = 0
    
    for i in range(1, n, 2):
        somme_impairs += f(a + i * h)
    
    for i in range(2, n - 1, 2):
        somme_pairs += f(a + i * h)
    
    return (h / 3) * (f(a) + f(b) + 4 * somme_impairs + 2 * somme_pairs)

def intSimpsonS(f, a, b, n):
    """Méthode de Simpson simple"""
    h = (b - a) / 2
    milieu = (a + b) / 2
    return (h / 3) * (f(a) + 4 * f(milieu) + f(b))

def prepare_expression(expr: str) -> str:
    """Prépare l'expression mathématique pour évaluation"""
    expr = expr.replace(" ", "")
    
    # Valeur absolue
    while "|" in expr:
        debut = expr.find("|")
        fin = expr.find("|", debut + 1)
        if fin == -1:
            expr = expr.replace("|", "", 1)
        else:
            contenu = expr[debut + 1:fin]
            expr = expr[:debut] + f"abs({contenu})" + expr[fin + 1:]
    
    # Multiplication implicite
    expr = re.sub(r"(\d)(π)", r"\1*π", expr)
    expr = re.sub(r"(\d)(√)", r"\1*√", expr)
    expr = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expr)
    
    # Remplacements
    expr = expr.replace("π", "pi")
    expr = expr.replace("√", "sqrt")
    expr = expr.replace("^", "**")
    expr = expr.replace("%", "/100")
    expr = re.sub(r"(\d+)!", r"factorial(\1)", expr)
    
    return expr

def equilibrer_parentheses(expr: str) -> str:
    """Équilibre les parenthèses"""
    ouvert = expr.count("(")
    ferme = expr.count(")")
    manque = ouvert - ferme
    if manque > 0:
        expr += ")" * manque
    return expr


#=============================================================================================================================
"""===============================================Virsualisation des graphes==============================================="""
#=============================================================================================================================


#Affichage polynome de dégré 1
def voir_graphe1(a, b):
    """
    Affiche le graphique de la fonction f(x) = ax + b
    """
    # Conversion sécurisée
    try:
        a_val = float(a)
        b_val = float(b)
    except (ValueError, TypeError) as e:
        print(f"Erreur de conversion : {e}")
        return
    
    # Création des données
    x = np.linspace(-100, 100, 1000)
    y = a_val * x + b_val
    
    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {a_val}x + {b_val}')
    
    # Ajout des axes
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    
    # Configuration
    plt.title(f"Fonction affine : f(x) = {a_val}x + {b_val}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()




#Affichage polynome de dégré 2
def voir_graphe2(a, b, c):
    """
    Affiche le graphique de la fonction f(x) = ax² + bx + c
    """
    # Conversion sécurisée
    try:
        a_val = float(a)
        b_val = float(b)
        c_val = float(c)
    except (ValueError, TypeError) as e:
        print(f"Erreur de conversion : {e}")
        return
    
    # Ajustement dynamique du domaine selon les racines
    discriminant = b_val**2 - 4*a_val*c_val
    
    if a_val != 0 and discriminant >= 0:
        # Si racines réelles, centrer autour des racines
        racine1 = (-b_val - np.sqrt(discriminant)) / (2*a_val)
        racine2 = (-b_val + np.sqrt(discriminant)) / (2*a_val)
        centre = (racine1 + racine2) / 2
        x_min = min(racine1, racine2) - 5
        x_max = max(racine1, racine2) + 5
    else:
        # Sinon domaine par défaut
        centre = 0
        x_min, x_max = -10, 10
    
    x = np.linspace(x_min, x_max, 1000)
    y = a_val * x**2 + b_val * x + c_val
    
    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {a_val}x² + {b_val}x + {c_val}')
    
    # Ajout des axes
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    
    # Marquer les racines si elles existent
    if a_val != 0 and discriminant >= 0:
        plt.scatter([racine1, racine2], [0, 0], color='red', zorder=5, 
                   label=f'Racines: x₁={racine1:.2f}, x₂={racine2:.2f}')
    
    # Marquer le sommet
    sommet_x = -b_val / (2*a_val) if a_val != 0 else 0
    sommet_y = a_val * sommet_x**2 + b_val * sommet_x + c_val
    plt.scatter(sommet_x, sommet_y, color='green', zorder=5, 
               label=f'Sommet: ({sommet_x:.2f}, {sommet_y:.2f})')
    
    # Configuration
    plt.title(f"Fonction du second degré : f(x) = {a_val}x² + {b_val}x + {c_val}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()



#Affichage polynome de dégré 3
def voir_graphe3(a, b, c, d):
    """
    Affiche le graphique de la fonction f(x) = ax³ + bx² + cx + d
    """
    # Conversion sécurisée
    try:
        a_val = float(a)
        b_val = float(b)
        c_val = float(c)
        d_val = float(d)
    except (ValueError, TypeError) as e:
        print(f"Erreur de conversion : {e}")
        return
    
    # Domaine adaptatif centré autour du point d'inflexion
    if a_val != 0:
        centre = -b_val / (3*a_val)  # Point d'inflexion
        x_min, x_max = centre - 8, centre + 8
    else:
        x_min, x_max = -10, 10
    
    x = np.linspace(x_min, x_max, 1000)
    y = a_val * x**3 + b_val * x**2 + c_val * x + d_val
    
    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {a_val}x³ + {b_val}x² + {c_val}x + {d_val}')
    
    # Ajout des axes
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    
    # Configuration
    plt.title(f"Fonction cubique : f(x) = {a_val}x³ + {b_val}x² + {c_val}x + {d_val}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()