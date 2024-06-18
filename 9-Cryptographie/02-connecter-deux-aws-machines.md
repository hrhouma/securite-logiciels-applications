# Objectifs du TP
- Comprendre les fondamentaux de la cryptographie asymétrique.
- Appliquer la connexion sécurisée entre deux machines virtuelles en utilisant des clés publiques et privées.

# Matériel nécessaire
- Oracle VirtualBox installé sur un PC ou un serveur.
- Images ISO de système d'exploitation, comme Ubuntu Server.

# Étapes du TP

# Partie 1 : Configuration des machines virtuelles
1. **Installation des machines virtuelles** :
   - Créez deux machines virtuelles dans VirtualBox. Assurez-vous de configurer suffisamment de ressources (CPU, mémoire, disque).
   - Installez un système d'exploitation Linux, comme Ubuntu, sur chaque VM en utilisant les images ISO.

2. **Configuration du réseau** :
   - Configurez les cartes réseau en mode "Réseau interne" pour que les VM puissent communiquer entre elles mais pas avec l'extérieur.

# Partie 2 : Configuration des clés SSH
3. **Génération des clés SSH sur la machine client** :
   - Connectez-vous à la première VM via la console VirtualBox.
   - Générez une paire de clés SSH en utilisant `ssh-keygen` :
     ```bash
     ssh-keygen -t rsa -b 2048
     ```
   - Suivez les instructions pour nommer et enregistrer les clés, généralement dans `~/.ssh/id_rsa` et `~/.ssh/id_rsa.pub`.

4. **Transfert de la clé publique au serveur** :
   - Copiez la clé publique de la machine client vers la machine serveur en utilisant `ssh-copy-id` :
     ```bash
     ssh-copy-id -i ~/.ssh/id_rsa.pub user@<adresse-IP-serveur>
     ```

# Partie 3 : Test de la connexion
5. **Connexion SSH depuis le client** :
   - Testez la connexion SSH depuis la machine client vers la machine serveur :
     ```bash
     ssh user@<adresse-IP-serveur>
     ```
   - Si la configuration est correcte, la connexion doit se faire sans demande de mot de passe.

# Partie 4 : Discussion et réflexion
6. **Questions de réflexion** :
   - Expliquer l'importance de la clé publique et de la clé privée dans ce processus.
   - Discuter des avantages de l'utilisation de clés SSH par rapport aux mots de passe traditionnels.
   - Quels seraient les risques si la clé privée était compromise ?

# Ressources supplémentaires
- Documentation VirtualBox pour la configuration de machines virtuelles.
- Tutoriels sur la configuration de SSH et la cryptographie asymétrique.

Ce TP permet aux étudiants de mettre en pratique les concepts de sécurité dans un environnement contrôlé, facilitant ainsi une meilleure compréhension de la gestion sécurisée des accès aux systèmes.
