# convertisseur_final.py
import json
import os

def convertir_tout():
    """Convertit tout le fichier Débutant.txt en JSON complet"""
    print("🔄 Conversion de toutes les questions...")
    
    try:
        with open("Débutant.txt", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Séparer les sections
        sections = content.split('"Intermédiaire"')
        debutant_content = sections[0]
        intermediaire_expert = sections[1].split('"Expert"')
        intermediaire_content = intermediaire_expert[0]
        expert_content = intermediaire_expert[1]
        
        # Extraire toutes les questions
        questions_completes = {
            "Débutant": _extraire_questions_completes(debutant_content),
            "Intermédiaire": _extraire_questions_completes(intermediaire_content),
            "Expert": _extraire_questions_completes(expert_content)
        }
        
        # Créer le dossier data
        os.makedirs("data", exist_ok=True)
        
        # Sauvegarder
        with open("data/questions.json", "w", encoding="utf-8") as f:
            json.dump(questions_completes, f, ensure_ascii=False, indent=2)
        
        # Statistiques
        stats = {niveau: len(questions) for niveau, questions in questions_completes.items()}
        total = sum(stats.values())
        
        print("✅ CONVERSION RÉUSSIE !")
        print(f"📊 Statistiques finales:")
        for niveau, count in stats.items():
            print(f"   • {niveau}: {count} questions")
        print(f"   • TOTAL: {total} questions")
        print(f"💾 Fichier: data/questions.json")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def _extraire_questions_completes(contenu):
    """Extrait toutes les questions d'une section"""
    questions = []
    lignes = contenu.split('\n')
    
    for line in lignes:
        line = line.strip()
        if not line or line == "{" or line == "}":
            continue
            
        if '"question":' in line and '"reponse":' in line:
            try:
                # Question
                debut_question = line.find('"question": "') + 13
                fin_question = line.find('",', debut_question)
                question = line[debut_question:fin_question]
                
                # Réponse
                debut_reponse = line.find('"reponse": ') + 11
                fin_reponse = line.find(',', debut_reponse)
                if fin_reponse == -1:
                    fin_reponse = line.find('}', debut_reponse)
                reponse_text = line[debut_reponse:fin_reponse].strip()
                
                # Conversion réponse
                if "indéfini" in reponse_text.lower():
                    reponse = "indéfini"
                elif '/' in reponse_text:
                    reponse = reponse_text
                elif '.' in reponse_text:
                    reponse = float(reponse_text)
                else:
                    reponse = int(reponse_text)
                
                # Points
                debut_points = line.find('"points": ') + 9
                fin_points = line.find('}', debut_points)
                points_text = line[debut_points:fin_points].strip()
                points = int(points_text)
                
                # Type
                debut_type = line.find('"type": "') + 9
                fin_type = line.find('"', debut_type)
                type_question = line[debut_type:fin_type]
                
                questions.append({
                    "question": question,
                    "reponse": reponse,
                    "points": points,
                    "type": type_question
                })
                
            except Exception as e:
                print(f"⚠️ Ligne ignorée: {line[:50]}...")
                continue
                
    return questions

if __name__ == "__main__":
    print("=" * 60)
    print("🎯 CRÉATION DU FICHIER QUESTIONS.JSON FINAL")
    print("=" * 60)
    
    if convertir_tout():
        print("\n" + "=" * 60)
        print("🎉 Fichier data/questions.json créé avec succès!")
        print("📦 Tu peux maintenant inclure ce fichier dans ton projet")
        print("👤 Les utilisateurs n'auront rien à installer")
        print("=" * 60)
    else:
        print("\n❌ La conversion a échoué")