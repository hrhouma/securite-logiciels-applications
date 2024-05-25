# Étape 1
****CONNEXION SSH À VOTRE MACHINE KALI ***
1- Ajout d'une deuxième carte en mode host-only-adapter
2- Exécution de ces commandes : 

```bash
apt update 
apt install openssh-server
ip a ou ifconfig (récupérer l'adresse IP)
```
3 - ouvrir cmd
```bash
ssh kali@adresse_ip_récupérée
mot de passe : kali
sudo -s (mot de passe : kali)
```
****DOSSIER PARTAGÉ ENTRE WINDOWS ET KALI****
```bash
1 - activer le partage bidirectionnel
2 - créer un dossier partagé entre la machine host et guest (par exemple, monkaliwindows dans windows et mysharedkali dans kali)
3 - exécutez cette commande mount -t vboxsf nomwindows chemin-vers-machinekali mysharedkali
4 - ajoutez des fichiers dans mon kaliwindows et vous le trouverez dans mysharedkali de kali
```
## Références : 

https://www.geeksforgeeks.org/how-to-enable-and-start-ssh-on-kali-linux/
https://www.geeksforgeeks.org/how-to-change-root-password-in-kali-linux/?ref=ml_lbp


# Étape 2

1. Création d'un répertoire et déplacement des fichiers :
   ```bash
   sudo mkdir /var/www/html/demo
   cd Desktop/mysharedkali
   sudo mv admin/ assets/ images/ article.php demobdd.sql galerie.php index.php /var/www/html/demo/
   ```

2. Listage et modification des permissions des fichiers :
   ```bash
   cd /var/www/html/demo/
   ls -al
   sudo chmod -R 755 /var/www/html/demo
   sudo chown -R www-data:www-data /var/www/html/demo
   ls -al
   ```

3. Démarrage des services Apache et MySQL :
   ```bash
   sudo service apache2 start
   sudo service mysql start
   ```

4. Accès à MySQL et mise à jour de l'utilisateur root :
   ```bash
   sudo mysql
   use mysql;
   UPDATE user SET plugin= '' WHERE user='root';
   flush privileges;
   ```

5. Commandes SQL pour la création et la gestion de la base de données :
   ```sql
   CREATE DATABASE demobdd;
   USE demobdd;
   source /var/www/html/demo/demobdd.sql;
   ```

6. Contenu du fichier `aide.txt` :
   ```text
   0. Prérequis :
   Ce fichier d'aide suppose que vous avez un fichier demobdd.sql avec tous les autres dossiers et fichiers.
   Donnez les droits au répertoire demo :
   chmod -R 755 /var/www/html/demo
   chown -R www-data:www-data /var/www/html/demo

   1. Lancement de apache2 et mysql :
   service apache2 start
   service mysql start
   mysql

   2. Création de la base de données une fois mysql lancé :
   CREATE DATABASE demobdd;
   USE demobdd;
   source /var/www/html/demo/demobdd.sql

   Si besoin de supprimer et de recréer la base de données :
   DROP DATABASE demobdd;
   DROP USER 'demoutilisateur'@'localhost'; (puis recréer la base de données)

   3. Si erreur de connexion MySQL :
   Vérifier le mot de passe SQL de demoutilisateur, par défaut "MdpAss3zS3curis3"
   Il est présent (et à modifier éventuellement) dans demobdd.sql et presque tous les fichiers .php
   ```
