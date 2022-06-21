awk '(NR>1)' BiDa_Uebung_9_friendship_table.tsv | sort -k3 -rn | awk '!seen[$1]++'

sed -e '1d' BiDa_Uebung_9_friendship_table.tsv | sort -k1,1 -k3,3,nr | awk'BEGIN{x=""}{if (x!= $1){print $0; x= $1}}