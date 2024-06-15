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



# ANNEXE  - PLUS DE DÉTAILS 


# Collecte d'Informations en Cybersécurité et Footprinting (ÉTAPE 1 DE LA PROCÉDURE D'ATTAQUE)

## Introduction

La collecte d'informations ou "footprinting" est la première étape dans le cycle d'une attaque informatique ou d'une évaluation de la sécurité. Elle permet de recueillir des données sur la cible, telles que les adresses IP, les noms de domaine, les sous-domaines, les serveurs, et les technologies utilisées. Ce guide détaille exhaustivement les différentes étapes et outils pour réaliser une collecte d'informations approfondie sur un site web.

## Étapes Détaillées

### 1. **Démonstration 1 : Collecte d'informations sur le site web**

#### Étape 1 : Ouvrir Whois DomainTools

1. **Ouvrez le navigateur et allez sur [whois.domaintools.com](https://whois.domaintools.com)** :
   - Whois DomainTools est un service en ligne qui permet d'obtenir des informations détaillées sur les noms de domaine enregistrés. Il fournit des données sur le propriétaire du domaine, les contacts administratifs, techniques, et de facturation, ainsi que les serveurs DNS et l'historique de l'enregistrement.

#### Étape 2 : Rechercher un domaine

2. **Entrez le nom de domaine (www.microsoft.com) et cliquez sur rechercher** :
   - La recherche WHOIS renvoie des informations telles que la date de création du domaine, la date d'expiration, les informations sur le registraire, et les coordonnées du propriétaire du domaine.

#### Étape 3 : Analyser les résultats

3. **Les résultats seront affichés dans l'enregistrement Whois** :
   - Notez les informations importantes telles que les adresses e-mail des contacts, les serveurs DNS, et l'historique du domaine.

#### Étape 4 : Détails de l'adresse IP

4. **Trouvez les détails relatifs à l'adresse IP et à la localisation de l'adresse IP** :
   - Utilisez les informations WHOIS pour identifier l'adresse IP du domaine. Vous pouvez ensuite utiliser des outils comme [IP Location](https://www.iplocation.net) pour trouver la localisation géographique de l'adresse IP.

#### Étape 5 : Utiliser Netcraft

5. **Ouvrez [www.netcraft.com](https://www.netcraft.com) et entrez le site cible (www.microsoft.com)** :
   - Netcraft est un service d'analyse de sites web qui fournit des informations détaillées sur les technologies utilisées par le site, l'historique des certificats SSL, et les rapports de sécurité.

#### Étape 6 : Générer un rapport Netcraft

6. **Netcraft générera le rapport** :
   - Le rapport inclura des informations sur les technologies utilisées par le site, comme le serveur web, le système d'exploitation, et les langages de programmation.

#### Étape 7 : Algorithme public et historique IP

7. **Obtenez des informations sur l'algorithme public, le numéro de série et les détails de l'historique IP** :
   - Netcraft peut fournir des détails sur l'algorithme de chiffrement utilisé par le site, le numéro de série du certificat SSL, et l'historique des adresses IP associées au domaine.

#### Étape 8 : Technologies de site

8. **Netcraft montrera les détails des technologies de site** :
   - Vous pouvez voir des informations sur les serveurs web, les frameworks utilisés, les systèmes de gestion de contenu, et les services tiers intégrés.

#### Étape 9 : Utiliser Shodan

9. **Ouvrez [www.shodan.io](http://www.shodan.io), recherchez Microsoft.com et cliquez sur "Go"** :
   - Shodan est un moteur de recherche pour les appareils connectés à Internet. Il permet de découvrir des informations sur les serveurs, les caméras, les routeurs, et d'autres appareils connectés.

#### Étape 10 : Résultats Shodan

10. **Les résultats affichent les serveurs de Microsoft** :
    - Shodan montre les serveurs associés au domaine cible, incluant les adresses IP, les ports ouverts, et les services en cours d'exécution.

#### Étape 11 : Informations du serveur

11. **Cliquez sur les informations du premier serveur** :
    - Accédez aux détails spécifiques du serveur, comme les versions des logiciels utilisés, les configurations, et les vulnérabilités potentielles.

#### Étape 12 : Détails du serveur

12. **Trouvez l'adresse IP du serveur, les numéros de port ouverts, et les services en cours d'exécution** :
    - Notez ces informations pour une analyse ultérieure ou pour préparer des étapes de test d'intrusion.

#### Étape 13 : Informations sur le certificat SSL

13. **Faites défiler pour voir les informations relatives au certificat SSL** :
    - Shodan affiche également des détails sur les certificats SSL utilisés, comme l'autorité de certification, la date d'expiration, et les algorithmes de chiffrement.

### 2. **Sites de Footprinting Utiles**

Voici une liste exhaustive de sites et outils utiles pour la collecte d'informations et le footprinting :

1. **[https://censys.io](https://censys.io)** : 
   - Censys est un moteur de recherche pour les appareils connectés à Internet. Il collecte des données sur les adresses IP, les certificats SSL, et les configurations de serveurs.

2. **[http://whois.domaintools.com](http://whois.domaintools.com)** :
   - Whois DomainTools fournit des informations détaillées sur les noms de domaine enregistrés, incluant les contacts administratifs, techniques, et de facturation.

3. **[https://toolbar.netcraft.com](https://toolbar.netcraft.com)** :
   - Netcraft offre des rapports détaillés sur les sites web, incluant les technologies utilisées, les historiques des certificats SSL, et les rapports de sécurité.

4. **[https://www.shodan.io](https://www.shodan.io)** :
   - Shodan est un moteur de recherche pour les appareils connectés à Internet, permettant de découvrir des informations sur les serveurs, les caméras, les routeurs, et d'autres appareils.

5. **[https://www.hybrid-analysis.com](https://www.hybrid-analysis.com)** :
   - Hybrid Analysis fournit des rapports détaillés sur les analyses de malwares, incluant les comportements des fichiers suspects et les indicateurs de compromission.

6. **[https://osintframework.com](https://osintframework.com)** :
   - OSINT Framework est une collection d'outils et de ressources pour la collecte d'informations en open source intelligence (OSINT).

7. **[https://www.virustotal.com](https://www.virustotal.com)** :
   - VirusTotal est un service en ligne qui analyse les fichiers et les URL pour détecter les malwares en utilisant plusieurs moteurs antivirus.

8. **[https://suip.biz](https://suip.biz)** :
   - SUIP est une plateforme qui offre divers outils pour la collecte d'informations, l'analyse de sécurité, et le test d'intrusion.

9. **[http://www.zabasearch.com](http://www.zabasearch.com)** :
   - ZabaSearch est un moteur de recherche pour trouver des informations sur les personnes, incluant les adresses, les numéros de téléphone, et les antécédents.

10. **[https://pipl.com](https://pipl.com)** :
    - Pipl est un moteur de recherche pour les informations sur les personnes, permettant de trouver des profils en ligne, des adresses e-mail, et d'autres informations personnelles.

11. **[http://www.intelius.com](http://www.intelius.com)** :
    - Intelius est un service de recherche de personnes qui fournit des rapports détaillés sur les antécédents, incluant les adresses, les numéros de téléphone, et les casiers judiciaires.

12. **[http://www.ussearch.com](http://www.ussearch.com)** :
    - US Search offre des services de recherche de personnes, permettant de trouver des informations sur les adresses, les numéros de téléphone, et les antécédents.

13. **[http://www.123people.com](http://www.123people.com)** :
    - 123People est un moteur de recherche pour les informations sur les personnes, incluant les profils en ligne, les adresses e-mail, et les numéros de téléphone.

14. **[https://records.txdps.state.tx.us/DpsWebsite/CriminalHistory/](https://records.txdps.state.tx.us/DpsWebsite/CriminalHistory/)** :
    - Ce site offre des services de recherche de casiers judiciaires, permettant de trouver des informations sur les antécédents criminels au Texas.

15. **[http://socialcatfish.com](http://socialcatfish.com)** :
    - Social Catfish est un service de vérification d'identité en ligne, permettant de vérifier les profils en ligne et de prévenir les arnaques.

### 3. **Démonstration 2 : Collecte d'informations avec Recon-ng dans Kali Linux**

Recon-ng est un framework de collecte d'informations open-source intégré dans Kali Linux. Voici un guide détaillé pour l'utiliser :

#### Étape 1 : Ouvrir Recon-ng

1. **Ouvrez Kali Linux puis allez dans Applications → Collecte d'informations → Recon-ng** :
   - Recon-ng offre une interface modulaire et scriptable pour la collecte d'informations, similaire à Metasploit.

#### Étape 2 : Installer les modules

2. **Installez tous les

 modules en utilisant l'option "installer tout"** :
   - Utilisez la commande `marketplace install all` pour installer tous les modules disponibles.

#### Étape 3 : Ajouter des domaines

3. **Ajoutez des domaines avec la commande `db insert domains`. Affichez les domaines avec `show domains`** :
   - Ajoutez le domaine cible à la base de données locale de Recon-ng pour commencer la collecte d'informations.

#### Étape 4 : Rechercher des informations par courrier électronique

4. **Recherchez des informations par courrier électronique** :
   - Utilisez les modules suivants pour rechercher des contacts par e-mail :
     - `marketplace search`  
     - `marketplace install recon/domains-contacts/whois_pocs`
     - `modules load recon/domains-contacts/whois_pocs`
     - `options set SOURCE Microsoft.com`
     - `run`

#### Étape 5 : Rechercher des sous-domaines

5. **Pour recueillir des informations sur les sous-domaines** :
   - Utilisez les modules suivants :
     - `modules load recon/domains-hosts/bing_domain_web`
     - `options set SOURCE Microsoft.com`
     - `run`

#### Étape 6 : Trouver l'enregistrement MX et l'adresse IP

6. **Pour trouver l'enregistrement MX et l'adresse IP** :
   - Utilisez les modules suivants :
     - `marketplace install recon/domains-hosts/brute_hosts`
     - `modules load recon/domains-hosts/brute_hosts`
     - `options set SOURCE Microsoft.com`
     - `run`

#### Étape 7 : Collecter des informations sur les fichiers intéressants

7. **Pour recueillir des informations sur les codes serveur** :
   - Utilisez les modules suivants :
     - `marketplace install discovery/info_disclosure/interesting_files`
     - `modules load discovery/info_disclosure/interesting_files`
     - `run`

#### Étape 8 : Afficher le tableau de bord des résultats

8. **Pour afficher le tableau de bord des résultats** :
   - Utilisez les commandes suivantes :
     - `show contacts`
     - `show domains`
     - `show hosts`

#### Étape 9 : Exporter les résultats en HTML

9. **Pour exporter les résultats en HTML** :
   - Utilisez les modules suivants :
     - `marketplace install reporting/html`
     - `modules load reporting/html`
     - `options set CREATOR vishwa`
     - `options set CUSTOMER microsoft.com`
     - `run`

### 4. **Démonstration 3 : Collecte d'informations avec Maltego**

Maltego est un outil puissant pour la collecte et la visualisation d'informations. Voici comment l'utiliser dans Kali Linux :

#### Étape 1 : Ouvrir Maltego

1. **Ouvrez Kali Linux et recherchez Maltego, puis cliquez sur Maltego CE** :
   - Maltego CE (Community Edition) est la version gratuite de Maltego qui permet de réaliser des transformations de base pour la collecte d'informations.

#### Étape 2 : Accepter l'Accord de licence

2. **Acceptez l'Accord de licence** :
   - Lisez et acceptez les termes de l'accord de licence pour utiliser Maltego.

#### Étape 3 : Inscription

3. **Inscrivez-vous sur Maltego** :
   - Créez un compte Maltego pour accéder aux fonctionnalités de l'outil.

#### Étape 4 : Connexion

4. **Connectez-vous au compte Maltego dans l'application** :
   - Utilisez vos identifiants pour vous connecter et accéder à l'interface de Maltego.

#### Étape 5 : Modules complémentaires

5. **Les modules complémentaires de transformations par défaut seront ajoutés** :
   - Maltego inclut des transformations par défaut pour la collecte d'informations sur les domaines, les adresses e-mail, les noms d'hôte, etc.

#### Étape 6 : Nouvel espace de travail

6. **Cliquez sur Nouveau pour l'espace de travail** :
   - Créez un nouvel espace de travail pour organiser votre collecte d'informations.

#### Étape 7 : Ajouter un domaine

7. **Cliquez sur Domaines dans le panneau de gauche** :
   - Ajoutez un domaine cible pour commencer la collecte d'informations.

#### Étape 8 : Écrire le nom de domaine

8. **Écrire le nom de domaine (Microsoft.com) sans protocole www** :
   - Entrez le nom de domaine cible dans le champ approprié.

#### Étape 9 : Collecter des adresses e-mail

9. **Cliquez avec le bouton droit de la souris et sélectionnez les adresses électroniques** :
   - Utilisez les transformations de Maltego pour collecter les adresses e-mail associées au domaine.

#### Étape 10 : Détails du serveur de domaine

10. **Collectez tous les détails du serveur de domaine** :
    - Cliquez avec le bouton droit de la souris et sélectionnez Vers le domaine pour rechercher d'autres TLD associés.

#### Étape 11 : Collecter des noms d'hôte

11. **Pour collecter les noms d'hôte du domaine, faites un clic droit sur Domaine et sélectionnez Vers le nom DNS** :
    - Utilisez les transformations pour découvrir les noms d'hôte associés au domaine cible.

### 5. **Démonstration 4 : Collecte d'informations sur les sous-domaines**

#### Énoncé du problème 1

1. **Utiliser Sublist3r** :
   - `sublist3r -d www.bing.com` :
     - Sublist3r est un outil de reconnaissance de sous-domaines qui utilise diverses sources pour découvrir les sous-domaines associés à un domaine.

#### Énoncé du problème 2

2. **Utiliser dnsmap et traceroute** :
   - `dnsmap google.com` :
     - dnsmap est un outil de reconnaissance de sous-domaines qui utilise une liste de mots pour découvrir les sous-domaines associés à un domaine.
   - `traceroute 172.217.14.237` :
     - traceroute est un outil de diagnostic réseau qui trace le chemin parcouru par les paquets pour atteindre une adresse IP cible.

### 6. **Démonstration 5 : Suivi de courrier électronique**

#### Étape 1 : Télécharger et installer eMail Tracker Pro

1. **Téléchargez et installez eMail Tracker Pro** :
   - [emailtrackerpro.com](http://www.emailtrackerpro.com) :
     - eMail Tracker Pro est un outil pour analyser les en-têtes des e-mails et suivre l'origine et le chemin parcouru par les e-mails.

#### Étape 2 : Ajouter un compte de messagerie

2. **Allez dans Fichier > Comptes de messagerie** :
   - Ajoutez un compte de messagerie pour commencer à analyser les e-mails.

#### Étape 3 : Ajouter un compte

3. **Cliquez sur ajouter pour ajouter un compte** :
   - Sélectionnez le compte de messagerie que vous souhaitez ajouter.

#### Étape 4 : Sélectionner le compte

4. **Sélectionnez le compte et cliquez sur "OK"** :
   - Confirmez l'ajout du compte de messagerie.

#### Étape 5 : En-têtes de traçage

5. **Sélectionnez les en-têtes de traçage** :
   - Choisissez les en-têtes d'e-mails que vous souhaitez analyser.

#### Étape 6 : Coller les détails de l'en-tête

6. **Collez les détails de l'en-tête de l'e-mail et cliquez sur Tracer** :
   - Entrez les informations de l'en-tête de l'e-mail et lancez l'analyse.

#### Étape 7 : Résultats

7. **Les résultats sont affichés** :
   - Les résultats incluent des informations sur l'origine de l'e-mail, le chemin parcouru, et les serveurs intermédiaires.

#### Étape 1 (b) : Sélectionner le message d'origine

8. **Sélectionnez le message d'origine pour afficher les en-têtes de messagerie** :
   - Affichez les en-têtes complets du message pour une analyse plus approfondie.

### 7. **Démonstration 6 : Tracé DNS**

#### Commande dnsrecon

1. **Utiliser dnsrecon pour le tracé DNS** :
   - `dnsrecon -d foxnews.co` :
     - dnsrecon est un outil pour effectuer diverses enquêtes DNS, incluant la découverte de serveurs de noms, d'enregistrements MX, et d'autres informations DNS.

### 8. **Démonstration 7 : Collecte d'informations sur un domaine à l'aide de Sublist3r**

#### Étape 1 : Trouver les sous-domaines

1. **Ouvrez Kali Linux et utilisez l'outil Sublist3r pour trouver les sous-domaines** :
   - `sublist3r -d www.bing.com` :
     - Utilisez Sublist3r pour découvrir les sous-domaines associés au domaine cible.

#### Étape 2 : Utiliser des threads

2. **Utiliser des threads pour rechercher les sous-domaines avec le port HTTPS ouvert** :
   - `sublist3r -d www.bing.com -t 50 -p 443` :
     - Utilisez des threads pour accélérer la recherche et spécifiez le port HTTPS pour découvrir les sous-domaines accessibles via HTTPS.

### 9. **Démonstration 8 :

 Utilisation de dnsmap**

#### Étape 1 : Trouver les sous-domaines

1. **Trouver les sous-domaines d'un domaine cible** :
   - `dnsmap google.com` :
     - Utilisez dnsmap pour découvrir les sous-domaines associés à un domaine cible.

#### Étape 2 : Utiliser traceroute

2. **Utiliser traceroute pour trouver le chemin jusqu'à une adresse IP** :
   - `traceroute 172.217.14.237` :
     - Utilisez traceroute pour tracer le chemin parcouru par les paquets pour atteindre une adresse IP cible.

### 10. **Démonstration 9 : Pister les découvertes par e-mail avec eMail Tracker Pro**

#### Étape 1 : Télécharger et installer eMail Tracker Pro

1. **Téléchargez et installez eMail Tracker Pro** :
   - [emailtrackerpro.com](http://www.emailtrackerpro.com) :
     - Téléchargez et installez eMail Tracker Pro pour analyser et suivre les e-mails.

#### Étape 2 : Ajouter un compte de messagerie

2. **Allez dans Fichier > Comptes de messagerie** :
   - Ajoutez un compte de messagerie pour commencer à analyser les e-mails.

#### Étape 3 : Ajouter un compte

3. **Cliquez sur ajouter pour ajouter un compte** :
   - Sélectionnez le compte de messagerie que vous souhaitez ajouter.

#### Étape 4 : Sélectionner le compte

4. **Sélectionnez le compte et cliquez sur "OK"** :
   - Confirmez l'ajout du compte de messagerie.

#### Étape 5 : En-têtes de traçage

5. **Sélectionnez les en-têtes de traçage** :
   - Choisissez les en-têtes d'e-mails que vous souhaitez analyser.

#### Étape 6 : Coller les détails de l'en-tête

6. **Collez les détails de l'en-tête de l'e-mail et cliquez sur Tracer** :
   - Entrez les informations de l'en-tête de l'e-mail et lancez l'analyse.

#### Étape 7 : Résultats

7. **Les résultats sont affichés** :
   - Les résultats incluent des informations sur l'origine de l'e-mail, le chemin parcouru, et les serveurs intermédiaires.

#### Étape 1 (b) : Sélectionner le message d'origine

8. **Sélectionnez le message d'origine pour afficher les en-têtes de messagerie** :
   - Affichez les en-têtes complets du message pour une analyse plus approfondie.

### 11. **Démonstration 10 : Utilisation des outils d'interrogation DNS pour le footprinting**

#### Commande dnsrecon

1. **Utiliser dnsrecon pour le tracé DNS** :
   - `dnsrecon -d foxnews.co` :
     - dnsrecon est un outil pour effectuer diverses enquêtes DNS, incluant la découverte de serveurs de noms, d'enregistrements MX, et d'autres informations DNS.

### 12. **Démonstration 11 : Utilisation de l'outil Maltego pour la collecte d'informations**

#### Étape 1 : Ouvrir Maltego

1. **Ouvrez Kali Linux et recherchez Maltego, puis cliquez sur Maltego CE** :
   - Maltego CE (Community Edition) est la version gratuite de Maltego qui permet de réaliser des transformations de base pour la collecte d'informations.

#### Étape 2 : Accepter l'Accord de licence

2. **Acceptez l'Accord de licence** :
   - Lisez et acceptez les termes de l'accord de licence pour utiliser Maltego.

#### Étape 3 : Inscription

3. **Inscrivez-vous sur Maltego** :
   - Créez un compte Maltego pour accéder aux fonctionnalités de l'outil.

#### Étape 4 : Connexion

4. **Connectez-vous au compte Maltego dans l'application** :
   - Utilisez vos identifiants pour vous connecter et accéder à l'interface de Maltego.

#### Étape 5 : Modules complémentaires

5. **Les modules complémentaires de transformations par défaut seront ajoutés** :
   - Maltego inclut des transformations par défaut pour la collecte d'informations sur les domaines, les adresses e-mail, les noms d'hôte, etc.

#### Étape 6 : Nouvel espace de travail

6. **Cliquez sur Nouveau pour l'espace de travail** :
   - Créez un nouvel espace de travail pour organiser votre collecte d'informations.

#### Étape 7 : Ajouter un domaine

7. **Cliquez sur Domaines dans le panneau de gauche** :
   - Ajoutez un domaine cible pour commencer la collecte d'informations.

#### Étape 8 : Écrire le nom de domaine

8. **Écrire le nom de domaine (Microsoft.com) sans protocole www** :
   - Entrez le nom de domaine cible dans le champ approprié.

#### Étape 9 : Collecter des adresses e-mail

9. **Cliquez avec le bouton droit de la souris et sélectionnez les adresses électroniques** :
   - Utilisez les transformations de Maltego pour collecter les adresses e-mail associées au domaine.

#### Étape 10 : Détails du serveur de domaine

10. **Collectez tous les détails du serveur de domaine** :
    - Cliquez avec le bouton droit de la souris et sélectionnez Vers le domaine pour rechercher d'autres TLD associés.

#### Étape 11 : Collecter des noms d'hôte

11. **Pour collecter les noms d'hôte du domaine, faites un clic droit sur Domaine et sélectionnez Vers le nom DNS** :
    - Utilisez les transformations pour découvrir les noms d'hôte associés au domaine cible.

### 13. **Démonstration 12 : Utilisation de Sublist3r pour la collecte d'informations sur les sous-domaines**

#### Étape 1 : Trouver les sous-domaines

1. **Utiliser Sublist3r pour trouver les sous-domaines** :
   - `sublist3r -d www.bing.com` :
     - Sublist3r est un outil de reconnaissance de sous-domaines qui utilise diverses sources pour découvrir les sous-domaines associés à un domaine.

#### Étape 2 : Utiliser des threads

2. **Utiliser des threads pour rechercher les sous-domaines avec le port HTTPS ouvert** :
   - `sublist3r -d www.bing.com -t 50 -p 443` :
     - Utilisez des threads pour accélérer la recherche et spécifiez le port HTTPS pour découvrir les sous-domaines accessibles via HTTPS.

### 14. **Démonstration 13 : Utilisation de dnsmap pour la collecte d'informations sur les sous-domaines**

#### Étape 1 : Trouver les sous-domaines

1. **Trouver les sous-domaines d'un domaine cible** :
   - `dnsmap google.com` :
     - Utilisez dnsmap pour découvrir les sous-domaines associés à un domaine cible.

#### Étape 2 : Utiliser traceroute

2. **Utiliser traceroute pour trouver le chemin jusqu'à une adresse IP** :
   - `traceroute 172.217.14.237` :
     - Utilisez traceroute pour tracer le chemin parcouru par les paquets pour atteindre une adresse IP cible.

### 15. **Démonstration 14 : Suivi de courrier électronique avec eMail Tracker Pro**

#### Étape 1 : Télécharger et installer eMail Tracker Pro

1. **Téléchargez et installez eMail Tracker Pro** :
   - [emailtrackerpro.com](http://www.emailtrackerpro.com) :
     - Téléchargez et installez eMail Tracker Pro pour analyser et suivre les e-mails.

#### Étape 2 : Ajouter un compte de messagerie

2. **Allez dans Fichier > Comptes de messagerie** :
   - Ajoutez un compte de messagerie pour commencer à analyser les e-mails.

#### Étape 3 : Ajouter un compte

3. **Cliquez sur ajouter pour ajouter un compte** :
   - Sélectionnez le compte de messagerie que vous souhaitez ajouter.

#### Étape 4 : Sélectionner le compte

4. **Sélectionnez le compte et cliquez sur "OK"** :
   - Confirmez l'ajout du compte de messagerie.

#### Étape 5 : En-têtes de traçage

5. **Sélectionnez les en-têtes de traçage** :
   - Choisissez les en-têtes d'e-mails que vous souhaitez analyser.

#### Étape 6 : Coller les détails de l'en-tête

6. **Collez les détails de l'en-tête de l'e-mail et cliquez sur Tracer** :
   - Entrez les informations de l'en-tête de l'e-mail et lancez l'analyse.

#### Étape 7 : Résultats

7. **Les résultats sont affichés** :
   - Les résultats incluent des informations sur l'origine de l'e-mail, le chemin parcouru, et les serveurs intermédiaires.

#### Étape 1 (b) : Sélectionner le message d'origine

8. **Sélectionnez le message d'origine pour afficher les en-têtes de messagerie** :
   - Affichez les en-têtes complets du message pour une analyse plus approfondie.

### 16. **Démonstration 15 : Utilisation des outils d'interrogation DNS pour le footprinting**

#### Commande dnsrecon



1. **Utiliser dnsrecon pour le tracé DNS** :
   - `dnsrecon -d foxnews.co` :
     - dnsrecon est un outil pour effectuer diverses enquêtes DNS, incluant la découverte de serveurs de noms, d'enregistrements MX, et d'autres informations DNS.

### 17. **Démonstration 16 : Utilisation de l'outil Maltego pour la collecte d'informations**

#### Étape 1 : Ouvrir Maltego

1. **Ouvrez Kali Linux et recherchez Maltego, puis cliquez sur Maltego CE** :
   - Maltego CE (Community Edition) est la version gratuite de Maltego qui permet de réaliser des transformations de base pour la collecte d'informations.

#### Étape 2 : Accepter l'Accord de licence

2. **Acceptez l'Accord de licence** :
   - Lisez et acceptez les termes de l'accord de licence pour utiliser Maltego.

#### Étape 3 : Inscription

3. **Inscrivez-vous sur Maltego** :
   - Créez un compte Maltego pour accéder aux fonctionnalités de l'outil.

#### Étape 4 : Connexion

4. **Connectez-vous au compte Maltego dans l'application** :
   - Utilisez vos identifiants pour vous connecter et accéder à l'interface de Maltego.

#### Étape 5 : Modules complémentaires

5. **Les modules complémentaires de transformations par défaut seront ajoutés** :
   - Maltego inclut des transformations par défaut pour la collecte d'informations sur les domaines, les adresses e-mail, les noms d'hôte, etc.

#### Étape 6 : Nouvel espace de travail

6. **Cliquez sur Nouveau pour l'espace de travail** :
   - Créez un nouvel espace de travail pour organiser votre collecte d'informations.

#### Étape 7 : Ajouter un domaine

7. **Cliquez sur Domaines dans le panneau de gauche** :
   - Ajoutez un domaine cible pour commencer la collecte d'informations.

#### Étape 8 : Écrire le nom de domaine

8. **Écrire le nom de domaine (Microsoft.com) sans protocole www** :
   - Entrez le nom de domaine cible dans le champ approprié.

#### Étape 9 : Collecter des adresses e-mail

9. **Cliquez avec le bouton droit de la souris et sélectionnez les adresses électroniques** :
   - Utilisez les transformations de Maltego pour collecter les adresses e-mail associées au domaine.

#### Étape 10 : Détails du serveur de domaine

10. **Collectez tous les détails du serveur de domaine** :
    - Cliquez avec le bouton droit de la souris et sélectionnez Vers le domaine pour rechercher d'autres TLD associés.

#### Étape 11 : Collecter des noms d'hôte

11. **Pour collecter les noms d'hôte du domaine, faites un clic droit sur Domaine et sélectionnez Vers le nom DNS** :
    - Utilisez les transformations pour découvrir les noms d'hôte associés au domaine cible.

- Ces étapes couvrent une large gamme de techniques et d'outils pour la collecte d'informations en cybersécurité, offrant une vue complète des pratiques de footprinting et d'analyse de sécurité.
