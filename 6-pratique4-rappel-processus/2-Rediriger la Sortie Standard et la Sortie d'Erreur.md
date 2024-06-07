### Tutoriel Rapide : Rediriger la Sortie Standard et la Sortie d'Erreur

#### Objectif
Ce tutoriel vous apprendra à rediriger la sortie standard (stdout) et la sortie d'erreur (stderr) dans le terminal Linux. Vous apprendrez également à combiner les deux sorties dans un même fichier.

#### 1. Rediriger la Sortie Standard (stdout)

Pour rediriger la sortie standard d'une commande vers un fichier, utilisez le symbole `>` :

```bash
commande > fichier.txt
```

Par exemple :

```bash
ls > liste_des_fichiers.txt
```

Cette commande écrira la liste des fichiers et répertoires dans le fichier `liste_des_fichiers.txt`.

#### 2. Rediriger la Sortie d'Erreur (stderr)

Pour rediriger la sortie d'erreur d'une commande vers un fichier, utilisez le symbole `2>` :

```bash
commande 2> erreurs.txt
```

Par exemple :

```bash
ls /dossier_inexistant 2> erreurs.txt
```

Cette commande écrira le message d'erreur généré par `ls` dans le fichier `erreurs.txt`.

#### 3. Rediriger les Deux Sorties (stdout et stderr) vers des Fichiers Différents

Pour rediriger la sortie standard et la sortie d'erreur vers deux fichiers différents, combinez les deux symboles :

```bash
commande > fichier_stdout.txt 2> fichier_stderr.txt
```

Par exemple :

```bash
ls /dossier_existant /dossier_inexistant > sortie.txt 2> erreurs.txt
```

Cette commande écrira la sortie standard dans `sortie.txt` et la sortie d'erreur dans `erreurs.txt`.

#### 4. Rediriger les Deux Sorties (stdout et stderr) vers le Même Fichier

Pour rediriger la sortie standard et la sortie d'erreur vers le même fichier, utilisez le symbole `&>` :

```bash
commande &> fichier.txt
```

Par exemple :

```bash
ls /dossier_existant /dossier_inexistant &> sortie_complete.txt
```

Cette commande écrira la sortie standard et la sortie d'erreur dans `sortie_complete.txt`.

### Exercices

1. **Rediriger la sortie standard** :
   - Utilisez la commande `ls` pour lister les fichiers dans un répertoire de votre choix et redirigez la sortie standard vers un fichier nommé `liste.txt`.

   ```bash
   ls > liste.txt
   ```

2. **Rediriger la sortie d'erreur** :
   - Utilisez la commande `ls` pour lister les fichiers dans un répertoire inexistant et redirigez la sortie d'erreur vers un fichier nommé `erreurs.txt`.

   ```bash
   ls /dossier_inexistant 2> erreurs.txt
   ```

3. **Rediriger les deux sorties vers des fichiers différents** :
   - Utilisez la commande `ls` pour lister les fichiers dans un répertoire existant et un répertoire inexistant, redirigez la sortie standard vers un fichier nommé `sortie.txt` et la sortie d'erreur vers un fichier nommé `erreurs.txt`.

   ```bash
   ls /dossier_existant /dossier_inexistant > sortie.txt 2> erreurs.txt
   ```

4. **Rediriger les deux sorties vers le même fichier** :
   - Utilisez la commande `ls` pour lister les fichiers dans un répertoire existant et un répertoire inexistant, et redirigez les deux sorties vers un fichier nommé `sortie_complete.txt`.

   ```bash
   ls /dossier_existant /dossier_inexistant &> sortie_complete.txt
   ```

### Conclusion

En suivant ce tutoriel, vous avez appris à rediriger la sortie standard et la sortie d'erreur dans le terminal Linux. Ces compétences sont essentielles pour la gestion des logs et la capture des messages d'erreur lors de l'exécution de commandes et de scripts.
