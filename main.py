import pygame
import sys

pygame.init()

#setting up window
width, height = 1280, 720
window_dimensions = width, height
screen = pygame.display.set_mode(window_dimensions)
pygame.display.set_caption("Simulador de Chamba")
my_icon = pygame.image.load("./img/pxArt.png")
pygame.display.set_icon(my_icon)

#ordering functions
def order_height(pos, n):
  return (height - (n*50 + (n - 1)*20))/2 + (pos + ((pos-1)*70))

#main menu options
options = [
  ['play', pygame.Rect((20, order_height(1, 5), 200, 50))],
  ['achievements', pygame.Rect((20, order_height(2, 5), 200, 50))],
  ['tutorial', pygame.Rect((20, order_height(3, 5), 200, 50))],
  ['options', pygame.Rect((20, order_height(4, 5), 200, 50))],
  ['close', pygame.Rect((20, order_height(5, 5), 200, 50))]
]
font = pygame.font.Font(None, 36)

click = False

def show_options():
  for option in options:
    option.append(pygame.image.load('./buttons/img.jpeg'))
    option[1].size = option[2].get_size()
    option[1].center = option[1].center
    pygame.draw.rect(screen, ('#5b6ee1'), option[1])
    text = font.render(option[0], True, (0, 0, 0))
    text_rect = text.get_rect(center=option[1].center)
    screen.blit(option[2], option[1])
    screen.blit(text, text_rect)

def main_menu():
  running = True
  show_options()
  while running:
    global options
    for option in options:
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
