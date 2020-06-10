#! python3
"""
Bài 05:
Câu hỏi: Định nghĩa một class có ít nhất 2 method: 
    getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển. 
    printString: in chuỗi vừa nhập sang chữ hoa. 
Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class. 
Ví dụ: Chuỗi nhập vào là baitap thì đầu ra phải là: BAITAP
"""


class InputOutputStr(object):

    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printStringUpperCase(self):
        print(self.str.upper())


def ex():
    print("exercise.")


def main():
    ioObj = InputOutputStr()
    ioObj.getString()
    ioObj.printStringUpperCase()


def test():
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
