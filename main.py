from tokenizer import Tokenizer 

def __main__():
    tokenizer = Tokenizer()
    with open('example1.txt', 'r') as file:
        input_code = file.read()
    print(input_code)
    print('---------')
    tokens = tokenizer.tokenize(input_code)
    print(tokens)

__main__()