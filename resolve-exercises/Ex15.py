#! python3
"""
Bài 15:
Câu hỏi: Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn.
In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
"""

COMMA = ","


def isAllEvenNumber(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True


def main():
    inputStr = input(
        "Input numbers to check even number seperator by comma(','): ")
    inputNumbers = [x for x in inputStr.split(COMMA)]
    evenNumbers = []
    for num in inputNumbers:
        if isAllEvenNumber(num):
            evenNumbers.append(num)
    print(COMMA.join(evenNumbers))


def test():
    assert(isAllEvenNumber(2468))
    assert(isAllEvenNumber(206628440))
    assert(not isAllEvenNumber(222222322222222))
    assert(not isAllEvenNumber(88888888888888888888898888))
    for num in range(1000, 3000 + 1):
        if isAllEvenNumber(num):
            print(num, end=",")
    print("\nunit test success.")


if __name__ == "__main__":
    test()
    main()
