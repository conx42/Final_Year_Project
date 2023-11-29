
def eval_cond(x):
    if x =='(':
        global CondCounter
        CondCounter=CondCounter+1
    elif x==')':
        CondCounter-=1
    elif CondCounter==0:
        return True
    return CondCounter

print(eval_cond('('))


