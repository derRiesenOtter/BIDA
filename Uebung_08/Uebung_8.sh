cut -d ';' -f11 alpha_Algen.csv | xargs wget -O tmp.fasta

cut -d ';' -f11 alpha_Algen.csv | head -2

cut -d ';' -f11 alpha_Algen.csv | sed -e '1,2d'
