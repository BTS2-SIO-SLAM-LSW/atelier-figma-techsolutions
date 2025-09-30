# 📚 Guide GitHub Classroom - Atelier Figma TechSolutions

## 🎯 Introduction à l'autograding

### Qu'est-ce que l'autograding ?

L'**autograding** (évaluation automatique) est un système qui :
- 🤖 **Teste automatiquement** les soumissions étudiants
- ⚡ **Donne un feedback immédiat** (sans attendre la correction manuelle)
- 📊 **Score automatiquement** selon des critères prédéfinis
- 📈 **Suit la progression** en temps réel

### Pourquoi utiliser l'autograding pour Figma ?

Même si Figma est créatif, on peut automatiser :
- ✅ **Structure** : Le JSON de soumission est-il valide ?
- ✅ **Complétude** : Tous les livrables sont-ils présents ?
- ✅ **Liens** : Les prototypes Figma sont-ils accessibles ?
- ✅ **QCM** : Les validations de connaissances sont-elles remplies ?

---

## 🚀 Configuration initiale

### 1. Créer l'assignment GitHub Classroom

1. **Aller sur** [classroom.github.com](https://classroom.github.com)
2. **Créer un nouvel assignment** 
3. **Sélectionner ce repository** comme template
4. **Activer "Enable feedback pull requests"**
5. **Configurer la deadline** si souhaitée

### 2. Configurer l'autograding

Dans les paramètres de l'assignment :

#### ✅ **Test 1 : Structure JSON** (20 points)
- **Setup command** : (laisser vide)
- **Run command** : `python tests/test_submissions.py --test structure`
- **Timeout** : 5 minutes
- **Points** : 20

#### ✅ **Test 2 : Contenu UX** (30 points)  
- **Setup command** : (laisser vide)
- **Run command** : `python tests/test_submissions.py --test ux_content`
- **Timeout** : 5 minutes
- **Points** : 30

#### ✅ **Test 3 : Liens Figma** (25 points)
- **Setup command** : (laisser vide)
- **Run command** : `python tests/test_submissions.py --test figma_links`
- **Timeout** : 10 minutes
- **Points** : 25

#### ✅ **Test 4 : Réponses QCM** (15 points)
- **Setup command** : (laisser vide)
- **Run command** : `python tests/test_submissions.py --test qcm_answers`
- **Timeout** : 5 minutes
- **Points** : 15

#### ✅ **Test 5 : Auto-évaluation** (10 points)
- **Setup command** : (laisser vide)
- **Run command** : `python tests/test_submissions.py --test self_evaluation`
- **Timeout** : 5 minutes
- **Points** : 10

### 3. Distribuer aux étudiants

1. **Copier le lien d'invitation** généré par GitHub Classroom
2. **L'envoyer aux étudiants** (email, LMS, etc.)
3. **Expliquer le processus** : Ils acceptent → Obtiennent leur repository privé

---

## 📊 Suivi et gestion

### Tableau de bord enseignant

GitHub Classroom fournit :

- 📈 **Vue d'ensemble** : Qui a accepté l'assignment
- ✅ **Statut des tests** : Réussite/échec en temps réel  
- 📊 **Scores automatiques** : Total des points par étudiant
- 📝 **Détails des erreurs** : Pour aider les étudiants

### Consulter les résultats

1. **Dashboard GitHub Classroom** → Vue générale
2. **Repository de chaque étudiant** → Onglet "Actions" → Détails des tests
3. **Pull Requests** → Feedback automatique généré

### Intervention pédagogique

**🟢 Tests réussis** : Étudiant autonome, livrable conforme
**🟡 Tests partiels** : Accompagnement ciblé sur points d'échec
**🔴 Tests échoués** : Intervention prioritaire requise

---

## 🎓 Workflow étudiants

### Étapes pour les étudiants

1. **Accepter l'assignment** via le lien
2. **Cloner leur repository** personnel
3. **Effectuer l'atelier Figma** normalement
4. **Remplir** `submissions/my_submission.json`
5. **Commit & Push** → Tests se déclenchent automatiquement
6. **Consulter les résultats** dans "Actions"
7. **Corriger** si nécessaire et re-soumettre

### Template à remplir

Les étudiants doivent compléter `submissions/student_template.json` avec :

```json
{
  "etudiant_info": { ... },
  "analyse_ux": { 
    "personas": [...],
    "cas_utilisation": [...],
    "journey_maps": { ... }
  },
  "conception": {
    "wireframes": [...],
    "design_system": { ... },
    "composants_ui": [...]
  },
  "prototypage": {
    "lien_prototype": "https://figma.com/...",
    "interactions": [...],
    "tests_utilisateurs": { ... }
  },
  "qcm_responses": { ... },
  "auto_evaluation": { ... }
}
```

---

## 🔧 Personnalisation avancée

### Modifier les critères de test

Éditer `tests/test_submissions.py` :

```python
# Exemple : Changer le nombre minimum de personas
if len(analyse["personas"]) >= 3:  # Au lieu de 2
    self.score += 3
```

### Ajuster le barème

Dans `autograding.yml` :

```yaml
- name: Test Contenu UX
  with:
    max-score: 35  # Au lieu de 30
```

### Ajouter de nouveaux tests

Créer une nouvelle fonction dans `test_submissions.py` :

```python
def test_innovation(self):
    """TEST 6: Critères d'innovation (bonus)"""
    # Votre logique ici
```

### Messages personnalisés

Modifier les messages d'erreur/succès dans le script Python :

```python
print("✅ Excellent travail sur les personas !")
self.errors.append("❌ Il manque des détails dans vos wireframes")
```

---

## 📈 Métriques et analytics

### Données disponibles

- **Taux de réussite** par test
- **Temps de complétion** moyen
- **Erreurs fréquentes** identifiées
- **Progression** dans l'atelier

### Amélioration continue

1. **Analyser les échecs récurrents** → Ajuster l'atelier
2. **Surveiller les temps** → Adapter le planning
3. **Collecter les retours** → Améliorer les tests
4. **Itérer sur les critères** → Affiner l'évaluation

### Rapports pour administration

GitHub Classroom permet d'exporter :
- **Notes finales** (CSV)
- **Détails des soumissions** 
- **Statistiques globales** de l'atelier

---

## 🛠️ Maintenance et troubleshooting

### Problèmes courants

**❌ "Tests failing for all students"**
→ Vérifier que `autograding.yml` est correctement configuré

**❌ "Python dependencies missing"** 
→ S'assurer que `jsonschema` et `requests` sont installés

**❌ "Timeout errors"**
→ Augmenter les timeouts dans la configuration

**❌ "Students can't access their repos"**
→ Vérifier les permissions et invitations GitHub Classroom

### Debug des tests

Exécuter localement :

```bash
# Cloner un repository étudiant
git clone https://github.com/classroom/student-repo

# Tester manuellement
cd student-repo
python tests/test_submissions.py --test structure
```

### Mise à jour du template

Si vous modifiez `student_template.json` :
1. **Mettre à jour** dans le repository template
2. **Informer les étudiants** des changements
3. **Tester** avec un repository de test

---
---

## 🎯 Checklist de déploiement

### Avant le premier cours

- [ ] Assignment GitHub Classroom créé
- [ ] Tests d'autograding configurés
- [ ] Template JSON validé
- [ ] Tests effectués avec un repository de test
- [ ] Instructions étudiants préparées
- [ ] Lien d'invitation généré

### Le jour J

- [ ] Distribuer le lien aux étudiants
- [ ] Expliquer le processus GitHub Classroom
- [ ] Montrer comment consulter les résultats des tests
- [ ] Être disponible pour les problèmes techniques

### Après l'atelier

- [ ] Consulter le dashboard des résultats
- [ ] Identifier les étudiants ayant besoin d'aide
- [ ] Analyser les échecs récurrents
- [ ] Planifier les améliorations pour la prochaine session

---

