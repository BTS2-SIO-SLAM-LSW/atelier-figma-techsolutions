# Exemples de Tickets - TechSolutions

## 🎯 Objectif

Ces **3 exemples représentatifs** illustrent les cas d'usage principaux de l'application TechSolutions. Ils vous aident à comprendre les **besoins métier réels** et à concevoir une interface adaptée pour l'atelier.

## 🎫 Ticket #TS-001 : Maintenance Urgente

## 🎫 Ticket #TS-001 : Maintenance Urgente

### Informations générales
- **Client** : Clinique Sainte-Marie
- **Type** : Maintenance
- **Priorité** : 🔴 CRITIQUE
- **Statut** : 🚨 Urgent - 2h dépassé
- **Technicien assigné** : Non assigné

### Description
Serveur principal en panne, impossible d'accéder aux dossiers patients. **Intervention d'urgence requise**.

### Impact UX à considérer
- ⚠️ **Visibilité maximum** : Doit apparaître en premier sur dashboard
- 🔴 **Codes couleur** : Rouge pour urgence, alertes visuelles
- ⏰ **Temps écoulé** : Affichage temps dépassé en évidence
- 🚀 **Action rapide** : Bouton "TRAITER" immédiatement accessible
- 🔔 **Notifications** : Alertes push pour non-assignés

---

## 🎫 Ticket #TS-002 : Installation Standard

### Informations générales
- **Client** : Entreprise Martin & Associés
- **Type** : Installation
- **Priorité** : 🟡 Moyenne
- **Statut** : 📋 Planifié
- **Technicien assigné** : Alexandre Dupont

### Description
Installation réseau informatique pour 15 postes de travail dans nouveaux locaux.

### Impact UX à considérer
- 📅 **Planning intégré** : Calendrier avec créneaux disponibles
- 📋 **Suivi étapes** : Progression visuelle (audit → devis → installation)
- 👤 **Assignation claire** : Photo et contact technicien
- 📦 **Matériel requis** : Liste équipements avec statut commande
- 🗺️ **Géolocalisation** : Adresse et itinéraire intégrés

---

## 🎫 Ticket #TS-003 : Formation Utilisateurs

### Informations générales
- **Client** : Mairie de Beaumont
- **Type** : Formation
- **Priorité** : 🟢 Basse
- **Statut** : ✅ Terminé
- **Formateur assigné** : Marc Dubois

### Description
Formation de 8 agents municipaux sur nouveau logiciel de gestion documentaire.

### Impact UX à considérer
- ✅ **États terminés** : Visuels de succès, badges de validation
- 📊 **Métriques satisfaction** : Note client et commentaires
- 📚 **Documentation** : Liens supports et manuels utilisateur
- � **Objectifs atteints** : Indicateurs de réussite formation
- 📝 **Feedback** : Évaluations participants intégrées

---

## 📊 Implications UX Directes pour l'Atelier

### 🎯 Fonctionnalités essentielles à concevoir

#### 1. **Dashboard avec priorisation visuelle**
- **Urgences en premier** : Section rouge visible immédiatement
- **Tri par priorité** : 🔴 Critique → 🟠 Haute → 🟡 Moyenne → 🟢 Basse
- **Temps écoulé** : Indicateurs visuels pour retards
- **Vue d'équipe** : Charge de travail par technicien

#### 2. **Système de statuts intuitif**
```
🆕 Nouveau → 📋 Planifié → 🔄 En cours → ⏳ Attente → ✅ Terminé
```

#### 3. **Navigation optimisée mobile**
- **Accès rapide urgences** : Maximum 2 clics
- **Assignation simple** : Glisser-déposer ou bouton direct
- **Contact client** : Téléphone et adresse intégrés
- **Géolocalisation** : Itinéraire vers intervention

### 🔍 Personas utilisateurs identifiés

#### Thomas "Le Vétéran" (Senior)
- **Besoin** : Voir urgences rapidement, éviter perte de temps
- **Interface** : Dashboard épuré, gros boutons, infos essentielles

#### Sophie "La Junior" (Débutante)
- **Besoin** : Guidage, aide contextuelle, pas d'oubli d'infos
- **Interface** : Formulaires guidés, aide intégrée, validation

#### Marie "La Manager" (Responsable)
- **Besoin** : Vue d'ensemble équipe, KPI, répartition charge
- **Interface** : Graphiques, métriques, assignation rapide

### 📱 Écrans prioritaires à prototyper

1. **Dashboard principal** : Vue urgences + équipe + stats
2. **Liste tickets filtrée** : Par statut, priorité, technicien
3. **Détail ticket** : Infos complètes + actions possibles
4. **Création ticket** : Formulaire simplifié, priorité guidée
5. **Planning technicien** : Interventions jour/semaine

### ⚡ Interactions critiques

- **Bouton "TRAITER URGENCE"** : Rouge, toujours visible
- **Swipe actions** : Glissement pour assigner/fermer
- **Pull to refresh** : Actualisation données temps réel
- **Notifications push** : Nouvelles urgences, retards

### 🎨 Codes visuels métier

#### Couleurs par priorité (à utiliser dans Figma)
- 🔴 **P1 Critique** : `#EF4444` - Service vital interrompu
- 🟠 **P2 Haute** : `#F59E0B` - Impact business significatif  
- 🟡 **P3 Moyenne** : `#EAB308` - Gêne utilisateur modérée
- 🟢 **P4 Basse** : `#10B981` - Amélioration/formation

#### Types d'intervention
- 🔧 **Maintenance** : Réparation, dépannage urgent
- 📦 **Installation** : Nouveau matériel, déploiement
- 👨‍🏫 **Formation** : Accompagnement utilisateur
- � **Audit** : Analyse, conseil, sécurité

### 📏 Métriques de succès à viser

- **Temps d'accès urgences** : ≤ 2 clics depuis accueil
- **Création ticket** : ≤ 30 secondes (vs 6 min actuellement)
- **Taux d'oubli infos** : ≤ 5% (vs 25% actuellement)
- **Satisfaction technicien** : Score SUS ≥ 80/100

### 🔄 Workflow simplifié pour prototypage

```
[URGENCE DÉTECTÉE] → [NOTIFICATION] → [ASSIGNATION] → [INTERVENTION] → [CLÔTURE]
      ↓                   ↓              ↓              ↓             ↓
Dashboard rouge     Push mobile    Drag & drop     Suivi temps    Validation
```

**Conseil atelier** : Concentrez-vous sur le **workflow urgence** qui représente 35% des cas et l'impact business le plus important ! 🚀