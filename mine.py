import random 
import os
import warnings
print('hi im a is game wite python : lets play');
varfay = True ; 
minimum = 0; 
maximum = 0;
while varfay == True: 
    print('send range of number same as  : 100 to 1000  ');
    number_range = input(''); 
    try:
        minimum = int(number_range.split('to')[0]) ;
        maximum = int(number_range.split('to')[1]) ;
    except : 
        warnings.warn('pleas send integer data , string data is not valid')
    if  maximum > minimum  : 
        print('n1')
        varfay = False ;
    else :
        print ('error !')
        minimum = None ;
        maximum = None;
         
         
#database
def newgamedatabase():
    file = open(os.path.join('database/data.txt'),'w');
    file.write('start new game | code |  ')
    file.close();
    return True ; 
def databasewriter (rounds,data,typewarn) :
    file = open(os.path.join('database/data.txt'),'a') ;
    file.write("round = {} data = {} type = {} | \n\n " . format(rounds,data,typewarn)) ;
    file.close() ;
def readallthedata():
    file = open(os.path.join('database/data.txt'),'r') ;
    alldata = file.read();
    file.close();
    return alldata
newgamedatabase();
rounds = 0 ; 
randomgenerator = random.randrange(minimum,maximum) ;
helnumber = None;
history = {};
win = False; 
while win == False :
    if rounds == 0 : 
        print (''''Okay lets play :) 
               we have some comand in the game !! 
               /history - for watching last comand in the game
               
               ok naw send your gass : 
               ''')
        inputcall = input('ok naw send your gass :');
        rounds += 1;
    else : 
        inputcall = input('''ok send your gass : 
                          
                          we are now on rond :{}''' .  format(rounds));
        rounds += 1;
    try :
        inputcall = int(inputcall); 
    except:
        inputcall = str(inputcall); 
    if type(inputcall) is int : 
        print('ns')
        if inputcall != randomgenerator : 
            if inputcall > maximum : 
                print('thes answer is out of range'); 
                databasewriter(rounds,inputcall,'thes answer is out of range')
            elif (inputcall < maximum) and (inputcall > randomgenerator) :
                print('thes answer is higher than the oure root answer');
                databasewriter(rounds,inputcall,'thes answer is higher than the oure root answer')
            elif inputcall < minimum :
                print('thes answer is out of range'); 
                databasewriter(rounds,inputcall,'thes answer is out of range')
            elif (minimum < inputcall) and (inputcall < randomgenerator) :
                print('thes number is lower than the oure root number');
                databasewriter(rounds,inputcall,'thes number is lower than the oure root number')
        else : 
            print('wow you are send a crect on the oure root'); 
            win = True ;
    else : 
        if inputcall =='/history' : 
            print (readallthedata());
        else : 
            print('what is thes trans comand');
            
                 
                