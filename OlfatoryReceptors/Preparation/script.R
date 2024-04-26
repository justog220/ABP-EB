library(ggmsa)
protein_sequences <- system.file("extdata", "olfatoys_alignment.fa", package = "ggmsa")
ggmsa(protein_sequences, start = 221, end = 280, char_width = 0.5, seq_name = T) + geom_seqlogo() + geom_msaBar()