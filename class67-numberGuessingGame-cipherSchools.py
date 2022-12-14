winning_number=43
guess=1
num=int(input("guess a number between 1 and 100: "))
game_over=False
while not game_over:
    if num==winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over=True
    #win
    else:
        if num<winning_number:
            print("too low")
            guess+=1
            num=int(input("guess again : "))
        else:
            print("too high")
            guess+=1
            num=int(input("guess again : "))
            

        #guess wrong