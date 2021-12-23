#py /e/NON_AMP_ANALYSIS/Python_scripts/001_combxls_2_ampresults.py g000001.xlsx
#cat DDD_excel_files/g0000??_ampdRn_results.csv | grep -v Cycle_ > g01to73_ampdRn_results.csv1
#Place one title row on the top of the file g01to73_ampdRn_results.csv
#head -1 DDD_excel_files/g000073_ampdRn_results.csv > t1.del
#cat header.txt g01to73_ampdRn_results.csv1 > g01to73_ampdRn_results.csv
#py /e/NON_AMP_ANALYSIS/Python_scripts/002_ampresults_2_pattseq.py g01to73_ampdRn_results.csv cID_ &

tail -2 $1_g01to73_ampdRn_results.csv > $1_extreme.csv
grep -v LowestValue $1_g01to73_ampdRn_results.csv | grep -v HighestValue > g01to73_$1_ampdRn.csv1
grep -v -f $1_extreme.csv g01to73_$1_ampdRn.csv1 > g01to73_$1_ampdRn.csv2
cat $1_extreme.csv g01to73_$1_ampdRn.csv2 > g01to73_$1_ampdRn.csv3
sed 's/\[//' g01to73_$1_ampdRn.csv3 | sed 's/\]//' > g01to73_$1_ampdRn.csv4
mv g01to73_$1_ampdRn.csv4 g01to73_$1_ampdRn.csv
#mv $1_ampdRn_results.csv1 $1_ampdRn_results.csv
