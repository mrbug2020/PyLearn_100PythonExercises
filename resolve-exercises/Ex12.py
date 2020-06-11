#! python3
"""
Bài 12:
Câu hỏi: Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình.
Giả sử đầu vào là: Hello world
Practice makes perfect
Thì đầu ra sẽ là: HELLO WORLD
PRACTICE MAKES PERFECT
"""


def upperCase(sentence):
    return sentence.upper()


def main():
    sentences = []
    print("Input sentence to upper case. End by empty line")
    while True:
        s = input()
        if s:
            sentences.append(s)
        else:
            break
    for s in sentences:
        print(upperCase(s))


def test():
    assert("OK" == upperCase("ok"))  # normal case
    assert("ASSERT" == upperCase("ASSERT"))  # same case
    assert("ASSERT" == upperCase("aSsErT"))  # complex case
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
