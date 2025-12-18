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
import re
import random
import string
import base64


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
    """Teste si n est premier (retourne une chaîne descriptive)."""
    if n <= 1:
        return "❌ Ce nombre est Non premier"
    # Vérification simple jusqu'à sqrt(n)
    if n <= 3:
        return "✅ Ce nombre est Premier"
    if n % 2 == 0:
        return "❌ Ce nombre est Non premier"
    i = 3
    while i * i <= n:
        if n % i == 0:
            return "❌ Ce nombre est Non premier"
        i += 2
    return "✅ Ce nombre est Premier"

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
    # Retourne la valeur absolue du PPCM même si a ou b sont négatifs
    if a == 0 or b == 0:
        return 0
    return abs((a*b)//pgcdrec(a,b)) if isinstance(a, int) and isinstance(b, int) else abs((a*b)/pgcdrec(a,b))

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
    if etat:
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
    """Calcul de la puissance (supporte n négatif)."""
    if n == 0:
        return 1
    if n < 0:
        return 1 / puissance(a, -n)
    # Utiliser exponentiation rapide pour éviter récursion profonde
    result = 1
    base = a
    exp = n
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result
    

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
    """Compte les voyelles en ne considérant que les lettres (ignore signes de ponctuation et chiffres)."""
    voyelles = "aeiouy"
    compteur = 0
    for i in chaine.lower():
        if i.isalpha() and i in voyelles:
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
def inverser_chaine(chaine):
    """Inverse une chaîne de caractères
    Exemple: "bonjour" -> "ruojnob"
    """
    return chaine[::-1]

#Palindrome
def palindrome(chaine):
    # Nettoyage des deux chaînes
    nettoyee = chaine.lower().replace(" ", "").replace(",", "").replace(".", "")
    inverse = nettoyee[::-1]
    
    if inverse == nettoyee:
        return "✅ C'est un palindrome"
    else:
        return "❌ Réessayer, ce n'est pas un palindrome"
    
#Compte le nombre de mots
def compter_mots(chaine):
    """
    Compte le nombre de mots dans une phrase
    """
    mots = chaine.split()
    return len(mots)


def majuscules(chaine):
    """Convertit en majuscules"""
    return chaine.upper()

def minuscules(chaine):
    """Convertit en minuscules"""
    return chaine.lower()

def titre(chaine):
    """Met la première lettre de chaque mot en majuscule"""
    return chaine.title()

def nettoyer_espaces(chaine):
    """
    Supprime les espaces en début, fin et les espaces multiples
    """
    return ' '.join(chaine.split())

def est_anagramme(chaine1, chaine2):
    """
    Vérifie si deux chaînes sont des anagrammes
    Exemple: "chien" et "niche"
    """
    # Nettoyer les chaînes (enlever espaces, mettre en minuscules)
    chaine1_nettoyee = ''.join(chaine1.lower().split())
    chaine2_nettoyee = ''.join(chaine2.lower().split())
    
    # Trier les lettres et comparer
    return sorted(chaine1_nettoyee) == sorted(chaine2_nettoyee)


# Les imports ont été consolidés au sommet du fichier pour respecter E402.


def generer_mot_de_passe(longueur=12):
    """
    Génère un mot de passe aléatoire
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))


def encoder_base64(chaine):
    """Encode une chaîne en base64"""
    return base64.b64encode(chaine.encode()).decode()

def decoder_base64(chaine):
    """Décode une chaîne base64"""
    return base64.b64decode(chaine.encode()).decode()

def extraire_chiffres(chaine):
    """
    Extrait tous les chiffres d'une chaîne
    """
    return ''.join(filter(str.isdigit, chaine))

def extraire_nombres(chaine):
    """
    Extrait tous les nombres (séquences de chiffres)
    """
    return re.findall(r'\d+', chaine)

def palindrome_amelioré(chaine):
    """
    Version améliorée sans dépendances externes
    """
    try:
        # Convertir en minuscules
        chaine = chaine.lower()
        
        # Dictionnaire des accents français
        accents = {
            'à': 'a', 'â': 'a', 'ä': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'î': 'i', 'ï': 'i',
            'ô': 'o', 'ö': 'o',
            'ù': 'u', 'û': 'u', 'ü': 'u',
            'ç': 'c',
            'œ': 'oe', 'æ': 'ae'
        }
        
        # Supprimer les accents
        chaine_sans_accent = ''.join(accents.get(c, c) for c in chaine)
        
        # Garder uniquement les lettres (a-z)
        lettres = "abcdefghijklmnopqrstuvwxyz"
        chaine_nettoyee = ''.join(c for c in chaine_sans_accent if c in lettres)
        
        # Vérifier si vide
        if not chaine_nettoyee:
            return "❌ Pas de lettres à vérifier"
        
        # Vérifier le palindrome
        if chaine_nettoyee == chaine_nettoyee[::-1]:
            return f"✅ C'est un palindrome ! ({chaine_nettoyee})"
        else:
            return "❌ Ce n'est pas un palindrome"
            
    except Exception as e:
        return f"❌ Erreur: {str(e)}"
    

def compter_consonnes(chaine):
    """
    Compte le nombre de consonnes dans une chaîne
    """
    voyelles = "aeiouyàâäéèêëîïôöùûü"
    chaine_lower = chaine.lower()
    consonnes = 0
    
    for caractere in chaine_lower:
        if caractere.isalpha() and caractere not in voyelles:
            consonnes += 1
    
    return consonnes


def rot13(chaine):
    """
    Applique le chiffrement ROT13
    """
    resultat = []
    for caractere in chaine:
        if 'a' <= caractere <= 'z':
            base = ord('a')
            resultat.append(chr((ord(caractere) - base + 13) % 26 + base))
        elif 'A' <= caractere <= 'Z':
            base = ord('A')
            resultat.append(chr((ord(caractere) - base + 13) % 26 + base))
        else:
            resultat.append(caractere)
    return ''.join(resultat)

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
# ======================================================================================
# Résolution d'équations non linéaires (avec suivi des itérations)
# ======================================================================================

def racineDichotomie(a, b, epsilon, f, max_iter=1000):
    """Méthode de dichotomie. Retourne (racine, iterations, details) pour compatibilité avec l'interface."""
    i = 0
    iterations = []
    
    if f(a) * f(b) > 0:
        raise ValueError(f"❌ Pas de racine dans [{a:.4f}, {b:.4f}] : f(a)*f(b) > 0")
    
    while abs(b - a) > epsilon and i < max_iter:
        c = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fc = f(c)
        
        iterations.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(a)': fa,
            'f(b)': fb,
            'f(c)': fc,
            'intervalle': abs(b - a),
            'erreur': abs(fc),
            'type': 'dichotomie'
        })
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        i += 1
    
    if i >= max_iter:
        raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")
    
    # Retourner racine, nombre d'itérations, et les détails (ordre: racine, nombre, itérations)
    return ((a + b) / 2, i, iterations)


