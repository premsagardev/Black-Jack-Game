
import random
import art
def black_jack():
    user_cards = []
    computer_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(art.logo)
    def deal_cards():   
        new_card = random.choice(cards)
        user_cards.append(new_card)

    def draw_cards():
        new_card = random.choice(cards)
        return new_card
    def compare(c_score, u_score):
        if c_score > 21:
            print("You Win!")
        if c_score == u_score:
            print("It's a Draw")
        if c_score < u_score:
            print("You Win!")
    # user cards  and current score

    i = 2
    while i != 0:
        deal_cards()
        i -= 1
    current_score = 0
    for i in user_cards:
        current_score += int(i)
    print(f"    Your Cards are :{user_cards}, Current Score: {current_score}")

    # computer draws
    card =draw_cards()
    computer_cards.append(card)
    comp_score = 0
    for i in computer_cards:
        comp_score += int(i)
                
    print(f"    Computer's First Card:{computer_cards}")
    
    while current_score <= 21:
        choice = input("Type 'y' to get another Card, type 'n' to pass: ").lower()
        new_score = 0
        if choice == "y":
            get_card = draw_cards()
            user_cards.append(get_card)
            for i in user_cards:
                new_score += int(i)
            current_score = new_score
            print(f"    Your Cards are :{user_cards}, Current Score: {current_score}")
            print(f"    Computer's First Card:{computer_cards}")

        elif choice == 'n':
            while comp_score < 16:
                card =draw_cards()
                computer_cards.append(card)
                for i in computer_cards:
                    comp_score += int(i)
            print(f"    Your Cards are :{user_cards}, Current Score: {current_score}")
            print(f"Computer's Cards: {computer_cards}, Score :{comp_score}")
            compare(c_score = comp_score, u_score = current_score)
        else :
            print("Enter a Valid choice")

    if current_score == 21:
        card =draw_cards()
        computer_cards.append(card)
        for i in computer_cards:
            comp_score += int(i)
        print(f"Computer's Cards: {computer_cards}, Score :{comp_score}")
        compare(c_score = comp_score, u_score = current_score)
    elif current_score > 21:
        print("You Lose! It's a Bust")

play = input("Do you want to play Black Jack? type 'y' for Yes and 'n' for No. \n").lower()

if play == "y":
    black_jack()
else:
    print("Thank you for Visiting")