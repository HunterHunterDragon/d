def get_intials(fullname):
    answer =[]    
    name_list = fullname.split(" ")    
       for word in name_list:
           answer.append (word(0).upper())
    return ''.join(answer)    
def main(): 
    inp = input("type your name!")
    print(get_intials(inp))

if __name__ == "__main__" 
    main()