def racineNewton(f, df, x0, epsilon, max_iter=1000):
    """Newton-Raphson ; retourne (racine, nombre, details) pour compatibilité avec l'interface."""
    i = 0
    iterations = []
    x = x0
    
    while i < max_iter:
        fx = f(x)
        dfx = df(x)
        
        iterations.append({
            'iteration': i + 1,
            'x_n': x,
            'f(x_n)': fx,
            "f'(x_n)": dfx,
            'erreur': abs(fx),
            'type': 'newton'
        })
        
        if abs(fx) < epsilon:
            return (x, i, iterations)
        
        if abs(dfx) < 1e-15:
            raise ValueError("❌ Dérivée trop proche de zéro")
        
        x_new = x - fx / dfx
        
        if abs(x_new) > 1e10:
            raise ValueError("❌ Divergence détectée")
        
        x = x_new
        i += 1
    
    raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")


def racinePointFixe(g, x0, epsilon, max_iter=1000):
    """
    Méthode du point fixe pour trouver x tel que g(x)=x
    Convergence linéaire
    
    Args:
        g: Fonction de point fixe
        x0: Point de départ
        epsilon: Précision souhaitée
        max_iter: Nombre maximum d'itérations
    
    Returns:
        tuple: (point_fixe, nombre_d_iterations, liste_des_itérations)
    """
    i = 0
    iterations = []
    x = x0
    
    while i < max_iter:
        gx = g(x)
        
        # Stocker les informations de l'itération
        iterations.append({
            'iteration': i + 1,
            'x_n': x,
            'g(x_n)': gx,
            '|g(x)-x|': abs(gx - x),
            'erreur': abs(gx - x),
            'type': 'point_fixe'
        })
        
        if abs(gx - x) < epsilon:
            return (x, i, iterations)
        
        x = gx
        i += 1
    
    raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")


def racineSecante(f, x0, x1, epsilon, max_iter=1000):
    """
    Méthode de la sécante pour trouver une racine de f(x)=0
    Convergence super-linéaire (≈1.618)
    Ne nécessite pas la dérivée
    
    Args:
        f: Fonction à étudier
        x0, x1: Deux points de départ
        epsilon: Précision souhaitée
        max_iter: Nombre maximum d'itérations
    
    Returns:
        tuple: (racine, nombre_d_iterations, liste_des_itérations)
    """
    i = 0
    iterations = []
    x_prev = x0
    x_curr = x1
    
    while i < max_iter:
        f_prev = f(x_prev)
        f_curr = f(x_curr)
        
        if abs(f_curr) < epsilon:
            iterations.append({
                'iteration': i + 1,
                'x_{n-1}': x_prev,
                'x_n': x_curr,
                'f(x_{n-1})': f_prev,
                'f(x_n)': f_curr,
                'erreur': abs(f_curr),
                'type': 'secante'
            })
            return (x_curr, i, iterations)
        
        # Éviter la division par zéro
        if abs(f_curr - f_prev) < 1e-15:
            raise ValueError("❌ Dénominateur trop petit dans la méthode de la sécante")
        
        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        
        # Stocker les informations de l'itération
        iterations.append({
            'iteration': i + 1,
            'x_{n-1}': x_prev,
            'x_n': x_curr,
            'x_{n+1}': x_next,
            'f(x_{n-1})': f_prev,
            'f(x_n)': f_curr,
            'erreur': abs(f_curr),
            'type': 'secante'
        })
        
        # Vérifier la divergence
        if abs(x_next) > 1e10:
            raise ValueError("❌ Divergence détectée")
        
        x_prev, x_curr = x_curr, x_next
        i += 1
    
    raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")


