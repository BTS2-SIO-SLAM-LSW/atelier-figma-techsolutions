# 🎓 Instructions pour les étudiants - Atelier Figma

## 🚀 Comment soumettre votre travail

### **Étape 1 : Fork du repository** (5 min)

1. **Aller sur** : https://github.com/BTS2-SIO-SLAM-LSW/atelier-figma-techsolutions
2. **Cliquer sur "Fork"** (bouton en haut à droite)
3. **Créer le fork** sur votre compte personnel
4. ✅ Vous avez maintenant **votre propre copie** du projet !

### **Étape 2 : Cloner sur votre ordinateur** (5 min)

```bash
# Dans votre terminal
git clone https://github.com/VOTRE_USERNAME/atelier-figma-techsolutions.git
cd atelier-figma-techsolutions
```

### **Étape 3 : Travailler sur Figma** (3h - pendant l'atelier)

- 🎨 Créez vos **personas**
- ✏️ Dessinez vos **wireframes**
- 🎯 Créez votre **design system**
- 🔗 Faites votre **prototype interactif**
- 📝 Répondez aux **QCM** pendant l'atelier

### **Étape 4 : Remplir le fichier de soumission** (30 min)

1. **Ouvrir** le fichier `submissions/student_template.json`
2. **Copier/Renommer** en `submissions/my_submission.json`
3. **Remplir TOUTES les sections** avec VOS données :
   - Vos informations personnelles
   - Liens vers votre projet Figma
   - Vos réponses aux QCM
   - Votre auto-évaluation

**⚠️ IMPORTANT** : Remplacez TOUS les exemples par vos vraies données !

### **Étape 5 : Enregistrer vos modifications** (5 min)

```bash
# Ajouter votre fichier
git add submissions/my_submission.json

# Commit avec votre nom
git commit -m "✅ Soumission: NOM Prénom - Atelier Figma"

# Envoyer sur GitHub
git push origin main
```

### **Étape 6 : Vérifier les tests automatiques** (2 min)

1. **Aller sur VOTRE fork** sur GitHub
2. **Cliquer sur l'onglet "Actions"**
3. **Voir les résultats** des tests :
   - ✅ Tests réussis = Tout est OK !
   - ❌ Tests échoués = Voir les détails et corriger

**Si tests échoués** : Corrigez, puis refaites Étape 5

### **Étape 7 : Créer la Pull Request** (5 min)

1. **Sur VOTRE fork**, cliquer **"Contribute"** → **"Open pull request"**
2. **Titre** : `Soumission atelier - NOM Prénom`
3. **Description** : Ajouter un commentaire sur votre travail (optionnel)
4. **Cliquer "Create pull request"**

✅ **C'EST TERMINÉ !** Votre professeur recevra votre travail !

---

## 📊 **Barème (100 points automatiques)**

Les tests automatiques vérifient :

| Test | Points | Critères |
|------|--------|----------|
| **Structure JSON** | 20 pts | Fichier valide, sections présentes |
| **Contenu UX** | 30 pts | 2+ personas, 3+ wireframes, design system |
| **Liens Figma** | 25 pts | Prototype accessible et valide |
| **QCM** | 15 pts | Réponses aux 4 phases |
| **Auto-évaluation** | 10 pts | Grille personnelle remplie |

---

## 🆘 **Problèmes fréquents**

### ❌ "Test Structure JSON failed"
**Solution** : Vérifier que `submissions/my_submission.json` existe et est un JSON valide

### ❌ "Test Contenu UX failed"  
**Solution** : Vérifier d'avoir au minimum :
- 2 personas
- 3 wireframes
- Design system (couleurs + typographie)

### ❌ "Test Liens Figma failed"
**Solution** : Vérifier que votre lien Figma :
- Commence par `https://www.figma.com/`
- Est **PUBLIC** (permissions de partage)

### ❌ "Git push rejected"
**Solution** : 
```bash
git pull origin main
git push origin main
```

---

## 📚 **Ressources disponibles**

Pendant l'atelier, consultez :

- 📖 **[Dossier étudiant](ressources/dossier_etudiant.md)** : Guide complet
- 🎨 **[Charte graphique](ressources/charte_graphique.md)** : Couleurs et typo TechSolutions
- 📝 **[QCM Phase 1](qcm/qcm_phase1_analyse_ux.md)** : Validation analyse UX
- 📝 **[QCM Phase 2](qcm/qcm_phase2_conception.md)** : Validation conception
- 📝 **[QCM Phase 3](qcm/qcm_phase3_presentation.md)** : Validation présentation
- 📝 **[QCM Final](qcm/qcm_final_synthese.md)** : Synthèse globale

---

## ⏰ **Timeline recommandée**

| Temps | Activité |
|-------|----------|
| 0-10 min | Fork + Clone du repository |
| 10-40 min | **Phase 1** : Analyse UX + QCM 1 |
| 40-130 min | **Phase 2** : Conception + QCM 2 |
| 130-160 min | **Phase 3** : Présentation + QCM 3 |
| 160-185 min | **Phase 4** : Documentation + QCM final |
| 185-195 min | Remplir `my_submission.json` |
| 195-200 min | Commit/Push + Pull Request |

---

**📧 Questions ?** Contactez votre enseignant ou consultez la documentation complète dans le repository.

**🎯 Bon courage pour l'atelier !** 🚀