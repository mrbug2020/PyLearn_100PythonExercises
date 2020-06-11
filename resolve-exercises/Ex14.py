#! python3
"""
Bài 14:
Câu hỏi: Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. 
Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
Ví dụ đầu vào là: 0100,0011,1010,1001
Đầu ra sẽ là: 1010
"""


COMMA = ","


def is4DigitBinaryNumberMod5(digit4Number: str):
    if not digit4Number:
        return False
    int2p = int(digit4Number, 2)
    return int2p % 5 == 0


def main():
    fourDigitBinaryNumbersStr = [x for x in input(
        "Input 4 digit numbers seperator by comma(','): ").split(COMMA)]
    fourDigitBinaryNumbersMod5 = []
    for x in fourDigitBinaryNumbersStr:
        if is4DigitBinaryNumberMod5(x):
            fourDigitBinaryNumbersMod5.append(x)
    print(COMMA.join(fourDigitBinaryNumbersMod5))


def test():
    assert(is4DigitBinaryNumberMod5("1010"))
    assert(is4DigitBinaryNumberMod5("0101"))
    assert(not is4DigitBinaryNumberMod5("1001"))
    assert(not is4DigitBinaryNumberMod5("0100"))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
