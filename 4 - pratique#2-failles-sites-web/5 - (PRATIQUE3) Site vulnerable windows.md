
*Site web vulnérable sur WINDOWS*
# Téléchargez XAAMP ICI : # Télcharger XAAMP server

- XAAMP: https://drive.google.com/drive/folders/16whK3A7i7uN4A6ZvNuk-w3Zk6WgO_rKa?usp=sharing
- Site web : 
# 1 - outils
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/7d37db99-eb5a-48d0-b374-6c9e550b98fd)

# 2 - XAAMP
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/c3793813-f692-47d3-ac9d-b5e1a7afc49b)

# 3 - XAAMP interface
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/7f304a02-ddfd-4df4-ab72-02ddbbfdafab)

# 4 -
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/af721017-0b59-44df-a153-77f2057eedaf)

# 5 -
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/885abee0-de77-4751-9665-7d59c5bd96eb)

# 6 -
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/827ef920-3524-449d-a070-e3fe61326930)

# 7 - Racine du site
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/c7b4888a-0ffe-44af-9b2f-aa50f4a44826)


# 8 - création du dossier demo
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/e242e421-9cc8-4878-a187-bd7f6b41289d)

# 9 - copier les dossiers
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/e6720994-9446-4bc2-a8d3-9042bc3e3336)

# 10 - importer la base de données
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/a426bc8c-1012-46b1-845b-476079304db4)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/b5750ffc-bdce-4db2-83bd-d12a7e6c1d86)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/2eeb675d-0594-49aa-b516-e1e4c3baf755)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/00b61d53-27cd-4374-a1aa-ece2768dea79)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/fdcf6b21-11d4-4b06-9838-2d520ad887e9)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/aaff37f0-70e3-4d5d-ad00-bda027376310)

# 11 - importer la base de données
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/72728406-7718-45ed-b3ce-321252248ff0)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/130a8fe1-5b34-4e5f-9960-fcb9efb3adc3)




# Annexe :
- Pour monter un dossier partagé VirtualBox sur un système Windows à l'aide de PowerShell, vous pouvez utiliser la commande suivante. Cela suppose que les outils VirtualBox Guest Additions sont installés et que le dossier partagé est configuré dans VirtualBox.

1. **Assurez-vous que le dossier partagé est configuré dans VirtualBox:**
   - Allez dans les paramètres de votre machine virtuelle.
   - Sélectionnez "Shared Folders" (Dossiers partagés).
   - Ajoutez un nouveau dossier partagé (par exemple, `dossier1`) et assurez-vous de noter le nom que vous lui donnez.

2. **Montez le dossier partagé dans Windows:**

```powershell
# Nom du dossier partagé configuré dans VirtualBox
$sharedFolderName = "dossier1"

# Lettre du lecteur à utiliser pour monter le dossier partagé
$driveLetter = "Z:"

# Exécutez la commande pour monter le dossier partagé
net use $driveLetter \\vboxsvr\$sharedFolderName
```

Remplacez `dossier1` par le nom de votre dossier partagé configuré dans VirtualBox et `Z:` par la lettre de lecteur que vous souhaitez utiliser.

Cette commande montera le dossier partagé de VirtualBox en tant que lecteur réseau sur votre système Windows. Vous pouvez ensuite accéder à ce dossier via l'Explorateur de fichiers ou via la ligne de commande en utilisant la lettre de lecteur spécifiée (par exemple, `Z:`).




