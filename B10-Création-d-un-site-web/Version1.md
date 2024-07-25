# Partie 1
```bash
nano 1-setup_web_server.sh
```
```bash
chmod +x 1-setup_web_server.sh
sh 1-setup_web_server.sh
```
-------

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
### Contenu de `1-setup_web_server.sh`
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇

```bash
#!/bin/bash

# Mise à jour du système
sudo yum update -y

# Affichage de la version du noyau
cat /proc/version

# Installation des paquets nécessaires
sudo yum install -y git httpd mariadb-server php

# Configuration du serveur Apache
sudo systemctl enable httpd
sudo systemctl start httpd
sudo systemctl status httpd

# Configuration du serveur MariaDB
sudo systemctl enable mariadb
sudo systemctl start mariadb
sudo systemctl status mariadb

# Vérification des versions
sudo httpd -v
sudo mysql --version
sudo php --version

# Configuration des permissions et des liens symboliques
sudo ln -s /var/www/ /home/ec2-user/environment
sudo chown ec2-user:ec2-user /var/www/html

# Création du fichier index.html initial
cd /var/www/html
echo "<html>Hello from the café web server</html>" > /var/www/html/index.html

# Pause pour vérification du site web
echo "Ajout d'une pause de 1 minute pour consulter le site web ==> Adresse IP publique"
echo "Début de la pause, testez svp"
sleep 60
echo "Pause terminée. Appuyez sur une touche pour continuer..."
read -n 1 -s -r -p " "
echo "Continuer le script"

# Nettoyage et clonage du projet MVC eCommerce
sudo rm -rf index.html /var/www/html/*
sudo git clone https://github.com/devopsgodhrehouma/mvc-ecommerce.git
sudo mv /var/www/html/mvc-ecommerce/* /var/www/html/
sudo rm -rf /var/www/html/mvc-ecommerce
sudo systemctl restart httpd
sudo chown ec2-user:ec2-user /var/www/html
sudo chmod -R 755 /var/www/html

# Pause pour vérification du site web
echo "Ajout d'une pause pour consulter le site web ==> Adresse IP publique"
echo "Testez et ensuite, Appuyez sur une touche pour continuer..."
read -n 1 -s -r -p " "
echo "Continuer le script"

# Nettoyage et création des répertoires de projets
sudo rm -rf /var/www/html/*
echo "<html>Hello from the café web server</html>" > /var/www/html/index.html

sudo mkdir /var/www/html/mvc-ecommerce
sudo mkdir /var/www/html/netflix
sudo mkdir /var/www/html/vcard

# Clonage des projets depuis GitHub
sudo git clone https://github.com/devopsgodhrehouma/mvc-ecommerce.git /var/www/html/mvc-ecommerce
sudo git clone https://github.com/pro-prodipto/Netflix-Website-Project.git /var/www/html/netflix
sudo git clone https://github.com/codewithsadee/vcard-personal-portfolio.git /var/www/html/vcard

# Configuration des permissions des répertoires
sudo chown -R ec2-user:ec2-user /var/www/html/mvc-ecommerce
sudo chown -R ec2-user:ec2-user /var/www/html/netflix
sudo chown -R ec2-user:ec2-user /var/www/html/vcard
sudo chmod -R 755 /var/www/html/mvc-ecommerce
sudo chmod -R 755 /var/www/html/netflix
sudo chmod -R 755 /var/www/html/vcard
sudo systemctl restart httpd

# Pause à la fin pour tester les projets
echo "Ajout d'une pause pour tester les projets ==> Adresse IP publique"
echo "Testez et ensuite, Appuyez sur une touche pour terminer..."
read -n 1 -s -r -p " "
echo "Fin du script."

# Fin du script
echo "Script terminé."
```

----
# Partie 2

```bash
nano 2-setup_database.sh
chmod +x 2-setup_database.sh
sh 2-setup_database.sh
```

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
### Contenu de `2-setup_database.sh`
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇


# `2-setup_database.sh`

