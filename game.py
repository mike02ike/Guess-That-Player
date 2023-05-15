import os
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Create the label
#         self.label = QLabel('Welcome to Guess that Player! Please enter your name below.\n')

#         # Create the layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)

#         # Set the layout
#         self.setLayout(layout)

# if __name__ == '__main__':
#     # Create the application
#     app = QApplication(sys.argv)

#     # Create the main window
#     window = MyWindow()

#     # Show the window
#     window.show()

#     # Run the event loop
#     sys.exit(app.exec_())4

file1 = open('/Users/MichaelIke/Desktop/Python/Game Project/player_list.txt', 'r')

read1 = file1.read().split('\n')

file_dict = {}
for line in read1[1:]:
    random_player_info = line.strip().split(',')
    name = random_player_info[0]
    info = [item.strip() for item in random_player_info]
    player_dict = {
        'name': name,
        'currently_playing': info[1] == 'Yes',
        'sport': info[2],
        'conference_league': info[3],
        'division': info[4],
        'current_team': info[5],
        'past_teams': info[6].split('|'),
        'age': info[7],
        'height': info[8],
        'weight': info[9],
        'position': info[10],
        'jersey_number': info[11],
        'nationality': info[12],
        'race_ethnicity': info[13],
        'accomplishments': info[14].split("|")
    }
    file_dict[name] = player_dict

#print(file_dict)

class User():
  def __init__(self, name, guess_list, hint_list, points):
    self.name = name
    self.guess_list = guess_list
    self.hint_list = hint_list
    self.points = points

