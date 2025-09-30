# Atelier Figma TechSolutions

## 📋 Description du projet

Ce repository contient tous les supports pédagogiques pour l'atelier **"Introduction au Design d'Interfaces avec Figma"** dans le contexte de l'entreprise fictive **TechSolutions**.

L'atelier suit une **méthodologie UX complète** : analyse d'interviews utilisateurs, création de cas d'utilisation, wireframes, design UI et prototypage. Les participants découvrent les bases du design d'interfaces et créent un prototype fonctionnel d'outil de gestion de tickets IT.

## 🎯 Objectifs pédagogiques

- Découvrir **Figma** et ses fonctionnalités principales
- Comprendre les principes fondamentaux du **design d'interfaces**
- Apprendre la **méthodologie UX** : interviews, cas d'utilisation, wireframes
- Créer des **diagrammes de cas d'utilisation** et analyser les besoins utilisateurs
- Réaliser des **prototypes interactifs** basés sur des besoins réels
- Maîtriser les outils de **collaboration** en design
- **Justifier ses choix design** avec des arguments UX

## ⏱️ Planning type (3h15)

| Durée | Activité | Supports à utiliser |
|-------|----------|---------------------|
| 30 min | **Analyse UX** - Interviews, cas d'utilisation, diagrammes | [Dossier étudiant p.1-7](ressources/dossier_etudiant.md) + [QCM Phase 1](qcm/qcm_phase1_analyse_ux.md) |
| 90 min | **Conception** - Wireframes, design UI, prototypage | [Charte graphique](ressources/charte_graphique.md) + [Bonnes pratiques](docs/bonnes_pratiques_ux_ui.md) + [QCM Phase 2](qcm/qcm_phase2_conception.md) |
| 30 min | **Présentation** - Demo des prototypes et justifications | [Grille d'évaluation](ressources/grille_auto_evaluation.md) + [QCM Phase 3](qcm/qcm_phase3_presentation.md) |
| 25 min | **Livraison** - Documentation et synthèse UX | [Template synthèse](ressources/dossier_etudiant.md) + [QCM Final](qcm/qcm_final_synthese.md) |


## 📁 Structure du repository (Nouvelle organisation 2024-2025)

```
├── ressources/                      # 🎓 ÉTUDIANTS - Tout pour l'atelier (3h15)
│   ├── dossier_etudiant.md         # Document principal unique et complet
│   ├── charte_graphique.md         # Identité visuelle TechSolutions
│   ├── exemples_tickets.md         # 3 cas d'usage métier avec implications UX
│   ├── patterns_interface.md       # Patterns essentiels mobile (nouveau)
│   └── grille_auto_evaluation.md   # Outil d'auto-évaluation personnelle
├── qcm/                            # 📝 QCM ET ÉVALUATIONS - Centralisé
│   ├── README.md                   # Guide complet des QCM
│   ├── qcm_phase1_analyse_ux.md    # QCM Phase 1 : Analyse UX (4 questions)
│   ├── qcm_phase2_conception.md    # QCM Phase 2 : Conception (6 questions)
│   ├── qcm_phase3_presentation.md  # QCM Phase 3 : Présentation (3 questions)
│   ├── qcm_final_synthese.md       # QCM Final : Synthèse (4 questions)
│   ├── qcm_enseignant_observation.md # Grille d'observation temps réel
│   └── qcm_intermediaires.md       # QCM complet consolidé
├── docs/                           # 👨‍🏫 ENSEIGNANTS + Approfondissement
│   ├── guide_enseignant.md         # Instructions complètes pour l'animateur
│   ├── guide_correction.md         # Guide détaillé de correction enseignant
│   ├── guide_methodologie_ux_avance.md # Méthodologie UX approfondie avec templates
│   ├── bonnes_pratiques_ux_ui.md   # Recueil des meilleures pratiques avec exemples
│   ├── prototype_exemple_complet.md # Prototype de référence avec justifications
│   ├── veille_technologique.md     # Outils et tendances 2024-2025 (nouveau)
│   └── slides/
│       └── atelier_figma.marp.md  # Présentation avec méthodologie UX enrichie
├── .github/                        # 🤖 GITHUB CLASSROOM - Automatisation
│   └── workflows/
│       ├── autograding.yml         # Tests automatiques des soumissions
│       └── feedback.yml            # Feedback automatique étudiants
├── tests/                          # 🧪 TESTS AUTOMATIQUES
│   └── test_submissions.py         # Validation format JSON étudiants
└── submissions/                    # 📤 TEMPLATES SOUMISSIONS
    └── student_template.json       # Format attendu pour GitHub Classroom
```

### 🎯 **Logique de la nouvelle organisation**
- **`ressources/`** = Tout ce dont les étudiants ont besoin **PENDANT** l'atelier
- **`qcm/`** = **NOUVEAU** - Toutes les évaluations centralisées avec guide d'usage
- **`docs/`** = Préparation enseignant + Approfondissement **APRÈS** l'atelier
- **`.github/`** = **NOUVEAU** - Intégration GitHub Classroom avec tests automatiques

## 📋 QCM et Évaluations

### 🎯 **Répertoire centralisé** : [`qcm/`](qcm/README.md)

**QCM par phase** (étudiants) :
- [`qcm/qcm_phase1_analyse_ux.md`](qcm/qcm_phase1_analyse_ux.md) - **Phase 1** : Analyse UX (4 questions, 5 min)
- [`qcm/qcm_phase2_conception.md`](qcm/qcm_phase2_conception.md) - **Phase 2** : Conception (6 questions, 5 min)  
- [`qcm/qcm_phase3_presentation.md`](qcm/qcm_phase3_presentation.md) - **Phase 3** : Présentation (3 questions, 3 min)
- [`qcm/qcm_final_synthese.md`](qcm/qcm_final_synthese.md) - **Synthèse finale** : Bilan complet (4 questions, 5 min)

**Outils enseignants** :
- [`qcm/qcm_enseignant_observation.md`](qcm/qcm_enseignant_observation.md) - Grille d'observation temps réel
- [`qcm/qcm_intermediaires.md`](qcm/qcm_intermediaires.md) - QCM complet consolidé

**📊 Total** : 17 questions (4+6+3+4) - **18 minutes** d'évaluation

## 🎓 Utilisation des supports

### Documents principaux étudiants
- **[dossier_etudiant.md](ressources/dossier_etudiant.md)** : Document unique et complet contenant :
  - Contexte métier avec 4 interviews détaillées
  - Méthodologie UX étape par étape
  - Mémento Figma avec raccourcis et glossaire
  - Aide-mémoire pratique avec exemples
  - Critères d'évaluation détaillés
- **[patterns_interface.md](ressources/patterns_interface.md)** : Patterns essentiels pour l'atelier
- **[exemples_tickets.md](ressources/exemples_tickets.md)** : 3 cas d'usage avec implications UX
- **[grille_auto_evaluation.md](ressources/grille_auto_evaluation.md)** : Suivi personnel de progression

### Supports enseignant
- **[guide_enseignant.md](docs/guide_enseignant.md)** : Guide complet avec planning détaillé, grille d'évaluation, conseils pratiques
- **[guide_correction.md](docs/guide_correction.md)** : Correction détaillée avec barème et exemples
- **[slides/atelier_figma.marp.md](docs/slides/atelier_figma.marp.md)** : Présentation avec exemples visuels et méthodologie UX

### Supports pédagogiques avancés
- **[guide_methodologie_ux_avance.md](docs/guide_methodologie_ux_avance.md)** : Méthodologie UX approfondie avec :
  - Templates de personas et customer journey maps
  - Techniques d'idéation et de test utilisateur
  - Métriques UX et processus d'itération
- **[bonnes_pratiques_ux_ui.md](docs/bonnes_pratiques_ux_ui.md)** : Recueil des meilleures pratiques avec :
  - Lois de l'UX appliquées (Fitts, Hick, Miller)
  - Patterns d'interface efficaces
  - Guidelines responsive et accessibilité
- **[prototype_exemple_complet.md](docs/prototype_exemple_complet.md)** : Prototype de référence avec :
  - Analyse UX détaillée et justifiée
  - Wireframes et design system appliqué
  - Tests utilisateurs et métriques de succès

## 📱 Projet à réaliser

Les participants créent l'interface d'une **application mobile** pour **TechSolutions**, une entreprise de services informatiques.

### Fonctionnalités à développer
- 🏠 **Page d'accueil** avec présentation des services
- 📞 **Page contact** avec formulaire et informations
- 👤 **Espace utilisateur** avec profil et historique
- 🎫 **Gestion des tickets** de support

### Livrables attendus
- **Analyse UX** : cas d'utilisation et diagrammes
- **Maquettes** haute fidélité (3 écrans minimum) basées sur les besoins utilisateurs
- **Prototype** interactif avec navigation
- **Documentation** : justification des choix design (2 pages)
- **Système de design** cohérent (couleurs, typographies, composants)

## 🎨 Charte graphique

### Couleurs principales
- **Bleu principal** : `#2563EB`
- **Vert secondaire** : `#10B981`
- **Gris neutre** : `#6B7280`

### Typographies
- **Titres** : Montserrat (Bold)
- **Corps** : Inter (Regular)

### Style
- Design moderne et professionnel
- Interface épurée et fonctionnelle
- Accessibilité prioritaire

## 🚀 Mise en route

### Pour les enseignants

1. **Préparer l'atelier** :
   - [ ] Lire le [guide enseignant](docs/guide_enseignant.md) (planning, évaluation, conseils)
   - [ ] Consulter la [méthodologie UX avancée](docs/guide_methodologie_ux_avance.md) pour approfondir
   - [ ] Réviser les [bonnes pratiques UX/UI](docs/bonnes_pratiques_ux_ui.md) avec exemples
   - [ ] Préparer les [QCM par phase](qcm/README.md) pour validation en temps réel
   - [ ] Consulter la [grille d'observation](qcm/qcm_enseignant_observation.md) pour suivi temps réel
   - [ ] Étudier le [prototype exemple](docs/prototype_exemple_complet.md) de référence
   - [ ] Réviser la [présentation](docs/slides/atelier_figma.marp.md)
   - [ ] Vérifier que tous les étudiants ont un compte Figma
   - [ ] Configurer GitHub Classroom avec ce repository

2. **Le jour J** :
   - Distribuer le [dossier étudiant](ressources/dossier_etudiant.md) (document principal)
   - Utiliser les [QCM par phase](qcm/README.md) après chaque étape (5 min chacun)
   - Distribuer la [grille d'auto-évaluation](ressources/grille_auto_evaluation.md) pour suivi personnel
   - Suivre le planning détaillé du guide enseignant

### Pour les étudiants

1. **Avant l'atelier** :
   - [ ] Créer un compte [Figma](https://figma.com) (gratuit)
   - [ ] Télécharger le [dossier étudiant](ressources/dossier_etudiant.md)
   - [ ] Consulter les [exemples de tickets](ressources/exemples_tickets.md)

2. **Pendant l'atelier** :
   - Suivre le [dossier étudiant](ressources/dossier_etudiant.md) étape par étape
   - Utiliser la [charte graphique](ressources/charte_graphique.md) pour cohérence
   - Valider sa compréhension avec les [QCM par phase](qcm/README.md)
   - S'auto-évaluer avec la [grille personnelle](ressources/grille_auto_evaluation.md)

## 🌐 GitHub Classroom - Évaluation automatique

### 📖 **Qu'est-ce que l'autograding ?**

L'**autograding** (évaluation automatique) permet de donner un **feedback immédiat** aux étudiants quand ils soumettent leur travail. GitHub Actions exécute automatiquement des **tests Python** qui vérifient :

- ✅ **Structure** : Format JSON respecté, sections présentes
- ✅ **Contenu UX** : Personas, wireframes, design system
- ✅ **Liens Figma** : Prototypes accessibles et valides  
- ✅ **QCM** : Réponses complètes aux 4 phases
- ✅ **Auto-évaluation** : Grille personnelle remplie

### 🎯 **Configuration enseignant**

1. **Créer l'assignment** GitHub Classroom avec ce repository
2. **Distribuer le lien** aux étudiants (ils obtiennent leur copie privée)
3. **Les tests s'exécutent automatiquement** à chaque soumission
4. **Consulter les résultats** dans l'onglet "Actions" de chaque repo étudiant

#### 📋 **Barème automatique** (100 points total)

| Test | Description | Points |
|------|-------------|--------|
| **Structure JSON** | Validation format soumission | 20 pts |
| **Contenu UX** | Personas, wireframes, design system | 30 pts |
| **Liens Figma** | URLs prototypes valides | 25 pts |
| **Réponses QCM** | Complétude des 4 phases | 15 pts |
| **Auto-évaluation** | Grille personnelle | 10 pts |

### 🎓 **Workflow étudiant**

1. **Accepter l'assignment** via le lien GitHub Classroom
2. **Cloner** le repository personnel généré
3. **Travailler** sur Figma pendant l'atelier
4. **Compléter** le fichier `submissions/my_submission.json`
5. **Commit/Push** → Tests automatiques déclenchés
6. **Voir le résultat** dans l'onglet "Actions" (✅ ou ❌)
7. **Corriger** si nécessaire et re-soumettre

### 💡 **Avantages pour l'enseignant**

- 🚀 **Gain de temps** : Correction automatique de la structure
- 📊 **Métriques instantanées** : Vue d'ensemble des soumissions
- 🎯 **Focus sur l'essentiel** : Plus de temps pour le feedback qualitatif
- 📈 **Suivi temps réel** : Voir qui a soumis, qui a des erreurs
- 🔄 **Amélioration continue** : Ajuster les tests selon les besoins

### 🛠️ **Tests disponibles**

#### **1. Structure JSON** (20 points)
```bash
python tests/test_submissions.py --test structure
```
Vérifie : sections requises, informations étudiant, format valide

#### **2. Contenu UX** (30 points)
```bash
python tests/test_submissions.py --test ux_content
```  
Vérifie : personas (2+), cas d'utilisation (3+), wireframes (3+), design system

#### **3. Liens Figma** (25 points)
```bash
python tests/test_submissions.py --test figma_links
```
Vérifie : URLs Figma valides, prototype accessible

#### **4. Réponses QCM** (15 points)
```bash
python tests/test_submissions.py --test qcm_answers
```
Vérifie : réponses aux 4 phases, complétude

#### **5. Auto-évaluation** (10 points)
```bash
python tests/test_submissions.py --test self_evaluation
```
Vérifie : grille personnelle remplie, scores cohérents

### ⚙️ **Personnalisation des tests**

Vous pouvez modifier `tests/test_submissions.py` pour :
- Ajuster les **critères de validation**
- Modifier le **barème de points**
- Ajouter de **nouveaux tests**
- Personnaliser les **messages d'erreur**

### 🆘 **Résolution des problèmes courants**

**❌ Test failed: Structure JSON**
→ Vérifier que `submissions/my_submission.json` existe et est valide

**❌ Test failed: Contenu UX** 
→ S'assurer d'avoir 2+ personas, 3+ wireframes, design system

**❌ Test failed: Liens Figma**
→ URLs Figma doivent être publiques et accessibles

**❌ Test failed: QCM**
→ Répondre aux QCM des 4 phases dans le JSON

### Intégration automatisée

Ce repository est **compatible GitHub Classroom** avec :

- **Tests automatiques** : Validation format JSON des soumissions étudiants
- **Feedback instantané** : Retours automatiques sur la structure des livrables
- **Template soumission** : Format standardisé pour les rendus
- **Workflows GitHub Actions** : Correction automatique et métriques

### Configuration enseignant

1. **Créer l'assignment** GitHub Classroom avec ce repository
2. **Activer les tests** automatiques (`.github/workflows/`)
3. **Personnaliser** le template de soumission (`submissions/student_template.json`)
4. **Configurer** les notifications de feedback automatique

### Utilisation étudiants

1. **Accepter l'assignment** via lien GitHub Classroom
2. **Cloner** le repository personnel généré
3. **Compléter** le fichier `submissions/my_submission.json`
4. **Commit/Push** pour déclencher les tests automatiques
5. **Recevoir** le feedback instantané via GitHub

## 🛠️ Outils utilisés

- **[Figma](https://figma.com)** - Design et prototypage
- **[Marp](https://marp.app)** - Création de slides
- **[GitHub Classroom](https://classroom.github.com)** - Gestion des devoirs et tests automatiques

## 📚 Ressources complémentaires

### Documentation officielle
- [Figma Help Center](https://help.figma.com/)
- [Figma Academy](https://www.figma.com/academy/)
- [Figma Community](https://www.figma.com/community/)

### Inspiration design
- [Dribbble](https://dribbble.com) - Inspiration UI/UX
- [Behance](https://behance.net) - Portfolios design
- [UI Movement](https://uimovement.com) - Animations interface

### Veille technologique
- Consultez [veille_technologique.md](docs/veille_technologique.md) pour les dernières tendances

---

## 🤝 Contributions

Les contributions sont les bienvenues ! N'hésitez pas à :
- Proposer des améliorations via Issues
- Soumettre des Pull Requests
- Partager vos retours d'expérience

---