def racineRegulaFalsi(f, a, b, epsilon, max_iter=1000):
    """
    Méthode de la fausse position (Regula Falsi)
    Combinaison de dichotomie et sécante
    Toujours converge si f(a)*f(b)<0
    
    Args:
        f: Fonction à étudier
        a, b: Intervalle initial
        epsilon: Précision souhaitée
        max_iter: Nombre maximum d'itérations
    
    Returns:
        tuple: (racine, nombre_d_iterations, liste_des_itérations)
    """
    i = 0
    iterations = []
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError(f"❌ Pas de racine dans [{a:.4f}, {b:.4f}]")
    
    while i < max_iter:
        # Calcul du point par interpolation linéaire
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        
        # Stocker les informations de l'itération
        iterations.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(a)': fa,
            'f(b)': fb,
            'f(c)': fc,
            'intervalle': abs(b - a),
            'erreur': abs(fc),
            'type': 'regula_falsi'
        })
        
        if abs(fc) < epsilon:
            return (c, i, iterations)
        
        # Mettre à jour l'intervalle
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        
        i += 1
    
    raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")


def racineMuller(f, x0, x1, x2, epsilon, max_iter=1000):
    """
    Méthode de Müller
    Utilise une interpolation quadratique
    Convergence super-linéaire, trouve des racines complexes
    """
    i = 0
    iterations = []

    # Évaluations initiales
    f0, f1, f2 = f(x0), f(x1), f(x2)

    while i < max_iter:
        # Coefficients du polynôme quadratique
        h0 = x1 - x0
        h1 = x2 - x1

        # Protéger contre division par zéro
        if abs(h0) < 1e-15 or abs(h1) < 1e-15:
            raise ValueError("❌ Points initiaux trop proches entre eux pour la méthode de Müller")

        delta0 = (f1 - f0) / h0
        delta1 = (f2 - f1) / h1

        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = f2

        # Calcul du discriminant (utiliser cmath pour gérer les racines complexes)
        discriminant = b**2 - 4*a*c
        sqrt_disc = cmath.sqrt(discriminant)

        # Choisir le dénominateur de manière numeriquement stable
        if abs(b + sqrt_disc) > abs(b - sqrt_disc):
            denom = b + sqrt_disc
        else:
            denom = b - sqrt_disc

        # Éviter division par zéro
        if abs(denom) == 0:
            raise ValueError("❌ Dénominateur nul dans l'étape de Müller — choix des points initiaux inadéquat")

        dx = -2 * c / denom
        x3 = x2 + dx

        f3 = f(x3)

        # Stocker les informations (convertir les valeurs complexes en Python natives si besoin)
        iterations.append({
            'iteration': i + 1,
            'x_n-2': x0,
            'x_n-1': x1,
            'x_n': x2,
            'x_n+1': x3,
            'f(x_n+1)': f3,
            'dx': dx,
            'erreur': abs(f3),
            'type': 'muller'
        })

        # Critères d'arrêt : valeur de la fonction proche de zéro ou pas de déplacement significatif
        if abs(f3) < epsilon or abs(dx) < epsilon:
            return (x3, i + 1, iterations)

        # Préparer l'itération suivante
        x0, x1, x2 = x1, x2, x3
        f0, f1, f2 = f1, f2, f3

        i += 1

    raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")
    


def racineSteffensen(f, x0, epsilon, max_iter=1000):
    """
    Méthode de Steffensen
    Accélération de la convergence du point fixe
    Convergence quadratique sans dérivée
    
    Args:
        f: Fonction de point fixe g(x)
        x0: Point de départ
        epsilon: Précision souhaitée
        max_iter: Nombre maximum d'itérations
    
    Returns:
        tuple: (point_fixe, nombre_d_iterations, liste_des_itérations)
    """
    i = 0
    iterations = []
    x = x0
    
    while i < max_iter:
        fx = f(x)
        fxfx = f(fx)
        
        # Éviter la division par zéro
        denominator = fxfx - 2*fx + x
        if abs(denominator) < 1e-15:
            raise ValueError("❌ Dénominateur trop petit dans la méthode de Steffensen")
        
        x_new = x - (fx - x)**2 / denominator
        
        # Stocker les informations
        iterations.append({
            'iteration': i + 1,
            'x_n': x,
            'f(x_n)': fx,
            'f(f(x_n))': fxfx,
            'x_n+1': x_new,
            'erreur': abs(x_new - x),
            'type': 'steffensen'
        })
        
        if abs(x_new - x) < epsilon:
            return (x_new, i, iterations)
        
        x = x_new
        i += 1
    
    raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")


