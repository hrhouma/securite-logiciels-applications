# Tutoriel d'installation de Wiki.js sur Ubuntu 22.04

## Prérequis

- Serveur Ubuntu 22.04 (Machine Ubuntu 22.04 Desktop)
- Accès root SSH ou utilisateur avec privilèges sudo

### Étape 1 : Connexion au serveur

Tout d'abord, connectez-vous à votre serveur Ubuntu 22.04 en utilisant SSH en tant que root :

```bash
ssh root@Adresse_IP -p Numéro_Port
```

Remplacez `Adresse_IP` et `Numéro_Port` par l'adresse IP et le port SSH de votre serveur. Si vous utilisez un utilisateur avec privilèges sudo, remplacez `root` par le nom de cet utilisateur.

Vérifiez la version d'Ubuntu installée avec la commande suivante :

```bash
lsb_release -a
```

Assurez-vous que tous les paquets du système d'exploitation sont à jour :

```bash
apt update -y
```

### Étape 2 : Installer NodeJS

Wiki.js nécessite NodeJS et npm. Nous allons installer la version la plus récente de NodeJS à partir du dépôt officiel :

```bash
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```

Ensuite, mettez à jour les informations des paquets et installez NodeJS et npm :

```bash
apt update
apt install nodejs
```

Vérifiez les versions installées :

```bash
node -v; npm -v
```

### Étape 3 : Installer MariaDB et créer une base de données

Installez le serveur MariaDB :

```bash
apt install mariadb-server
```

Le serveur MariaDB sera automatiquement lancé après l'installation. Créez une base de données et un utilisateur pour Wiki.js :

```bash
mysql
```

Dans le shell MySQL, exécutez les commandes suivantes :

```sql
CREATE DATABASE wikijs;
show databases;
GRANT ALL on wikijs.* to wikijs@localhost identified by 'm0d1fyth15';
FLUSH PRIVILEGES;
\q
```

Remplacez `m0d1fyth15` par un mot de passe plus sécurisé.

```sql
mysql -u wikijs -p
entrez votre password, par exemple m0d1fyth15
\q
```
### Étape 4 : Installer Wiki.js

Créez un nouvel utilisateur système pour Wiki.js :

```bash
useradd -m -d /opt/wikijs -U -r -s /bin/bash wikijs
```

Passez à cet utilisateur et téléchargez le fichier d'installation de Wiki.js :

```bash
su - wikijs
wget https://github.com/Requarks/wiki/releases/latest/download/wiki-js.tar.gz
```

Extrayez le fichier téléchargé :

```bash
tar -xzvf wiki-js.tar.gz
```

### Étape 5 : Configurer Wiki.js

Copiez le fichier de configuration échantillon et modifiez-le :

```bash
cp -a config.sample.yml config.yml
nano config.yml
```

Modifiez les lignes suivantes pour correspondre à votre configuration MariaDB :

```yaml
db:
  type: mariadb
  host: localhost
  port: 3306
  user: wikijs
  pass: m0d1fyth15
  db: wikijs
```

Quittez l'éditeur et revenez à l'utilisateur root :

```bash
exit
```

### Étape 6 : Créer un fichier Systemd

Créez un fichier de service systemd pour gérer le service Wiki.js :

```bash
nano /etc/systemd/system/wikijs.service
```

Ajoutez les lignes suivantes :

```ini
[Unit]
Description=Wiki.js
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/node server
Restart=always

User=wikijs
Environment=NODE_ENV=production
WorkingDirectory=/opt/wikijs

[Install]
WantedBy=multi-user.target
```

Sauvegardez le fichier, quittez l'éditeur et rechargez le daemon systemd :

```bash
systemctl daemon-reload
```

Activez et démarrez le service Wiki.js :

```bash
systemctl enable --now wikijs
```

### Étape 7 : Installer et configurer Nginx

Installez Nginx pour créer un proxy inverse :

```bash
apt install nginx
```

Créez un bloc de serveur pour Wiki.js :

```bash
nano /etc/nginx/sites-enabled/wikijs.conf
```

Ajoutez les lignes suivantes :

```nginx
server {
  listen 80;
  server_name wikijs.votredomaine.com;
  root /opt/wikijs;

  location / {
    proxy_pass http://127.0.0.1:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```

