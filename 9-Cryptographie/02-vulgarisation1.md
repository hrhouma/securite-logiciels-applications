## Vulgarisation du Processus d'Autorisation des Clés SSH

### Histoire

- Imaginons que vous souhaitez accéder à la maison de Karine, mais elle n'est pas là pour vous ouvrir la porte. 
- Karine a une méthode sécurisée pour permettre à des personnes de confiance d'entrer dans sa maison même lorsqu'elle est absente.

### Concept

1. **La Boîte avec un Cadenas** :
- Karine utilisera votre boîte spéciale avec un cadenas que vous allez lui envoyer.
- Karine ajoutera votre boîte à l'extérieur de sa maison parmi les objets de confiance. Pour pouvoir l'ouvrir, il faut utiliser votre clé priv.

# Une clé privée ne sert qu'à déchiffrer la clé publique !!!!!! Ouvrir le cadenas 
   
2. **La Clé Privée** :
   Vous avez une clé privée qui peut ouvrir cette boîte. Cette clé privée est unique et vous êtes le seul à la posséder.

### Processus

1. **Demande d'Accès** :
   Vous contactez Karine et lui demandez d'accéder à sa maison. Karine vous ajoute alors à sa liste de personnes autorisées en mettant votre clé publique dans le fichier `authorized_keys`. En termes simples, elle place votre boîte avec votre cadenas parmi les objets de confiance.
   
2. **Accès à la Boîte** :
   Vous utilisez votre clé privée pour ouvrir la boîte avec le cadenas (qui représente la clé publique). En ouvrant cette boîte, vous obtenez un code ou une autre méthode d'accès pour entrer dans la maison de Karine.

3. **Entrée dans la Maison** :
   Avec le code ou la méthode d'accès obtenus en ouvrant la boîte, vous pouvez maintenant entrer dans la maison de Karine, même en son absence.

### Explication en Termes de SSH

- **Clé Publique** : La boîte avec le cadenas que Karine place à l'extérieur de sa maison. Elle est ouverte par la clé privée.
- **Clé Privée** : La clé unique que vous possédez et qui peut ouvrir la boîte avec le cadenas.
- **authorized_keys** : Le fichier dans lequel Karine ajoute les clés publiques des personnes autorisées à entrer dans sa maison.

En ajoutant votre clé publique dans le fichier `authorized_keys`, Karine vous donne la possibilité d'ouvrir la boîte avec votre clé privée, et ainsi, d'accéder à sa maison en toute sécurité.
