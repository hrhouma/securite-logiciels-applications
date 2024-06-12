## Tutoriel d'installation et d'utilisation de SonarQube sur Ubuntu 22.04

SonarQube est une plateforme d'analyse de code qui permet de détecter des vulnérabilités, des bugs et des problèmes de code au sein des applications.

### Fonctionnalités Clés de SonarQube

- **Analyse de Code** : SonarQube analyse le code source pour détecter les vulnérabilités, les bugs et les mauvaises pratiques de codage.
- **Plugins de Sécurité** : Intégration avec des plugins de sécurité pour une détection approfondie des vulnérabilités.
- **Rapports Détailés** : Génération de rapports détaillés sur l'état de la sécurité du code, incluant des métriques sur la couverture de tests, la qualité du code et les failles de sécurité.
- **Intégration CI/CD** : Intégration avec les pipelines CI/CD pour une analyse continue et une détection précoce des vulnérabilités pendant le développement.

### Avantages de SonarQube

- **Détection Précoce** : Identification des problèmes de sécurité dès les premières phases du développement, permettant une correction rapide et efficace.
- **Amélioration de la Qualité du Code** : Promotion des bonnes pratiques de codage et amélioration de la qualité générale du code.
- **Conformité** : Aide à assurer la conformité avec les normes de sécurité et les réglementations, telles que OWASP Top 10 et SANS Top 25.

### Étape 1 : Prérequis

- Serveur Ubuntu 22.04
- Accès root SSH ou utilisateur avec privilèges sudo
- Java 11 ou supérieur

### Étape 2 : Installer Java

1. **Mettre à jour les paquets du système** :
    ```bash
    sudo apt update -y
    ```

2. **Installer Java** :
    ```bash
    sudo apt install openjdk-11-jdk -y
    ```

3. **Vérifier l'installation de Java** :
    ```bash
    java -version
    ```

### Étape 3 : Installer et configurer PostgreSQL

1. **Installer PostgreSQL** :
    ```bash
    sudo apt install postgresql postgresql-contrib -y
    ```

2. **Créer un utilisateur et une base de données pour SonarQube** :
    ```bash
    sudo -i -u postgres
    createuser sonar
    createdb sonarqube -O sonar
    psql
    ALTER USER sonar WITH ENCRYPTED PASSWORD 'your_password';
    \q
    exit
    ```

### Étape 4 : Télécharger et installer SonarQube

1. **Télécharger SonarQube** :
    ```bash
    wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.51034.zip
    ```

2. **Décompresser le fichier téléchargé** :
    ```bash
    sudo apt install unzip -y
    unzip sonarqube-9.4.0.51034.zip
    ```

3. **Déplacer SonarQube vers `/opt`** :
    ```bash
    sudo mv sonarqube-9.4.0.51034 /opt/sonarqube
    ```

### Étape 5 : Configurer SonarQube

1. **Modifier le fichier de configuration SonarQube** :
    ```bash
    sudo nano /opt/sonarqube/conf/sonar.properties
    ```

2. **Configurer la connexion à la base de données** :
    Ajoutez les lignes suivantes ou modifiez-les :
    ```ini
    sonar.jdbc.username=sonar
    sonar.jdbc.password=your_password
    sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
    ```

3. **Configurer les propriétés du système** :
    Ajoutez ou modifiez les lignes suivantes :
    ```ini
    sonar.web.host=0.0.0.0
    sonar.web.port=9000
    ```

### Étape 6 : Créer un utilisateur système pour SonarQube

1. **Créer un utilisateur sonar** :
    ```bash
    sudo useradd -d /opt/sonarqube -c "SonarQube user" sonar
    ```

2. **Donner les permissions appropriées** :
    ```bash
    sudo chown -R sonar:sonar /opt/sonarqube
    ```

### Étape 7 : Créer un service systemd pour SonarQube

1. **Créer le fichier de service** :
    ```bash
    sudo nano /etc/systemd/system/sonarqube.service
    ```

2. **Ajouter les lignes suivantes** :
    ```ini
    [Unit]
    Description=SonarQube service
    After=syslog.target network.target

    [Service]
    Type=forking
    ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
    ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
    User=sonar
    Group=sonar
    Restart=always
    LimitNOFILE=65536
    LimitNPROC=4096
    TimeoutStartSec=5

    [Install]
    WantedBy=multi-user.target
    ```

3. **Démarrer et activer le service** :
    ```bash
    sudo systemctl start sonarqube
    sudo systemctl enable sonarqube
    ```

### Étape 8 : Accéder à l'interface web de SonarQube

Ouvrez votre navigateur et accédez à `http://localhost:9000`. Connectez-vous avec les identifiants par défaut (`admin`/`admin`) et changez le mot de passe lors de la première connexion.

### Résumé des commandes

#### Installation de Java
```bash
sudo apt update -y
sudo apt install openjdk-11-jdk -y
java -version
```

