# Configuration GitHub Classroom - Atelier Figma TechSolutions

## 🎯 Objectif

Intégrer les QCM de l'atelier dans GitHub Classroom avec notation automatique et rétroaction immédiate via GitHub Actions.

## 📋 Structure recommandée pour GitHub Classroom

### 🗂️ **Organisation des fichiers** :

```
atelier-figma-techsolutions/
├── .github/
│   └── workflows/
│       ├── autograding.yml          # Tests automatisés
│       └── feedback.yml             # Rétroaction personnalisée
├── tests/
│   ├── test_phase1_analyse.py       # Tests Phase 1
│   ├── test_phase2_conception.py    # Tests Phase 2
│   ├── test_phase3_presentation.py  # Tests Phase 3
│   └── test_final_synthese.py       # Tests final
├── submissions/
│   ├── qcm_phase1_reponses.json     # Template réponses étudiants
│   ├── qcm_phase2_reponses.json
│   ├── qcm_phase3_reponses.json
│   └── qcm_final_reponses.json
├── ressources/                      # Documents étudiants existants
└── docs/                           # Documents enseignants existants
```

## ⚙️ Configuration GitHub Actions

### 1. **Workflow principal** (`.github/workflows/autograding.yml`)

```yaml
name: GitHub Classroom Workflow

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

permissions:
  checks: write
  actions: read
  contents: read

jobs:
  run-autograding-tests:
    runs-on: ubuntu-latest
    if: github.actor != 'github-classroom[bot]'
    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install pytest pytest-json-report

    - name: Phase 1 - Analyse UX
      id: phase1
      uses: classroom-resources/autograding-command-grader@v1
      with:
        test-name: "Phase 1 - Analyse UX"
        setup-command: ""
        command: "python tests/test_phase1_analyse.py"
        timeout: 2
        max-score: 4

    - name: Phase 2 - Conception
      id: phase2
      uses: classroom-resources/autograding-command-grader@v1
      with:
        test-name: "Phase 2 - Conception" 
        setup-command: ""
        command: "python tests/test_phase2_conception.py"
        timeout: 2
        max-score: 6

    - name: Phase 3 - Présentation
      id: phase3
      uses: classroom-resources/autograding-command-grader@v1
      with:
        test-name: "Phase 3 - Présentation"
        setup-command: ""
        command: "python tests/test_phase3_presentation.py"
        timeout: 2
        max-score: 3

    - name: QCM Final - Synthèse
      id: final
      uses: classroom-resources/autograding-command-grader@v1
      with:
        test-name: "QCM Final - Synthèse"
        setup-command: ""
        command: "python tests/test_final_synthese.py"
        timeout: 2
        max-score: 4

    - name: Autograding Reporter
      uses: classroom-resources/autograding-grading-reporter@v1
      env:
        PHASE1_RESULTS: "${{steps.phase1.outputs.result}}"
        PHASE2_RESULTS: "${{steps.phase2.outputs.result}}"
        PHASE3_RESULTS: "${{steps.phase3.outputs.result}}"
        FINAL_RESULTS: "${{steps.final.outputs.result}}"
      with:
        runners: phase1,phase2,phase3,final
```

### 2. **Tests Phase 1** (`tests/test_phase1_analyse.py`)

```python
#!/usr/bin/env python3
"""
Tests automatisés Phase 1 : Analyse UX
GitHub Classroom Auto-grading
"""

import json
import sys
import os

def load_student_answers():
    """Charge les réponses de l'étudiant depuis le fichier JSON"""
    try:
        with open('submissions/qcm_phase1_reponses.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ ERREUR: Fichier qcm_phase1_reponses.json introuvable")
        print("💡 Créez le fichier avec vos réponses dans submissions/")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ ERREUR: Format JSON invalide")
        sys.exit(1)

def test_phase1_analyse():
    """Test des réponses Phase 1 - Analyse UX"""
    
    # Réponses correctes
    correct_answers = {
        "question1": "b",  # Format cas d'utilisation
        "question2": "b",  # Interview Thomas
        "question3": "c",  # Priorisation UX
        "question4": "c"   # Acteurs identifiés
    }
    
    # Messages d'explication
    explanations = {
        "question1": "Format standard 'En tant que... je veux... pour...'",
        "question2": "Thomas mentionne explicitement cette complexité excessive",
        "question3": "La priorisation UX se base sur les besoins utilisateurs réels",
        "question4": "Les 4 profils distincts révélés par les interviews"
    }
    
    student_answers = load_student_answers()
    score = 0
    max_score = 4
    feedback = []
    
    print("🎯 CORRECTION PHASE 1 : ANALYSE UX")
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
    
    # Résultats
    percentage = (score / max_score) * 100
    print(f"\n📊 RÉSULTAT: {score}/{max_score} ({percentage:.0f}%)")
    
    if percentage >= 75:
        print("🎉 VALIDÉ ! Vous pouvez passer à la Phase 2")
        feedback.append("🎉 Phase 1 validée ! Excellente compréhension de l'analyse UX")
    else:
        print("⚠️  Reprise conseillée. Relisez les interviews dans dossier_etudiant.md")
        feedback.append("⚠️ Reprise conseillée : relisez les interviews et le format des cas d'utilisation")
    
    # Sauvegarde feedback pour GitHub Classroom
    with open('feedback_phase1.txt', 'w', encoding='utf-8') as f:
        f.write(f"PHASE 1 - ANALYSE UX: {score}/{max_score} ({percentage:.0f}%)\n")
        f.write("\n".join(feedback))
    
    return score == max_score

if __name__ == "__main__":
    success = test_phase1_analyse()
    sys.exit(0 if success else 1)
```