class Game():
  def __init__(self):
    self.listOfPlayers = read1
    self.dictOfPlayers = file_dict
    self.current_player = None
    self.correct_answer = None
    self.game_over = False
    self.error_messages = [
      'Invalid Input: Make sure you input your choice as a valid option given.',
      'Incorrect Guess',
      'Repetitive Input: Make sure you chose a choice that hasnt been given already.',
      'Hint Error: You must buy the "Sport" hint first.',
      'Hint Error: You must buy the "Conference/League" hint first.',
      'Hint Error: You must buy the "Division" hint first.',
      'Hint Error: You must buy the "Current Team" hint first.'
    ]
    self.gameRules = [
      '\nObjective:\nThe goal of this game is to guess the name of a randomly selected professional athlete within the point limit.\n',
      'How to Play:\nThe main menu consists of three other options:\n',
      '     1. Quick Play - this option allows you to play the game immediately.',
      '     2. View Leaderboard - this option allows you to view your score from your most recent game.',
      '     4. Exit - this option allows you to quit the game.\n',
      'To play, select Quick Play from the main menu.',
      'The game will then randomly select a basketball player.\nYour objective is to guess the players name.',
      'You have two options to guess the players name:\n',
      '     a. Enter the name of a player to guess.',
      '     b. Select a hint from a list of 14 hints. Each hint provides a clue to help you identify the player.\n',
      'Scoring:',
      'You start with 0 points.',
      'EACH INCORRECT GUESS WILL RESULT IN A TWO-POINT DEDUCTION.',
      'EACH GIVEN HINT WILL RESULT IN A ONE-POINT DEDUCTION.',
      'You lose the game if you reach the 10-point limit',
      'You win the game if you correctly guess the players name before you get to 10 points.'
    ]

  def main_menu(self):
    menu = True
  
    print('Welcome to Guess that Player! Please enter your name below.\n')
    name = input().strip()
    self.current_player = User(name, [], [], 0)

    #Main Menu
    while not self.game_over:
      print(f'\nHi {name}, select an option below (1 - 4).\n1. Quick Play\n2. View Leaderboard\n3. View Game Manual\n4. Exit')
      menu_choice = input().strip()

      #Quick Play
      if menu_choice == '1':
        self.play()
        self.game_over = False
        x = True
        while x:
          print(f'{self.current_player.name}\'s Points: {self.current_player.points}/10\nCorrect Answer: {self.correct_answer}\nGood game {name}, what next?\n1. Main Menu or 2. Quit Game')
          response = input().strip()

          if response == '1':
            print('\nSure!')
            x = False
            self.current_player.points = 0
            self.current_player.guess_list = []
            self.current_player.hint_list = []
            continue

          elif response == '2':
            print(f'Thanks for playing {name} :)')
            x = False
            self.game_over = True

          else:
            print(self.error_messages[0])
    
      elif menu_choice == '2':
        print(f'LEADERBOARD FROM CURRENT SESSION\n--------------------------------\n{name}: {self.play.hint_num} Hints and {self.play.guess_num} Guesses')
      
      elif menu_choice == '3':
        for rule in self.gameRules:
          print(rule)

      #Exit
      elif menu_choice == '4':
        print(f'Thanks for playing {name} :)')
        self.game_over = True

      else:
        print(self.error_messages[0])


  def play(self):

      keys = list(self.dictOfPlayers.keys())[1:]
      random_key = random.choice(keys)
      random_player = self.dictOfPlayers[random_key]

      self.correct_answer = random_key
      pick_set = set()
      guess_num = 0
      hint_num = 0

      #Start
      print('\n\n----------GAME START----------\nIve chosen my player, lets begin.')
      #print(f'Correct Answer: {self.correct_answer}')

      while(not self.game_over and self.current_player.points < 10):
        print(f'\n{self.current_player.name}\'s Points: {self.current_player.points}/10 \nWould you like to:\n1. Guess Player\n2. Take Hint\n3. View Guesses/Hints')
        choice = input().strip()

        #Guess Player
        if choice == '1':
          while(self.current_player.points < 10 and not self.game_over):
            print(f'\n{self.current_player.name}s Points: {self.current_player.points}/10\n')
            print('Enter your guess below (NOT Case-Sensitive)(Ex: MiChAeL jOrDaN) or enter "Exit":\n')
            guess = input().strip()
            self.current_player.guess_list.append(guess)

            if guess.lower().strip() == 'exit':
              break

            elif guess.lower().strip() == self.correct_answer.lower().strip():
              print('\nCONGRATULATIONS, you guessed my player!\n')
              self.game_over = True
            else:
              self.current_player.points += 2
              print(self.error_messages[1],f'#{len(self.current_player.guess_list)}')

            guess_num += 1
        
        #Take Hint
        elif choice == '2':
          unlock1 = False
          unlock2 = False
          unlock3 = False
          unlock4 = False

          while(self.current_player.points < 10):
            print(f'\n{self.current_player.name}s Points: {self.current_player.points}/10\n')
            print('Pick a hint (1 - 14) or "Exit".')
            for count, item in enumerate(self.listOfPlayers[0].split(',')[1:], 1):
              print(f'{count}. {item}')

            pick = input().strip()
            
            if pick == '1':
              if pick not in pick_set:
                print('\n',random_player['currently_playing'])
                self.current_player.hint_list.append(random_player['currently_playing'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '2':
              if pick not in pick_set:
                print('\n',random_player['sport'])
                self.current_player.hint_list.append(random_player['sport'])
                pick_set.add(pick)
                unlock1 = True
              else:
                print(self.error_messages[2])
                continue
            elif pick == '3':
              #if user hasnt picked the "Sport" hint first
              if pick not in pick_set and not unlock1:
                print(self.error_messages[3])
                continue
              if pick not in pick_set:
                print('\n',random_player['conference_league'])
                self.current_player.hint_list.append(random_player['conference_league'])
                pick_set.add(pick)
                unlock2 = True
              else:
                print(self.error_messages[2])
                continue
            elif pick == '4':
              #if user hasnt picked the "Conference/League" hint first
              if pick not in pick_set and not unlock2:
                print(self.error_messages[4])
                continue
              if pick not in pick_set:
                print('\n',random_player['division'])
                self.current_player.hint_list.append(random_player['division'])
                pick_set.add(pick)
                unlock3 = True
              else:
                print(self.error_messages[2])
                continue
            elif pick == '5':
              #if user hasnt picked the "Division" hint first
              if pick not in pick_set and not unlock3:
                print(self.error_messages[5])
                continue
              if pick not in pick_set:
                print('\n',random_player['current_team'])
                self.current_player.hint_list.append(random_player['current_team'])
                pick_set.add(pick)
                unlock4 = True
              else:
                print(self.error_messages[2])
                continue
            elif pick == '6':
              #if user hasnt picked the "Sport" hint first
              if pick not in pick_set and not unlock1:
                print(self.error_messages[3])
                continue
              if pick not in pick_set:
                print('\n',random_player['past_teams'])
                self.current_player.hint_list.append(random_player['past_teams'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '7':
              if pick not in pick_set:
                print('\n',random_player['age'])
                self.current_player.hint_list.append(random_player['age'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '8':
              if pick not in pick_set:
                print('\n',random_player['height'])
                self.current_player.hint_list.append(random_player['height'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '9':
              if pick not in pick_set:
                print('\n',random_player['weight'])
                self.current_player.hint_list.append(random_player['weight'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '10':
              #if user hasnt picked the "Sport" hint first
              if pick not in pick_set and not unlock1:
                print(self.error_messages[3])
                continue
              if pick not in pick_set:
                print('\n',random_player['position'])
                self.current_player.hint_list.append(random_player['position'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '11':
              if pick not in pick_set:
                print('\n',random_player['jersey_number'])
                self.current_player.hint_list.append(random_player['jersey_number'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '12':
              if pick not in pick_set:
                print('\n',random_player['nationality'])
                self.current_player.hint_list.append(random_player['nationality'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '13':
              if pick not in pick_set:
                print('\n',random_player['race_ethnicity'])
                self.current_player.hint_list.append(random_player['race_ethnicity'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue
            elif pick == '14':
              #if user hasnt picked the "Sport" hint first
              if pick not in pick_set and not unlock1:
                print(self.error_messages[3])
                continue
              if pick not in pick_set and not unlock4:
                print(self.error_messages[6])
                continue
              if pick not in pick_set:
                print('\n',random_player['accomplishments'])
                self.current_player.hint_list.append(random_player['accomplishments'])
                pick_set.add(pick)
              else:
                print(self.error_messages[2])
                continue

            elif pick.lower().strip() == 'exit':
              break

            else:
              print('',self.error_messages[0])
              continue

            self.current_player.points += 1
            hint_num += 1

        #View Guesses/Hints
        elif choice == '3':
          print(f'\n{self.current_player.name}\'s guesses so far: {self.current_player.guess_list}\n{self.current_player.name}\'s hints so far: {self.current_player.hint_list}')

        else:
          print(self.error_messages[0])

game = Game()
game.main_menu()