➤ cat clean.py 
import os
import sys
import requests

# --- CONFIGURATION ---
BASE_URL = os.environ.get('CONF_URL', 'https://axepartner.atlassian.net')
# ID de départ
ROOT_ID = os.environ.get('CONF_PARENT_ID', '3040804941') 
EMAIL = os.environ.get('CONF_EMAIL', 'ctrecourt@axeesante.com')
TOKEN = os.environ.get('CONF_TOKEN')

OUTPUT_FILE = "arborescence_confluence.txt"
AUTH = (EMAIL, TOKEN)

def log(text, file_obj):
    """Affiche à l'écran ET écrit dans le fichier"""
    print(text)
    file_obj.write(text + "\n")

def get_page_info(page_id):
    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}"
    try:
        r = requests.get(url, auth=AUTH)
        if r.status_code == 200:
            return r.json().get('title', 'Inconnu')
    except:
        pass
    return "Erreur récupération"

def get_child_pages(parent_id):
    all_results = []
    start = 0
    limit = 100
    while True:
        url = f"{BASE_URL}/wiki/rest/api/content/{parent_id}/child/page"
        params = {'limit': limit, 'start': start}
        try:
            r = requests.get(url, auth=AUTH, params=params)
            if r.status_code != 200: break
            data = r.json()
            results = data.get('results', [])
            if not results: break
            all_results.extend(results)
            if len(results) < limit: break
            start += limit
        except:
            break
    return all_results

def print_node(title, page_id, prefix, is_last, file_obj):
    connector = "└── " if is_last else "├── "
    line = f"{prefix}{connector}[{page_id}] {title}"
    log(line, file_obj)

def print_tree_recursive(parent_id, prefix, is_parent_last, file_obj):
    children = get_child_pages(parent_id)
    count = len(children)
    
    new_prefix = prefix + ("    " if is_parent_last else "│   ")
    
    for i, child in enumerate(children):
        is_last = (i == count - 1)
        print_node(child['title'], child['id'], new_prefix, is_last, file_obj)
        
        # Récursion
        print_tree_recursive(child['id'], new_prefix, is_last, file_obj)

def main():
    if not TOKEN:
        print("Erreur: Token manquant")
        sys.exit(1)

    print(f"🌳 Génération de l'arborescence vers : {OUTPUT_FILE} ...")
    
    # On ouvre le fichier une seule fois au début
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        
        # Racine
        root_title = get_page_info(ROOT_ID)
        header = f"📂 {root_title} (ID: {ROOT_ID})"
        log(header, f)
        
        # Arbre
        print_tree_recursive(ROOT_ID, "", True, f)
    
    print(f"\n✅ Terminé. Ouvrez le fichier '{OUTPUT_FILE}' pour voir le résultat.")

if __name__ == "__main__":
    main()⏎     
