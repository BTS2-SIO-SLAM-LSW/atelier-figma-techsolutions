#!/usr/bin/env python3
"""
Génération de feedback personnalisé pour GitHub Classroom
Analyse les résultats des 4 phases et génère des recommandations
"""

import json
import os
from datetime import datetime

def load_all_results():
    """Charge tous les résultats des phases"""
    results = {}
    
    # Tente de charger chaque phase
    phases = ['phase1', 'phase2', 'phase3', 'final']
    
    for phase in phases:
        try:
            with open(f'submissions/qcm_{phase}_reponses.json', 'r', encoding='utf-8') as f:
                results[phase] = json.load(f)
        except FileNotFoundError:
            results[phase] = None
    
    return results

def calculate_total_score(results):
    """Calcule le score total sur 17 points"""
    scores = {
        'phase1': 0,
        'phase2': 0, 
        'phase3': 0,
        'final': 0
    }
    
    # Récupération des scores depuis les fichiers de feedback
    feedback_files = {
        'phase1': 'feedback_phase1.txt',
        'phase2': 'feedback_phase2.txt',
        'phase3': 'feedback_phase3.txt',
        'final': 'feedback_final.txt'
    }
    
    for phase, file in feedback_files.items():
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extraction du score depuis "X/Y (Z%)"
                import re
                match = re.search(r'(\d+)/(\d+)', content)
                if match:
                    scores[phase] = int(match.group(1))
        except FileNotFoundError:
            pass
    
    return scores

def get_level_description(total_score):
    """Détermine le niveau atteint selon le score total"""
    percentage = (total_score / 17) * 100
    
    if total_score >= 15:
        return {
            'niveau': '🏆 EXCELLENT',
            'description': 'Niveau professionnel atteint ! Vous maîtrisez parfaitement la méthodologie UX et Figma.',
            'badge': '🥇 Expert UX/UI'
        }
    elif total_score >= 13:
        return {
            'niveau': '🎯 TRÈS BIEN', 
            'description': 'Solides bases UX/UI acquises. Vous êtes prêt(e) pour des projets plus complexes.',
            'badge': '🥈 UX Designer'
        }
    elif total_score >= 10:
        return {
            'niveau': '✅ BIEN',
            'description': 'Objectifs pédagogiques atteints. Continuez à pratiquer pour gagner en aisance.',
            'badge': '🥉 UI Designer Junior'
        }
    elif total_score >= 8:
        return {
            'niveau': '⚠️ MOYEN',
            'description': 'Quelques notions à approfondir. Reprenez les ressources fournies.',
            'badge': '📚 En apprentissage'
        }
    else:
        return {
            'niveau': '🔄 DIFFICULTÉS',
            'description': 'Support enseignant recommandé. Ne vous découragez pas !',
            'badge': '🆘 Support nécessaire'
        }

def generate_recommendations(scores, results):
    """Génère des recommandations personnalisées"""
    recommendations = []
    
    # Analyse par phase
    if scores['phase1'] < 3:
        recommendations.append("📋 **Méthodologie UX** : Reprenez le guide_methodologie_ux_avance.md pour maîtriser les personas et cas d'utilisation")
    
    if scores['phase2'] < 4:
        recommendations.append("🎨 **Figma & Design** : Pratiquez avec les patterns_interface.md et la charte_graphique.md")
    
    if scores['phase3'] < 2:
        recommendations.append("🎤 **Justification UX** : Travaillez l'argumentation avec les bonnes_pratiques_ux_ui.md")
    
    if scores['final'] < 3:
        recommendations.append("📊 **Vision globale** : Relisez le prototype_exemple_complet.md pour comprendre la démarche complète")
    
    # Recommandations générales
    total = sum(scores.values())
    if total >= 13:
        recommendations.append("🚀 **Projet personnel** : Vous êtes prêt(e) à appliquer cette méthodologie sur un cas réel")
        recommendations.append("📈 **Portfolio** : Documentez ce projet avec vos justifications UX pour votre portfolio")
    elif total >= 10:
        recommendations.append("💪 **Pratique** : Refaites l'exercice avec un autre contexte métier pour consolider")
        recommendations.append("👥 **Communauté** : Rejoignez des groupes UX/UI pour échanger et progresser")
    else:
        recommendations.append("🎯 **Révision** : Reprenez l'atelier étape par étape avec les ressources fournies")
        recommendations.append("👨‍🏫 **Accompagnement** : Sollicitez votre enseignant pour un suivi personnalisé")
    
    return recommendations

