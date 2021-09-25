# My first Ticktacktoe with python

import tkinter as tk
import random as rand
import time as t

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

turn = 0

winner = 0

FNT = ('Times New Roman', 60)


def make_board():
    cvs.delete('all')

    for i in range(1, 3):
        cvs.create_line(200*i, 0, 200*i, 600, fill='gray', width=8)  # 縦線
        cvs.create_line(0, 200*i, 600, 200*i, fill='gray', width=8)  # 横線

    for row in range(3):
        for column in range(3):
            x = column * 200
            y = row * 200
            if board[row][column] == 1:
                cvs.create_oval(20+x, 20+y, 180+x, 180+y, outline='red', width=12)
            elif board[row][column] == 2:
                cvs.create_line(20+x, 20+y, 180+x, 180+y, fill='blue', width=12)
                cvs.create_line(180+x, 20+y, 20+x, 180+y, fill='blue', width=12)

    if turn == 0:
        cvs.create_text(300, 300, text='Start!', fill='navy', font=FNT)

    cvs.update()


def click(event):
    global turn

    if turn == 9:
        replay()
        return

    for count in range(1, 9, 2):    # 連続してクリック出来ないように制御
        if turn == count:
            return

    mx = int(event.x/200)
    my = int(event.y/200)

    if mx > 2:   # mx,myの値が3にならないように制御
        mx = 2
    if my > 2:
        my = 2

    if board[my][mx] == 0:
        board[my][mx] = 1
        turn += 1
        make_board()
        t.sleep(0.5)
        judge()
        draw_judge()
        if turn < 9:
            computer()
            make_board()
            t.sleep(0.5)
            judge()
            draw_judge()

    '''
    s = '{},{}'.format(event.x/200, event.y/200)
    cvs.create_text(300, 200, text=s, font=FNT)
    '''


def computer():
    global turn
    for y in range(3):   #置いたら勝てるマスを探す
        for x in range(3):
            if board[y][x] == 0:
                board[y][x] = 2
                judge()
                if winner == 2:
                    turn += 1
                    return
                board[y][x] = 0
    for y in range(3):   #置いたら邪魔できるマスを探す
        for x in range(3):
            if board[y][x] == 0:
                board[y][x] = 1
                judge()
                if winner == 1:
                    board[y][x] = 2
                    turn += 1
                    return
                board[y][x] = 0
    while True:
        x = rand.randint(0, 2)
        y = rand.randint(0, 2)
        if board[y][x] == 0:
            board[y][x] = 2
            turn += 1
            break


def judge():
    global winner
    winner = 0
    for n in range(1, 3):
        if board[0][0] == n and board[1][0] == n and board[2][0] == n:  # 縦判定
            winner = n
        if board[0][1] == n and board[1][1] == n and board[2][1] == n:
            winner = n
        if board[0][2] == n and board[1][2] == n and board[2][2] == n:
            winner = n

        if board[0][0] == n and board[0][1] == n and board[0][2] == n:  # 横判定
            winner = n
        if board[1][0] == n and board[1][1] == n and board[1][2] == n:
            winner = n
        if board[2][0] == n and board[2][1] == n and board[2][2] == n:
            winner = n

        if board[0][0] == n and board[1][1] == n and board[2][2] == n:  # 斜め判定
            winner = n
        if board[0][2] == n and board[1][1] == n and board[2][0] == n:
            winner = n


def draw_judge():
    global turn
    if winner == 1:
        cvs.create_text(300, 300, text='Player win!', font=FNT, fill='cyan')
        turn = 9
    elif winner == 2:
        cvs.create_text(300, 300, text='Computer win!', font=FNT, fill='gold')
        turn = 9
    elif winner == 9 and turn == 9:
        cvs.create_text(300, 300, text='Draw', font=FNT, fill='lime')


def replay():
    global turn
    turn = 0
    for init_y in range(3):
        for init_x in range(3):
            board[init_y][init_x] = 0
    make_board()


root = tk.Tk()
root.title('Ticktacktoe')
root.resizable(False, False)
root.bind('<Button>', click)
cvs = tk.Canvas(width=600, height=600, bg='white')
cvs.pack()
make_board()
root.mainloop()
