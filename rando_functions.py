
import time



def rip(message):
        user_msg = message
        for x in usernames.values():
            for y in x.values():
                name = y
                if name in user_msg:
                    x = str(datetime.datetime.now())
                    msg = (f"Rip {name.title()},\n Time of Death: {x[:-7]}")
        return msg
        

def tendies(random):
    num = random
    print(num)
    if num in range(0, 6):
        msg = (f"Yes, my son, here are your tendies {tendies[randomx(tendies)]}")
    else:
        msg = ("Not enough good boi points.")
    return msg