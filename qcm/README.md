# 📋 QCM Interactifs - Atelier Figma TechSolutions

## � **Accès principal via GitHub Pages**

### 🚀 **Interface web moderne**
**[🌐 Accéder aux QCM via GitHub Pages](https://bts2-sio-slam-lsw.github.io/atelier-figma-techsolutions)**

Page d'accueil avec navigation guidée et interface moderne pour tous les QCM interactifs.

---

## 🎯 QCM HTML Interactifs

### � **Accès direct aux QCM HTML**

| Phase | Fichier QCM HTML | Questions | Timing |
|-------|------------------|-----------|---------|
| 🔍 **Phase 1 - Analyse UX** | [**🚀 QCM Phase 1**](qcm_phase1_analyse_ux.html) | 4 questions | Après 30 min d'analyse |
| 🎨 **Phase 2 - Conception** | [**🚀 QCM Phase 2**](qcm_phase2_conception.html) | 6 questions | Après 90 min de conception |
| 🎤 **Phase 3 - Présentation** | [**🚀 QCM Phase 3**](qcm_phase3_presentation.html) | 3 questions | Après présentation orale |
| 📊 **Phase 4 - Synthèse** | [**🚀 QCM Final**](qcm_final_synthese.html) | 4 questions | Fin de l'atelier |

### ✨ **Fonctionnalités des QCM HTML**
- ✅ **Validation en temps réel** - Bouton "Valider" activé automatiquement
- 📊 **Score instantané** - Affichage immédiat des résultats
- 💡 **Explications détaillées** - Justifications des bonnes réponses
- 📋 **Génération JSON** - Format compatible GitHub Classroom
- 📱 **Design responsive** - Fonctionne sur mobile et desktop
- 🎨 **Thèmes visuels** - Couleurs spécifiques par phase

---

## 🎯 Instructions pour les Étudiants

### � Méthode recommandée

**🌐 Option 1 : Via GitHub Pages (Recommandé)**
1. Aller sur : `https://bts2-sio-slam-lsw.github.io/atelier-figma-techsolutions`
2. Cliquer sur le QCM de votre phase
3. Interface moderne avec navigation guidée

**🔗 Option 2 : Liens directs HTML**
1. Cliquer directement sur les liens ci-dessus
2. Accès direct aux fichiers HTML

### ✅ Workflow QCM

1. **Répondre aux questions** - Sélectionner les réponses
2. **Valider automatiquement** - Le bouton s'active seul
3. **Consulter les résultats** - Score et explications
4. **Copier le JSON** - Bouton "Copier le JSON"
5. **Coller dans submission.json** - Format GitHub Classroom
6. **Commit et push** - Soumission automatique

---

## 🎯 Planning des QCM

### 📅 Phase 1 - Analyse UX (30 minutes)
**Quand :** Après avoir lu les interviews et analysé les besoins  
**QCM :** [**🔗 Cliquer ici pour le QCM Phase 1**](qcm_phase1_analyse_ux.html)  
**Questions :** 4 questions sur la méthodologie UX  
**Objectif :** Valider votre compréhension des besoins utilisateurs

### 📅 Phase 2 - Conception (90 minutes)  
**Quand :** Après avoir créé votre prototype Figma  
**QCM :** [**🔗 Cliquer ici pour le QCM Phase 2**](qcm_phase2_conception.html)  
**Questions :** 6 questions sur Figma et le design  
**Objectif :** Vérifier vos compétences techniques

### 📅 Phase 3 - Présentation (après présentation)
**Quand :** Juste après votre présentation orale  
**QCM :** [**🔗 Cliquer ici pour le QCM Phase 3**](qcm_phase3_presentation.html)  
**Questions :** 3 questions sur la justification UX  
**Objectif :** Valider votre capacité d'argumentation

### 📅 Phase 4 - Synthèse finale
**Quand :** À la toute fin de l'atelier  
**QCM :** [**🔗 Cliquer ici pour le QCM Final**](qcm_final_synthese.html)  
**Questions :** 4 questions de synthèse globale  
**Objectif :** Bilan complet de vos acquis

---

## 📁 Structure de votre submission.json

Votre fichier `submission.json` doit ressembler à ceci après tous les QCM :

```json
{
  "student_info": {
    "nom": "Votre nom",
    "prenom": "Votre prénom", 
    "email": "votre.email@ecole.fr",
    "date_soumission": "2024-09-30T14:30:00.000Z"
  },
  "qcm_responses": {
    "phase1": {
      "q1_cas_utilisation": "b",
      "q2_interview_thomas": "b",
      "q3_priorisation": "c",
      "q4_acteurs": "c"
    },
    "phase2": {
      "q1_outils_figma": "b",
      "q2_composants_instances": "b",
      "q3_charte_graphique": "b",
      "q4_hierarchie_visuelle": "c",
      "q5_ergonomie_tablette": "c",
      "q6_prototypage": "b"
    },
    "phase3": {
      "q1_justification_ux": "c",
      "q2_loi_fitts": "c",
      "q3_feedback_utilisateur": "c"
    },
    "final": {
      "q1_methodologie_ux": "b",
      "q2_outils_collaboratifs": "b",
      "q3_mesure_succes": "b",
      "q4_iteration_design": "b"
    }
  },
  "scores": {
    "qcm_phase1_score": 4,
    "qcm_phase1_total": 4,
    "qcm_phase2_score": 6,
    "qcm_phase2_total": 6,
    "qcm_phase3_score": 3,
    "qcm_phase3_total": 3,
    "qcm_final_score": 4,
    "qcm_final_total": 4
  },
  "figma_links": {
    "prototype_url": "https://figma.com/proto/VOTRE-LIEN",
    "design_file_url": "https://figma.com/file/VOTRE-LIEN"
  },
  "auto_evaluation": {
    "understanding_level": 4,
    "difficulty_encountered": 2,
    "methodology_application": 5,
    "satisfaction_globale": 4
  }
}
```

---

## ⚡ Workflow Rapide

```bash
# 1. Faire le travail de la phase
[Lire, analyser, concevoir, présenter...]

# 2. Ouvrir le QCM correspondant
Cliquer sur le lien QCM dans ce README

# 3. Répondre et valider
[Cliquer sur les réponses] → [Valider]

# 4. Copier le JSON
[Bouton "Copier le JSON"]

# 5. Mettre à jour submission.json
[Coller dans la section appropriée]

# 6. Commit et push
git add submission.json
git commit -m "QCM Phase X complété"
git push origin main
```

---

## 🎯 Accès Rapide aux QCM

### 🚀 **Liens directs pour chaque phase :**

| 🎯 Phase | 🔗 Lien QCM | ⏱️ Timing |
|----------|-------------|-----------|
| **1️⃣ Analyse UX** | [**📋 QCM Phase 1**](qcm_phase1_analyse_ux.html) | Après analyse (30 min) |
| **2️⃣ Conception** | [**🎨 QCM Phase 2**](qcm_phase2_conception.html) | Après prototypage (90 min) |
| **3️⃣ Présentation** | [**🎤 QCM Phase 3**](qcm_phase3_presentation.html) | Après présentation orale |
| **4️⃣ Synthèse** | [**📊 QCM Final**](qcm_final_synthese.html) | Fin de l'atelier |

---

## 🎯 Conseils pour Réussir

### ✅ Bonnes pratiques :
- 📖 **Lisez bien** les documents ressources avant les QCM
- 🎯 **Prenez votre temps** : pas de limite de temps
- 🔄 **Relisez** vos réponses avant de valider
- 📋 **Copiez le JSON** immédiatement après validation

### ⚠️ Erreurs à éviter :
- ❌ Ne pas copier le JSON → tests échouent
- ❌ Modifier manuellement le JSON → format invalide  
- ❌ Oublier de push → soumission incomplète
- ❌ Faire les QCM sans avoir fait le travail

### 🆘 En cas de problème :
- **JSON invalide** → Recommencez le QCM et utilisez "Copier"
- **Tests échouent** → Vérifiez le format de votre submission.json
- **QCM ne s'ouvre pas** → Utilisez un navigateur récent (Chrome/Firefox)
- **Lien ne fonctionne pas** → Double-cliquez directement sur le fichier .html dans le dossier

---

## 📊 Scoring et Évaluation

### 🎯 Répartition des points QCM :
- **Phase 1** : 4 points (Analyse UX)
- **Phase 2** : 6 points (Conception)  
- **Phase 3** : 3 points (Présentation)
- **Phase 4** : 4 points (Synthèse)
- **TOTAL** : 17 points QCM

### 📈 Interprétation de vos scores :
- **15-17/17** : 🏆 **Excellent** ! Maîtrise complète
- **13-14/17** : 🎯 **Très bien** ! Solides compétences  
- **10-12/17** : ✅ **Bien** ! Objectifs atteints
- **8-9/17** : ⚠️ **Moyen** ! À consolider
- **< 8/17** : 🔄 **Difficultés** ! Demandez de l'aide

---

## 🤖 GitHub Classroom - Auto-évaluation

### 📊 **Tests automatiques intégrés**

| Test | Description | Points | Critères |
|------|-------------|--------|----------|
| **Structure JSON** | Validation format soumission | 20 | Sections requises, info étudiant |
| **Contenu UX** | Vérification livrables UX | 30 | Personas, wireframes, design system |
| **Liens Figma** | Validation URLs prototypes | 25 | Liens valides et accessibles |
| **Réponses QCM** | Complétude des QCM | 15 | Réponses aux 4 phases |
| **Auto-évaluation** | Grille personnelle remplie | 10 | Tous les critères documentés |

### ✅ **Total** : 100 points - **Feedback instantané**

---

## 🎉 Bonne Chance !

Les QCM sont là pour **vous aider à progresser** et **valider vos acquis**. 

**N'hésitez pas à demander de l'aide** si vous rencontrez des difficultés !

---

*💡 **Astuce** : Les explications dans les QCM sont aussi importantes que les points. Elles vous aident à comprendre la méthodologie UX professionnelle !*