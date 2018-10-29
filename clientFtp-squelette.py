##########################
# Import de librairie(s) #
##########################

# *** COMPLETER ICI ***

######################
# Paramètres globaux #
######################

# Pour la fonction getPortNumber()
# -- variable r = réponse du serveur
r=""
# -- variable i = compteur de caractères
i=0

# Paramètres de connexion

# *** COMPLETER ICI ***

#############
# Fonctions #
#############

# *** AMELIORATIONS POSSIBLES ***

def caractereSuivant() :
    global r
    global i

    i=i+1
    return(r[i])

def avanceJusque(d) :
    global r
    global i

    c=caractereSuivant()
    while (c != d) :
        c=caractereSuivant()

def enregistreJusque(d)
    global r
    global i

    p=''    
    c=caractereSuivant()
    while (c != d) :
        p=p+c
        c=caractereSuivant()
    return p
        
def getPortNumber() :
    global i
    global r
    
    avanceJusque(",")
    avanceJusque(",")
    avanceJusque(",")
    avanceJusque(",")

    p1=enregistreJusque(",")
    p2=enregistreJusque(")")

    numport=int(p1)*256+int(p2)

    return numport

###################
# Corps du script #
###################


# Etablissement de la connexion de contrôle avec le serveur

# *** COMPLETER ICI ***

# Connexion en tant qu'utilisateur anonyme

# *** COMPLETER ICI ***

# Passage en mode passif, extraction du numéro de port à employer

# *** COMPLETER ICI ***

# Etablissement de la connexion de données avec le serveur

# *** COMPLETER ICI ***

# Demande du fichier

# *** COMPLETER ICI ***

# Réception (réponses du serveur et données)

# *** COMPLETER ICI ***

# Fermeture de la connexion de contrôle (celle de données est fermée par le serveur à la fin du tranfert)

# *** COMPLETER ICI ***


