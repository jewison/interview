def mul(n1, n2):
    n1.reverse()
    n2.reverse()
    n3 = []
    print(n1, n2)
    # 确定最长位数
    for i0 in range(len(n1) + len(n2)):
        n3.append(0)
    # 取n1的每一位乘上n2的对应位放入n3的对应位
    for i1 in range(len(n1)):
        for i2 in range(len(n2)):
            n3[i1 + i2] += n1[i1] * n2[i2]
     # 如果有n3的对应位大于9了，则大的那部分整数加到n3的前一位
    for i3 in range(len(n3)):
        if (n3[i3] > 9):
            n3[i3 + 1] += int(n3[i3] / 10)
            n3[i3] = n3[i3] % 10

    n3.reverse()
    return n3


if __name__ == '__main__':
    print(mul([3, 2, 5], [3, 7, 5]))