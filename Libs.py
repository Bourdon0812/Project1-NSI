# Retourne si le mot de passe est valide ou non
def isValid(mdp: str) -> bool:
    return True


# Retourne la raison de la non validité du mot de passe
def getNoValidReason(mdp: str) -> str:
    return "Pas de majuscule"


# Retourne si une chaine de caractere contient au moins 1 majuscule
def hasMajChar(string: str) -> bool:
    maj = ["A", "B", "C", "D"]
    return strContent(string, maj)


# Retourne si une chaine de caractere contient au moins 1 minuscule
def hasMinChar(string: str) -> bool:
    return True


# Retourne si une chaine de caracetre a minimum 8 charactere
def hasMinEightChar(string: str) -> bool:
    if len(string) >= 8:
        return True
    else:
        return False


# Retourne si une chaine de caractere contient au moins 1 caractere special ou un chiffre
def hasSpecialOrIntChar(string: str) -> bool:
    return True


# retourne si la chaine "string" contient au moins 1 fois un charactere present dans le tableau "array"
def strContent(string: str, array: list) -> bool:
    return True


# Retourne le niveau de sécuriter du mot de passe
def getMDPLevelSecurity(mdp: str) -> int:
    level = 0
    if hasMinEightChar(mdp):
        level = level + 1
    if hasMajChar(mdp):
        level = level + 1
    if hasMinChar(mdp):
        level = level + 1
    if hasSpecialOrIntChar(mdp):
        level = level + 1
    return level