#### Installation et configuration de PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib -y
sudo -i -u postgres
createuser sonar
createdb sonarqube -O sonar
psql
ALTER USER sonar WITH ENCRYPTED PASSWORD 'your_password';
\q
exit
```

#### Installation de SonarQube
```bash
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.51034.zip
sudo apt install unzip -y
unzip sonarqube-9.4.0.51034.zip
sudo mv sonarqube-9.4.0.51034 /opt/sonarqube
sudo nano /opt/sonarqube/conf/sonar.properties
```

#### Création de l'utilisateur système et configuration des permissions
```bash
sudo useradd -d /opt/sonarqube -c "SonarQube user" sonar
sudo chown -R sonar:sonar /opt/sonarqube
```

#### Création du service systemd pour SonarQube
```bash
sudo nano /etc/systemd/system/sonarqube.service
sudo systemctl start sonarqube
sudo systemctl enable sonarqube
```

- Ces instructions détaillées vous guideront à travers l'installation et la configuration de SonarQube sur un serveur Ubuntu 22.04. 
- Pour plus d'informations sur l'utilisation de SonarQube, consultez la documentation officielle de SonarQube.

# IMPORTANT + CORRECTION

- Par défaut, SonarQube ne permet pas de s'exécuter en tant qu'utilisateur root pour des raisons de sécurité.
- Nous devons créer un utilisateur dédié pour exécuter SonarQube.

### Étape 1 : Prérequis

- Serveur Ubuntu 22.04
- Accès root SSH ou utilisateur avec privilèges sudo
- Java 11 ou supérieur

### Étape 2 : Installer Java

1. **Mettre à jour les paquets du système** :
    ```bash
    sudo apt update -y
    ```

2. **Installer Java** :
    ```bash
    sudo apt install openjdk-11-jdk -y
    ```

3. **Vérifier l'installation de Java** :
    ```bash
    java -version
    ```

### Étape 3 : Installer et configurer PostgreSQL

1. **Installer PostgreSQL** :
    ```bash
    sudo apt install postgresql postgresql-contrib -y
    ```

2. **Créer un utilisateur et une base de données pour SonarQube** :
    ```bash
    sudo -i -u postgres
    createuser sonar
    createdb sonarqube -O sonar
    psql
    ALTER USER sonar WITH ENCRYPTED PASSWORD 'your_password';
    \q
    exit
    ```

### Étape 4 : Créer un utilisateur système pour SonarQube

1. **Créer un utilisateur sonar** :
    ```bash
    sudo useradd -m -d /opt/sonarqube -c "SonarQube user" sonar
    ```

2. **Donner les permissions appropriées** :
    ```bash
    sudo chown -R sonar:sonar /opt/sonarqube
    ```

### Étape 5 : Télécharger et installer SonarQube

1. **Télécharger SonarQube** :
    ```bash
    wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.51034.zip
    ```

2. **Décompresser le fichier téléchargé** :
    ```bash
    sudo apt install unzip -y
    unzip sonarqube-9.4.0.51034.zip
    ```

3. **Déplacer SonarQube vers `/opt`** :
    ```bash
    sudo mv sonarqube-9.4.0.51034 /opt/sonarqube
    sudo chown -R sonar:sonar /opt/sonarqube
    ```

### Étape 6 : Configurer SonarQube

1. **Modifier le fichier de configuration SonarQube** :
    ```bash
    sudo nano /opt/sonarqube/conf/sonar.properties
    ```

2. **Configurer la connexion à la base de données** :
    Ajoutez les lignes suivantes ou modifiez-les :
    ```ini
    sonar.jdbc.username=sonar
    sonar.jdbc.password=your_password
    sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
    ```

3. **Configurer les propriétés du système** :
    Ajoutez ou modifiez les lignes suivantes :
    ```ini
    sonar.web.host=0.0.0.0
    sonar.web.port=9000
    ```

### Étape 7 : Créer un service systemd pour SonarQube

1. **Créer le fichier de service** :
    ```bash
    sudo nano /etc/systemd/system/sonarqube.service
    ```

2. **Ajouter les lignes suivantes** :
    ```ini
    [Unit]
    Description=SonarQube service
    After=syslog.target network.target

    [Service]
    Type=forking
    ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
    ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
    User=sonar
    Group=sonar
    Restart=always
    LimitNOFILE=65536
    LimitNPROC=4096
    TimeoutStartSec=5

    [Install]
    WantedBy=multi-user.target
    ```

3. **Démarrer et activer le service** :
    ```bash
    sudo systemctl start sonarqube
    sudo systemctl enable sonarqube
    ```

### Étape 8 : Accéder à l'interface web de SonarQube

Ouvrez votre navigateur et accédez à `http://localhost:9000`. Connectez-vous avec les identifiants par défaut (`admin`/`admin`) et changez le mot de passe lors de la première connexion.

### Résumé des commandes

#### Installation de Java
```bash
sudo apt update -y
sudo apt install openjdk-11-jdk -y
java -version
```

#### Installation et configuration de PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib -y
sudo -i -u postgres
createuser sonar
createdb sonarqube -O sonar
psql
ALTER USER sonar WITH ENCRYPTED PASSWORD 'your_password';
\q
exit
```

#### Création de l'utilisateur système et configuration des permissions
```bash
sudo useradd -m -d /opt/sonarqube -c "SonarQube user" sonar
sudo chown -R sonar:sonar /opt/sonarqube
```

#### Installation de SonarQube
```bash
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.51034.zip
sudo apt install unzip -y
unzip sonarqube-9.4.0.51034.zip
sudo mv sonarqube-9.4.0.51034 /opt/sonarqube
sudo nano /opt/sonarqube/conf/sonar.properties
```

#### Création du service systemd pour SonarQube
```bash
sudo nano /etc/systemd/system/sonarqube.service
sudo systemctl start sonarqube
sudo systemctl enable sonarqube
```

- Ces instructions détaillées vous guideront à travers l'installation et la configuration de SonarQube sur un serveur Ubuntu 22.04 sans utiliser l'utilisateur root pour exécuter SonarQube. 
- Pour plus d'informations sur l'utilisation de SonarQube, consultez la documentation officielle de SonarQube.
