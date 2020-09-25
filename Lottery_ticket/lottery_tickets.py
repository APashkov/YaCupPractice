def read_file(file='input.txt'):
    with open(file) as input_file:
        selected_numbers = input_file.readline()
        ticket_number = input_file.readline()
        lottery_numbers = input_file.readlines()
    return selected_numbers, ticket_number, lottery_numbers


def write_file(result, file='output.txt'):
    with open(file, 'w') as output_file:
        for line in result:
            output_file.write(line + '\n')
    return


def find_winner(selected_num, numbers):
    selected_num_set = set(selected_num.split())
    lucky_list = []
    for num in numbers:
        if len(selected_num_set & set(num.split())) >= 3:
            lucky_list.append('Lucky')
        else:
            lucky_list.append('Unlucky')
    return lucky_list


if __name__ == '__main__':
    a, b, c = read_file()
    write_file(find_winner(a, c))
