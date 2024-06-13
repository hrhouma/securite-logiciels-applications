### Introduction à Nessus

#### Objectifs du cours
1. **Comprendre les bases de Nessus**
   - Qu'est-ce que Nessus ?
   - Pourquoi utiliser Nessus ?
2. **Installation et configuration de Nessus**
   - Installation sur différents systèmes d'exploitation
   - Configuration initiale et création d'un compte
3. **Utilisation de Nessus pour scanner les vulnérabilités**
   - Création et exécution de scans
   - Analyse des résultats
4. **Gestion des rapports de vulnérabilités**
   - Génération de rapports
   - Interprétation des résultats
   - Priorisation et remédiation des vulnérabilités
5. **Manipulations intermédiaires et avancées**
   - Configuration avancée des scans
   - Utilisation de plugins et politiques personnalisées
   - Automatisation des scans avec l'API Nessus

### Partie 1: Introduction à Nessus

#### Qu'est-ce que Nessus ?
Nessus est un scanner de vulnérabilités développé par Tenable, Inc. Il est utilisé pour identifier les failles de sécurité dans les systèmes informatiques. Nessus permet de scanner des réseaux et des systèmes pour trouver des vulnérabilités, des configurations erronées, des logiciels obsolètes, etc.

#### Pourquoi utiliser Nessus ?
- **Identification proactive des vulnérabilités** : Permet de détecter les failles avant qu'elles ne soient exploitées.
- **Facilité d'utilisation** : Interface utilisateur intuitive.
- **Rapports détaillés** : Fournit des informations complètes et des recommandations pour corriger les vulnérabilités.

### Partie 2: Installation et configuration de Nessus

#### Installation sur Windows
1. Télécharger Nessus depuis le site officiel de Tenable.
2. Exécuter l'installateur et suivre les instructions à l'écran.
3. Une fois l'installation terminée, ouvrir un navigateur web et accéder à `https://localhost:8834` pour la configuration initiale.

#### Installation sur Linux
1. Télécharger le paquet Nessus pour Linux.
2. Installer le paquet en utilisant les commandes appropriées pour votre distribution (ex : `sudo dpkg -i` pour Debian/Ubuntu ou `sudo rpm -ivh` pour RedHat/CentOS).
3. Démarrer le service Nessus avec `sudo systemctl start nessusd`.
4. Accéder à `https://localhost:8834` pour la configuration initiale.

#### Configuration initiale et création d'un compte
1. Créer un compte utilisateur pour accéder à l'interface de Nessus.
2. Saisir la clé de licence (si nécessaire).
3. Mettre à jour les plugins de Nessus pour avoir la base de données de vulnérabilités la plus récente.


### Partie 3: Utilisation de Nessus pour scanner les vulnérabilités

#### Création et exécution de scans
1. **Création d'un nouveau scan** :
   - Se connecter à l'interface Nessus.
   - Aller à l'onglet "Scans" et cliquer sur "New Scan".
   - Choisir un modèle de scan en fonction des besoins (ex : Basic Network Scan, Web Application Test, etc.).
   - Configurer les paramètres du scan (nom, description, cibles, etc.).

2. **Exécution d'un scan** :
   - Sélectionner le scan créé et cliquer sur "Launch".
   - Surveiller la progression du scan en temps réel.

#### Analyse des résultats
1. Une fois le scan terminé, cliquer sur le scan pour voir les résultats.
2. Les résultats sont catégorisés par niveaux de sévérité (critique, haute, moyenne, basse, info).
3. Examiner chaque vulnérabilité trouvée pour comprendre les risques et les mesures correctives recommandées.

### Partie 4: Gestion des rapports de vulnérabilités

#### Génération de rapports
1. Depuis l'interface des résultats du scan, cliquer sur "Report".
2. Choisir le format du rapport (PDF, HTML, CSV, etc.).
3. Personnaliser le rapport en incluant/excluant certaines sections ou informations.

#### Interprétation des résultats
1. Comprendre les descriptions des vulnérabilités et les CVE (Common Vulnerabilities and Exposures) associés.
2. Utiliser les informations fournies par Nessus pour évaluer l'impact potentiel des vulnérabilités.

#### Priorisation et remédiation des vulnérabilités
1. Prioriser les vulnérabilités en fonction de leur sévérité et de l'impact potentiel sur l'organisation.
2. Mettre en place des actions correctives :
   - Appliquer les correctifs (patches) recommandés.
   - Modifier les configurations pour corriger les failles de sécurité.
   - Mettre à jour les logiciels obsolètes.

