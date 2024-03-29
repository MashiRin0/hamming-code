# Hamming-code 
## Introduction

This project has been made to better understand Hamming code. It contains a base 2 matrix class with basic operators, a simple 1-bit parity check, Hamming(7,4) code and lastly a general Hamming(2<sup>m</sup>-1,2<sup>m</sup>-m-1) code where m is the number of parity bits. We used Python 3 for our code. 

## How to use the code

To use the code run the **use_hamming_codes.py** file. It will first ask for a natural number of parity bits *m*, which will decide what hamming code will be used. Please note that this number should be greater than 1, and in general, the program's complexity will scale as a function of this number. There is one exception to this, this is with 3 parity bits, meaning Hamming(7,4) code, since we made this one separately, it has a lower complexity than all other possibilities. After this you choose whether to encode or decode, and finally it will ask for a message, and if you want to encode/decode several nibbles, you should separate these with a single space for decoding. The program can only deal with 1-bit errors.
