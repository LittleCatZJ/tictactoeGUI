#Original author: zkan
#https://github.com/zkan/tictactoe

#author : zhangjian
#date : 2018.04.17

import random
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo

class TicTacToe(tkinter.Frame):
    def __init__(self,parent):
        tkinter.Frame.__init__(self,parent)
        self.parent=parent
        self.parent.title('tic-tac-toe')
        self.parent.resizable(False,False)

        self.board = [' '] * 9
        self.canvas=Canvas(self.parent,width=300,height=300)
        self.canvas.pack()        
        self.draw_board()
        self.canvas.bind('<Button-1>',self.clicked)

    #图形界面tkinter画图部分
    def draw_board(self):
        self.canvas.create_line(2,2,300,2)
        self.canvas.create_line(0,300,300,300)
        self.canvas.create_line(2,2,2,300)

        self.canvas.create_line(0,100,300,100)
        self.canvas.create_line(0,200,300,200)
        self.canvas.create_line(100,0,100,300)
        self.canvas.create_line(200,0,200,300)
        self.canvas.create_line(300,0,300,300)
        
    def clear(self):
        self.canvas.delete('all')
        self.draw_board()
        self.board=[' ']*9

    def draw_x(self,a,b,c,d):
        self.canvas.create_line(a,b,c,d,width=5,fill='red')
        self.canvas.create_line(a,d,c,b,width=5,fill='red')
        
    def draw_o_int(self,c):
        if c==0 : self.canvas.create_oval(90,90,10,10,width=5)
        elif c==1 : self.canvas.create_oval(190,90,110,10,width=5)
        elif c==2 : self.canvas.create_oval(290,90,210,10,width=5)
        
        elif c==3 : self.canvas.create_oval(90,190,10,110,width=5)
        elif c==4 : self.canvas.create_oval(190,190,110,110,width=5)
        elif c==5 : self.canvas.create_oval(290,190,210,110,width=5)
        
        elif c==6 : self.canvas.create_oval(90,290,10,210,width=5)
        elif c==7 : self.canvas.create_oval(190,290,110,210,width=5)
        elif c==8 : self.canvas.create_oval(290,290,210,210,width=5)
        
    def draw_x_int(self,c):
        if c==0 : self.draw_x(90,90,10,10)
        elif c==1 : self.draw_x(190,90,110,10)
        elif c==2 : self.draw_x(290,90,210,10)
        
        elif c==3 : self.draw_x(90,190,10,110)
        elif c==4 : self.draw_x(190,190,110,110)
        elif c==5 : self.draw_x(290,190,210,110)
        
        elif c==6 : self.draw_x(90,290,10,210)
        elif c==7 : self.draw_x(190,290,110,210)
        elif c==8 : self.draw_x(290,290,210,210)
        
    def display_board(self):
        for i in range(len(self.board)):
            if self.board[i]==' ':pass
            elif self.board[i]=='O': self.draw_o_int(i)
            elif self.board[i]=='X': self.draw_x_int(i)
            
    #判定
    def board_full(self):
        return not any([space == ' ' for space in self.board])

    def player_wins(self):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if self.board[a] == self.board[b] == self.board[c]!=' ':
                return True
        return False

    #鼠标点击事件
    def clicked(self,event):
        b=-1
        if 0<event.x<100 and 0<event.y<100 : b= 0
        elif 100<event.x<200 and 0<event.y<100 : b= 1
        elif 200<event.x<300 and 0<event.y<100 : b= 2
        elif 0<event.x<100 and 100<event.y<200 : b= 3
        elif 100<event.x<200 and 100<event.y<200 : b= 4
        elif 200<event.x<300 and 100<event.y<200 : b= 5
        elif 0<event.x<100 and 200<event.y<300 : b= 6
        elif 100<event.x<200 and 200<event.y<300 : b= 7
        elif 200<event.x<300 and 200<event.y<300 : b= 8

        #玩家鼠标点击走棋
        self.board[b] = 'O' if self.board[b]==' 'else self.board[b]

        self.display_board()

        if self.player_wins() :
            tkinter.messagebox.showinfo(title='END', message='You win!')
            self.clear()

        if self.board_full():
            tkinter.messagebox.showinfo(title='DRAW', message='Draw!')
            self.clear()

        #算法走棋
        m=self.move(self.board)
        self.board[m-1] = 'X' if self.board[m-1]==' 'else self.board[m-1]
        
        self.display_board()
        
        if self.player_wins():
            tkinter.messagebox.showinfo(title='END', message='Robot wins!')
            self.clear()       

        if self.board_full():
            tkinter.messagebox.showinfo(title='DRAW', message='Draw!')
            self.clear()

    #极大极小搜索算法部分
    def available_moves(self,board):
        return [i + 1 for i in range(0, 9) if board[i] == ' ']
    
    def move(self,board):
        if len(self.available_moves(board)) == 9:
            return random.choice([1, 3, 7, 9])

        best_value = 0
        for move in self.available_moves(board):
            board[move - 1] = 'X'
            value = self.min_value(board)
            board[move - 1] = ' '
            if value > best_value:
                return move

        return random.choice(self.available_moves(board))

    def terminal_test(self,board):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if 'X' == board[a] == board[b] == board[c]:
                return (True, 1)
            elif 'O' == board[a] ==board[b] == board[c]:
                return (True, -1)

        if not any([space == ' ' for space in board]):
            return (True, 0)

        return (False, 0)

    def max_value(self,board):
        in_terminal_state, utility_value = self.terminal_test(board)
        if in_terminal_state:
            return utility_value

        value = -100000
        for move in self.available_moves(board):
            board[move - 1] = 'X'
            value = max(value, self.min_value(board))
            board[move - 1] = ' '

        return value

    def min_value(self, board):
        in_terminal_state, utility_value = self.terminal_test(board)
        if in_terminal_state:
            return utility_value

        value = 100000
        for move in self.available_moves(board):
            board[move - 1] = 'O'
            value = min(value, self.max_value(board))
            board[move - 1] = ' '

        return value
    
if __name__=='__main__':    
    root=tkinter.Tk()
    t = TicTacToe(root)
    root.mainloop()
    
