
from ColabTurtlePlus.Turtle import *
import numpy as np

# ============ TILE FUNCTIONS ============

# Function definition for person 1 here  Tyranny White
# Insert your name in the function name.
# Do not change anything else yet!
def draw_tyranny_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["secondary"])
      t.pensize(3)
      t.forward(quarter)
      t.right(90)
      t.forward(quarter)
      t.left(180)

      t.pendown()
      t.forward(half)
      t.left(90)
      t.forward(half)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter + quarter / 2)
      t.left(90)
      t.forward(quarter)

      t.pendown()
      t.begin_fill()
      t.circle(quarter / 2)
      t.end_fill()
      t.left(90)
      t.forward(quarter / 2)
      t.color(palette["accent"])
      t.dot(quarter / 4)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.color(palette["primary"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 45)
      t.forward(quarter * 1.2)
      t.left(90)
      t.forward(quarter * 1.2)
      t.pendown()
      for i in range(4):
          t.left(90)
          t.forward(half * 1.2)
      t.left(45)
      t.penup()

      t.forward(half * 0.9)

      t.color(palette["accent"])
      t.pendown()
      for i in range(5):
        t.left(144)
        t.forward(half * 0.2)
      t.penup()


      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 60)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.forward(quarter * 1.4)
            t.left(120)
        t.end_fill()
        t.penup()
        t.left(90)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(2)

      for _ in range(8):
          t.pendown()
          t.forward(quarter * 0.9)
          t.penup()
          t.jumpto(x, y)
          t.right(45)

 #border
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go 2 corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

# Function definition for person 2 here Nayonika Karia

# Insert your name in the function name.
# Do not change anything else yet!
def draw_nayonika_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["accent"])
      t.pensize(5)
      t.forward(quarter)
      t.right(30)
      t.forward(quarter)
      t.left(170)

      t.pendown()
      t.forward(half)
      t.left(80)
      t.forward(half)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter + quarter / 3)
      t.left(90)
      t.forward(quarter)

      t.pendown()
      t.begin_fill()
      t.circle(quarter / 2)
      t.end_fill()
      t.left(90)
      t.forward(quarter / 2)
      t.color(palette["secondary"])
      t.dot(quarter / 4)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.color(palette["primary"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(1):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 15)
      t.forward(quarter * 1.25)
      t.left(40)
      t.forward(quarter * 0.35)
      t.pendown()
      for i in range(7):
          t.left(120)
          t.forward(half * 1.4)
      t.left(95)
      t.penup()

      t.forward(half * 1.1)

      t.color(palette["accent"])
      t.pendown()
      for i in range(5):
        t.left(110)
        t.forward(half * 0.29)
      t.penup()


      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 20)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.forward(quarter * 0.7)
            t.left(20)
        t.end_fill()
        t.penup()
        t.left(90)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(1)

      for _ in range(8):
          t.pendown()
          t.forward(quarter * 0.7)
          t.penup()
          t.jumpto(x, y)
          t.right(15)


  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