```bash
#!/bin/bash

# Naviguer vers le répertoire de l'environnement
cd ~/environment

# Télécharger et extraire les fichiers nécessaires
wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/ILT-TF-200-ACACAD-20-EN/mod4-challenge/setup.tar.gz
tar -zxvf setup.tar.gz

wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/ILT-TF-200-ACACAD-20-EN/mod4-challenge/db.tar.gz
tar -zxvf db.tar.gz

wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/ILT-TF-200-ACACAD-20-EN/mod4-challenge/cafe.tar.gz
tar -zxvf cafe.tar.gz

# Déplacer les fichiers extraits vers le répertoire web
sudo mv cafe /var/www/html/
cd setup
chmod +x set-app-parameters.sh

# Remplacer les scripts existants avec les nouveaux contenus
echo "
#!/bin/bash
#
# Script pour définir le mot de passe root de MariaDB juste après l'installation de la base de données.
# et créer un utilisateur admin.
#
# Vérifiez le fichier set-root-password.log après l'exécution pour vérifier l'exécution réussie.
#

sudo mysql --verbose < sql/set-root-password.sql > set-root-password.log

echo
echo \"Le script de définition du mot de passe root est terminé.\"
echo \"Veuillez vérifier le fichier set-root-password.log pour vérifier l'exécution réussie.\"
echo
" > ../db/set-root-password.sh

echo "
--
-- Crée un utilisateur root pouvant se connecter depuis n'importe quel hôte et définit le mot de passe pour tous les utilisateurs root dans MariaDB
--
USE mysql;

DROP USER IF EXISTS 'root'@'%';
DROP USER IF EXISTS 'admin'@'%';

CREATE USER 'root'@'%' IDENTIFIED BY 'Re:Start!9';
CREATE USER 'admin'@'%' IDENTIFIED BY 'Re:Start!9';

ALTER USER 'root'@'%' IDENTIFIED BY 'Re:Start!9';
ALTER USER 'admin'@'%' IDENTIFIED BY 'Re:Start!9';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
" > ../db/sql/set-root-password.sql

echo "
#!/bin/bash
#
# Script pour créer et peupler la base de données cafe.
# Vérifiez le fichier create-db.log après l'exécution pour vérifier l'exécution réussie.
#
sudo mysql --user=admin --password=\"Re:Start!9\" --verbose < sql/create-db.sql > create-db.log

echo
echo \"Le script de création de la base de données est terminé.\"
echo \"Veuillez vérifier le fichier create-db.log pour vérifier l'exécution réussie.\"
echo
" > ../db/create-db.sh

# Insérer le script SQL mis à jour
echo "
/*
Script de création de la base de données pour la base de données cafe
*/
DROP DATABASE IF EXISTS cafe_db;

CREATE DATABASE cafe_db;

USE cafe_db;

/* Créer la table PRODUCT_GROUP. */

CREATE TABLE product_group (
  product_group_number INT(3) NOT NULL PRIMARY KEY,
  product_group_name VARCHAR(25) NOT NULL DEFAULT ''
  );

/* Insérer les données d'initialisation dans la table PRODUCT_GROUP. */

INSERT INTO product_group (product_group_number, product_group_name) VALUES
 (1, 'Pastries'),
 (2, 'Drinks');

/* Créer la table PRODUCT. */

CREATE TABLE product (
  id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(40) NOT NULL DEFAULT '',
  description VARCHAR(200) NOT NULL DEFAULT '',
  price DECIMAL(10,2) NOT NULL DEFAULT 0.0,
  product_group INT(2) NOT NULL DEFAULT 1,
  image_url VARCHAR(256) DEFAULT 'images/default-image.jpg',
  FOREIGN KEY (product_group) REFERENCES product_group (product_group_number)
  );
CREATE TABLE orders (
  order_number INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  order_date_time DATETIME NOT NULL,
  customer_id INT(5),
  amount DECIMAL(10,2)
  );

/* Créer la table ORDER_ITEM. */

CREATE TABLE order_item (
  order_number INT(5) NOT NULL,
  order_item_number INT(5) NOT NULL,
  product_id INT(3),
  quantity INT(2),
  amount DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (order_number, order_item_number),
  FOREIGN KEY (order_number) REFERENCES orders (order_number),
  FOREIGN KEY (product_id) REFERENCES product (id)
  );


/* Insérer les données d'initialisation dans la table PRODUCT. */

INSERT INTO product (product_name, description, price, product_group, image_url) VALUES 
 ('Croissant', 'Fraîche, beurrée et moelleuse... Tout simplement délicieuse!', 1.50, 1, 'images/Croissants.jpg'), 
 ('Donut', 'Nous avons plus d''une demi-douzaine de saveurs!', 1.00, 1, 'images/Donuts.jpg'), 
 ('Cookie aux pépites de chocolat', 'Fait avec du chocolat suisse avec une touche de vanille de Madagascar', 2.50, 1, 'images/Chocolate-Chip-Cookies.jpg'), 
 ('Muffin', 'Banana bread, myrtille, canneberge ou pomme', 3.00, 1, 'images/Muffins.jpg'), 
 ('Tarte fraise-myrtille', 'Pleine du goût et de l''arôme de fruits frais', 3.50, 1, 'images/Strawberry-Blueberry-Tarts.jpg'), 
 ('Tarte aux fraises', 'Fait avec des fraises fraîches mûres et une délicieuse crème fouettée', 3.50, 1, 'images/Strawberry-Tarts.jpg'), 
 ('Café', 'Café noir fraîchement moulu ou café colombien mélangé', 3.00, 2, 'images/Coffee.jpg'), 
 ('Chocolat chaud', '

Riche et crémeux, fait avec du vrai chocolat', 3.00, 2, 'images/Cup-of-Hot-Chocolate.jpg'), 
 ('Latte', 'Proposé chaud ou froid et dans diverses saveurs délicieuses', 3.50, 2, 'images/Latte.jpg');


" > ../db/sql/create-db.sql

# Exécution des scripts de base de données
cd ../db/
sudo sh set-root-password.sh
sudo sh create-db.sh

# Fin du script
echo "Script de configuration de la base de données terminé."
```

