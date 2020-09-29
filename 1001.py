def callatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = (3*n+1)/2
        count = count + 1
    return count

if __name__ == "__main__":
    n = int(input())
    print(callatz(n))
