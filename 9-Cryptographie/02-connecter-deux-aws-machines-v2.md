## Tutoriel détaillé : Comment connecter deux instances EC2 sur AWS via SSH
# Référence : https://superuser.com/questions/1135766/how-to-ssh-from-one-ec2-instance-to-another
### Pré-requis
- Deux instances EC2 créées sur AWS.
- Accès aux clés privées (.pem) de chaque instance.

### Méthode 1 : Utiliser les mêmes clés sur les serveurs

1. **Convertir les clés au format OpenSSH** :
   Si vos clés ne sont pas déjà au format OpenSSH, convertissez-les en utilisant `ssh-keygen` ou un outil similaire.

2. **Télécharger et transférer les clés privées** :
   Téléchargez les clés privées et transférez-les sur chaque serveur.

3. **Connexion SSH en spécifiant le fichier de clé privée** :
   Utilisez la commande suivante pour vous connecter au serveur de destination en spécifiant le fichier de clé privée :
   ```bash
   ssh -i mykey.pem private.ip.du.serveur.cible
   ```

### Méthode 2 : Créer de nouvelles clés

1. **Générer des clés sur chaque serveur** :
   Exécutez la commande suivante sur chaque serveur pour générer une nouvelle paire de clés SSH :
   ```bash
   ssh-keygen
   ```
   Appuyez sur Entrée trois fois pour accepter les options par défaut. Vous obtiendrez deux fichiers :
   - `~/.ssh/id_rsa`
   - `~/.ssh/id_rsa.pub`

2. **Copier la clé publique du serveur A** :
   Sur le serveur A, affichez et copiez la clé publique dans le presse-papier :
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
   Sélectionnez et copiez le contenu affiché.

3. **Ajouter la clé publique au serveur B** :
   Connectez-vous au serveur B et ajoutez le contenu copié au fichier `authorized_keys` :
   ```bash
   cat >> ~/.ssh/authorized_keys
   ```
   Collez le contenu de votre presse-papier et appuyez sur `Ctrl+D` pour quitter.

4. **Connexion SSH à partir du serveur A** :
   Maintenant, vous pouvez vous connecter depuis le serveur A au serveur B en utilisant la clé privée :
   ```bash
   ssh -i ~/.ssh/id_rsa private.ip.du.serveur.cible
   ```

### Méthode 3 : Utiliser le transfert d'agent SSH

1. **Configurer le fichier `~/.ssh/config` sur la machine locale** :
   Ajoutez la section suivante à votre fichier `~/.ssh/config` :
   ```bash
   Host serveur-A
     ForwardAgent yes
   ```

2. **Ajouter les clés publiques aux fichiers `authorized_keys` des serveurs A et B** :
   Sur chaque serveur, assurez-vous que votre clé publique locale est ajoutée au fichier `authorized_keys` :
   ```bash
   ssh-copy-id user@serveur-A
   ssh-copy-id user@serveur-B
   ```

3. **Vérifier la configuration de l'agent SSH** :
   Connectez-vous au serveur A et vérifiez si la variable d'environnement `SSH_AUTH_SOCK` est configurée :
   ```bash
   echo $SSH_AUTH_SOCK
   ```
   Vous devriez voir une sortie indiquant une connexion de socket pour l'échange de clés.

4. **Connexion au serveur B depuis le serveur A** :
   Une fois connecté au serveur A, utilisez la commande suivante pour vous connecter au serveur B :
   ```bash
   ssh user@serveur-B
   ```

### Conseils supplémentaires

- **Groupes de sécurité** :
  Assurez-vous que les groupes de sécurité des instances EC2 autorisent le trafic SSH (port 22) entre elles.

- **Agent SSH** :
  Vérifiez que l'agent SSH est en cours d'exécution sur votre machine locale et sur les serveurs. Utilisez `ps -e | grep [s]sh-agent` pour vérifier cela.

En suivant ces méthodes, vous pourrez établir des connexions SSH sécurisées entre deux instances EC2 sur AWS.
