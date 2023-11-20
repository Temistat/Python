"""
Author: [Temilolwa Omomuwasan]
Assignment / Part: HW5 - Q3
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

A = 'T'
C = 'G'
T = 'A'
G = 'C'

DNA_sequence_1 = input("Enter a DNA sequence: ")
DNA_sequence_2 = input("Enter a second DNA sequence: ")
combined = ''
result = ''
shorter = len(DNA_sequence_1)

if len(DNA_sequence_1) > len(DNA_sequence_2):
   shorter = len(DNA_sequence_2)

for x in range(shorter):
    if DNA_sequence_1[x] in 'ACTG':
       combined += DNA_sequence_1[x] 
    if DNA_sequence_2[x] in 'ACTG':
       combined += DNA_sequence_2[x]
       
if len(DNA_sequence_1) > len(DNA_sequence_2):
    longer = DNA_sequence_1
else:
    longer = DNA_sequence_2
    
rest = longer[shorter:]
for x in range(len(rest)):
    if rest[x] in 'ACTG':
       combined += rest[x]

   
for i in range(len(combined)):
    if combined[i] == 'A':
       new = 'T'
    elif combined[i] == 'C':
       new = 'G'
    elif combined[i] == 'T':
       new = 'A'
    elif combined[i] == 'G':
       new = 'C'   
    result += new
    
print(result)
