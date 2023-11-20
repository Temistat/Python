##Question 1
var = 0
for i in range (2,5,3):
    for j in range(i,0,-1):
        var +=j
print(var)
    
var = []
ls = [1,2,3]
for i in ls:
    ls.pop()
    var.append( ls[:] )

print(var)

ls=[5, 10, 15, 20]
var = ls
ls.pop()
var[0]+=1
print(var)

quote = "a wse man can see the mssng lttrs"
message = quote[10:17] + " " + quote[-5:]
var = message.split(" ")
print(var)

area_codes = {"NY": "212",
              "NJ": "201",
              "DC": "202"}
del area_codes["DC"]
var = area_codes
print(var)

##Question 2
def make_alphanum_codes(chars, num_list):
    i = 10
    for num in num_list[::-1]:
        for pos in range(len(chars)):
            code = chars[pos] + ',' + str(num)
            print(i, ':', code, sep='') #sep is empty str
            i - 1
n_list = [1, 2, 3]
alphas = "abc"
make_alphanum_codes(alphas, n_list)

##Question 5a
def get_movies(pairings, name):
    movie_lst = []
    for i in range(len(pairings)):
        if pairings[i][0] == name:
           movie_lst.append(pairings[i][1])
    return movie_lst

##Question 5b
def convert(pairings):
    dic = {}
    for i in range(len(pairings)):
        if not pairings[i][1] in dic:
           dic[pairings[i][0]] =  get_movies(pairings, pairings[i][1])
     return dic

##Question 5c
def get_average(dic):
    length_of_actors = len(dic)
    length_of_movies = 0
    for key in dic:
        length_of_movies += len(dic[key])
    average =  length_of_movies / length_of_actors
    return average

##Question 6    
class MadLib:
    def __init__(self, filepath):
        lines = ''
        try:
            file = open(filepath, 'r')
        except FileNotFoundError:
            self.contents = lines
        for line in file:
            line.strip()
            lines += line
        file.close()    
        self.contents = lines
     def populate_madlib(word_bank):
        for line in self.contents:
            for char in line:
                if char == "[N]":
                   char = word_bank.get_noun()
                elif char == "[V]":
                   char = word_bank.get_verb()
                elif char == "[AV]":
                   char = word_bank.get_advb()
                elif char == "[AJ]":
                   char = word_bank.get_adjv()
     def __str__(self):
         string = self.contents = " ".join(self.contents)
         return string

def main():
    filepath = input("Enter the name of the file: ")
    name = MadLib(filepath).contents
    print(name)