### Partie 5: Manipulations intermédiaires et avancées

#### Configuration avancée des scans
1. **Utilisation de modèles de scan avancés** :
   - Sélectionner des modèles de scan spécifiques (comme Advanced Network Scan).
   - Configurer les paramètres avancés : ports à scanner, plages d'adresses IP, etc.

2. **Personnalisation des politiques de scan** :
   - Créer des politiques de scan personnalisées adaptées aux besoins spécifiques de l'organisation.
   - Configurer des politiques de sécurité spécifiques (ex : SCADA, PCI DSS, etc.).

#### Utilisation de plugins et politiques personnalisées
1. **Plugins Nessus** :
   - Accéder à la liste des plugins Nessus et comprendre leur rôle.
   - Activer ou désactiver des plugins spécifiques en fonction des besoins du scan.
   - Mettre à jour régulièrement les plugins pour bénéficier des dernières détections de vulnérabilités.

2. **Politiques personnalisées** :
   - Créer des politiques de scan sur mesure en définissant des paramètres spécifiques comme les ports, les protocoles, et les types de vulnérabilités à rechercher.
   - Sauvegarder et réutiliser ces politiques pour des scans réguliers.

#### Automatisation des scans avec l'API Nessus
1. **Introduction à l'API Nessus** :
   - Présentation des capacités de l'API Nessus pour automatiser les tâches de scan.
   - Comprendre les endpoints disponibles et comment les utiliser.

2. **Utilisation de l'API pour automatiser les scans** :
   - Exemples de scripts pour lancer des scans, récupérer des résultats et générer des rapports automatiquement.
   - Intégration avec des outils de gestion de la sécurité et des systèmes de ticketing pour la remédiation des vulnérabilités.

3. **Exemple de script en Python** :
   ```python
   import requests
   import json

   # URL et credentials Nessus
   url = "https://localhost:8834"
   username = "votre_nom_utilisateur"
   password = "votre_mot_de_passe"

   # Connexion à Nessus
   login_url = f"{url}/session"
   payload = {"username": username, "password": password}
   headers = {"Content-Type": "application/json"}
   response = requests.post(login_url, data=json.dumps(payload), headers=headers, verify=False)
   token = response.json()['token']

   # Lancer un scan
   scan_url = f"{url}/scans/1/launch"  # Remplacer '1' par l'ID de votre scan
   headers = {"X-Cookie": f"token={token}", "Content-Type": "application/json"}
   response = requests.post(scan_url, headers=headers, verify=False)
   print(response.json())

   # Récupérer les résultats
   result_url = f"{url}/scans/1"  # Remplacer '1' par l'ID de votre scan
   response = requests.get(result_url, headers=headers, verify=False)
   print(json.dumps(response.json(), indent=4))
   ```

### Exercices Pratiques Intermédiaires et Avancés

1. **Configuration avancée des scans** :
   - Configurer un scan avancé pour une plage d'adresses IP spécifiques.
   - Activer des plugins spécifiques pour un type de scan précis.

2. **Création de politiques personnalisées** :
   - Créer une politique de scan personnalisée pour un audit de conformité PCI DSS.
   - Exécuter un scan en utilisant cette politique et analyser les résultats.

3. **Automatisation avec l'API Nessus** :
   - Écrire un script Python pour lancer un scan périodiquement et envoyer les résultats par email.
   - Intégrer l'API Nessus avec un système de gestion des tickets pour créer automatiquement des tickets de remédiation en fonction des vulnérabilités trouvées.

### Conclusion

En maîtrisant les fonctionnalités de base, intermédiaires et avancées de Nessus, vos étudiants seront capables de :
- Effectuer des scans de vulnérabilités de manière efficace et personnalisée.
- Analyser et interpréter les résultats pour une remédiation rapide.
- Automatiser les tâches de sécurité pour une gestion proactive des vulnérabilités.

# Partie 6 - Tutoriel Complet : Exécution d'un Script Python pour Automatiser les Scans Nessus avec FastAPI

#### Objectifs
1. Créer une API REST avec FastAPI pour automatiser les scans Nessus.
2. Utiliser un script Python pour interagir avec l'API Nessus.
3. Exposer des endpoints pour lancer des scans et récupérer des résultats.

### Prérequis
- Python 3.7+
- Nessus installé et configuré
- FastAPI et Uvicorn installés (`pip install fastapi uvicorn`)
- Requests library installée (`pip install requests`)

### Étape 1: Installer les dépendances nécessaires
Ouvrez un terminal et installez les dépendances nécessaires :
```bash
pip install fastapi uvicorn requests
```

