from csv import reader as csvReader
import os
def blankLines(n):
   for _ in range(0, n, 1):
      print()

def importWordsAsList():
   filePath = os.path.join(os.path.dirname(__file__), '../assets/words.csv')
   file = open(filePath, mode="r", encoding="utf-8")
   return list(csvReader(file))