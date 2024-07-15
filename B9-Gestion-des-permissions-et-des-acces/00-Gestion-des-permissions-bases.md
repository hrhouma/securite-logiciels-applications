🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# Partie 1 - Introduction aux Permissions Unix/Linux
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
Dans Unix et Linux, chaque fichier et répertoire est doté de permissions qui contrôlent l'accès en lecture (`r`), écriture (`w`), et exécution (`x`) pour trois catégories d'utilisateurs : le propriétaire du fichier, le groupe auquel appartient le fichier, et les autres utilisateurs.

### Tableau des Permissions

| Permission | Code Binaire | Code Octal | Description                    |
|------------|--------------|------------|--------------------------------|
| ---        | 000          | 0          | Aucune permission              |
| --x        | 001          | 1          | Permission d'exécution         |
| -w-        | 010          | 2          | Permission d'écriture          |
| -wx        | 011          | 3          | Écriture et exécution          |
| r--        | 100          | 4          | Permission de lecture          |
| r-x        | 101          | 5          | Lecture et exécution           |
| rw-        | 110          | 6          | Lecture et écriture            |
| rwx        | 111          | 7          | Lecture, écriture, et exécution|

### Modification des Permissions avec `chmod`

La commande `chmod` est utilisée pour changer les permissions d'un fichier ou d'un répertoire. Vous pouvez spécifier les permissions soit en notation octale, soit par un ensemble de lettres (`r`, `w`, `x` ajoutées ou soustraites).

#### Exemples de Commandes

- **Donner à tous les utilisateurs les droits de lecture et exécution sur un fichier :**
  ```bash
  chmod 755 fichier
  ```

- **Retirer les droits d'écriture pour le groupe et les autres sur un fichier :**
  ```bash
  chmod go-w fichier
  ```
  
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# Partie 2 - Tableau des Permissions Unix/Linux - Utilisation de `chmod`
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇


L'objectif est de comprendre l'utilisation de `chmod` en expliquant de manière approfondie ce que signifient les codes numériques et comment ils se traduisent en permissions. 


### Tableau Détaillé des Permissions Unix/Linux

| Permission | Code Binaire | Code Octal | Description                          |
|------------|--------------|------------|--------------------------------------|
| ---        | 000          | 0          | Aucune permission                    |
| --x        | 001          | 1          | Permission d'exécution uniquement    |
| -w-        | 010          | 2          | Permission d'écriture uniquement     |
| -wx        | 011          | 3          | Écriture et exécution                |
| r--        | 100          | 4          | Permission de lecture uniquement     |
| r-x        | 101          | 5          | Lecture et exécution                 |
| rw-        | 110          | 6          | Lecture et écriture                  |
| rwx        | 111          | 7          | Lecture, écriture, et exécution      |

### Explication des Codes Octaux

- **0 (Aucune permission)**: Aucun droit n'est accordé.
- **1 (Exécution)**: Permet l'exécution d'un fichier (comme un script ou un programme exécutable) ou l'accès à un répertoire.
- **2 (Écriture)**: Permet la modification d'un fichier ou l'ajout/suppression de fichiers dans un répertoire.
- **3 (Écriture + Exécution)**: Combiner les permissions d'écriture et d'exécution sans permettre la lecture peut être utile pour des répertoires temporaires.
- **4 (Lecture)**: Permet de voir le contenu d'un fichier ou de lister les fichiers d'un répertoire.
- **5 (Lecture + Exécution)**: Souvent utilisé pour les répertoires qui doivent être traversés par l'utilisateur.
- **6 (Lecture + Écriture)**: Permet de modifier des fichiers, sans exécution.
- **7 (Lecture + Écriture + Exécution)**: Donne tous les droits, souvent utilisé pour des scripts que l'utilisateur veut lire, modifier et exécuter.

### Utilisation de `chmod` avec des Exemples Pratiques

- **`chmod 777 fichier`**: Ceci donne à l'utilisateur, au groupe et à tous les autres utilisateurs (world) tous les droits sur le fichier. Cela peut poser des risques de sécurité, donc à utiliser avec prudence.
- **`chmod 644 fichier`**: Donne au propriétaire du fichier les droits en lecture et écriture, mais seulement en lecture pour le groupe et les autres. Couramment utilisé pour les fichiers que vous voulez que tout le monde puisse lire mais que seul le propriétaire puisse modifier.
- **`chmod 755 fichier`**: Accorde au propriétaire tous les droits et seulement la lecture et l'exécution aux autres. Fréquemment utilisé pour les scripts ou les programmes que l'utilisateur veut exécuter mais ne pas modifier par d'autres.

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# Partie 3 - Pratiquer la modification de ces permissions de manière sécuritaire et appropriée.
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇


# Informations sur la différence entre les fichiers et les répertoires, ainsi que sur la manière dont ces types d'objets sont indiqués

### Indicateur de Type de Fichier

Dans les permissions Unix/Linux, le premier caractère de la liste des permissions indique le type de l'élément :

- **`d`**: Indique un répertoire (directory). Par exemple, `drwxrwxrwx` montre un répertoire avec des permissions complètes pour le propriétaire, le groupe et les autres.
- **`-`**: Indique un fichier ordinaire. Par exemple, `-rwxrwxrwx` montre un fichier avec des permissions complètes pour tous.
- **`l`**: Indique un lien symbolique (symbolic link).
- D'autres indicateurs moins fréquents incluent `c` pour les fichiers de périphérique à accès séquentiel et `b` pour les fichiers de périphérique à accès bloc.

