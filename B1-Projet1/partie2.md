# Guide détaillé pour ajouter une attaque Man-in-the-Middle (MiTM) à l'environnement de laboratoire

## Introduction

Dans cette section, nous allons ajouter un scénario d'attaque Man-in-the-Middle (MiTM) à notre laboratoire virtuel existant. Une attaque MiTM permet à un attaquant d'intercepter, modifier et injecter des messages entre deux parties qui croient communiquer directement entre elles. Pour ce laboratoire, nous allons utiliser `Ettercap`, un outil puissant pour les attaques MiTM, sur notre VM de surveillance (Ubuntu Desktop).

### Objectifs

1. **Comprendre les attaques MiTM** : Apprendre comment une attaque MiTM fonctionne et les implications sur la sécurité.
2. **Configurer l'outil Ettercap** : Installer et configurer Ettercap sur la VM de surveillance.
3. **Effectuer une attaque MiTM** : Mettre en place un scénario d'attaque MiTM pour intercepter et modifier le trafic réseau entre la VM Windows (analyse) et la VM de stockage de fichiers.
4. **Analyser les résultats** : Examiner les données capturées et comprendre les risques associés à une attaque MiTM.

### Prérequis

- VM de surveillance (Ubuntu Desktop) configurée et fonctionnelle.
- VM Windows (analyse) et VM de stockage de fichiers configurées et fonctionnelles.
- Configuration réseau isolée avec IP forwarding activé et règles iptables configurées.

### Schéma du Scénario

1. **VM Windows 10 (Analyse)** : Adresse IP `192.168.1.10`
2. **VM Ubuntu Server (Réseau isolé)** : Adresse IP `192.168.1.1`
3. **VM Ubuntu Desktop (Stockage de fichiers)** : Adresse IP `192.168.1.20`
4. **VM Ubuntu Desktop (Surveillance)** : Adresse IP `192.168.1.30`

```
             +----------------------+
             |  VM Windows 10       |
             |  (Analyse)           |
             |  192.168.1.10        |
             +----------+-----------+
                        |
                        | (Trafic intercepté)
                        |
             +----------+-----------+
             |  VM Ubuntu Desktop   |
             |  (Surveillance)      |
             |  192.168.1.30        |
             +----------+-----------+
                        |
                        | (Trafic intercepté)
                        |
             +----------+-----------+
             |  VM Ubuntu Desktop   |
             |  (Stockage de Fichiers) |
             |  192.168.1.20        |
             +----------------------+
```

## Étape 1 : Installation de Ettercap

1. Connectez-vous à la VM de surveillance (Ubuntu Desktop).
2. Ouvrez un terminal et exécutez les commandes suivantes pour mettre à jour les paquets et installer Ettercap :
    ```sh
    sudo apt update
    sudo apt install ettercap-graphical
    ```

## Étape 2 : Configuration de Ettercap

1. Lancez Ettercap en mode graphique :
    ```sh
    sudo ettercap -G
    ```
2. Configurez Ettercap pour écouter sur l'interface réseau appropriée (par exemple, `eth0` ou `enp0s3`).

### Configuration des interfaces réseau

1. Dans l'interface graphique de Ettercap, allez dans **Sniff** -> **Unified sniffing**.
2. Sélectionnez l'interface réseau appropriée et cliquez sur **OK**.

### Configuration de l'attaque ARP Poisoning

1. Dans Ettercap, allez dans **Mitm** -> **ARP poisoning**.
2. Cochez les cases “Sniff remote connections” et “OK”.

## Étape 3 : Exécution de l'attaque MiTM

### Exemple concret : Interception d'une requête HTTP

1. **Scanner le réseau** : Identifiez les adresses IP des machines cibles (VM Windows et VM de stockage de fichiers).
    - Allez dans **Hosts** -> **Scan for hosts** pour scanner le réseau.
    - Allez dans **Hosts** -> **Hosts list** pour voir les adresses IP des hôtes détectés.
2. **Sélectionner les cibles** :
    - Ajoutez l'adresse IP de la VM Windows (analyse) comme cible 1 en la sélectionnant et en cliquant sur **Add to Target 1**.
    - Ajoutez l'adresse IP de la VM de stockage de fichiers comme cible 2 en la sélectionnant et en cliquant sur **Add to Target 2**.
3. **Lancer l'attaque** :
    - Allez dans **Mitm** -> **ARP poisoning** et cliquez sur **OK** pour lancer l'attaque.

### Exemple de scénario d'interception

1. **Envoi de la requête HTTP** :
    - Depuis la VM Windows 10 (analyse), ouvrez un navigateur web et accédez à une page web hébergée sur la VM de stockage de fichiers (par exemple, `http://192.168.1.20/page.html`).
2. **Interception du trafic** :
    - Ettercap sur la VM de surveillance interceptera le trafic HTTP entre les deux VM.
3. **Analyse des paquets interceptés** :
    - Dans Ettercap, allez dans **View** -> **Connections** pour voir les connexions interceptées.
    - Cliquez sur une connexion HTTP pour voir les requêtes et réponses en texte clair.

### Exemple concret d'interception HTTP

1. Sur la VM Windows (analyse), ouvrez un navigateur et accédez à `http://192.168.1.20/index.html`.
2. Sur la VM de surveillance, Ettercap affiche la requête HTTP interceptée :
    ```
    GET /index.html HTTP/1.1
    Host: 192.168.1.20
    User-Agent: Mozilla/5.0
    ```
3. La réponse interceptée peut ressembler à ceci :
    ```
    HTTP/1.1 200 OK
    Content-Type: text/html
    ...
    <html>
    <head><title>Page Test</title></head>
    <body>Bienvenue sur la page de test</body>
    </html>
    ```

### Modification des données interceptées

1. Vous pouvez modifier le contenu de la réponse HTTP pour injecter du code malveillant ou altérer les données.
2. Par exemple, remplacer le contenu de la page avec un script JavaScript malveillant.

## Étape 4 : Analyse des résultats

1. Une fois l'attaque en cours, Ettercap commencera à intercepter le trafic entre les deux VM.
2. Allez dans **View** -> **Connections** pour voir les connexions interceptées.
3. Cliquez sur une connexion pour voir les paquets interceptés. Vous pouvez également utiliser des filtres pour cibler des types de trafic spécifiques (par exemple, HTTP, FTP).

## Étape 5 : Mitigation et bonnes pratiques

1. **Utiliser HTTPS** : Encouragez l'utilisation de HTTPS pour chiffrer les communications et prévenir les attaques MiTM.
2. **Configurer des filtres ARP** : Utilisez des filtres ARP statiques pour prévenir les empoisonnements ARP.
3. **Surveiller le réseau** : Utilisez des outils de détection d'intrusion pour surveiller les activités suspectes sur le réseau.

## Conclusion

Vous avez maintenant configuré et exécuté une attaque Man-in-the-Middle (MiTM) dans un environnement virtuel sécurisé. Ce laboratoire vous a permis de comprendre les mécanismes des attaques MiTM, de configurer des outils d'attaque, et d'analyser les résultats pour mieux appréhender les risques et les mesures de mitigation nécessaires. En suivant ce guide, vous êtes capable de simuler une attaque MiTM, d'intercepter et de modifier le trafic réseau pour des fins éducatives et de sensibilisation à la sécurité.

---

### Pour toute question supplémentaire ou demande d'assistance, n'hésitez pas à me contacter. Bon apprentissage !
