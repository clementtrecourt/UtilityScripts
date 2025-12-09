👋 Bienvenue dans helpfull-scripts! 🛠️

Ceci est une collection organisée de scripts divers et utiles conçus pour automatiser les tâches quotidiennes, rationaliser la configuration et vous rendre la vie un peu plus facile. Pensez-y comme à votre couteau suisse numérique ! 🔪
🚀 Scripts dans ce Dépôt
Fichier	Langage	Objectif	Emojis
confluence_get.py	Python	Récupérateur de Données Confluence : Un script puissant pour interagir avec l'API Confluence, parfait pour récupérer, exporter ou sauvegarder des pages, des pièces jointes ou des données spécifiques de votre instance Confluence. 📄➡️💾	🐍 Atlassian
create_grafana_user.sh	Shell	Provisionneur d'Utilisateurs Grafana : Automatise la création de nouveaux utilisateurs sur votre serveur Grafana. Un gain de temps pour l'intégration ou les configurations d'infrastructure-as-code ! 👤✨	🐚 Grafana
sav-creator.py	Python	Créateur de Données Personnalisées : Un utilitaire pour générer ou manipuler des fichiers .sav (souvent utilisés pour les sauvegardes de données ou des configurations système spécifiques). Utilisez-le pour configurer rapidement des données de sauvegarde de base. 📝🧱	🔧💾
⚙️ Démarrage Rapide

    Cloner le Dépôt :
    code Bash

    
git clone https://github.com/clementtrecourt/helpfull-scripts.git
cd helpfull-scripts

  

Prérequis :

    Scripts Python (.py) : Assurez-vous d'avoir Python 3 installé. Vous pourriez avoir besoin d'installer des bibliothèques spécifiques (par exemple, requests pour les appels d'API). Vérifiez les entêtes des scripts pour les dépendances !

    Scripts Shell (.sh) : Assurez-vous simplement que le script dispose des permissions d'exécution :
    code Bash

        
    chmod +x create_grafana_user.sh

      

Exécuter un Script :
code Bash

        
    # Exemple pour le script Grafana
    ./create_grafana_user.sh --username "new-dev" --email "dev@example.com"

    # Exemple pour le script Confluence
    python confluence_get.py --page-id 12345 --output-format markdown

      

🌟 Contributions

Vous avez un petit script utile qui vous fait gagner du temps ? Nous serions ravis de le voir !

    Forkez le dépôt.

    Créez votre branche de fonctionnalité (git checkout -b feature/ScriptGenial).

    Commitez vos modifications (git commit -m 'Ajout d'un script génial pour X').

    Poussez vers la branche (git push origin feature/ScriptGenial).

    Ouvrez une demande de tirage (Pull Request) ! 🎉

Joyeux Scripting ! 🧑‍💻✨
