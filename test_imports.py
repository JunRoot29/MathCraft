#!/usr/bin/env python3
"""
Script de test pour vérifier les imports
"""

try:
    from App.operation_de_base import launch_operation
    from App.theorie_des_nombres import lancer_theorie
    from App.historique_manager import historique_manager
    print("✅ Tous les imports fonctionnent !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")