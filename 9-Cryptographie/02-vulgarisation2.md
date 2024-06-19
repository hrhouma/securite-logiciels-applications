## Vulgarisation du Processus d'Autorisation des Clés SSH avec l'Application Turo
# Référence : 
- https://superuser.com/questions/1135766/how-to-ssh-from-one-ec2-instance-to-another
- https://stackoverflow.com/questions/9270734/ssh-permissions-are-too-open
### Histoire

Imaginons que vous souhaitez louer une voiture via l'application Turo. Turo est une plateforme où les propriétaires de voitures peuvent louer leurs véhicules à d'autres utilisateurs. Pour que tout se passe en toute sécurité, il y a un processus d'autorisation similaire à celui des clés SSH.

### Concept

1. **La Boîte avec un Cadenas (Clé Publique)** :
   Le propriétaire de la voiture (comme Karine) laisse la voiture avec un cadenas électronique (clé publique) que seule une personne autorisée peut ouvrir.

2. **La Clé Privée** :
   En tant que locataire, vous recevez un code unique (clé privée) qui vous permet d'ouvrir la voiture.

### Processus

1. **Demande de Location** :
   Vous réservez la voiture via l'application Turo. Le propriétaire de la voiture reçoit votre demande et décide de vous ajouter à la liste des personnes autorisées à ouvrir la voiture. Cela revient à ajouter votre clé publique au fichier `authorized_keys`.

2. **Accès à la Voiture** :
   Une fois votre réservation confirmée, vous recevez un code unique (votre clé privée) via l'application Turo. Ce code est ce qui vous permet d'ouvrir le cadenas électronique sur la voiture.

3. **Ouverture de la Voiture** :
   En arrivant à la voiture, vous utilisez le code reçu pour déverrouiller le cadenas électronique et accéder à la voiture. Ce processus est sécurisé car seul vous, avec votre clé privée (le code unique), pouvez ouvrir la voiture.

### Explication en Termes de SSH

- **Clé Publique** : Le cadenas électronique sur la voiture que le propriétaire configure pour chaque locataire.
- **Clé Privée** : Le code unique que vous recevez via l'application Turo.
- **authorized_keys** : La liste dans laquelle le propriétaire ajoute les locataires autorisés, similaire à ajouter des clés publiques pour permettre l'accès.

En ajoutant votre clé publique dans le fichier `authorized_keys`, le propriétaire de la voiture vous permet d'utiliser votre clé privée pour accéder à la voiture, garantissant ainsi que seul vous pouvez déverrouiller et utiliser la voiture pendant la période de location.
