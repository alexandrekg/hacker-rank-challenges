
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 0:
        if n in range(5, 21):
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')