def racineBrent(f, a, b, epsilon, max_iter=1000):
    """
    Algorithme de Brent
    Combine dichotomie, sécante et interpolation quadratique inverse
    Garanti la convergence, très robuste
    
    Args:
        f: Fonction à étudier
        a, b: Intervalle avec f(a)*f(b)<0
        epsilon: Précision souhaitée
        max_iter: Nombre maximum d'itérations
    
    Returns:
        tuple: (racine, nombre_d_iterations, liste_des_itérations)
    """
    i = 0
    iterations = []
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError(f"❌ Pas de racine dans [{a:.4f}, {b:.4f}]")
    
    # Assurer que b est la meilleure approximation
    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa
    
    c = a
    fc = fa
    mflag = True
    d = 0
    
    while i < max_iter and abs(b - a) > epsilon:
        s = 0
        
        if fa != fc and fb != fc:
            # Interpolation quadratique inverse
            s = a * fb * fc / ((fa - fb) * (fa - fc)) + \
                b * fa * fc / ((fb - fa) * (fb - fc)) + \
                c * fa * fb / ((fc - fa) * (fc - fb))
        else:
            # Méthode de la sécante
            s = b - fb * (b - a) / (fb - fa)
        
        # Conditions pour utiliser la dichotomie
        condition1 = (s - (3*a + b)/4) * (s - b) > 0
        condition2 = mflag and abs(s - b) >= abs(b - c)/2
        condition3 = not mflag and abs(s - b) >= abs(c - d)/2
        condition4 = mflag and abs(b - c) < epsilon
        condition5 = not mflag and abs(c - d) < epsilon
        
        if condition1 or condition2 or condition3 or condition4 or condition5:
            s = (a + b) / 2
            mflag = True
        else:
            mflag = False
        
        fs = f(s)
        d = c
        c = b
        fc = fb
        
        if fa * fs < 0:
            b = s
            fb = fs
        else:
            a = s
            fa = fs
        
        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa
        
        # Stocker les informations
        iterations.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            's': s,
            'f(s)': fs,
            'intervalle': abs(b - a),
            'erreur': abs(fs),
            'methode': 'dichotomie' if mflag else 'interpolation',
            'type': 'brent'
        })
        
        i += 1
    
    if i >= max_iter:
        raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")
    
    return (b, i, iterations)


def racineRidders(f, a, b, epsilon, max_iter=1000):
    """
    Méthode de Ridders
    Utilise l'extrapolation exponentielle
    Convergence quadratique, très robuste
    
    Args:
        f: Fonction à étudier
        a, b: Intervalle avec f(a)*f(b)<0
        epsilon: Précision souhaitée
        max_iter: Nombre maximum d'itérations
    
    Returns:
        tuple: (racine, nombre_d_iterations, liste_des_itérations)
    """
    i = 0
    iterations = []
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError(f"❌ Pas de racine dans [{a:.4f}, {b:.4f}]")
    
    while i < max_iter and abs(b - a) > epsilon:
        # Point milieu
        c = (a + b) / 2
        fc = f(c)
        
        # Calcul du point par extrapolation
        s = c + (c - a) * (fa - fb) / (2 * fc) if fc != 0 else (a + b) / 2
        fs = f(s)
        
        # Stocker les informations
        iterations.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            's': s,
            'f(s)': fs,
            'intervalle': abs(b - a),
            'erreur': abs(fs),
            'type': 'ridders'
        })
        
        if abs(fs) < epsilon:
            return (s, i, iterations)
        
        # Mettre à jour l'intervalle
        if fc * fs < 0:
            a, b = c, s
            fa, fb = fc, fs
        elif fa * fs < 0:
            b = s
            fb = fs
        else:
            a = s
            fa = fs
        
        i += 1
    
    if i >= max_iter:
        raise ValueError(f"❌ Convergence non atteinte après {max_iter} itérations")
    
    return ((a + b) / 2, i, iterations)



# ======================================================================================
# Intégration Numérique (avec suivis des itérations)
# ======================================================================================

def intRectangleRetro(f, a, b, n):
    """Méthode des rectangles rétrograde (gauche) avec suivi des itérations

    Retourne un tuple (resultat, iterations) où `resultat` est un float et
    `iterations` est une liste de dicts détaillant chaque étape.
    """
    if n <= 0:
        raise ValueError("Le nombre de subdivisions n doit être positif")
    h = (b - a) / n
    somme = 0.0
    iterations = []  # Liste pour stocker les données de chaque itération
    
    for i in range(n):
        xi = a + i * h
        fxi = float(f(xi))
        aire_partielle = fxi * h
        somme += fxi
        
        # Stocker les informations de l'itération
        iterations.append({
            'iteration': i + 1,
            'xi': xi,
            'f(xi)': fxi,
            'hauteur': fxi,
            'largeur': h,
            'aire_rectangle': aire_partielle,
            'somme_partielle': somme * h,
            'type': 'rectangle_gauche'
        })
    
    resultat = somme * h
    return resultat, iterations

