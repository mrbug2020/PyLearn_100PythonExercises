#! python3
"""
Bài 04:
Câu hỏi: Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là: ['34', '67', '55', '33', '12', '98'] \ ('34', '67', '55', '33', '12', '98')
"""


def getInputAsListAndTuple():
    arrInput = input("Input list element seperator by comma(','): ").split(",")
    tupInput = tuple(arrInput)
    return arrInput, tupInput


def main():
    arrResult, tupResult = getInputAsListAndTuple()
    print(arrResult)
    print(tupResult)


def test():
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
