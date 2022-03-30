if __name__ == '__main__':
    # n = int(input())
    n = 3
    save_numbers_as_string = ''
    for i in range(1, n + 1):
        save_numbers_as_string += str(i)

    print(int(save_numbers_as_string))