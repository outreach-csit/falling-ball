# Falling Ball Simulation Workshop

This is the public repository for The School of Computing Technologies workshop on introduction to Algorithmic Thinking and Coding.

This workshop teaches you how to code a simulator in Python that models how objects fall due to gravity.
You'll learn the basics of physics behind free fall (including position, velocity, and acceleration) and how to translate those concepts into code. The workshop will focus on simulating a ball falling and rebounding off the ground, taking into account gravity and energy loss with each bounce. By the end, you’ll have built a simple yet powerful simulation that brings these physical principles to life using Python! 🏀 ⚽

This workshop is based on the Scratch project [Falling Ball](https://scratch.mit.edu/projects/1106875189/) presented at [MAV Annual Conference 2022 and 2024](https://www.mav.vic.edu.au/Conference/Previous-Annual-Conferences).

This repository steps students through the project in a 1-day tutorial, beginning with starter code in [fall.py](fall.py).

- [Falling Ball Simulation Workshop](#falling-ball-simulation-workshop)
  - [Setup and Requirements](#setup-and-requirements)
  - [Part I: Tutorial Overview](#part-i-tutorial-overview)
    - [1️⃣ Prepare your JuiceMind workspace and test run](#1️⃣-prepare-your-juicemind-workspace-and-test-run)
    - [2️⃣ Setup screen and draw a circle (the “ball”)](#2️⃣-setup-screen-and-draw-a-circle-the-ball)
    - [📖 The flip-book simulator…](#-the-flip-book-simulator)
    - [3️⃣ Let’s move the ball higher up! 🔼](#3️⃣-lets-move-the-ball-higher-up-)
    - [4️⃣  Make the ball fall like magic 🔽](#4️⃣--make-the-ball-fall-like-magic-)
  - [Tutorial Overview](#tutorial-overview)
  - [Phase 1: The Basics](#phase-1-the-basics)
    - [Step 0: Setup VSCode and the code](#step-0-setup-vscode-and-the-code)
    - [Step 1: Set up the screen and draw a ball](#step-1-set-up-the-screen-and-draw-a-ball)
    - [The flip-book simulation](#the-flip-book-simulation)
      - [Drawing a ball in the screen](#drawing-a-ball-in-the-screen)
    - [Step 2: Move the ball higher up](#step-2-move-the-ball-higher-up)
    - [Step 3: Make the ball fall at constant speed](#step-3-make-the-ball-fall-at-constant-speed)
    - [Step 4: Add a floor](#step-4-add-a-floor)
      - [Detect collision with the floor](#detect-collision-with-the-floor)
    - [CONGRATULATIONS! 🎆](#congratulations-)
  - [Phase 2: Advanced features](#phase-2-advanced-features)
    - [Step 5: Add gravity as acceleration](#step-5-add-gravity-as-acceleration)
    - [Step 6: Make the ball bounce (no energy loss)](#step-6-make-the-ball-bounce-no-energy-loss)
    - [Step 7: Add energy loss when bouncing](#step-7-add-energy-loss-when-bouncing)
    - [CONGRATULATIONS! 🎆](#congratulations--1)
  - [Phase 3: Look \& Feel](#phase-3-look--feel)
    - [Step 8: Change circle to an image, add floor/background](#step-8-change-circle-to-an-image-add-floorbackground)
    - [Step 9: Add music](#step-9-add-music)
    - [CONGRATULATIONS! 🎆](#congratulations--2)
  - [Phase 4: Super Extensions](#phase-4-super-extensions)
    - [Step 10: Use Pygame's built-in collision detection](#step-10-use-pygames-built-in-collision-detection)
    - [Step 11: More accurate bouncing](#step-11-more-accurate-bouncing)
  - [CONTRIBUTORS](#contributors)

## Setup and Requirements

This tutorial requires the following software:

- Python 3.10+
- [pygame](https://www.pygame.org/wiki/about) library
- [VSCode](https://code.visualstudio.com/) as the IDE

The linked [Installation](INSTALL.md) instructions install these requirements for Windows and Mac.

## Part I: Tutorial Overview

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

### 📖 The flip-book simulator…

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















































## Tutorial Overview

In this tutorial, we’ll use code to control what appears on the screen. Coding is how we give instructions to a computer using a programming language—in this case, Python.

Python is popular because it’s easy to read (its code looks a bit like plain English!) and very versatile. It’s used by companies like Google, Netflix, Spotify, and NASA, and across many fields including web development, data science, automation, scientific research, game design, and healthcare—for tasks such as predictive analytics and image analysis.

It’s a great choice for beginners, while still being powerful enough for building complex projects. 👍

In this tutorial, we’ll **simulate a ball falling and bouncing off the ground** ⚽ 🔽. Along the way, you’ll learn how to position the ball, update its movement as it falls, and even add gravity so it loses energy with each bounce.

As you progress, you’ll explore **key programming concepts** such as sequential steps, variables, functions, loops, and if-statements. These are essential building blocks that can be used to create a wide range of exciting projects.

We’ll write **instructions using functions—named blocks of code** that perform specific tasks, like moving the ball or drawing on the screen. Many useful functions are already available in Python and its libraries. Functions can take inputs called variables, which are like labelled boxes that store information we can use or update.

Instead of writing everything from scratch, we can also use _libraries_, which are collections of code created by others that we can reuse in our own programs. One such library is **Pygame**, which makes it easy to draw graphics and build interactive projects like animations and simple games. 🎮

The tutorial is **organised into 10 steps** 🦶, with each step introducing a new idea and showing how code can be used to model motion and animate our virtual ball. To get started, we’ve provided an **initial code template** for you to work on. **Let’s do it!**


In this tutorial, we will simulate a **ball falling and bouncing off the ground** ⚽ 🔽 We will learn how to position the ball, adjust its motion when falling, and even include gravity and make it lose energy with each bounce. As you go, you will learn how to use basic programming ideas like sequential steps, variables, functions, loops, and if-statements. These are building blocks that can be used to make a wide range of exciting projects.

We will write instructions using functions (many already provided by Python and its library), which are named blocks of code that do something—like moving the ball or drawing on the screen. Functions can take variables as input, which are like labelled boxes that store information we want to use or change. Rather than writing everything from scratch, we can also use libraries—collections of functions written by others that we can bring into our own project. Pygame is one such library. It makes it easy to draw on the screen and build interactive projects like animations and simple games.

The tutorial is organised into **10 steps** 🦶. Each step adds a new idea and shows how we can use code to describe motion and animate the virtual ball.

The system uses Python and [pygame](http://www.pygame.org/wiki/about), a toolkit to write games. 🎮

We have already provided an initial code template in file [fall.py](fall.py). You need to copy-and-paste the contents of this file into your own VSCode folder.

## Phase 1: The Basics

### Step 0: Setup VSCode and the code

To get started with this tutorial, you will need to use VSCode, and get the starting Python code file. To get underway:

1. Open VSCode.
2. Create a new folder where you want your project to be, for example, folder `falling-ball`.
3. Download the file `fall.py` file to your project folder. This can be done by using the download button at the top right corner in the file in GitHub:

    ![download in GH](assets/gh-download.png)

    - Alternatively, you create an empty file [`fall.py`](https://raw.githubusercontent.com/outreach-csit/falling-ball-public/refs/heads/main/fall.py?token=GHSAT0AAAAAAC5GJNQPCTNCQHAGILHIVDE2Z7SGBWA) with VSCode in your project and then do copy-and-paste; GitHub has s button to copy the file contents into memory:
4. Save the file.

All ready, it is time to run the code. You can do that by clinking the **PLAY** triangle button in the top-right corner of the VSCode window:

![run](assets/vscode-run.png)

You should see the following window, with a ball (or it is a sun? 🌞) in the center of the stage:

![initial](assets/step_00-initial-screen.png)

### Step 1: Set up the screen and draw a ball

In the first step, we just want to **understand** the code we were given. Having a good understanding of each piece will be important to know how to modify it later on... 😉

In Pygame—and in most libraries designed for drawing or graphics—the screen is like a piece of graph paper. In fact, as you learnt in school, the window created is a **Cartesian plane**, as you learnt in school! As the window is a 2D plane, we refer to a particular point (or location) in it using the `x` and `y` coordinate system. A point is called a "pixel", and we can set each pixel to different colors.

- The top-left corner is `(0, 0)`.
- Moving to the right increases the `x` coordinate. Moving down increases `y`.
- So point `(100, 100)` means 100 pixels across and 100 pixels down.

Let us understand the skeleton code before modifying it. 👀

The first two lines tell Python to load and initialize the `pygame` library for building graphical applications and games, and the next two instructions create a clock that will be used to tell Pygame to re-draw the screen at 60 frames/seconds.

```python
import pygame  # Import the Pygame library
pygame.init()  # Set up Pygame

# Set up consistent frame rate
clock = pygame.time.Clock()
FPS = 60  # Frames per second – how often the screen updates
```

> [!NOTE]
> In the code, you'll see lines that start with a `#` symbol — these are **comments**. They're not run by the computer. Comments are used to explain what each part of the code does, which makes it easier to read later (by others and you in the future!). Always leave comments in your code.

Next, the following code defines the application screen. It will create a display screen of size `1200` (width) by `800` (length) and set its title too:

```python
# Set up the screen
WIDTH = 1200
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the screen window
pygame.display.set_caption('Falling Ball Simulation :)')  # Window title
```

Here, `WIDTH` and `HEIGHT` are the **variables** storing the size of the window we want to create.

The variable `SCREEN` is the most important one here: it refers to the whole Pygame screen window and we will use it to draw things on it!

> **QUESTION*: Remember we said that point `(0, 0)` is the top-left one in the screen? Well, our right-bottom pixel will then be `(1199, 799)`. _What would the middle of the screen window be?_

Next, we define three **variables** that define the size of the ball we want to draw, and its initial location in the center of the screen:

```python
# Ball properties
ball_radius = 50  # size of the ball
ball_x = WIDTH // 2  # initial x position of the ball
ball_y = HEIGHT // 2  # initial y position of the ball
```

### The flip-book simulation

A **simulation** works like a “[flip-book](https://en.wikipedia.org/wiki/Flip_book)”: it displays many images one after another, very quickly. Each image represents a small step—for example, the ball moving just a tiny bit.

In practice, a simulation repeatedly goes through three phases:

1. Check if the user has closed the window. If so, stop the simulation.
2. Update the state of the simulation (e.g., move the ball).
3. Redraw the screen with the updated state.

This repetition is implemented by a `while` loop, that will execute a given piece of code until the simulation is not running anymore. To store whether the simulation is running, we make use a boolean variable `simulation_running`, which is initially `True` and made `False` when the user closes the window. This is how the simulation-cycle looks like:

```python
# Main game loop
simulation_running = True  # keep running?
while simulation_running:
    # 1. if window is closed; set simulation_running = False
    ...

    # 2. Update simulation configuration: ball position, velocity, etc.
    ...

    # 3. Draw the stage: background, ball, etc
    ...
```

We have not shown the code for the first step, it is not that interesting. Basically, it will set  variable `simulation_runnning` to False, which will cuase the `while` look to terminate, and the whole program finishes: there is nothing left in th program to execute...

In the second step, which we will explain below, the simulation **does all the updates in the `SCREEN` for the cycle**, for example, changing the position of the ball, setting its (new) color, changing the background color or picture, etc.

The final step in each simulation cycle is to **re-draw and update the screen**, that is, to draw the "new picture" with the changes just done in step 2! ✏️

#### Drawing a ball in the screen

Let us look at the second step in the simulation cycle. The initial code does two things:

1. Paint the screen yellow, to represent the background.
2. Draw a blue circle in the middle of the screen to represent the ball.

Both steps are changes to the simulation screen, which is always stored in variable `SCREEN` created at the very start as we explained above. So here is the code for those two instructions:

```python
SCREEN.fill("yellow")  # Fill the screen with a sky blue background
pygame.draw.circle(SCREEN, "blue", (ball_x, ball_y), ball_radius)  # Draw the ball
```

The first command "fills" the `SCREEN` with `yellow` color, while the second one draws a circle with the following information:

- `SCREEN` is where we want the circle to be drawn, namely, in the window of the simulation.
- `blue` is the colour we want the ball to be inside.
- `(ball_x, ball_y)` gives the position.
- `ball_radius` is the size of the ball.

In this case, `pygame` is the library, `draw` is the module inside it, and `circle` is the **function** that does the actual drawing. All is provided by the library we imported at the top!

> [!IMPORTANT]
> Observe that some things are written in quotes, like, `"blue"`. These are **strings**, that is, data that is not a number, "textual data". If we just write `blue`, Python will think it is a variable called like that! In programming, we use strings to store and work with words, sentences, or any other kind of _text_. You can also manipulate them — like combining strings, cutting parts out, changing letters, or checking if certain words are inside.

If you're using VS Code, you can hover over the function name to see what inputs it takes. Or you can search online—typing something like “pygame draw circle” into your browser will often give you clear documentation and examples. You can also use the interactive Python shell to explore help functions if you're comfortable doing so.

> **QUESTION**: what would happen if we swap the instructions, and we first draw the ball and then fill the background? Try it!

### Step 2: Move the ball higher up

Time to implement some of _our_ changes!

In this step, you are to:

1. Change the background of the simulation to whatever color you prefer. 🖌️ Most obvious colors will be accepted, but there are many more Pygame knows about [here](https://www.pygame.org/docs/ref/color_list.html).
2. Put the ball higher up in the screen. You can do that by changing the variable that holds the `y` coordinate of the ball. 😉 Put the ball up in the screen so that it has "space" to fall, but is all visible. _What number would you use?_Remember that `(0, 0)` is not the middle of the screen, but the top-left corner.

Go ahead and set the initial simulation step as you wish! 🖐️

### Step 3: Make the ball fall at constant speed

Now let us **add motion to the ball** so it falls down at a constant speed. 🔽 ⚽ 🔽

The way to implement that is to update, in every simulation cycle, the position of the ball a bit down. Remember that the lower part of the screen has higher `y` values, as the very top has `y = 0`.

So, each time the loop runs (which happens 60 times per second), we will update the ball `y` coordinate by adding a some small amount. For example, to move it three pixes per simulation step (one cycle), we can write:

```python
ball_y = ball_y + 3
```

In programming, this instruction is called an "**assignment**", as we are assigning the value at the right of the `=` symbol to the variable on the left side of the symbol `=`. In English, it says: _"set to variable `ball_y` to hold the value `ball_y + 3`"_ Python will first calculate the right hand side expression (`ball_y + 3` in our case), and then assign it to teh variable on the left (`ball_y`).

> [!WARNING]
> Variables can only hold one value at a time, so when you assign a value to a variable, the old value is "lost". If you want to keep it, for some reason, you would need to first store it in another variable; for example:

```python
old_ball_y = ball_y # save the current value
ball_y = ball_y + 3
```

> [!TIP]
> Many times, an assignment is about  add or subtract an amount to the existing value of a variable. This is what we did above. In those cases, there is a shortcut, namely:  `ball_y += 3` and `ball_y -= 3`.

Now go ahead and implement the change. Be careful to do the change before the draw is drawn and inside the simulation loop (in the second phase). By updating `ball_y` by a small amount

To try this, add `ball_y += 3` just below the `# Move` line in your code. When you run it, the ball should now fall downward at a constant speed. 👍

### Step 4: Add a floor

Wow, _how come the ball keeps going down and disappears out of the screen?_ What happens when `ball_y` becomes larger than the value of `HEIGHT` (800 in our case)?

The fact is that, at the moment, the ball just keeps falling because there is nothing telling it to stop.

To make the simulation more realistic, let us add a **floor and stop the ball once it hits it** 🛑.

First, we define some new constants, somewhere before the simulation loop:

```python
FLOOR_HEIGHT = 100
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
```

This means the floor is 100 pixels high, and it starts at the bottom of the screen. Make sure to include good comments to your new code 😉

Then, just below the `pygame.draw.circle` line, we draw a rectangle to show the floor:

```python
pygame.draw.rect(SCREEN, "black", (0, FLOOR_Y, WIDTH, HEIGHT))
```

**Try it!**

#### Detect collision with the floor

We have the floor, but the ball keeps going through it! 😕 Remember, for the computer these are just colors.

We want the door to stop short when it hits the floor, right? What does that mean in the code? Well, when the ball `y` position is the same (or more?) as the start of the floor....

When the ball is at the floor, we simply stop the ball to be _at_ the floor. This means that the code to move the ball down that we did above, only has to run if the ball is not touching the floor.

To execute a particular code based on a particular condition, we use the `if` construct. Let us change the update of the code we did to check whether the bottom of the ball has passed the top of the floor. Only if it hasn’t (`not`), we keep it falling:

```python
if not (ball_y) > FLOOR_Y:
    ball_y += 3
```

Try it! Does it work? If not exactly as you would expect, _why?_ What does the coordinate `(ball_x, ball_y)` represent exactly? What place in the ball? Think how you can fix it by slightly fixing teh condition in the `if`-conditional.

### CONGRATULATIONS! 🎆

Well done! 👏 👏 You’ve got the core part of a simulation. You have:

- Installed your development environment to be able to code and run!
- Used coordinate systems in the Cartesian plane.
- Implemented (fixed) velocity as a change of position.
- Used conditional logic (if statements).
- Used repetition/loop logic (simulation loop).
- Used arithmetic expressions and logical conditions to model the ball dynamics.
- Implemented collision detection with the floor.

Feel free to experiment with different sizes, speeds, colours, or even make your own version!

## Phase 2: Advanced features

### Step 5: Add gravity as acceleration

In real life, gravity speeds things up as they fall. We can copy that by gradually increasing the ball’s speed every frame.

There are actually three concepts in classical dynamics:

1. **Position:** where an object is. In our case, the ball is, at any point in time, at a coordinate `(x, y)`
2. **Velocity:** the rate of change of the position, like km/h in a car. In our case, the vertical velocity of our ball above is how many pixels the ball drops per simulation cycle (3 pixels/cycle).
3. **Accelleration:** the rate of change of the velocity, like the gravitational acceleration of 9.834 m/s2. In our case, we want the ball to fall faster and faster as it approaches the floor, thus simulating the gravitational force.

In order to implement gravitational acceleration on the ball, we first need to change the fix velocity of 3 pixels/cycle implemented above so that it can change as the simulation runs. To do so, first replace the `3` with a variable called `ball_vel` which should be 0 at the start:

```python
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_velocity = 0   # current velocity of the ball
```

Then, we need to update the `y`-position of the ball to increment by the current velocity of the ball:

```python
ball_y += ball_velocity
```

Next, define a constant (a variable that never changes, usually written full capital letters)  `GRAVITY` and set it to, say, 0.50 pixels/cycle:

```python
GRAVITY = 0.50
```

Finally, similarly to the update of the ball location (by its velocity), add code to change the velocity of the ball by the gravity value. You r code should look like this (but think carefully where you will place it 🤔):

```python
# apply gravity
ball_velocity += GRAVITY
```

Now, _what should the velocity when the ball does hit the floor?_ Check the code already done for recognising the coalition to the floor, and when there is a collision, reset its velocity. You can use the `else` in the `if` condition:

```python
    if not (......) > FLOOR_Y:
        ball_y += ball_velocity
    else:
        ball_velocity = ...
```

Now when you Run the file the ball should fall faster and faster and then stop when it hits the floor... 🏀

### Step 6: Make the ball bounce (no energy loss)

We are doing great, but surely a ball doesn't get stuck in the floor at the first collision, at least not a soccer ⚽ or basketball 🏀 ball!

Think about it. What happens with the ball's velocity if the ball is meant to _bounce_? Should you keep adding to the ball's `y`-coordinate or should you start subtracting instead?

The thing is that the velocity of the ball changes direction when it bounces, as the ball will go up (lower `y`-values). And, in general, it will keep its magnitude. So, if the velocity was 5 pixels/cycle, it should not be -5/cycle, right?

So, instead of fixing the velocity to zero and stop the motion, change its sign:

```python
ball_velocity = ball_velocity * -1 # Reverse the velocity
```

The ball now bounces back up with the same speed it had when falling.

### Step 7: Add energy loss when bouncing

In real life, each bounce loses a bit of energy (due to friction), say 10%. We can copy that by reducing the velocity a little each time the ball hits the floor.

First we need to define an energy loss constant:

```python
ENERGY_LOSS = 0.1
```

Then we refine how the velocity changes when bouncing, by keeping `(1- ENERGY_LOSS)` of it:

```python
ball_velocity = (ball_velocity * -1)
ball_velocity = ball_velocity * (1 - ENERGY_LOSS)
```

Now when you run the code, the ball will bounce lower and lower each time, eventually settling.

> [!WARNING]
> Why does the ball never stops? See that 90% of something very small, is always something great than zero. We can say that if the velocity is very small when it bounces, say less than 4 pixels/cycle (you may need to find your value here!), then we fix it to zero. Use another `if` (inside the `else` to do this).

### CONGRATULATIONS! 🎆

Well done! 👏 👏 You’ve implemented some more realistic features into your simulation. You have:

- Abstracted the fixed velocity to a variable. This is necessary if we ever want to change the velocity of the ball!
- Implemented gravity as acceleration on the ball: change of velocity.
- Simulated the bounce of the ball by using integers and multiplication by -1.
- Implemented loss of energy when bouncing, using notions of percentage and multiplications with a number between 0 and 1.

The actual simulator is finished. In the following, we will make it look "nicer".

## Phase 3: Look & Feel

### Step 8: Change circle to an image, add floor/background

Time to make our simulation more "realistic", by replacing the circle with a actual image of a ball, and add a background. For this, we need to load another Python package at the very top of the file:

```python
import os
```

This helps us find and load files stored in folders.

Right after setting up the screen, add the following code to load the ball and background images:

```python
# load assets
ball_img = pygame.image.load(os.path.join("assets", "soccerball.png"))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "basketball-netball-court.png")), (WIDTH, HEIGHT))
```

To work with the new images, we will also increase the floor height so the ball can bounce higher and look right against the background:

```python
FLOOR_HEIGHT = 200  # Adjusted to suit the background image
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
```

Instead of drawing a circle to represent the ball, we can now blit an its image loaded (in variable `ball_img`) as follows:

```python
SCREEN.blit(ball_img, (ball_x, ball_y))
```

Similary, we can blit the background image (`back_img` variable) at the origin coordinate `(0, 0)` of the simulation screen so that it fits the whole screen.

> [!IMPORTANT]
> THink carefully the order of drawing, so that all background and ball are seen as wanted.

This will make the ball look like a soccer ball and add a themed background.

### Step 9: Add music

In this step we will add sounds and music. We will include background music and a bounce sound effect each time the ball hits the floor.

First, we need to import Pygame’s mixer system, which lets us play audio:

```python
import pygame
from pygame import mixer
import os
pygame.init()
mixer.init()
```

Next we load the music and sound files, by adding this two variables just after setting up the clock and frame rate:

```python
clock = pygame.time.Clock()
FPS = 60

# music
bounce_sound = pygame.mixer.Sound(os.path.join("sound", "bounce.wav")) #define bounce as the sound in the file bounce.wav
back_sound = pygame.mixer.Sound(os.path.join("sound", "back.mp3")) #define the background music
```

We can start playing the background sound anywhere before the simulation loop starts (the -1 option tells Pygame to repeat the track):

```python
back_sound.play(-1) # play background music on loop
```

The bouncing should only be added when the ball bounces:

```python
bounce_sound.play()
```

:fl

> [!WARNING]
> Make sure the bouncing sound is only when it truly bounces, that is, when the ball will start  traveling upwards. ⏫

### CONGRATULATIONS! 🎆

Amazing! 👏 👏 You’ve now built a full animation using Python, and it lokos great! You have:

- Loaded images and audio files into variables.
- Use images to represent the ball (rather than the circle), and the background (rather than a flat color).
- Play sounds, both in the background and at bouncing using `if` conditional.

Feel free to experiment with different sizes, speeds, colours, or even make your own version!

## Phase 4: Super Extensions

### Step 10: Use Pygame's built-in collision detection

If you want to go a bit further, Pygame has built-in tools to detect when objects bump into each other—this is called collision detection. Pygame uses something called a `Rect` (short for rectangle) to represent the position and size of things on the screen.

We can create a rectangle around the ball and check if it overlaps with another rectangle (like the floor).

The rectangles for the ball and floor need to be defined in the `variables` code block

```python
# variables

run = True
ball_x = WIDTH // 2 - ball_img.get_width() // 2
ball_y = 100
ball_velocity = 0
ball_rect = pygame.Rect(ball_x, ball_y, ball_img.get_width(), ball_img.get_height())
floor_rect = pygame.Rect(0, FLOOR_Y, WIDTH, FLOOR_HEIGHT)
```

Then in the main game loop, we check if the rectangle representing the ball has collided with the rectangle representing the floor, if not we update the velocity of the ball. Otherwise we reflect the balls velocity and add energy loss. We need to then reset the rectangle representing the ball to be analogous with the balls new position. The main game loop then looks like:

```python
# main game loop

while run:

    # loop through all events
    for event in pygame.event.get():

        # if the X / close button is pressed then exit the loop
        if event.type == pygame.QUIT:
            run = False

    # draw

    SCREEN.blit(back_img, (0, 0))
    SCREEN.blit(ball_img, (ball_x, ball_y))
   
    # move
   
    if not pygame.Rect.colliderect(ball_rect, floor_rect):
        ball_y += ball_velocity
       
    else:
        ball_y = FLOOR_Y - ball_img.get_height()
        ball_velocity = (ball_velocity * -1) + ENERGY_LOSS

        if not (ball_velocity >  -3 and ball_velocity < 3):
            bounce.play()
```

This is a more advanced technique, but it's useful if you want to check collisions between different objects—like bouncing off walls, hitting targets, or building a game.

### Step 11: More accurate bouncing

TODO

## CONTRIBUTORS

- Prof. [Sebastian Sardina](https://github.com/ssardina) (contact: sebastian.sardina@rmit.edu.au)
- Mr. [Marcos Sardina](https://github.com/msardina) (original Scratch project and first translation to Python)
- Dr. [Timothy Wiley](https://github.com/timothy-wiley)
- Dr. [Irina Grossman](https://github.com/irigrossman?tab=repositories)