# Function for person 3: Ani
def draw_ani_tile(t, x, y, size, rotation, palette, tile_type="center"):
    """
    Draws a parameterized geometric tile centered at (x, y).
    Corner: concentric quarter arcs and a diamond. Border: row of triangles
    with a dotted line. Center: diamond, hexagon, ring and rays.
    """
    # TURTLE SETUP
    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)

    half = size / 2
    quarter = size / 4

    # BASE BACKGROUND
    t.forward(-half)
    t.left(90)
    t.forward(-half)
    t.right(90)

    t.pencolor(palette["bg"])
    t.fillcolor(palette["bg"])
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()

    t.jumpto(x, y)
    t.setheading(rotation)

    # Helper: move in the tile's rotated frame (dx along heading, dy to its left)
    def go(dx, dy, extra_turn=0):
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(dx)
        t.left(90)
        t.forward(dy)
        t.right(90)
        t.setheading(rotation + extra_turn)

    # Helper: regular polygon from the current position and heading
    def shape(sides, length, line_col, fill_col):
        t.color(line_col, fill_col)
        t.pendown()
        t.begin_fill()
        for _ in range(sides):
            t.forward(length)
            t.left(360 / sides)
        t.end_fill()
        t.penup()

    if tile_type == "corner":
        t.pensize(4)
        arc_colors = [palette["accent"], palette["secondary"], palette["primary"]]
        for r, col in zip((half * 0.9, half * 0.65, half * 0.4), arc_colors):
            go(-half, -half)
            t.forward(r)
            t.left(90)
            t.pencolor(col)
            t.pendown()
            t.circle(r, 90)
            t.penup()

        side = quarter * 0.8
        go(quarter, quarter - side * 0.7071, 45)
        t.pensize(2)
        shape(4, side, palette["accent"], palette["primary"])

        go(quarter, quarter)
        t.color(palette["secondary"])
        t.dot(quarter / 3)

    elif tile_type == "border":
        t.pensize(2)
        for i in range(4):
            go(-half + i * quarter, -half)
            col = palette["primary"] if i % 2 == 0 else palette["secondary"]
            shape(3, quarter, palette["accent"], col)

        for i in range(8):
            go(-half + size / 16 + i * size / 8, quarter * 0.3)
            t.dot(size / 25, palette["accent"])

        t.pencolor(palette["accent"])
        t.pensize(3)
        go(-half, quarter * 1.4)
        t.pendown()
        t.forward(size)
        t.penup()

    else:
        reach = half * 0.85
        t.pensize(3)
        go(0, -reach, 45)
        shape(4, reach * 1.4142, palette["accent"], palette["primary"])

        r = quarter * 1.1
        go(-r / 2, -r * 0.866)
        t.pensize(2)
        shape(6, r, palette["accent"], palette["secondary"])

        go(0, -quarter * 0.55)
        t.pensize(3)
        t.color(palette["accent"], palette["primary"])
        t.pendown()
        t.begin_fill()
        t.circle(quarter * 0.55)
        t.end_fill()
        t.penup()

        t.pencolor(palette["accent"])
        t.pensize(2)
        for i in range(8):
            go(0, 0, i * 45 + 22.5)
            t.forward(quarter * 1.2)
            t.pendown()
            t.forward(quarter * 0.45)
            t.penup()

        go(0, 0)
        t.dot(quarter / 3, palette["bg"])

    # DOUBLE FRAME
    def square(side):
        t.pendown()
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.penup()

    t.pencolor(palette["secondary"])
    t.pensize(3)
    go(-half, -half)
    square(size)

    inset = size * 0.05
    t.pencolor(palette["accent"])
    t.pensize(1)
    go(-half + inset, -half + inset)
    square(size - 2 * inset)

    # TURTLE TEARDOWN
    t.penup()
    t.setheading(0)
    t.pencolor((0, 0, 0))


tile_functions = [draw_tyranny_tile, draw_nayonika_tile, draw_ani_tile]

# palettes
palette_options = {}

ani_palette = {
    "bg": (232, 231, 122),
    "primary": (246, 54, 138),
    "secondary": (140, 116, 242),
    "accent": (85, 196, 255),
}
palette_options["pistachio red pink"] = ani_palette

nayonika_palette = {
    "bg": (206, 230, 182),
    "primary": (236, 64, 138),
    "secondary": (130, 114, 222),
    "accent": (255, 196, 218),
}
palette_options["pistachio"] = nayonika_palette

tyranny_palette = {
    "bg": (15, 12, 50),
    "primary": (255, 0, 110),
    "secondary": (0, 200, 123),
    "accent": (120, 245, 212),
}
palette_options["cashew"] = tyranny_palette


#  palette names

palette_names = list(palette_options)
palette_names.append("random")
print(f"These are the available palettes: {palette_names}")


# user input
title_text = input("Name your poster!")
while len(title_text) == 0 or len(title_text) > 40:
  if len(title_text) == 0:
    print("Write something!")
  else:
    print("Too long! Keep it under 40 characters :)")
  title_text = input("Name your poster!")

nrows = int(input("Grid height: "))
while nrows < 3 or nrows > 8:
  print("Should be between 3 and 8!")
  nrows = int(input("Grid height: "))

ncols = int(input("Grid width: "))
while ncols < 3 or ncols > 8:
  print("Should be between 3 and 8!")
  ncols = int(input("Grid width: "))

p_name = input("Write the palette you want!").lower()

while p_name not in palette_names:
  print(f"That doesn't exist! Choose from: {palette_names}.")
  p_name = input("Write the palette you want!").lower()

print(f"Good choice choosing {p_name} palette!")


# random selection palette
if p_name == "random":
  print("Generating your very own random palette!")
  palette = {}
  for key in ["bg", "primary", "secondary", "accent"]:
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    palette[key] = (int(r), int(g), int(b))
else:
  palette = palette_options[p_name]

print("Your poster is coming soon! Get excited!")


# draw + setup
clearscreen()
setup(1000, 700)
t = Turtle()
t.speed(0)

