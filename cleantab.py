import sys
import re

filename = raw_input("Tabanalys file:")
outputfile = raw_input("Output file:")
f = open(filename,'r')
o = open(outputfile,'w')
linenum = 1
o.write('\"Tables\",\"Records\",\"Size(bytes)\",\"Record Size Min\",\"Record Size Max\",\"Record Size Mean\",\"Fragment Count\",\"Fragment Factor\",\"Scatter Factor\"')
for line in f:
        if (line.find("PUB") == -1 and linenum > 0):
            linenum = linenum + 1 
            line =''
            if (linenum > 200):
                print "Doesn't seem to be a tabanalys"
                break
        elif (line.find("-------") != -1 and linenum == -1): #end of table data
                break       
        else:
            linenum = -1
            #My RegEx Foo is weak:
            line = re.sub(r'([\s*]{1,25})',',',line.rstrip()) #strip spaces and replace with commas
            line = re.sub(r',,',',',line.rstrip()) #strip double commas
            line = re.sub(r'PUB\.','\nPUB.',line.rstrip()) #insert newlines before PUBs
            line = re.sub(r'(?P<nm>[0-9])(?P<dot>[\.])(?P<nx>[0-9])(?P<sz>[BKMG])','\g<nm>\g<nx>\g<sz>',line.rstrip()) #strip decimals from values, but NOT tables
            line = re.sub(r'(?P<nb>[0-9])B','',line.rstrip()) # strip B's
            line = re.sub(r'(?P<nk>[0-9])K','\g<nk>00',line.rstrip()) #strip K's and add 00 (250.4K becomes 250400 and so on...)
            line = re.sub(r'(?P<nM>[0-9])M','\g<nM>00000',line.rstrip()) #strip M's and add 00000
            line = re.sub(r'(?P<nG>[0-9])G','\g<nG>00000000',line.rstrip()) #strip G's and add 00000000
            sys.stdout.write(line)
            o.write(line)   
o.close()
