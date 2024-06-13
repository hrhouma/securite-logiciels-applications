## Tutoriel d'installation et d'utilisation des Outils de Gestion des Vulnérabilités

# Référentiel : 
- https://www.digitalocean.com/community/tutorials/how-to-use-nessus-for-vulnerability-scanning-on-ubuntu-2204
- https://abhijit-pal.medium.com/resolving-nessus-installation-issue-on-ubuntu-dpkg-frontend-lock-error-a161123c0378
- https://www.howtoforge.com/how-to-install-nessus-security-scanner-on-ubuntu-22-04/
  
### Nessus

#### Étape 1 : Installation de Nessus sur Ubuntu 22.04

1. **Téléchargez le paquet Nessus** :
    ```bash
    wget https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/13795/download?i_agree_to_tenable_license_agreement=true -O Nessus-10.0.1-ubuntu910_amd64.deb
    ```

2. **Installez Nessus** :
    ```bash
    sudo dpkg -i Nessus-10.0.1-ubuntu910_amd64.deb
    ```

3. **Démarrez le service Nessus** :
    ```bash
    sudo systemctl start nessusd
    sudo systemctl enable nessusd
    ```

4. **Accédez à l'interface web** :
    Ouvrez votre navigateur et accédez à `https://localhost:8834`.

5. **Configurez et activez Nessus** :
    Suivez les instructions à l'écran pour configurer et activer Nessus.

#### Étape 2 : Utilisation de Nessus

1. **Connectez-vous à l'interface web de Nessus**.
2. **Créez un nouveau scan** :
    - Cliquez sur `New Scan`.
    - Choisissez un type de scan (Basic Network Scan, Web Application Tests, etc.).
    - Configurez les paramètres du scan (adresse IP, plages IP, etc.).
    - Cliquez sur `Save`.
3. **Lancez le scan** :
    - Sélectionnez le scan créé.
    - Cliquez sur `Launch`.
4. **Consultez les résultats** :
    - Après le scan, consultez les résultats détaillés et les rapports des vulnérabilités détectées.

### OpenVAS

#### Étape 1 : Installation d'OpenVAS sur Ubuntu 22.04

1. **Ajoutez le dépôt PPA d'OpenVAS** :
    ```bash
    sudo add-apt-repository ppa:mrazavi/openvas
    sudo apt-get update
    ```

2. **Installez OpenVAS** :
    ```bash
    sudo apt-get install openvas
    ```

3. **Configurez OpenVAS** :
    ```bash
    sudo gvm-setup
    ```

4. **Démarrez les services OpenVAS** :
    ```bash
    sudo gvm-start
    ```

5. **Accédez à l'interface web** :
    Ouvrez votre navigateur et accédez à `https://localhost:9392`.

#### Étape 2 : Utilisation d'OpenVAS

1. **Connectez-vous à l'interface web d'OpenVAS**.
2. **Créez un nouvel objectif de scan** :
    - Cliquez sur `Scans`.
    - Cliquez sur `Tasks` puis `New Task`.
    - Configurez les paramètres du scan (adresse IP, plages IP, etc.).
    - Cliquez sur `Create`.
3. **Lancez le scan** :
    - Sélectionnez le scan créé.
    - Cliquez sur `Start`.
4. **Consultez les résultats** :
    - Après le scan, consultez les résultats détaillés et les rapports des vulnérabilités détectées.

### Qualys

#### Étape 1 : Inscription et configuration de Qualys

1. **Inscrivez-vous sur le site de Qualys** :
    Allez sur [Qualys](https://www.qualys.com) et inscrivez-vous pour obtenir un compte.

2. **Configurez vos actifs** :
    - Connectez-vous à l'interface web de Qualys.
    - Ajoutez vos actifs (adresses IP, plages IP, etc.).

#### Étape 2 : Utilisation de Qualys

1. **Connectez-vous à l'interface web de Qualys**.
2. **Créez un nouveau scan** :
    - Cliquez sur `Scans` dans le menu de navigation.
    - Cliquez sur `New Scan`.
    - Choisissez un type de scan (Internal, External, Web Application, etc.).
    - Configurez les paramètres du scan (adresses IP, plages IP, etc.).
    - Cliquez sur `Launch`.
3. **Lancez le scan** :
    - Sélectionnez le scan créé.
    - Cliquez sur `Launch`.
4. **Consultez les résultats** :
    - Après le scan, consultez les résultats détaillés et les rapports des vulnérabilités détectées.

### Résumé des commandes

#### Nessus
```bash
wget https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/13795/download?i_agree_to_tenable_license_agreement=true -O Nessus-10.0.1-ubuntu910_amd64.deb
sudo dpkg -i Nessus-10.0.1-ubuntu910_amd64.deb
sudo systemctl start nessusd
sudo systemctl enable nessusd
```

#### OpenVAS
```bash
sudo add-apt-repository ppa:mrazavi/openvas
sudo apt-get update
sudo apt-get install openvas
sudo gvm-setup
sudo gvm-start
```

Ces tutoriels vous guideront dans l'installation et l'utilisation de Nessus, OpenVAS et Qualys pour gérer les vulnérabilités sur vos systèmes.
