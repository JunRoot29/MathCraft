import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
print('default root before imports:', tk._default_root)
modules = ['polynome','operation_de_base','theorie_des_nombres','conversion','chaine_de_caractere','integration_numerique','interface_historique','explorateur_concepts','soutient_manager','interpolation_lineaire','equation_numerique','jeux_math','modules']
for m in modules:
    modname = 'App.'+m
    try:
        __import__(modname)
        print(f'imported {modname} -> default root now: {tk._default_root}')
    except Exception as e:
        print(f'failed to import {modname}: {e}')