### Exemples Pratiques

Voici quelques exemples pour illustrer comment les permissions et les types de fichiers sont présentés :

- **Répertoire avec Permissions Complètes**:
  ```
  drwxrwxrwx
  ```
  Cela indique un répertoire (`d`) où le propriétaire, le groupe et les autres utilisateurs ont tous les droits de lecture, écriture et exécution.

- **Fichier avec Permissions Complètes**:
  ```
  -rwxrwxrwx
  ```
  Cela montre un fichier ordinaire (`-`) où le propriétaire, le groupe, et les autres ont tous les droits de lecture, écriture et exécution.

- **Répertoire avec Permissions Restreintes**:
  ```
  drwxr-x---
  ```
  Cela signifie que le propriétaire du répertoire a tous les droits, les membres du groupe ont uniquement les droits de lecture et d'exécution, et les autres n'ont aucun droit.

- **Fichier avec Permissions de Lecture Seule**:
  ```
  -r--r--r--
  ```
  Ce fichier peut être lu par tout le monde mais ne peut être modifié par personne.

### Utilisation de `ls -l` pour Voir les Permissions

La commande `ls -l` est essentielle pour afficher les permissions ainsi que le type de fichier ou répertoire :

```bash
ls -l
```

Cela retournera une liste de fichiers et de répertoires avec leurs permissions, type, propriétaire, groupe, taille, et date de modification.

### Exercices Suggérés

1. Demander aux étudiants de créer un répertoire et de modifier ses permissions pour permettre à tout le monde de l'écrire, mais à personne de le lire.
2. Proposer un scénario où les étudiants doivent sécuriser un fichier contenant des informations sensibles, en permettant seulement au propriétaire de le lire et de le modifier.



🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# Partie 4 - Exercice Guidé : Gestion des Permissions et des Propriétaires sous Unix/Linux
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇


#### Objectif
Apprendre à créer des répertoires, modifier les permissions et changer les propriétaires de fichiers sous Unix/Linux.

#### Prérequis
- Avoir accès à un système Kali Linux.

#### Instructions

1. **Ouvrir le Terminal**
   - Sur votre système Kali Linux, ouvrez le terminal, disponible via le menu des applications ou en le recherchant avec la commande "terminal".

2. **Vérification du Répertoire Actuel**
   - Tapez `pwd` pour afficher le répertoire de travail actuel.
   - Utilisez `ls -la` pour examiner les fichiers et répertoires présents, ainsi que leurs permissions détaillées.

3. **Navigation vers le Bureau**
   - Changez votre répertoire actuel pour le bureau avec la commande `cd ~/Desktop`.

4. **Création d'un Répertoire**
   - Créez un répertoire `TestPermissions` en tapant `mkdir TestPermissions`.
   - Confirmez la création avec `ls -l`.

5. **Modification des Permissions du Répertoire**
   - Attribuez des permissions complètes avec `chmod 777 TestPermissions`, puis vérifiez avec `ls -l`.
   - Reconsidérez la sécurité de ces permissions et changez-les pour `chmod 755 TestPermissions`, plus sécuritaires, et vérifiez à nouveau.

6. **Création d'un Fichier Texte**
   - Dans `TestPermissions`, créez `example.txt` en tapant `touch example.txt`.

7. **Gestion des Permissions du Fichier**
   - Attribuez `chmod 666 example.txt` pour permettre la lecture et l'écriture à tous.
   - Discutez des risques de sécurité puis ajustez à `chmod 644 example.txt`, restreignant l'écriture au propriétaire seulement.

8. **Gestion des Utilisateurs et Changement de Propriétaire**
   - Consultez les utilisateurs existants avec `cat /etc/passwd`. Choisissez un utilisateur existant ou créez-en un nouveau (`sudo adduser nouvelutilisateur`).
   - Changez le propriétaire de `example.txt` à cet utilisateur avec `sudo chown nouvelutilisateur example.txt` et vérifiez le changement avec `ls -l`.

#### Diversification des Scénarios de Permissions
- Proposez des scénarios variés, comme sécuriser un journal (`logfile.txt`) ou configurer un script exécutable (`run.sh`), et demandez la configuration appropriée des permissions.

#### Questions de Réflexion
- Pourquoi limiter les permissions d'écriture sur certains fichiers?
- Quelles pourraient être les conséquences de permissions trop permissives sur un script exécutable?
- Quels sont les risques associés aux permissions `777`?

#### Conclusion
- Récapitulez les pratiques de sécurité et discutez de l'importance de permissions appropriées pour la sécurité des systèmes.

### Explications Complémentaires sur les Permissions
- **Pourquoi `755` est préférable à `777`?** : `755` limite la modification des fichiers ou répertoires aux propriétaires uniquement, empêchant les modifications non autorisées, tandis que `777` permet à tous les utilisateurs de modifier les fichiers, augmentant les risques de sécurité.

#### Autres Permissions Communes
- **`644`** : Idéal pour les documents réguliers, permettant la lecture par tous mais la modification uniquement par le propriétaire.
- **`700`** : Sécurise les fichiers sensibles en n'autorisant que le propriétaire à y accéder.
- **`600`** : Restreint tous les accès aux non-propriétaires, utilisé pour les fichiers sensibles.
- **`711`** : Permet au propriétaire de tout faire, tandis que les autres peuvent uniquement exécuter le fichier.
