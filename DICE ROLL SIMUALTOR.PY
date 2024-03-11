#DICE ROLL SIMUATOR PROJECT
import random

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def main():
    print("Welcome to the Dice Roll Simulator!")
    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides for each die: "))
        
        if num_dice <= 0 or num_sides <= 0:
            print("Please enter valid values (greater than zero) for the number of dice and number of sides.")
            continue
        
        print("Rolling the dice...")
        rolls = roll_dice(num_dice, num_sides)
        print("You rolled:", rolls)
        
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for rolling the dice!")
            break

if __name__ == "__main__":
    main()
