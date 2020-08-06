#rock paper scissors

from random import randint
import time

def rps(x):
    choices = ['rock','paper','scissors']
    y = choices[randint(0,2)]
    m = ""
    if x == 'rock':
        if y == 'rock':
            m = "rock\n wew, we tied."
        if y == 'paper':
            m = "paper\n lol I win you LOSE"
        if y == 'scissors':
            m = "scissors\n you win, I guess..."
    if x == 'paper':
        if y == 'rock':
            m = " rock.\nok.... you win........"
        if y == 'paper':
            m = "paper\n Tied HA you cant even beat a BOT"
        if y == 'scissors':
            m = "scissors...YOU LOST HAHAHHH"
    if x == 'scissors':
        if y == 'rock':
            m = "rock.\n..i win lol"
        if y == 'paper':
            m = "paper.\n..how....i lost wtf"
        if y == 'scissors':
            m = "scissors.\n..we tied LOL" 
    time.sleep(2)       

    return 