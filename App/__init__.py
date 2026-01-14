"""
Package MathCraft - Application éducative de mathématiques
"""

from .historique_manager import historique_manager
from .interface_historique import InterfaceHistorique

__version__ = "2.1.0"
__author__ = "Junior Kossivi"
__description__ = "Un espace malin pour calculer et s'amuser avec les maths"

def enregistrer_calcul(module, operation, entree, resultat):
    """Enregistre un calcul dans l'historique"""
    return historique_manager.ajouter_calcul(module, operation, entree, resultat)