### 3. **Template réponses étudiant** (`submissions/qcm_phase1_reponses.json`)

```json
{
  "etudiant": {
    "nom": "Nom Prénom",
    "email": "email@example.com",
    "date_soumission": "2025-09-30"
  },
  "phase1_analyse_ux": {
    "question1": "",
    "question2": "",
    "question3": "",
    "question4": ""
  },
  "commentaires": {
    "difficultes_rencontrees": "",
    "temps_passe_minutes": 30,
    "auto_evaluation": ""
  }
}
```

## 🎓 Instructions pour les étudiants

### 📝 **Comment soumettre vos réponses** :

1. **Clonez** votre dépôt GitHub Classroom
2. **Complétez** le fichier `submissions/qcm_phase1_reponses.json` :
   ```json
   {
     "etudiant": {
       "nom": "Dupont Jean",
       "email": "jean.dupont@school.fr",
       "date_soumission": "2025-09-30"
     },
     "phase1_analyse_ux": {
       "question1": "b",
       "question2": "b", 
       "question3": "c",
       "question4": "c"
     }
   }
   ```
3. **Commitez** et **pushez** vos changements
4. **Vérifiez** les résultats dans l'onglet "Actions" de GitHub

### ✅ **Rétroaction automatique** :
- ✅ **Score immédiat** : Visible dans GitHub Actions
- 📝 **Explications** : Pourquoi chaque réponse est correcte/incorrecte  
- 🎯 **Conseils** : Actions de rattrapage si score < 75%
- 📊 **Progression** : Suivi des 4 phases

## 🔧 Configuration GitHub Classroom

### 1. **Créer le devoir** :
- **Titre** : "Atelier Figma TechSolutions - QCM Validation"
- **Type** : Individual assignment
- **Repository template** : Votre repo avec les fichiers ci-dessus

### 2. **Activer l'auto-grading** :
- ✅ **Enable autograding**
- **Add test** pour chaque phase :
  - **Test name** : "Phase 1 - Analyse UX"
  - **Setup command** : (vide)
  - **Run command** : `python tests/test_phase1_analyse.py`
  - **Timeout** : 2 minutes
  - **Points** : 4

### 3. **Feedback template** :
```markdown
## 🎯 Résultats Atelier Figma TechSolutions

### 📊 Scores par phase :
- **Phase 1 - Analyse UX** : {score_phase1}/4
- **Phase 2 - Conception** : {score_phase2}/6  
- **Phase 3 - Présentation** : {score_phase3}/3
- **QCM Final** : {score_final}/4

**TOTAL** : {score_total}/17 ({percentage}%)

### 🎓 Niveau atteint :
{niveau_description}

### 📝 Recommandations :
{recommandations_personnalisees}
```

## 🚀 Avantages de cette approche

### ✅ **Pour les étudiants** :
- **Feedback immédiat** après chaque soumission
- **Progression visible** phase par phase
- **Conseils personnalisés** selon les erreurs
- **Autonomie** dans l'apprentissage

### ✅ **Pour l'enseignant** :
- **Correction automatisée** des QCM
- **Vue d'ensemble** des difficultés classe
- **Temps libéré** pour accompagnement personnalisé
- **Données précises** sur la progression

### ✅ **Intégration pédagogique** :
- **Validation progressive** : Pas d'accumulation de lacunes
- **Traçabilité** : Historique des tentatives
- **Gamification** : Badges et scores motivants
- **Scalabilité** : Fonctionne pour 5 ou 500 étudiants

Cette configuration transforme les QCM en outil d'apprentissage actif avec rétroaction immédiate ! 🎯✨