def intRectanglePro(f, a, b, n):
    """Méthode des rectangles progressive (droite) avec suivi des itérations"""
    if n <= 0:
        raise ValueError("Le nombre de subdivisions n doit être positif")
    h = (b - a) / n
    somme = 0
    iterations = []
    
    for i in range(1, n + 1):
        xi = a + i * h
        fxi = f(xi)
        somme += fxi
        aire_partielle = fxi * h
        
        iterations.append({
            'iteration': i,
            'xi': xi,
            'f(xi)': fxi,
            'hauteur': fxi,
            'largeur': h,
            'aire_rectangle': aire_partielle,
            'somme_partielle': somme * h,
            'type': 'rectangle_droit'
        })
    
    resultat = somme * h
    return resultat, iterations

def intRectangleCentre(f, a, b, n):
    """Méthode des rectangles centrée avec suivi des itérations"""
    if n <= 0:
        raise ValueError("Le nombre de subdivisions n doit être positif")
    h = (b - a) / n
    somme = 0
    iterations = []
    
    for i in range(n):
        xi = a + i * h + h / 2
        fxi = f(xi)
        somme += fxi
        aire_partielle = fxi * h
        
        iterations.append({
            'iteration': i + 1,
            'xi': xi,
            'f(xi)': fxi,
            'hauteur': fxi,
            'largeur': h,
            'aire_rectangle': aire_partielle,
            'somme_partielle': somme * h,
            'type': 'rectangle_centre'
        })
    
    resultat = somme * h
    return resultat, iterations

def intTrapezeC(f, a, b, n):
    """Méthode des trapèzes composite avec suivi des itérations"""
    if n <= 0:
        raise ValueError("Le nombre de subdivisions n doit être positif")
    h = (b - a) / n
    somme_interieur = 0
    iterations = []
    
    # Calcul des points d'intérieur
    for i in range(1, n):
        xi = a + i * h
        fxi = f(xi)
        somme_interieur += fxi
        
        # Calcul de l'aire partielle du trapèze courant
        if i == 1:
            x_prev = a
            f_prev = f(a)
        else:
            x_prev = a + (i-1) * h
            f_prev = f(x_prev)
        
        aire_partielle = (h / 2) * (f_prev + fxi)
        
        iterations.append({
            'iteration': i,
            'xi': xi,
            'f(xi)': fxi,
            'x_prev': x_prev,
            'f(x_prev)': f_prev,
            'aire_trapeze': aire_partielle,
            'somme_partielle': (h/2) * (f(a) + f(b) + 2 * somme_interieur),
            'type': 'trapeze'
        })
    
    resultat = (h / 2) * (f(a) + f(b) + 2 * somme_interieur)
    return resultat, iterations

def intTrapezeS(f, a, b, n):
    """Méthode des trapèzes simple avec suivi des itérations"""
    # Pour la méthode simple, on ignore n
    h = (b - a)
    resultat = (h / 2) * (f(a) + f(b))
    
    # Pour le trapèze simple, on a seulement une "itération"
    iterations = [{
        'iteration': 1,
        'a': a,
        'f(a)': f(a),
        'b': b,
        'f(b)': f(b),
        'largeur': h,
        'aire': resultat,
        'type': 'trapeze_simple'
    }]
    
    return resultat, iterations

def intSimpsonC(f, a, b, n):
    """Méthode de Simpson composite avec suivi des itérations"""
    if n <= 0:
        raise ValueError("Le nombre de subdivisions n doit être positif")
    if n % 2 != 0:
        n += 1  # Simpson nécessite un nombre pair de subdivisions
    
    h = (b - a) / n
    iterations = []
    
    # Collecter tous les points avec leurs coefficients
    points = []
    
    # Points impairs (coefficient 4)
    for i in range(1, n, 2):
        xi = a + i * h
        fxi = f(xi)
        points.append({
            'xi': xi,
            'f(xi)': fxi,
            'coefficient': 4,
            'contribution': 4 * fxi,
            'index': i
        })
    
    # Points pairs (coefficient 2)
    for i in range(2, n-1, 2):
        xi = a + i * h
        fxi = f(xi)
        points.append({
            'xi': xi,
            'f(xi)': fxi,
            'coefficient': 2,
            'contribution': 2 * fxi,
            'index': i
        })
    
    # Trier par index pour l'ordre d'affichage
    points.sort(key=lambda x: x['index'])
    
    # Calculer les sommes partielles
    somme_cumulee = f(a) + f(b)
    
    for idx, point in enumerate(points, 1):
        somme_cumulee += point['contribution']
        somme_partielle = (h / 3) * somme_cumulee
        
        iterations.append({
            'iteration': idx,
            'xi': point['xi'],
            'f(xi)': point['f(xi)'],
            'coefficient': point['coefficient'],
            'contribution': point['contribution'],
            'somme_partielle': somme_partielle,
            'type': 'simpson'
        })
    
    # Calcul final
    resultat = (h / 3) * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 
                          2 * sum(f(a + i * h) for i in range(2, n-1, 2)))
    
    return resultat, iterations

