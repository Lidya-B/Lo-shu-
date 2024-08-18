# ****************************************************************************************************
#
# File name:   LoShu.py
# Description:
#       This program checks if sum of each row, each column, and each diagonal all add up to 15.
#
# ****************************************************************************************************

def checkLeftDiagonal(square):
    diagonal_sum = sum(square[i][i] for i in range(3))
    return diagonal_sum == 15


# ****************************************************************************************************

def checkRightDiagonal(square):
    diagonal_sum = sum(square[i][2 - i] for i in range(3))
    return diagonal_sum == 15


# ****************************************************************************************************

def checkRows(square):
    row_sums = [sum(row) for row in square]
    return all(sum == 15 for sum in row_sums)


# ****************************************************************************************************

def checkCols(square):
    col_sums = [sum(square[i][j] for i in range(3)) for j in range(3)]
    return all(sum == 15 for sum in col_sums)


# ****************************************************************************************************

def getInput():
    print('Enter all values:')
    square = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        print(f'row {i}:')
        for j in range(3):
            while True:
                num = int(input(f"Enter: "))
                if 1 <= num <= 9:
                    square[i][j] = num
                    break
                else:
                    print("Number must be between 1 and 9. Please try again.")
    return square


# ****************************************************************************************************

def display(square):
    for i in range(3):
        for j in range(3):
            print(f"{square[i][j]:<5}", end="")
            if (j + 1) % 3 == 0:
                print()


# ****************************************************************************************************

def checkLoShu(square):
    return checkLeftDiagonal(square) and checkRightDiagonal(square) and checkRows(square) and checkCols(square)


# ****************************************************************************************************

def main():
    square = getInput()
    display(square)

    if checkLoShu(square):
        print("This is a Lo Shu magic square.")
    else:
        print("This is not a Lo Shu magic square.")


# ****************************************************************************************************

if __name__ == '__main__':
    main()

# ****************************************************************************************************

