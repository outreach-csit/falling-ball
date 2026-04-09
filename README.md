# Falling Ball Simulation Workshop

This is the public repository for The School of Computing Technologies workshop on introduction to Algorithmic Thinking and Coding.

This workshop teaches you how to code a simulator in Python that models how objects fall due to gravity.
You'll learn the basics of physics behind free fall (including position, velocity, and acceleration) and how to translate those concepts into code. The workshop will focus on simulating a ball falling and rebounding off the ground, taking into account gravity and energy loss with each bounce. By the end, you’ll have built a simple yet powerful simulation that brings these physical principles to life using Python! 🏀 ⚽

This workshop is based on the Scratch project [Falling Ball](https://scratch.mit.edu/projects/1106875189/) presented at [MAV Annual Conference 2022 and 2024](https://www.mav.vic.edu.au/Conference/Previous-Annual-Conferences).

This repository steps students through the project in a 1-day tutorial, beginning with starter code in [fall.py](fall.py).

- [Falling Ball Simulation Workshop](#falling-ball-simulation-workshop)
  - [Setup and Requirements](#setup-and-requirements)
  - [🕹️ Part I: Tutorial Overview](#️-part-i-tutorial-overview)
    - [1️⃣ Prepare your JuiceMind workspace and test run](#1️⃣-prepare-your-juicemind-workspace-and-test-run)
    - [2️⃣ Setup screen and draw a circle (the “ball”)](#2️⃣-setup-screen-and-draw-a-circle-the-ball)
      - [📖 The flip-book simulator…](#-the-flip-book-simulator)
    - [3️⃣ Let’s move the ball higher up! 🔼](#3️⃣-lets-move-the-ball-higher-up-)
    - [4️⃣  Make the ball fall like magic 🔽](#4️⃣--make-the-ball-fall-like-magic-)
  - [🕹️ Part 2: Add a Floor – Make the Ball Bounce!](#️-part-2-add-a-floor--make-the-ball-bounce)
    - [1️⃣ Define the Floor](#1️⃣-define-the-floor)
    - [2️⃣ Draw the Floor](#2️⃣-draw-the-floor)
    - [3️⃣ Stop the Ball at the Floor](#3️⃣-stop-the-ball-at-the-floor)
  - [CONTRIBUTORS](#contributors)

## Setup and Requirements

This tutorial requires the following software:

- Python 3.10+
- [pygame](https://www.pygame.org/wiki/about) library
- [VSCode](https://code.visualstudio.com/) as the IDE

The linked [Installation](INSTALL.md) instructions install these requirements for Windows and Mac.

## 🕹️ Part I: Tutorial Overview

In this tutorial, we’ll use code to control what appears on the screen. Coding is how we give instructions to a computer using a programming language—in this case, Python.

Python is popular because it’s easy to read (its code looks a bit like plain English!) and very versatile. It’s used by companies like Google, Netflix, Spotify, and NASA, and across many fields including web development, data science, automation, scientific research, game design, and healthcare—for tasks such as predictive analytics and image analysis. It’s a great choice for beginners, while still being powerful enough for building complex projects. 👍

In this tutorial, we’ll **simulate a ball falling and bouncing off the ground** ⚽ 🔽. Along the way, you’ll learn how to position the ball, update its movement as it falls, and even add gravity so it loses energy with each bounce.

As you progress, you’ll explore **key programming concepts** such as sequential steps, variables, functions, loops, and if-statements. These are essential building blocks that can be used to create a wide range of exciting projects.

We’ll write **instructions using functions—named blocks** of code that perform specific tasks, like moving the ball or drawing on the screen. Many useful functions are already available in Python and its libraries. Functions can take inputs called variables, which are like labelled boxes that store information we can use or update.

Instead of writing everything from scratch, we can also use libraries, which are collections of code created by others that we can reuse in our own programs. One such library is Pygame, which makes it easy to draw graphics and build interactive projects like animations and simple games. 🎮

The tutorial is organised into 10 steps 🦶, with each step introducing a new idea and showing how code can be used to model motion and animate our virtual ball. To get started, we’ve provided an initial code template for you to work on. Let’s do it!

### 1️⃣ Prepare your JuiceMind workspace and test run

To improve legibility, setup your JuiceMind screen to show only the instructions (left) and the code (right):

Slide left the Lesson Plan on the left.

Slide right the “Your Progress” panel on the right.

Now, run the given template by clicking the blue PLAY button ⏯️ and see what happens… 👀

### 2️⃣ Setup screen and draw a circle (the “ball”)

Now let’s take a closer look at the starter code 👀 The first lines load and initialise Pygame library, and  create a clock to control how often the screen will update, in our case, 60 frames per second for a smooth animation. 📺

```python
import pygame  # Import the Pygame library for graphics and game development
pygame.init()  # Initialize all Pygame modules (required before using Pygame)

# Set up consistent frame rate to ensure smooth animation
clock = pygame.time.Clock()
FPS = 60  # Frames per second – how often the screen updates (60 is standard)
```

> [!NOTE]
> The symbol # marks the start of a comment. Comments are not executed by the computer—they are there to explain what the code does, making it easier to read and understand later (both for others and for your future self!). 👍 It’s a good habit to include comments in your code so it remains clear and easy to follow.
>
> FPS is a variable, a kind of “box” that can store a value, we can check its value and also replace its value. 👍 It is good habit to use names that tell us what kind of data the variable contains, in this case frames-per-second. When we know we will never change the value of the variable, we often write it in capital letters and we call it a  “constant”.

Next wee need to create our **canvas screen** where things will be drawn. In Pygame (and most graphics libraries), the screen works like a piece of graph paper—a 2D Cartesian plane (maths in action!). We use `x` and `y` coordinates to describe positions, where each point is a pixel that can be coloured:

- The top-left corner is `(0, 0)` — see computers start with 0, not 1! 😯
- Moving right increases `x`; moving down increases `y`
- So `(100, 100)` means 101 pixels across and 101 pixels down (remember we start with 0!)

So, let us define two variables `WIDTH` and `HEIGHT` to store our desired size of the screen and create a display screen using Pygame:

```python
# Define screen dimensions
WIDTH = 1200   # Screen width in pixels
HEIGHT = 800   # Screen height in pixels

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # Create the display window

pygame.display.set_caption('Falling Ball Simulation') # Set window title
```

The variable SCREEN is the most important one here: it refers to the whole Pygame screen window and we will use it to draw things on it!

**Fill the blanks:** The coordinate for the bottom right pixel is [blank] and the coordinate for the middle of the screen is [blank] Remember our screen is of size (1200, 800) with (0,0) being the top-left corner.

Next, we define three variables that define the size of the ball we want to draw, and its initial location in the center of the screen:

```python
ball_radius = 50  # Radius of the ball in pixels
ball_x = WIDTH // 2  # Initial x position (centered horizontally)
ball_y = HEIGHT // 2  # Initial y position (centered vertically)
```

> [!NOTE]
> The operation // is called “integer division”: It divides two numbers and rounds the result down to the nearest whole number. So, 5.5 // 2 = 2

**Question:** What are `ball_radius`, `ball_x` and `ball_y`?

#### 📖 The flip-book simulator…

A simulation works like a “flip-book”: it displays many images one after another, very quickly. Each image represents a small step—for example, the ball moving just a tiny bit.

In practice, a simulation repeatedly goes through four phases:

1. Check if the user has closed the window. If so, stop the simulation.
2. Update the state of the simulation (e.g., move the ball).
3. Render the new picture in the screen.
4. Update the screen.

This cycle is implemented using a `while` loop, which keeps running as long as the simulation is active. We use a boolean true/false (maths again!) variable `simulation_running` to track this: it starts as `True` and is set to `False` only when the user closes the window.

Here’s what the simulation loop looks like:

```python
# Main game loop
simulation_running = True  # keep running?
while simulation_running:
    # 1. if window is closed; set simulation_running = False
    ...

    # 2. Physics simulation update: ball position, velocity, etc.
    ...

    # 3. Render/draw the stage: background, ball, etc
    ...

    # 4. Render/draw the stage: background, ball, etc
    pygame.display.update()
```

- Phase 1 is always the same in Pygame and is given.
- Phase 2 is the most interesting one, as it is  where the actual simulation of a ball falling is implemented.
- Phase 3 is where the rendering (drawing of the whole scene) of the new frame is done, based on all the updates of Phase 2. Here we can chose how to draw the ball, the background, etc!
- Phase 4 just tells pygame to update the whole rendered screen.

**Question:** which is the line of code that draws the background of the stage?

Let us look at the third phase in the simulation cycle. The initial code provided does two things:

1. Fill the screen with yellow color, to represent the background (line 46 on right).
2. Draw a circle in the middle of the screen to represent the ball (line 47 on right).

Both steps are changes to the simulation `SCREEN` variable that we created at the start.

The instruction `pygame.draw.circle` tells pygame to draw a circle with the following information:

- `SCREEN` is where the circle needs to be drawn, namely, in the window of the simulation.
- `blue` is the colour we want the ball to be inside.
- `(ball_x, ball_y)` gives the coordinate position of the center of the circle.
- `ball_radius` is the size of the ball.

In this case, pygame is the library, draw  is the module in the library, and circle is the function in the module that does the actual drawing (there is another function in the draw module called rect). All is provided by the library we imported at the top!  🙆‍♀️

> [!NOTE]
> Notice that some things are written in quotes, like "blue". These are called strings—pieces of data that represent text rather than numbers. If you just write blue without quotes, Python will treat it as a variable name instead! In programming, we use strings to store and work with words, sentences, or any other kind of text. You can also manipulate strings—combine them, extract parts, change letters, or check if certain words appear inside.

### 3️⃣ Let’s move the ball higher up! 🔼

**Step Time! Make it your own:**

1. **Pick your background and ball colors** for your simulation—anything you like! 🖌️ Go wild. Most obvious colors work, but Pygame knows a ton more. Check them out [here](https://www.pygame.org/docs/ref/color_list.html).
2. **Raise the ball up** on the screen so it has room to fall. 😉 Change the variable that holds the ball’s **y-coordinate**. Remember: `(0,0)` is the **top-left corner**, not the middle! Make sure the ball is fully visible—what number will you pick?

🚀 Now you’re in control. Go ahead and tweak things—experiment and see what happens! Maybe move the ball to a side?

### 4️⃣  Make the ball fall like magic 🔽

Time to **bring our ball to life**—let’s make it fall at a steady speed!

**Here’s the trick:** every time the simulation loops (60 times per second 😲), we **move the ball a little bit down**. Remember, in Pygame, the top of the screen is `y = 0`, and the further down you go, the bigger the `y` value.

So if you want the ball to fall **3 pixels per frame**, just do:

```python
ball_y = ball_y + 3
```

💡In programming, this is called an **assignment**. It basically says:

> "Take the current value of `ball_y`, add 3, and then save the result back into `ball_y`."

⚠️ **Heads up:** variables only hold one value at a time. Assign a new value, and the old one is gone—unless you save it somewhere else first:

```python
old_ball_y = ball_y  # save it for later
ball_y = ball_y + 3
```

🚀 **Your mission:**

- Move the ball down some number of pixels every simulation step by changing the ball’s y coordinate
- Make sure it’s inside the simulation loop and before you draw the screen.

Run it, and boom—the ball should start falling smoothly! 👏

## 🕹️ Part 2: Add a Floor – Make the Ball Bounce!

Whoa! Why does the ball just keep falling off the screen? 😱 What happens when `ball_y` goes past the bottom (`HEIGHT`, 800 in our case)?

Right now, nothing is stopping it—it just keeps going. Let’s fix that by **adding a floor** 🛑 so the ball can bounce or stop when it hits it.

### 1️⃣ Define the Floor

Somewhere before your simulation loop, add these variables to store useful information:

```python
FLOOR_HEIGHT = 100
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
```

The first variable stores how tall you want the floor to be (100 pixels). With it, we can then calculate at what y-coordinate the floor at the bottom should start, which is stored in `FLOOR_Y` variable. Don’t forget to **add a comment** explaining your new constants—future-you will thank you! 😉

### 2️⃣ Draw the Floor

Just after we draw the background of the stage, draw a floor as a long rectangle using pygame `rect(..)` drawing function:

```python
pygame.draw.rect(SCREEN, "black", (0, FLOOR_Y, WIDTH, HEIGHT))
```

👉 This command **draws a rectangle on the screen**. In our case, it’s the **floor**. 🧱

What each part means:

- `pygame.draw.rect(...)` → tells Pygame to draw a rectangle
- `SCREEN` → where to draw it (our window)
- `"black"` → the color of the rectangle
- `(0, FLOOR_Y, WIDTH, HEIGHT)` → the top-left rectangle position `(0, FLOOR_Y)` and size `(WIDTH, HEIGHT)`

👀 You should now **see a black floor** at the bottom of the screen. Go ahead—run it and check it out!

💡 Try changing the color or height to see how it affects the floor!

### 3️⃣ Stop the Ball at the Floor

Uh-oh… the ball still goes **through the floor** 😕. Remember, for the computer, colors are just pixels. To make the ball stop, we need a **rule**:

> If the ball position goes beyond the floor, then set the ball exactly at the floor.

In code, we can tell the computer to execute a line only if a condition is true using `if` statements. After you update the balls’ position, you should check Only let the ball fall if it `hasn’t hit the floor yet`.

```python
if (<condition: ball beyond floor>):
    ball_y = <value to set the ball exactly at floor>
```

Ty it! 🏀

_Does it look right?  What if we change say 14 pixels down every frame?_ If it doesn’t look exactly right, think carefully: 🤔

- What does `(ball_x, ball_y)` actually represent?
- Which part of the ball hits the floor first?
- How could you tweak the condition to make it land perfect on the floor top?

💡 You can “debug” your code by printing useful information in interesting places. For example:

```python
print("Ball y position:", ball_y)
```

🎉 **You Did It!**

👏 **Congratulations!** You’ve just built the core of a simulation. Here’s what you’ve learned so far:

- Set up your coding environment and run your simulation.
- Worked with coordinates on a Cartesian plane.
- Updated position using “velocity”.
- Used **if statements** to control behavior.
- Created a **simulation loop** with repetition.
- Applied **math and logic** to model motion.
- Added **collision detection** with the floor.

💡 Now you can **experiment**: try different ball sizes, speeds, colors, or even create your own floor designs. Make it yours!





## CONTRIBUTORS

- Prof. [Sebastian Sardina](https://github.com/ssardina) (contact: sebastian.sardina@rmit.edu.au)
- Mr. [Marcos Sardina](https://github.com/msardina) (original Scratch project and first translation to Python)
- Dr. [Timothy Wiley](https://github.com/timothy-wiley)
- Dr. [Irina Grossman](https://github.com/irigrossman?tab=repositories)