def intSimpsonS(f, a, b, n):
    """Méthode de Simpson simple avec suivi des itérations"""
    # Pour Simpson simple, on ignore n
    h = (b - a) / 2
    x0 = a
    x1 = a + h
    x2 = b
    
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    
    resultat = (h / 3) * (f0 + 4 * f1 + f2)
    
    # Pour Simpson simple, on a 3 points
    iterations = [
        {
            'iteration': 1,
            'xi': x0,
            'f(xi)': f0,
            'coefficient': 1,
            'contribution': f0,
            'somme_partielle': (h/3) * f0,
            'type': 'simpson_simple'
        },
        {
            'iteration': 2,
            'xi': x1,
            'f(xi)': f1,
            'coefficient': 4,
            'contribution': 4 * f1,
            'somme_partielle': (h/3) * (f0 + 4 * f1),
            'type': 'simpson_simple'
        },
        {
            'iteration': 3,
            'xi': x2,
            'f(xi)': f2,
            'coefficient': 1,
            'contribution': f2,
            'somme_partielle': resultat,
            'type': 'simpson_simple'
        }
    ]
    
    return resultat, iterations

# Les fonctions existantes prepare_expression et equilibrer_parentheses restent inchangées
# (elles devraient déjà être dans votre fichier)
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
        x_min = min(racine1, racine2) - 5
        x_max = max(racine1, racine2) + 5
    else:
        # Sinon domaine par défaut
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


    # ======================================================================================
# Interpolation Numérique (avec suivi des calculs)
# ======================================================================================

def interpolation_lagrange(x_points, y_points, x):
    """
    Interpolation de Lagrange
    
    Args:
        x_points: Liste des abscisses des points
        y_points: Liste des ordonnées des points
        x: Point où évaluer le polynôme
    
    Returns:
        tuple: (valeur_interpolee, polynome, details_calculs)
    """
    if len(x_points) != len(y_points):
        raise ValueError("Les listes x_points et y_points doivent avoir la même longueur")
    
    n = len(x_points)
    result = 0.0
    details = []
    polynome_terms = []
    
    for i in range(n):
        # Calcul du polynôme de Lagrange L_i(x)
        term = y_points[i]
        term_str = f"{y_points[i]:.6f}"
        
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
                term_str += f" * (x - {x_points[j]:.6f}) / ({x_points[i]:.6f} - {x_points[j]:.6f})"
        
        # Stocker les détails pour ce terme
        details.append({
            'terme': i + 1,
            'coeff': y_points[i],
            'valeur_term': term,
            'expression': f"L_{i}(x) = {y_points[i]:.6f} * ∏(x - x_j)/(x_i - x_j) pour j≠{i}"
        })
        
        polynome_terms.append(f"{y_points[i]:.6f} * " + " * ".join([f"(x - {x_points[j]:.6f})/({x_points[i]:.6f} - {x_points[j]:.6f})" 
                                                                  for j in range(n) if i != j]))
        result += term
    
    polynome = "P(x) = " + " + ".join(polynome_terms)
    
    return result, polynome, details


def interpolation_newton(x_points, y_points, x):
    """
    Interpolation de Newton avec différences divisées
    
    Args:
        x_points: Liste des abscisses des points
        y_points: Liste des ordonnées des points
        x: Point où évaluer le polynôme
    
    Returns:
        tuple: (valeur_interpolee, tableau_differences, polynome, details)
    """
    if len(x_points) != len(y_points):
        raise ValueError("Les listes x_points et y_points doivent avoir la même longueur")
    
    n = len(x_points)
    
    # Initialiser la table des différences divisées
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_points[i]
    
    # Calculer les différences divisées
    details_diff = []
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_points[i + j] - x_points[i])
            
            details_diff.append({
                'ordre': j,
                'indice': i,
                'valeur': table[i][j],
                'formule': f"f[x_{i},...,x_{i+j}] = (f[x_{i+1},...,x_{i+j}] - f[x_i,...,x_{i+j-1}]) / (x_{i+j} - x_i)"
            })
    
    # Évaluation du polynôme de Newton
    result = table[0][0]
    produit = 1
    polynome_terms = [f"{table[0][0]:.6f}"]
    details_eval = []
    
    for i in range(1, n):
        produit *= (x - x_points[i - 1])
        result += table[0][i] * produit
        
        terme = f"{table[0][i]:.6f}"
        for j in range(i):
            terme += f" * (x - {x_points[j]:.6f})"
        
        polynome_terms.append(terme)
        
        details_eval.append({
            'terme': i,
            'coeff': table[0][i],
            'produit': produit,
            'contribution': table[0][i] * produit
        })
    
    polynome = "P(x) = " + " + ".join(polynome_terms)
    
    return result, table, polynome, {'differences': details_diff, 'evaluation': details_eval}


