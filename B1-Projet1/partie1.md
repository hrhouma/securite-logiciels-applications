# Guide détaillé pour l'analyse de logiciels malveillants dans un environnement virtuel sécurisé

## Introduction

Établir un environnement virtuel sécurisé pour analyser des fichiers suspects et effectuer une ingénierie inverse fondamentale est une étape cruciale en cybersécurité. Ce processus permet de créer des machines virtuelles (VM) isolées, réduisant efficacement les risques potentiels liés à la manipulation de fichiers potentiellement malveillants. En simulant un réseau sans connexion Internet, vous pouvez explorer et documenter chaque étape du processus d'analyse en toute sécurité. Dans ce guide, nous utiliserons VirtualBox sur une machine hôte Windows pour configurer plusieurs VM, formant notre réseau isolé.

### Objectif

L'objectif de ce guide est de fournir une méthodologie complète pour :
- **Configurer un environnement sécurisé** : Utilisation de VM pour isoler l'analyse des logiciels malveillants.
- **Analyser les logiciels malveillants** : Utiliser des outils spécialisés pour effectuer des analyses et des ingénieries inverses.
- **Créer un réseau isolé** : Configurer des VM avec un réseau privé sans accès à Internet pour éviter toute fuite de données malveillantes.
- **Assurer la sécurité et la gestion** : Utiliser des règles de pare-feu et des configurations réseau pour contrôler le trafic et les interactions entre les VM.

### Configuration nécessaire

Pour ce guide, nous aurons besoin des machines suivantes :
- **1 VM Windows 10** : Pour l'analyse des logiciels malveillants.
- **1 VM Ubuntu Server** : Pour créer un réseau isolé et gérer le trafic réseau.
- **1 VM Ubuntu Desktop (Stockage de fichiers)** : Pour stocker et partager des fichiers malveillants et des outils d'analyse.
- **1 VM Ubuntu Desktop (Surveillance)** : Pour surveiller le trafic réseau et détecter les comportements suspects.

## Étape 1 : Installation de VirtualBox

1. Téléchargez et installez VirtualBox depuis le site officiel.
2. Suivez les instructions d'installation pour configurer VirtualBox sur votre machine hôte.

## Étape 2 : Installation d'une VM Windows propre

### Téléchargement de l'image ISO de Windows

1. Téléchargez une image ISO de Windows pour la version que vous souhaitez utiliser depuis le site officiel de Microsoft.

### Création d'une nouvelle VM Windows

1. Ouvrez VirtualBox et cliquez sur le bouton “Nouveau”.
2. Nommez votre VM (par exemple, “Windows 10 Analysis”). Pour cet exemple, nous utiliserons le nom "Flare VM".
3. Choisissez “Type” comme “Microsoft Windows” et “Version” comme “Windows 10 (64-bit)”.
4. Cliquez sur “Suivant”.

### Configuration de la VM

1. Choisissez la quantité de RAM à allouer à la VM. Pour des performances optimales, allouez au moins 2GB (2048 MB) si votre machine hôte a suffisamment de ressources.
2. Cliquez sur “Suivant”.
3. Créez un disque dur virtuel et définissez sa taille. Un minimum de 50GB est recommandé pour la VM d'analyse.
4. Cliquez sur “Suivant” puis sur “Terminer” après avoir vérifié vos paramètres.

### Démarrage de la VM

1. Démarrez la VM en cliquant sur “Démarrer”.
2. La VM démarrera à partir de l'ISO de Windows 10.
3. Suivez les instructions à l'écran pour installer Windows 10.

### Installation des outils essentiels

1. Installez des outils pour l'analyse et l'ingénierie inverse tels que :
    - Wireshark : Pour capturer et analyser le trafic réseau.
    - IDA Pro : Pour effectuer une ingénierie inverse sur des binaires.
    - HxD : Un éditeur hexadécimal pour examiner les fichiers binaires.
2. Téléchargez et installez ClamAV pour Windows pour détecter les virus et les logiciels malveillants.
3. Créez un compte utilisateur non privilégié pour l'analyse afin d'éviter d'utiliser le compte administrateur par défaut pour des raisons de sécurité.

## Étape 3 : Création et configuration d'un réseau isolé avec Ubuntu Server

### Téléchargement et installation de Ubuntu Server

