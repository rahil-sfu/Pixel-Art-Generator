# Create some helper functions to wrap the
# Pygame image functions

import pygame
import numpy

def getImage(filename):
  """
  Input: filename - string containing image filename to open
  Returns: 3d list of lists
  """
  image = pygame.image.load(filename)
  return pygame.surfarray.array3d(image).tolist()

def saveImage(pixels, filename):
  """
  Input:  pixels - 2d array of RGB values
          filename - string containing filename to save image
  Output: Saves a file containing pixels
  """
  nparray = numpy.asarray(pixels)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  surf = pygame.display.set_mode((width, height))
  pygame.surfarray.blit_array(surf, nparray)
  pygame.image.save(surf, filename)

def showImage(pixels):
  """
  Input:  pixels - 2d array of RGB values
  Output: show the image in a window
  """
  nparray = numpy.asarray(pixels)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  #surf = pygame.display.set_mode((width, height))
  #pygame.surfarray.blit_array(surf, nparray)
  # for pixels2
  pygame.display.init()
  pygame.display.set_caption("CMPT120 - Image")
  screen = pygame.display.set_mode((width, height))
  screen.fill((225, 225, 225))
  screen.blit(surf, (0, 0))
  pygame.display.update()
    
def getBlackImage(width, height):
  return [[[0, 0, 0] for i in range(height)] for j in range(width)]
