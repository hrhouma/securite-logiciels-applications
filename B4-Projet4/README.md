# Module 5: Cryptographie


```bash
# Mettez à jour votre gestionnaire de paquets
sudo apt update

# Installez Python et pip
sudo apt install python3 python3-pip

# Installez virtualenv pour créer des environnements virtuels isolés
sudo pip3 install virtualenv

# Créez un environnement virtuel nommé 'hacker_ethique' dans votre répertoire de projet
virtualenv hacker_ethique

# Activez l'environnement virtuel
# Sur Linux et macOS :
source hacker_ethique/bin/activate
```


## Démo 1 – Chiffrement de César

1. **Téléchargement du fichier `caesar_cipher.py`**
   - Assurez-vous d'avoir téléchargé le fichier `caesar_cipher.py` depuis votre GitHub dossier fichiers.

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
   - Assurez-vous d'avoir téléchargé le fichier `des.py` depuis votre GitHub dossier fichiers.

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
   - Assurez-vous d'avoir téléchargé le fichier `aes_d.py` depuis votre GitHub dossier fichiers.

2. **Exécution du fichier `aes_d.py`**
   - Ouvrez votre terminal.
   - Naviguez jusqu'au répertoire où se trouve `aes_d.py`.
   - Exécutez la commande suivante :
     ```bash
     pip install pycryptodome
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
   - Assurez-vous d'avoir téléchargé le fichier `known_plaintext_attack.py` depuis votre GitHub dossier fichiers.

2. **Exécution du fichier `known_plaintext_attack.py`**
   - Ouvrez votre terminal.
   - Naviguez jusqu'au répertoire où se trouve `known_plaintext_attack.py`.
   - Exécutez la commande suivante :
     ```bash
     python known_plaintext_attack.py
     ```
   - Suivez les instructions affichées pour réaliser l'attaque par texte en clair connu.


# Explications Approfondies des Démonstrations Cryptographiques

# Démo 1 – Chiffrement de César
Le chiffrement de César est une méthode de cryptographie symétrique simple où chaque lettre du texte est décalée d'un certain nombre de positions dans l'alphabet. Par exemple, avec un décalage de 3, 'A' devient 'D', 'B' devient 'E', et ainsi de suite. La force de ce chiffrement réside dans la simplicité de sa mise en œuvre, mais il est vulnérable aux attaques par force brute ou analyse de fréquence.

# Démo 2 – DES (Data Encryption Standard)
DES est un algorithme de chiffrement par bloc qui utilise une clé de 56 bits pour chiffrer les données en blocs de 64 bits. Bien qu'ancien et considéré comme vulnérable à cause de la petite taille de sa clé (permettant des attaques par force brute), il a été largement utilisé et reste instructif pour comprendre les concepts de base du chiffrement symétrique et des modes d'opération des blocs.

# Démo 3 – AES (Advanced Encryption Standard)
AES est le successeur de DES, utilisant des clés de 128, 192 ou 256 bits pour chiffrer les données en blocs de 128 bits. Cet algorithme est actuellement l'un des standards de chiffrement les plus sûrs et les plus utilisés, employé tant dans les applications gouvernementales que commerciales. Il est résistant à toutes les attaques connues, à l'exception de celles par force brute contre les clés les plus courtes.

# Démo 4 – Génération de Hash
Le hachage est utilisé pour créer une empreinte digitale unique d'un ensemble de données. MD5 et SHA512 sont des fonctions de hachage cryptographiques. MD5 produit un hachage de 128 bits, mais il est considéré comme vulnérable à certaines attaques et donc moins sécurisé. SHA512 est une fonction de hachage plus robuste produisant un hachage de 512 bits, offrant une sécurité accrue pour les applications modernes.

# Démo 5 – Identification de Hash
Identifier le type d'algorithme de hachage utilisé pour un hash donné est crucial dans les tests de sécurité pour comprendre les vulnérabilités potentielles. Des outils comme `hash-identifier` aident à reconnaître le type de hash basé sur des caractéristiques et des longueurs spécifiques.

# Démo 6 – Signature numérique d'un fichier
La signature numérique permet de vérifier l'authenticité et l'intégrité d'un document. Elle utilise des clés publiques et privées pour permettre à l'émetteur de signer numériquement un document et au destinataire de vérifier la signature. Ce processus est essentiel pour des communications sécurisées et la validation de l'identité des parties dans les transactions numériques.

# Démo 7 – Attaque par texte en clair connu
Cette démonstration illustre une méthode d'attaque où l'attaquant possède à la fois un échantillon de texte en clair et son équivalent chiffré. L'objectif est d'exploiter cette information pour dériver la clé cryptographique utilisée ou pour obtenir plus d'informations sur l'algorithme de chiffrement. Cela démontre la nécessité de sécuriser non seulement les clés mais aussi les schémas de chiffrement contre de telles vulnérabilités.

- Chaque démonstration couvre un aspect différent de la cryptographie, offrant aux étudiants une vue d'ensemble des méthodes, de leur application, et de leur sécurité. Ces exemples pratiques renforcent la compréhension des principes fondamentaux de la cryptographie tout en exposant les élèves à des techniques de cryptanalyse et de sécurisation des données.
