pdf_file_base=$1
python_file=$2 #../convert.py
rm ~/Desktop/*.pdf
mkdir output
automator -v -i $pdf_file_base.pdf pdf2png.workflow
cd output
num=`ls *.png | wc -l`
for i in $(seq 1 $num); do tesseract -psm 6 $pdf_file_base-page$i.png $pdf_file_base-$i nolower; done
for i in $(seq 1 $num); do cat $pdf_file_base-$i.txt >> $pdf_file_base.txt; done
python $python_file $pdf_file_base.txt > $pdf_file_base.tsv