def generate_next_steps(total_score):
    """Génère les prochaines étapes selon le niveau"""
    if total_score >= 13:
        return [
            "📚 Approfondir avec le cours Google UX Design Certificate",
            "🎨 Explorer les outils avancés (Principle, ProtoPie, Framer)",
            "👥 Participer à des projets UX en équipe",
            "📝 Contribuer à des design systems existants"
        ]
    elif total_score >= 10:
        return [
            "🔄 Refaire l'atelier avec d'autres contextes métier",
            "📖 Lire 'Don't Make Me Think' de Steve Krug",
            "🎯 Pratiquer le prototypage sur des apps existantes",
            "📱 S'entraîner au design mobile-first"
        ]
    else:
        return [
            "🔄 Reprendre l'atelier en utilisant tous les supports",
            "📚 Revoir les bases UX avec les ressources fournies",
            "👨‍🏫 Planifier une session de rattrapage avec l'enseignant",
            "💻 Pratiquer Figma avec les tutoriels officiels"
        ]

def generate_feedback_markdown():
    """Génère le feedback complet en markdown"""
    results = load_all_results()
    scores = calculate_total_score(results)
    total_score = sum(scores.values())
    level_info = get_level_description(total_score)
    recommendations = generate_recommendations(scores, results)
    next_steps = generate_next_steps(total_score)
    
    # Récupération info étudiant
    student_info = {}
    for phase_data in results.values():
        if phase_data and 'etudiant' in phase_data:
            student_info = phase_data['etudiant']
            break
    
    # Génération du markdown
    markdown = f"""# 🎯 Feedback Atelier Figma TechSolutions

## 👤 Étudiant
**Nom** : {student_info.get('nom', 'Non renseigné')}
**Email** : {student_info.get('email', 'Non renseigné')}
**Date** : {datetime.now().strftime('%d/%m/%Y %H:%M')}

## 📊 Résultats détaillés

### Scores par phase :
- **Phase 1 - Analyse UX** : {scores['phase1']}/4 ({'✅' if scores['phase1'] >= 3 else '⚠️'})
- **Phase 2 - Conception** : {scores['phase2']}/6 ({'✅' if scores['phase2'] >= 4 else '⚠️'})
- **Phase 3 - Présentation** : {scores['phase3']}/3 ({'✅' if scores['phase3'] >= 2 else '⚠️'})
- **QCM Final - Synthèse** : {scores['final']}/4 ({'✅' if scores['final'] >= 3 else '⚠️'})

### 🏆 Score total : {total_score}/17 ({(total_score/17)*100:.0f}%)

## {level_info['niveau']} - {level_info['badge']}

{level_info['description']}

## 💡 Recommandations personnalisées

"""
    
    for i, rec in enumerate(recommendations, 1):
        markdown += f"{i}. {rec}\n"
    
    markdown += f"""
## 🚀 Prochaines étapes

"""
    
    for i, step in enumerate(next_steps, 1):
        markdown += f"{i}. {step}\n"
    
    markdown += f"""
## 📚 Ressources pour approfondir

### 🎯 Selon vos points faibles :
"""
    
    if scores['phase1'] < 3:
        markdown += "- **[Guide méthodologie UX avancé](docs/guide_methodologie_ux_avance.md)** - Personas et customer journey maps\n"
    
    if scores['phase2'] < 4:
        markdown += "- **[Patterns d'interface](ressources/patterns_interface.md)** - Composants essentiels mobile\n"
        markdown += "- **[Charte graphique](ressources/charte_graphique.md)** - Couleurs et styles TechSolutions\n"
    
    if scores['phase3'] < 2:
        markdown += "- **[Bonnes pratiques UX/UI](docs/bonnes_pratiques_ux_ui.md)** - Lois et principes design\n"
    
    markdown += """
### 🌐 Ressources externes :
- **Figma Academy** : [figma.com/academy](https://figma.com/academy)
- **Laws of UX** : [lawsofux.com](https://lawsofux.com)
- **Google UX Design Certificate** : [coursera.org](https://coursera.org)

---

💡 **Conseil** : Gardez ce feedback et utilisez-le pour votre plan de progression personnel !

🔄 **Relance** : Vous pouvez refaire l'atelier à tout moment pour améliorer votre score.
"""
    
    return markdown

if __name__ == "__main__":
    feedback = generate_feedback_markdown()
    
    with open('generated_feedback.md', 'w', encoding='utf-8') as f:
        f.write(feedback)
    
    print("✅ Feedback personnalisé généré avec succès !")
    print(f"📄 Fichier : generated_feedback.md")