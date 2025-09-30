# 👨‍🏫 Guide Enseignant - Workflow Simple (sans GitHub Classroom)

## 🎯 Vue d'ensemble

Ce guide explique comment utiliser le système d'évaluation automatique **sans configurer GitHub Classroom**.

### **Principe simple :**
1. **Étudiants** font un Fork du repository
2. **Ils travaillent** sur leur copie personnelle  
3. **Tests automatiques** s'exécutent sur leur fork
4. **Ils créent une Pull Request** pour soumettre
5. **Vous reviewez** les PR et donnez la note finale

---

## 🚀 Configuration initiale (15 min - une seule fois)

### **Étape 1 : Préparer le repository**

Votre repository est déjà prêt ! Il contient :
- ✅ Tests automatiques (`.github/workflows/autograding.yml`)
- ✅ Template de soumission (`submissions/student_template.json`)
- ✅ Documentation complète

### **Étape 2 : Distribuer les instructions**

1. **Partager le lien** du repository : 
   ```
   https://github.com/BTS2-SIO-SLAM-LSW/atelier-figma-techsolutions
   ```

2. **Distribuer** le fichier `INSTRUCTIONS_ETUDIANTS.md` :
   - Par email
   - Sur votre ENT/Moodle
   - En version imprimée

### **Étape 3 : Expliquer le workflow** (5 min en cours)

Expliquez aux étudiants :
- **Fork** : Créer leur copie personnelle
- **Travail** : Remplir `my_submission.json` avec leurs livrables
- **Tests** : Vérifier automatiquement dans "Actions"
- **Pull Request** : Soumettre pour correction

---

## 📊 Pendant l'atelier (3h15)

### **Votre rôle :**

#### **🔍 Monitoring temps réel**

1. **Demander aux étudiants** de vous envoyer le lien de leur fork
2. **Créer une liste** avec les URLs de leurs repositories
3. **Consulter périodiquement** l'onglet "Actions" de chaque fork

**Exemple de liste :**
```
- Alice: https://github.com/alice/atelier-figma-techsolutions
- Bob: https://github.com/bob/atelier-figma-techsolutions  
- Charlie: https://github.com/charlie/atelier-figma-techsolutions
```

#### **🆘 Interventions ciblées**

Quand un étudiant a des tests qui échouent :

1. **Aller sur son fork** → Onglet "Actions"
2. **Voir les détails** de l'erreur
3. **Intervenir** avec des conseils précis

**Exemples :**
- ❌ "Structure JSON failed" → "Vérifie la syntaxe de ton JSON"
- ❌ "Liens Figma failed" → "Ton lien Figma doit être public"
- ❌ "Contenu UX failed" → "Il te manque des wireframes"

#### **✅ Validation continue**

Les étudiants peuvent **commit/push** plusieurs fois pendant l'atelier :
- Chaque push → Tests automatiques
- Feedback immédiat
- Corrections en temps réel

---

## 📥 Après l'atelier : Correction des Pull Requests

### **Étape 1 : Accéder aux soumissions**

1. **Aller sur votre repository** : https://github.com/BTS2-SIO-SLAM-LSW/atelier-figma-techsolutions
2. **Cliquer sur "Pull requests"**
3. **Voir la liste** de toutes les soumissions étudiantes

### **Étape 2 : Reviewer chaque PR**

Pour chaque Pull Request :

#### **1. Consulter le score automatique**

Dans la PR, onglet "Checks" :
```
✅ Structure JSON: 20/20
✅ Contenu UX: 28/30
✅ Liens Figma: 25/25
✅ QCM: 15/15
✅ Auto-évaluation: 10/10

📊 Score automatique: 98/100
```

#### **2. Vérifier le fichier de soumission**

- **Cliquer "Files changed"**
- **Voir** `submissions/my_submission.json`
- **Consulter** les liens Figma fournis

#### **3. Évaluer la qualité créative** (sur Figma)

Ouvrir les liens Figma de l'étudiant et évaluer :

| Critère | Points | Évaluation |
|---------|--------|------------|
| **Qualité des personas** | /10 | Détail, réalisme |
| **Pertinence UX** | /15 | Analyse besoins, solutions adaptées |
| **Qualité design** | /20 | Esthétique, cohérence visuelle |
| **Prototypage** | /15 | Interactions, fluidité |
| **Originalité** | /5 | Créativité, innovation |

