# Guide de Correction - Atelier Figma TechSolutions

## 🎯 Corrigé des livrables attendus

### 1. Analyse des cas d'utilisation (5 points)

#### Cas d'utilisation attendus (exemples de bonnes réponses)

**Acteurs identifiés** :
- Technicien senior (expérimenté)
- Technicien junior (nouveau, < 6 mois)
- Chef d'équipe/Manager
- Technicien itinérant (travail sur site)

**Cas d'utilisation prioritaires** :

1. **"En tant que technicien senior, je veux voir immédiatement les tickets urgents non assignés pour pouvoir réagir rapidement"**
   - *Justification* : Répond au problème de Marie (4 clics pour accéder aux urgents)
   - *Priorité* : CRITIQUE

2. **"En tant que nouveau technicien, je veux créer un ticket avec un guidage visuel pour éviter d'oublier des champs obligatoires"**
   - *Justification* : Répond aux problèmes de Sophie (oubli urgence, confusion catégories)
   - *Priorité* : HAUTE

3. **"En tant que technicien expérimenté, je veux créer un ticket rapidement (< 30 sec) même avec un client pressé au téléphone"**
   - *Justification* : Répond au problème de Thomas (12 champs, 3 onglets)
   - *Priorité* : HAUTE

#### Diagramme de cas d'utilisation - Structure attendue

```
    [Chef d'équipe] ──────── (Voir tableau de bord équipe)
           │                         │
           └──────────────── (Répartir les tickets)
                                     │
    [Technicien Senior] ──── (Consulter tickets urgents) ◄─┘
           │                         │
           ├──────────────── (Modifier priorité ticket)
           │                         │
           └──────────────── (Assigner à un collègue)
                                     │
    [Technicien Junior] ──── (Créer un ticket guidé) ◄────┘
           │                         │
           ├──────────────── (Demander aide/validation)
           │                         │
           └──────────────── (Consulter aide contextuelle)
                                     │
    [Technicien Itinérant] ── (Consulter ticket sur tablette) ◄─┘
           │                         │
           └──────────────── (Ajouter photos du problème)

    [Système] ──────────── (Envoyer notifications urgentes)
                                     │
                           (Sauvegarder automatiquement)
```

**Critères d'évaluation** :
- ✅ Format correct "En tant que... je veux... pour..." (1 pt)
- ✅ Cas d'utilisation pertinents liés aux interviews (2 pts)
- ✅ Priorisation justifiée (1 pt)
- ✅ Diagramme lisible avec acteurs et actions (1 pt)

---

### 2. Prototype Figma (7 points)

#### Écran 1 : Dashboard - Éléments attendus

**Structure obligatoire** :
- [ ] Header avec nom utilisateur et notifications
- [ ] Section "TICKETS URGENTS" mise en évidence (rouge/orange)
- [ ] Accès rapide création ticket (bouton + visible)
- [ ] Liste tickets avec statuts visuels (couleurs priorité)
- [ ] Filtres simples (urgence, assigné/non-assigné)

