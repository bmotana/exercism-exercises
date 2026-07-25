def to_rna(dna_strand: str) -> str:
    """
    Transcribes a DNA strand into its RNA counterpart.

    Args:
        dna_strand (str): The DNA strand to be transcribed.

    Returns:
        str: The RNA transcript of the input DNA strand.
    """
    # Define the translation table for DNA to RNA conversion
    dna_to_rna_translation_table = str.maketrans("GCTA", "CGAU")
    # Use the translation table to convert DNA to RNA
    rna_transcript = dna_strand.translate(dna_to_rna_translation_table)
    
    return rna_transcript