# Évaluation formative de la Sécurité des Sites Web des Collèges et Universités

Pour les sites webs des 50 institutions listées, nous allons vérifier les éléments suivants pour quelques sites (choisissez 3):

1. **Protection de /wp-admin :** Vérifier si la page de connexion à l'administration WordPress est protégée.
2. **Utilisateurs WordPress :** Utiliser la commande curl pour lister les utilisateurs disponibles via l'API REST.

#### Tableau de Vérification

| Site Web                                      | /wp-admin Protégé | Utilisateurs WordPress (via curl)          |
|-----------------------------------------------|-------------------|--------------------------------------------|
| https://www.crosemont.qc.ca/                  | Oui/Non           | Utilisateur(s)                             |
| https://www.bdeb.qc.ca/                       | Oui/Non           | Utilisateur(s)                             |
| https://www.collegecanada.com/                | Oui/Non           | Utilisateur(s)                             |
| https://institutelite.ca/                     | Oui/Non           | Utilisateur(s)                             |
| https://www.lasallecollege.com/               | Oui/Non           | Utilisateur(s)                             |
| https://www.johnabbott.qc.ca/                 | Oui/Non           | Utilisateur(s)                             |
| https://www.dawsoncollege.qc.ca/              | Oui/Non           | Utilisateur(s)                             |
| https://www.vaniercollege.qc.ca/              | Oui/Non           | Utilisateur(s)                             |
| https://www.claurendeau.qc.ca/                | Oui/Non           | Utilisateur(s)                             |
| https://www.cmaisonneuve.qc.ca/               | Oui/Non           | Utilisateur(s)                             |
| https://www.collegeahuntsic.qc.ca/            | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepsl.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.cvm.qc.ca/                        | Oui/Non           | Utilisateur(s)                             |
| https://www.marianopolis.edu/                 | Oui/Non           | Utilisateur(s)                             |
| https://www.cimf.qc.ca/                       | Oui/Non           | Utilisateur(s)                             |
| https://www.etsmtl.ca/                        | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepgarneau.ca/                  | Oui/Non           | Utilisateur(s)                             |
| https://www.cegeplimoilou.ca/                 | Oui/Non           | Utilisateur(s)                             |
| https://uqam.ca/                              | Oui/Non           | Utilisateur(s)                             |
| https://umontreal.ca/                         | Oui/Non           | Utilisateur(s)                             |
| https://enit.rnu.tn/                          | Oui/Non           | Utilisateur(s)                             |
| https://www.cegeptr.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepshawinigan.ca/               | Oui/Non           | Utilisateur(s)                             |
| https://www.clafleche.qc.ca/                  | Oui/Non           | Utilisateur(s)                             |
| https://www.ellis.qc.ca/                      | Oui/Non           | Utilisateur(s)                             |
| https://www.conservatoire.gouv.qc.ca/         | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepst.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepsth.qc.ca/                   | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepvalleyfield.ca/              | Oui/Non           | Utilisateur(s)                             |
| https://www.cegepmontpetit.ca/                | Oui/Non           | Utilisateur(s)                             |
| https://www.cstjean.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.champlainonline.com/              | Oui/Non           | Utilisateur(s)                             |
| https://www.academie-ent.com/                 | Oui/Non           | Utilisateur(s)                             |
| https://www.airrichelieu.com/                 | Oui/Non           | Utilisateur(s)                             |
| https://www.april-fortier.com/                | Oui/Non           | Utilisateur(s)                             |
| https://www.cdicollege.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.collegeimmobilier.com/            | Oui/Non           | Utilisateur(s)                             |
| https://cargair.com/                          | Oui/Non           | Utilisateur(s)                             |
| https://www.centreequestredechambly.com/      | Oui/Non           | Utilisateur(s)                             |
| https://sainthubertflyingcollege.com/         | Oui/Non           | Utilisateur(s)                             |
| https://collegemilestone.ca/                  | Oui/Non           | Utilisateur(s)                             |
| https://helicraft.ca/                         | Oui/Non           | Utilisateur(s)                             |
| https://www.teccart.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.itaq.ca/                          | Oui/Non           | Utilisateur(s)                             |
| https://www.collegemv.qc.ca/                  | Oui/Non           | Utilisateur(s)                             |
| https://www.cgodin.qc.ca/                     | Oui/Non           | Utilisateur(s)                             |
| https://www.grasset.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.brebeuf.qc.ca/                    | Oui/Non           | Utilisateur(s)                             |
| https://www.collegedecarie.ca/                | Oui/Non           | Utilisateur(s)                             |
| https://www.osullivan.edu/                    | Oui/Non           | Utilisateur(s)                             |
| https://collegeuniversel.ca/programme/        | Oui/Non           | Utilisateur(s)                             |

# Étapes pour la Vérification

1. **Protection de /wp-admin :**
   - Tenter d'accéder à `https://[site]/wp-admin`.
   - Vérifier si une page de connexion sécurisée apparaît ou si l'accès est libre.

2. **Liste des Utilisateurs :**
   - Utiliser la commande curl pour lister les utilisateurs via l'API REST :
     ```bash
     curl -s https://[site]/wp-json/wp/v2/users
     ```
   - Noter les utilisateurs retournés.

# Importance de la Sécurité

La vérification de ces éléments est cruciale pour garantir la sécurité des sites WordPress. Les administrateurs de sites doivent :

- Protéger l'accès à l'administration (`/wp-admin`).
- Empêcher les accès non autorisés aux informations des utilisateurs via l'API REST.
- Mettre en œuvre des mesures de sécurité supplémentaires comme l'authentification à deux facteurs (2FA) et la limitation des tentatives de connexion.

Ces pratiques permettent de réduire les risques de compromission et d'assurer la sécurité des données.
