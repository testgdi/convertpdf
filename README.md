# convertpdf

These files convert a pdf of bills into tab-separated records.

This is for running on Mac OSX -- I found that png file produced by preview work better than those produced with sips.

This uses automator on the mac to
 1. separate the pdf into separate pages
 2. convert each page pdf into png,
 3. rotates the png.

The next step is to use tesseract to do OCR on each png to produce text files

The final step is to cat the text
files and run them through a python program to parse into expenditures
associated with vendors.

To run the scripts pull into a directory.
Put the bills pdf, call it bills-yyyymmdd.pdf in same directory. as run-month.sh

then on the command line do

. ./run-month.sh bills-yyyymmdd

You will need to rm the pdf's that get written to the ~/Desktop.  Also do rm -r output
so that the script can create a fresh directory with nothing in it.

There is a separate process to convert the summary page. Typically the summary page is the next to last page in the pdf. So

. ./run-summary.sh yyyymmdd pg vendor1

e.g.

. ./run-summary.sh 20160112 42 P.A.E.C
