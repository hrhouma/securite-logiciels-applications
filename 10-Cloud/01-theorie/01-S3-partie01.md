# Cours sur Amazon S3 - partie 1

## Table des matières
1. [Introduction à Amazon S3](#introduction-à-amazon-s3)
2. [Création d'un Bucket S3](#création-dun-bucket-s3)
3. [Gestion des Objets dans S3](#gestion-des-objets-dans-s3)
4. [Gestion des Permissions et de la Sécurité](#gestion-des-permissions-et-de-la-sécurité)
5. [Versioning et Restauration](#versioning-et-restauration)
6. [Logging et Monitoring](#logging-et-monitoring)
7. [Pricing et Facturation](#pricing-et-facturation)
8. [Exercices Pratiques](#exercices-pratiques)
9. [Conclusion](#conclusion)

---

## Introduction à Amazon S3
Amazon Simple Storage Service (Amazon S3) est un service de stockage d'objets évolutif, sécurisé et performant. Il permet aux utilisateurs de stocker et de récupérer n'importe quelle quantité de données à tout moment et de n'importe où sur le web.

### Caractéristiques principales :
- **Évolutivité** : S3 peut gérer des volumes de données massifs.
- **Sécurité** : Options avancées de contrôle d'accès et de chiffrement des données.
- **Durabilité** : Conçu pour offrir une durabilité de 99,999999999%.
- **Accessibilité** : Accessible via des APIs REST, SDKs et la console AWS.

[Revenir en haut](#cours-sur-amazon-s3)

---

## Création d'un Bucket S3
Un bucket est un conteneur de stockage dans S3.

### Étapes pour créer un bucket :
1. Accédez à la console S3 via AWS Management Console.
2. Cliquez sur "Créer un bucket".
3. Entrez un nom de bucket unique et sélectionnez la région.
4. Configurez les options de paramètres (par exemple, versioning, journaux d'accès).
5. Configurez les autorisations de bucket.
6. Cliquez sur "Créer un bucket".

[Revenir en haut](#cours-sur-amazon-s3)

---

## Gestion des Objets dans S3
Les objets sont les éléments de données stockés dans les buckets.

### Opérations courantes :
- **Téléversement d'objets** : Utilisez la console, l'API ou le SDK.
- **Téléchargement d'objets** : Depuis la console ou via des commandes API.
- **Suppression d'objets** : Supprimez les objets individuellement ou par lot.

### Exemples :
```bash
# Télécharger un fichier vers S3
aws s3 cp fichier.txt s3://nom-du-bucket/

# Télécharger un fichier depuis S3
aws s3 cp s3://nom-du-bucket/fichier.txt .

# Supprimer un fichier dans S3
aws s3 rm s3://nom-du-bucket/fichier.txt
```

[Revenir en haut](#cours-sur-amazon-s3)

---

## Gestion des Permissions et de la Sécurité
Amazon S3 offre plusieurs mécanismes pour gérer la sécurité et les permissions.

### Principaux outils de sécurité :
- **Politiques de bucket** : Définissez les permissions au niveau du bucket.
- **Contrôles d'accès (ACLs)** : Définissez les permissions au niveau de l'objet.
- **Chiffrement** : Chiffrez les données en transit et au repos.

### Exemple de politique de bucket :
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::nom-du-bucket/*"
    }
  ]
}
```

[Revenir en haut](#cours-sur-amazon-s3)

---

## Versioning et Restauration
Le versioning permet de conserver plusieurs versions d'un même objet dans un bucket.

### Activer le versioning :
1. Accédez à la page de configuration du bucket.
2. Cliquez sur "Propriétés".
3. Activez le versioning.

### Restaurer une version :
1. Accédez à l'objet souhaité.
2. Cliquez sur "Versions".
3. Sélectionnez la version à restaurer.

[Revenir en haut](#cours-sur-amazon-s3)

---

## Logging et Monitoring
Il est essentiel de surveiller et de journaliser les activités dans vos buckets S3 pour des raisons de sécurité et d'audit.

### Activer les journaux d'accès :
1. Allez dans les paramètres de votre bucket.
2. Activez l'option "Journaux d'accès au bucket".
3. Choisissez un bucket cible pour stocker les journaux.

### Utiliser Amazon CloudWatch :
- Configurez des métriques et des alarmes pour surveiller les performances et les accès.

[Revenir en haut](#cours-sur-amazon-s3)

---

## Pricing et Facturation
Le coût de S3 dépend de plusieurs facteurs :
- **Stockage utilisé** : Facturé par Go/mois.
- **Requêtes et récupération de données** : Facturé par millier de requêtes.
- **Transfert de données** : Coût associé aux données transférées vers l'extérieur d'AWS.

### Estimation des coûts :
Utilisez le [calculateur de prix AWS](https://calculator.aws/#/) pour estimer vos coûts en fonction de votre utilisation.

[Revenir en haut](#cours-sur-amazon-s3)

---

## Exercices Pratiques
1. **Créer un bucket S3** :
   - Suivez les étapes pour créer un nouveau bucket.
   - Configurez les permissions pour permettre l'accès public en lecture.
2. **Téléverser et gérer des objets** :
   - Téléversez un fichier texte.
   - Modifiez les permissions de l'objet pour le rendre public.
3. **Activer le versioning et restaurer un objet** :
   - Activez le versioning sur votre bucket.
   - Téléversez une nouvelle version d'un objet existant.
   - Restaurez la version précédente de l'objet.
4. **Configurer des journaux d'accès et des alarmes CloudWatch** :
   - Activez les journaux d'accès pour votre bucket.
   - Configurez une alarme CloudWatch pour surveiller les requêtes.

[Revenir en haut](#cours-sur-amazon-s3)

---

## Conclusion
Amazon S3 est un service de stockage flexible et robuste qui peut être utilisé pour une variété de cas d'utilisation. En suivant ce cours, vous avez appris les bases de la création, de la gestion et de la sécurisation des buckets et des objets S3.

Pour plus d'informations, consultez la [documentation officielle d'Amazon S3](https://docs.aws.amazon.com/s3/).

[Revenir en haut](#cours-sur-amazon-s3)
