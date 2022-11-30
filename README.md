# CS320-Algorithm

# PA1 Line of sight 

Givenn an array, X[i,j] of the elevations of points in a (hilly)
terrain, and n information about where the sun currently is,
determine, for each point, whether it is sunlit or in
the shade.

The azimuth is due west, Φ = 270°. So only points to the west
(i.e., on the i
th row) can cast a shadow on [i, j]

### Inputs

n Y[i, j] is an n x n array of (floating point) numbers (in meters)

n The angle of elevation of the sun Θ ≤ 90°

n The angle of azimuth of the sun, Φ

n The horizontal distance (in meters) between adjacent points, d,
(the resolution or scale of our data)

### Output:

n S[i, j] an n x n array of Booleans:

n If [i, j] is in the shade, S[i, j] is 1

n Otherwise it is 0

# PA2 Huffman encoding algorithm 

It takes the name of a file as input and it returns a Huffman code for the letters in the file, in the form of a dict mapping from letters to a binary code as a string. 

For example, when given the example text file provided (example.txt), the method huffman_letter_codes_from_file_contents might return the following dictionary:

**{'H': '00000', 'u': '00001', 'W': '00010', '3': '00011', 'c': '00100', '0': '00101', 'd': '00110', 'S': '00111', 'C': '01000', '\n': '01001', 'm': '0101', '!': '01100', 'g': '01101', 'n': '0111',
    ' ': '100', 't': '1010', 'e': '1011', 's': '1100', 'i': '1101', '.': '11100', 'l': '11101', 'o': '11110', 'r': '111110', '2': '111111'}**
    
Using these Huffman encodings, the file example.txt_encoded would contain:

**000001011111011110111110100010000011110000011111111001011001100101000001001101011011110101100111001000001011010111101010111111101001101110010000100111100101010111010111011010110001001**

Then decoding, we should recover the original message in example.txt. That is, the file example.txt_encoded_decoded would contain:

**Hello CS 320 students. Winter is comming!**

# PA3 Counting Inversion 

The objective of PA3 is to create a program that counts inversions. CountInv code is based on merge sort and must run in O(n log n) time, where n is the input size.
