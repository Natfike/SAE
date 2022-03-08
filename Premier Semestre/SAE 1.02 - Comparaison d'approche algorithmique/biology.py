def est_base(c):
    if c != "A" and c != "T" and c != "G" and c != "C" :
        return False
    else :
        return True


def est_adn(s):
    i = 0
    while i < len(s) :
        if not est_base(s[i]) :
            return False
        i += 1
    return True


def arn(adn):
    if not est_adn(adn) :
        return None
    i = 0
    arn = ""
    while i < len(adn) :
        if adn[i] == "T" :
            arn += "U"
        else :
            arn += adn[i]
        i += 1
    return arn


def arn_to_codons(arn):
    i = 0
    nb = len(arn) - len(arn)%3
    codon = []
    while i < nb :
        codon.append(arn[i] + arn[i+1] + arn[i+2])
        i += 3
    return codon



from json import *
def load_dico_codons_aa(filename):
    #penser à import json avant le def
    fichier = open (filename, "r")
    strjson = fichier.read()
    dico = loads(strjson)
    fichier.close()
    return dico


def codons_stop(dico):
    dico_stop = []
    tab_lettre = ["U","C","A","G"]
    i = 0
    while i < 4 :
        First = tab_lettre[i]
        j = 0
        while j < 4 :
            Second = tab_lettre[j]
            k = 0
            while k < 4 :
                Third = tab_lettre[k]
                codon = First + Second + Third
                if codon not in dico :
                    dico_stop.append(codon)
                k += 1
            j += 1
        i += 1
    return dico_stop


def codons_to_aa(codons, dico):
    tab_stop = codons_stop(dico)
    tab_aa = []
    i = 0
    while i < len(codons):
        if codons[i] in tab_stop :
            return tab_aa
        else : 
            tab_aa.append(dico[codons[i]])
        i += 1
    return tab_aa




def nextIndice(tab, ind, elements):
    def nextIndice(tab,ind,elements):
    while ind < len(tab):
        i = 0
        while i < len(elements):
            if tab[ind] == elements[i] :
                return ind
            else :
                i += 1
        ind += 1
    return len(tab)


def decoupe_sequence(seq, start, stop):
    tab_morc = []
    morc = []
    enregistrement = False
    i = 0
    while i < len(seq):
        if seq[i] in start and enregistrement == False :
            enregistrement = True
        elif seq[i] in stop :
            enregistrement = False
            if morc != [] :
                tab_morc.append(morc)
                morc = []
        else :
            if enregistrement == True :
                morc.append(seq[i])
        i += 1
    return tab_morc


def codons_to_seq_codantes(codons, dico):
    def codons_to_seq_codantes(tab_cod, dico):
    stop = codons_stop(dico)
    start = ["AUG"]
    seq = decoupe_sequence(tab_cod,start,stop)
    if seq != [] :
        return seq
    else :
        return "Séquence vide"


def seq_codantes_to_seq_aas(seq_codantes, dico):
    def seq_codantes_to_seq_aas(tab_seq,dico):
    tab_seq_aa = []
    i = 0
    while i < len(tab_seq) :
        j = 0
        seq_aa = []
        while j < len(tab_seq[i]):
            seq_aa.append(dico[tab_seq[i][j]])
            j += 1
        tab_seq_aa.append(seq_aa)
        i += 1
    return tab_seq_aa


def adn_encode_molecule(adn, dico, molecule):
    def adn_encode_molecule(adn,dico,molécule):
    if not est_adn(adn):
        return "Ceci n'est pas un brin d'adn valide"
    stop = codons_stop(dico)
    start = ["AUG"]
    
    Arn = arn(adn)
    codons = arn_to_codons(Arn)
    seq_codante = codons_to_seq_codantes(codons,dico)
    seq_aas = seq_codantes_to_seq_aas(seq_codante,dico)
    if molécule in seq_aas :
        return True
    else:
        return False
