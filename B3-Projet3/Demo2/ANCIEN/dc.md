Le fichier `encrypted_hosts.txt` que nous reçevons contient une ligne avec le format suivant :

```
MSEDGEWIN10 : SlqtEOBKCbYN{G}tWT.xjctgaCIyBXSQ.Te}]eQW?{j,nsLD<fE?]g<lGDvORc>U
```

### Explication du Contenu

1. **`MSEDGEWIN10` :** C'est le nom d'hôte de la machine attaquée. Cela permet d'identifier quelle machine a été chiffrée.

2. **`SlqtEOBKCbYN{G}tWT.xjctgaCIyBXSQ.Te}]eQW?{j,nsLD<fE?]g<lGDvORc>U` :** C'est la clé de chiffrement générée pour cette machine. Cette clé est utilisée pour chiffrer et pourra être utilisée pour déchiffrer les fichiers.

### Étapes Suivantes

1. **Vérification des Fichiers Chiffrés :**
   - Sur la machine attaquée, assurez-vous que les fichiers sur le bureau sont chiffrés et ne peuvent plus être lus en clair.

2. **Déchiffrement des Fichiers :**
   - Utilisez la clé reçue (`SlqtEOBKCbYN{G}tWT.xjctgaCIyBXSQ.Te}]eQW?{j,nsLD<fE?]g<lGDvORc>U`) pour déchiffrer les fichiers. Vous pouvez créer un script de déchiffrement similaire au script de chiffrement mais inversant le processus.

### Script de Déchiffrement (dc.py)

Voici un exemple de script pour déchiffrer les fichiers :

```python
import os
import threading
import queue
import logging

# Configurer le logging
logging.basicConfig(filename='decryption.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Fonction de déchiffrement
def decrypt(file, key):
    try:
        key_index = 0
        max_key_index = len(key) - 1
        decrypted_data = bytearray()
        
        with open(file, 'rb') as f:
            data = f.read()
        
        for byte in data:
            xor_byte = byte ^ ord(key[key_index])
            decrypted_data.append(xor_byte)
            
            # Incrémenter l'index de la clé
            if key_index >= max_key_index:
                key_index = 0
            else:
                key_index += 1
        
        with open(file, 'wb') as f:
            f.write(decrypted_data)
        
        logging.info(f'{file} successfully decrypted')
    except Exception as e:
        logging.error(f'Failed to decrypt {file}: {e}')
        print(f'Failed to decrypt {file}: {e}')

# Informations sur le chiffrement
ENCRYPTION_LEVEL = 64  # 64 bytes for 512-bit encryption

# Préparer les fichiers à déchiffrer
print("Preparing files...")
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(os.path.join(desktop_path, f)) and f != __file__[:-2] + 'exe':
        abs_files.append(os.path.join(desktop_path, f))
print("Successfully located all files!")

# Demander la clé de déchiffrement
key = input("Please enter the decryption key: ")

# Créer la file d'attente des fichiers à déchiffrer
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Configurer les threads pour le déchiffrement
for i in range(10):
    t = threading.Thread(target=lambda q, arg1: decrypt(q.get(), arg1), args=(q, key), daemon=True)
    t.start()

q.join()
print('Decryption complete!!!')
input()
```

### Instructions pour le Déchiffrement

1. **Exécutez le script de déchiffrement (`dc.py`) sur la machine attaquée.**
2. **Entrez la clé de déchiffrement lorsque le script le demande (`SlqtEOBKCbYN{G}tWT.xjctgaCIyBXSQ.Te}]eQW?{j,nsLD<fE?]g<lGDvORc>U`).**
3. **Vérifiez que les fichiers sur le bureau sont maintenant lisibles.**

En utilisant ces scripts et cette clé, vous devriez être en mesure de déchiffrer les fichiers chiffrés sur la machine attaquée.
