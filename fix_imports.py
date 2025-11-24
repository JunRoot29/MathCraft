#!/usr/bin/env python3
"""
Script de correction des imports pour MathCraft
"""

import os
import re

def fix_imports_in_file(filepath):
    """Corrige les imports dans un fichier"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Corrections spécifiques
    replacements = {
        'from App import modules as modu': 'from . import modules as modu',
        'from historique_manager import': 'from App.historique_manager import',
        # Ajouter d'autres remplacements si nécessaire
    }
    
    original_content = content
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Corrigé : {filepath}")

def main():
    """Corrige tous les fichiers du projet"""
    files_to_fix = [
        'App/operation_de_base.py',
        'App/polynome.py', 
        'App/integration_numerique.py',
        'App/theorie_des_nombres.py',
        'main.py'
    ]
    
    for filepath in files_to_fix:
        if os.path.exists(filepath):
            fix_imports_in_file(filepath)
        else:
            print(f"✗ Fichier non trouvé : {filepath}")
    
    print("Correction des imports terminée!")

if __name__ == "__main__":
    main()