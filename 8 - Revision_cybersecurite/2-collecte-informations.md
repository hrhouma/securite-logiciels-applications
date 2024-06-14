# Étapes: 

1. **Démonstration 1 : Collecte d'informations sur le site web**
   - Étape 1 : Ouvrez le navigateur et allez sur [whois.domaintools.com](https://whois.domaintools.com)
   - Étape 2 : Entrez le nom de domaine (www.microsoft.com) et cliquez sur rechercher.
   - Étape 3 : Les résultats seront affichés dans l'enregistrement Whois.
   - Étape 4 : Trouvez les détails relatifs à l'adresse IP et à la localisation de l'adresse IP.
   - Étape 5 : Ouvrez [www.netcraft.com](https://www.netcraft.com) et entrez le site cible (www.microsoft.com).
   - Étape 6 : Netcraft générera le rapport.
   - Étape 7 : Obtenez des informations sur l'algorithme public, le numéro de série et les détails de l'historique IP.
   - Étape 8 : Netcraft montrera les détails des technologies de site.
   - Étape 9 : Ouvrez [www.shodan.io](http://www.shodan.io), recherchez Microsoft.com et cliquez sur "Go".
   - Étape 10 : Les résultats affichent les serveurs de Microsoft.
   - Étape 11 : Cliquez sur les informations du premier serveur.
   - Étape 12 : Trouvez l'adresse IP du serveur, les numéros de port ouverts, et les services en cours d'exécution.
   - Étape 13 : Faites défiler pour voir les informations relatives au certificat SSL.

2. **Sites de footprinting utiles :**
   - [https://censys.io](https://censys.io)
   - [http://whois.domaintools.com](http://whois.domaintools.com)
   - [https://toolbar.netcraft.com](https://toolbar.netcraft.com)
   - [https://www.shodan.io](https://www.shodan.io)
   - [https://www.hybrid-analysis.com](https://www.hybrid-analysis.com)
   - [https://osintframework.com](https://osintframework.com)
   - [https://www.virustotal.com](https://www.virustotal.com)
   - [https://suip.biz](https://suip.biz)
   - [http://www.zabasearch.com](http://www.zabasearch.com)
   - [https://pipl.com](https://pipl.com)
   - [http://www.intelius.com](http://www.intelius.com)
   - [http://www.ussearch.com](http://www.ussearch.com)
   - [http://www.123people.com](http://www.123people.com)
   - [https://records.txdps.state.tx.us/DpsWebsite/CriminalHistory/](https://records.txdps.state.tx.us/DpsWebsite/CriminalHistory/)
   - [http://socialcatfish.com](http://socialcatfish.com)

3. **Démonstration 2 : Collecte d'informations avec Recon-ng dans Kali Linux**
   - Étape 1 : Ouvrez Kali Linux puis allez dans Applications → Collecte d'informations → Recon-ng
   - Étape 2 : Installez tous les modules en utilisant l'option "installer tout".
   - Étape 3 : Ajoutez des domaines avec la commande `db insert domains`. Affichez les domaines avec `show domains`.
   - Étape 4 : Recherchez des informations par courrier électronique :
     - `marketplace search`  
     - `marketplace install recon/domains-contacts/whois_pocs`
     - `modules load recon/domains-contacts/whois_pocs`
     - `options set SOURCE Microsoft.com`
     - `run`
   - Étape 5 : Pour recueillir des informations sur les sous-domaines :
     - `modules load recon/domains-hosts/bing_domain_web`
     - `options set SOURCE Microsoft.com`
     - `run`
   - Étape 6 : Pour trouver l'enregistrement MX et l'adresse IP :
     - `marketplace install recon/domains-hosts/brute_hosts`
     - `modules load recon/domains-hosts/brute_hosts`
     - `options set SOURCE Microsoft.com`
     - `run`
   - Étape 7 : Pour recueillir des informations sur les codes serveur :
     - `marketplace install discovery/info_disclosure/interesting_files`
     - `modules load discovery/info_disclosure/interesting_files`
     - `run`
   - Étape 8 : Pour afficher le tableau de bord des résultats :
     - `show contacts`
     - `show domains`
     - `show hosts`
   - Étape 9 : Pour exporter les résultats en HTML :
     - `marketplace install reporting/html`
     - `modules load reporting/html`
     - `options set CREATOR vishwa`
     - `options set CUSTOMER microsoft.com`
     - `run`

4. **Démonstration 3 : Collecte d'informations avec Maltego**
   - Étape 1 : Ouvrez Kali Linux et recherchez Maltego, puis cliquez sur Maltego CE.
   - Étape 2 : Acceptez l'Accord de licence.
   - Étape 3 : Inscrivez-vous sur Maltego.
   - Étape 4 : Connectez-vous au compte Maltego dans l'application.
   - Étape 5 : Les modules complémentaires de transformations par défaut seront ajoutés.
   - Étape 6 : Cliquez sur Nouveau pour l'espace de travail.
   - Étape 7 : Cliquez sur Domaines dans le panneau de gauche.
   - Étape 8 : Écrire le nom de domaine (Microsoft.com) sans protocole www.
   - Étape 9 : Cliquez avec le bouton droit de la souris et sélectionnez les adresses électroniques.
   - Étape 10 : Collectez tous les détails du serveur de domaine.
   - Étape 11 : Pour collecter les noms d'hôte du domaine, faites un clic droit sur Domaine et sélectionnez Vers le nom DNS.

5. **Démonstration 4 : Collecte d'informations sur les sous-domaines**
   - Énoncé du problème 1 :
     - `sublist3r -d www.bing.com`
     - `sublist3r -d www.bing.com -t 50 -p 443`
   - Énoncé du problème 2 :
     - `dnsmap google.com`
     - `traceroute 172.217.14.237`

6. **Démonstration 5 : Suivi de courrier électronique**
   - Étape 1 : Téléchargez et installez eMail Tracker Pro.
   - Étape 2 : Allez dans Fichier > Comptes de messagerie.
   - Étape 3 : Cliquez sur ajouter pour ajouter un compte.
   - Étape 4 : Sélectionnez le compte et cliquez sur "OK".
   - Étape 5 : Sélectionnez les en-têtes de traçage.
   - Étape 6 : Collez les détails de l'en-tête de l'e-mail et cliquez sur Tracer.
   - Étape 7 : Les résultats sont affichés.
   - Étape 1 (b) : Sélectionnez le message d'origine pour afficher les en-têtes de messagerie.

7. **Démonstration 6 : Tracé DNS**
   - `dnsrecon -d foxnews.co`

8. **Démonstration 7 : Collecte d'informations sur un domaine à l'aide de l'outil Sublist3r**
   - Étape 1 : Ouvrez Kali Linux et utilisez l'outil Sublist3r pour trouver les sous-domaines :
     - `sublist3r -d www.bing.com`
   - Étape 2 : Utilisez des threads pour rechercher les sous-domaines avec le port HTTPS ouvert :
     - `sublist3r -d www.bing.com -t 50 -p 443`

9. **Démonstration 8 : Utilisation de l'outil dnsmap**
   - Étape 1 : Trouver les sous-domaines d'un domaine cible :
     - `dnsmap google.com`
   - Étape 2 : Utiliser traceroute pour trouver le chemin jusqu'à une adresse IP :
     - `traceroute 172.217.14.237`

10. **Démonstration 9 : Pister les découvertes par email avec eMail Tracker Pro**
    - Étape 1 : Téléchargez et installez eMail Tracker Pro depuis [emailtrackerpro.com](http://www.emailtrackerpro.com)
    - Étape 2 : Après l'installation, allez dans Fichier > Comptes de messagerie
    - Étape 3 : Cliquez sur ajouter pour ajouter un compte
    - Étape 4 : Sélectionnez le compte et cliquez sur "OK"
    - Étape 5 : Sélectionnez les en-têtes de traçage sous l'onglet Fichier
    - Étape 6 : Collez les détails de l'en-tête de l'e-mail que vous souhaitez suivre et cliquez sur Tracer
    - Étape 7 : Les résultats sont maintenant affichés et vous pouvez les retracer à partir du Résumé par e-mail
    - Étape 1 (b) : Sélectionnez le message d'origine dans les options de l'e-mail pour afficher les en-têtes

11. **Démonstration 10 : Utilisation des outils d'interrogation DNS pour le footprinting**
    - Outil utilisé : Outils d'interrogation DNS
    - Commande :
      - `dnsrecon -d foxnews.co`

12. **Démonstration 11 : Utilisation de l'outil Maltego pour la collecte d'informations**
    - Étape 1 : Ouvrez Kali Linux et recherchez le logiciel Maltego
    - Étape 2 : Acceptez l'Accord de licence
    - Étape 3 : Inscrivez-vous sur Maltego
    - Étape 4 : Connectez-vous au compte Maltego dans l'application
    - Étape 5 : Les modules complémentaires de transformations par défaut seront ajoutés
    - Étape 6 : Cliquez sur Nouveau pour l'espace de

travail
    - Étape 7 : Cliquez sur Domaines dans le panneau de gauche
    - Étape 8 : Écrivez le nom de domaine (Microsoft.com) sans protocole www
    - Étape 9 : Cliquez avec le bouton droit de la souris et sélectionnez les adresses électroniques
    - Étape 10 : Collectez tous les détails du serveur de domaine -> Cliquez avec le bouton droit de la souris et sélectionnez Vers le domaine (rechercher d'autres TLD)
    - Étape 11 : Pour collecter les noms d'hôte du domaine, faites un clic droit sur Domaine et sélectionnez Vers le nom DNS

13. **Démonstration 12 : Utilisation de l'outil Sublist3r pour la collecte d'informations sur les sous-domaines**
    - Étape 1 : Trouver les sous-domaines de www.bing.com avec :
      - `sublist3r -d www.bing.com`
    - Étape 2 : Utiliser des threads pour rechercher les sous-domaines avec le port HTTPS ouvert :
      - `sublist3r -d www.bing.com -t 50 -p 443`

14. **Démonstration 13 : Utilisation de l'outil dnsmap pour la collecte d'informations sur les sous-domaines**
    - Étape 1 : Trouver les sous-domaines de google.com avec :
      - `dnsmap google.com`
    - Étape 2 : Utiliser traceroute pour trouver le chemin jusqu'à une adresse IP trouvée à l'étape précédente :
      - `traceroute 172.217.14.237`

15. **Démonstration 14 : Suivi de courrier électronique avec eMail Tracker Pro**
    - Étape 1 : Téléchargez et installez eMail Tracker Pro depuis [emailtrackerpro.com](http://www.emailtrackerpro.com)
    - Étape 2 : Après l'installation, allez dans Fichier > Comptes de messagerie
    - Étape 3 : Cliquez sur ajouter pour ajouter un compte
    - Étape 4 : Sélectionnez le compte et cliquez sur "OK"
    - Étape 5 : Sélectionnez les en-têtes de traçage sous l'onglet Fichier
    - Étape 6 : Collez les détails de l'en-tête de l'e-mail que vous souhaitez suivre et cliquez sur Tracer
    - Étape 7 : Les résultats sont maintenant affichés et vous pouvez les retracer à partir du Résumé par e-mail
    - Étape 1 (b) : Sélectionnez le message d'origine dans les options de l'e-mail pour afficher les en-têtes

16. **Démonstration 15 : Utilisation des outils d'interrogation DNS pour le footprinting**
    - Commande :
      - `dnsrecon -d foxnews.co`

17. **Démonstration 16 : Utilisation de l'outil Maltego pour la collecte d'informations**
    - Étape 1 : Ouvrez Kali Linux et recherchez le logiciel Maltego
    - Étape 2 : Acceptez l'Accord de licence
    - Étape 3 : Inscrivez-vous sur Maltego
    - Étape 4 : Connectez-vous au compte Maltego dans l'application
    - Étape 5 : Les modules complémentaires de transformations par défaut seront ajoutés
    - Étape 6 : Cliquez sur Nouveau pour l'espace de travail
    - Étape 7 : Cliquez sur Domaines dans le panneau de gauche
    - Étape 8 : Écrivez le nom de domaine (Microsoft.com) sans protocole www
    - Étape 9 : Cliquez avec le bouton droit de la souris et sélectionnez les adresses électroniques
    - Étape 10 : Collectez tous les détails du serveur de domaine -> Cliquez avec le bouton droit de la souris et sélectionnez Vers le domaine (rechercher d'autres TLD)
    - Étape 11 : Pour collecter les noms d'hôte du domaine, faites un clic droit sur Domaine et sélectionnez Vers le nom DNS

- Ces commandes couvrent diverses démonstrations sur la collecte d'informations en cybersécurité et piratage éthique, utilisant des outils en ligne, Recon-ng, Maltego, Sublist3r, dnsmap, et eMail Tracker Pro.
