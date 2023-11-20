"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW9 - Q1 
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from pprint import pprint
def get_nucleotide_frequencies(nucleotides):
    nucleotides = nucleotides.upper()
    dic = {}
    junk_dic = {}
    not_junk = "ACTG"
    for char in nucleotides:
        if char in not_junk:
           if not char in dic:
              dic[char] = 1
           else:
              dic[char] += 1
        else:
           if not char in junk_dic:
              junk_dic[char] = 1
           else:
              junk_dic[char] += 1
    print(dic)                    
    dic["Junk"] = junk_dic
    return dic
    
def main():
    frequencies = get_nucleotide_frequencies("ACTGTCACGRFRTNHYCTCGACCSGTGTCACGT")
    pprint(frequencies)

main()    