# Tile size so the grid fits in a 900 x 440 area at the top of the screen
size = min(900 / ncols, 440 / nrows)

y_offset = 330 - size / 2
x_offset = -size * (ncols - 1) / 2

for row in range(nrows):
  y = y_offset - size * row

  for col in range(ncols):
    x = x_offset + size * col

    # Randomly choose which person's tile to draw
    F = tile_functions[np.random.randint(len(tile_functions))]

    if row == 0:
      if col == 0:
        tile_type = "corner"     # upper left
        rotation = 270
      elif col == ncols - 1:
        tile_type = "corner"     # upper right
        rotation = 180
      else:
        tile_type = "border"     # horizontal
        rotation = np.random.randint(2) * 180
    elif row == nrows - 1:
      if col == 0:
        tile_type = "corner"     # lower left
        rotation = 0
      elif col == ncols - 1:
        tile_type = "corner"     # lower right
        rotation = 90
      else:
        tile_type = "border"     # horizontal
        rotation = np.random.randint(2) * 180
    else:
      if col == 0 or col == ncols - 1:
        tile_type = "border"     # vertical
        rotation = 90 + np.random.randint(2) * 180
      else:
        tile_type = "center"
        rotation = np.random.randint(4) * 90

    F(t, x, y, size, int(rotation), palette, tile_type)

# title, creds
t.jumpto(0, -170)
t.write(title_text, align="center", font=(20, "Arial", "bold"))
t.setheading(270)
t.forward(30)
t.write("By Tyranny, Nayonika, Ani, and Alex!", align="center", font=(14, "Arial", "normal"))

# palette draw
t.jumpto(-245, -290)
for v in palette.values():
  t.color(v, v)
  t.setheading(90)
  t.pendown()

  # Draw rectangle.
  t.begin_fill()
  t.forward(40)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(40)
  t.right(90)
  t.forward(100)
  t.end_fill()

  t.penup()
  t.right(180)
  t.forward(50)
  t.right(90)
  t.forward(20)
  # Write the RGB values
  t.pencolor((0, 0, 0))
  t.write(f"RGB {v}", align="center")
  t.setheading(0)
  t.forward(80)
  t.left(90)
  t.forward(20)

t.hideturtle()
t.done()
def draw_alex_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(quarter)
      t.right(90)
      t.forward(quarter)
      t.left(180)

      t.pendown()
      t.forward(half)
      t.left(90)
      t.forward(half)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter + quarter / 2)
      t.left(90)
      t.forward(quarter)

      t.pendown()
      t.begin_fill()
      t.circle(quarter / 2)
      t.end_fill()
      t.left(90)
      t.forward(quarter / 2)
      t.color(palette["secondary"])
      t.dot(quarter / 4)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.color(palette["primary"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 45)
      t.forward(quarter * 1.2)
      t.left(90)
      t.forward(quarter * 1.2)
      t.pendown()
      for i in range(4):
          t.left(90)
          t.forward(half * 1.2)
      t.left(45)
      t.penup()

      t.forward(half * 0.9)

      t.color(palette["accent"])
      t.pendown()
      for i in range(5):
        t.left(144)
        t.forward(half * 0.2)
      t.penup()


      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 60)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.forward(quarter * 1.4)
            t.left(120)
        t.end_fill()
        t.penup()
        t.left(90)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(2)

      for _ in range(8):
          t.pendown()
          t.forward(quarter * 0.9)
          t.penup()
          t.jumpto(x, y)
          t.right(45)




  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

tile_functions = [draw_alex_tile,draw_tyranny_tile,draw_nayonika_tile,draw_tile]

ani_palette = {
    "bg": (232, 231, 122),
    "primary": (246, 54, 138),
    "secondary": (140, 116, 242),
    "accent": (85, 196, 255),
}

palette_options["pistachio red pink"] = ani_palette
nayonika_palette = {
       "bg": (206, 230, 182),
        "primary": (236, 64, 138),
        "secondary": (130, 114, 222),
        "accent": (255, 196, 218)
    }
palette_options["pistachio"] = nayonika_palette
tyranny_palette = {
        "bg": (15, 12, 50),
        "primary": (255, 0, 110),
        "secondary": (0, 200, 123),
        "accent": (120, 245, 212)
    }

palette_options["cashew"] = tyranny_palette
alex_palette = {
    "bg": (229, 222, 210),
    "primary": (38, 144, 227),
    "secondary": (163, 92, 159),
    "accent": (98, 161, 183)
}

palette_options["beach"] = alex_palette

palette_options = {}

saveSVG("/content/poster.svg")
