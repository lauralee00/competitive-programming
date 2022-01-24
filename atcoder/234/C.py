# https://atcoder.jp/contests/abc234/tasks/abc234_c

# Among the positive integers that consist of 0's and 2's when written in base 10, find the K-th smallest integer.

# 02 ->   0000 0010 (2)
# 10 -> 0000 1010
# 20 right shifted once is 10
# 10 left shifted once is 20

# 20 ->  0001 0100 (2)
# 11 -> 0000 1011
# 22 ->  0001 0110 (2)
# 200 -> 1100 1000 (2) -> 0xC8 (hex)
# 202 -> 1100 1010 (2)
# 220 -> 1101 1100 (2)

# strategy is to find kth smallest binary (aka the lookalike of the decimal integer k), left shift it once
k = int(input())
k_in_binary = int(bin(k)[2:]) #get rid of '0b' in '0b0101'
print(k_in_binary << 1)