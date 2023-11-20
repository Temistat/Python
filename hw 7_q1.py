"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW7 - Q1 
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


def update_frequencies(old_frequencies, new_sequence):
    a_count = 0
    c_count = 0
    t_count = 0
    g_count = 0
    for dna in new_sequence:
        if dna == "A":
           a_count += 1
        elif dna == "C":
           c_count += 1   
        elif dna == "T":
           t_count += 1
        elif dna == "G":
           g_count += 1
    
    a_num = old_frequencies[0][1] + a_count
    c_num = old_frequencies[1][1] + c_count
    t_num = old_frequencies[2][1] + t_count
    g_num = old_frequencies[3][1] + g_count
    line = "Number of nucleotides added: A -> {} | C -> {} | T -> {} | G -> {} | [('A', {}), ('C', {}), ('T', {}), ('G', {})]".format(a_count,c_count,t_count,g_count,a_num,c_num,t_num,g_num)
    return line



def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)

main()    
