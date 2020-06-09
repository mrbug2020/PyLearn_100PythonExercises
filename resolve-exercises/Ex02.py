#! python3
"""
Bài 02:
Câu hỏi: Viết một chương trình có thể tính giai thừa của một số cho trước.
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
"""


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)



def main():
    x = int(input("Nhap vao so can tinh giai thua x = "))
    print(fact(x))


def test():
    assert(fact(8) == 40320)
    assert(fact(0) == 1)


if __name__ == "__main__":
    test()
    main()
