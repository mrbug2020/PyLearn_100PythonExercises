#! python3
"""
Bài 13:
Câu hỏi: Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
Giả sử đầu vào là:
hello world and practice makes perfect and hello world again
Thì đầu ra là:
again and hello makes perfect practice world
"""

SPACE = " "


def removeDuplicateAndSortSentence(sentence):
    sentenceSet = set(sentence.split(SPACE))
    sentenceSetSort = sorted(sentenceSet)
    return SPACE.join(sentenceSetSort)


def main():
    sente = input("Input sentence to remove duplicate word and sort: ")
    print(removeDuplicateAndSortSentence(sente))


def test():
    inputSentence = "hello world and practice makes perfect and hello world again"
    assertSentenceOutput = "again and hello makes perfect practice world"
    assert(assertSentenceOutput == removeDuplicateAndSortSentence(inputSentence))
    print("Unit test success.")


if __name__ == "__main__":
    test()
    main()
