def set_bits_and_convert(A, B):
    num = (1 << A) | (1 << B)
    return num
A,B=map(int,input().split())
result = set_bits_and_convert(A, B)
print(result)
