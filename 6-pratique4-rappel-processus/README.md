### Tutoriel : Utilisation des commandes bg, fg, lsof, ps, kill et pkill

# Partie 1
- Ce tutoriel vise à vous apprendre à utiliser diverses commandes Linux pour gérer les processus. 
- Vous apprendrez à lancer des processus en arrière-plan, à les ramener au premier plan, à lister les processus ouverts, et à terminer les processus à l'aide de différentes commandes de kill.

#### Prérequis
- Accès à un terminal Linux.
- Connaissances de base en ligne de commande.

#### 1. Lancer un processus

Pour lancer un processus, utilisez simplement la commande appropriée. Par exemple, pour lancer un éditeur de texte :

```bash
gedit &
```

Le `&` à la fin de la commande place le processus en arrière-plan.

#### 2. Utilisation de `bg` et `fg`

- **bg** : Mettre un processus en arrière-plan.

  Si vous avez suspendu un processus en utilisant `Ctrl+Z`, vous pouvez le reprendre en arrière-plan avec :

  ```bash
  bg %1
  ```

- **fg** : Ramener un processus au premier plan.

  Pour ramener un processus en arrière-plan au premier plan :

  ```bash
  fg %1
  ```

Le numéro `%1` est le job ID du processus que vous pouvez obtenir en listant les jobs avec la commande `jobs`.

#### 3. Utilisation de `lsof`

- **lsof** (List Open Files) : Afficher tous les fichiers ouverts par les processus.

  ```bash
  lsof
  ```

  Pour filtrer les fichiers ouverts par un utilisateur spécifique :

  ```bash
  lsof -u username
  ```

#### 4. Utilisation de `ps`

- **ps -ef** : Afficher une liste détaillée de tous les processus en cours.

  ```bash
  ps -ef
  ```

- **ps -ef | grep -i** : Filtrer les processus en cours par un critère spécifique.

  ```bash
  ps -ef | grep -i process_name
  ```

#### 5. Utilisation de `kill` et `pkill`

- **kill -9** : Terminer un processus immédiatement.

  ```bash
  kill -9 pid
  ```

- **kill -15** : Terminer un processus proprement (par défaut).

  ```bash
  kill -15 pid
  ```

  ou simplement :

  ```bash
  kill pid
  ```

- **pkill** : Terminer des processus par nom.

  ```bash
  pkill process_name
  ```

#### 6. Exercice Pratique

1. **Lancer un processus en arrière-plan** :

   ```bash
   sleep 300 &
   ```

   Utilisez `jobs` pour voir le processus en arrière-plan.

2. **Ramener le processus au premier plan** :

   ```bash
   fg %1
   ```

   (Remplacez `%1` par le job ID approprié).

3. **Suspendre le processus** :

   Utilisez `Ctrl+Z` pour suspendre le processus ramené au premier plan.

4. **Lister les fichiers ouverts par le processus `sleep`** :

   ```bash
   lsof -c sleep
   ```

5. **Lister les processus `sleep`** :

   ```bash
   ps -ef | grep -i sleep
   ```

6. **Terminer le processus avec `kill`** :

   ```bash
   kill -9 <PID>
   ```

   (Remplacez `<PID>` par le Process ID du processus `sleep`).

7. **Terminer tous les processus `sleep` avec `pkill`** :

   ```bash
   pkill sleep
   ```

# Partie 2

### Tutoriel Avancé : Gestion de Services avec Apache et Systèmes de Processus

#### Objectif
Ce tutoriel avancé vous apprendra à installer et gérer le serveur web Apache, vérifier son état avec `systemctl`, et gérer ses processus avec les commandes `kill` et `pkill`.

#### Prérequis
- Accès à un terminal Linux avec des privilèges sudo.
- Connaissances de base en ligne de commande et gestion de processus.

#### 1. Installer Apache

Pour installer le serveur web Apache sur votre système, utilisez la commande suivante :

```bash
sudo apt update
sudo apt install apache2 -y
```

#### 2. Vérifier l'état du service Apache

Après l'installation, vous pouvez vérifier si le service Apache est en cours d'exécution :

```bash
sudo systemctl status apache2
```

Vous devriez voir une sortie indiquant que le service est actif (running).

#### 3. Lister les processus Apache

Pour lister tous les processus associés à Apache, vous pouvez utiliser la commande `ps` :

```bash
ps -ef | grep apache2
```

Cela affichera une liste de tous les processus Apache en cours d'exécution.

#### 4. Terminer un processus Apache

Pour terminer un processus spécifique d'Apache, utilisez la commande `kill`. Par exemple, pour terminer un processus avec l'ID `PID`, utilisez :

```bash
sudo kill -9 PID
```

