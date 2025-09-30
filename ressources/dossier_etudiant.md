# Dossier étudiant – Atelier Figma TechSolutions

## 🔎 Contexte

Vous êtes une équipe de designers juniors recrutés par **TechSolutions**, une ESN spécialisée dans l'infogérance pour PME.

L'entreprise utilise un **outil interne vieillissant** pour gérer les tickets clients. Cet outil présente plusieurs problèmes :

* **40%** des tickets sont mal catégorisés → perte de temps.
* **25%** des techniciens oublient de renseigner des champs critiques (ex. urgence).
* Les nouveaux arrivants mettent **3 semaines** à maîtriser l'outil → manque d'intuitivité.

🎯 **Objectif de la mission** :

* Réduire de **30%** le temps de traitement des tickets.
* Améliorer la satisfaction des techniciens (note cible : **8/10** contre 5/10 actuellement).
* Concevoir une interface plus intuitive, claire et adaptée à un usage sur desktop et tablette.

---

## 🎤 Interviews utilisateurs

### Interview 1 : Marie Dubois - Cheffe du support technique

> *"Actuellement, quand un technicien veut voir ses tickets urgents, il doit cliquer sur 4 menus différents. C'est du temps perdu ! Et ne me parlez pas des nouveaux : ils créent des tickets sans catégorie et on perd 2h à les re-dispatcher."*

**Points clés** :
- Besoin d'un **accès rapide** aux tickets urgents
- **Formation** trop longue pour les nouveaux
- **Re-travail** constant à cause des erreurs de saisie

### Interview 2 : Thomas Martin - Technicien senior (5 ans d'ancienneté)

> *"L'interface actuelle ? C'est un cauchemar. Pour créer un ticket, je dois remplir 12 champs répartis sur 3 onglets. Quand un client est au téléphone et pressé, c'est la galère. Et puis, impossible de voir d'un coup d'œil si mes collègues sont débordés ou disponibles."*

**Points clés** :
- **Création de ticket** trop complexe (12 champs, 3 onglets)
- Besoin de **vision d'ensemble** de la charge d'équipe
- **Urgence** des situations client

### Interview 3 : Sophie Chen - Technicienne junior (3 mois d'ancienneté)

> *"Je galère encore avec l'outil. Parfois j'oublie de cocher 'urgent' et Marie n'est pas contente. Il faudrait que ce soit plus visuel, avec des couleurs ou des alertes. Et aussi, je ne sais jamais quoi mettre dans 'catégorie' vs 'sous-catégorie'."*

**Points clés** :
- Besoin d'**indices visuels** pour l'urgence
- **Confusion** entre catégorie/sous-catégorie
- Manque de **guidage** dans l'interface

### Interview 4 : Julien Moreau - Technicien itinérant

> *"Moi je travaille souvent sur tablette dans les locaux clients. L'interface actuelle n'est pas du tout adaptée : texte trop petit, boutons difficiles à toucher. Et impossible de prendre une photo du problème directement depuis l'outil."*

**Points clés** :
- Usage **mobile/tablette** essentiel
- Besoin d'**ergonomie tactile**
- **Intégration photos** souhaitée

---

## Contraintes
- Compatible desktop + tablette (≥ 1024x768).
- Champs obligatoires : ID client, urgence, catégorie.
- Respect charte graphique TechSolutions.
- Prototype cliquable en 3h maximum.

---

## Livrables attendus
1. **Prototype Figma interactif** :  
   - Écran 1 : tableau de bord tickets.  
   - Écran 2 : détail ticket.  
   - Écran 3 : création de ticket.  
   - Bonus : statistiques.  
2. **Document de synthèse (2 pages)** :
   - Page 1 : Analyse des cas d'utilisation et diagrammes
   - Page 2 : Justification des choix design avec arguments UX

---

## 🛠️ Étapes de travail

### Étape 1 – Analyse et compréhension (30 min)

