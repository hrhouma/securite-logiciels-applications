## Tutoriel : Connexion entre deux serveurs AWS avec des clés SSH
# Référence : https://superuser.com/questions/1135766/how-to-ssh-from-one-ec2-instance-to-another
### Méthode 1 - Utiliser les mêmes clés sur les serveurs
- https://stackoverflow.com/questions/9270734/ssh-permissions-are-too-open

1. **Convertir les clés au format OpenSSH** :
   Convertissez vos clés au format OpenSSH et téléchargez les clés privées sur les serveurs.

2. **Spécifier le fichier de clé privée lors de la connexion** :
   Lors de la connexion SSH au serveur de destination, spécifiez le fichier de clé privée :
   ```bash
   ssh -i mykey.pem private.ip.du.serveur.cible
   ```

### Méthode 2 - Créer de nouvelles clés

1. **Générer des clés sur chaque serveur** :
   Sur chaque serveur, exécutez la commande suivante pour générer une nouvelle paire de clés SSH :
   ```bash
   ssh-keygen
   ```
   Appuyez sur Entrée trois fois pour accepter les options par défaut. Vous aurez deux fichiers :
   - `.ssh/id_rsa`
   - `.ssh/id_rsa.pub`

2. **Copier la clé publique du serveur A** :
   Sur le serveur A, affichez et copiez la clé publique dans le presse-papier :
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
   [Sélectionnez et copiez le contenu]

3. **Ajouter la clé publique au serveur B** :
   Connectez-vous au serveur B et ajoutez le contenu copié au fichier `authorized_keys` :
   ```bash
   cat >> ~/.ssh/authorized_keys
   ```
   [Collez le contenu de votre presse-papier]
   Appuyez sur `Ctrl+D` pour quitter.

4. **Connexion SSH à partir du serveur A** :
   Maintenant, vous pouvez vous connecter depuis le serveur A au serveur B en utilisant la clé privée :
   ```bash
   ssh -i ~/.ssh/id_rsa private.ip.du.serveur.cible
   ```

En suivant ces étapes, vous pourrez configurer et utiliser des connexions SSH sécurisées entre deux serveurs AWS.
