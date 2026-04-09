"""
WORKSHOP Monday April 7th 2025 - SLDWC Young Women in Aerospace

This is the first step in creating a falling ball simulation.
The code will be built up in steps, with each step adding more functionality.

The code is based on the Pygame library, which is a Python library for
creating games and multimedia applications.

The template includes:
- Setup import modules
- Draw screen stage where things will happen
- Draw a circle in a position

HAVE FUN!
"""

# ==============================================================================
# IMPORTS AND INITIALIZATION
# ==============================================================================

import pygame  # Import the Pygame library for graphics and game development

pygame.init()  # Initialize all Pygame modules (required before using Pygame)

# Set up consistent frame rate to ensure smooth animation
clock = pygame.time.Clock()
FPS = 60  # Frames per second – how often the screen updates (60 is standard)

# ==============================================================================
# SCREEN SETUP
# ==============================================================================

# Define screen dimensions
WIDTH = 1200  # Screen width in pixels
HEIGHT = 800  # Screen height in pixels

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the display window

pygame.display.set_caption("Falling Ball Simulation")  # Set window title

# ==============================================================================
# OBJECTS AND PHYSICS PROPERTIES
# ==============================================================================
GRAVITY = 2  # 3 - pixels per frame
ENERGY_LOSS = 0.1  # 4 - energy loss factor (0.1 means 10% energy loss)

ball_radius = 50  # Radius of the ball in pixels
ball_x = WIDTH // 2  # Initial x position (centered horizontally)
ball_y = 50  # Initial y position (higher up!) - Step 2
ball_velocity = 3  # 3 - initial velocity of the ball

# store floor properties
FLOOR_HEIGHT = 100
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
FLOOR_COLOUR = "red"

# 5 - load assets
ball_img = pygame.image.load("assets/ball-soccer.png")
back_img = pygame.image.load("assets/court-02.png")
back_img = pygame.transform.scale(back_img, (WIDTH, HEIGHT))
ball_radius = ball_img.get_width() // 2  # 5 - ball radius based on image size

# ==============================================================================
# MAIN SIMULATION LOOP
# ==============================================================================
simulation_running = True  # Flag to control the main loop
while simulation_running:
    # -------------------------------------------------------------------------
    # 1. EVENT HANDLING: windows closed?
    # -------------------------------------------------------------------------
    # Process all events (mouse clicks, key presses, window close, etc.)
    for event in pygame.event.get():
        # Check if the window close button was pressed
        if event.type == pygame.QUIT:
            simulation_running = False  # Exit the loop and end the program

    # -------------------------------------------------------------------------
    # 2. PHYSICS UPDATE: update positions, velocities, colors, etc.
    # -------------------------------------------------------------------------
    # Movement logic will be added here in future steps
    # This is where we'll update ball position based on velocity and gravity

    # 3 - apply gravity acceleration, then velocity to position
    ball_velocity = ball_velocity + GRAVITY  # 3 - apply gravity
    ball_y = ball_y + ball_velocity  # 3 - abstract velocity to position

    # 3 - if ball beyond floor, move it back to floor level
    if (ball_y + ball_radius) > FLOOR_Y:  # 4 - below ground?
        ball_y = FLOOR_Y - ball_radius  # Keep the ball on the floor
        # ball_velocity = 0  # 4 - stop the ball from falling further
        ball_velocity = -1 * ball_velocity  # 5 - reverse the ball's velocity
        ball_velocity = ball_velocity * (1 - ENERGY_LOSS)  # 4 - apply energy loss factor

    if abs(ball_velocity) < 2:  # 4 - adjust this value if needed
        ball_velocity = 0

    print(f"Ball velocity: {ball_velocity}")  # Debugging: print current velocity to console
    print(f"Ball position: {ball_y}")  # Debugging: print current position to console
    # -------------------------------------------------------------------------
    # 3. RENDERING: draw the entire frame
    # -------------------------------------------------------------------------
    # Clear the screen with a background color
    # SCREEN.fill("orange")  # Fill the entire screen with yellow
    SCREEN.blit(back_img, (0, 0))   # 5 - court image

    # 2 - draw a floor rectangle at the bottom of screen
    # pygame.draw.rect(SCREEN, "red", (0, FLOOR_Y, WIDTH, HEIGHT))

    # Draw the ball at its current position
    # pygame.draw.circle(SCREEN, "black", (ball_x, ball_y), ball_radius)

    # 5 - draw the ball image instead of a circle
    ball_rect = ball_img.get_rect(center=(ball_x, ball_y))
    SCREEN.blit(ball_img, ball_rect)

    # -------------------------------------------------------------------------
    # 4. DISPLAY UPDATE: refresh the screen
    # -------------------------------------------------------------------------
    # Refresh the display to show all drawings
    pygame.display.update()

    # Control frame rate (wait to maintain consistent FPS)
    clock.tick(FPS)  # Delay to keep frame rate steady at 60 FPS
