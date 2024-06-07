# Tutoriel Complet : Installation de Figlet et Personnalisation d'un Message dans .bashrc

## 1 - Introduction
Figlet est un programme en ligne de commande qui génère des bannières textuelles à partir de texte standard. Ce guide explique comment installer Figlet, créer un message personnalisé et l'ajouter à votre fichier `.bashrc`.

### Prérequis
- Un système Unix (Linux, macOS) ou Windows avec un terminal compatible.
- Connexion Internet.

## 2 - Installation de Figlet

### Sous Linux (Debian/Ubuntu)
1. Ouvrez un terminal.
2. Mettez à jour la liste des paquets :
   ```bash
   sudo apt update
   ```
3. Installez Figlet :
   ```bash
   sudo apt install figlet
   ```

### Sous macOS
1. Ouvrez un terminal.
2. Installez Homebrew si ce n'est pas déjà fait, suivez les instructions sur [brew.sh](https://brew.sh/).
3. Installez Figlet :
   ```bash
   brew install figlet
   ```

### Sous Windows
1. Téléchargez et installez Cygwin depuis [cygwin.com](https://www.cygwin.com/).
2. Sélectionnez `figlet` pendant l'installation de Cygwin.
3. Ouvrez le terminal Cygwin.

## 3 - Ajout du Message Personnalisé à `.bashrc`

1. Ouvrez le fichier `.bashrc` :
   ```bash
   nano ~/.bashrc
   ```

2. Ajoutez la commande Figlet à la fin du fichier :
   ```bash
   echo 'figlet "Se former avec Haythem"' >> ~/.bashrc
   ```

3. Enregistrez et fermez l'éditeur.
4. Pour appliquer les modifications immédiatement :
   ```bash
   source ~/.bashrc
   ```

### Exemple Complet
Voici un exemple de fichier `.bashrc` après modification :
```bash
# ~/.bashrc

# ... autres configurations ...

# Ajouter un message personnalisé avec Figlet
figlet "Se former avec Haythem"
```

## 4 - Résultat
Chaque fois que vous ouvrez un nouveau terminal, le message personnalisé sera affiché :

```
 ____  _____                          _       _             _           
/ ___|| ____|__  ___ __  _ __   __ _ (_) __ _| |_ ___   ___| |_ ___ _ __ 
\___ \|  _| / _ \/ __/ _ \| '_ \ / _` || |/ _` | __/ _ \ / __| __/ _ \ '__|
 ___) | |__|  __/ (_| (_) | | | | (_| || | (_| | ||  __/| (__| ||  __/ |   
|____/|_____\___|\___\___/|_| |_|\__, |_|\__,_|\__\___| \___|\__\___|_|   
                                |___/                                  
```

## 5 - Conclusion
Vous avez maintenant installé Figlet, créé un message personnalisé et l'avez ajouté à votre fichier `.bashrc`. Profitez de la formation avec Haythem !
