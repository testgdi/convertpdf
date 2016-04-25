dt=$1 #20160112
pg=$2 # 42
first=$3 #P.A.E.C
tesseract -psm 6 output-$dt/bills-$dt-page$pg.png summary-$dt  onlyupperkeypad
python convert-summary.py summary-$dt.txt "$first" > summary-$dt.tsv