**Bonnes pratiques observées** :
- ✅ Tickets urgents en haut de page (loi de Fitts)
- ✅ Couleurs cohérentes avec charte (bleu #2563EB, vert #10B981)
- ✅ Information dense mais lisible
- ✅ Actions principales facilement accessibles

**Erreurs fréquentes à pénaliser** :
- ❌ Tickets urgents noyés dans la liste
- ❌ Bouton création ticket difficile à trouver
- ❌ Pas de distinction visuelle des priorités
- ❌ Interface trop chargée (overload cognitif)

#### Écran 2 : Détail ticket - Éléments attendus

**Informations obligatoires** :
- [ ] ID ticket et statut (visuel clair)
- [ ] Client et contact
- [ ] Priorité (visuelle + textuelle)
- [ ] Description complète
- [ ] Historique des actions
- [ ] Technicien assigné
- [ ] Actions possibles (modifier, clôturer, réassigner)

**Ergonomie tablette** :
- ✅ Boutons assez grands (> 44px)
- ✅ Texte lisible (> 16px)
- ✅ Zones de touch adaptées
- ✅ Navigation simple (retour visible)

#### Écran 3 : Création ticket - Éléments attendus

**Champs obligatoires** :
- [ ] Client (recherche/autocomplete)
- [ ] Urgence (sélection visuelle radio/boutons)
- [ ] Catégorie (dropdown simple)
- [ ] Description (texte libre)

**Guidage utilisateur** :
- ✅ Champs obligatoires marqués visuellement (*)
- ✅ Validation en temps réel
- ✅ Aide contextuelle (tooltips)
- ✅ Étapes claires et logiques

**Réponses aux problèmes identifiés** :
- ✅ Moins de 5 champs sur 1 seul écran (vs 12 champs/3 onglets)
- ✅ Urgence impossible à oublier (sélection visuelle)
- ✅ Catégories claires et limitées

#### Navigation et prototypage (2 points)

**Interactions attendues** :
- Dashboard → Détail ticket (clic sur ligne)
- Dashboard → Création (bouton +)
- Détail → Modification (bouton éditer)
- Création → Dashboard (bouton créer/annuler)

**Qualité prototypage** :
- ✅ Liens fonctionnels et cohérents
- ✅ Retour navigation toujours possible
- ✅ États hover/active (bonus)
- ✅ Transitions fluides (bonus)

---

### 3. Qualité design (3 points)

#### Respect charte graphique (1 pt)
- ✅ Couleurs : Bleu #2563EB, Vert #10B981, Gris #6B7280
- ✅ Typographies : Montserrat (titres), Inter (corps)
- ✅ Cohérence visuelle entre écrans
- ✅ Hiérarchie claire (tailles, contrastes)

#### Ergonomie et accessibilité (1 pt)
- ✅ Contrastes suffisants (texte lisible)
- ✅ Tailles tactiles adaptées (> 44px)
- ✅ Navigation intuitive
- ✅ États d'erreur prévus

#### Innovation et créativité (1 pt)
- ✅ Solutions originales aux problèmes
- ✅ Micro-interactions pensées
- ✅ Adaptation mobile/tablette
- ✅ Fonctionnalités bonus (recherche, statistiques)

---

### 4. Documentation et justification (3 points)

#### Page 1 : Analyse UX attendue
**Contenu minimum** :
- Liste des 5-7 cas d'utilisation identifiés
- Diagramme de cas d'utilisation propre
- Justification des 3 cas prioritaires
- Lien explicite avec les interviews

**Exemple de justification** :
> "Nous avons priorisé l'accès rapide aux tickets urgents car Marie (cheffe support) a explicitement mentionné que les techniciens doivent actuellement faire 4 clics pour y accéder, ce qui génère des pertes de temps et du mécontentement client."

#### Page 2 : Choix design attendus

**Format tableau recommandé** :
| Élément | Choix design | Justification UX |
|---------|--------------|-------------------|
| Bouton urgence | Rouge, placé en haut à droite | Loi de Fitts : accès rapide, couleur d'alerte universelle |
| Formulaire création | 4 champs sur 1 écran | Réduction cognitive load vs 12 champs/3 onglets actuels |
| Sélection urgence | Boutons radio colorés | Guidage visuel pour éviter l'oubli (problème Sophie) |

**Critères d'évaluation documentation** :
- ✅ Arguments UX précis et référencés (1 pt)
- ✅ Lien explicite interviews → solutions (1 pt)
- ✅ Document structuré et professionnel (1 pt)

---

## 🔍 Grille d'évaluation détaillée

### Barème sur 20 points

#### Excellent (18-20/20)
- Tous les cas d'utilisation pertinents identifiés
- Prototype fonctionnel et ergonomique
- Design cohérent et innovant
- Documentation argumentée et professionnelle
- Réponses créatives aux problèmes utilisateurs

#### Très bien (15-17/20)
- Bonne analyse avec quelques manques mineurs
- Prototype fonctionnel avec design correct
- Respect de la charte graphique
- Justifications présentes mais perfectibles
- Solutions adaptées aux besoins identifiés

#### Bien (12-14/20)
- Analyse correcte mais superficielle
- Prototype de base fonctionnel
- Design acceptable avec quelques incohérences
- Documentation minimale mais présente
- Compréhension des enjeux UX démontrée

#### Passable (10-11/20)
- Cas d'utilisation basiques identifiés
- Prototype partiel avec navigation limitée
- Design basic respectant partiellement la charte
- Justifications succinctes
- Effort UX visible mais limité

#### Insuffisant (< 10/20)
- Analyse UX manquante ou inadéquate
- Prototype non fonctionnel
- Design incohérent ou non finalisé
- Pas de justification des choix
- Compréhension limitée des enjeux

---

## 💡 Conseils pour la correction

### Points d'attention pendant l'atelier
- **Circuler régulièrement** pour identifier les équipes en difficulté
- **Noter les bonnes pratiques** observées pour les valoriser
- **Repérer les innovations** pour les mettre en avant
- **Vérifier l'alignement** analyse → wireframes → prototype

### Feedback constructif
**Ce qui fonctionne bien** :
- Valoriser les solutions créatives
- Souligner les justifications UX pertinentes
- Encourager l'esprit d'équipe
- Reconnaître l'effort de recherche utilisateur

**Points d'amélioration** :
- Suggérer des améliorations concrètes
- Proposer des ressources complémentaires
- Encourager l'itération et le test utilisateur
- Orienter vers des références inspirantes

### Adaptations selon le niveau
**Étudiants novices** :
- Se concentrer sur la méthode plus que le résultat
- Valoriser la démarche de recherche utilisateur
- Accepter des wireframes simples mais bien pensés

**Étudiants avancés** :
- Encourager la réflexion sur l'accessibilité
- Demander des justifications plus poussées
- Proposer des défis additionnels (micro-interactions, etc.)

---

## 📋 Checklist correction rapide

### Analyse UX (/5)
- [ ] Format cas d'utilisation correct
- [ ] Cas pertinents vs interviews  
- [ ] Priorisation justifiée
- [ ] Diagramme lisible

### Prototype (/7)
- [ ] 3 écrans créés et reliés
- [ ] Navigation fonctionnelle
- [ ] Réponse aux problèmes identifiés
- [ ] Ergonomie tablette respectée

### Design (/3)
- [ ] Charte graphique respectée
- [ ] Cohérence visuelle
- [ ] Solutions créatives

### Documentation (/3)
- [ ] 2 pages structurées
- [ ] Justifications UX argumentées
- [ ] Lien interviews → solutions

### Bonus (/2)
- [ ] Innovation particulière
- [ ] Micro-interactions
- [ ] Accessibilité avancée
- [ ] Fonctionnalités supplémentaires

**Total : /20**

Cette grille permet une évaluation objective tout en valorisant la créativité et la démarche UX des étudiants ! 🎯