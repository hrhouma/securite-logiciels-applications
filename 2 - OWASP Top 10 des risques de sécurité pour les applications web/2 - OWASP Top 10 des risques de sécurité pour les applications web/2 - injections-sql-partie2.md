# Comprendre l'Injection SQL

Ce document fournit une explication détaillée de l'injection SQL, avec des exemples de requêtes vulnérables et des recommandations pour sécuriser les applications.

## Qu'est-ce que l'Injection SQL ?

L'injection SQL est une technique d'attaque qui exploite les vulnérabilités de sécurité dans une application utilisant des bases de données en insérant ou "injectant" du code SQL malveillant dans une requête.

## Exemples d'Injection SQL et Explications

### 1. Injection SQL Basique

**Input Malveillant:**
```
' OR '1'='1
```

**Requête SQL Vulnérable:**
```sql
SELECT * FROM users WHERE username = '$username' AND password = '$password';
```

**Explication:**
- L'attaquant utilise `' OR '1'='1` pour rompre la logique de la requête. Le `'` termine la chaîne de caractères précédente, `OR '1'='1` ajoute une condition toujours vraie, et la requête retournera tous les utilisateurs car `1=1` est toujours vrai.

### 2. Bypass de Mot de Passe

**Input Malveillant:**
```
admin' --
```

**Requête Modifiée:**
```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything';
```

**Explication:**
- Le `--` est utilisé pour commenter le reste de la requête, ignoré par le serveur SQL. Cela permet à l'attaquant de se connecter en tant qu'`admin` sans connaître le mot de passe.

## Comment l'Injection Affecte les Conditions SQL ?

**Requête Initiale:**
```sql
SELECT * FROM users WHERE username = 'johndoe' AND password = 'mypassword';
```

**Input Malveillant et Requête Modifiée:**
```sql
Username: admin' --
Password: anything
```

**Requête Modifiée:**
```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything';
```

### Question: Est-ce que `mypassword` va être écrasé ?

**Réponse:**
- Oui, la partie `AND password = 'anything'` est commentée et donc ignorée. L'attaquant n'a pas besoin de connaître ou d'écraser le mot de passe existant.

## Préventions Contre l'Injection SQL

1. **Validation et Échappement des Entrées:**
   - Assurez-vous que toutes les entrées utilisateur sont validées pour éviter les injections de caractères dangereux.

2. **Utilisation de Requêtes Préparées:**
   - Les requêtes préparées (statements) séparent les données des commandes SQL, empêchant les injections.

3. **Utilisation de Frameworks ORM:**
   - Les ORM évitent généralement l'usage direct de chaînes SQL brutes, réduisant le risque d'injections.

## Conclusion

Comprendre et prévenir les injections SQL est essentiel pour la sécurité des applications interagissant avec des bases de données. En suivant les meilleures pratiques, vous pouvez protéger vos applications contre ces attaques courantes et dangereuses.
