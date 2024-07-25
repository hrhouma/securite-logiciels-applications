### Module 4 - Laboratoire de défi : Création d'un site Web dynamique pour le café
### Scénario

Après le lancement de la première version de leur site web, les clients ont dit au personnel du café à quel point le site web était joli. Cependant, en plus des éloges, les clients ont souvent demandé s'ils pouvaient passer des commandes en ligne.

Sofía, Nikhil, Frank et Martha ont discuté de la situation. Ils ont convenu que leur stratégie commerciale et leurs décisions devraient se concentrer sur la satisfaction de leurs clients et leur offrir la meilleure expérience possible au café.

### Vue d'ensemble du laboratoire et objectifs

Dans ce laboratoire, vous déploierez une application sur une instance Amazon Elastic Compute Cloud (Amazon EC2). L'application permet au café d'accepter des commandes en ligne. Après avoir testé que l'application fonctionne comme prévu dans la première région AWS (l'environnement de développement), vous créerez une Amazon Machine Image (AMI) à partir de l'instance EC2. Vous déploierez également une deuxième instance de la même application en tant qu'environnement de production dans une autre région AWS.

Après avoir terminé ce laboratoire, vous devriez être capable de :

- Vous connecter à l'IDE AWS Cloud9 sur une instance EC2 existante
- Analyser l'environnement de l'instance EC2 et confirmer l'accessibilité du serveur web
- Installer une application web sur une instance EC2 utilisant également AWS Systems Manager Parameter Store
- Tester l'application web
- Créer une AMI
- Déployer une deuxième copie de l'application web dans une autre région AWS

### Début du laboratoire

1. **Lancer le laboratoire :** Choisissez **Start Lab** pour lancer votre laboratoire.
2. **Accéder à la console de gestion AWS :** Une fois que le statut du laboratoire est prêt, fermez le panneau de démarrage du laboratoire en choisissant **X**. Ensuite, choisissez **AWS** pour ouvrir la console de gestion AWS dans un nouvel onglet du navigateur.

### Préparation d'une instance EC2 pour héberger un site web (Défi #1)

Le café souhaite introduire la commande en ligne pour les clients et permettre au personnel du café de voir les commandes soumises. Leur architecture actuelle du site web, où le site est hébergé sur Amazon S3, ne prend pas en charge les nouvelles exigences commerciales.

Dans la première partie de ce laboratoire, vous jouerez le rôle de Sofía. Vous configurerez une instance Amazon EC2 pour qu'elle soit prête à héberger un site web pour le café.

#### Tâche 1 : Analyse de l'instance EC2 existante

1. **Accéder à l'instance EC2 :** Recherchez et sélectionnez **EC2** dans la boîte de recherche à côté de Services. Ensuite, choisissez **Instances**.
2. **Observer l'instance :** Notez l'instance en cours d'exécution nommée aws-cloud9-CafeWebServer-...

#### Répondre aux questions sur l'instance

1. **Accéder aux questions :** Choisissez le menu **Détails**, puis **Afficher**. Choisissez le lien **Accéder aux questions à choix multiples** qui apparaît en bas de la page.
2. **Questions :**
    - Question 1 : L'instance est-elle dans un sous-réseau public ?
    - Question 2 : L'instance EC2 a-t-elle une adresse IP publique IPv4 assignée ?
    - Question 3 : Quels numéros de port TCP entrants sont ouverts pour cette instance ?
    - Question 4 : L'instance EC2 a-t-elle un rôle AWS Identity and Access Management (IAM) associé ?

#### Tâche 2 : Connexion à l'IDE sur l'instance EC2

1. **Accéder à AWS Cloud9 :** Recherchez et sélectionnez **Cloud9** dans la boîte de recherche à côté de Services.
2. **Ouvrir l'environnement :** Dans la page des environnements, notez l'environnement CafeWebServer de type instance EC2. Choisissez **Ouvrir**.
3. **Interface IDE :** L'IDE inclut :
    - Un terminal Bash dans le panneau en bas à droite.
    - Un navigateur de fichiers dans le panneau de gauche qui montre les fichiers dans le répertoire /home/ec2-user/environment.
    - Un éditeur de fichiers dans le panneau en haut à droite.

#### Tâche 3 : Analyse de l'environnement LAMP et confirmation de l'accessibilité du serveur web

1. **Observer la version de l'OS :**
    ```bash
    cat /proc/version
    ```
2. **Observer le serveur web, la base de données et les détails PHP :**
    ```bash
    sudo httpd -v
    sudo yum -y install httpd php-mbstring
    service httpd status
    php --version
    ```
3. **Démarrer le serveur web et la base de données :**
    ```bash
    sudo chkconfig httpd on
    sudo service httpd start
    sudo service httpd status

    sudo yum install -y mariadb-server
    sudo mariadb --version
    sudo systemctl enable mariadb
    sudo chkconfig mariadb on
    sudo service mariadb start
    sudo service mariadb status
    ```
4. **Configurer l'instance EC2 pour utiliser l'éditeur AWS Cloud9 :**
    ```bash
    ln -s /var/www/ /home/ec2-user/environment
    sudo chown ec2-user:ec2-user /var/www/html
    ```
