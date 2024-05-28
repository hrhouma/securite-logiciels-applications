# README pour l'installation de Metasploitable 2.0 sur VirtualBox

# Références: 

- https://medium.com/@dangerhulk26022022/installing-metasploitable-2-in-virtual-box-for-windows-host-bf0a5b4f8375
- https://ambhalerao12.medium.com/how-to-install-metasploitable-on-virtual-box-5e9220a2041a
- https://www.geeksforgeeks.org/how-to-install-metasploitable-2-in-virtualbox/
  
## Prérequis
- **VirtualBox** doit être installé sur votre machine. Téléchargez-le depuis le [site officiel de VirtualBox](https://www.virtualbox.org/).
- **Image Metasploitable 2.0** téléchargée (fichier `.vmdk`) depuis sourceforge : https://sourceforge.net/projects/metasploitable/.

## Instructions d'installation

### Création d'une nouvelle machine virtuelle

1. **Ouvrir VirtualBox et créer une nouvelle machine virtuelle :**
   - Cliquez sur `Nouvelle` pour créer une nouvelle machine virtuelle.

2. **Configurer les paramètres de la machine virtuelle :**
   - **Nom :** Metasploitable2.0
   - **Dossier :** Choisissez l'emplacement où vous souhaitez enregistrer la VM.
   - **Type :** Linux
   - **Version :** Debian 11 Bullseye (32-bit)
   - Cliquez sur `Suivant`.

3. **Attribuer de la mémoire (RAM) :**
   - Définissez la mémoire de base (RAM) à au moins 2048 Mo (2 Go).
   - Cliquez sur `Suivant`.

4. **Configurer le disque dur virtuel :**
   - Sélectionnez `Utiliser un fichier de disque dur virtuel existant`.
   - Cliquez sur l'icône du dossier et sélectionnez le fichier `.vmdk` de Metasploitable 2.0 téléchargé.
   - Cliquez sur `Créer`.

### Configuration avancée de la machine virtuelle

5. **Ajouter un disque dur supplémentaire :**
   - Sélectionnez la machine virtuelle Metasploitable2.0 et cliquez sur `Configuration`.
   - Allez dans `Stockage`.
   - Cliquez sur le contrôleur `IDE`, puis sur l'icône d'ajout de disque dur (comme indiqué dans la deuxième image téléchargée).
   - Choisissez `Créer un nouveau disque dur`.
   - Sélectionnez `VDI (VirtualBox Disk Image)` et cliquez sur `Suivant`.
   - Sélectionnez `Alloué dynamiquement` et cliquez sur `Suivant`.
   - Définissez la taille du disque dur virtuel à au moins 8 Go et cliquez sur `Créer`.

### Configuration réseau

6. **Configurer les paramètres réseau :**
   - Allez dans `Réseau`.
   - Assurez-vous que `Adapter 1` est activé et attaché à `Adaptateur Ponté`.
   - Cliquez sur `Avancé` et définissez le mode de promiscuité sur `Autoriser tout`.
   - Cliquez sur `OK` pour enregistrer les paramètres.

### Démarrage de la machine virtuelle

7. **Démarrer la machine virtuelle :**
   - Sélectionnez la machine virtuelle Metasploitable2.0 et cliquez sur `Démarrer`.

8. **Connexion à Metasploitable 2.0 :**
   - Nom d'utilisateur : `msfadmin`
   - Mot de passe : `msfadmin`

## Ressources supplémentaires
- https://www.geeksforgeeks.org/how-to-install-metasploitable-2-in-virtualbox/
