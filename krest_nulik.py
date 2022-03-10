# Показываем доску
# Получаем ход игрока
# Проверяем есть ли выигрыш, если есть - игра закончена
# Если нет выигрыша, повторяем шаги
board = ['.', '.', '.',
         '.', '.', '.',
         '.', '.', '.']


def print_board():
    for i in (0, 1, 2):
        line = ''
        for j in (0, 1, 2):
            line = line + board[i * 3 + j]
        print(line)


def get_input(cross_or_zero):
    ask = input('Ваш ход (x,y), as ' + cross_or_zero)
    (xc, yc) = ask.split(',')
    board[int(yc) * 3 + int(xc)] = cross_or_zero


def is_won(cross_or_zero):
    return is_won_horizontal(cross_or_zero) or is_won_vertical(cross_or_zero) or is_won_cross(cross_or_zero)


def is_won_horizontal(cross_or_zero):
    for i in (0, 1, 2):
        count = 0
        for j in (0, 1, 2):
            if board[i * 3 + j] == cross_or_zero:
                count = count + 1
        if count == 3:
            return True
    return False


def is_won_vertical(cross_or_zero):
    for j in (0, 1, 2):
        count = 0
        for i in (0, 1, 2):
            if board[i * 3 + j] == cross_or_zero:
                count = count + 1
        if count == 3:
            return True
    return False


def is_won_cross(cross_or_zero):
    if board[1 * 3 + 1] != cross_or_zero:
        return False
    if board[0 * 3 + 0] == cross_or_zero and board[2 * 3 + 2] == cross_or_zero:
        return True
    if board[0 * 3 + 2] == cross_or_zero and board[2 * 3 + 0] == cross_or_zero:
        return True
    return False


def won():
    return is_won('x') or is_won('0')


def has_space():
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            if board[i * 3 + j] == '.':
                return True
    return False


def main():
    while has_space():
        print_board()
        get_input('x')
        if is_won('x'):
            print('X won!')
            return
        get_input('0')
        if is_won('0'):
            print ('0 won!')
            return
    print ('Nobody won!')

main()
