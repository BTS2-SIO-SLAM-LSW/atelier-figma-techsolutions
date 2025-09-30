# 📝 QCM - Atelier Figma TechSolutions

## 🎯 Organisation des évaluations

Ce répertoire contient **tous les QCM** et outils d'évaluation de l'atelier, organisés par usage et format.

---

## 📋 QCM par Phase (Étudiants)

### 🎓 **Usage pendant l'atelier**

| Fichier | Phase | Questions | Temps | Usage |
|---------|--------|-----------|-------|--------|
| [qcm_phase1_analyse_ux.md](qcm_phase1_analyse_ux.md) | **Analyse UX** | 4 | 5 min | Validation après 30 min d'analyse |
| [qcm_phase2_conception.md](qcm_phase2_conception.md) | **Conception** | 6 | 5 min | Validation après 90 min de prototypage |
| [qcm_phase3_presentation.md](qcm_phase3_presentation.md) | **Présentation** | 3 | 3 min | Validation après présentation |
| [qcm_final_synthese.md](qcm_final_synthese.md) | **Synthèse** | 4 | 5 min | Bilan complet de l'atelier |

### ✅ **Scoring total** : 17 points (4+6+3+4)

---

## 👨‍🏫 QCM Enseignants

### 📊 **Outils pédagogiques**

| Fichier | Usage | Description |
|---------|--------|-------------|
| [qcm_enseignant_observation.md](qcm_enseignant_observation.md) | **Observation temps réel** | Grille de suivi pendant l'atelier |
| [qcm_intermediaires.md](qcm_intermediaires.md) | **QCM complet** | Version consolidée avec tous les QCM |

---

## 🤖 GitHub Classroom - Auto-évaluation

### � **Tests automatiques intégrés**

| Test | Description | Points | Critères |
|------|-------------|--------|----------|
| **Structure JSON** | Validation format soumission | 20 | Sections requises, info étudiant |
| **Contenu UX** | Vérification livrables UX | 30 | Personas, wireframes, design system |
| **Liens Figma** | Validation URLs prototypes | 25 | Liens valides et accessibles |
| **Réponses QCM** | Complétude des QCM | 15 | Réponses aux 4 phases |
| **Auto-évaluation** | Grille personnelle remplie | 10 | Tous les critères documentés |

### ✅ **Total** : 100 points - **Feedback instantané**

---

## 🎯 Modes d'utilisation

### 📱 **Mode autonome** (Recommandé)
- ✅ **QCM individuels** par phase
- 🎯 **Auto-correction** immédiate
- 💡 **Conseils** de rattrapage intégrés
- 📊 **Progression** étape par étape

### 👥 **Mode guidé enseignant**
- 📋 **QCM complet** avec toutes les phases
- 👁️ **Observation** temps réel
- 🚨 **Alertes** et interventions
- 📈 **Métriques** d'atelier

### 🤖 **Mode GitHub Classroom** (Recommandé)
- � **Tests automatiques** avec scoring détaillé
- 🔄 **Feedback instantané** via GitHub Actions
- � **Métriques** de progression automatisées
- � **Workflow** de correction optimisé

---

## 📊 Utilisation recommandée

### 🎓 **Pour les étudiants** :

1. **Pendant l'atelier** :
   - Utilisez les QCM individuels phase par phase
   - Auto-corrigez immédiatement
   - Suivez les conseils de rattrapage si besoin

2. **Version PDF** :
   - Téléchargez pour usage hors ligne
   - Imprimez si besoin (format A4 optimisé)
   - Gardez comme référence post-atelier

### 👨‍🏫 **Pour les enseignants** :

1. **Préparation** :
   - Consultez `qcm_enseignant_observation.md`
   - Préparez les interventions types
   - Configurez les exports LMS si besoin

2. **Animation** :
   - Utilisez la grille d'observation temps réel
   - Intervenez selon les alertes définies
   - Collectez les métriques pour amélioration

3. **Suivi** :
   - Analysez les résultats globaux
   - Identifiez les points d'amélioration
   - Adaptez l'atelier pour prochaines sessions

---

## 🔄 Maintenance et évolution

### 📝 **Mise à jour** :
- **Questions** : Ajustement selon retours étudiants
- **Explications** : Amélioration pédagogique continue
- **Formats** : Nouveaux exports selon besoins

### 📈 **Métriques de qualité** :
- **Taux de réussite** par question
- **Temps de complétion** moyen
- **Points de blocage** fréquents
- **Satisfaction** étudiante

### 🎯 **Roadmap** :
- [ ] QCM adaptatifs selon niveau étudiant
- [ ] Integration GitHub Classroom complète
- [ ] Exports automatiques multi-plateformes
- [ ] Analytics avancés avec dashboards

---

## 📚 Documentation technique

### 🔗 **Liens utiles** :
- **GitHub Classroom** : [classroom.github.com](https://classroom.github.com/)
- **GitHub Actions** : [docs.github.com/actions](https://docs.github.com/en/actions)
- **Autograding** : [docs.github.com/classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/use-autograding)

### 🛠️ **Configuration autograding** :
```yaml
# .github/workflows/autograding.yml
name: Autograding Tests
env:
  PYTHON_VERSION: 3.8
on:
  push:
  repository_dispatch:
```

### 🐍 **Tests Python** :
```bash
# Exécution locale des tests
python tests/test_submissions.py --test structure
python tests/test_submissions.py --test ux_content
python tests/test_submissions.py --test figma_links
```

---

*📝 Répertoire maintenu par l'équipe pédagogique - Dernière mise à jour : 30/09/2025*