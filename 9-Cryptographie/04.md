# Objectifs du TP
- Comprendre les principes de la cryptographie asymétrique.
- Mettre en pratique la connexion sécurisée entre deux machines virtuelles utilisant des clés publiques et privées.

# Matériel nécessaire
- Oracle VirtualBox installé sur un PC ou un serveur.
- Image ISO de Ubuntu Desktop.

# Étapes du TP

# Partie 1 : Installation et configuration des machines virtuelles
1. **Création des machines virtuelles** :
   - Lancez Oracle VirtualBox et créez deux nouvelles machines virtuelles.
   - Attribuez à chaque machine des ressources adaptées (CPU, mémoire, espace disque).

2. **Installation d'Ubuntu Desktop** :
   - Téléchargez l'image ISO d'Ubuntu Desktop depuis le site officiel.
   - Installez Ubuntu Desktop sur chaque VM en attachant l'image ISO dans les paramètres de la VM et en suivant les instructions d'installation.

3. **Configuration du réseau** :
   - Configurez les cartes réseau de chaque VM en mode "Réseau interne" pour que les machines puissent communiquer entre elles.

# Partie 2 : Configuration des clés SSH
4. **Génération des clés SSH sur la machine client** :
   - Connectez-vous à la première VM via l'interface graphique.
   - Ouvrez un terminal et générez une paire de clés SSH avec la commande :
     ```bash
     ssh-keygen -t rsa -b 2048
     ```
   - Suivez les instructions pour nommer et sauvegarder les clés, habituellement dans `~/.ssh/id_rsa` pour la clé privée et `~/.ssh/id_rsa.pub` pour la clé publique.

5. **Transfert de la clé publique au serveur** :
   - Toujours dans le terminal, utilisez `ssh-copy-id` pour copier la clé publique sur la machine serveur :
     ```bash
     ssh-copy-id -i ~/.ssh/id_rsa.pub ubuntu@<adresse-IP-serveur>
     ```
   - Cette étape assure que la machine client peut se connecter au serveur sans nécessiter de mot de passe.

# Partie 3 : Test de la connexion
6. **Connexion SSH depuis le client** :
   - Testez la connexion SSH depuis la machine client en utilisant :
     ```bash
     ssh ubuntu@<adresse-IP-serveur>
     ```
   - Si la configuration est correcte, la connexion doit se faire sans demande de mot de passe.

# Partie 4 : Discussion et réflexion
7. **Questions de réflexion** :
   - Quel est le rôle de la clé publique et de la clé privée ?
   - Quels sont les avantages de l'utilisation de la cryptographie asymétrique pour les connexions SSH ?
   - Quels risques sont associés à la compromission de la clé privée ?

Cette configuration avec Ubuntu Desktop permet d'illustrer le processus dans un environnement plus familier pour les utilisateurs habitués aux interfaces graphiques, tout en couvrant les aspects essentiels de la sécurité des connexions entre serveurs.
