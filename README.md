# Huffman Coding

## Introdution
Huffman coding is a lossless data compression algorithm. Huffman coding uses a variable-length code to represent a source symbol (for example, a character in a file). The code is determined from an estimate of the probabilities of occurrence of source symbols, with a short code associated with the most frequent source symbols.

A Huffman code is optimal in the sense of the shortest length for a per-symbol coding, and a known probability distribution. More complex methods that perform probabilistic modeling of the source provide better compression ratios.

It was invented by David Albert Huffman, and published in 1952.

## How to use the code
1. Put your file in the **assets** folder.
2. Run main.py and input in the terminal the name of your file.
3. A binary compressed file and a frequencies text file are generated in the **result** folder. 
4. The program display on the terminal the compression ratio and the avarage number of bits per characters.

## Organization
I organized the creation of this project with [Trello](https://trello.com/b/BiNcsIKa/huffmancoding).
## Referals
>D.A. Huffman, A method for the construction of minimum-redundancy codes, Proceedings of the I.R.E., septembre 1952, pp. 1098-1102.
