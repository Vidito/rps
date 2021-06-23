import random
hand = {
  "rock": '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

  ''',
  "paper":'''
  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''',
  "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
}
choice = input('rock, paper, or scissors?').lower()
ran = random.choice(list(hand.keys()))

if choice == ran:
  print(f"Draw! You: {hand[choice]} \nComputer: {hand[ran]}")
elif choice== 'paper' and ran == 'scissors':
  print(f"You have lost! You: {hand[choice]} \nComputer: {hand[ran]}")
elif choice == "scissors" and ran == "rock":
  print(f"You have lost You: {hand[choice]} \nComputer: {hand[ran]}")
elif choice == "rock" and ran == "paper":
  print(f"You have lostcYou: {hand[choice]} \nComputer: {hand[ran]}")
else:
  print(f"You have won! You: {hand[choice]} \nComputer: {hand[ran]}")
