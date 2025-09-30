# 📊 Guide Rapide : Récupération Automatique des Notes

## 🎯 Vue d'ensemble

**GitHub Classroom fait TOUT automatiquement !** Vous n'avez qu'à :
1. ✅ Télécharger les travaux (1 clic)
2. ✅ Consulter les scores (déjà calculés)
3. ✅ Ajouter votre note créative

---

## 📥 Récupération automatique des notes

### **Option 1 : Directement dans GitHub Classroom** ⭐ **RECOMMANDÉ**

#### **Tableau de bord automatique**

1. **Aller sur** [classroom.github.com](https://classroom.github.com)
2. **Sélectionner** "Atelier Figma TechSolutions"
3. **Cliquer** sur l'onglet **"Submissions"** ou **"Students"**

#### **Ce que vous voyez automatiquement :**

```
┌─────────────────────────────────────────────────────────────┐
│ TABLEAU DE BORD GITHUB CLASSROOM                            │
├─────────────┬──────────────┬──────────┬─────────────────────┤
│ Étudiant    │ Status       │ Score    │ Actions             │
├─────────────┼──────────────┼──────────┼─────────────────────┤
│ Alice Dupont│ ✅ Submitted │ 98/100   │ View │ Grade │ Repo │
│ Bob Martin  │ ✅ Submitted │ 85/100   │ View │ Grade │ Repo │
│ Charlie D.  │ ⚠️ Failed    │ 45/100   │ View │ Grade │ Repo │
│ Diana Lopez │ ❌ Not started│ -/100   │ View │ Grade │ Repo │
└─────────────┴──────────────┴──────────┴─────────────────────┘
```

#### **Détail des scores automatiques :**

Pour chaque étudiant, cliquez sur **"View"** :

```
┌──────────────────────────────────────────────┐
│ 🎓 Alice Dupont - Détail des tests           │
├──────────────────────────┬─────────┬─────────┤
│ Test                     │ Points  │ Status  │
├──────────────────────────┼─────────┼─────────┤
│ Structure JSON           │ 20/20   │ ✅ Pass │
│ Contenu UX               │ 28/30   │ ✅ Pass │
│ Liens Figma              │ 25/25   │ ✅ Pass │
│ Réponses QCM             │ 15/15   │ ✅ Pass │
│ Auto-évaluation          │ 10/10   │ ✅ Pass │
├──────────────────────────┼─────────┼─────────┤
│ TOTAL AUTOMATIQUE        │ 98/100  │ ✅      │
└──────────────────────────┴─────────┴─────────┘
```

#### **Actions disponibles :**

- 🔍 **"View"** : Voir les détails des tests
- 📝 **"Grade"** : Ajouter votre note manuelle
- 🔗 **"Repo"** : Accéder au repository étudiant

---

### **Option 2 : Export CSV pour tableur** 📊

Si vous voulez traiter les données dans Excel/Google Sheets :

#### **1. Export depuis GitHub Classroom**

1. **Onglet "Submissions"**
2. **Cliquer "Export grades"** (bouton en haut)
3. **Télécharger** le fichier `grades.csv`

#### **2. Le CSV contient :**

```csv
student_name,github_username,assignment_status,points_earned,points_available
Alice Dupont,alice-dupont,submitted,98,100
Bob Martin,bob-martin,submitted,85,100
Charlie Durand,charlie-durand,submitted,45,100
```

#### **3. Compléter avec vos notes**

Ouvrez dans Excel et ajoutez vos colonnes :

| Nom | Score Auto | Qualité Figma | Note Finale |
|-----|------------|---------------|-------------|
| Alice | 98/100 | 85/100 | 91.5/100 |
| Bob | 85/100 | 90/100 | 87.5/100 |
| Charlie | 45/100 | 60/100 | 52.5/100 |

---

### **Option 3 : Script d'extraction détaillée QCM** 🐍

Pour une analyse détaillée des réponses QCM :

#### **Commande :**

```bash
# 1. Télécharger tous les repos depuis GitHub Classroom
#    (bouton "Download all repositories")

# 2. Dézipper le fichier téléchargé

# 3. Lancer le script
python scripts/extract_qcm_results.py ./atelier-figma-assignments
```

#### **Résultat : Fichier CSV détaillé**

```csv
nom,prenom,email,score_qcm,p1_q1,p1_q2,p1_q3,p1_q4,p2_q1,...
Dupont,Alice,alice@ecole.fr,17/17,B,A,C,B,A,...
Martin,Bob,bob@ecole.fr,15/17,B,A,C,A,A,...
```

**Avantage** : Voir question par question les réponses de chaque étudiant

---

## 🎯 Notation finale recommandée

### **Barème suggéré :**

| Composante | Points | Comment |
|------------|--------|---------|
| **Tests automatiques** | 50 pts | GitHub Classroom calcule |
| **Qualité créative Figma** | 50 pts | Vous évaluez manuellement |
| **TOTAL** | 100 pts | Note finale |

### **Évaluation manuelle Figma :**

Pour chaque étudiant, ouvrez ses liens Figma et évaluez :

| Critère | Points |
|---------|--------|
| Qualité des personas | /10 |
| Pertinence UX | /15 |
| Design esthétique | /15 |
| Prototypage (interactions) | /10 |

---

## ⚡ Workflow rapide de correction

### **Pour 30 étudiants = 30 minutes de correction**

1. **Ouvrir GitHub Classroom** (5 sec)
2. **Pour CHAQUE étudiant** (1 min par étudiant) :
   - Voir le score auto (déjà affiché)
   - Cliquer sur le lien Figma
   - Noter la qualité créative /50
   - Cliquer "Grade" et entrer la note finale

**Temps total** : 30 min pour toute la classe !

---

## 📊 Statistiques automatiques

GitHub Classroom vous donne automatiquement :

- **Taux de soumission** : X/30 étudiants
- **Score moyen** : XX/100
- **Répartition** : Graphique des notes
- **Temps de soumission** : Qui a rendu à l'heure

---

## 🆘 FAQ

### **Q : Les scores automatiques sont-ils fiables ?**
✅ OUI ! Les tests Python vérifient :
- Structure JSON valide
- Présence de tous les livrables
- Liens Figma accessibles
- Réponses QCM complètes

### **Q : Dois-je installer Python ?**
❌ NON ! GitHub Actions exécute tout automatiquement dans le cloud

### **Q : Les étudiants peuvent-ils tricher ?**
✅ Difficile ! Chaque étudiant a son propre repository privé

### **Q : Puis-je modifier les tests ?**
✅ OUI ! Modifiez `tests/test_submissions.py` selon vos critères

### **Q : Comment gérer les retards ?**
✅ GitHub Classroom affiche la date/heure de chaque commit

---

## ✅ Checklist de correction

- [ ] Ouvrir GitHub Classroom
- [ ] Consulter l'onglet "Submissions"
- [ ] Vérifier les scores automatiques (déjà calculés)
- [ ] Pour chaque étudiant :
  - [ ] Voir le score auto /100
  - [ ] Ouvrir les liens Figma
  - [ ] Noter la qualité créative /50
  - [ ] Entrer la note finale
- [ ] Exporter les notes finales (CSV)
- [ ] Importer dans votre système de notes

**⏱️ Temps total : 30-45 minutes pour 30 étudiants**

---

## 🎉 Résumé

**GitHub Classroom fait 90% du travail automatiquement !**

Vous n'avez qu'à :
1. ✅ Consulter les scores calculés
2. ✅ Évaluer la créativité sur Figma
3. ✅ Entrer la note finale

**C'est tout !** 🚀

---

*Pour plus de détails, consultez `docs/guide_enseignant.md`*