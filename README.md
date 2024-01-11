# API pour test.immo
## Description
Ce document présente des requêtes Python pour interagir avec une base de données locale. Ces requêtes sont associées aux tables de la base de données et fournissent les résultats pour les 12 scénarios utilisateurs.

### Contenu des fichiers
- README.md : Ce document que vous lisez actuellement.
- Brief03API.py : Fichier Python contenant :
  - Description des requêtes Python connectées à la base de données.
  - Tables associées aux requêtes SQL.
  - Résultats pour les 12 scénarios utilisateurs.

### Prérequis
## Installation nécessaire :

- Un environnement Python (par exemple, VSCode) pour exécuter le fichier Brief03API.py.
- Pour installer les dépendances, exécutez la commande pip install uvicorn.

### Exécution du code :
1. Assurez-vous d'avoir un visualiseur de code installé, tel que VSCode.
2. Exécutez le code Brief03API.py dans un terminal prenant en charge Python.
3. Vérifiez dans le terminal que le serveur fonctionne correctement. Lorsque vous exécutez le code, vérifiez que le message suivant s'affiche : "amina@FOND-1101:~/api.test.immo$ /bin/python3 /home/amina/api.test.immo/Brief03API.py INFO: Started server process [1604] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://127.0.0.1:8002 (Press CTRL+C to quit)"
4. Ouvrez l'URL suivante dans votre navigateur : [http://127.0.0.1:8002/docs#/](http://127.0.0.1:8002/docs#/). Assurez-vous de ne pas confondre cette URL avec [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/).
5. Vous pouvez désormais utiliser l'API et soumettre les valeurs souhaitées pour les User Stories disponibles.

### Données
Les données exploitées ici proviennent de deux tables : transaction_sample et loyer, utilisées grâce à des requêtes SQL spécifiques à chaque scénario utilisateur. Veuillez les installer en amont afin que les requêtes SQL puissent fonctionner...

### Notes
Dans certains cas, des requêtes de maisons ont été modifiées en requêtes d'appartements pour illustrer le fonctionnement des exports. Enjoy!
