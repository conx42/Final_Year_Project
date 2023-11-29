import nltk
with open('C:/Users/91629/OneDrive/Desktop/7th_SEM_proj_NLTK/custom_Input.c', 'r') as file:
    c_code = file.read()
tokens=nltk.word_tokenize(c_code)
n=len(tokens)
print('After tokenization of the External C file:\n')
print(tokens,'\n')
maxval=2**31-1
minval=-2**31
Condition=[]

c_operators = ['>','<','==','+', '-', '', '/', '%', '++', '--', '=', '+=', '-=', '=', '/=', '%=', '==', '!=', '<', '>', '<=', '>=', '!', '&&', '||', '&', '|', '^', '~', '<<', '>>', '&=', '|=', '^=', '<<=', '>>=', ',', '.', '->', '[', ']', '{', '}', ';', ':', '?']


def eval_cond(x, count):
    global CondCounter
    if(count==1 and x=='('):
        CondCounter=0
        count+=1
    if x =='(':
        CondCounter+=1
    elif x==')':
        CondCounter-=1
    elif CondCounter==0:
        return True
    return False


for i in range(n):
    if tokens[i]=='if':
        for j in range(i+1,n):
            if eval_cond(tokens[j], 1)== False:
                Condition.append(tokens[j])
                # print('token: ',tokens[j])
                # print('condition: ',Condition)
            else:
#                 print(eval_cond(tokens[j]))
                break;

            
print('Conditional statements Identified: \n\n\t', Condition)
possible_test_cases=[]
for i in range(len(Condition)):
    if Condition[i] in c_operators :
        val=(int)(Condition[i+1])
        possible_test_cases.append([val,maxval])
        possible_test_cases.append([minval,val])
        possible_test_cases.append([val])
print("\nPossible Range of Test Cases Identified: \n\n\t",possible_test_cases)
        

print('\nInternal Test cases Identified:\n\t')
for i in range(1,len(Condition)-1):
    print(Condition[i]," ", end="")
    
print('')
    
print('\nPossible Test cases Identified: \n\t')
for i in range(1,len(Condition)-1):
    if Condition[i] == '>':
        print(c_operators[1]," ", end="")
    else:
        print(Condition[i]," ", end="")

print('')        

for i in range(1,len(Condition)-1):
    if Condition[i] == '>':
        print(c_operators[2]," ", end="")
    else:
        print(Condition[i]," ", end="")

def Access_CStatements():
    print("For beautifully printing of Conditional Statements!!!")
def Access_CRanges():
    print("For beautifully printing of Conditional Statements!!!")
def Access_CInternalTestCases():
    print("For beautifully printing of Conditional Statements!!!")
def Access_CPossibleTestCases():
    print("For beautifully printing of Conditional Statements!!!")

print("\n\n/******************end-of-Program*******************/")