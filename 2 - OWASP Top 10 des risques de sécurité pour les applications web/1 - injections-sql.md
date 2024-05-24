# Situation

Vous avez un formulaire de connexion sur votre site web où les utilisateurs entrent leur nom d'utilisateur et leur mot de passe. Ces informations sont utilisées pour construire une requête SQL qui vérifie si le nom d'utilisateur et le mot de passe correspondent à une entrée dans la base de données de votre application.

### Code vulnérable

```sql
SELECT * FROM users WHERE username = '$username' AND password = '$password';
```

Dans ce code, `$username` et `$password` sont des variables qui sont remplacées par les entrées de l'utilisateur. Si l'utilisateur entre un nom d'utilisateur et un mot de passe normaux, la requête pourrait ressembler à quelque chose comme :

```sql
SELECT * FROM users WHERE username = 'johndoe' AND password = 'mypassword';
```

### Exploitation

Un attaquant utilise l'injection SQL pour modifier la logique de la requête SQL en insérant des caractères spéciaux et du SQL supplémentaire. En utilisant l'input `' OR '1'='1`, l'attaquant peut manipuler la requête pour qu'elle devienne :

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '';
```

#### Analyse de l'injection

1. **`'`** - Le premier apostrophe termine la chaîne de caractères pour la variable `$username`.
2. **`OR '1'='1'`** - Cette condition est toujours vraie. L'opérateur OR permet à cette condition d'être évaluée indépendamment de la vérification du nom d'utilisateur et du mot de passe. Comme '1' est toujours égal à '1', cette condition renvoie `true`.
3. **`AND password = ''`** - Cette partie de la requête devient insignifiante car la partie OR a déjà validé la requête à `true`.

### Résultat de l'attaque

Cette requête modifiée n'exige pas de connaître un nom d'utilisateur ou un mot de passe valide pour être exécutée avec succès. Elle retournera les enregistrements de tous les utilisateurs dans la base de données, car la condition `OR '1'='1'` est toujours vraie. Cela signifie que l'attaquant peut se connecter en tant que n'importe quel utilisateur, y compris les utilisateurs administrateurs, sans avoir besoin de connaître les mots de passe.

### Prévention

Pour prévenir les injections SQL comme celle-ci, il est essentiel de :

- **Utiliser les requêtes préparées (prepared statements)** : Ce type de requêtes sépare clairement le code SQL de données, ce qui empêche les entrées malveillantes de modifier la logique de la requête.
- **Sanitiser et valider toutes les entrées utilisateurs** : Assurez-vous que les entrées correspondent aux attentes en termes de type, de format et de longueur.
- **Utiliser des ORM (Object Relational Mapping) et des frameworks qui échappent automatiquement les entrées SQL** : Ces outils réduisent le risque d'injection en gérant les données d'entrée correctement.

Ces mesures aideront à sécuriser vos applications contre les injections SQL, protégeant ainsi vos données et celles de vos utilisateurs.
