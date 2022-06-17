awk '(NR>1)' BiDa_Uebung_9_friendship_table.tsv | sort -k3 -rn | awk '!seen[$1]++'
