#! python3
from Ex02 import *
"""
Bài 03:
Câu hỏi: Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
"""


def createDictPowOfNumber(n):
    if n <= 0:
        return dict()
    resultDict = {}
    for num in range(1, n + 1):
        resultDict[num] = num * num
    return resultDict


def main():
    n = int(input("Nhap n: "))
    dictN = createDictPowOfNumber(n)
    print(dictN)


def test():
    emptyDict = dict()
    number8Dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    assert(createDictPowOfNumber(8) == number8Dict)
    assert(createDictPowOfNumber(0) == emptyDict)
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
