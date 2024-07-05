#  Installation de Metasploitable2 sur Ubuntu22.04 (OPTIONNEL)
# Création du fichier d'installation
- nano install_metasploitable.sh
- copier/coller le contenu suivante puis faire CTL+X

# Exécution du script
```bash
#!/bin/bash

# Mettre à jour le système
sudo apt update && sudo apt upgrade -y

# Installer les paquets nécessaires
sudo apt install -y wget curl nano ufw software-properties-common dirmngr apt-transport-https gnupg2 ca-certificates lsb-release ubuntu-keyring unzip

# Installer Nmap
sudo apt install -y nmap

# Créer un répertoire temporaire pour l'installation de Metasploit et y accéder
mkdir msf-install && cd msf-install

# Télécharger le script d'installation de Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall

# Donner les permissions d'exécution au script
chmod 755 msfinstall

# Exécuter le script d'installation
sudo ./msfinstall

# Lancer la console Metasploit pour terminer l'installation
msfconsole

# Configurer la base de données pour Metasploit
echo "Would you like to use and setup a new database (recommended)? (y/n)"
read setup_db
if [ "$setup_db" = "y" ]; then
  msfdb init
fi

# Installation terminée, vérifier l'état de la base de données
msfconsole -q -x "db_status; exit"

echo "Installation de Metasploit terminée. Vous pouvez lancer Metasploit avec la commande 'msfconsole'."

# Retourner au répertoire initial
cd ..

# Supprimer le répertoire temporaire d'installation
rm -rf msf-install
```

Ce script effectue les étapes suivantes :

1. Mise à jour du système.
2. Installation des paquets nécessaires.
3. Installation de Nmap.
4. Création d'un répertoire temporaire pour l'installation de Metasploit.
5. Téléchargement et exécution du script d'installation de Metasploit.
6. Lancement de la console Metasploit et configuration de la base de données.
7. Nettoyage des fichiers temporaires.

Pour exécuter ce script, enregistrez-le dans un fichier, par exemple `install_metasploitable.sh`, rendez-le exécutable avec `chmod +x install_metasploitable.sh`, puis exécutez-le avec `./install_metasploitable.sh`.
