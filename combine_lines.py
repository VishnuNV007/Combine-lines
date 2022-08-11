# Python program to combine each line from first file with the corresponding line in second file.

with open('python1.txt') as fh1, open('abc.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
       
        print(line1+line2)