Assurez-vous que le script est exécutable et exécutez-le :

```bash
chmod +x 2-setup_database.sh
sh 2-setup_database.sh
```

En suivant ces étapes, le script de création de la base de données devrait s'exécuter sans erreurs de syntaxe et les tables devraient être créées correctement.





---------------

# Annexes

#  `main_setup.sh` 

```bash
#!/bin/bash

# Appel du script de configuration du serveur web
./1-setup_web_server.sh

# Appel du script de configuration de la base de données
./2-setup_database.sh

# Pause finale pour tester les projets
echo "Ajout d'une pause pour tester les projets ==> Adresse IP publique"
echo "Testez et ensuite, Appuyez sur une touche pour terminer..."
read -n 1 -s -r -p " "
echo "Fin du script principal."

# Fin du script principal
echo "Script principal terminé."
```


--------------

# Script de nettoyage : `cleanup.sh`

```bash
#!/bin/bash

# Supprimer les répertoires et fichiers créés
sudo rm -rf /var/www/html/*
sudo rm -rf ~/environment/setup.tar.gz ~/environment/db.tar.gz ~/environment/cafe.tar.gz
sudo rm -rf ~/environment/setup ~/environment/db ~/environment/cafe

# Supprimer les bases de données MariaDB
sudo mysql -u root -p'Re:Start!9' -e "DROP DATABASE IF EXISTS cafe_db;"
sudo mysql -u root -p'Re:Start!9' -e "DROP USER IF EXISTS 'root'@'%';"
sudo mysql -u root -p'Re:Start!9' -e "DROP USER IF EXISTS 'admin'@'%';"

# Arrêter les services
sudo systemctl stop httpd
sudo systemctl stop mariadb

# Démarrer les services pour vérifier que tout a été supprimé
sudo systemctl start httpd
sudo systemctl start mariadb

# Message de fin
echo "Nettoyage terminé. Vous pouvez maintenant réexécuter les scripts."
```
