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


def find(a_l, b_l, nn, mm):
    n_max = max(nn)
    m_max = max(mm)

    i = j = 0
    #s = func(nn[i], mm[j])
    s1 = nn[0]
    s2 = mm[0]
    a1 = a_l - 1
    b1 = b_l - 1

    for _ in range(a1 + b1):
        if (j == b1) or (nn[i] < n_max):
            i += 1
        elif (i == a1) or (mm[j] < m_max):
            j += 1
        elif max(nn[i+1:]) < n_max:
            j += 1
        else:
            i += 1
        #s += func(nn[i], mm[j])
        s1 += nn[i]
        s2 += mm[j]
    return s1 * 10 ** 9 + s2


'''def func(ni, mj):
    return ni * 10 ** 9 + mj'''


def begin():
    a_len, b_len, n_line, m_line = read_file()
    summa = find(int(a_len), int(b_len), n_line, m_line)
    write_file(str(summa))


if __name__ == '__main__':
    begin()

