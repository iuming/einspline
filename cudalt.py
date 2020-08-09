#!/usr/bin/python
# libtoolish hack
import sys
import os
out_lo = sys.argv[1]
out_o = out_lo.replace(".lo", ".o")

try:
    i = out_o.rindex("/")
    dir = out_o[0:i+1] + ".libs/"
    out_l = ".libs/" + out_o[i+1:]
    out_o = out_o[0:i+1] + ".libs/" + out_o[i+1:]
    
except ValueError:
    dir = ".libs/"
    out_o = ".libs/" + out_o
    out_l = out_o

#print out_o

# Make lib dir
try:
    os.mkdir(dir)
except OSError:
    pass

args = sys.argv[2:]
args.extend(["-Xcompiler","-fPIC"]) # position indep code
args.append("-o")
args.append(out_o)

rv = os.system(" ".join(args))
if rv != 0:
    #print "******** RV is ", rv
    sys.exit(1)

f = open(out_lo, "w")
f.write("# multi_bspline_cuda_c.lo - a libtool object file\n")
f.write("# Generated by ltmain.sh - GNU libtool 1.5.22 Debian 1.5.22-4 (1.1220.2.365 2005/12/18 22:14:06)\n")

f.write("pic_object='" + out_l + "'")
f.close()

sys.exit(0)
