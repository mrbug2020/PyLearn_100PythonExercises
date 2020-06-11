#! python3
"""
Bài 15:
Câu hỏi: Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn.
In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
"""

COMMA = ","


def isEvenNumber(num):
    return num % 2 == 0


def main():
    inputStr = input(
        "Input numbers to check even number seperator by comma(','): ")
    inputNumbers = [int(x) for x in inputStr.split(COMMA)]
    evenNumbers = []
    for num in inputNumbers:
        if isEvenNumber(int(num)):
            evenNumbers.append(str(num))
    print(COMMA.join(evenNumbers))


def test():
    assert(isEvenNumber(2))
    assert(isEvenNumber(9792))
    assert(not isEvenNumber(1001))
    assert(not isEvenNumber(99999))
    for num in range(1000, 3000 + 1):
        if isEvenNumber(num):
            print(num, end=",")
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
