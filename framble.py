#!/usr/bin/python


from letterGenerator import letter_generator

__author__ = "Owen Martin"

WORDS = open("/usr/share/dict/words", "r").readlines()


class Coordinate():
  """The coordinates of a tile in a board"""
  def __init__(self, x, y):
    assert x in range(4)
    assert y in range(4)
    self.x = x
    self.y = y
 
  def __getitem__(self,index):
    if index == 0: return self.x
    if index == 1: return self.y
    
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y  
    
  def tuple(self):
    return tuple(self.x, self.y)
    
  def nextTo(self, other):
    x1 = self.x
    x2 = other.x
    y1 = self.y
    y2 = other.y
    if abs(x1-x2) == 1 and abs(y1-y2) <= 1: return True
    elif abs(y1-y2) == 1 and abs(x1-x2) <= 1: return True
    else: return False
    
  def neighbors(self):
    if self.x == 0:
      xs = [1]
    elif self.x == 3:
      xs = [2]
    else: xs = [self.x-1, self.x+1]
    if self.y == 0:
      ys = [1]
    elif self.y == 3:
      ys = [2]
    else: ys = [self.y-1, self.y+1]
    
    return [Coordinate(x, y) for x in xs for y in ys]

class Tile():
  """A single tile in a board"""
  def __init__(self, letter, place = Coordinate(0,0)):
     self.letter = letter
     assert isinstance(place, Coordinate)
     self.place = place
     
  def __repr__(self):
    return self.letter

  def nextTo(self, other):
    return self.place.nextTo(other.place)


class Board():
  """A board comprised of 4 x 4 tiles"""
  def __init__(self, letters):
    assert len(letters) == 16         
    self.assign_tile_locations(letters)
#    self.word_list = self.generate_word_list()

  def assign_tile_locations(self, letters):
    self.tiles = {}
    for x in range(4):
      for y in range(4):
        self.tiles[(x,y)] = Tile(letters[4*x + y], Coordinate(x, y))
  
  
  def traverse_board(self, start):
    assert isinstance(start, Coordinate)
    
    
  def generate_word_list(self):
    # for tile in Tiles:
    #   for ...:
    #     if word in WORDS:
    #       self.word_list.append(word)
    pass  


def test_board():
  letters = "ABTVERCOPELVEGRI"
  assert len(letters) == 16
  my_board = Board(letters)  
  #print my_board.tiles
  assert my_board.tiles[(3,3)].letter == "I"
  assert my_board.tiles[(2,1)].nextTo(my_board.tiles[(1,2)])
  my_board.traverse_board(Coordinate(3,3))
  assert Coordinate(1,1) in Coordinate(2,2).neighbors()


def test():  
  assert letter_generator            
  test_board()
  print "tests pass"
  
  
test()