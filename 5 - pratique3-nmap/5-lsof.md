### Laboratoire Complet : Utilisation de `lsof` sur Kali Linux

#### Objectif
Fournir une série d'exercices pratiques pour apprendre à utiliser `lsof` pour voir tous les ports ouverts et gérer les processus, y compris les tuer, sur une machine Kali Linux.

### Préparation

1. **Vérifiez que `lsof` est installé sur votre machine Kali Linux :**
   ```bash
   sudo apt update
   sudo apt install lsof
   ```

### Étape 1 : Visualiser les Ports Ouverts

1. **Lister tous les fichiers ouverts par les processus :**
   ```bash
   lsof
   ```

2. **Lister tous les ports ouverts :**
   ```bash
   sudo lsof -i
   ```

3. **Lister les ports TCP ouverts :**
   ```bash
   sudo lsof -i TCP
   ```

4. **Lister les ports UDP ouverts :**
   ```bash
   sudo lsof -i UDP
   ```

5. **Lister les ports ouverts sur une plage spécifique (par exemple, 80) :**
   ```bash
   sudo lsof -i :80
   ```

### Étape 2 : Filtrer par Processus

1. **Lister les fichiers ouverts par un utilisateur spécifique (par exemple, root) :**
   ```bash
   sudo lsof -u root
   ```

2. **Lister les fichiers ouverts par un processus spécifique (par exemple, PID 1234) :**
   ```bash
   sudo lsof -p 1234
   ```

3. **Lister les fichiers ouverts par un programme spécifique (par exemple, nginx) :**
   ```bash
   sudo lsof -c nginx
   ```

### Étape 3 : Identifier et Tuer des Processus

1. **Identifier les processus utilisant un port spécifique (par exemple, 80) :**
   ```bash
   sudo lsof -i :80
   ```

2. **Tuer un processus spécifique par son PID (par exemple, PID 1234) :**
   ```bash
   sudo kill -9 1234
   ```

### Étape 4 : Exercices Pratiques

1. **Lister tous les ports ouverts sur la machine :**
   ```bash
   sudo lsof -i
   ```

2. **Lister les ports TCP ouverts :**
   ```bash
   sudo lsof -i TCP
   ```

3. **Lister les ports ouverts sur le port 80 :**
   ```bash
   sudo lsof -i :80
   ```

4. **Lister les fichiers ouverts par le processus avec PID 1234 :**
   ```bash
   sudo lsof -p 1234
   ```

5. **Identifier les processus utilisant le port 80 :**
   ```bash
   sudo lsof -i :80
   ```

6. **Tuer le processus utilisant le port 80 (remplacez `PID` par l'identifiant de processus correct) :**
   ```bash
   sudo kill -9 PID
   ```

### Résumé des Commandes

- **Lister tous les fichiers ouverts :** `lsof`
- **Lister tous les ports ouverts :** `sudo lsof -i`
- **Lister les ports TCP ouverts :** `sudo lsof -i TCP`
- **Lister les ports UDP ouverts :** `sudo lsof -i UDP`
- **Lister les ports ouverts sur le port 80 :** `sudo lsof -i :80`
- **Lister les fichiers ouverts par un utilisateur spécifique :** `sudo lsof -u root`
- **Lister les fichiers ouverts par un processus spécifique :** `sudo lsof -p 1234`
- **Lister les fichiers ouverts par un programme spécifique :** `sudo lsof -c nginx`
- **Identifier les processus utilisant le port 80 :** `sudo lsof -i :80`
- **Tuer un processus par son PID :** `sudo kill -9 1234`

### Exemple d'Exercice Pratique : Utilisation de `lsof`

1. **Lister tous les ports ouverts sur la machine :**
   ```bash
   sudo lsof -i
   ```

2. **Lister les ports TCP ouverts :**
   ```bash
   sudo lsof -i TCP
   ```

3. **Lister les ports ouverts sur le port 80 :**
   ```bash
   sudo lsof -i :80
   ```

4. **Lister les fichiers ouverts par le processus avec PID 1234 :**
   ```bash
   sudo lsof -p 1234
   ```

5. **Identifier les processus utilisant le port 80 :**
   ```bash
   sudo lsof -i :80
   ```

6. **Tuer le processus utilisant le port 80 (remplacez `PID` par l'identifiant de processus correct) :**
   ```bash
   sudo kill -9 PID
   ```

Ces exercices permettront aux étudiants de se familiariser avec les différentes fonctionnalités de `lsof` et de comprendre comment elles peuvent être utilisées pour analyser et gérer les processus sur une machine Kali Linux. Ils n'auront qu'à copier-coller les commandes pour les exécuter sur leur machine Kali Linux.
