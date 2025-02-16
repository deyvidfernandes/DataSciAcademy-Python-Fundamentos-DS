from drawingStates import drawingStates
from random import randint
import util
class Game:

   def __init__(self, src):
      self.src = src
      self.categories = list(set([row[0] for row in src]))
      self.words = list(set([row[1] for row in src]))
      self.attempts = 0
      self.getNewWord()
      self.guessed = []
      self.result = ""
      self.showTip = False

   def getNewWord(self):
      newWord = self.words.pop(randint(0, len(self.words) - 1 ))
      self.currentWord = newWord

   def getCharFieldAsList(self):
      return [char if char.lower() in self.guessed else "_" for char in self.currentWord]

   def resetGame(self):
      self.getNewWord()
      self.attempts = 0
      self.guessed.clear()
      self.showTip = False

   def runTurn(self):
      print(" ")
      
      if self.attempts > 5:
         print(f"\nSuas tentativas acabaram.\nA palavra era:", self.currentWord)
         print(drawingStates[self.attempts])
         print("\nDeseja jogar novamente? (S/N) ")
         util.blankLines(29)
         option = input()
         if option == "N":
            return "END"
         elif option == "S":
            return self.resetGame()
         
      elif set(self.currentWord).issubset(self.guessed):
         print(" ")
         print(f"\n\nVocê venceu!\nA palavra é:", self.currentWord)
         print(drawingStates[self.attempts])
         print("\nDeseja jogar novamente? (S/N) ")
         util.blankLines(29)
         option = input()
         if option == "N":
            return "END"
         elif option == "S":
            return self.resetGame()
         
      else: 
         remainingAttempts = 6 - self.attempts
         wrongLetters = list(filter(lambda c: c not in self.currentWord, self.guessed))
         headerString = f"\n\nVocê tem {6 - self.attempts} tentativas restantes."
         currentCategory = list(filter(lambda word: word[1] == self.currentWord, self.src))[0][0]

         if self.showTip: headerString += f" A palavra tem a ver com: '{currentCategory}'"
         elif remainingAttempts <= 3: headerString += " Digite 'Tip' para ver uma dica."
         print(headerString)
 
         print(f"Letras erradas:", wrongLetters)
         print(drawingStates[self.attempts])
         print("\nPalavra: ", self.getCharFieldAsList())
         self.getChar()

   def getChar(self):
      
      print("Digite seu palpite: ")
      util.blankLines(29)
      char = input().lower()

      if char == "tip":
         self.showTip = True
      elif char not in self.currentWord:
         self.result = "WRONG_ANSWER"
         self.attempts = self.attempts + 1
         self.guessed.append(char)
      else:
         self.result = "CORRECT"
         self.guessed.append(char)

game = Game(util.importWordsAsList())

while True:
   cmd = game.runTurn()
   if cmd=="END": break
