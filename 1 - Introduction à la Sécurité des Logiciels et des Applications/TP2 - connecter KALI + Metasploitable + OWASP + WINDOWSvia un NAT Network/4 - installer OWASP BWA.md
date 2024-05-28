# 4 - Installer OWASP BWA  (Broken Web Applications)
# Références
- https://www.youtube.com/watch?v=Wm57-GR1Zps&ab_channel=r2schools
- https://koayyongcett.medium.com/01-burp-suite-tutorial-starting-up-with-burp-and-owasp-bwa-vm-installation-2b95ea51da63


# Introduction
Le projet OWASP BWA fournit une machine virtuelle (VM) autonome avec diverses applications vulnérables connues. Cette VM est idéale pour les étudiants ou les apprenants souhaitant se familiariser avec la sécurité des applications web, pratiquer leurs compétences et utiliser des outils de pénétration tels que Burp Suite.

# Prérequis
- **Oracle VirtualBox** ([télécharger ici](https://www.virtualbox.org/wiki/Downloads))
- **Mozilla Firefox** ([télécharger ici](https://www.mozilla.org/en-US/firefox/new/))
- **7-Zip** ([télécharger ici](https://www.7-zip.org/download.html))
- **OWASP BWA VM** ([télécharger ici](https://sourceforge.net/projects/owaspbwa/))
- **Burp Suite (Community ou Professional)** ([télécharger ici](https://portswigger.net/burp))
- **Oracle Java** ([télécharger ici](https://www.java.com/en/download/))

# Installation de la VM OWASP BWA

### Étape 1 : Télécharger et extraire OWASP BWA VM
1. Téléchargez l'archive OWASP BWA VM depuis [ce lien](https://sourceforge.net/projects/owaspbwa/).
2. Extrayez le fichier téléchargé à l'aide de 7-Zip ou d'un autre outil de décompression.

### Étape 2 : Importer la VM dans VirtualBox
1. Ouvrez VirtualBox.
2. Cliquez sur `Nouvelle` pour créer une nouvelle machine virtuelle.
3. Remplissez les détails comme suit :
   - **Nom :** OWASP BWA
   - **Type :** Linux
   - **Version :** Ubuntu (64-bit)
   - Cliquez sur `Suivant`.

4. **Configurer la mémoire (RAM) :**
   - Définissez la mémoire de base (RAM) à au moins 2048 Mo (2 Go).
   - Cliquez sur `Suivant`.

5. **Ajouter un disque dur existant :**
   - Sélectionnez `Utiliser un fichier de disque dur virtuel existant`.
   - Cliquez sur l'icône du dossier et sélectionnez le fichier `.vmdk` extrait.
   - Cliquez sur `Créer`.

### Étape 3 : Configurer les paramètres réseau
1. Sélectionnez la machine virtuelle OWASP BWA et cliquez sur `Configuration`.
2. Allez dans `Réseau`.
3. Assurez-vous que `Adapter 1` est activé et attaché à `Adaptateur hôte uniquement`.
4. Cliquez sur `OK` pour enregistrer les paramètres.

### Étape 4 : Démarrer la machine virtuelle
1. Sélectionnez la machine virtuelle OWASP BWA et cliquez sur `Démarrer`.
2. Attendez que le système Linux soit complètement démarré. Cela peut prendre quelques minutes.

### Étape 5 : Accéder aux applications web vulnérables
1. Une fois la VM démarrée, vous verrez une adresse IP à l'écran (par exemple : http://192.168.56.101/).
2. Ouvrez Firefox sur votre machine hôte et entrez l'URL indiquée.
3. Vous verrez une page d'index contenant des liens vers des applications web vulnérables.

## Installation et utilisation de Burp Suite

### Étape 1 : Télécharger et installer Burp Suite
1. Téléchargez Burp Suite depuis [ce lien](https://portswigger.net/burp).
2. Si vous utilisez la version JAR, assurez-vous que Java est installé sur votre machine.

### Étape 2 : Démarrer Burp Suite
1. **Via l'interface graphique :**
   - Exécutez Burp Suite en double-cliquant sur le fichier téléchargé.
   - Suivez les instructions à l'écran pour configurer le projet et les paramètres.

2. **Via la ligne de commande :**
   - Ouvrez un terminal.
   - Exécutez la commande suivante pour démarrer Burp Suite :
     ```bash
     java -jar burpsuite_community_vX.X.X.jar
     ```
   - Pour définir une taille de mémoire spécifique :
     ```bash
     java -Xmx2g -jar burpsuite_community_vX.X.X.jar
     ```
   - Pour démarrer Burp Suite en mode sans interface graphique (headless) :
     ```bash
     java -Djava.awt.headless=true -jar burpsuite_community_vX.X.X.jar
     ```

### Étape 3 : Configurer le proxy Burp Suite dans Firefox
1. Ouvrez Firefox.
2. Allez dans `Options` > `Paramètres` > `Réseau` > `Paramètres de connexion`.
3. Sélectionnez `Configuration manuelle du proxy`.
4. Configurez le proxy HTTP sur `127.0.0.1` et le port sur `8080`.
5. Cliquez sur `OK`.

## Conclusion
En suivant ces étapes, vous aurez configuré une VM OWASP BWA et installé Burp Suite pour pratiquer les tests de pénétration sur des applications web vulnérables. Utilisez cet environnement pour améliorer vos compétences en matière de sécurité des applications web et de tests de pénétration.

Pour plus d'informations et de ressources, consultez les sites officiels d'OWASP et de Burp Suite.
