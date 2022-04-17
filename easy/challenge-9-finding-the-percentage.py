if __name__ == '__main__':
    marks = [
        {'Krishna': [67, 68, 69]},
        {'Arjun': [70, 98, 63]},
        {'Malika': [52, 56, 60]}
    ]

    max
    for mark in marks:
        print(sum(list(mark.values())[0]))

    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()



def split_string(param):
    return param.split('-')


assert split_string('lost-ark') == ['lost', 'ark']
assert split_string('banana-abacaxi-laranja-melao-melancia') == ['banana', 'abacaxi', 'laranja', 'melao', 'melancia']