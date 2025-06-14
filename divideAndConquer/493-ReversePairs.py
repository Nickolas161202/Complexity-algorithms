
def mergeAndCount(A, B) -> list:
    print(A, B)
    return A + B
def reversePairs(S:list) -> tuple[list[int], int]:
    n = len(S)
    if n <= 1:
        return S, 0
    mid = n //2

    A =   reversePairs(S[:mid])
    B=  reversePairs(S[mid:])
    aa =  mergeAndCount(A[0], B[0])
    return (aa, 0)
arr =  [1,3,2,3,1]
res = 0

res =  reversePairs(arr)
