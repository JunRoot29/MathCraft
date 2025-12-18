"""Test automatique : s'assure qu'aucun module d'App n'instancie une racine Tk lors de l'import.

Retourne code d'erreur non nul si une racine Tk est créée.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk

modules = ['polynome','operation_de_base','theorie_des_nombres','conversion','chaine_de_caractere','integration_numerique','interface_historique','explorateur_concepts','soutient_manager','interpolation_lineaire','equation_numerique','jeux_math','modules']

print('default root before imports:', tk._default_root)
failed = False
for m in modules:
    name = 'App.' + m
    try:
        __import__(name)
    except Exception as e:
        print(f'WARNING: import {name} failed: {e}')

    if tk._default_root is not None:
        print(f'ERROR: importing {name} created a default root: {tk._default_root}')
        failed = True

if failed:
    print('\nTest failed: un module a créé une racine Tk lors de l\'import. Veuillez corriger.')
    sys.exit(1)

print('OK: aucun module n\'a créé de racine Tk lors de l\'import')
sys.exit(0)
