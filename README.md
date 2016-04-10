# convertpdf
These files convert a pdf of bills into tab-separated records.
This is for running on Mac OSX -- I found that png file produced by preview work better than those produced with sips.
So this uses automator on the mac to 1. separate the pdf into separate pages, 2. convert each page pdf into png,
3. rotates the png.
The next step is to use tesseract to do OCR on each png to produce text files
THe final step is to cat the text files and run them through a python program to parse into expenditures
associated with vendors.