#### a) Lecture du brief et interviews (15 min)
* Lecture du contexte et des interviews utilisateurs
* Questions/réponses avec le "client" (un étudiant ou l'enseignant joue le rôle de **Marie**, cheffe de support)
* Clarification des besoins prioritaires

#### b) Identification des cas d'utilisation (15 min)
* **Listez les cas d'utilisation principaux** en vous basant sur les interviews :
  - Exemple : "En tant que technicien senior, je veux voir rapidement les tickets urgents non assignés"
  - Exemple : "En tant que nouveau technicien, je veux créer un ticket sans risque d'erreur"
* **Créez un diagramme de cas d'utilisation** simple (acteurs + actions principales)
* **Priorisez** les 3 cas d'utilisation les plus critiques pour le prototype

### Étape 2 – Conception et maquettage (1h30)

#### a) Wireframes et architecture (25 min)
* **Dessinez une première version simplifiée** de l'interface basée sur vos cas d'utilisation
* **Notez les points de friction** de l'ancien outil (trop de clics, infos dispersées…)
* **Définissez la structure générale** : Dashboard, détail ticket, formulaire création

#### b) Design UI (45 min)
* **Appliquez la charte graphique** TechSolutions (couleurs, typo, icônes)
* **Mettez en valeur les urgences** (rouge, icône ⚠️) → réponse au besoin de Sophie
* **Simplifiez les formulaires** → réponse au besoin de Thomas
* **Optimisez pour tablette** → réponse au besoin de Julien

#### c) Prototypage (20 min)
* **Reliez vos écrans** dans Figma pour créer une navigation interactive
* **Testez vos 3 cas d'utilisation prioritaires** sur le prototype

### Étape 3 – Présentation (30 min)
* Présentez votre prototype comme à un client
* Structure : problème résolu → démonstration → améliorations futures

### Étape 4 – Livraison (25 min)
* **Lien Figma** (lecture seule avec commentaires activés)
* **Document de synthèse** avec analyse UX et justifications design  

---

## Partie cours (synthèse)

### UX et UI
- **UX** = expérience utilisateur → efficacité et simplicité.
- **UI** = interface utilisateur → visuel et graphisme.

### Méthodologie UX
1. **Recherche utilisateur** - Interviews et observations
2. **Analyse des besoins** - Cas d'utilisation et diagrammes
3. **Conception** - Wireframes et prototypes
4. **Test et validation** - Retours utilisateurs

### Étapes de conception
- **Wireframes** → schémas rapides de structure
- **Prototype** → version interactive
- **Test utilisateur** → validation des choix

### Principes clés
- **Loi de Fitts** → rapidité d'accès aux boutons (taille et distance)
- **Hiérarchie visuelle** → urgences en avant, informations prioritaires
- **Accessibilité** → contrastes, icônes claires, ergonomie tactile

### Outil : Figma
- **Travail collaboratif** en ligne temps réel
- **Plugins utiles** : Content Reel (données fictives), Chart (graphiques)
- **Composants** : éléments réutilisables synchronisés
- **Prototypage** : liens interactifs entre écrans

---

## 🎨 Mémento Figma

### Interface principale
- **Barre d'outils** (gauche) : Outils de création
- **Canvas** (centre) : Zone de travail
- **Panneau propriétés** (droite) : Modification des éléments
- **Panneau calques** (gauche) : Structure et organisation

### Outils essentiels (raccourcis)
- **V** : Sélection (Move tool)
- **F** : Frame (conteneur principal)
- **R** : Rectangle
- **O** : Ellipse  
- **T** : Texte
- **P** : Plume (tracés personnalisés)
- **Échap** : Retour à l'outil sélection

### Raccourcis indispensables
- **Ctrl + D** : Dupliquer la sélection
- **Ctrl + G** : Grouper les éléments
- **Ctrl + Shift + G** : Dégrouper
- **Alt + glisser** : Dupliquer en déplaçant
- **Shift + glisser** : Contraindre les proportions
- **Ctrl + Z** : Annuler
- **Ctrl + Y** : Rétablir

### Navigation
- **Molette souris** : Zoom
- **Espace + glisser** : Déplacer la vue
- **Ctrl + 0** : Ajuster à l'écran
- **Ctrl + 1** : Zoom 100%
- **Shift + 1** : Centrer sur la sélection

### Création de composants
1. **Sélectionner** l'élément à transformer
2. **Ctrl + Alt + K** ou clic droit → "Create Component"
3. **Glisser** depuis Assets pour créer une instance
4. **Modifier** le composant maître met à jour toutes les instances

### Prototypage
1. **Basculer** en mode Prototype (onglet en haut à droite)
2. **Cliquer** sur un élément → poignée bleue apparaît
3. **Glisser** la poignée vers l'écran de destination
4. **Configurer** l'interaction (On Click, Navigate To, etc.)
5. **Tester** avec le bouton Play

### Auto Layout (mise en page automatique)
- **Shift + A** : Ajouter Auto Layout à la sélection
- **Espacement** : Espace entre les éléments
- **Padding** : Marge intérieure du conteneur
- **Direction** : Horizontal ou vertical
- **Alignement** : Top, center, bottom / Left, center, right

### Styles et design system
- **Couleurs** : Créer des styles dans le panneau propriétés
- **Typographie** : Définir des styles de texte réutilisables
- **Effets** : Ombres, flous, contours standardisés
- **Grilles** : Layout grids pour l'alignement

### Plugins recommandés
- **Content Reel** : Génère du faux contenu (textes, images)
- **Iconify** : Bibliothèque d'icônes massive
- **Unsplash** : Photos gratuites haute qualité
- **Chart** : Création de graphiques et diagrammes

### Conseils pratiques
- **Nommer** clairement vos calques et frames
- **Organiser** en pages (Dashboard, Détails, Création)
- **Utiliser** les composants pour la cohérence
- **Sauvegarder** régulièrement (auto-save activé)
- **Commenter** pour la collaboration

---

## 📖 Glossaire des termes techniques

### Figma - Concepts de base
- **Frame** : Conteneur principal, équivalent à un "plan de travail" ou "artboard"
- **Layer/Calque** : Élément individuel (texte, forme, image, etc.)
- **Canvas** : Zone de travail infinie où vous placez vos designs
- **Asset** : Ressource réutilisable (composant, couleur, police)

### Composants et instances
- **Component/Composant** : Élément maître réutilisable (bouton, carte, etc.)
- **Instance** : Copie d'un composant qui reste synchronisée avec le maître
- **Variant** : Différents états d'un même composant (normal, hover, disabled)
- **Override** : Modification locale d'une instance sans affecter le composant maître

### Mise en page
- **Auto Layout** : Système de mise en page automatique et responsive
- **Constraints** : Règles de redimensionnement (left, right, center, scale)
- **Grid** : Grille d'alignement pour organiser les éléments
- **Spacing** : Espacement entre les éléments dans un Auto Layout
- **Padding** : Marge intérieure d'un conteneur

### Styles et design
- **Fill** : Remplissage d'un élément (couleur, dégradé, image)
- **Stroke** : Contour/bordure d'un élément
- **Effect** : Effet visuel (ombre, flou, etc.)
- **Blend Mode** : Mode de fusion entre calques
- **Opacity** : Transparence d'un élément (0-100%)

### Prototypage
- **Hotspot** : Zone cliquable pour déclencher une interaction
- **Transition** : Animation entre deux écrans ou états
- **Overlay** : Élément qui s'affiche par-dessus le contenu existant
- **Flow** : Parcours utilisateur à travers plusieurs écrans
- **Smart Animate** : Animation automatique entre éléments similaires

### Collaboration
- **Share** : Partager un fichier avec d'autres utilisateurs
- **Comment** : Annotation collaborative sur le design
- **Version History** : Historique des modifications du fichier
- **Permissions** : Droits d'accès (view, edit, admin)
- **Team Library** : Bibliothèque partagée de composants et styles

---

## 🛠️ Guide d'utilisation Figma étape par étape

### 1. Démarrage d'un projet
1. **Créer un nouveau fichier** : "Design file" depuis l'accueil
2. **Nommer le projet** : "TechSolutions - Gestion Tickets"
3. **Créer des pages** : Dashboard, Détails, Création (via le panneau gauche)
4. **Définir les frames** : Utiliser les tailles prédéfinies (Desktop, Tablet)

### 2. Configuration du design system
1. **Couleurs** : Créer des "Color Styles" dans le panneau propriétés
   - Bleu principal : #2563EB
   - Vert secondaire : #10B981
   - Gris neutre : #6B7280
2. **Typographie** : Créer des "Text Styles"
   - H1 : Montserrat Bold 32px
   - H2 : Montserrat Semibold 24px
   - Body : Inter Regular 16px
3. **Composants de base** : Boutons, cartes, champs de saisie

### 3. Création d'un écran
1. **Frame principal** : F → sélectionner "Desktop" (1440x1024)
2. **Structure** : Header, sidebar, contenu principal
3. **Éléments** : Ajouter textes (T), formes (R, O), images
4. **Organisation** : Grouper (Ctrl+G) et nommer les calques

### 4. Utilisation des composants
1. **Créer un composant** : Sélectionner → Ctrl+Alt+K
2. **Publier dans la librairie** : Clic droit → "Publish to library"
3. **Utiliser une instance** : Glisser depuis le panneau Assets
4. **Modifier une instance** : Changer texte, couleur sans casser le lien

### 5. Auto Layout pour la responsivité
1. **Sélectionner un groupe** d'éléments
2. **Ajouter Auto Layout** : Shift+A
3. **Configurer** :
   - Direction : Horizontal/Vertical
   - Spacing : 16px entre éléments
   - Padding : 24px autour
   - Alignment : Left/Center/Right

### 6. Prototypage des interactions
1. **Basculer en mode Prototype** (onglet à droite)
2. **Sélectionner l'élément déclencheur** (bouton, carte)
3. **Glisser la poignée bleue** vers l'écran de destination
4. **Configurer l'interaction** :
   - Trigger : On Click, On Hover, etc.
   - Action : Navigate To, Open Overlay
   - Animation : Instant, Dissolve, Smart Animate
5. **Tester** : Bouton Play en haut à droite

### 7. Collaboration et partage
1. **Partager le fichier** : Bouton "Share" en haut à droite
2. **Définir les permissions** : Can view / Can edit
3. **Ajouter des commentaires** : C → cliquer pour annoter
4. **Générer le lien de présentation** : Présent → Copy link

### 8. Export et livraison
1. **Sélectionner l'élément** à exporter
2. **Panneau Export** : Choisir format (PNG, JPG, SVG, PDF)
3. **Prototype interactif** : Share → Present → Copy link
4. **Specifications développeur** : Mode "Inspect" pour le CSS

### Erreurs courantes à éviter
- ❌ Ne pas nommer les calques → organisation difficile
- ❌ Oublier d'utiliser des composants → incohérences
- ❌ Frames trop petits → contenu coupé
- ❌ Trop d'effets visuels → interface chargée
- ❌ Textes non vectoriels → problème d'export
- ❌ Oublier les états hover/active → prototype incomplet

---

## 📋 Aide-mémoire pratique

### Exemples de cas d'utilisation à identifier
- "En tant que **technicien senior**, je veux voir rapidement mes tickets urgents pour prioriser mon travail"
- "En tant que **nouveau technicien**, je veux créer un ticket sans risquer d'oublier des informations importantes"
- "En tant que **chef d'équipe**, je veux voir la charge de travail de mes techniciens pour équilibrer les assignations"
- "En tant que **technicien itinérant**, je veux consulter les détails d'un ticket sur ma tablette"

### Exemple de diagramme de cas d'utilisation
```
         TechSolutions - Gestion de tickets

    [Technicien Senior] ──────── (Consulter tickets urgents)
           │                            │
           ├─────────────────── (Assigner un ticket)
           │                            │
           └─────────────────── (Modifier priorité)
                                        │
    [Technicien Junior] ──────── (Créer un ticket) ◄──┘
           │                            │
           ├─────────────────── (Demander aide)
           │                            │
           └─────────────────── (Consulter historique)
                                        │
    [Chef d'équipe] ────────── (Voir tableau de bord) ◄─┘
           │                            │
           ├─────────────────── (Générer rapport)
           │                            │
           └─────────────────── (Répartir charge)

    [Système] ──────────────── (Envoyer notifications)
                                        │
                             (Sauvegarder automatiquement)
```

### Exemple de wireframe Dashboard
```
┌─────────────────────────────────────────────────────────┐
│ [🏠] TechSolutions              [🔔] [👤] Marie Dubois   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ ⚠️  TICKETS URGENTS (3)     📊 STATISTIQUES    ➕ NOUVEAU│
│ ┌─────────────────────────┐ ┌─────────────────┐       │
│ │ #1234 - CRITIQUE        │ │ En cours: 15    │       │
│ │ Installation serveur    │ │ Résolus: 8      │       │
│ │ ⏰ 2h dépassé           │ │ Nouveaux: 3     │       │
│ └─────────────────────────┘ └─────────────────┘       │
│                                                         │
│ 📋 TOUS LES TICKETS                                     │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ⚪ #1235 - Maintenance | Moyenne  | Sophie C. | 2h  │ │
│ │ 🟢 #1236 - Formation  | Basse    | Thomas M. | 1j  │ │
│ │ 🔴 #1237 - Audit      | Haute    | Non assigné     │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ [Filtrer] [Trier] [Exporter]              Page 1/3     │
└─────────────────────────────────────────────────────────┘
```

### Exemple de wireframe Création ticket
```
┌─────────────────────────────────────────────────────────┐
│ ← Retour                     NOUVEAU TICKET             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ CLIENT * ┌─────────────────────────────────────────────┐│
│          │ 🔍 Rechercher client...           [↓]      ││
│          └─────────────────────────────────────────────┘│
│                                                         │
│ URGENCE * ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐        │
│           │ 🔴   │ │ 🟠   │ │ 🟡   │ │ 🟢   │        │
│           │CRITIC│ │HAUTE │ │MOYEN │ │BASSE │        │
│           └──────┘ └──────┘ └──────┘ └──────┘        │
│                                                         │
│ CATÉGORIE * ┌─────────────────────────────────────────┐│
│             │ Installation                    [↓]    ││
│             └─────────────────────────────────────────┘│
│                                                         │
│ DESCRIPTION *                                           │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Décrivez le problème ou la demande...              │ │
│ │                                                     │ │
│ │                                                     │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ PIÈCES JOINTES                                          │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ + Ajouter fichiers ou photos                       │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│                    [Annuler]  [💾 Créer le ticket]     │
└─────────────────────────────────────────────────────────┘
```

### Acteurs pour le diagramme de cas d'utilisation
- **Technicien junior** (< 6 mois)
- **Technicien senior** (> 1 an)
- **Chef d'équipe** / Manager
- **Technicien itinérant** (travail sur site)

### Champs obligatoires à prévoir
- **ID client** (recherche/sélection)
- **Catégorie** (Installation, Maintenance, Formation, Audit, Migration)
- **Urgence** (Critique, Haute, Moyenne, Basse)
- **Description** du problème
- **Technicien assigné** (optionnel au début)

### Ressources disponibles
- [Charte graphique](charte_graphique.md)
- [Exemples de tickets](exemples_tickets.md)
- [Patterns d'interface](patterns_interface.md)

---

## 📊 Critères d'évaluation détaillés

### **Grille d'évaluation sur 20 points**

#### 1. **Analyse UX** (5 points - 25%)

**🎯 Cas d'utilisation et diagrammes**

**Excellent (5 pts)** :
- Format correct : "En tant que [acteur], je veux [action] pour [objectif]"
- 5-7 cas d'utilisation pertinents liés aux interviews
- Diagramme de cas d'utilisation clair avec tous les acteurs
- Priorisation des 3 cas les plus critiques avec justification

**Bien (4 pts)** :
- Format respecté avec quelques imprécisions mineures
- Cas d'utilisation appropriés mais manque de détails
- Diagramme présent mais perfectible
- Priorisation logique

**Moyen (3 pts)** :
- Format basique respecté
- Cas d'utilisation corrects mais superficiels
- Diagramme simple mais fonctionnel
- Priorisation présente

**Insuffisant (1-2 pts)** :
- Format incorrect ou cas d'utilisation inadaptés
- Diagramme confus ou manquant
- Pas de priorisation ou illogique

---

#### 2. **Qualité du prototype** (7 points - 35%)

**🎨 Design et fonctionnalités**

**2.1 Écrans et navigation (3 pts)** :
- ✅ **3 écrans minimum** : Dashboard, Détail ticket, Création ticket
- ✅ **Navigation fonctionnelle** : liens entre écrans, retour possible
- ✅ **Prototype testable** : cas d'utilisation vérifiables

**2.2 Ergonomie et utilisabilité (2 pts)** :
- ✅ **Tickets urgents facilement visibles** (≤ 2 secondes)
- ✅ **Création ticket simplifiée** (≤ 30 secondes)
- ✅ **Interface intuitive** pour un débutant
- ✅ **Compatible tablette** : boutons ≥ 44px, texte ≥ 16px

**2.3 Réponse aux problèmes identifiés (2 pts)** :
- ✅ **Résout le problème de Thomas** : création rapide (vs 12 champs/3 onglets)
- ✅ **Résout le problème de Sophie** : guidage visuel urgence et catégories
- ✅ **Résout le problème de Marie** : accès rapide tickets urgents
- ✅ **Résout le problème de Julien** : interface adaptée tablette

---

#### 3. **Design et cohérence** (5 points - 25%)

**🎨 Charte graphique et esthétique**

**3.1 Respect de la charte (2 pts)** :
- ✅ **Couleurs** : Bleu #2563EB, Vert #10B981, Gris #6B7280
- ✅ **Typographies** : Montserrat (titres), Inter (corps)
- ✅ **Cohérence** entre les 3 écrans

**3.2 Hiérarchie visuelle (2 pts)** :
- ✅ **Priorités visuelles** : urgences mises en avant
- ✅ **Actions principales** facilement identifiables
- ✅ **Information density** : équilibre lisibilité/efficacité

**3.3 Maîtrise Figma (1 pt)** :
- ✅ **Composants utilisés** pour la cohérence
- ✅ **Organisation** : calques nommés, pages structurées
- ✅ **Qualité technique** : alignements, espacements

---

#### 4. **Documentation et justification** (3 points - 15%)

**📋 Livrables écrits**

**4.1 Page 1 - Analyse (1.5 pts)** :
- ✅ **Liste complète** des cas d'utilisation identifiés
- ✅ **Diagramme propre** et correctement annoté
- ✅ **Justification** des 3 cas prioritaires

**4.2 Page 2 - Choix design (1.5 pts)** :
- ✅ **Tableau structuré** : Élément | Choix | Justification UX
- ✅ **Arguments UX** : références aux principes (loi de Fitts, etc.)
- ✅ **Lien explicite** interviews → solutions proposées

---

### **Critères de réussite opérationnels**

#### ✅ **Critères techniques obligatoires**
- [ ] Un technicien junior peut créer un ticket en **< 30 sec**
- [ ] Les tickets urgents sont visibles en **< 2 sec**
- [ ] L'interface respecte la **charte graphique TechSolutions**
- [ ] Navigation possible sur **desktop ET tablette** (≥ 1024x768)
- [ ] **Champs obligatoires** présents : ID client, urgence, catégorie

#### ✅ **Critères UX attendus**
- [ ] **Accès rapide** aux tickets urgents (problème Marie)
- [ ] **Création simplifiée** vs 12 champs/3 onglets (problème Thomas)
- [ ] **Guidage visuel** pour éviter les oublis (problème Sophie)
- [ ] **Ergonomie tactile** adaptée tablette (problème Julien)

#### ✅ **Critères de qualité**
- [ ] **Navigation intuitive** : utilisateur se repère facilement
- [ ] **Feedback visuel** : boutons, états, confirmations
- [ ] **Gestion d'erreur** : que se passe-t-il si champ vide ?
- [ ] **Cohérence** : mêmes patterns sur tous les écrans

---

### **Bonus possibles** (jusqu'à +2 points)

#### 🌟 **Fonctionnalités avancées**
- **Recherche intelligente** dans les tickets
- **Notifications visuelles** pour les urgences
- **Statistiques dashboard** (graphiques, KPI)
- **Mode sombre** ou thèmes alternatifs

#### 🌟 **Excellence UX**
- **Micro-interactions** : hover, transitions, feedback
- **Accessibilité avancée** : contraste élevé, navigation clavier
- **États multiples** : loading, erreur, succès
- **Personnalisation** : préférences utilisateur

#### 🌟 **Innovation design**
- **Solutions créatives** aux problèmes identifiés
- **Interactions originales** mais utilisables
- **Design system** poussé avec variants
- **Prototype haute fidélité** avec vraies données

---

### **Conseils pour maximiser votre note**

#### 🎯 **Phase d'analyse (30 min)**
- **Relisez attentivement** les 4 interviews
- **Identifiez tous les pain points** mentionnés
- **Rédigez 6-8 cas d'utilisation** en format strict
- **Créez un diagramme lisible** avec tous les acteurs

#### 🎯 **Phase de conception (90 min)**
- **Commencez par des wireframes** basés sur vos cas d'utilisation
- **Testez mentalement** chaque cas d'utilisation sur vos wireframes
- **Appliquez la charte** systématiquement
- **Vérifiez l'ergonomie tablette** (tailles, espaces)

#### 🎯 **Phase de documentation (25 min)**
- **Structurez votre document** : 2 pages claires
- **Justifiez chaque choix** par une référence UX ou interview
- **Relisez et corrigez** : fautes d'orthographe pénalisées
- **Vérifiez les liens Figma** : permissions lecture activées

#### ⚠️ **Erreurs à éviter**
- ❌ Oublier les champs obligatoires (ID client, urgence, catégorie)
- ❌ Tickets urgents noyés dans la liste
- ❌ Interface non adaptée tablette
- ❌ Pas de justification des choix design
- ❌ Prototype non fonctionnel (liens cassés)
- ❌ Documentation bâclée ou incomplète

**Bonne chance ! Votre prototype peut vraiment améliorer le quotidien des techniciens TechSolutions ! 🚀**

---

