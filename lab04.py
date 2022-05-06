"""
SDEV 300
Tyler Heil
Lab 04
02/06/2022
"""
# pip install numpy
import numpy as np


def phonenum():
    """
    This asks for the phone number without dashes and checks to
    see if what they entered was valid if not then it prompts
    again.
    """
    flag = True
    while flag:
        phone = input("Enter your phone number: XXXXXXXXXXX (No Dashes)")
        if len(phone) != 10 or phone.isdigit() != flag:
            print("Phone number invalid, Try again please...")
        else:
            flag = False


def zippycode():
    """
    This does the same as phone number. Only checks for a different length.
    """
    flag = True
    while flag:
        zippy = input("Enter your Zipcode+4: XXXXXXXXX (No Dashes)")
        if len(zippy) != 9 or zippy.isdigit() != flag:
            print("Zipcode invalid, Try again please...")
        else:
            flag = False


def matrix():
    """
    This has 2 different loop statements. The "for" loop is designed to
    iterate through the array and add values 1 at a
    time as the user gives it. The "While" loop is
    designed to check to make sure that the user's answer is valid.
    Lastly it returns the array as a full 3 by 3 matrix by using ".reshape"
    """
    mat = np.empty(9)
    for i in range(9):
        flag = True
        while flag:
            num = input("Num {}: What is the value".format(i))
            if num.isdigit():
                mat[i] = num
                flag = False
            else:
                print("Invalid number, Retry..")
    print("Matrix: ")
    print(mat.reshape(3, 3))
    return mat.reshape(3, 3)


def matadd(mat1, mat2):
    """
    Simply adds the matrix and returns it
    """
    print("You selected Addition. Your results are: ")
    print(np.add(mat1, mat2))
    return np.add(mat1, mat2)


def matsub(mat1, mat2):
    """
    Simply subtracts the matrix and returns it
    """
    print("You selected Subtraction. Your results are: ")
    print(np.subtract(mat1, mat2))
    return np.subtract(mat1, mat2)


def matmultiplies(mat1, mat2):
    """
    Simply multiplies the matrix and returns it
    """
    print("You selected Multiplication. Your results are: ")
    print(np.matmul(mat1, mat2))
    return np.matmul(mat1, mat2)


def matelemul(mat1, mat2):
    """
    Simply multiplies the matrix element by element and returns it
    """
    print("You selected Multiplication Element by Element. Your results are: ")
    print(np.multiply(mat1, mat2))
    return np.multiply(mat1, mat2)


def mattrans(mat1):
    """
    Transpose the matrix it is given
    """
    tran = mat1.transpose()
    print("Your transpose is: ")
    print(tran)


def rowcol(mat1):
    """
    Mean of the rows and columns
    """
    mean = mat1.sum(axis=0) / 3
    mean2 = mat1.sum(axis=1) / 3
    print("The mean of your Rows: ")
    print(mean)
    print("The mean of your Columns: ")
    print(mean2)


def matrixgame():
    """
    This gives the beginning of the matrix game. By asking the user
    if they want to play. The checks are using the first
    character they type and the whole answer in case they put numbers
    with the 'Y'. Otherwise it exits the program
    completely. If it does not exit then it returns back to main.
    After checking the phone number and zip code.
    """
    flag = True
    while flag:
        print("Welcome to my Python Matrix Application! \nDo you want to play the Matrix Game?")
        answer = input("Enter Y for Yes and N for No\n")
        firstchar = answer[0]
        if firstchar.upper() == "Y" and answer.isalpha() == flag:
            phonenum()
            zippycode()
            flag = False
            return flag
        elif firstchar.upper() != "N" or firstchar.isdigit():
            print("Invalid answer... Try again...")
        else:
            print("Goodbye, Thank You for coming!")
            exit()


def main():
    """
    This has 2 loops. So once the user passes the phone and zipcode.
    They make their 2 matrices. and goes into the options
    of what they would like to do. Has 2 exceptions for if they type
    anything but a number or if they type a key out of
    the range of 0-3. But once they pick an option. It does the option
    then comes back to ask the user if they want to play again.
    """
    while True:
        matrixgame()
        print("Enter your First Matrix.")
        matrixone = matrix()
        print("Enter your Second Matrix.")
        matrixtwo = matrix()
        flag = True
        while flag:
            try:
                print("0: Addition. \n1: Subtraction. \n2: Matrix Multiplication "
                      "\n3: Element by element multiplication")
                num = int(input())
                options = {0: matadd,
                           1: matsub,
                           2: matmultiplies,
                           3: matelemul,
                           }
                newmat = options[num](matrixone, matrixtwo)
                mattrans(newmat)
                rowcol(newmat)
                print("*" * 100)
                flag = False
            except ValueError:
                print("Invalid Value! Retry...")
            except KeyError:
                print("Value out of range! Retry...")


if __name__ == '__main__':
    main()
