from mySuffixTree import *
import suffixTree as st
import time
import random
import string


#-------------The smaller test----------------------------
#input="banana$"
#input = "Mississippi$"


#-----------The bigger test-------------------------------

# initialize the size of the input string
size = 50000

#using random.choices() generating random strings
input = ''.join(random.choices(string.ascii_lowercase, k= size))
input = input + "$"


suffix_set=set()
for i in range(len(input)):
    suffix_set.add(input[i:len(input)])
print(len(suffix_set))

print(f"The input size is: {len(input)}")
startTime = time.perf_counter()

suffixtree1=mySuffixTree(input)
suffixtree1.build_suffixtree()

endTime = time.perf_counter()
print(f"Build the suffix using my implementation in {endTime - startTime:0.4f} seconds")

startTime = time.perf_counter()
suffixtree2= st.Suffixtree(input)
suffixtree2.build_suffixtree()


endTime = time.perf_counter()
print(f"Build the suffix using the suffix-tree library in {endTime - startTime:0.4f} seconds")

suffixlist1=suffixtree1.print_dfs()
print(len(suffixlist1))
#print(suffixlist1)

if (set(suffixlist1)==suffix_set):
    print("The suffixes tree in my implementation contains all the suffixes.")
