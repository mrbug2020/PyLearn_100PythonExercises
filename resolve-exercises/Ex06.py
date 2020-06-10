#! python3
"""
Bài 06:
Câu hỏi: Viết một method tính giá trị bình phương của một số.
"""


def square(num):
    return num ** 2


def main():
    num = int(input("Input a number: "))
    print(f"Square of number {num} is: {square(num)}")


def test():
    assert(9 == square(3))
    assert(0 == square(0))
    assert(9801 == square(99))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
