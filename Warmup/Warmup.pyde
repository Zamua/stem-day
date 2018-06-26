# These are global variables
# Notice we have access to them in all of our functions
initial_x = 100
initial_y = 300

def setup():
    # Draw the canvas to be 500px by 500px
    size(500, 500)
    
# This function gets called every 'tick'
# Stuff you write in here will be executed over and over again
def draw():
    global initial_x, initial_y
    background(0, 0, 0)
    
    # Draw a red rectangle at the x and y coordinates given
    draw_red_rectangle(100, 100)
    
    # TODO: Draw a red rectangle located to the right of the previous rectangle

    # TODO: Draw a red rectangle using the global variables defined above
    
    # We can add 5 to the initial_x every tick to make the rectangle move
    # to the right 5 pixels every tick 
    initial_x = initial_x + 5
    
    # TODO: Update initial_y value so that it makes the last
    #       rectangle we drew appear to move by 1px down as well as right every tick
    
    # Notice how the rectangle goes off screen
    # We can bound the position of the rectangle with some conditional logic
    
    # 100 is the width of the rectangle, so initial_y + 100 is the bottom edge of the rectangle
    # height is a way to get the the current height of the canvas/screen
    if initial_y + 100 > height:
        # Move the top edge of the rectangel to be 100 pixels above the bottom of the screen
        # This accomodates the entire rectangle
        initial_y = height - 100
    
    # TODO: Prevent the rectangle from moving off of the right side of the screens
    

# This is a function
# They get passed 'parameters' (the things between the parenthesis)
# These can be used in the function and are passed when a function is 'called'
# Functions can be used to reduce code duplication. 
def draw_red_rectangle(x, y):
    w = 100 # width
    h = 100 # height
    
    r = 255 # red
    g = 0   # green
    b = 0   # blue
    
    # Fill all shapes from here on out with the color (255, 0, 0) aka red
    # Note: Colors are described by three numbers, the amount of red, green and blue
    #       These numbers can range from 0 (none) to 255 (a lot)
    #       Mixing and matching the numbers gives different colors
    fill(r, g , b)
    
    # This function actually draws our rectangle
    # It places it's top left corner at x and y, and gives it dimensions w x h
    rect(x, y, w, h)
