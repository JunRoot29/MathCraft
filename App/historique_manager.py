"""
Gestionnaire d'historique et sauvegarde des calculs
"""
import json
import os
import datetime
from typing import Dict, List, Any
import pickle
import csv

class HistoriqueManager:
    def __init__(self, dossier_sauvegarde: str = "sauvegardes"):
        self.dossier_sauvegarde = dossier_sauvegarde
        self.fichier_historique = os.path.join(dossier_sauvegarde, "historique_calculs.json")
        self.fichier_sessions = os.path.join(dossier_sauvegarde, "sessions.pkl")
        
        # Créer le dossier de sauvegarde s'il n'existe pas
        os.makedirs(dossier_sauvegarde, exist_ok=True)
        
        # Initialiser l'historique
        self.historique = self._charger_historique()
        self.session_actuelle = []
    
    def _charger_historique(self) -> List[Dict]:
        """Charge l'historique depuis le fichier JSON"""
        try:
            if os.path.exists(self.fichier_historique):
                with open(self.fichier_historique, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        return []
    
    def _sauvegarder_historique(self):
        """Sauvegarde l'historique dans le fichier JSON"""
        try:
            with open(self.fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(self.historique, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erreur sauvegarde historique: {e}")
    
    def ajouter_calcul(self, module: str, operation: str, entree: Dict, resultat):
        """Ajoute un calcul à l'historique.

        Le champ `resultat` peut être :
        - une valeur simple (float, str...)
        - un tuple (valeur, details) pour les méthodes d'intégration et d'itérations
        - une structure (dict/list)

        Cette méthode normalise le résultat pour garantir une représentation JSON-friendly.
        """
        # Normaliser le résultat pour supporter (valeur, details) et autres types
        try:
            if isinstance(resultat, tuple) and len(resultat) == 2 and isinstance(resultat[1], (list, dict)):
                normalized = {"valeur": resultat[0], "details": resultat[1]}
            elif isinstance(resultat, dict):
                normalized = resultat
            elif isinstance(resultat, list):
                normalized = {"valeur": None, "details": resultat}
            else:
                normalized = resultat
        except Exception:
            normalized = str(resultat)

        calcul = {
            "id": len(self.historique) + 1,
            "timestamp": datetime.datetime.now().isoformat(),
            "date_affichage": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "module": module,
            "operation": operation,
            "entree": entree,
            "resultat": normalized
        }
        
        # Ajouter à l'historique global
        self.historique.append(calcul)
        
        # Ajouter à la session actuelle
        self.session_actuelle.append(calcul)
        
        # Sauvegarder
        self._sauvegarder_historique()
        
        return calcul
    
    def obtenir_historique_complet(self, limite: int = None) -> List[Dict]:
        """Retourne l'historique complet ou les N derniers calculs"""
        if limite and limite > 0:
            return self.historique[-limite:]
        return self.historique.copy()
    
    def obtenir_session_actuelle(self) -> List[Dict]:
        """Retourne les calculs de la session en cours"""
        return self.session_actuelle.copy()
    
    def filtrer_par_module(self, module: str) -> List[Dict]:
        """Filtre l'historique par module"""
        return [calc for calc in self.historique if calc["module"] == module]
    
    def rechercher_calculs(self, terme: str) -> List[Dict]:
        """Recherche dans l'historique"""
        terme = terme.lower()
        resultats = []
        
        for calcul in self.historique:
            resultat_str = json.dumps(calcul.get("resultat", ""), ensure_ascii=False).lower()
            if (terme in calcul["module"].lower() or 
                terme in calcul["operation"].lower() or 
                terme in resultat_str or
                any(terme in str(v).lower() for v in calcul["entree"].values())):
                resultats.append(calcul)
        
        return resultats
    
    def exporter_json(self, fichier: str = None):
        """Exporte l'historique en JSON"""
        if not fichier:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            fichier = os.path.join(self.dossier_sauvegarde, f"export_historique_{timestamp}.json")
        
        try:
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(self.historique, f, ensure_ascii=False, indent=2)
            return f"✅ Historique exporté: {fichier}"
        except Exception as e:
            return f"❌ Erreur export: {str(e)}"
    
    def exporter_csv(self, fichier: str = None):
        """Exporte l'historique en CSV"""
        if not fichier:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            fichier = os.path.join(self.dossier_sauvegarde, f"export_historique_{timestamp}.csv")
        
        try:
            with open(fichier, 'w', newline='', encoding='utf-8') as f:
                if self.historique:
                    fieldnames = ['id', 'date_affichage', 'module', 'operation', 'entree', 'resultat']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    
                    writer.writeheader()
                    for calcul in self.historique:
                        row = {
                            'id': calcul['id'],
                            'date_affichage': calcul['date_affichage'],
                            'module': calcul['module'],
                            'operation': calcul['operation'],
                            'entree': str(calcul['entree']),
                            'resultat': json.dumps(calcul['resultat'], ensure_ascii=False)
                        }
                        writer.writerow(row) 
            
            return f"✅ Historique exporté CSV: {fichier}"
        except Exception as e:
            return f"❌ Erreur export CSV: {str(e)}"
    
    def importer_json(self, fichier: str):
        """Importe un historique depuis un fichier JSON"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                nouvel_historique = json.load(f)
            
            # Fusionner avec l'historique existant
            self.historique.extend(nouvel_historique)
            self._sauvegarder_historique()
            
            return f"✅ Historique importé: {len(nouvel_historique)} calculs ajoutés"
        except Exception as e:
            return f"❌ Erreur import: {str(e)}"
    
    def vider_historique(self):
        """Vide complètement l'historique"""
        self.historique = []
        self.session_actuelle = []
        self._sauvegarder_historique()
        return "✅ Historique vidé"
    
    def supprimer_calcul(self, calcul_id: int):
        """Supprime un calcul spécifique"""
        self.historique = [calc for calc in self.historique if calc["id"] != calcul_id]
        self.session_actuelle = [calc for calc in self.session_actuelle if calc["id"] != calcul_id]
        self._sauvegarder_historique()
        return f"✅ Calcul #{calcul_id} supprimé"
    
    def obtenir_statistiques(self) -> Dict:
        """Retourne des statistiques sur l'historique"""
        if not self.historique:
            return {"total": 0}
        
        modules = {}
        for calcul in self.historique:
            module = calcul["module"]
            modules[module] = modules.get(module, 0) + 1
        
        return {
            "total_calculs": len(self.historique),
            "session_actuelle": len(self.session_actuelle),
            "par_module": modules,
            "premier_calcul": self.historique[0]["date_affichage"] if self.historique else "Aucun",
            "dernier_calcul": self.historique[-1]["date_affichage"] if self.historique else "Aucun"
        }

# Instance globale
historique_manager = HistoriqueManager()