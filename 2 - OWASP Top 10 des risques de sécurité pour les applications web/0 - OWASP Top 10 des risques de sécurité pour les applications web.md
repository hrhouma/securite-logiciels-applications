# OWASP Top 10 des risques de sécurité pour les applications web

Le Top 10 OWASP est un document de sensibilisation standard pour les développeurs et la sécurité des applications web. Il représente un large consensus sur les risques de sécurité les plus critiques pour les applications web.

## A1: Contrôle d'accès défaillant

Les failles de contrôle d'accès permettent aux attaquants d'accéder à des fonctionnalités ou des données non autorisées, telles que l'accès aux comptes d'autres utilisateurs, la visualisation de fichiers sensibles et la modification des données d'autres utilisateurs.

### Exemple

Un utilisateur non autorisé accède à une URL qui devrait être accessible uniquement par les administrateurs :
```
http://exemple.com/admin/settings
```

## A2: Défaillances cryptographiques

Cette catégorie comprend les failles liées à la cryptographie qui conduisent souvent à une exposition de données sensibles ou à un compromis du système. Cela peut être dû à de mauvaises pratiques de cryptage ou à des failles dans les algorithmes de cryptage.

## A3: Injection

Les failles d'injection, telles que l'injection SQL, NoSQL et de commande, se produisent lorsque des données non fiables sont envoyées à un interprète dans le cadre d'une commande ou d'une requête. Les données hostiles de l'attaquant peuvent tromper l'interprète pour exécuter des commandes non prévues ou accéder à des données non autorisées.

### Exemple de l'injection SQL

Un attaquant insère une instruction SQL malveillante dans un champ de formulaire qui est ensuite exécutée par la base de données.
```sql
Input:
' OR '1'='1

Code SQL Vulnérable:
SELECT * FROM users WHERE username = '$username' AND password = '$password';
```

## A4: Conception non sécurisée

La conception non sécurisée englobe les vulnérabilités dues à des défauts de conception. Elle concerne les risques liés aux motifs de conception et d'architecture qui conduisent à des mécanismes de sécurité insuffisants.

## A5: Mauvaise configuration de la sécurité

La mauvaise configuration de la sécurité se produit lorsque les paramètres de sécurité sont définis, mis en œuvre ou maintenus de manière incorrecte. Cela peut se produire à tout niveau de la pile d'applications, y compris les services réseau, les plateformes, les serveurs web, les bases de données et les applications.

## A6: Composants vulnérables et obsolètes

Utiliser des composants avec des vulnérabilités connues ou ne pas mettre à jour les composants peut conduire à des violations de données graves et à un accès non autorisé à l'application web.

## A7: Défaillances de l'identification et de l'authentification

Ce risque fait référence aux faiblesses dans les fonctions d'authentification et de gestion des sessions. Les attaquants peuvent compromettre les mots de passe, les clés ou les jetons de session, ou exploiter d'autres failles de mise en œuvre pour assumer l'identité d'autres utilisateurs.

## A8: Défaillances de l'intégrité des logiciels et des données

Le manque de vérification de l'intégrité, comme ne pas vérifier les mises à jour logicielles ou l'intégrité des données avant utilisation, peut conduire au déploiement de logiciels ou de données non autorisés ou malveillants.

## A9: Défaillances de journalisation et de surveillance de la sécurité

Une journalisation et une surveillance insuffisantes et le manque d'intégration avec la réponse aux incidents permettent aux attaquants de poursuivre leurs attaques, de maintenir la persistance, de pivoter vers plus de systèmes, et de falsifier ou d'extraire des données sans être détectés.

## A10: Falsification de requête côté serveur (SSRF)

La SSRF se produit lorsqu'un attaquant abuse de la fonctionnalité sur le serveur pour lire

 ou modifier des ressources internes. Les attaquants peuvent cibler des systèmes internes derrière le pare-feu qui ne sont pas directement accessibles depuis le réseau externe.

---

### Pour plus d'informations

Pour une explication détaillée et des stratégies d'atténuation pour ces risques, visitez la [page web OWASP Top 10](https://owasp.org/www-project-top-ten/).
