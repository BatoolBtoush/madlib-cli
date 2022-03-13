import re

def welcome():
    line_1= "{:^111}"
    line_2 = "{:^120}"
    line_3= "{:^121}"

    print('*'*120)
    print('')
    print(line_1.format("Welcome to madlib game!"))
    print(line_2.format("You'll be prompted with some messages that will ask you to input a variation of words"))
    print(line_3.format("that will then be returned back to you but this time it'll be in a funny stroy line."))
    print('*'*120)




def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        raise FileNotFoundError('Error: File could not be found')
    else:
        content = file.read()
        file.close()    
        return content        
   
    

def parse_template(content):
    
    parse= re.findall("{(.+?)}",content)
    for part in parse:    
        content= re.sub(part, "",content) 
    return content, tuple(parse)


def user_input(parse):
    user_inputs = []
    for part in parse:
      printed_out = input(f'Please type in {part}: ')
      user_inputs.append(printed_out)
    return user_inputs


def merge(content, user_input):
    result = content.format(*user_input)

    # with open('../madlib_cli/assets/filled_template.txt','w') as output:
    #     output.write(result)
    return result

def filled_template(content):
    print(content)
    ouptut = open('../madlib_cli/assets/filled_template.txt','w')
    ouptut.write(content)
    ouptut.close()





if __name__ == "__main__":
    welcome()
    read = read_template('../madlib_cli/assets/madlib.txt')
    parse, printed = parse_template(read)
    input  = user_input(printed)
    merged = merge (parse,input)
    # print(merged)
    filled_template(merged)
    # print(txt)
    # print(parsed)




