
bord_size = 3

# Игровое поле

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board() -> object:
    ''' Выводим игровое поле '''
    print("_" * 4 * bord_size)
    for i in range(bord_size):
        print((" " * 3 + "|") * 3)
        print("", board[i * bord_size], "|", board[1 + i * bord_size], "|", board[2 + i * bord_size], "|")
        print(("_" * bord_size + "|") * bord_size)



def game_step(index, char):
    ''' Выполняем ход '''
    if 0 > index > 10 or board[index - 1] in ("x", "o"):
        return False
    board[index - 1] = char
    return True

def check_win():
    win = False
    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_comb:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win

def start_game():
    # текущий игрок
    current_player = "x"
    # номер шага
    step = 1
    draw_board()
    while step < 10 and check_win() == False:
        index = input(f"Ходит игрок: {current_player}. Введите номер поля (0 - выход): ")
        if index == "0":
            break
        if game_step(int(index), current_player):
            print("Удачный ход")
            if current_player == "x":
                current_player = "o"
            else:
                current_player = "x"

            draw_board()
            step += 1
        else:
            print("Неверный номер! Повторите!")
    if step == 10:
        print("Игра окончена! Ничья!")
    else:
        print("Выйграл " + check_win())

print("Добро пожаловать в крестики-нолики!")
start_game()
