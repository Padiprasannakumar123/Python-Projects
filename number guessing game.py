import random 
class NUMBER_GUESSING_GAME:
    def get_random_number(self):
        return random.randint(self.l,self.u)
    def start(self):
        self.l=int(input("Enter a lower number:"))
        self.u=int(input("enter a upper number:"))
        random_number=self.get_random_number()
        print(f'Guess the randomly generated number from {self.l} to {self.u}')
        chances=0
        while chances<5: # only 5 chances to guess the random number
            user_number=int(input("Enter the guessed number:"))
            if user_number==random_number:
                print(f'-->Huraay u got it in {chances+1} step')
                break
            elif user_number<random_number:
                print("-->your number is less than the random number")
            else:
                print("--->your number is greater than the random number")
            chances+=1
number_guess=NUMBER_GUESSING_GAME()
number_guess.start()

