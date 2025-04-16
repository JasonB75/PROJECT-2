from persistqueue import Queue
import math
import random

PATH = "rad_bit_path_testbranch"
random_bit_q = Queue(PATH)

base_output = open('die_hard_output.txt', 'wb')
saftey_output = open('backup_bits.txt', 'a')

main_header = "#==================================================================\n# generator Nuclear_RNG  seed = 1\n#==================================================================\ntype: d\n"

total_bits = random_bit_q.qsize()
total_output_nums = math.floor(total_bits/32)
print(total_output_nums)

header = main_header + "count: " + str(total_output_nums) + "\n" + "numbit: 32\n"

base_output.write(header.encode('ascii'))

total_read = 0

for totalout in range(total_output_nums):
    bit_output = ''
    for bits_per_num in range(32):
        temp = random_bit_q.get()
        bit_output += str(temp)
        saftey_output.write(str(temp)+"\n")
    if totalout % 250000 == 0:
        print(totalout)

    out_num = str(int(bit_output,2)) + "\n"
    base_output.write(out_num.encode('ascii'))

base_output.close()
saftey_output.close()
random_bit_q.task_done()
print("done")
