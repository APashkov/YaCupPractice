def read_file(file='input.txt'):
    with open(file) as input_file:
        a, b = input_file.readline().split()
        n = tuple(map(int, input_file.readline().split()))
        m = tuple(map(int, input_file.readline().split()))
    return a, b, n, m


def write_file(result, file='output.txt'):
    with open(file, 'w') as output_file:
        output_file.write(result)
    return


def find(a_len, b_len, n_tuple, m_tuple):
    a_len = int(a_len) - 1
    b_len = int(b_len) - 1

    n_max = max(n_tuple)
    m_max = max(m_tuple)

    n_reverse = list(n_tuple)
    n_reverse.reverse()

    index_first_n_max = n_tuple.index(n_max)
    index_last_n_max = a_len - n_reverse.index(n_max)
    count_m_max = index_last_n_max - index_first_n_max

    s1 = sum(n_tuple) + n_max * (b_len)

    s21 = m_tuple[0] * index_first_n_max
    s22 = sum(m_tuple)
    s23 = m_max * count_m_max
    s24 = m_tuple[b_len] * (a_len - index_last_n_max)
    s2 = s21 + s22 + s23 + s24

    s = s1 * 10 ** 9 + s2

    return s


def begin():
    a_l, b_l, n_line, m_line = read_file()
    summa = find(a_l, b_l, n_line, m_line)
    write_file(str(summa))


if __name__ == '__main__':
    begin()