1. Téléchargez l'ISO de Ubuntu Server depuis le site officiel.
2. Installez Ubuntu Server avec les spécifications suivantes :
    - 1 core CPU, 2 GB de RAM.
    - 40 GB de disque, alloué dynamiquement.
3. Démarrez la VM et sélectionnez l'ISO de Ubuntu Server comme disque de démarrage.
4. Suivez les instructions à l'écran pour installer Ubuntu Server.

### Configuration du réseau pendant l'installation

1. Une fois Ubuntu Server installé, connectez-vous avec les identifiants créés lors de l'installation.
2. Mettez à jour le système avec les commandes :
    ```sh
    sudo apt update
    sudo apt upgrade
    ```

### Installation d'un GUI sur Ubuntu Server

1. Installez `tasksel` pour faciliter l'installation de groupes de paquets :
    ```sh
    sudo apt install tasksel
    ```
2. Installez le GUI Ubuntu Desktop :
    ```sh
    sudo tasksel install ubuntu-desktop
    ```
3. Redémarrez le système :
    ```sh
    sudo reboot
    ```

## Étape 4 : Installation et configuration d'iptables

### Installation d'iptables

1. Installez `iptables` pour améliorer la sécurité du réseau :
    ```sh
    sudo apt install iptables
    ```

### Activation de l'IP Forwarding

1. Modifiez le fichier de configuration sysctl :
    ```sh
    sudo nano /etc/sysctl.conf
    ```
2. Décommentez la ligne suivante :
    ```sh
    net.ipv4.ip_forward=1
    ```
3. Appliquez les modifications :
    ```sh
    sudo sysctl -p
    ```

### Configuration des règles iptables

1. Créez un script de règles iptables :
    ```sh
    sudo nano /etc/iptables/rules.v4
    ```
2. Ajoutez les règles suivantes :
    ```sh
    *filter
    :INPUT ACCEPT [0:0]
    :FORWARD ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    -A INPUT -p tcp --dport 22 -j ACCEPT
    -A INPUT -p icmp -j ACCEPT
    -A INPUT -j DROP
    COMMIT
    ```
3. Rendre le script exécutable :
    ```sh
    sudo chmod +x /etc/iptables/rules.v4
    ```
4. Redémarrez le réseau pour appliquer les modifications :
    ```sh
    sudo systemctl restart networking
    ```

### Sauvegarde des règles iptables

1. Sauvegardez les règles pour qu'elles soient appliquées au démarrage :
    ```sh
    sudo iptables-save | sudo tee /etc/iptables/rules.v4
    ```

## Étape 5 : Installation d'INetSim

1. Installez INetSim pour simuler des services falsifiés :
    ```sh
    sudo apt install inetsim
    ```
2. Configurez INetSim en modifiant le fichier `inetsim.conf` :
    ```sh
    sudo nano /etc/inetsim/inetsim.conf
    ```
3. Modifiez l'adresse de liaison des services à `0.0.0.0` et l'IP par défaut DNS à celle de votre serveur Ubuntu.
4. Désactivez `systemd-resolved` pour éviter les conflits DNS :
    ```sh
    sudo systemctl disable systemd-resolved
    sudo systemctl stop systemd-resolved
    ```
5. Redémarrez le serveur :
    ```sh
    sudo reboot
    ```

### Configuration des règles iptables pour DNS

1. Modifiez vos règles iptables pour accepter les requêtes DNS :
    ```sh
    sudo nano /etc/iptables/rules.v4
    ```
2. Ajoutez la règle suivante :
    ```sh
    -A INPUT -p udp --dport 53 -j ACCEPT
    ```

## Étape 6 : Configuration de la VM de stockage de fichiers

### Installation d'Ubuntu Desktop

1. Téléchargez et installez Ubuntu Desktop comme VM de stockage de fichiers.
2. Créez un répertoire à partager et installez Samba :
    ```sh
    sudo apt install samba
    ```

### Configuration de Samba

1. Configurez Samba :
    ```sh
    sudo nano /etc/samba/smb.conf
    ```
2. Ajoutez les lignes suivantes à la fin du fichier :
    ```sh
    [SharedFolder]
    comment = Shared Folder
    path = /home/username/shared
    read only = no
    browsable = yes
    guest ok = yes
    ```
