import re
def welcome_messeg():
    print('************************')
    print('welcome to the madlib game')
    print('here  i will aske you  to add specifice world then i will show you a text have your world in in diffrent places.')
    print('enjoy with the game :)')
    print('***********************')

def read_template():
    #read the file
    with open('assets/sample_template.txt', 'r') as file:
        content = file.read()
        
        return content
def parse(content):
    # returns a string with language parts removed and a separate list of those language parts.
    parts=[]
    string = re.findall(r'\{.*?\}',content)
    text = re.sub("{[^}]*}", " {}", content)
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
  
     