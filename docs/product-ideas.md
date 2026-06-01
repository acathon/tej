# TEJ-Fisc Product Ideas

## Idée A : Smart Universal Connector (Transcodage Intelligent)

**Problème**
L'administration impose un XML rigide, mais les entreprises ont des données hétérogènes (Excel mal formés, PDF scannés, exports ERP variés).

**Fonctionnalité**
Créer un moteur de transcodage intelligent pour transformer des données “sales” en XML conforme TEJ.

**Flow technique**
1. **Ingestion** : upload de fichiers CSV, XLSX, PDF, images.
2. **Mapping IA** : déduction automatique des colonnes (ex. `Client_ID` → Matricule Fiscal, `NET` → Montant Net).
3. **Sanitization** : nettoyage automatique (suppression des espaces dans les matricules, conversion virgules → points, formats de dates).
4. **Output** : génération d’un fichier `.xml` compressé (ZIP) et nommé selon la nomenclature officielle TEJ.

## Idée B : Tax Wallet (Freelances & TPE)

**Problème**
Les freelances subissent des retenues à la source qu’ils oublient de réclamer ou déduire, perdant de l’argent.

**Fonctionnalité**
Un gestionnaire de crédit d’impôt qui suit les RS subies et calcule les montants récupérables.

**Flow technique**
1. **Suivi des RS** : saisie/scan des factures, calcul automatique des retenues attendues.
2. **Matching TEJ** : vérification par import de fichier ou scan que le certificat est bien déposé.
3. **Dashboard de trésorerie** : affichage en temps réel du crédit d’impôt disponible.
4. **Alertes** : notification J-2 avant les échéances de déclaration mensuelle.

## Idée C : Pre-Audit Shield (Liasse Fiscale)

**Problème**
La liasse fiscale impose 30+ tableaux avec des cohérences strictes : une erreur bloque tout.

**Fonctionnalité**
Un moteur de validation croisée et conformité XSD avec rapport d’audit.

**Flow technique**
1. **Import liasse** : ingestion Excel/CSV de la liasse préparée.
2. **Cross-check mathématique** : validation des équations clés (Total Actif = Total Passif).
3. **Validation XSD** : test du XML contre les schémas officiels pour éviter les rejets.
4. **Rapport d’audit** : sortie en “Warnings” et “Criticals” avec priorisation.

## Idée E : Control Tower (Experts-Comptables)

**Problème**
Les cabinets gèrent des centaines de dossiers et ont besoin d’une vue macro avec priorisation.

**Fonctionnalité**
Un cockpit multi-dossiers avec indicateurs de conformité, collecte client et reporting.

**Flow technique**
1. **Multi-tenancy** : bascule instantanée entre sociétés clientes sans déconnexion.
2. **Dashboard conformité** : statuts colorés (urgent/en cours/validé).
3. **Collecte collaborative** : portail client pour dépôt de factures et pièces.
4. **Rapports d’activité** : synthèse mensuelle (volume, montants, statuts).

## Formule de rentabilité (Argument SaaS)

Le gain financier est lié au temps gagné par certificat de RS :

```
Gain = (Temps_manuel - Temps_Nexus) × Nb_Dossiers
```

Exemple : si Nexus réduit le traitement à 1 minute, un cabinet avec 100 clients économise des dizaines d’heures par mois.
