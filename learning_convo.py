
# This code needs to read, and properly store two messages, taking the intial into a dict as the key, and the reply will go within that keys item, which is a nested dict. 
# This reply will be placed at the end of the lsit, with a value of 0. if this message combo is found again, the value of that item will grow to 1. The dictionary will be sorted by highest
# to lowest value for its phrase. This should give a proper response after about a value of 10 or so. Should. ( ͡° ͜ʖ ͡°)
 
from convo_library import convo


def open_create_dict(filename):
    dict_ = {}
    with open(filename) as f:
        contents = f.read()
        dict_ = ast.literal_eval(contents)
        return dict_


'''def learntotalk(initial,reply):
    convo = open_create_dict("conversations.txt")
    for x,y  in convo.items():
        if x == initial:
        # then add the y to the item of that x key
            if y in x.values():
                yeet = yeet
'''


def learntotalk(initial,reply):
        for x,y  in convo.items():
            if initial == x:
            # then add the y to the item of that x key ONLY IF the reply is not already in the dict, add to 'else'
                for z,c in y.items():
                    if reply == x:
                        c +=1
                        return
                    if reply not in y.items():
                        #append y with reply, and make its value pair 0
                        x[y].append(reply)
                        return
            else:
                #add x into the main dict as a key, and y as an element in the nested dict.
                    return
            convo = sort(convo)
            return
        with open("conversation.txt",'w' ) as f:
                print(convo,file = f)
                return "success"