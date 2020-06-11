#! python3
"""
Bài 10:
Câu hỏi: Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j. Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def createMultiArr(row, col):
    multiArr = [[r for r in range(col)] for c in range(row)]
    for r in range(row):
        for c in range(col):
            multiArr[r][c] = r * c
    return multiArr


def main():
    x = int(input("Input X: "))
    y = int(input("Input Y: "))
    print(createMultiArr(x, y))


def test():
    row3col5MultiArr = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    assert(row3col5MultiArr == createMultiArr(3, 5))
    print("unit test success.")


if __name__ == "__main__":
    test()
    main()
