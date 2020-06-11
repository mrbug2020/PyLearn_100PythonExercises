#! python3
"""
Bài 16:
Câu hỏi: Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
Giả sử đầu vào sau được cấp cho chương trình: hello world! 123 Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
"""


def countDigitAndAlpha(inputStr):
    totalDigit = 0
    totalAlpha = 0
    for x in str(inputStr):
        if x.isdigit():
            totalDigit += 1
            continue
        if x.isalpha():
            totalAlpha += 1
    return (totalDigit, totalAlpha)


def main():
    inStr = input("Input sentence: ")
    numberDigit, numberAlpha = countDigitAndAlpha(inStr)
    print(f"Digit: {numberDigit}")
    print(f"Alpha: {numberAlpha}")


def test():
    testInputStr = "hello world! 123"
    assertOutput = (3, 10)
    assert(assertOutput == countDigitAndAlpha(testInputStr))
    assert((2, 9) == countDigitAndAlpha("ok 2 so va 9 chu"))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
