#!/usr/bin/python3

from fractions import Fraction
import numpy as np
import os

d = 3 #half_dimension 

def omega(v, w):
	sum = 0
	for i in range(int(len(v)/2)):
		sum += v[2*i]*w[2*i + 1] - w[2*i]*v[2*i+1]
	return sum

def vert_write(file_name,parametr,v):
	vertex_file = open(file_name, parametr)
	for vertex in v:
		vertex_file.write("1")
		for coordinate in vertex:
			vertex_file.write(" ")
			vertex_file.write(str(coordinate))
		vertex_file.write("\n")
		vertex_file.write("1")
		for coordinate in vertex:
			vertex_file.write(" ")
			vertex_file.write(str(-coordinate))
		vertex_file.write("\n")
	vertex_file.close()
	return

def vertices_gen(v, w, deep, flag):
	if (deep != 2*d):
		if(flag):
			v = vertices_gen(v, w + [1], deep + 1, True)
			v = vertices_gen(v, w + [0], deep + 1, True)
			v = vertices_gen(v, w + [-1], deep + 1, True)
		else:
			v = vertices_gen(v, w + [1], deep + 1, True)
			v = vertices_gen(v, w + [0], deep + 1, False)
	else:
		if(flag):
			v.append(w)
	return v

def fill_omega_matrix(omega_matrix, v):
	for i in range(len(v)):
		for j in range(i+1, len(v)):
			if (abs(omega(v[i],v[j])) > 1):
				omega_matrix[i][j] = False
				omega_matrix[j][i] = False
	return omega_matrix

def recurtion_enum(omega_matrix, v, number_of_taken_vertices, list_of_ban, deep):
	if(not(any(list_of_ban))):
		vert_write('Vertices.txt','w',[v[i] for i in number_of_taken_vertices])
		os.system('python Self_polar_check.py')
		with open('Self_pol_true.txt', 'r') as f:
			self_pol_true = f.read()
		if(self_pol_true):
			os.system('polymake --script Volume.pl')
			with open('volume.txt') as volume_now:
				vol = Fraction(volume_now.read())
			volume_rec = open('vol_rec_6.txt', 'a')
			with open('vertnum_orig.txt') as f:
				real_vert = (f.read()).rstrip('\n')
			volume_rec.write(real_vert)			
			volume_rec.write(" ")
			volume_rec.write(str(vol))
			volume_rec.write("\n")
			volume_rec.close()
	else:
		next_able_vertices = [i for i in range(deep, len(v)) if list_of_ban[i]]
		for i in next_able_vertices:
			temp_list_of_ban = list_of_ban.copy()
			temp_list_of_ban[i] = False
			add_ban_number = [j for j in range(len(v)) if not(omega_matrix[i][j])]
			for j in add_ban_number:
				temp_list_of_ban[j] = False
			recurtion_enum(omega_matrix, v, number_of_taken_vertices + [i], temp_list_of_ban, i+1)
	return	

v = vertices_gen([], [], 0, False)
omega_matrix = np.full((len(v), len(v)), True)
omega_matrix = fill_omega_matrix(omega_matrix, v)
list_of_ban = np.full(len(v), True)
recurtion_enum(omega_matrix,v ,[], list_of_ban, 0)