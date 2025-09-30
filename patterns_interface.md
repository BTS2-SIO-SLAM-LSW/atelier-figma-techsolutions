# Patterns d'Interface - Atelier TechSolutions

## 🎯 Objectif

Ce document contient les **patterns essentiels** pour créer une interface mobile professionnelle dans l'atelier. Focus sur les éléments **directement applicables** dans Figma pendant les 3h15.

## 📱 Navigation Mobile

### Tab Bar (Navigation principale)
- **Usage** : 3-5 sections principales maximum
- **Position** : Bas de l'écran pour accessibilité pouce
- **Icônes** : Claires et universelles (home, search, profile, etc.)
- **États** : Normal, sélectionné, avec badge notification

```
┌─────────────────────────────────────────┐
│                                         │
│         Contenu principal              │
│                                         │
│                                         │
├─────────────────────────────────────────┤
│ 🏠    📋    📊    👤    ⚙️           │
│Home  Tasks Stats Profile Settings      │
└─────────────────────────────────────────┘
```

### Navigation Drawer (Menu secondaire)
- **Usage** : Actions secondaires, paramètres, profil
- **Déclenchement** : Bouton hamburger (☰) en haut à gauche
- **Overlay** : Fond semi-transparent quand ouvert

## 📋 Affichage des Données

### Cards (Cartes) - Idéal pour tickets
```
┌─────────────────────────────────────────┐
│ 🔴 #1234 CRITIQUE - Serveur FAIL       │
│ 📍 Martin & Asso • ⏰ 2h dépassé       │
│ 👤 Non assigné          [🚀 TRAITER]   │
└─────────────────────────────────────────┘
```

**Composants d'une card ticket** :
- **Header** : Priorité + numéro + type
- **Titre** : Description concise du problème
- **Métadonnées** : Client, temps, technicien
- **Actions** : Bouton principal d'action

### Listes avec états visuels
- **En cours** : Barre de progression
- **Terminé** : ✅ Coche verte
- **Bloqué** : ⏸️ Pause orange
- **Urgent** : 🔴 Indicateur rouge

## 🎨 Couleurs de Statuts (Métier IT)

### Priorités tickets
- **🔴 P1 - Critique** : `#EF4444` (Rouge TechSolutions)
- **🟠 P2 - Haute** : `#F59E0B` (Orange)
- **🟡 P3 - Moyenne** : `#EAB308` (Jaune)
- **🟢 P4 - Basse** : `#10B981` (Vert TechSolutions)

### États système
- **✅ Opérationnel** : `#10B981` (Vert)
- **⚠️ Attention** : `#F59E0B` (Orange)
- **❌ Erreur** : `#EF4444` (Rouge)
- **⏸️ Maintenance** : `#6B7280` (Gris)

### Types d'intervention
- **🔧 Maintenance** : Bleu principal `#2563EB`
- **📦 Installation** : Vert `#10B981`
- **👨‍🏫 Formation** : Violet `#8B5CF6`
- **🔍 Audit** : Orange `#F59E0B`

## 📐 Espacements et Tailles

### Zone de touch mobile
- **Minimum** : 44px x 44px (Apple HIG)
- **Recommandé** : 48px x 48px
- **Espacement** : 8px minimum entre éléments tactiles

### Hiérarchie des textes mobile
- **Titre principal** : 24px (Inter Semibold)
- **Sous-titre** : 18px (Inter Medium)
- **Corps** : 16px (Inter Regular)
- **Légende** : 14px (Inter Regular)
- **Small** : 12px (Inter Regular)

### Marges mobile
- **Écran** : 16px latérales
- **Cards** : 16px padding interne
- **Éléments** : 8px espacement vertical

## 🔄 Micro-interactions Essentielles

### États des boutons
1. **Normal** : Couleur de base
2. **Hover** : Légère opacité (90%)
3. **Active** : Couleur plus foncée
4. **Disabled** : Opacité 50%
5. **Loading** : Spinner + texte "Chargement..."

### Feedback utilisateur
- **Succès** : Toast vert + icône ✅
- **Erreur** : Toast rouge + icône ❌
- **Info** : Toast bleu + icône ℹ️
- **Chargement** : Skeleton ou spinner

## 🏗️ Composants TechSolutions

### Bouton Urgence (Spécial)
```
┌─────────────────┐
│ 🚨 URGENCE     │ ← Rouge, grande taille
│                 │   Toujours visible
└─────────────────┘
```

### Indicateur de charge technicien
```
Sophie Lemoine    [████████░░] 8/10
Marc Dubois       [██████░░░░] 6/10
```

### Timeline intervention
```
✅ 09:00 - Diagnostic à distance
🔄 10:30 - Intervention sur site
⏳ 14:00 - Attente pièce
⏸️ 16:00 - Reporté demain
```

## 📊 Dashboard Mobile - Exemple

```
┌─────────────────────────────────────────┐
│ 🏠 TechSolutions    🔔(3)    👤 Thomas  │
├─────────────────────────────────────────┤
│ ⚠️ URGENCES NON TRAITÉES (2)           │
│ ┌─────────────────────────────────────┐ │
│ │ 🔴 #1234 CRITIQUE - Serveur FAIL   │ │
│ │ 📍 Martin & Asso • ⏰ 2h dépassé   │ │
│ │ 👤 Non assigné    [🚀 TRAITER]     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 📊 VUE ÉQUIPE          📈 STATS         │
│ Sophie: 🟡 3/5         📋 Résolus: 12   │
│ Marc:   🔴 8/6         🎯 Objectif: 15  │
├─────────────────────────────────────────┤
│ 🏠 📋 📊 👤 ⚙️                        │
└─────────────────────────────────────────┘
```

## ✅ Checklist Design

### À vérifier dans votre prototype :
- [ ] **Navigation** : Tab bar avec 3-5 onglets max
- [ ] **Couleurs** : Respect priorités P1-P4
- [ ] **Tailles** : Boutons ≥ 44px, texte ≥ 16px
- [ ] **Contraste** : Texte sur fond ≥ 4.5:1
- [ ] **États** : Normal, hover, disabled visibles
- [ ] **Feedback** : Actions ont une réponse visuelle
- [ ] **Cohérence** : Mêmes patterns partout

## 🎯 Objectifs Atelier

Votre prototype doit montrer :
1. **Dashboard** avec vue urgences
2. **Liste tickets** avec filtres
3. **Détail ticket** avec actions
4. **Création ticket** simplifiée
5. **Navigation** fluide entre écrans

**Temps recommandé sur les patterns** : 15 min lecture + application continue pendant la conception.