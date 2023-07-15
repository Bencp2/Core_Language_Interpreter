#Author: Ben Pearlstein

class Tokenizer:
    
    #creates a tokenizer object for the file given
    def __init__(self, file):
        self.Tokenizer = open(file, "r")
        self.tokens = list()
        self.string = list()
        self.tokenizeLine()
        self.pointer = 0
        
    #This is where the string for an identifier, unsigned integer, reserved word, or invalid token is being created.
    #It will call tokenizeString() if the next character being read is not related to any of the four possibilites.    
    def createString(self, c):
        previous = self.tokens.pop()
        if type(previous) == int:
            #previous was already tokenized
            self.tokens.append(previous)
            self.tokens.append(c)
        elif not previous[0].isdigit() and not previous[0].isalpha():
            #previous is an invalid token
            self.tokenizeString(previous)
            self.tokens.append(c)
        else:
            #previous is either an unsigned interger or reserved word
            new = previous + c
            self.tokens.append(new)
        
    #This is where a string is tokenized to be evaluated to determine if it is one of the following:
    #a specifc reserved word, a specific special symbol, an unsigned integer, an identifier, or a invalid token. 
    #Each string is then represented with a token.
    def tokenizeString(self, previous):
        if type(previous) != int:
            if previous.isnumeric():
                self.tokens.append(31)
            elif previous[0].isalpha() and previous[0].isupper():
                # print(previous)
                if previous == "END OF FILE":
                    self.tokens.append(33)
                else:
                    validId = True
                    for c in previous:
                        if validId and not c.isdigit() and not (c.isalpha() and c.isupper()):
                            validId = False
                            self.tokens.append(34)
                    if validId:
                        self.tokens.append(32)

            elif previous[0].isalpha() and previous[0].islower():
                validRW = True
                for c in previous:
                    if validRW and (c.isdigit() or (c.isalpha() and c.isupper())):
                        validRW = False
                        self.tokens.append(34)
                if validRW:
                    match previous:
                        case "program":
                            self.tokens.append(1)
                        case "begin":
                            self.tokens.append(2)
                        case "end":
                            self.tokens.append(3)
                        case "int":
                            self.tokens.append(4)
                        case "if":
                            self.tokens.append(5)
                        case "then":
                            self.tokens.append(6)
                        case "else":
                            self.tokens.append(7)
                        case "while":
                            self.tokens.append(8)
                        case "loop":
                            self.tokens.append(9)
                        case "read":
                            self.tokens.append(10)
                        case "write":
                            self.tokens.append(11)
                        case default:
                            self.tokens.append(34)
            else:
                match previous:
                    case ';':
                        self.tokens.append(12)
                    case ',':
                        self.tokens.append(13)
                    case '=':
                        self.tokens.append(14)
                    case '!':
                        self.tokens.append(15)
                    case '[':
                        self.tokens.append(16)
                    case ']':
                        self.tokens.append(17)
                    case '&&':
                        self.tokens.append(18)
                    case '||':
                        self.tokens.append(19)
                    case '(':
                        self.tokens.append(20)
                    case ')':
                        self.tokens.append(21)
                    case '+':
                        self.tokens.append(22)
                    case '-':
                        self.tokens.append(23)
                    case '*':
                        self.tokens.append(24)
                    case '!=':
                        self.tokens.append(25)
                    case '==':
                        self.tokens.append(26)
                    case '<':
                        self.tokens.append(27)
                    case '>':
                        self.tokens.append(28)
                    case '<=':
                        self.tokens.append(29)
                    case '>=':
                        self.tokens.append(30)
                    case default:    
                        self.tokens.append(34)                                               
                        
            self.string.append(previous)            

    #This is where the next line from the file chosen -which that must not be empty- is 
    #read character by character and split into strings to become tokenized by tokenizeString(). 
    #If there only exists empty lines, once tokenizeLine has reached the end of the file, it will
    #stop and tell tokenizeStsring to create a end of file token.    
    def tokenizeLine(self):
        line = self.Tokenizer.readline()
        blank = True
        end = False
        lineCounter = 0
        
        while blank and not end:
            for c in line:
                if blank and (c != ' ' and c != '\n'):
                    blank = False

                if len(line) == lineCounter and c != '\n':
                    end = True
                    self.tokenizeString("END OF FILE")
                    
                lineCounter += 1

            if not end and len(line) == 0:
                end = True
                self.tokenizeString("END OF FILE")
            if blank and not end:
                line = self.Tokenizer.readline()
                lineCounter = 0
        
        lineCounter = 0
        for c in line:    
            if lineCounter == 0 or len(self.tokens) == 0:
                if c != ' ':
                    self.tokens.append(c)
                lineCounter += 1
            else:   
                if c in ";,+-*![]()<>":
                    previous = self.tokens.pop()
                    if type(previous) == int:  
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)                        
                    self.tokens.append(c)
                    
                elif c == '&':
                    previous = self.tokens.pop()
                    if previous == '&':
                        new = previous + '&'
                        self.tokenizeString(new)
                    else:
                        if type(previous) == int:  
                            self.tokens.append(previous)
                        else:
                            self.tokenizeString(previous)
                        self.tokens.append('&')
                        
                elif c == '|':
                    previous = self.tokens.pop()
                    if previous == '|':
                        new = previous + '|'
                        self.tokenizeString(new)
                    else:
                        if type(previous) == int:  
                            self.tokens.append(previous)
                        else:
                            self.tokenizeString(previous)
                        self.tokens.append('|')

                elif c == '=':
                    previous = self.tokens.pop()
                    if previous == '!' or previous == '>' or previous == '<' or previous == '=':
                        new = previous + '='
                        self.tokenizeString(new)
                    else:
                        if type(previous) == int:  
                            self.tokens.append(previous)
                        else:
                            self.tokenizeString(previous)         
                        self.tokens.append('=')

                elif c.isdigit() or c.isalpha():
                    self.createString(c)
                elif c == ' ' or c == '\n':
                    previous = self.tokens.pop()
                    if type(previous) == int:  
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)
                        
                else:
                    previous = self.tokens.pop()
                    if type(previous) == int:  
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)                        

                    self.tokenizeString(c)

                lineCounter += 1
                if len(line) == lineCounter and c != '\n':
                    previous = self.tokens.pop()
                    if type(previous) == int:
                        self.tokens.append(previous)
                    else:
                        self.tokenizeString(previous)

                    self.tokenizeString("END OF FILE")
                   
    #returns the current token
    def getToken(self):
        return self.tokens[self.pointer]
        
    #will make the next token the current token
    def skipToken(self):
        if self.getToken() != 33 and self.getToken() != 34:
            if (self.pointer == len(self.tokens) - 1):
                #when there is no tokens after the current token AND the current token is not the last token nor an invalid token
                self.tokenizeLine()
            self.pointer += 1
            
    # returns the integer value of the current unsigned integer token
    def intVal(self):
        currentToken = self.getToken()
        if currentToken != 31:
            #when the current token is not an unsigned integer
            print("\nError: Invalid token!\nToken: ", self.string[self.pointer])
            quit()
        else:
            return int(self.string[self.pointer])
       
    #returns the string name of the current identifier token
    def idName(self):
        currentToken = self.getToken()
        if currentToken != 32:
            #when the current token is not an identifier
            print("\nError: Invalid token!\nToken: ", self.string[self.pointer])
            quit()
        else:
            return self.string[self.pointer]                        
    
    #returns the string name for an identifier
    #This is ONLY used for printing error statements during parsing
    def tokenString(self):
        return self.string[self.pointer]
