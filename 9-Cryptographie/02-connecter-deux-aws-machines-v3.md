# README

## Analogie : Processus de chiffrement asymétrique

Bob et Alice n'échangent pas de clés avant de s'envoyer des messages secrets. Ils utilisent plutôt chacun un cadenas distinct avec des clés correspondantes séparées.

Pour envoyer un message secret à Bob, Alice doit d'abord le contacter et lui demander de lui envoyer son cadenas ouvert (Clé publique pour chiffrer). Bob envoie alors son cadenas, mais conserve sa clé. Lorsqu'Alice reçoit le cadenas, elle écrit son message secret et le place dans une petite boîte. Elle y place également son propre cadenas ouvert, mais conserve sa clé. Ensuite, elle verrouille la boîte avec le cadenas de Bob.

Une fois le cadenas fermé, Alice ne peut plus ouvrir la boîte, car elle ne possède pas la clé appropriée. Elle envoie la boîte à Bob par courrier. Personne ne peut ouvrir la boîte alors qu'elle est en transit.

Lorsque Bob reçoit la boîte, il peut utiliser sa clé pour ouvrir le cadenas et récupérer le message d'Alice. Pour envoyer une réponse sécurisée, Bob place son message secret dans la boîte, accompagné de son cadenas ouvert, et verrouille la boîte avec le cadenas d'Alice. À son tour, Bob envoie la boîte fermée à Alice.

## Les algorithmes asymétriques

Illustration du processus de chiffrement et de déchiffrement :

![Algorithmes Asymétriques](image.png)

---

### Explication de l'illustration :

1. **Clé de chiffrement** : Utilisée pour chiffrer le message. Cette clé est publique et peut être partagée.
2. **Chiffrer** : Le processus de conversion du message original en un message chiffré en utilisant la clé de chiffrement.
3. **Message chiffré** : Le message converti (par exemple, `%37f&4`) qui ne peut être compris sans la clé de déchiffrement.
4. **Clé de déchiffrement** : Utilisée pour déchiffrer le message. Cette clé est privée et doit être gardée secrète.
5. **Déchiffrer** : Le processus de conversion du message chiffré en son format original en utilisant la clé de déchiffrement.

Dans cette illustration, deux clés distinctes (une pour le chiffrement et une pour le déchiffrement) ne sont pas partagées, garantissant ainsi la sécurité du message échangé.

## Connexion SSH entre deux serveurs EC2

### Méthode 2 : Créer de nouvelles clés

1. **Générer des clés sur chaque serveur** :
   Sur chaque serveur, exécutez la commande suivante pour générer une nouvelle paire de clés SSH :
   ```bash
   ssh-keygen
   ```
   Appuyez sur Entrée trois fois pour accepter les options par défaut. Vous aurez deux fichiers :
   - `~/.ssh/id_rsa`
   - `~/.ssh/id_rsa.pub`

2. **Copier la clé publique du serveur A** :
   Sur le serveur A, affichez et copiez la clé publique dans le presse-papier :
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
   Sélectionnez et copiez le contenu affiché.

3. **Ajouter la clé publique au serveur B** :
   Connectez-vous au serveur B et ajoutez le contenu copié au fichier `authorized_keys` :
   ```bash
   cat >> ~/.ssh/authorized_keys
   ```
   Collez le contenu de votre presse-papier et appuyez sur `Ctrl+D` pour quitter.

4. **Connexion SSH à partir du serveur A** :
   Maintenant, vous pouvez vous connecter depuis le serveur A au serveur B en utilisant la clé privée :
   ```bash
   ssh -i ~/.ssh/id_rsa private.ip.du.serveur.cible
   ```

### Analogie

Autoriser la clé publique dans le serveur B est similaire à Alice ou Bob laissant la boîte avec le cadenas fermé parmi les choses autorisées pour accéder à sa maison. C'est comme dire : "Je laisse la clé dans ma maison dans cette boîte qui ne peut être ouverte qu'avec une clé secrète que l'autre dispose."

Ainsi, lorsque vous exécutez `ssh -i ~/.ssh/id_rsa private.ip.du.serveur.cible`, c'est comme utiliser cette clé secrète pour ouvrir la boîte et accéder aux ressources de la maison (serveur).