### Étape 2: Créer le fichier principal de l'application FastAPI
Créez un fichier nommé `main.py` et ajoutez le code suivant :

```python
from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

NESSUS_URL = "https://localhost:8834"
USERNAME = "votre_nom_utilisateur"
PASSWORD = "votre_mot_de_passe"

def get_token():
    login_url = f"{NESSUS_URL}/session"
    payload = {"username": USERNAME, "password": PASSWORD}
    headers = {"Content-Type": "application/json"}
    response = requests.post(login_url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to authenticate with Nessus")
    return response.json()['token']

@app.get("/launch_scan/{scan_id}")
def launch_scan(scan_id: int):
    token = get_token()
    scan_url = f"{NESSUS_URL}/scans/{scan_id}/launch"
    headers = {"X-Cookie": f"token={token}", "Content-Type": "application/json"}
    response = requests.post(scan_url, headers=headers, verify=False)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to launch scan")
    return response.json()

@app.get("/scan_results/{scan_id}")
def scan_results(scan_id: int):
    token = get_token()
    result_url = f"{NESSUS_URL}/scans/{scan_id}"
    headers = {"X-Cookie": f"token={token}", "Content-Type": "application/json"}
    response = requests.get(result_url, headers=headers, verify=False)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve scan results")
    return response.json()
```

### Étape 3: Démarrer l'application FastAPI
Dans le terminal, lancez l'application FastAPI en utilisant Uvicorn :
```bash
uvicorn main:app --reload
```

L'application sera disponible à l'adresse `http://127.0.0.1:8000`.

### Étape 4: Utiliser l'API FastAPI pour lancer des scans et récupérer les résultats

#### Lancer un scan
Ouvrez un navigateur web ou un outil comme Postman, et accédez à l'URL suivante pour lancer un scan (remplacez `{scan_id}` par l'ID du scan que vous souhaitez lancer) :
```
http://127.0.0.1:8000/launch_scan/{scan_id}
```

#### Récupérer les résultats d'un scan
Accédez à l'URL suivante pour récupérer les résultats d'un scan (remplacez `{scan_id}` par l'ID du scan dont vous souhaitez voir les résultats) :
```
http://127.0.0.1:8000/scan_results/{scan_id}
```

### Étape 5: Tester les endpoints
Vous pouvez tester les endpoints directement depuis le navigateur ou en utilisant un outil comme Postman. Assurez-vous que Nessus est en cours d'exécution et accessible.

### Étape 6: Sécuriser l'API
Pour une utilisation en production, pensez à sécuriser votre API :
- Utilisez HTTPS.
- Mettez en place une authentification et une autorisation pour l'accès aux endpoints.
- Validez les entrées pour éviter les injections.

### Conclusion
Vous avez maintenant une API REST avec FastAPI permettant d'automatiser les scans Nessus et de récupérer les résultats. 
Cette solution permet d'intégrer facilement les scans de vulnérabilités dans des workflows automatisés et des systèmes de gestion de la sécurité.

# Partie 7 - AVANCÉ - Tutoriel Complet : Ajout d'un Frontend à l'API FastAPI pour Automatiser les Scans Nessus

#### Objectifs
1. Créer une API REST avec FastAPI pour automatiser les scans Nessus.
2. Créer un frontend en React pour interagir avec l'API et visualiser les résultats des scans.
3. Utiliser un script Python pour interagir avec l'API Nessus.

### Prérequis
- Python 3.7+
- Nessus installé et configuré
- FastAPI et Uvicorn installés (`pip install fastapi uvicorn`)
- Requests library installée (`pip install requests`)
- Node.js et npm installés (pour créer le frontend React)

### Étape 1: Installer les dépendances nécessaires
Ouvrez un terminal et installez les dépendances nécessaires :
```bash
pip install fastapi uvicorn requests
```

### Étape 2: Créer le fichier principal de l'application FastAPI
Créez un fichier nommé `main.py` et ajoutez le code suivant :

```python
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

app = FastAPI()

# Allow CORS for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NESSUS_URL = "https://localhost:8834"
USERNAME = "votre_nom_utilisateur"
PASSWORD = "votre_mot_de_passe"

def get_token():
    login_url = f"{NESSUS_URL}/session"
    payload = {"username": USERNAME, "password": PASSWORD}
    headers = {"Content-Type": "application/json"}
    response = requests.post(login_url, data=json.dumps(payload), headers=headers, verify=False)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to authenticate with Nessus")
    return response.json()['token']

@app.get("/launch_scan/{scan_id}")
def launch_scan(scan_id: int):
    token = get_token()
    scan_url = f"{NESSUS_URL}/scans/{scan_id}/launch"
    headers = {"X-Cookie": f"token={token}", "Content-Type": "application/json"}
    response = requests.post(scan_url, headers=headers, verify=False)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to launch scan")
    return response.json()

@app.get("/scan_results/{scan_id}")
def scan_results(scan_id: int):
    token = get_token()
    result_url = f"{NESSUS_URL}/scans/{scan_id}"
    headers = {"X-Cookie": f"token={token}", "Content-Type": "application/json"}
    response = requests.get(result_url, headers=headers, verify=False)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve scan results")
    return response.json()
```

### Étape 3: Démarrer l'application FastAPI
Dans le terminal, lancez l'application FastAPI en utilisant Uvicorn :
```bash
uvicorn main:app --reload
```

L'application sera disponible à l'adresse `http://127.0.0.1:8000`.

### Étape 4: Créer le frontend en React

#### Initialiser le projet React
Ouvrez un nouveau terminal et exécutez les commandes suivantes pour créer une nouvelle application React :
```bash
npx create-react-app nessus-frontend
cd nessus-frontend
```

#### Installer axios pour les requêtes HTTP
Dans le répertoire du projet React, installez `axios` :
```bash
npm install axios
```

#### Créer des composants React pour interagir avec l'API

##### Créez un composant pour lancer les scans
Dans le répertoire `src`, créez un fichier `LaunchScan.js` et ajoutez le code suivant :

```jsx
import React, { useState } from 'react';
import axios from 'axios';

const LaunchScan = () => {
  const [scanId, setScanId] = useState('');
  const [response, setResponse] = useState(null);

  const handleLaunchScan = async () => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/launch_scan/${scanId}`);
      setResponse(res.data);
    } catch (error) {
      console.error("Error launching scan", error);
    }
  };

  return (
    <div>
      <h2>Launch Scan</h2>
      <input 
        type="text" 
        value={scanId} 
        onChange={(e) => setScanId(e.target.value)} 
        placeholder="Enter Scan ID"
      />
      <button onClick={handleLaunchScan}>Launch Scan</button>
      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
};

