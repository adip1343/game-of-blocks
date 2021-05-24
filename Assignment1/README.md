# Assignment-1
**Task** - To write program that takes input of a string and gives a number which gives sha256 smaller than 
```
target = 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```
Probaility of getting desired string is 1 in 2**20 = 1M so expected number of trials are 1M
Here we randomly generate a number and append it to given string and compute its hash.

To run the code  `python sol.py` 
Give the input string
The output format is as follows
```
Initial hash of our string is : <hash value of input string>  
Hash of new string is : <hash value of output string>
New string is : <output string>
It took <#iterations> iterations.
Time taken is <time>
```