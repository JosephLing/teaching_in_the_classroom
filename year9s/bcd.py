import math

def int2BCD(number):
    bin_list = [2**v for v in range(math.trunc(math.log2(number)), 0, -1)]
    bin_list.append(1)

    bcd = []
    for i in range(len(bin_list)):
        if number >= bin_list[i]:
            bcd.append(1)
            number -= bin_list[i]
        else:
            bcd.append(0)
    return bcd

if __name__ == "__main__":
    print(int2BCD(256))
    print(int2BCD(257))

    print(int2BCD(56))
    print(int2BCD(36))
