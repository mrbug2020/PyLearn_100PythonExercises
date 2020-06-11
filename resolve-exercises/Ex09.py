#! python3
"""
Bài 09:
Câu hỏi: Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
"""
import math

COMMA = ","


def ex(D):
    C = 50
    H = 30
    Q = math.sqrt(((2 * C * D) / H))
    return int(Q)


def main():
    print("Q = √([(2 * C * D)/H])")
    arrD = input("Input numbers seperator by comma(','): \n").split(COMMA)
    for num in arrD:
        print(ex(int(num)), end=",")


def test():
    assert(18 == ex(100))
    assert(22 == ex(150))
    assert(24 == ex(180))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
