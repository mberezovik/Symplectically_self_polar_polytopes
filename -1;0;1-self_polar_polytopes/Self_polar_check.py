#!/usr/bin/python3

from fractions import Fraction
import numpy as np
import os

def omega(v, w):
	sum = 0
	for i in range(int(len(v)/2)):
		sum += v[2*i]*w[2*i + 1] - w[2*i]*v[2*i+1]
	return sum

def omega_check(v):
	flag = True
	for i  in range(len(v)):
		for j in range(i+1,len(v)):
			if(abs(omega(v[i],v[j])) > 1):
				flag = False
	return flag

def vert_read(file_name):
	v = []
	with open(file_name) as poly_vert:
		for line in poly_vert:
			line.rstrip('\n')
			line = line.split()
			w = []
			for i in range(1,len(line)):
				w.append(Fraction(line[i]))
			v.append(w)

	return v

os.system('polymake --script Polar.pl')
with open('vertnum_orig.txt') as f:
	vertnum_orig = int(f.read())
with open('vertnum_polar.txt') as f:
	vertnum_polar = int(f.read())

if(vertnum_orig != vertnum_polar):
	flag = False
else:
	v = vert_read('poly_polar_vert.txt')
	flag = omega_check(v)


Self_polar_true = open('Self_pol_true.txt', 'w')
Self_polar_true.write(str(flag))
Self_polar_true.close()



