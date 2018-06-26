# Some Constants
screenw = 720
screenh = 600

ballh = 20
ballw = 20

brickh = 20
brickw = 90

paddleh = 20
paddlew = 90

paddlespeedx = 8

# Initial ball position
ballx = screenw / 2.0 - ballw / 2.0
bally = 360

# Initial paddle position
paddlex = screenw / 2.0 - paddlew / 2.0
paddley = 580

# Initial ball speed (5px/tick downward)
speedx = 0
speedy = 5

# Initial brick values
brick1x = int(screenw / 2.0 - 2 * brickw + brickw / 2.0)
brick1y = 40
brick1show = True

brick2x = brick1x + brickw
brick2y = 40
brick2show = True

# TODO: Define properties for a third brick

def setup():
    # Set the size of the canvas/screen 
    size(screenw, screenh)

def draw():
    global speedy, brick1show, brick2show, brick3show

    # TODO: Change the background color
    background(0, 0, 0)

    # Check for a win
    if win():
        textAlign(CENTER, CENTER)
        textSize(32)
        text("You win!", width / 2, height / 2)
        return

    # Draw the paddle, ball, and bricks
    drawPaddle()
    drawBall()
    drawBricks()

    # Move the ball
    moveBall()
    
    # Move the paddle
    movePaddle()

    # Check for collisions with brick1
    if brick1show and checkCollision(brick1x, brick1y):
        speedy = -speedy
        brick1show = False

    # Check for collisions with brick2
    elif brick2show and checkCollision(brick2x, brick2y):
        speedy = -speedy
        brick2show = False

    # TODO: Handle collisions for brick3

def win():
    # TODO: Add the third brick to the win condition
    return not brick1show and not brick2show

def drawPaddle():
    # TODO: Change the color of the paddle
    
    rect(paddlex, paddley, paddlew, paddleh)

def drawBall():
    # TODO: Change the color of the ball
    
    # Make the pen blue
    fill(0, 0, 255)
    
    # Draw a rectangle
    rect(ballx, bally, ballw, ballh)
    
    # Put the pen back to white
    fill(255, 255, 255)

def drawBricks():
    # TODO: Change the color of the bricks
    if brick1show:
        # Make the pen red
        fill(255, 0, 0)
        
        # Draw a rectangle
        rect(brick1x, brick1y, brickw, brickh)
        
        # Put the pen back to white
        fill(255, 255, 255)

    if brick2show:
        # Make the pen red
        fill(255, 0, 0)
        
        # Draw a rectangle
        rect(brick2x, brick2y, brickw, brickh)
        
        # Put the pen back to white
        fill(255, 255, 255)

    # TODO: Draw brick3 (but only if it should be shown)

def moveBall():
    global ballx, bally, speedx, speedy

    # If the ball is below the paddle
    if bally + ballh > paddley:
        # TODO: Split the paddle into 5 collision zones instead of 3

        # Move the ball to the left if collision with left third
        if (ballx + ballw > paddlex) and (ballx < paddlex + paddlew / 3.0):
            speedx = -5
            speedy = -abs(speedy)

        # Move the ball straight if collision with middle third
        elif (ballx > paddlex + paddlew / 3.0) and (ballx < paddlex + 2 * paddlew / 3.0):
            speedx = 0
            speedy = -abs(speedy)

        # Move the ball right if collision with right third
        elif (ballx + ballw > paddlex + 2 * paddlew / 3.0) and (ballx < paddlex + paddlew):
            speedx = 5
            speedy = -abs(speedy)

    # Stop ball from moving off top of screen
    if bally < 0:
        speedy = -speedy

    # Stop ball from moving off left or right side of screen
    if ballx < 0 or ballx > 700:
        speedx = -speedx

    # Stop ball from moving off bottom of screen, reset ball
    if bally > 600:
        ballx = 360
        bally = 360
        speedx = 0
        speedy = 5
        
    
    # TODO: Update the ballx and bally according to to the speedx and speedy


def movePaddle():
    """
    TODO: Complete this function to make the paddle controllable by the left and right arrow keys
    
    paddlex      (the x position of the top left corner of the paddle) is accessible as a global variable.
    paddlespeedx (the amount the paddle should move)                   is accessible as a global variable.
    """
    global paddlex
 
    if keyPressed:
        if keyCode == LEFT:
            # Move the paddle to the left by paddlespeedx, but don't let it move off screen
            pass
        elif keyCode == RIGHT:
            # Move the paddle to the right by paddlespeedx, but don't let it move off screen
            pass
    

def checkCollision(brickx, bricky):
    """
    TODO: Complete this function to make ball-brick collisons work

    Parameter: brickx - the x value of the topleft corner of a brick
    Parameter: bricky - the y value of the topleft corner of a brick

    brickh (the height of a brick) is accessible as a global variable.
    brickw (the width of a brick)  is accessible as a global variable.
    """

    return ((ballx < brickx + brickw) and
            (ballx + ballw > brickx) and
            (bally < bricky + brickh) and
            (bally + ballh > bricky))