3. Remplacez `username` par votre nom d'utilisateur.
4. Redémarrez le service Samba :
    ```sh
    sudo systemctl restart smbd
    ```

### Installation du serveur NFS

1. Installez le serveur NFS :
    ```sh
    sudo apt install nfs-kernel-server
    ```
2. Créez un répertoire à exporter via NFS :
    ```sh
    mkdir -p /home/username/nfs_shared
    ```
3. Configurez les exports NFS :
    ```sh


    sudo nano /etc/exports
    ```
4. Ajoutez la ligne suivante :
    ```sh
    /home/username/nfs_shared *(rw,sync,no_subtree_check,insecure)
    ```
5. Redémarrez le serveur NFS :
    ```sh
    sudo systemctl restart nfs-kernel-server
    ```

## Étape 7 : Connexion au partage Samba

1. Dans la VM Windows 10 Analysis, ouvrez l'Explorateur de fichiers (Ctrl + E).
2. Cliquez sur “Ce PC” puis sur l’onglet “Ordinateur” en haut.
3. Cliquez sur “Connecter un lecteur réseau”.
4. Entrez le chemin du partage Samba dans le champ “Dossier” (par exemple, \\192.168.1.5\SharedFolder).
5. Cliquez sur “Terminer” et entrez les identifiants si nécessaire.

## Étape 8 : Configuration de la VM de surveillance

### Installation d'Ubuntu Desktop

1. Téléchargez et installez Ubuntu Desktop comme VM de surveillance.
2. Installez Snort :
    ```sh
    sudo apt update
    sudo apt install snort
    ```

### Configuration de Snort

1. Configurez Snort en modifiant le fichier `snort.conf` :
    ```sh
    sudo nano /etc/snort/snort.conf
    ```
2. Modifiez la ligne `ipvar HOME_NET` avec votre réseau.
3. Téléchargez les règles Emerging Threats :
    ```sh
    sudo mkdir -p /etc/snort/rules/et_rules
    sudo wget https://rules.emergingthreats.net/open/snort-2.9.0/emerging.rules.tar.gz -P /etc/snort/rules/et_rules
    sudo tar -zxvf /etc/snort/rules/et_rules/emerging.rules.tar.gz -C /etc/snort/rules/et_rules
    ```
4. Configurez les règles locales :
    ```sh
    sudo nano /etc/snort/rules/local.rules
    ```
5. Ajoutez les règles de détection des comportements suspects.
6. Démarrez Snort en mode test :
    ```sh
    sudo snort -A console -q -c /etc/snort/snort.conf -i enp0s3
    ```

### Configuration du service Snort

1. Créez un script de service Snort :
    ```sh
    sudo nano /etc/systemd/system/snort.service
    ```
2. Ajoutez les lignes suivantes :
    ```sh
    [Unit]
    Description=Snort NIDS
    After=syslog.target network.target

    [Service]
    Type=simple
    ExecStart=/usr/sbin/snort -D -c /etc/snort/snort.conf -i enp0s3
    ExecReload=/bin/kill -HUP $MAINPID
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
3. Activez et démarrez le service Snort :
    ```sh
    sudo systemctl enable snort
    sudo systemctl start snort
    ```
4. Testez le service Snort pour s'assurer qu'il fonctionne sans erreur :
    ```sh
    sudo systemctl status snort
    ```

## Conclusion

Vous avez maintenant configuré un environnement virtuel sécurisé pour l'analyse des logiciels malveillants avec plusieurs VM isolées, des outils d'analyse, et des configurations réseau adaptées. Continuez à ajuster et améliorer votre environnement selon vos besoins spécifiques.

# Références : 
- https://medium.com/@piusppk/malware-analysis-home-lab-bbefe7d1c53b
- https://medium.com/@efamharris/my-first-attempt-at-building-a-simple-home-lab-for-threat-detection-and-monitoring-a0e6513e5432
- https://dev.to/dharmil18/man-in-the-middle-attack-mitm-part-1-arp-spoofing-3747
- https://dev.to/dharmil18/man-in-the-middle-attack-mitm-part-2-packet-sniffer-1nch
- https://www.malekal.com/iptables-comment-configurer-firewall-netfilter-linux/
- https://hackingeek.com/manipuler-des-machines-avec-le-framework-mitmf/