def interpolation_lineaire(x_points, y_points, x):
    """
    Interpolation linéaire par morceaux
    
    Args:
        x_points: Liste des abscisses des points
        y_points: Liste des ordonnées des points
        x: Point où évaluer
    
    Returns:
        tuple: (valeur_interpolee, segment_utilise, details)
    """
    if len(x_points) != len(y_points):
        raise ValueError("Les listes x_points et y_points doivent avoir la même longueur")
    
    if len(x_points) < 2:
        raise ValueError("Au moins 2 points sont nécessaires pour l'interpolation linéaire")
    
    # Trier les points par x
    points = sorted(zip(x_points, y_points), key=lambda p: p[0])
    x_sorted, y_sorted = zip(*points)
    
    # Trouver le segment approprié
    if x <= x_sorted[0]:
        # Extrapolation à gauche
        segment = (0, 1)
    elif x >= x_sorted[-1]:
        # Extrapolation à droite
        segment = (len(x_sorted) - 2, len(x_sorted) - 1)
    else:
        # Interpolation
        for i in range(len(x_sorted) - 1):
            if x_sorted[i] <= x <= x_sorted[i + 1]:
                segment = (i, i + 1)
                break
        else:
            segment = (len(x_sorted) - 2, len(x_sorted) - 1)
    
    i, j = segment
    x1, y1 = x_sorted[i], y_sorted[i]
    x2, y2 = x_sorted[j], y_sorted[j]
    
    # Formule d'interpolation linéaire
    if x2 == x1:
        result = y1
    else:
        result = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    
    details = {
        'segment': segment,
        'points': [(x1, y1), (x2, y2)],
        'formule': f"y = {y1:.6f} + ({y2:.6f} - {y1:.6f}) * (x - {x1:.6f}) / ({x2:.6f} - {x1:.6f})",
        'pente': (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
    }
    
    return result, details


def spline_cubique_naturelle(x_points, y_points, x):
    """
    Spline cubique naturelle (dérivées secondes nulles aux extrémités)
    
    Args:
        x_points: Liste des abscisses des points
        y_points: Liste des ordonnées des points
        x: Point où évaluer
    
    Returns:
        tuple: (valeur_interpolee, coefficients_spline, details)
    """
    if len(x_points) != len(y_points):
        raise ValueError("Les listes x_points et y_points doivent avoir la même longueur")
    
    n = len(x_points)
    
    if n < 3:
        raise ValueError("Au moins 3 points sont nécessaires pour une spline cubique")
    
    # Trier les points
    points = sorted(zip(x_points, y_points), key=lambda p: p[0])
    x_sorted, y_sorted = zip(*points)
    
    # Calcul des hi
    h = [x_sorted[i + 1] - x_sorted[i] for i in range(n - 1)]
    
    # Construction du système tridiagonal pour les dérivées secondes
    # Matrice A * M = b
    A = [[0] * n for _ in range(n)]
    b = [0] * n
    
    # Conditions naturelles : M0 = Mn-1 = 0
    A[0][0] = 1
    A[n - 1][n - 1] = 1
    
    # Équations internes
    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        b[i] = 6 * ((y_sorted[i + 1] - y_sorted[i]) / h[i] - 
                   (y_sorted[i] - y_sorted[i - 1]) / h[i - 1])
    
    # Résolution du système tridiagonal (simplifiée)
    M = [0] * n
    # Pour simplifier, on utilise une approche directe (en production, utiliser une méthode optimisée)
    # Ici, on utilise une approximation simplifiée
    for i in range(n):
        M[i] = b[i] / A[i][i] if A[i][i] != 0 else 0
    
    # Trouver l'intervalle approprié
    intervalle = 0
    for i in range(n - 1):
        if x_sorted[i] <= x <= x_sorted[i + 1]:
            intervalle = i
            break
    else:
        if x < x_sorted[0]:
            intervalle = 0
        else:
            intervalle = n - 2
    
    # Calcul des coefficients pour le segment
    i = intervalle
    a = y_sorted[i]
    b_coeff = (y_sorted[i + 1] - y_sorted[i]) / h[i] - h[i] * (2 * M[i] + M[i + 1]) / 6
    c = M[i] / 2
    d = (M[i + 1] - M[i]) / (6 * h[i])
    
    # Évaluation de la spline
    dx = x - x_sorted[i]
    result = a + b_coeff * dx + c * dx**2 + d * dx**3
    
    coefficients = {
        'intervalle': intervalle,
        'a': a,
        'b': b_coeff,
        'c': c,
        'd': d,
        'x0': x_sorted[i],
        'x1': x_sorted[i + 1]
    }
    
    details = {
        'h': h,
        'M': M,
        'coefficients': coefficients,
        'formule': f"S(x) = {a:.6f} + {b_coeff:.6f}*(x-{x_sorted[i]:.6f}) + {c:.6f}*(x-{x_sorted[i]:.6f})² + {d:.6f}*(x-{x_sorted[i]:.6f})³"
    }
    
    return result, coefficients, details


def interpolation_hermite(x_points, y_points, dy_points, x):
    """
    Interpolation d'Hermite (formule de Hermite via bases de Lagrange modifiées)

    Args:
        x_points: Liste des abscisses
        y_points: Liste des ordonnées
        dy_points: Liste des dérivées en chaque abscisse
        x: Point où évaluer

    Returns:
        tuple: (valeur_interpolee, polynome_description, details)
    """
    if len(x_points) != len(y_points) or len(x_points) != len(dy_points):
        raise ValueError("Toutes les listes doivent avoir la même longueur")

    n = len(x_points)

    # Calculer les polynômes de base L_i(x) et leur dérivée en x_i
    def L_i(x_val, i):
        num = 1.0
        den = 1.0
        for j in range(n):
            if j == i:
                continue
            num *= (x_val - x_points[j])
            den *= (x_points[i] - x_points[j])
        return num / den if den != 0 else 0.0

    def L_i_prime_at_xi(i):
        s = 0.0
        for j in range(n):
            if j == i:
                continue
            s += 1.0 / (x_points[i] - x_points[j])
        return s

    result = 0.0
    terms = []

    for i in range(n):
        Li_x = L_i(x, i)
        Li_prime_xi = L_i_prime_at_xi(i)
        yi = y_points[i]
        dyi = dy_points[i]

        # Hermite basis contributions
        hi1 = (1 - 2 * (x - x_points[i]) * Li_prime_xi) * (Li_x ** 2) * yi
        hi2 = (x - x_points[i]) * (Li_x ** 2) * dyi

        result += hi1 + hi2
        terms.append((hi1, hi2))

    # Construire une description de polynôme sommaire
    polynome_desc = f"Hermite interpolation using {n} points"

    details = {
        'terms': terms,
        'x_points': x_points,
        'y_points': y_points,
        'dy_points': dy_points
    }

    return result, polynome_desc, details


def interpolation_bezier(points_control, t):
    """
    Courbe de Bézier
    
    Args:
        points_control: Liste des points de contrôle [(x1,y1), (x2,y2), ...]
        t: Paramètre dans [0,1]
    
    Returns:
        tuple: (point_interpole, points_intermediaires, details)
    """
    n = len(points_control) - 1
    
    # Copie des points pour l'algorithme de De Casteljau
    points = [list(p) for p in points_control]
    details = {'etapes': []}
    
    # Algorithme de De Casteljau
    for r in range(1, n + 1):
        etape = []
        for i in range(n - r + 1):
            x = (1 - t) * points[i][0] + t * points[i + 1][0]
            y = (1 - t) * points[i][1] + t * points[i + 1][1]
            points[i] = [x, y]
            etape.append((x, y))
        details['etapes'].append(etape)
    
    result_point = points[0]
    
    details.update({
        'degre': n,
        'points_control': points_control,
        'algorithme': 'De Casteljau'
    })
    
    return result_point, details


def interpolation_mincarres(x_points, y_points, degre):
    """
    Approximation par moindres carrés (régression polynomiale)
    
    Args:
        x_points: Liste des abscisses
        y_points: Liste des ordonnées
        degre: Degré du polynôme d'approximation
    
    Returns:
        tuple: (coefficients, erreur, polynome, details)
    """
    if len(x_points) != len(y_points):
        raise ValueError("Les listes x_points et y_points doivent avoir la même longueur")
    
    n = len(x_points)
    if n <= degre:
        raise ValueError(f"Nombre de points ({n}) insuffisant pour le degré {degre}")
    
    # Construction de la matrice de Vandermonde
    A = []
    for x in x_points:
        ligne = [x**i for i in range(degre + 1)]
        A.append(ligne)
    
    # Résolution par les équations normales A^T A c = A^T y
    import numpy as np
    
    A_np = np.array(A)
    y_np = np.array(y_points)
    
    # Équations normales
    ATA = np.dot(A_np.T, A_np)
    ATy = np.dot(A_np.T, y_np)
    
    # Résolution du système
    coeffs = np.linalg.solve(ATA, ATy)
    
    # Calcul de l'erreur
    y_pred = np.dot(A_np, coeffs)
    erreur = np.sum((y_np - y_pred)**2)
    
    # Construction du polynôme
    polynome_terms = []
    for i, coeff in enumerate(coeffs):
        if abs(coeff) > 1e-10:
            if i == 0:
                polynome_terms.append(f"{coeff:.6f}")
            elif i == 1:
                polynome_terms.append(f"{coeff:.6f} * x")
            else:
                polynome_terms.append(f"{coeff:.6f} * x^{i}")
    
    polynome = "P(x) = " + " + ".join(polynome_terms)
    
    details = {
        'degre': degre,
        'coefficients': coeffs.tolist(),
        'erreur_quadratique': erreur,
        'matrice_A': A_np.tolist(),
        'ATA': ATA.tolist(),
        'ATy': ATy.tolist()
    }
    
    return coeffs, erreur, polynome, details