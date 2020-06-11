#! python3
"""
Bài 07:
Câu hỏi: Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách.
Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python.
Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.
"""


def functionDocEx(param):
    """
    this is documention for function.
    fucName: 'functionDocEx'
    param: {param}
    @return docOfThisFunc

    """
    return functionDocEx.__doc__


def square(num):
    """
    Function return square of number
    """
    return num ** 2


def main():
    print(functionDocEx.__doc__)
    print(abs.__doc__)
    print(input.__doc__)
    print(int.__doc__)
    print(square.__doc__)


def test():
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
