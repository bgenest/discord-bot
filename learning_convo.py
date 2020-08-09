
dictionary = {

            "initial message":{"recorded reply":"confidence level(number of appearances)","recorded reply":"confidence level(number of appearances)","etc":"etc",},
            "initial message":{"recorded reply":"confidence level(number of appearances)","recorded reply":"confidence level(number of appearances)","etc":"etc",},
            
            }


# This code needs to read, and properly store two messages, taking the intial into a dict as the key, and the reply will go within that keys item, which is a nested dict. 
# This reply will be placed at the end of the lsit, with a value of 0. if this message combo is found again, the value of that item will grow to 1. The dictionary will be sorted by highest
# to lowest value for its phrase. This should give a proper response after about a value of 10 or so. Should. ( ͡° ͜ʖ ͡°)


def open_create_dict(filename):
    dict_ = {}
    with open(filename) as f:
        contents = f.read()
        dict_ = ast.literal_eval(contents)
        return dict_


def learntotalk(initial,reply):
    convo = open_create_dict("conversations.txt")
    for x,y  in convo.items():
        if x == initial:
        # then add the y to the item of that x key
            if y in x.values():
                yeet = yeet


def learntotalk(initial,reply):
    conv = {}
    with open("conversation.txt") as f:
        contents = f.read()
        cooldown = ast.literal_eval(contents)
        for x,y  in convo.items():
            if initial == x:
            # then add the y to the item of that x key
                for z,c in y.items():
                    if reply == x:
                        c +=1
                        return
                    if reply not in y.items():
                        #append y with reply, and make its value pair 0
                        return
                    return
            convo = sort(convo)
            return
        with open("conversation.txt",'w' ) as f:
                print(cconvo,file = f)

                return "success"
                    

def cooldowntimer(cc):
    cooldown = {}
    with open("cooldown.txt") as f:
        contents = f.read()
        cooldown = ast.literal_eval(contents)
        for user,value in cooldown.items():
            if cc == user :
                cooldown[cc] = str(time.time())
                with open("cooldown.txt",'w' ) as f:
                    print(cooldown,file = f)
            return cooldown[cc]
        else:
            return "false"
