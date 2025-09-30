#!/usr/bin/env python3
"""
Script d'extraction des réponses QCM depuis les soumissions GitHub Classroom
Usage: python extract_qcm_results.py <dossier_submissions>
"""

import json
import os
import sys
import csv
from pathlib import Path
from datetime import datetime

def extract_qcm_from_submission(submission_file):
    """Extrait les réponses QCM d'un fichier de soumission"""
    try:
        with open(submission_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        student_info = data.get('etudiant_info', {})
        qcm_responses = data.get('qcm_responses', {})
        
        result = {
            'nom': student_info.get('nom', 'N/A'),
            'prenom': student_info.get('prenom', 'N/A'),
            'email': student_info.get('email', 'N/A'),
            'date_soumission': student_info.get('date_soumission', 'N/A'),
        }
        
        # Extraction Phase 1
        phase1 = qcm_responses.get('phase1', {})
        result['p1_q1'] = phase1.get('q1_methodologie_ux', '')
        result['p1_q2'] = phase1.get('q2_personas', '')
        result['p1_q3'] = phase1.get('q3_cas_utilisation', '')
        result['p1_q4'] = phase1.get('q4_journey_mapping', '')
        
        # Extraction Phase 2
        phase2 = qcm_responses.get('phase2', {})
        result['p2_q1'] = phase2.get('q1_wireframes', '')
        result['p2_q2'] = phase2.get('q2_design_system', '')
        result['p2_q3'] = phase2.get('q3_couleurs', '')
        result['p2_q4'] = phase2.get('q4_typographie', '')
        result['p2_q5'] = phase2.get('q5_composants', '')
        result['p2_q6'] = phase2.get('q6_accessibilite', '')
        
        # Extraction Phase 3
        phase3 = qcm_responses.get('phase3', {})
        result['p3_q1'] = phase3.get('q1_prototypage', '')
        result['p3_q2'] = phase3.get('q2_interactions', '')
        result['p3_q3'] = phase3.get('q3_tests_utilisateurs', '')
        
        # Extraction Final
        final = qcm_responses.get('final', {})
        result['final_q1'] = final.get('q1_methodologie_complete', '')
        result['final_q2'] = final.get('q2_outils_figma', '')
        result['final_q3'] = final.get('q3_livrables', '')
        result['final_q4'] = final.get('q4_amelioration_continue', '')
        
        return result
        
    except Exception as e:
        print(f"❌ Erreur lors de la lecture de {submission_file}: {e}")
        return None

def calculate_qcm_score(responses):
    """Calcule le score QCM selon le barème"""
    correct_answers = {
        'p1_q1': 'B', 'p1_q2': 'A', 'p1_q3': 'C', 'p1_q4': 'B',
        'p2_q1': 'A', 'p2_q2': 'B', 'p2_q3': 'C', 'p2_q4': 'A', 'p2_q5': 'B', 'p2_q6': 'C',
        'p3_q1': 'A', 'p3_q2': 'B', 'p3_q3': 'C',
        'final_q1': 'B', 'final_q2': 'A', 'final_q3': 'C', 'final_q4': 'B'
    }
    
    score = 0
    total = 0
    details = {}
    
    for question, correct_answer in correct_answers.items():
        if question in responses:
            total += 1
            if responses[question] == correct_answer:
                score += 1
                details[question] = '✅'
            else:
                details[question] = f"❌ ({responses[question]}→{correct_answer})"
    
    return score, total, details

def process_classroom_download(download_folder):
    """Traite tous les repositories téléchargés depuis GitHub Classroom"""
    results = []
    
    download_path = Path(download_folder)
    
    if not download_path.exists():
        print(f"❌ Dossier introuvable: {download_folder}")
        return []
    
    print(f"🔍 Recherche des soumissions dans: {download_folder}\n")
    
    # Parcourir tous les sous-dossiers (1 par étudiant)
    for student_folder in download_path.iterdir():
        if not student_folder.is_dir():
            continue
        
        submission_file = student_folder / "submissions" / "my_submission.json"
        
        if submission_file.exists():
            print(f"✅ Trouvé: {student_folder.name}")
            result = extract_qcm_from_submission(submission_file)
            
            if result:
                # Calculer le score
                score, total, details = calculate_qcm_score(result)
                result['score_qcm'] = f"{score}/{total}"
                result['pourcentage'] = f"{(score/total*100):.1f}%"
                result['details'] = str(details)
                results.append(result)
        else:
            print(f"⚠️  Pas de soumission: {student_folder.name}")
    
    return results

def export_to_csv(results, output_file="qcm_results.csv"):
    """Export les résultats en CSV"""
    if not results:
        print("\n❌ Aucun résultat à exporter")
        return
    
    fieldnames = ['nom', 'prenom', 'email', 'date_soumission', 'score_qcm', 'pourcentage',
                  'p1_q1', 'p1_q2', 'p1_q3', 'p1_q4',
                  'p2_q1', 'p2_q2', 'p2_q3', 'p2_q4', 'p2_q5', 'p2_q6',
                  'p3_q1', 'p3_q2', 'p3_q3',
                  'final_q1', 'final_q2', 'final_q3', 'final_q4']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for result in results:
            # Filtrer pour ne garder que les champs du CSV
            row = {k: result.get(k, '') for k in fieldnames}
            writer.writerow(row)
    
    print(f"\n✅ Export CSV réussi: {output_file}")

def print_summary(results):
    """Affiche un résumé des résultats"""
    if not results:
        return
    
    print("\n" + "="*60)
    print("📊 RÉSUMÉ DES RÉSULTATS QCM")
    print("="*60)
    
    for result in results:
        print(f"\n👤 {result['prenom']} {result['nom']}")
        print(f"   📧 {result['email']}")
        print(f"   📅 Soumis le: {result['date_soumission']}")
        print(f"   ✅ Score: {result['score_qcm']} ({result['pourcentage']})")
    
    # Statistiques globales
    total_students = len(results)
    scores = [int(r['score_qcm'].split('/')[0]) for r in results]
    avg_score = sum(scores) / len(scores) if scores else 0
    
    print("\n" + "="*60)
    print("📈 STATISTIQUES GLOBALES")
    print("="*60)
    print(f"   Nombre d'étudiants: {total_students}")
    print(f"   Score moyen: {avg_score:.1f}/17 ({avg_score/17*100:.1f}%)")
    print(f"   Score minimum: {min(scores)}/17")
    print(f"   Score maximum: {max(scores)}/17")

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_qcm_results.py <dossier_submissions>")
        print("\nExemple:")
        print("  python extract_qcm_results.py ./atelier-figma-assignments")
        sys.exit(1)
    
    download_folder = sys.argv[1]
    
    print("🚀 Extraction des réponses QCM - Atelier Figma TechSolutions")
    print("="*60 + "\n")
    
    results = process_classroom_download(download_folder)
    
    if results:
        print_summary(results)
        
        # Export CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"qcm_results_{timestamp}.csv"
        export_to_csv(results, output_file)
        
        print(f"\n✅ Traitement terminé!")
        print(f"📁 Fichier CSV: {output_file}")
    else:
        print("\n❌ Aucune soumission trouvée")

if __name__ == "__main__":
    main()