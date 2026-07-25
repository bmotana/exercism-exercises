
PROTEINS = {
    "Methionine": ["AUG"],
	"Phenylalanine" : ["UUU","UUC"],
	"Leucine": ["UUA","UUG"],
	"Serine": ["UCU", "UCC","UCA","UCG"],
	"Tyrosine": ["UAU", "UAC"],
	"Cysteine": ["UGU", "UGC"],
	"Tryptophan": ["UGG"],
	"STOP": ["UAA", "UAG", "UGA"]
}

def proteins(strand: str) -> list:
    """
    Returns a protein list from a strand of RNA's
    
    Args:
        strand (str): RNA strand
        
    Returns:
        list: list of amino acids
    """
    strand_length = len(strand)
    condons = [strand[i:i+3]for i in range(0,strand_length,3)]
    protein_list = []
    for condon in condons:
        for protein in PROTEINS.keys():
            if condon in PROTEINS["STOP"]:
                return protein_list
            if condon in PROTEINS[protein]:
                protein_list.append(protein)
    return protein_list
