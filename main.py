from gen_words import load_words_len_x
from termcolor import colored, cprint
import sys
import os
import random


def clear():
    os.system("cls")


def get_word(words) -> str:
    return words[random.randint(0, len(words) - 1)]


def gen_new_board(lenght, guesses):
    return [[None for j in range(lenght)] for i in range(guesses)]


def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("".join("[-]" if board[i][j] == None else board[i][j]), end="")
        print()


def draw_score(score, maxscore):
    print("".join(str(score) + "/" + str(maxscore)))


def count_letters(word):
    l_count = [0] * 26
    for c in word:
        l_count[ord(c) - 97] += 1
    return l_count


def new_guess(board, words, word, score):
    guess = ""
    while len(guess) <= 1:
        # while not guess in words:
        print("".join("#" for i in range(len(board[0]))), end="\r")
        guess = str(input())
    # guess = [i for i in guess]
    word_letters = count_letters(word)

    for i in range(len(guess)):
        if word_letters[ord(guess[i]) - 97] == 0:
            board[score][i] = colored("[" + guess[i] + "]", "white")
        elif guess[i] == word[i]:
            board[score][i] = colored("[" + guess[i] + "]", "green")
            word_letters[ord(guess[i]) - 97] -= 1
        else:
            if word_letters[ord(guess[i]) - 97] > 0 and board[score][i] == None:
                board[score][i] = colored("[" + guess[i] + "]", "yellow")
                word_letters[ord(guess[i]) - 97] -= 1

    if word == guess:
        return True
    else:
        return False


def draw_fancy_board(board, score):
    for i in range(score):
        for j in range(len(board[0])):
            if "32" in board[i][j]:
                print("🟩", end="")
            elif "33" in board[i][j]:
                print("🟨", end="")
            else:
                print("⬜", end="")
        print()


if __name__ == "__main__":
    clear()
    win = False
    x = int(input("Word's length: "))
    y = int(input("How many guesses: "))
    score = 0
    words = load_words_len_x(x)
    word = get_word(words)
    board = gen_new_board(x, y)
    while win == False and score <= y:
        clear()
        draw_score(score, y)
        draw_board(board)
        win = new_guess(board, words, word, score)
        score += 1
    clear()
    if win == True:
        print("Won")
    else:
        print("Lost")
        print("".join("the word was: " + word))

    draw_score(score, y)
    draw_fancy_board(board, score)
