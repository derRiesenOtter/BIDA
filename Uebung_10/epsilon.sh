mafft-qinsi nuclear_SSU_rRNA.fasta > MSA_nuclear_SSU_rRNA.fasta
mafft-qinsi plastid_SSU_rRNA.fasta > MSA_plastid_SSU_rRNA.fasta
echo "ENA|JABBYQ010000031.1" | gotree reroot outgroup -i Tree_MSA_plastid_SSU_rRNA.tree -l - > reroot_Tree_MSA_plastid_SSU_rRNA.tree
#less reroot_Tree_MSA_plastid_SSU_rRNA.tree | gotree draw text -w 150
echo "ENA|AF081592.1" | gotree reroot outgroup -i Tree_MSA_nuclear_SSU_rRNA.tree -l - > reroot_Tree_MSA_nuclear_SSU_rRNA.tree
#less reroot_Tree_MSA_nuclear_SSU_rRNA.tree | gotree draw text -w 150
less reroot_Tree_MSA_nuclear_SSU_rRNA.tree | sed -e 's/ENA|ICRL01000007.1/Hap/' | sed -e 's/ENA|MT760788.1/Gla/' | sed -e 's/ENA|X57162.1/Cry/' | sed -e 's/ENA|AF081592.1/Eug/' | sed -e 's/ENA|CP006628.1/Chl/' | sed -e 's/ENA|AF022195.1/Din/' | sed -e 's/ENA|KX431455.1/STR/' | sed -e 's/ENA|Z14140.1/Rho/' | sed -e 's/ENA|CACVBZ020000051.1/Vir/' | gotree draw text -w 150
less reroot_Tree_MSA_plastid_SSU_rRNA.tree | sed -e 's/ENA|KT428890.1/Cry/' | sed -e 's/ENA|JN674636.2/Eug/' | sed -e 's/ENA|AB027236.1/Din/' | sed -e 's/ENA|KF438023.1/Chl/' | sed -e 's/ENA|VLTL01000396.1/Str/' | sed -e 's/ENA|MT471325.1/Hap/' | sed -e 's/ENA|Z29521.1/Rho/' | sed -e 's/ENA|LR761918.1/Vir/' | sed -e 's/ENA|MG601102.1/Gla/' | sed -e 's/ENA|JABBYQ010000031.1/Cya/' | gotree draw text -w 150

#cut -d  ';' -f 2,11 alpha_Algen.csv | sed -e '1,2' -e 's/https.*fasta\///' -e 's/:.*//'| awk -f ';' '{print "\"s/" $2 "\t" $2}'
