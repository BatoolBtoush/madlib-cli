

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



def prompt_user(path):
    try:
        f = open(path)
    except:
        print('there\'s an error')
    else:
        content = f.read()
        f.close()
        with open("./assets/madlib_story.txt",'w') as f:
            f.write(content.format(

                adjective_1 = input('Please enter an adjactive '),
                adjective_2 = input('Please enter another adjactive '),
                past_verb = input('Please enter a past tense verb '),
                first_name1 = input('Please enter another first name '),
                adjective_3 = input('Please enter another adjactive '),
                adjective_4 = input('Please enter another adjactive '),
                noun_1 = input('Please enter a plural noun '),
                large_animal = input('Please enter a large animal '),
                small_animal = input('Please enter a small animal '),
                girl_name = input('Please enter a a girl\'s name '),
                adjective_5 = input('Please enter another adjactive '),
                noun_2 = input('Please enter a plural noun '),
                adjective_6 = input('Please enter another adjactive '),
                noun_3 = input('Please enter a plural noun '),
                number_1 = input('Please enter a number between 1-50 '),
                first_name2 = input('Please enter a first name with \'s '),
                number_2 = input('Please enter a number '),
                noun_4 = input('Please enter a plural noun '),
                number_3 = input('Please enter a number '),
                noun_5 = input('Please enter a plural noun '),
                    )

            )
    finally:
        return content



def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        content = "The file could not be found"
    else:
        content = file.read()
        file.close()    
    finally:
        return content        
   
    


def parse_template(content):
    words =[]
    for word in content:
       user_input = input(word +'')
       words.append(user_input)
    return words,content





def merge():
    pass





if __name__ == "__main__":
    welcome()
    content =  read_template("./assets/madlib_story.txt")
    user = prompt_user("./assets/madlib_story.txt")
    # print(txt)
    print(parse_template(user))
    # print(parsed)