Remplacez `wikijs.votredomaine.com` par le domaine ou sous-domaine que vous souhaitez utiliser.

Sauvegardez le fichier et redémarrez Nginx :

```bash
systemctl restart nginx
```

Vous pouvez maintenant accéder à Wiki.js à l'adresse `http://wikijs.votredomaine.com` et compléter l'installation via un navigateur web.

### Résumé des commandes

```bash
ssh root@Adresse_IP -p Numéro_Port
lsb_release -a
apt update -y
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
apt update
apt install nodejs
node -v; npm -v
apt install mariadb-server
mysql
CREATE DATABASE wikijs;
GRANT ALL on wikijs.* to wikijs@localhost identified by 'm0d1fyth15';
FLUSH PRIVILEGES;
\q
useradd -m -d /opt/wikijs -U -r -s /bin/bash wikijs
su - wikijs
wget https://github.com/Requarks/wiki/releases/latest/download/wiki-js.tar.gz
tar -xzvf wiki-js.tar.gz
cp -a config.sample.yml config.yml
nano config.yml
exit
nano /etc/systemd/system/wikijs.service
systemctl daemon-reload
systemctl enable --now wikijs
apt install nginx
nano /etc/nginx/sites-enabled/wikijs.conf
systemctl restart nginx
```

Félicitations ! Vous avez installé avec succès Wiki.js sur votre serveur Ubuntu 22.04. Pour plus d'informations, consultez le site officiel de Wiki.js.

# Annexe - tous supprimer 

- Pour supprimer complètement Wiki.js et toutes les configurations associées de votre serveur Ubuntu 22.04, vous devez suivre les étapes inverses des instructions d'installation.
- Voici un script qui couvre toutes les étapes nécessaires pour effectuer cette désinstallation :

### Étape 1 : Arrêter et désactiver les services

Tout d'abord, arrêtez et désactivez les services de Wiki.js et Nginx :

```bash
systemctl stop wikijs
systemctl disable wikijs
systemctl stop nginx
systemctl disable nginx
```

### Étape 2 : Supprimer les fichiers de configuration et les services

Supprimez les fichiers de service systemd et les fichiers de configuration Nginx :

```bash
rm /etc/systemd/system/wikijs.service
rm /etc/nginx/sites-enabled/wikijs.conf
```

### Étape 3 : Supprimer les fichiers et les utilisateurs de Wiki.js

Supprimez l'utilisateur système et les fichiers de Wiki.js :

```bash
userdel -r wikijs
```

### Étape 4 : Supprimer les bases de données MariaDB

Connectez-vous à MariaDB et supprimez la base de données et l'utilisateur de Wiki.js :

```bash
mysql -u root -p
```

Dans le shell MySQL, exécutez les commandes suivantes :

```sql
DROP DATABASE wikijs;
DROP USER wikijs@localhost;
FLUSH PRIVILEGES;
\q
```

### Étape 5 : Désinstaller les logiciels installés

Désinstallez Node.js, npm, MariaDB et Nginx :

```bash
apt remove --purge nodejs npm mariadb-server nginx -y
apt autoremove -y
apt clean
```

### Étape 6 : Vérifier et nettoyer le système

Assurez-vous qu'il ne reste plus de fichiers de configuration ou de données en vérifiant les répertoires suivants et en les nettoyant si nécessaire :

```bash
rm -rf /opt/wikijs
```

Vous pouvez également vérifier et supprimer les répertoires de configuration restants dans `/etc` et `/var` si nécessaire.

### Résumé des commandes

```bash
systemctl stop wikijs
systemctl disable wikijs
systemctl stop nginx
systemctl disable nginx
rm /etc/systemd/system/wikijs.service
rm /etc/nginx/sites-enabled/wikijs.conf
userdel -r wikijs
mysql -u root -p
# Dans le shell MySQL
# DROP DATABASE wikijs;
# DROP USER wikijs@localhost;
# FLUSH PRIVILEGES;
# \q
apt remove --purge nodejs npm mariadb-server nginx -y
apt autoremove -y
apt clean
rm -rf /opt/wikijs
```

En suivant ces étapes, vous supprimerez complètement Wiki.js et toutes les configurations associées de votre serveur Ubuntu 22.04.


