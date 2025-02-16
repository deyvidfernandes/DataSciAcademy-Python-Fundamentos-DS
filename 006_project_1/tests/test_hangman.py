import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.realpath(f"{dir_path}/../src"))

from hangman import Game
from util import importWordsAsList
import logging

LOGGER = logging.getLogger(__name__)

game = Game(importWordsAsList())

def test_getCategories():
   assert set(game.categories).issubset(['Categoria', 'Países', 'Cores', 'Tecnologia', 'Partes do Corpo', 'Instrumentos Musicais', 'Frutas', 'Profissões', 'Comidas', 'Esportes', 'Animais'])

def test_getNewWord():
   game.getNewWord()
   LOGGER.info("Palavra Atual: " + game.currentWord)   
   assert game.currentWord and not (game.currentWord in game.categories)
