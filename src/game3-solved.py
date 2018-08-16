import pygame  # This is the library of code we are using to play the game.
import time 


class GameState():
    """This is a 'class' which allows us to store data about our game. """
    
    quit = False

    # Colors we want to use in our game.
    black = (0,0,0)
    white = (255,255,255)

    # How big we want our game screen to be.
    display_width = 800
    display_height = 600

    # Images we want to use in our game, and where we want the bird image to start.
    birdImage = pygame.image.load("yellow-bird.png")
    treeImage = pygame.image.load("hearts-tree.png")
    nestImage = pygame.image.load("nest.png")
    bird_x =  0
    bird_y = 0

    
# This is the copy of the class we defined above. We will use it in our code
# to tell pygame information about our game.
state = GameState()


def display_tree_at(x, y):
    """This function is used to tell the computer where
    to move the bird to. It takes an x and y as its inputs
    and moves the bird to those coordinates on the game board."""
    
    state.gameDisplay.blit(state.treeImage, (x,y))

    
def display_bird_at(x, y):
    """This function is used to tell the computer where
    to move the bird to. It takes an x and y as its inputs
    and moves the bird to those coordinates on the game board."""
        
    state.gameDisplay.blit(state.birdImage, (x,y))
    
    
def display_nest_at(x, y):
    """This function is used to tell the computer where
    to place the bird's nest. It takes an x and y as its inputs
    and places the nest to those coordinates on the game board."""
    
    state.gameDisplay.blit(state.nestImage, (x,y))

    
def clear_screen():
    """This function creates the gameboard, include the color
    of the background (sky) and the location of the trees."""
    
    state.gameDisplay.fill(state.white)
    
    display_tree_at(0, 100)
    display_tree_at(100, 200)
    display_tree_at(200, 300)
    display_tree_at(300, 400)
    display_tree_at(300, 0)
    display_tree_at(400, 100)
    display_tree_at(500, 200)
    display_tree_at(600, 100)
    display_tree_at(700, 400)
    
    display_nest_at(450, 125)

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
    It responds to the actions of the user and moves the bird!"""
    
    fixed_events = [
        "R", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R", "D", "R",
        "D", "R", "R", "R", "R", "U", "R", "R", "U", "U", "U", "U", "U", "U",
        "U", "L", "L", "L", "L", "L", "L", "D", "D",
    ]

    # This a loop that will run as long as the user does not quit the game.
    while not state.quit:
        for event in pygame.event.get():
            # This checks if the user implements a "quit" event, if so it
            # stops the game.
            if event.type == pygame.QUIT:
                state.quit = True
            
            # Loop one by one through the list `fixed_events` and move the bird according
            # to the letter from the list.
            for event in fixed_events:
                # This is defining a variable for x and y so we can use them later.
                bird_x_change = 0
                bird_y_change = 0
                
                pygame.time.wait(500)  # This tells pygame to wait 500ms between each action.
            
                # Each of these make a change to the bird's location, according to the letter.
                if event == "L":
                    bird_x_change = -50
                elif event == "R":
                    bird_x_change = 50
                elif event == "U":
                    bird_y_change = -50
                elif event == "D":
                    bird_y_change = 50
                
                # This tells pygame to add the amount to the bird's "x" and "y" coordinates.
                state.bird_x += bird_x_change
                state.bird_y += bird_y_change
                
                # This creates a clean gameboard with appropriate sky and trees.
                clear_screen()
                display_bird_at(state.bird_x, state.bird_y)  # Place the bird at the new location.
                pygame.display.update()  # Update the board.
                
            fixed_events = []
            
init_game()  # Create the game.
play_game()  # Play the game.

pygame.quit()  # Quit the game.
quit() 
