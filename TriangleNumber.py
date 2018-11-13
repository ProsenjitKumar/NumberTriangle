print("Triangle With Numbers\n")

# Enter a Integer Number: 7
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
def same_row_and_serialize_column_number(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")


same_row_and_serialize_column_number(int(input("Enter a Integer Number: ")))


# Enter a Integer Number: 6
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
def row_column_serialize(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")


row_column_serialize(int(input("Enter a Integer Number: ")))