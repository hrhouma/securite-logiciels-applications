# README - Évaluation Formative

## Étape 0 - Installation de Windows VM

### Téléchargement de la VM
- Téléchargez la VM Windows depuis ce lien : [MSW10.zip](https://cyberini.com/ressources-cours-hacking-ethique/MSW10.zip)
- Si vous rencontrez des erreurs de mot de passe, téléchargez la machine à partir de ce lien alternatif : [Google Drive](https://drive.google.com/drive/folders/1yu2q85JJjoKS9726tHLgeIt7zWg56ZEQ?usp=sharing)
- Utilisez [WinRAR](https://winrar.fr.softonic.com/) pour décompresser le fichier. Mot de passe : `lbdh`
- Désactivez le pare-feu de la VM Windows.

Pour plus d’informations, consultez :
[sécurité-logiciels-applications/1 - Introduction à la Sécurité des Logiciels et des Applications/TP1 - connecter 3 machines via un NAT Network/1-machinewindows.md](https://github.com/hrhouma/securite-logiciels-applications)

## Étape 1 : Télécharger les logiciels sur votre hôte

Téléchargez tous les logiciels nécessaires à partir de ce lien : [0 - Tous les logiciels - Google Drive](https://drive.google.com/drive/folders/1yu2q85JJjoKS9726tHLgeIt7zWg56ZEQ?usp=sharing)

## Étape 2 : Transférer les fichiers à la VM

Placez les fichiers dans votre dossier partagé pour y accéder via la VM Windows.

- **Machine hôte Windows** : Mettez les fichiers dans le dossier partagé avec la VM Windows.
- **Machine invité Windows** : Accédez aux fichiers depuis la machine virtuelle Windows.

## Étape 3: Installer XAMPP dans votre VM Windows

Installez XAMPP en suivant les étapes suivantes :
- Cliquez sur suivant, suivant...

## Étape 4: Copier le dossier du site web dans XAMPP

1. Allez au chemin `C:\xampp`
2. Entrez dans le dossier `htdocs`
3. Créez un dossier nommé `demobeef1`
4. Collez le site web décompressé dans le dossier `demobeef1`

## Étape 5: Installation de la base de données

1. Démarrez XAMPP.
2. Ouvrez votre navigateur et allez à l'adresse : [http://localhost/phpmyadmin/](http://localhost/phpmyadmin/)
3. Cliquez sur `Database`.
4. Donnez un nom à la base de données `demobdd` et cliquez sur `Create`.
5. Sélectionnez la base de données `demobdd`, puis cliquez sur `Import`.
6. Choisissez le fichier `demobdd.sql`.
7. Cliquez sur `Go`.

## Étape 6: Affichage du site web

1. Ouvrez votre navigateur et entrez l'adresse suivante : [http://localhost/demobeef1/](http://localhost/demobeef1/)

Félicitations, vous avez maintenant un site web vulnérable !

## Étape 7: Travailler avec BeEF

1. Installez Kali Linux à partir de ce lien : [Download Custom Kali - zSecurity](https://zsecurity.org/downloads/)
2. L'installation est très simple : double-cliquez sur le fichier téléchargé avec l'extension `.ova`, puis cliquez sur suivant, suivant, etc.
3. Démarrez la machine Kali Linux.
4. Assurez-vous que les machines sont connectées en Nat Network.
5. Démarrez BeEF sur Kali Linux.
6. Lors du premier lancement, changez le mot de passe. Par exemple, changez-le en `beef_`.
   - Nom d'utilisateur : `beef`
   - Mot de passe : `beef_`
7. Une fois BeEF démarré, accédez à l'interface suivante : [http://127.0.0.1:3000/ui/panel](http://127.0.0.1:3000/ui/panel)

---

Vous avez maintenant configuré une machine Windows vulnérable et installé BeEF sur Kali Linux pour tester des exploits. Bonne chance !
