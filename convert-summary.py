import sys

if len( sys.argv) != 3:
    print "usage: python " + sys.argv[0] + ' infile "vendor1"'
    print "eg: " + "python " + sys.argv[0] + \
          ' summary-20160412-ouk.txt "P.A.E.C."'
    sys.exit(1)
    
fn = sys.argv[1]
# fn="summary-20160412-ouk.txt"

lines=[]
f=open(fn)
f.next()
f.next()
top1= sys.argv[2] # "P.A.E.C."
# top2= sys.argv[3] # "EDUCATION OPERATION MAINTENANCE"

start=False
for line in f:
    if line.strip().count( top1) < 1:
        start = True
    if not start:
        continue
    if line.strip() == '':
        continue
    lines.append( line.strip())

# print lines[:10]

clean_lines=[x.split("  ") for x in lines]

table_lines=[]
for line in clean_lines:
    while line.count('') > 0:
        line.remove('')
    table_lines.append( line)
    
vendor_name=[x[0].strip() for x in table_lines]
description=[x[1].strip() for x in table_lines]
amount=[x[2].strip() for x in table_lines]

# print vendor_name[:5]
# print description[:5]
# print amount[:5]

# print vendor_name[-5:]
# print description[-5:]
# print amount[-5:]

def clean_money(s):
    s=s[1:]
    s=s.replace(" ","").replace(",","").replace(".","")
    return s[:-2]+"."+s[-2:]
    
amount_clean=[ clean_money(x) for x in amount]

if len(vendor_name) != len(description):
    print "len(vendor_name) != len(description)"
    sys.exit(1)
if len(vendor_name) != len(amount_clean):
    print "len(vendor_name) != len(amount_clean)"
    sys.exit(1)

for i in range( len( vendor_name)):
    print "\t".join( [vendor_name[i],description[i],amount_clean[i]])
