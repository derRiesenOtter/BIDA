mafft-qinsi nuclear_SSU_rRNA.fasta > MSA_nuclear_SSU_rRNA.fasta
mafft-qinsi plastid_SSU_rRNA.fasta > MSA_plastid_SSU_rRNA.fasta
echo "ENA|JABBYQ010000031.1" | gotree reroot outgroup -i Tree_MSA_plastid_SSU_rRNA.tree -l - > reroot_Tree_MSA_plastid_SSU_rRNA.tree
less reroot_Tree_MSA_plastid_SSU_rRNA.tree | gotree draw text -w 150
echo "ENA|CACVBZ020000051.1" | gotree reroot outgroup -i Tree_MSA_nuclear_SSU_rRNA.tree -l - > reroot_Tree_MSA_nuclear_SSU_rRNA.tree
less reroot_Tree_MSA_nuclear_SSU_rRNA.tree | gotree draw text -w 150