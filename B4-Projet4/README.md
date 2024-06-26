# Module 5: Cryptographie

## Démo 1 – Chiffrement de César

1. **Téléchargement du fichier `caesar_cipher.py`**
   - Assurez-vous d'avoir téléchargé le fichier `caesar_cipher.py` depuis votre LMS.

2. **Exécution du fichier `caesar_cipher.py`**
   - Ouvrez votre terminal.
   - Naviguez jusqu'au répertoire où se trouve `caesar_cipher.py`.
   - Exécutez la commande suivante :
     ```bash
     python caesar_cipher.py
     ```
   - Suivez les instructions affichées pour chiffrer ou déchiffrer un texte.

## Démo 2 – DES (Data Encryption Standard)

1. **Téléchargement du fichier `des.py`**
   - Assurez-vous d'avoir téléchargé le fichier `des.py` depuis votre LMS.

2. **Exécution du fichier `des.py`**
   - Ouvrez votre terminal.
   - Naviguez jusqu'au répertoire où se trouve `des.py`.
   - Exécutez la commande suivante :
     ```bash
     python des.py
     ```
   - Suivez les instructions affichées pour chiffrer ou déchiffrer un texte.

## Démo 3 – AES (Advanced Encryption Standard)

1. **Téléchargement du fichier `aes_d.py`**
   - Assurez-vous d'avoir téléchargé le fichier `aes_d.py` depuis votre LMS.

2. **Exécution du fichier `aes_d.py`**
   - Ouvrez votre terminal.
   - Naviguez jusqu'au répertoire où se trouve `aes_d.py`.
   - Exécutez la commande suivante :
     ```bash
     python aes_d.py
     ```
   - Suivez les instructions affichées pour chiffrer ou déchiffrer un texte.

## Démo 4 – Génération de Hash

1. **Problème 1: Générer le hash MD5 d'un fichier texte**
   - Syntaxe :
     ```bash
     md5sum <nom_fichier> > <nom_fichier_hash>
     ```
   - Exemple de commande :
     ```bash
     md5sum a.txt > md5.hash
     ```

2. **Problème 2: Générer le hash SHA512 d'un fichier texte**
   - Syntaxe :
     ```bash
     sha512sum <nom_fichier> > <nom_fichier_hash>
     ```
   - Exemple de commande :
     ```bash
     sha512sum a.txt > sha.hash
     ```

## Démo 5 – Identification de Hash

1. **Identification de l'algorithme de hachage à partir d'un hash donné**
   - Ouvrez votre terminal.
   - Exécutez la commande suivante :
     ```bash
     hash-identifier
     ```
   - Entrez le hash et appuyez sur Entrée.
   - L'outil affichera la liste des types de hash les plus probables.

## Démo 6 – Signature numérique d'un fichier

1. **Génération des clés pour la signature numérique**
   - Ouvrez votre terminal.
   - Exécutez la commande suivante pour générer une clé :
     ```bash
     gpg --full-generate-key
     ```
   - Suivez les instructions pour sélectionner l'algorithme, entrer la taille de la clé, la validité, les détails requis et le mot de passe.
   - Les clés seront générées.

2. **Signer un fichier avec la signature numérique**
   - Syntaxe :
     ```bash
     gpg --sign <nom_fichier>
     ```
   - Exemple de commande :
     ```bash
     gpg --sign a.txt
     ```
   - Entrez votre mot de passe lorsque cela est demandé. Un fichier avec l'extension `.gpg` sera généré.

## Démo 7 – Attaque par texte en clair connu

1. **Téléchargement du fichier `known_plaintext_attack.py`**
   - Assurez-vous d'avoir téléchargé le fichier `known_plaintext_attack.py` depuis votre LMS.

2. **Exécution du fichier `known_plaintext_attack.py`**
   - Ouvrez votre terminal.
   - Naviguez jusqu'au répertoire où se trouve `known_plaintext_attack.py`.
   - Exécutez la commande suivante :
     ```bash
     python known_plaintext_attack.py
     ```
   - Suivez les instructions affichées pour réaliser l'attaque par texte en clair connu.

