#usr/bin/env python3
from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta
from operator import itemgetter
import sys
import glob
import os
#新方法
#input_file2= sys.argv[1]
#print("Output#144:")
#with open(input_file2,'r',newline= '')as filereader2:
  #for row in filereader2:
   # print("{}".format(row.strip()))

#print("input#145:")
#inputPath=sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
 # with open(input_file,'r',newline='')as filereader:
  # for row in filereader:
  #  print("{}".format(row.strip()))

my_letters=['a','b','c','d','e','f','g','h','i','j']
max_index= len(my_letters)
output_file= sys.argv[1]
filewriter= open(output_file,'w')
for index_value in range(len(my_letters)):
  if index_value<(max_index-1):
    filewriter.write(my_letters[index_value]+',')
  else:
    filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output#146:Output written to file")