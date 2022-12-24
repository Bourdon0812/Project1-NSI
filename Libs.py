# Retourne si le mot de passe est valide ou non
def isValid(mdp: str) -> bool:
    return True


# Retourne la raison de la non validité du mot de passe
def getNoValidReason(mdp: str) -> str:
    return "Pas de majuscule"


# Retourne si une chaine de caractere contient au moins 1 majuscule
def hasMajChar(string: str) -> bool:
    return True


# Retourne si une chaine de caractere contient au moins 1 minuscule
def hasMinCar(string: str) -> bool:
    return True


# Retourne si une chaine de caracetre a minimum 8 charactere
def hasMinEightChar(string: str) -> bool:
    return True


# Retourne si une chaine de caractere contient au moins 1 caractere special ou un chiffre
def hasSpecialOrIntChar(string: str) -> bool:
    return True


# retourne si la chaine "string" contient au moins 1 fois le caractere "char"
def strContent(string: str, char: str) -> bool:
    return True


# Retourne le niveau de sécuriter du mot de passe
def getMDPLevelSecurity(mdp: str) -> int:
    return 0