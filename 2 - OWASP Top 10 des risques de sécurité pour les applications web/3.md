# Pouvouns nous insérer un utilisateur ?
Supposons que vous ayez un formulaire vulnérable où les données insérées ne sont pas correctement nettoyées. Si le formulaire exécute la requête SQL suivante pour insérer des données :

```sql
INSERT INTO admin (nomutilisateur, motdepasse) VALUES ('input_username', 'input_password');
```

Une injection SQL pour créer un nouvel utilisateur pourrait être :

```sql
'); INSERT INTO admin (nomutilisateur, motdepasse) VALUES ('nouvelUtilisateur', 'nouveauMotDePasse'); --
```

En insérant cette chaîne dans un champ de saisie, cela ferait ce qui suit :
1. Termine la première requête SQL après les valeurs initialement prévues (`input_username` et `input_password`).
2. Commence une nouvelle instruction `INSERT` pour ajouter un utilisateur `nouvelUtilisateur` avec le mot de passe `nouveauMotDePasse`.
3. Utilise `--` pour commenter le reste de la requête originale pour éviter des erreurs d'exécution.

Cette technique montre comment un attaquant pourrait exploiter une vulnérabilité pour modifier les données ou la structure de la base de données de manière non autorisée. Utilisez ces informations uniquement à des fins d'apprentissage dans un environnement contrôlé.
