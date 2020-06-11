#! python3
"""
Bài 11:
Câu hỏi: Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
"""

COMMA = ","


def sortArr(arrInput):
    return sorted(arrInput)


def main():
    userArrInput = input(
        "Input words seperator by comma(','): \n").split(COMMA)
    print("Words be sorted:")
    print(sortArr(userArrInput))


def test():
    testArrInput = ["without", "hello", "bag", "world"]
    testArrAssert = ["bag", "hello", "without", "world"]
    assert(testArrAssert == sortArr(testArrInput))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
