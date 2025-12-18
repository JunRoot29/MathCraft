import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
print('default root before import:', tk._default_root)
print('default root after import:', tk._default_root)
# Pour vérifier, si une racine existe on affiche son titre
if tk._default_root:
    try:
        print('root title:', tk._default_root.title())
    except Exception as e:
        print('could not get title:', e)
