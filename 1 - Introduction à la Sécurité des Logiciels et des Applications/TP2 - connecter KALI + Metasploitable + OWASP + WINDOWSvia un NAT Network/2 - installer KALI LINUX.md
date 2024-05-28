# README pour l'installation de Kali 2024 personnalisé par zSecurity

## Instructions d'installation

### VirtualBox (64 bits)
1. **Télécharger et installer VirtualBox :**
   - Assurez-vous que VirtualBox est installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger depuis le [site officiel de VirtualBox](https://www.virtualbox.org/).

2. **Télécharger l'image Kali 2024 64 bits :**
   - Utilisez les liens fournis pour télécharger l'image :
   - https://zsecurity.org/download-custom-kali/


3. **Importer la machine virtuelle :**
   - Ouvrez VirtualBox.
   - Allez dans `Fichier` > `Importer une appliance`.
   - Sélectionnez le fichier `.ova` téléchargé.
   - Cliquez sur `Suivant` et suivez les instructions pour importer l'appliance.

4. **Ou deuxième méthode  :**

4.1. **Créer une nouvelle machine virtuelle :**
   - Ouvrez VirtualBox et cliquez sur `Nouvelle` pour créer une nouvelle machine virtuelle.

4.2. **Configurer la machine virtuelle :**
   - Remplissez les champs comme suit :
     - **Nom :** Kali2024
     - **Dossier :** L'emplacement où vous souhaitez enregistrer la VM.
     - **Type :** Linux
     - **Version :** Linux (64-bit) ou Debian (64-bit)
   - Cliquez sur `Suivant`.

4.3. **Attribuer de la mémoire (RAM) :**
   - Définissez la mémoire de base (RAM) à au moins 2048 Mo (2 Go), puis cliquez sur `Suivant`.

4.4. **Créer un disque dur virtuel :**
   - Sélectionnez `Créer un disque dur virtuel maintenant`, puis cliquez sur `Créer`.
   - Choisissez `VDI (VirtualBox Disk Image)` et cliquez sur `Suivant`.
   - Sélectionnez `Alloué dynamiquement` et cliquez sur `Suivant`.
   - Définissez la taille du disque dur virtuel à au moins 20 Go et cliquez sur `Créer`.

4.5. **Configurer le disque dur virtuel avec l'ISO de Kali :**
   - Sélectionnez la machine virtuelle Kali2024 nouvellement créée et cliquez sur `Configuration`.
   - Allez dans `Stockage`, cliquez sur le vide sous `Contrôleur IDE`.
   - Cliquez sur l'icône de disque à droite et sélectionnez `Choisir un fichier de disque` puis sélectionnez l'image ISO de Kali 2024 que vous avez téléchargée.


5. **Ou troisième méthode  : choisir le fichier ISO depuis le début :**
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/e177dc8f-46ff-463e-8dbe-739dcf50afcb)
     
6. **Configurer la machine virtuelle :**
   - Une fois l'importation terminée, sélectionnez la machine virtuelle Kali nouvellement ajoutée.
   - Cliquez sur `Configuration` pour personnaliser les paramètres de la machine virtuelle.
     - **Système :**
       - Assurez-vous que la mémoire de base (RAM) est définie à au moins 2048 Mo (2 Go).
       - Activez les fonctionnalités de virtualisation matérielle si disponibles.
     - **Réseau :**
       - Choisissez `Adaptateur Ponté` si vous souhaitez que la VM fasse partie du même réseau que la machine hôte.
     - **Affichage :**
       - Augmentez la mémoire vidéo à au moins 128 Mo pour de meilleures performances.

7. **Démarrer la machine virtuelle :**
   - Sélectionnez la machine virtuelle Kali.
   - Cliquez sur `Démarrer` pour lancer la VM.

8. **Connexion :**
   - Nom d'utilisateur : `root`
   - Mot de passe : `toor`

## Ressources supplémentaires
- Pour des étapes plus détaillées, référez-vous au cours d'installation dans le cours zSecurity.
- La [documentation VirtualBox](https://www.virtualbox.org/manual/UserManual.html) peut fournir une aide supplémentaire si nécessaire.

## Contact et Support
Pour toute question, veuillez contacter [info@zsecurity.org](mailto:info@zsecurity.org).

Découvrez notre [adhésion VIP](https://example.com) pour un accès direct à Zaid et à l'équipe de zSecurity, des sessions de hacking en direct, des CTF, des compétitions, et plus encore !

Restez à jour avec les dernières nouveautés en matière de sécurité informatique et de hacking éthique en nous suivant sur les réseaux sociaux.

## zSecurity
- [Accueil](https://example.com)
- [À propos de nous](https://example.com)
- [Articles sur la sécurité et le hacking](https://example.com)
- [Télécharger Kali personnalisé](https://example.com)
- [Contactez-nous](https://example.com)
- [FAQ](https://example.com)

### Services
- Tests de pénétration
- Consulting
- Revue de code
- Formation individuelle
- VPN
- Adhésion VIP
