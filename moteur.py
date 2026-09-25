#Moteur de Combat Occitanie
def initialiser_arena(nom: str):
    return {"nom": nom, "combattans" : []}

print("moteur de jeux charge.")
print("systeme pret.")

def attaque_charge():
    return "Charge inflige 20 degats"

def attaque_griffe():
    return "Griffe inflige 25 degats"

def boire_potion(points: int =30):
    return f"Soin de {points} PV"

def determiner_initiative(vitesse_a: int, vitesse_b: int) -> str:
    if vitesse_a >= vitesse_b:
        return "combattant_a"
    return "combattant_b"