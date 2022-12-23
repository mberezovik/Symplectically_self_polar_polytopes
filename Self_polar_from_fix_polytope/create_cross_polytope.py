#!/usr/bin/python3

from fractions import Fraction
import numpy as np
import os

def vert_write(file_name,parametr,v):
	vertex_file = open(file_name, parametr)
	for vertex in v:
		vertex_file.write("1")
		for coordinate in vertex:
			vertex_file.write(" ")
			vertex_file.write(str(coordinate))
		vertex_file.write("\n")
	return

d = 6
v = np.zeros((4*d, 2*d)).astype(int)
for i in range(2*d):
	v[2*i][i] = 1
	v[2*i+1][i] = -1
vert_write('Vertices.txt','w', v)