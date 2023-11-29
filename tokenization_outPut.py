import nltk
with open('C:/Users/91629/OneDrive/Desktop/7th_SEM_proj_NLTK/custom_Input.c', 'r') as file:
    c_code = file.read()
tokens=nltk.word_tokenize(c_code)
n=len(tokens)
print('After tokenization of the External C file:\n')
print(tokens,'\n')