#library 


def randomx(x):
    return randint(0, len(x) - 1)


def random_dict_key(x):
    random = randint(0, len(x) - 1)
    return x[random]


replys = {}
with open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + "replys.txt") as f:
    for line in f:
        (key, val) = line.split(";")
        replys[key] = val
        val.lower()

f = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'roasts.txt', 'r+')
roasts = [line for line in f.readlines()]

z = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'whales.txt', 'r+')
whales = [line for line in z.readlines()]

k = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'tendies.txt', 'r+')
tendies = [line for line in k.readlines()]