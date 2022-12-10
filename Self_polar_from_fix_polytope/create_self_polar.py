#!/usr/bin/python3

from fractions import Fraction
import numpy as np
import os
from random import randint

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

def polar_check(v):
	with open('vertnum_orig.txt') as f:
		vertnum_orig = int(f.read())
	with open('vertnum_polar.txt') as f:
		vertnum_polar = int(f.read())

	if(vertnum_orig != vertnum_polar):
		flag = False
	else:
		v = vert_read('poly_polar_vert.txt')
		flag = omega_check(v)
	return flag

def J_multiplication(v):
	w = v
	for i in range(len(v)):
		for j in range(int(len(v[i])/2)):
			temp = w[i][2*j]
			w[i][2*j] = -w[i][2*j + 1]
			w[i][2*j + 1] = temp
	return w

def polar_add(v):
	flagmassive = np.full(len(v),True)
	add_vert = []
	for i in range(len(v)):
		if(flagmassive[i]):
			add_vert.append(v[i])
			flagmassive[i] = False
			for j in range(i+1, len(v)):
				if(flagmassive[j] == True):
					if(abs(omega(v[i],v[j])) > 1):
						flagmassive[j] = False
	return add_vert


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

def vert_write(file_name,parametr,v):
	vertex_file = open(file_name, parametr)
	for vertex in v:
		vertex_file.write("1")
		for coordinate in vertex:
			vertex_file.write(" ")
			vertex_file.write(str(coordinate))
		vertex_file.write("\n")
	vertex_file.close()
	return

os.system('polymake --script Polar.pl')
v = vert_read('poly_polar_vert.txt')
vert_write('Vertices.txt','w', v)
while(polar_check(v) != True):
	add_vert = polar_add(v)
	add_vert = J_multiplication(add_vert)
	w = vert_read('real_vert.txt')
	vert_write('Vertices.txt','w', w)
	vert_write('Vertices.txt','a', add_vert)
	os.system('polymake --script Polar.pl')
	v = vert_read('poly_polar_vert.txt')
os.system('polymake --script Volume.pl')


