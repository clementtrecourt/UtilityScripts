# ====== Couleurs ANSI ======
BLEU = "\033[94m"
VERT = "\033[92m"
JAUNE = "\033[93m"
ROUGE = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ====== Texte modèle ======
modele = f"""
Bonjour,

Demande de prise en compte d'une intervention technique

Nom du client : {{nom_client}}

Référence Axe du dispositif : {{ref_axe}}

Référence du matériel impacté : {{ref_materiel}}

Symptôme : {{symptome}}

Adresse postale : {{adresse}}

Coordonnées du contact sur place :
Nom : {{contact_nom}}
Téléphone : {{contact_tel}}
Email : {{contact_email}}

Créneau préférentiel pour intervention : {{creneau}}

Demande d'intervention :
{{demande}}

Cordialement,
"""

# ====== Fonction pour poser une question colorée ======
def ask(question):
    return input(f"{CYAN}{BOLD}{question}{RESET} ")

# ====== Programme ======
print(f"{BLEU}{BOLD}\n==============================")
print(" FORMULAIRE DE DEMANDE D'INTERVENTION ")
print("==============================\n" + RESET)

nom_client = ask("Nom du client :")
ref_axe = ask("Référence Axe du dispositif :")
ref_materiel = ask("Référence du matériel impacté :")
symptome = ask("Symptôme :")
adresse = ask("Adresse postale :")

print(f"\n{JAUNE}{BOLD}--- Coordonnées du contact sur place ---{RESET}")
contact_nom = ask("Nom du contact :")
contact_tel = ask("Téléphone :")
contact_email = ask("Email :")

creneau = ask("Créneau préférentiel pour intervention :")
demande = ask("Demande d'intervention :")

# ====== Remplissage du texte ======
texte_final = modele.format(
    nom_client=nom_client,
    ref_axe=ref_axe,
    ref_materiel=ref_materiel,
    symptome=symptome,
    adresse=adresse,
    contact_nom=contact_nom,
    contact_tel=contact_tel,
    contact_email=contact_email,
    creneau=creneau,
    demande=demande
)

# ====== Affichage final ======
print(f"\n{VERT}{BOLD}===== TEXTE GÉNÉRÉ ====={RESET}\n")
print(texte_final)
print(f"{VERT}{BOLD}========================{RESET}")

