#! python3
"""
Bài 17:
Câu hỏi:Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
Giả sử đầu vào là: ExamPle InpUt StR
Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8
"""


def countUpperChar(inputStr: str):
    count = 0
    for c in inputStr:
        if c.isupper():
            count += 1
    return count


def countLowerChar(inputStr: str):
    count = 0
    for c in inputStr:
        if c.islower():
            count += 1
    return count


def main():
    inStr = input("Input sentence: ")
    print(f"Upper char: {countUpperChar(inStr)}")
    print(f"Lower char: {countLowerChar(inStr)}")


def test():
    testInputStr = "ExamPle InpUt  5 StR"
    assert(6 == countUpperChar(testInputStr))
    assert(9 == countLowerChar(testInputStr))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
