### Accéder à un Téléphone Android Connecté à un Réseau Wi-Fi à des Fins Pédagogiques

Pour des raisons éducatives, il est possible de démontrer certaines vulnérabilités de sécurité sur un appareil Android. Ces méthodes doivent être utilisées de manière responsable et éthique, et uniquement sur des appareils dont vous avez la permission explicite d'accéder.

#### Étapes

1. **Préparation de l'environnement**
   - Assurez-vous d'avoir un appareil Android à tester.
   - Connectez-vous au même réseau Wi-Fi que l'appareil Android cible.

2. **Scanner le réseau pour trouver les appareils connectés**
   Utilisez `nmap` pour scanner le réseau et identifier les appareils connectés.

   ```bash
   nmap -sP 192.168.1.0/24
   ```

   - Remplacez `192.168.1.0/24` par la plage d'adresses IP de votre réseau.

3. **Identifier l'appareil Android dans la liste des appareils**
   Recherchez l'adresse MAC correspondant à un appareil Android. Les adresses MAC des appareils Android varient, mais vous pouvez souvent les reconnaître par le fabricant.

4. **Utiliser `adb` pour accéder à l'appareil Android**
   L'Android Debug Bridge (adb) est un outil puissant qui permet de communiquer avec un appareil Android. Vous devez activer le débogage USB sur l'appareil Android.

   - **Installer adb sur votre machine**
     ```bash
     sudo apt-get install adb
     ```

   - **Connecter adb à l'appareil Android via Wi-Fi**
     ```bash
     adb connect [Android_IP]
     ```

     - Remplacez `[Android_IP]` par l'adresse IP de l'appareil Android.

5. **Utiliser `adb` pour accéder à l'appareil**
   Une fois connecté, vous pouvez utiliser plusieurs commandes adb pour interagir avec l'appareil.

   - **Lister les appareils connectés**
     ```bash
     adb devices
     ```

   - **Ouvrir un shell sur l'appareil**
     ```bash
     adb shell
     ```

6. **Démonstration de commandes `adb`**

   - **Capturer une capture d'écran**
     ```bash
     adb shell screencap -p /sdcard/screen.png
     adb pull /sdcard/screen.png
     ```

   - **Transférer un fichier vers l'appareil**
     ```bash
     adb push local_file /sdcard/remote_file
     ```

   - **Extraire un fichier de l'appareil**
     ```bash
     adb pull /sdcard/remote_file local_file
     ```

#### Commandes Résumées

1. **Scanner le réseau**
   ```bash
   nmap -sP 192.168.1.0/24
   ```

2. **Identifier l'adresse IP de l'appareil Android**

3. **Installer adb sur votre machine**
   ```bash
   sudo apt-get install adb
   ```

4. **Connecter adb à l'appareil Android via Wi-Fi**
   ```bash
   adb connect [Android_IP]
   ```

5. **Lister les appareils connectés**
   ```bash
   adb devices
   ```

6. **Ouvrir un shell sur l'appareil**
   ```bash
   adb shell
   ```

7. **Capturer une capture d'écran**
   ```bash
   adb shell screencap -p /sdcard/screen.png
   adb pull /sdcard/screen.png
   ```

8. **Transférer un fichier vers l'appareil**
   ```bash
   adb push local_file /sdcard/remote_file
   ```

9. **Extraire un fichier de l'appareil**
   ```bash
   adb pull /sdcard/remote_file local_file
   ```

#### Remarques Importantes
- **Éthique et Légalité** : L'accès non autorisé à un appareil est illégal. Assurez-vous d'avoir la permission de l'utilisateur de l'appareil avant d'entreprendre toute action.
- **Débogage USB** : Le débogage USB doit être activé sur l'appareil Android pour utiliser adb. Cela peut nécessiter l'accès physique à l'appareil.
- **Responsabilité** : Utilisez ces techniques de manière responsable et uniquement à des fins éducatives ou de test de sécurité.
