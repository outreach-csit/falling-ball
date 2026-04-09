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

ball_radius = 50  # Radius of the ball in pixels
ball_x = WIDTH // 2  # Initial x position (centered horizontally)
ball_y = HEIGHT // 2  # Initial y position (centered vertically)

# ==============================================================================
# MAIN SIMULATION LOOP
# ==============================================================================
simulation_running = True  # Flag to control the main loop
while simulation_running:
    # -------------------------------------------------------------------------
    # 1. EVENT HANDLING
    # -------------------------------------------------------------------------
    # Process all events (mouse clicks, key presses, window close, etc.)
    for event in pygame.event.get():
        # Check if the window close button was pressed
        if event.type == pygame.QUIT:
            simulation_running = False  # Exit the loop and end the program

    # -------------------------------------------------------------------------
    # 2. PHYSICS UPDATE
    # -------------------------------------------------------------------------
    # Movement logic will be added here in future steps
    # This is where we'll update ball position based on velocity and gravity

    # -------------------------------------------------------------------------
    # 3. RENDERING
    # -------------------------------------------------------------------------
    # Clear the screen with a background color
    SCREEN.fill("yellow")  # Fill the entire screen with yellow

    # Draw the ball at its current position
    pygame.draw.circle(SCREEN, "blue", (ball_x, ball_y), ball_radius)

    # -------------------------------------------------------------------------
    # 4. DISPLAY UPDATE
    # -------------------------------------------------------------------------
    # Refresh the display to show all drawings
    pygame.display.update()

    # Control frame rate (wait to maintain consistent FPS)
    clock.tick(FPS)  # Delay to keep frame rate steady at 60 FPS
