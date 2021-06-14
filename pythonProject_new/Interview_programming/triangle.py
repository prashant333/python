# This set of code returns * printed in triangle pattern.
"""
def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i + 1):

            print("* ", end="")

        print("\r")
"""
# another way of printing triangle using list


def triangle(n):
    myList = []
    for i in range(1, n+1):
        myList.append("*"*i)
    print("\n".join(myList))


n = int(input("Enter value:"))
triangle(n)


