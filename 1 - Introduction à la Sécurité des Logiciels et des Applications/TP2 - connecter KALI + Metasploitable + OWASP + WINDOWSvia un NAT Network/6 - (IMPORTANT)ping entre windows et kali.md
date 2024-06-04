# Référence 1
## Méthode 1  : (pas de connectivité internet 😵‍💫) : 
- https://medium.com/@jbtechmaven/creating-an-isolated-network-between-kali-linux-and-windows-10-vms-35efa7134f0b
## Méthode 2  : ( +  connectivité internet 😍) : 
- https://www.youtube.com/watch?v=2Fkf6Kysh7I&ab_channel=Abstractprogrammer

# Étude de cas : 
- Considérons deux machines une windows et l'autre Kali. Nous désirons que les deux machines se pinguent entre elle !
  
# Les différents types de réseaux virtuels, leurs possibilités de ping, leurs avantages, inconvénients, descriptions et leur possibilité de connexion à Internet :

| Type de Réseau | Possibilité de se pinguer (Oui/Non) | Avantages                          | Inconvénients                         | Description                                                                 | Possibilité de se connecter à Internet (Oui/Non) |
|----------------|------------------------------------|-----------------------------------|--------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------|
| NAT            | Non                                | - Simple à configurer            | - Pas de communication directe entre VM | Les machines virtuelles accèdent à Internet via l'hôte.                     | Oui                                               |
| Bridge         | Oui                                | - Communication directe          | - Peut nécessiter une configuration réseau | Les machines virtuelles sont connectées au réseau physique de l'hôte.        | Oui                                               |
| Host-only      | Oui                                | - Réseau isolé sécurisé          | - Pas d'accès Internet                | Les machines virtuelles communiquent uniquement entre elles et avec l'hôte. | Non                                               |
| NAT Network    | Oui                                | - Isolé du réseau physique       | - Configuration un peu plus complexe   | Un réseau privé avec des adresses IP virtuelles pour les VM.                | Oui                                               |
| Internal Network | Oui                             | - Isolé du réseau physique       | - Pas d'accès Internet                | Les machines virtuelles communiquent uniquement entre elles.                | Non                                               |

### Description des Types de Réseau

- **NAT (Network Address Translation)** :
  - **Description** : Les machines virtuelles utilisent l'adresse IP de l'hôte pour accéder à Internet. Elles ne peuvent pas communiquer directement entre elles.
  - **Possibilité de se pinguer** : Non
  - **Avantages** : Facile à configurer, les VM ont accès à Internet.
  - **Inconvénients** : Pas de communication directe entre les machines virtuelles.

- **Bridge** :
  - **Description** : Les machines virtuelles sont connectées au même réseau que l'hôte, avec des adresses IP du même sous-réseau.
  - **Possibilité de se pinguer** : Oui
  - **Avantages** : Les machines peuvent se pinguer et accéder à Internet.
  - **Inconvénients** : Peut nécessiter une configuration réseau et des adresses IP statiques.

- **Host-only** :
  - **Description** : Les machines virtuelles sont sur un réseau isolé, ne communiquant qu'entre elles et avec l'hôte.
  - **Possibilité de se pinguer** : Oui
  - **Avantages** : Sécurité accrue avec un réseau isolé.
  - **Inconvénients** : Pas d'accès à Internet.

- **NAT Network** :
  - **Description** : Un réseau privé virtuel où les machines virtuelles peuvent communiquer entre elles et avec Internet via l'hôte.
  - **Possibilité de se pinguer** : Oui
  - **Avantages** : Permet la communication entre les VM et l'accès à Internet.
  - **Inconvénients** : Configuration un peu plus complexe que le NAT simple.

- **Internal Network** :
  - **Description** : Un réseau interne où les machines virtuelles peuvent uniquement communiquer entre elles.
  - **Possibilité de se pinguer** : Oui
  - **Avantages** : Isolé et sécurisé.
  - **Inconvénients** : Pas d'accès à Internet.
