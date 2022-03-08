import biology.py as bio


def test_est_base():
    assert bio.est_base("A")
    assert bio.est_base("G")
    assert bio.est_base("C")
    assert bio.est_base("T")
    assert not bio.est_base("t")
    assert not bio.est_base("&")
    assert not bio.est_base("a")
    assert not bio.est_base("c")
    assert not bio.est_base("g")
    print("Test ok !")
    

def test_est_adn():
    assert bio.est_adn("ATGTCAAA")
    assert not bio.est_adn("ATBOA ATG")
    assert not bio.est_adn("ATGtCAAA")
    assert bio.est_adn("ATTGGCCCAAAATTTCGG")
    print("Test ok !")
    
def test_arn():
    assert bio.arn("ATGTCAAA") == "AUGUCAAA"
    assert not bio.arn("ATGTATCC") == "ATGTATCC"
    assert bio.arn("ATBOAATG") == None
    print("Test ok !")
    
def test_arn_to_codons():
    assert bio.arn_to_codons("CGUAAUGCCCUU") == ['CGU', 'AAU', 'GCC', 'CUU']
    assert bio.arn_to_codons("CGUAAUGCCCU") == ['CGU', 'AAU', 'GCC']
    assert bio.arn_to_codons("CGUCGUCGUC") == ['CGU', 'CGU', 'CGU']
    print("Test ok !")
    
def test_codons_stop():
    assert bio.codons_stop(bio.load_dico_codons_aa("./data/codons_aa.json")) == ['UAA', 'UAG', 'AGA', 'AGG']
    assert not bio.codons_stop(bio.load_dico_codons_aa("./data/codons_aa.json")) == ['UUU']
    print("Test ok !")
    
def test_codons_to_aa():
    dico = load_dico_codons_aa("./data/codons_aa.json")
    assert bio.codons_to_aa( ['CGU', 'CGG', 'UUU', 'CUU'],dico)== ['Arginine', 'Arginine', 'Phenylalanine', 'Leucine']
    assert bio.codons_to_aa(['CGU', 'CGG', 'UAA', 'CUU'],dico) == ['Arginine', 'Arginine']
    assert bio.codons_to_aa(['UAA', 'UUU', 'UUU', 'UUU', 'UUU', 'UUU', 'UUU'],dico) == []
    print("Test ok !")


def test_nextIndice():
    tab = ["bonjour", "hello", "buongiorno", "ciao", "bye"]
    elements = ["hello", "bye"]
    assert nextIndice(tab,0,elements) == 1
    assert nextIndice(tab,1,elements) == 1
    assert nextIndice(tab,2,elements) == 4
    assert nextIndice(tab,3,elements) == 4
    assert nextIndice(tab,4,elements) == 4
    assert nextIndice(tab,5,elements) == 5
    print("Test ok !")



def test_decoupe_sequence():
    seq = ["val1", "début", "val2", "val3", "end", "val4", "fin", "begin", "val5", "fin", "val6"]
    start = ["début", "begin"]
    stop = ["fin", "end"]
    assert decoupe_sequence(seq,start,stop) == [['val2','val3'],["val5"]]
    print("Test ok !")


def test_codons_to_seq_codantes():
    tab_cod = ["CGU", "UUU", "AUG","CGU", "AUG","AAU", "UAA", "AUG","GGG", "CCC",  "CGU", "UAG", "GGG"]
    dico = load_dico_codons_aa("./data/codons_aa.json")
    assert codons_to_seq_codantes(tab_cod,dico) == [["CGU","AUG","AAU"],["GGG","CCC","CGU"]]
    print("Test ok !")

def test_seq_codantes_to_seq_aas():
    dico = load_dico_codons_aa("./data/codons_aa.json")
    tab_seq = [["CGU","AUG","AAU"],["GGG","CCC","CGU"]]
    assert seq_codantes_to_seq_aas(tab_seq,dico) == [['Arginine','Methionine','Asparagine'],['Glycine','Proline','Arginine']]
    print("Test ok !")

def test_adn_encode_molecule():
    adn = "CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG"
    molécule = ["Glycine", "Proline", "Arginine"]
    dico = load_dico_codons_aa("./data/codons_aa.json")
    assert adn_encode_molecule(adn,dico,molécule)
    print("Test ok !")