#! python3
"""
Bài 01:
Câu hỏi: Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
"""


def isNumberMod7AndNotMod5(num):
    if num % 7 == 0 and num % 5 != 0:
        return True
    return False


def main():
    for num in range(2000, 3200 + 1):
        if isNumberMod7AndNotMod5(num):
            print(num, end=";")


def test():
    assert(isNumberMod7AndNotMod5(7))
    assert(isNumberMod7AndNotMod5(2464))
    assert(not isNumberMod7AndNotMod5(35))
    assert(not isNumberMod7AndNotMod5(105))


if __name__ == "__main__":
    test()
    main()