export default LaunchScan;
```

##### Créez un composant pour afficher les résultats des scans
Dans le répertoire `src`, créez un fichier `ScanResults.js` et ajoutez le code suivant :

```jsx
import React, { useState } from 'react';
import axios from 'axios';

const ScanResults = () => {
  const [scanId, setScanId] = useState('');
  const [results, setResults] = useState(null);

  const handleGetResults = async () => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/scan_results/${scanId}`);
      setResults(res.data);
    } catch (error) {
      console.error("Error fetching scan results", error);
    }
  };

  return (
    <div>
      <h2>Scan Results</h2>
      <input 
        type="text" 
        value={scanId} 
        onChange={(e) => setScanId(e.target.value)} 
        placeholder="Enter Scan ID"
      />
      <button onClick={handleGetResults}>Get Results</button>
      {results && <pre>{JSON.stringify(results, null, 2)}</pre>}
    </div>
  );
};

export default ScanResults;
```

##### Modifier le composant App.js pour inclure les nouveaux composants
Ouvrez `src/App.js` et modifiez-le comme suit :

```jsx
import React from 'react';
import LaunchScan from './LaunchScan';
import ScanResults from './ScanResults';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Nessus Scan Automation</h1>
      <LaunchScan />
      <ScanResults />
    </div>
  );
}

export default App;
```

#### Démarrer l'application React
Dans le terminal, lancez l'application React :
```bash
npm start
```

L'application React sera disponible à l'adresse `http://localhost:3000`.

### Conclusion

Vous avez maintenant une application complète avec un backend FastAPI pour automatiser les scans Nessus et un frontend React pour interagir avec l'API et visualiser les résultats des scans. Cette solution permet de gérer et de surveiller facilement les scans de vulnérabilités Nessus à partir d'une interface web conviviale.
Assurez-vous de sécuriser votre API et votre application frontend pour une utilisation en production. Pensez également à utiliser des certificats SSL pour sécuriser les communications entre le frontend, le backend et Nessus.

# Annexe 1 :  Enviroonement virtuel
```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install virtualenv
python3 -m venv nom_env
source nom_env/bin/activate
```
```bash
 apt install python3.10-venv
```

# Anenxe 2 : Installer vscode

- https://phoenixnap.com/kb/install-vscode-ubuntu