5. **Créer une page de test simple :**
    - Créez un fichier nommé `index.html` dans le répertoire `html` avec le contenu :
      ```html
      <html>Hello from the café web server!</html>
      ```
6. **Rendre le site accessible depuis internet :**
    - **IP publique de l'instance EC2 :** Chargez `http://<public-ip>` dans un nouvel onglet du navigateur.
    - **Mettre à jour le groupe de sécurité :** Permettre le trafic HTTP entrant sur le port TCP 80 de n'importe où.

### Installation d'une application web dynamique sur l'instance EC2 (Défi #2)

#### Tâche 4 : Installation de l'application du café

1. **Télécharger et extraire les fichiers de l'application :**
    ```bash
    cd ~/environment
    wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACACAD-2-91555/04-lab-mod4-challenge-EC2/s3/setup.zip
    unzip setup.zip
    wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACACAD-2-91555/04-lab-mod4-challenge-EC2/s3/db.zip
    unzip db.zip
    wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACACAD-2-91555/04-lab-mod4-challenge-EC2/s3/cafe.zip
    unzip cafe.zip -d /var/www/html/
    ```
2. **Configurer les paramètres de l'application dans AWS Systems Manager Parameter Store :**
    ```bash
    cd setup
    ./set-app-parameters.sh
    ```
3. **Configurer la base de données MySQL :**
    ```bash
    cd ../db/
    ./set-root-password.sh
    ./create-db.sh
    ```
4. **Mettre à jour la configuration du fuseau horaire dans PHP :**
    ```bash
    sudo sed -i "2i date.timezone = \"America/New_York\" " /etc/php.ini
    sudo service httpd restart
    ```
5. **Tester l'application web du café :**
    - Chargez `http://<public-ip>/cafe` dans un navigateur.
    - Résoudre les problèmes d'accès en ajustant les permissions et rôles IAM si nécessaire.

#### Tâche 5 : Tester l'application web

1. **Passer une commande :**
    - Sur la page `http://<public-ip>/cafe`, choisissez **Menu** et passez une commande.
    - Consultez l'historique des commandes pour vérifier que les commandes ont bien été enregistrées.

### Créer des environnements de développement et de production dans différentes régions AWS (Défi #3)

#### Tâche 6 : Créer une AMI et lancer une autre instance EC2

1. **Créer une nouvelle paire de clés sur l'instance EC2 :**
    ```bash
    sudo hostname cafeserver
    ssh-keygen -t rsa -f ~/.ssh/id_rsa
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    ```
2. **Créer une image AMI à partir de l'instance :**
    - Nom de l'image : CafeServer
    - Créez l'image dans la console de gestion AWS et attendez qu'elle soit disponible.
3. **Créer une AMI dans une autre région AWS (Oregon - us-west-2) :**
    - Copier l'ID de l'AMI et le partager avec la région us-west-2.
4. **Créer une nouvelle instance EC2 à partir de l'AMI :**
    - Critères :
      - Région : Oregon
      - Taille de l'instance : t2.small
      - Réseau : Lab VPC Région 2, sous-réseau public
      - Rôle IAM : CafeRole
      - Groupe de sécurité : Ouvrir le port TCP 22 et 80 à partir de n'importe où


5. **Configurer les paramètres de l'application dans la nouvelle région AWS :**
    - Modifiez les lignes 12 et 18 du fichier `set-app-parameters.sh` pour correspondre à la région et au DNS public de la nouvelle instance.
    - Exécutez le script.

#### Tâche 7 : Vérifier la nouvelle instance du café

1. **Vérifier que la nouvelle instance ProdCafeServer fonctionne :**
    - Chargez l'IP publique dans un navigateur pour vérifier l'accès.
    - Chargez `http://<public-ip>/cafe` et testez les fonctionnalités de l'application en passant une commande.

### Annexes

#### Commandes à exécuter

```bash
cat /proc/version
sudo httpd -v
sudo yum -y install httpd php-mbstring
service httpd status
php --version
sudo chkconfig httpd on
sudo service httpd start
sudo service httpd status
sudo yum install -y mariadb-server
sudo mariadb --version
sudo systemctl enable mariadb
sudo chkconfig mariadb on
sudo service mariadb start
sudo service mariadb status
ln -s /var/www/ /home/ec2-user/environment
sudo chown ec2-user:ec2-user /var/www/html
cd ~/environment
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACACAD-2-91555/04-lab-mod4-challenge-EC2/s3/setup.zip
unzip setup.zip
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACACAD-2-91555/04-lab-mod4-challenge-EC2/s3/db.zip
unzip db.zip
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACACAD-2-91555/04-lab-mod4-challenge-EC2/s3/cafe.zip
unzip cafe.zip -d /var/www/html/
cd setup
./set-app-parameters.sh
cd ../db/
./set-root-password.sh
./create-db.sh
sudo sed -i "2i date.timezone = \"America/New_York\" " /etc/php.ini
sudo service httpd restart
sudo hostname cafeserver
ssh-keygen -t rsa -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

### Compléter le laboratoire

1. **Soumettre le travail :** Choisissez **Submit** en haut des instructions pour enregistrer votre progression.
2. **Terminer le laboratoire :** Choisissez **End Lab**, puis **Yes**.

Félicitations ! Vous avez terminé le laboratoire.
