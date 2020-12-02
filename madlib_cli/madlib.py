from textwrap import dedent

import re
def welcome_messeg():
    print(dedent("""
    ************************
    welcome to the madlib game
    here  i will aske you  to add specifice world then i will show you a text have your world in in diffrent places.
    enjoy with the game :)
    ************************
    """))
    # print('************************')
    # print('welcome to the madlib game')
    # print('here  i will aske you  to add specifice world then i will show you a text have your world in in diffrent places.')
    # print('enjoy with the game :)')
    # print('***********************')

def read_template():
    """
    This function reads a file in the same directory
    """
    with open('assets/sample_template.txt', 'r') as file:
        content = file.read()
    return content

def parse(content):
    """
    This function returns a string with language parts removed and a separate list of those language parts.
    Input: a string with language parts
    Outputs: 
        1. a string without language parts
        2. list of language parts
    """
    parts=[]
    string = re.findall(r'\{.*?\}',content) # find list of all words between {}
    print(string)
    text = re.sub("{[^}]*}", " {}", content) # removes the words in {}
    print(text)
    for i in string:
        parts.append(i.strip("{ }"))
    return parts,text  

def merge(text,word):
    #returns a string with the language parts inserted into the template
    var = text.format(*word)
    return var

def copyFile(text):
    #creat new text file 
    print()
    print(text)
    file = open('assets/ready.txt','w')
    file.write(text)




if __name__ == "__main__":
    welcome_messeg()
   
    content = read_template()
    parts =parse(content)
    
    word =[]
    for i in parts[0]:
        msg=input("please add a : " +i + ":" )
        word.append(msg)
    copy = merge(parts[1],word)
    copyFile(copy)
  
     