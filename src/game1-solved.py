import pygame  # This is the library of code we are using to play the game.

class GameState():
    """This is a 'class' which allows us to store data about our game. """
    
    quit = False

    # Colors we want to use in our game.
    black = (0,0,0)
    white = (255,255,255)
    purple = (128,0,128)

    # How big we want our game screen to be.
    display_width = 800
    display_height = 600

    # Images we want to use in our game, and where we want the image to start.
    birdImage = pygame.image.load('green-bird.png')
    bird_x =  0
    bird_y = 0

# This is the copy of the class we defined above. We will use it in our code
# to tell pygame information about our game.
state = GameState()  


def display_bird_at(x,y):
    """This function is used to tell the computer where
    to move the bird to. It takes an x and y as its inputs
    and moves the bird to those coordinates on the game board."""
    
    state.gameDisplay.blit(state.birdImage, (x,y))


def init_game():
    """This function starts our game."""
    
    # Tell pygame to start out game.
    pygame.init()

    # Use `state` to get details about our game and tell pygame how big to make
    # the display.
    state.gameDisplay = pygame.display.set_mode((state.display_width, state.display_height))
    
    # Tell pygame what caption to use in the title bar of the game.
    pygame.display.set_caption('Birdzzz')


def play_game():
    """This function is what allows us to interact with the game.
    It responds to the actions of the user and move the bird!"""
    
    # This a loop that will run as long as the user does not quit the game.
    while not state.quit:
        # This will loop over all game "events", which are the actions that user
        # takes. 
        for event in pygame.event.get():
            # This checks if the user implements a "quit" event, if so it
            # stops the game.
            if event.type == pygame.QUIT:
                state.quit = True

            # The is defining a variable so we can use it later. 
            bird_x_change = 0

            # This checks if the user pressed a key.
            if event.type == pygame.KEYDOWN:
                # This checks if the key that the user pressed is the LEFT arrow.
                if event.key == pygame.K_LEFT:
                    bird_x_change = -5
                elif event.key == pygame.K_RIGHT:  # This can also be an `if` statement.
                    bird_x_change = 5

        # This tells pygame to add the amount above to the bird's "x" coordinate.
        state.bird_x += bird_x_change

        # This tells pygame what color to fill the game display.
        state.gameDisplay.fill(state.purple)
        
        # This calls the `diplay_bird_at` function, which tells pygame where to
        # display the bird.
        display_bird_at(state.bird_x, state.bird_y)
        
        # This tells pygame to update its display with all the actions specified.
        pygame.display.update()


init_game()  # Create the game.
play_game()  # Play the game.

pygame.quit()  # Quit the game.
quit()