(Remplacez `PID` par l'identifiant du processus Apache que vous souhaitez terminer).

#### 5. Terminer tous les processus Apache

Pour terminer tous les processus Apache en une seule commande, vous pouvez utiliser `pkill` :

```bash
sudo pkill apache2
```

#### 6. Redémarrer le service Apache

Après avoir terminé les processus, vous pouvez redémarrer le service Apache pour qu'il fonctionne correctement :

```bash
sudo systemctl restart apache2
```

#### 7. Exercice Pratique

1. **Installer Apache** :
   ```bash
   sudo apt update
   sudo apt install apache2 -y
   ```

2. **Vérifier l'état d'Apache** :
   ```bash
   sudo systemctl status apache2
   ```

3. **Lister les processus Apache** :
   ```bash
   ps -ef | grep apache2
   ```

4. **Terminer un processus Apache** :
   ```bash
   sudo kill -9 <PID>
   ```

5. **Terminer tous les processus Apache** :
   ```bash
   sudo pkill apache2
   ```

6. **Redémarrer Apache** :
   ```bash
   sudo systemctl restart apache2
   ```

7. **Vérifier l'état après redémarrage** :
   ```bash
   sudo systemctl status apache2
   ```


- Cette partie vous a montré comment installer et gérer le serveur web Apache, vérifier son état avec `systemctl`, et gérer ses processus avec les commandes `kill` et `pkill`. Vous avez également appris à redémarrer le service Apache après avoir terminé ses processus. Ces compétences sont essentielles pour la gestion et la maintenance des services sur un système Linux.

# Partie 3 - exercices : Gestion de Services avec Apache et Systèmes de Processus


### Exercice 1 : Installation et Vérification d'Apache

**Étapes :**

1. **Mettre à jour les paquets** :
   ```bash
   sudo apt update
   ```

2. **Installer Apache** :
   ```bash
   sudo apt install apache2 -y
   ```

3. **Vérifier l'état du service Apache** :
   ```bash
   sudo systemctl status apache2
   ```

**Questions :**

1. Quelle commande permet de mettre à jour la liste des paquets disponibles sur le système ?
2. Quelle commande avez-vous utilisée pour installer Apache ?
3. Quelle est la sortie de la commande `systemctl status apache2` lorsque le service Apache fonctionne correctement ?

### Exercice 2 : Gestion des Processus Apache

**Étapes :**

1. **Lister les processus Apache** :
   ```bash
   ps -ef | grep apache2
   ```

2. **Terminer un processus Apache spécifique** :
   ```bash
   sudo kill -9 <PID>
   ```

   (Remplacez `<PID>` par l'ID du processus Apache que vous souhaitez terminer).

3. **Terminer tous les processus Apache** :
   ```bash
   sudo pkill apache2
   ```

4. **Redémarrer Apache** :
   ```bash
   sudo systemctl restart apache2
   ```

5. **Vérifier l'état du service Apache après redémarrage** :
   ```bash
   sudo systemctl status apache2
   ```

**Questions :**

1. Quelle commande avez-vous utilisée pour lister tous les processus Apache en cours d'exécution ?
2. Comment avez-vous terminé un processus Apache spécifique ? Indiquez la commande exacte.
3. Quelle commande permet de terminer tous les processus Apache en une seule fois ?
4. Pourquoi est-il nécessaire de redémarrer le service Apache après avoir terminé ses processus ?

### Exercice 3 : Utilisation Avancée de `lsof` et `ps`

**Étapes :**

1. **Lister tous les fichiers ouverts par les processus Apache** :
   ```bash
   sudo lsof -c apache2
   ```

2. **Lister les processus qui utilisent un port spécifique (par exemple, le port 80)** :
   ```bash
   sudo lsof -i :80
   ```

3. **Utiliser `ps` pour filtrer les processus par nom** :
   ```bash
   ps -ef | grep apache2
   ```

**Questions :**

1. Quelle commande avez-vous utilisée pour lister tous les fichiers ouverts par Apache ?
2. Comment pouvez-vous trouver quels processus utilisent le port 80 ?
3. Quelle est l'utilité de la commande `ps -ef | grep apache2` ?

### Exercice 4 : Simuler et Gérer un Conflit de Port

**Étapes :**

1. **Lancer un processus qui utilise le port 80** (par exemple, un serveur Python simple) :
   ```bash
   python3 -m http.server 80 &
   ```

2. **Tenter de redémarrer Apache et observer l'erreur** :
   ```bash
   sudo systemctl restart apache2
   ```

3. **Lister le processus qui utilise le port 80 et le terminer** :
   ```bash
   sudo lsof -i :80
   sudo kill -9 <PID>
   ```

   (Remplacez `<PID>` par l'ID du processus Python).

4. **Redémarrer Apache** :
   ```bash
   sudo systemctl restart apache2
   ```

5. **Vérifier l'état du service Apache après redémarrage** :
   ```bash
   sudo systemctl status apache2
   ```

**Questions :**

1. Quelle commande avez-vous utilisée pour lancer un serveur HTTP sur le port 80 ?
2. Quelle erreur avez-vous observée lors du redémarrage d'Apache avec le port 80 déjà utilisé ?
3. Comment avez-vous identifié et terminé le processus qui utilisait le port 80 ?
4. Quelle commande avez-vous utilisée pour redémarrer Apache après avoir résolu le conflit de port ?
