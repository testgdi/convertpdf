import sys
fn = sys.argv[1]
# fn="output/bills-20150811.txt"
lines=[]

for line in open(fn):
    if len(line.strip()) ==0:
        continue 
    if line.count( 'PAYABLES')>0:
        continue 
    if line.count( 'VENDOR')>0:
        continue 
    if line.count( 'INVOICE')>0:
        continue 
    if line.count( 'PAY DATE')>0:
        continue 
        
    lines.append( line.strip())

class Rec():
    def __init__(self, n, add, x, s):
        self.name = n
        self.address = add
        self.exp = x
        self.sub = s

    def clean(self, s):
        s = s.replace('$',''). \
                  replace(',','').replace('.',''). \
                  replace('-','')
        s = s[:-2] + '.' + s[-2:]
        if s[0] == '0':
            s = '8'+s[1:]
        return s

    def check_subtotal(self):
        s = self.sub
        s = self.clean(s)
        
        
    def printme(self):
        name = self.name
        exp_list = self.exp
        
        for exp in exp_list:
            exp_amt = exp.split()[-1]
            exp_amt = self.clean(exp_amt)
            
            exp_amt = exp_amt.replace('$',''). \
                      replace(',','').replace('.',''). \
                      replace('-','')
            exp_amt = exp_amt[:-2] + '.' + exp_amt[-2:]
            outstr = "\t".join( [name, exp, exp_amt])
            print outstr
        
## go through find name and subtotal
## name
## add1
## add2
## ...
## addn
## EXP
## ...
## EXP
## SUB-TOTAL
next_line_is_start=True
subtotal_list=[]
exp_list=[]
add_list=[]

def probably_subtotal(line):
    matchme="SUB-TOTAL"
    min_length= min( len(matchme), len( line))
    matches = [line[i] == matchme[i] for i in range( min_length)]
    count_su = line.count("SU")
    count_total = line.count("TOTAL")
    return sum( matches) > 5 or (count_su>0 and count_total>0)
    
for line in lines:
    if next_line_is_start:
        start = line
        next_line_is_start=False
        continue

    if line[:4] != 'EXP ' and not probably_subtotal(line[:9]):
        add_list.append( line)

    if line[:4] == 'EXP ':
        exp_list.append( line)

    if probably_subtotal(line.split()[0]):
        sub = line.split()[1]
        if sub == "'":
            sub = line.split()[2]
        if sub[0] == 0:
            sub[0] = 8
        ## if first character is a 0, then it proabably should be 8.
        sub = float(sub.replace('$','').replace(',','').replace('.','').replace("C","0").replace("_",""))
        sub /= 100.0
        next_line_is_start=True
        subtotal_list.append( Rec( start, add_list, exp_list, sub))
        add_list=[]
        exp_list=[]
        
print "\t".join(["name", "expenditure", "amt"])
for x in subtotal_list:
    x.printme()
