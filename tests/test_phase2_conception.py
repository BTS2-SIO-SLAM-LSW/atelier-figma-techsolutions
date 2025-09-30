#!/usr/bin/env python3
"""
Tests automatisés Phase 2 : Conception
GitHub Classroom Auto-grading
"""

import json
import sys
import os

def load_student_answers():
    """Charge les réponses de l'étudiant depuis le fichier JSON"""
    try:
        with open('submissions/qcm_phase2_reponses.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ ERREUR: Fichier qcm_phase2_reponses.json introuvable")
        print("💡 Créez le fichier avec vos réponses dans submissions/")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ ERREUR: Format JSON invalide")
        sys.exit(1)

def test_phase2_conception():
    """Test des réponses Phase 2 - Conception"""
    
    # Réponses correctes
    correct_answers = {
        "question1": "b",  # Outils Figma (Frame)
        "question2": "b",  # Composants vs Instances
        "question3": "b",  # Charte TechSolutions
        "question4": "c",  # Hiérarchie visuelle urgences
        "question5": "c",  # Ergonomie tablette (44px)
        "question6": "b"   # Prototypage interactions
    }
    
    # Messages d'explication
    explanations = {
        "question1": "Frame (F) - Les conteneurs principaux de Figma",
        "question2": "Composant = modèle maître, Instance = copie synchronisée",
        "question3": "Couleurs officielles de la charte TechSolutions",
        "question4": "Urgences en évidence selon la loi de Fitts",
        "question5": "44x44px minimum pour utilisation tactile confortable",
        "question6": "Outil Prototype pour les interactions"
    }
    
    # Conseils de rattrapage
    tips = {
        "question1": "💡 Raccourci Figma : F=Frame, R=Rectangle, K=Scale, V=Move",
        "question2": "💡 Composants : Clic droit > 'Create Component' puis 'Create Instance'",
        "question3": "💡 Relisez charte_graphique.md - Section 'Couleurs principales'",
        "question4": "💡 Principe UX : Les éléments importants doivent être visibles et accessibles",
        "question5": "💡 Standards : 44px minimum Apple, 48px recommandé Google",
        "question6": "💡 Mode Prototype : Glisser flèche entre frames"
    }
    
    student_answers = load_student_answers()
    score = 0
    max_score = 6
    feedback = []
    technical_help = []
    
    print("🎨 CORRECTION PHASE 2 : CONCEPTION")
    print("=" * 50)
    
    for question, correct_answer in correct_answers.items():
        student_answer = student_answers.get(question, "").lower().strip()
        
        if student_answer == correct_answer:
            score += 1
            print(f"✅ {question.upper()}: CORRECT ({student_answer})")
            feedback.append(f"✅ {question}: Bonne réponse !")
        else:
            print(f"❌ {question.upper()}: INCORRECT ({student_answer} ≠ {correct_answer})")
            feedback.append(f"❌ {question}: {explanations[question]}")
            technical_help.append(tips[question])
    
    # Résultats
    percentage = (score / max_score) * 100
    print(f"\n📊 RÉSULTAT: {score}/{max_score} ({percentage:.0f}%)")
    
    # Évaluation spécifique Phase 2
    if percentage >= 83:  # 5/6
        print("🏆 EXCELLENT ! Maîtrise technique validée")
        feedback.append("🏆 Phase 2 excellente ! Vous maîtrisez Figma et les principes design")
    elif percentage >= 67:  # 4/6
        print("✅ BIEN ! Vous pouvez présenter")
        feedback.append("✅ Phase 2 validée ! Quelques points techniques à approfondir")
    else:
        print("⚠️  Support enseignant recommandé pendant présentation")
        feedback.append("⚠️ Difficultés techniques : support enseignant pendant présentation")
    
    # Checklist prototype
    print("\n📱 CHECKLIST AVANT PRÉSENTATION:")
    checklist = [
        "3 écrans minimum fonctionnels",
        "Navigation entre écrans qui marche", 
        "Couleurs TechSolutions appliquées",
        "Urgences visibles et accessibles",
        "Boutons taille minimum 44px"
    ]
    
    for item in checklist:
        print(f"☐ {item}")
    
    # Sauvegarde feedback pour GitHub Classroom
    with open('feedback_phase2.txt', 'w', encoding='utf-8') as f:
        f.write(f"PHASE 2 - CONCEPTION: {score}/{max_score} ({percentage:.0f}%)\n\n")
        f.write("FEEDBACK:\n")
        f.write("\n".join(feedback))
        
        if technical_help:
            f.write("\n\nAIDE TECHNIQUE:\n")
            f.write("\n".join(technical_help))
        
        f.write("\n\nCHECKLIST PROTOTYPE:\n")
        for item in checklist:
            f.write(f"☐ {item}\n")
    
    return score >= 4  # Minimum 4/6 pour valider

if __name__ == "__main__":
    success = test_phase2_conception()
    sys.exit(0 if success else 1)