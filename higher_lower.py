import random
import os
from logo import logo,vs,end
from data import data
score=0
random_data1=random.choice(data)
random_data2=random.choice(data)

#First data from data.py
def first():
    #global random_data1
    for key in random_data1:
        if key=='name':
            name1=random_data1[key]
        elif key=='follower_count':
            follower1=random_data1[key]
        elif key=='description':
            description1=random_data1[key]
        elif key=='country':
            country1=random_data1[key]
    return name1,follower1,description1,country1   

#Second data from data.py
def second():
     #global random_data2
     for key in random_data2:
        if key=='name':
            name2=random_data2[key]
        elif key=='follower_count':
            follower2=random_data2[key]
        elif key=='description':
            description2=random_data2[key]
        elif key=='country':
            country2=random_data2[key]
     return name2,follower2,description2,country2        

#Extra for the end of the program
def ends():
    print(f'Your final score is {score} ')
    print(end)
    quit()

#Compare both the data
def compare(compare):
    global random_data1,random_data2,score
    

    name1,follower1,description1,country1=first()
    name2,follower2,description2,country2=second()
    follower1=int(follower1)
    follower2=int(follower2)
    if ((follower1>=follower2) and (compare=='a')) or ((follower1<=follower2) and (compare=='b')):
        print('Right Guess :) ')
        score=score+1
        random_data1=random_data2
        random_data2=random.choice(data)

    else:
        print('You lose :( ')
        ends() 
    


#Main Game

def play():
    Game_continues=True
    while Game_continues==True:
        print(logo)
        name1,follower1,description1,country1=first()
        print(f'Compare A: {name1}, a {description1}, from {country1}.\n')
        print(vs)
        name2,follower2,description2,country2=second()
        print(f'Compare B: {name2}, a {description2}, from {country2}')
        compare_both=input("Who has more followers? Type 'A' or 'B': ").lower()
        compare(compare_both)
        os.system('cls')

#code lol        
play()




        


        
    

