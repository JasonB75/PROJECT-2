import hashlib
import random

# Python code for 2D random walk.
import numpy
import pylab
import math

# defining the number of steps
n = 10

numBits = n*3
input_string = ""
b = ""

#Converts a binary sequence into a floating point number between 0 and 1
#Assumes that the binary string is a binary fraction. Ex. 1101 assumes 0.1101
#Max realistic precision of 14 due to python's float var
def binary_to_decimal(binary_sequence):
    output = 0.0
    for i, bit in enumerate(binary_sequence):
        output += int(bit) * (2 ** -(i + 1))
    return output

with open('example2.txt', 'wb') as file_out:

    test = hashlib.sha3_224()
    x = [0,0]
    for i in range(math.ceil(numBits/224)):
        input_string = ""
        b = ""
        

        for i in range(224):
            input_string += str(random.randint(0,1))


        input_bytes = bytes(input_string, "utf-8")
        test.update(input_bytes)
        hex = test.hexdigest()
        #print(hex)

        d = int(hex, 16)

        b += bin(d)[2:]  # Remove the "0b" prefix

        for i in range(0,len(b), 32):
            out_num = str(int(b[i:i+32],2)) +" " + str(binary_to_decimal(b[i:i+32])) +"\n"
            file_out.write(out_num.encode('ascii'))



    """
        for num in b:
            if num == "0":
                x[0] +=1
            else:
                x[1] +=1

    #print(b)
    print(x)
    print(b)"""




    """
    #creating two array for containing x and y coordinate
    #of size equals to the number of size and filled up with 0's
    x = numpy.zeros(n)
    y = numpy.zeros(n)
    test = []

    # filling the coordinates with random variables
    incrementer = 0
    for i in range(1, n):
        val = str(b[incrementer: incrementer+2])
        incrementer += 2
        test.append(val)
        if val == "00":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == "01":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == "10":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        elif val == "11":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
        

    # plotting stuff:
    #print(test)
    pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
    pylab.plot(x, y)
    pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
    pylab.show()"""