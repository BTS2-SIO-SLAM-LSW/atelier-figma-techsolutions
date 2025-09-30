#!/usr/bin/env python3
"""
Tests automatiques pour l'Atelier Figma TechSolutions
GitHub Classroom Autograding
"""

import json
import sys
import argparse
import os
import re
from pathlib import Path
import requests
from jsonschema import validate, ValidationError

class FigmaWorkshopTester:
    def __init__(self):
        self.submission_path = "submissions/my_submission.json"
        self.template_path = "submissions/student_template.json"
        self.errors = []
        self.warnings = []
        self.score = 0
        self.max_score = 0

    def load_submission(self):
        """Charge le fichier de soumission étudiant"""
        if not os.path.exists(self.submission_path):
            raise FileNotFoundError(f"❌ Fichier de soumission introuvable: {self.submission_path}")
        
        try:
            with open(self.submission_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"❌ Fichier JSON invalide: {e}")

    def load_template(self):
        """Charge le template pour validation du schéma"""
        try:
            with open(self.template_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def test_json_structure(self):
        """TEST 1: Validation de la structure JSON (20 points)"""
        print("\n🔍 TEST 1 - Structure JSON")
        self.max_score = 20
        
        try:
            submission = self.load_submission()
            template = self.load_template()
            
            # Vérifications de base
            required_sections = [
                "etudiant_info", "analyse_ux", "conception", 
                "prototypage", "qcm_responses", "auto_evaluation"
            ]
            
            for section in required_sections:
                if section not in submission:
                    self.errors.append(f"❌ Section manquante: {section}")
                else:
                    self.score += 3
                    print(f"✅ Section présente: {section}")
            
            # Validation des champs étudiant
            if "etudiant_info" in submission:
                student_info = submission["etudiant_info"]
                required_fields = ["nom", "prenom", "email", "date_soumission"]
                
                for field in required_fields:
                    if field in student_info and student_info[field]:
                        self.score += 1
                        print(f"✅ Info étudiant: {field}")
                    else:
                        self.errors.append(f"❌ Info manquante: {field}")
            
            # Score bonus pour structure propre
            if len(self.errors) == 0:
                self.score += 2
                print("✅ Bonus: Structure parfaite")
            
        except Exception as e:
            self.errors.append(f"❌ Erreur structure: {e}")
        
        print(f"📊 Score structure: {self.score}/{self.max_score}")
        return self.score > 0

    def test_ux_content(self):
        """TEST 2: Validation du contenu UX obligatoire (30 points)"""
        print("\n🎨 TEST 2 - Contenu UX")
        self.score = 0
        self.max_score = 30
        
        try:
            submission = self.load_submission()
            
            # Test analyse UX (10 points)
            if "analyse_ux" in submission:
                analyse = submission["analyse_ux"]
                
                # Personas définis
                if "personas" in analyse and len(analyse["personas"]) >= 2:
                    self.score += 3
                    print("✅ Personas définis (2+ personas)")
                else:
                    self.errors.append("❌ Minimum 2 personas requis")
                
                # Cas d'utilisation
                if "cas_utilisation" in analyse and len(analyse["cas_utilisation"]) >= 3:
                    self.score += 3
                    print("✅ Cas d'utilisation définis (3+ cas)")
                else:
                    self.errors.append("❌ Minimum 3 cas d'utilisation requis")
                
                # Journey maps
                if "journey_maps" in analyse and analyse["journey_maps"]:
                    self.score += 4
                    print("✅ Journey maps présents")
                else:
                    self.warnings.append("⚠️ Journey maps recommandés")
            
            # Test conception (10 points)
            if "conception" in submission:
                conception = submission["conception"]
                
                # Wireframes
                if "wireframes" in conception and len(conception["wireframes"]) >= 3:
                    self.score += 5
                    print("✅ Wireframes présents (3+ écrans)")
                else:
                    self.errors.append("❌ Minimum 3 wireframes requis")
                
                # Design system
                if "design_system" in conception:
                    ds = conception["design_system"]
                    if "colors" in ds and "typography" in ds:
                        self.score += 3
                        print("✅ Design system défini")
                    else:
                        self.errors.append("❌ Design system incomplet")
                else:
                    self.errors.append("❌ Design system manquant")
                
                # Composants UI
                if "composants_ui" in conception and len(conception["composants_ui"]) >= 5:
                    self.score += 2
                    print("✅ Composants UI créés")
            
            # Test prototypage (10 points)
            if "prototypage" in submission:
                proto = submission["prototypage"]
                
                # Interactions définies
                if "interactions" in proto and len(proto["interactions"]) >= 5:
                    self.score += 5
                    print("✅ Interactions définies (5+)")
                else:
                    self.warnings.append("⚠️ Plus d'interactions recommandées")
                
                # Navigation cohérente
                if "navigation" in proto and proto["navigation"]:
                    self.score += 3
                    print("✅ Navigation définie")
                
                # Tests utilisateurs
                if "tests_utilisateurs" in proto and proto["tests_utilisateurs"]:
                    self.score += 2
                    print("✅ Tests utilisateurs documentés")
        
        except Exception as e:
            self.errors.append(f"❌ Erreur contenu UX: {e}")
        
        print(f"📊 Score contenu UX: {self.score}/{self.max_score}")
        return self.score >= 15  # 50% minimum

    def test_figma_links(self):
        """TEST 3: Validation des liens Figma (25 points)"""
        print("\n🔗 TEST 3 - Liens Figma")
        self.score = 0
        self.max_score = 25
        
        try:
            submission = self.load_submission()
            figma_pattern = r'https://www\.figma\.com/(file|proto)/[A-Za-z0-9]+'
            
            # Recherche liens dans toute la soumission
            links_found = []
            
            def extract_links(obj, path=""):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        if isinstance(value, str) and re.search(figma_pattern, value):
                            links_found.append(f"{path}.{key}" if path else key)
                        elif isinstance(value, (dict, list)):
                            extract_links(value, f"{path}.{key}" if path else key)
                elif isinstance(obj, list):
                    for i, item in enumerate(obj):
                        extract_links(item, f"{path}[{i}]" if path else f"[{i}]")
            
            extract_links(submission)
            
            # Validation des liens
            valid_links = 0
            for link_path in links_found:
                # Test simple de format (sans requête HTTP pour éviter rate limits)
                if "figma.com" in str(submission):
                    valid_links += 1
                    self.score += 5
                    print(f"✅ Lien Figma trouvé: {link_path}")
            
            # Bonus pour liens multiples
            if valid_links >= 2:
                self.score += 5
                print("✅ Bonus: Liens multiples")
            
            # Vérification spécifique prototype
            if "prototypage" in submission and "lien_prototype" in submission["prototypage"]:
                proto_link = submission["prototypage"]["lien_prototype"]
                if re.search(figma_pattern, proto_link):
                    self.score += 10
                    print("✅ Lien prototype valide")
                else:
                    self.errors.append("❌ Lien prototype invalide")
            else:
                self.errors.append("❌ Lien prototype manquant")
        
        except Exception as e:
            self.errors.append(f"❌ Erreur liens Figma: {e}")
        
        print(f"📊 Score liens Figma: {self.score}/{self.max_score}")
        return self.score >= 10  # Minimum 40%

    def test_qcm_answers(self):
        """TEST 4: Validation réponses QCM (15 points)"""
        print("\n📝 TEST 4 - Réponses QCM")
        self.score = 0
        self.max_score = 15
        
        try:
            submission = self.load_submission()
            
            if "qcm_responses" not in submission:
                self.errors.append("❌ Section qcm_responses manquante")
                print(f"📊 Score QCM: {self.score}/{self.max_score}")
                return False
            
            qcm = submission["qcm_responses"]
            expected_phases = ["phase1", "phase2", "phase3", "final"]
            
            for phase in expected_phases:
                if phase in qcm:
                    phase_answers = qcm[phase]
                    if isinstance(phase_answers, dict) and len(phase_answers) > 0:
                        self.score += 3
                        print(f"✅ QCM {phase}: réponses présentes")
                        
                        # Vérification que les réponses ne sont pas vides
                        valid_answers = sum(1 for v in phase_answers.values() if v is not None and v != "")
                        if valid_answers >= len(phase_answers) * 0.8:  # 80% des réponses
                            self.score += 1
                            print(f"✅ QCM {phase}: réponses complètes")
                    else:
                        self.errors.append(f"❌ QCM {phase}: réponses manquantes")
                else:
                    self.errors.append(f"❌ QCM {phase}: section manquante")
            
            # Bonus pour justifications
            if any("justification" in str(phase_data) for phase_data in qcm.values()):
                self.score += 3
                print("✅ Bonus: Justifications présentes")
        
        except Exception as e:
            self.errors.append(f"❌ Erreur QCM: {e}")
        
        print(f"📊 Score QCM: {self.score}/{self.max_score}")
        return self.score >= 8  # Minimum 50%

    def test_self_evaluation(self):
        """TEST 5: Auto-évaluation complète (10 points)"""
        print("\n📋 TEST 5 - Auto-évaluation")
        self.score = 0
        self.max_score = 10
        
        try:
            submission = self.load_submission()
            
            if "auto_evaluation" not in submission:
                self.errors.append("❌ Section auto_evaluation manquante")
                print(f"📊 Score auto-évaluation: {self.score}/{self.max_score}")
                return False
            
            auto_eval = submission["auto_evaluation"]
            
            # Critères obligatoires
            required_criteria = [
                "analyse_ux_score", "conception_score", "prototypage_score",
                "points_forts", "points_amelioration", "satisfaction_globale"
            ]
            
            for criterion in required_criteria:
                if criterion in auto_eval and auto_eval[criterion] is not None:
                    self.score += 1
                    print(f"✅ Auto-évaluation: {criterion}")
                else:
                    self.errors.append(f"❌ Auto-évaluation manquante: {criterion}")
            
            # Validation des scores (doivent être numériques)
            score_fields = ["analyse_ux_score", "conception_score", "prototypage_score", "satisfaction_globale"]
            for field in score_fields:
                if field in auto_eval:
                    try:
                        score_val = float(auto_eval[field])
                        if 0 <= score_val <= 5:  # Échelle 0-5
                            self.score += 1
                            print(f"✅ Score valide: {field}")
                        else:
                            self.warnings.append(f"⚠️ Score hors échelle (0-5): {field}")
                    except (ValueError, TypeError):
                        self.warnings.append(f"⚠️ Score non numérique: {field}")
        
        except Exception as e:
            self.errors.append(f"❌ Erreur auto-évaluation: {e}")
        
        print(f"📊 Score auto-évaluation: {self.score}/{self.max_score}")
        return self.score >= 6  # Minimum 60%

    def run_test(self, test_name):
        """Exécute un test spécifique"""
        test_methods = {
            "structure": self.test_json_structure,
            "ux_content": self.test_ux_content,
            "figma_links": self.test_figma_links,
            "qcm_answers": self.test_qcm_answers,
            "self_evaluation": self.test_self_evaluation
        }
        
        if test_name not in test_methods:
            print(f"❌ Test inconnu: {test_name}")
            return False
        
        try:
            success = test_methods[test_name]()
            
            # Affichage résumé
            if self.errors:
                print(f"\n❌ Erreurs ({len(self.errors)}):")
                for error in self.errors:
                    print(f"   {error}")
            
            if self.warnings:
                print(f"\n⚠️ Avertissements ({len(self.warnings)}):")
                for warning in self.warnings:
                    print(f"   {warning}")
            
            if success:
                print(f"\n✅ Test {test_name} RÉUSSI")
            else:
                print(f"\n❌ Test {test_name} ÉCHOUÉ")
            
            return success
            
        except Exception as e:
            print(f"\n💥 Erreur test {test_name}: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description="Tests Atelier Figma TechSolutions")
    parser.add_argument("--test", required=True, 
                       choices=["structure", "ux_content", "figma_links", "qcm_answers", "self_evaluation"],
                       help="Type de test à exécuter")
    
    args = parser.parse_args()
    
    tester = FigmaWorkshopTester()
    success = tester.run_test(args.test)
    
    # Exit code pour GitHub Actions
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()