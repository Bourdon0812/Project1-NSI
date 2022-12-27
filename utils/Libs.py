# Retourne si le mot de passe est valide ou non
def isValid(mdp: str) -> bool:
    return hasMajChar(mdp) and hasMinChar(mdp) and hasMinEightChar(mdp) and hasSpecialOrIntChar(mdp)


# Retourne la raison de la non validité du mot de passe
def getNoValidReason(mdp: str) -> str:
    reason = ""
    if not hasMajChar(mdp):
        reason += "- Votre mot de passe ne contient pas de caractere Majuscule \n"
    if not hasMinChar(mdp):
        reason += "- Votre mot de passe ne contient pas de caractere Minuscule \n"
    if not hasMinEightChar(mdp):
        reason += "- Votre mot de passe ne contient pas au moins 8 caracteres \n"
    if not hasSpecialOrIntChar(mdp):
        reason += "- Votre mot de passe ne contient pas de chiffre ou de caractere special \n"
    return reason


# Retourne si une chaine de caractere contient au moins 1 majuscule
def hasMajChar(string: str) -> bool:
    maj: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return strContent(string, maj)


# Retourne si une chaine de caractere contient au moins 1 minuscule
def hasMinChar(string: str) -> bool:
    min: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return strContent(string, min)


# Retourne si une chaine de caracetre a minimum 8 charactere
def hasMinEightChar(string: str) -> bool:
    return len(string) >= 8


# Retourne si une chaine de caractere contient au moins 1 caractere special ou un chiffre
def hasSpecialOrIntChar(string: str) -> bool:
    special: list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    ints: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return strContent(string, special) or strContent(string, ints)


# retourne si la chaine "string" contient au moins 1 fois un charactere present dans le tableau "array"
def strContent(string: str, array: list) -> bool:
    for i in string:
        if i in array:
            return True
    return False


# Retourne le niveau de sécuriter du mot de passe
def getMDPLevelSecurity(mdp: str) -> int:
    level: int = 0
    if hasMinEightChar(mdp):
        level = level + 1
    if hasMajChar(mdp):
        level = level + 1
    if hasMinChar(mdp):
        level = level + 1
    if hasSpecialOrIntChar(mdp):
        level = level + 1
    return level