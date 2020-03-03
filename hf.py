#This is a program to calculate the Hartree-Fock energy of a closed shell molecule
import numpy as np
from no_of_electrons import no_of_e
from helper_print import find_distance
from helper_print import file_read
#read the geometry
input_file=open('geom.dat')   #open the file
file_content=input_file.readlines() #read content
input_file.close()            #close the file
#print(file_content)

#store the input in list
temp_geom=[]
for line in file_content:
    v_line=line.rstrip()  #strips off the blank spaces in the line
    #print(v_line)
    if len(v_line)>0:
        f=v_line.split()
        temp_geom.append(f)
    
#print(temp_geom)

#number of atoms
NATOM=int(temp_geom[0][0])
print("Total number of atoms are "+str(NATOM))
Atom_Symbol=[]
Geom=[]
for i in range(1,NATOM+1):
    Atom_Symbol.append(temp_geom[i][0])
    Geom.append(temp_geom[i][1:4])   # here we append geometric coordinates of the molecule
print(Atom_Symbol)
print(Geom)
#counting the total number of electrons
total=0
for i in range(len(Atom_Symbol)):
    total=total+no_of_e(Atom_Symbol[i])

print("The total number of electrons in the molecule are "+ str(total))

#calculate the nuclear repulsion energy
E_nuc=0.0
for i in range(NATOM):
    for j in range(0,i):
        Z_a=no_of_e(Atom_Symbol[i])
        Z_b=no_of_e(Atom_Symbol[j])
        R_ab=find_distance(Geom[i],Geom[j])
        E_nuc=E_nuc+(Z_a*Z_b/R_ab)

print(E_nuc)


#reading files
nbasis=7
S=file_read('s.dat',nbasis)

V=file_read('v.dat',nbasis)

T=file_read('t.dat',nbasis)

#hcore
H_core=np.zeros([nbasis,nbasis])
H_core=np.add(V,T)
print(H_core)
