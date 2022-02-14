def scale(A):
    n = A[0]
    if n == 1:
        for i in range(0, len(A)):
            if n == A[i]:
                n += 1
            else:
                print("mixed")
                return
        print("ascending")
        return
    elif n == 8:
        for i in range(0, len(A)):
            if n == A[i]:
                n -= 1
            else:
                print("mixed")
                return
        print("descending")
        return
    else:
        print("mixed")
        return


A = list(map(int, input().split()))
scale(A)