**Total qualité créative : /65**

#### **4. Note finale**

```
Score automatique (structure/complétude) : /100 (35% de la note)
Score qualitatif (créativité/pertinence) : /65 (65% de la note)

Note finale = (Score auto × 0.35) + (Score qualité × 1.0)
```

**Exemple :**
```
Score auto: 98/100 → 98 × 0.35 = 34.3
Score qualité: 52/65

Note finale = 34.3 + 52 = 86.3/100 (17.26/20)
```

#### **5. Donner le feedback**

Dans la Pull Request, **ajouter un commentaire** :

```markdown
## 🎓 Évaluation - Alice Dupont

### ✅ Partie automatique (35%) : 34.3/35
- Structure JSON: 20/20 ✅
- Contenu UX: 28/30 ⚠️ (Journey maps peu détaillés)
- Liens Figma: 25/25 ✅
- QCM: 15/15 ✅
- Auto-évaluation: 10/10 ✅

### 🎨 Partie créative (65%) : 52/65

**Points forts :**
- Personas très détaillés et réalistes
- Design cohérent avec la charte
- Prototype fluide avec bonnes interactions

**Points d'amélioration :**
- Wireframes auraient pu être plus détaillés
- Manque de tests utilisateurs documentés
- Quelques problèmes de contraste (accessibilité)

### 📊 Note finale : 86.3/100 (17.26/20)

**Commentaire général :** Très bon travail ! Méthodologie UX bien appliquée, 
design soigné. Continue à approfondir les tests utilisateurs pour les prochains projets.

🎉 Félicitations !
```

#### **6. Merger ou Fermer la PR**

- ✅ **Merger** : Si vous voulez garder le travail dans l'historique
- 🔒 **Fermer sans merger** : Si vous voulez juste valider la soumission

---

## 📈 Tableau de suivi (optionnel)

Créez un tableur pour suivre :

| Étudiant | Fork créé | Tests OK | PR créée | Score auto | Score créatif | Note finale |
|----------|-----------|----------|----------|------------|---------------|-------------|
| Alice | ✅ | ✅ | ✅ | 98/100 | 52/65 | 86.3/100 |
| Bob | ✅ | ⚠️ | ✅ | 75/100 | 48/65 | 74.25/100 |
| Charlie | ✅ | ❌ | ❌ | - | - | - |

---

## 🔧 Avantages de cette méthode

### **Pour vous :**
- ✅ **Pas de configuration complexe** GitHub Classroom
- ✅ **Tests automatiques** fonctionnent quand même
- ✅ **Feedback structuré** dans les Pull Requests
- ✅ **Historique complet** de toutes les soumissions
- ✅ **Réutilisable** d'année en année

### **Pour les étudiants :**
- ✅ **Workflow Git réel** (comme en entreprise)
- ✅ **Feedback immédiat** via tests automatiques
- ✅ **Autonomie** : Peuvent tester avant de soumettre
- ✅ **Portfolio** : Leur fork reste sur leur compte GitHub

---

## 🆘 Problèmes courants et solutions

### **Problème : "Étudiant a oublié de faire le Fork"**
**Solution** : Le guider pas à pas, c'est simple à rattraper

### **Problème : "Tests ne s'exécutent pas sur le fork"**
**Solution** : L'étudiant doit activer GitHub Actions dans Settings → Actions

### **Problème : "Pull Request vers le mauvais repository"**
**Solution** : Fermer la PR et guider l'étudiant pour en créer une nouvelle

### **Problème : "Étudiant a modifié les tests"**
**Solution** : Visible dans "Files changed" → Invalider la soumission

---

## 📚 Ressources complémentaires

- **Documentation complète** : `docs/guide_enseignant.md`
- **Correction détaillée** : `docs/guide_correction.md`
- **Grille observation** : `qcm/qcm_enseignant_observation.md`

---

## ✅ Checklist avant l'atelier

- [ ] Repository public et accessible
- [ ] `INSTRUCTIONS_ETUDIANTS.md` distribué
- [ ] Workflow expliqué en 5 minutes
- [ ] Liste des forks étudiants préparée
- [ ] Grille d'évaluation créative prête

---

**🎯 Cette méthode est PLUS SIMPLE que GitHub Classroom et tout aussi efficace !**

*Questions ? Consultez la documentation complète ou testez le workflow vous-même.*