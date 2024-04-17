import pygame
import sys

pygame.init()

#setting up window
width, height = 800, 600
window_dimensions = width, height
screen = pygame.display.set_mode(window_dimensions)
pygame.display.set_caption("Simulador de Chamba")
my_icon = pygame.image.load("./img/pxArt.png")
pygame.display.set_icon(my_icon)

#main menu functions
def order_height(pos, n):
  return (height - (n*50 + (n - 1)*20))/2 + (pos + ((pos-1)*70))

#main menu options
options = [
  ['play', pygame.Rect((30, order_height(1, 5), 300, 50))],
  ['achievements', pygame.Rect((30, order_height(2, 5), 300, 50))],
  ['tutorial', pygame.Rect((30, order_height(3, 5), 300, 50))],
  ['options', pygame.Rect((30, order_height(4, 5), 300, 50))],
  ['close', pygame.Rect((30, order_height(5, 5), 300, 50))]
]
font = pygame.font.Font(None, 36)

click = False
def main_menu():
  running = True
  while running:

    for option in options:
      pygame.draw.rect(screen, (255, 255, 255), option[1])
      text = font.render(option[0], True, (0, 0, 0))
      text_rect = text.get_rect(center=option[1].center)
      screen.blit(text, text_rect)
      if pygame.mouse.get_pressed():
        if option[1].collidepoint(pygame.mouse.get_pos()) and click:
          if option[0] == 'play':
            game()
          elif option[0] == 'achievements':
            achievements()
          elif option[0] == 'tutorial':
            tutorial()
          elif option[0] == 'options':
            config()
          elif option[0] == 'close':
            close()

    click = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          click = True
    pygame.display.flip()

def game():
  running = True
  print('game')
  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    pygame.display.flip()

def achievements():
  running = True
  print('achievements')
  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    pygame.display.flip()

def tutorial():
  running = True
  print('tutorial')
  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    pygame.display.flip()

def config():
  running = True
  print('options')
  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    pygame.display.flip()

def close():
  running = True
  print('close')
  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
    pygame.display.flip()


main_menu()
