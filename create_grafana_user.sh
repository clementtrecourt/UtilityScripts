#!/bin/bash

# Couleurs pour la lisibilité
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Assistant création utilisateur Grafana via SSH ===${NC}"

# 1. Demande de la cible SSH
read -p "Cible SSH (nom dans .ssh/config, ex: icans-dfa) : " SSH_TARGET

# 2. Demande du mot de passe Admin (mode caché)
read -s -p "Mot de passe Admin (admin) : " ADMIN_PASS
echo ""

# 3. Demande des infos du nouvel utilisateur
read -p "Nouveau nom d'utilisateur (ex: bob) : " NEW_USER
read -s -p "Nouveau mot de passe pour $NEW_USER : " NEW_PASS
echo ""

echo -e "\n${GREEN}Connexion à $SSH_TARGET et création de l'utilisateur...${NC}"

# 4. Exécution via SSH
# L'astuce ici est d'utiliser 'bash -s' pour passer les variables comme arguments ($1, $2...)
# Cela évite que les caractères spéciaux ($ < >) ne cassent la commande SSH.

ssh -T "$SSH_TARGET" "bash -s" -- "$ADMIN_PASS" "$NEW_USER" "$NEW_PASS" <<'ENDSSH'
    # --- DÉBUT DU SCRIPT DISTANT ---
    ADMIN_P="$1"
    USER_N="$2"
    USER_P="$3"
    
    # URL API Grafana (Localhost car on est sur le serveur)
    URL="http://localhost:3000/api/admin/users"

    # Echappement des caractères pour le JSON (au cas où le mdp contient \ ou ")
    # On utilise sed pour échapper les backslashes et les double quotes
    SAFE_USER_P=$(echo "$USER_P" | sed 's/\\/\\\\/g' | sed 's/"/\\"/g')
    SAFE_USER_N=$(echo "$USER_N" | sed 's/\\/\\\\/g' | sed 's/"/\\"/g')

    # Construction du JSON
    # On génère l'email et le login automatiquement basé sur le nom
    JSON_DATA=$(cat <<EOF
{
  "name": "$SAFE_USER_N",
  "email": "$SAFE_USER_N@localhost",
  "login": "$SAFE_USER_N",
  "password": "$SAFE_USER_P"
}
EOF
)

    echo "Payload JSON généré. Envoi à l'API..."

    # Appel CURL
    # -s = silencieux, -S = affiche les erreurs, -f = fail on error
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" \
    -u "admin:$ADMIN_P" \
    -d "$JSON_DATA" \
    "$URL")

    if [ "$HTTP_CODE" -eq 200 ]; then
        echo "SUCCÈS : Utilisateur créé (Code 200)"
        exit 0
    elif [ "$HTTP_CODE" -eq 412 ] || [ "$HTTP_CODE" -eq 400 ]; then
         echo "ERREUR : L'utilisateur existe déjà ou données invalides (Code $HTTP_CODE)"
         exit 1
    elif [ "$HTTP_CODE" -eq 401 ]; then
         echo "ERREUR : Mot de passe Admin incorrect (Code 401)"
         exit 1
    else
         echo "ERREUR INCONNUE : Code retour $HTTP_CODE"
         exit 1
    fi
    # --- FIN DU SCRIPT DISTANT ---
ENDSSH

# Vérification du code de retour SSH
if [ $? -eq 0 ]; then
  echo -e "${GREEN}Opération terminée avec succès !${NC}"
else
  echo -e "${RED}Une erreur est survenue.${NC}"
fi
