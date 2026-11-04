def draw_tile(t, x, y, size, rotation, palette, tile_type="center"):


    # ==========================================
    # TURTLE SETUP
    # ==========================================
    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)

    half = size / 2
    quarter = size / 4

    # ==========================================
    # BASE BACKGROUND
    # ==========================================
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

    ######################### YOUR CHANGES START HERE ###########################

    # Helpers: move in the tile's rotated frame (dx along heading, dy to its left)
    def go(dx, dy, extra_turn=0):
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(dx)
        t.left(90)
        t.forward(dy)
        t.right(90)
        t.setheading(rotation + extra_turn)

    # Regular polygon starting at the current position/heading
    def shape(sides, length, line_col, fill_col):
        t.color(line_col, fill_col)
        t.pendown()
        t.begin_fill()
        for _ in range(sides):
            t.forward(length)
            t.left(360 / sides)
        t.end_fill()
        t.penup()

    # ==========================================
    # CONDITIONAL GEOMETRY (Based on tile_type)
    # ==========================================

    # ------------------------------------------
    # OPTION 1: CORNER TILE
    # Concentric quarter-circle arcs + diamond with a dot
    # ------------------------------------------
    if tile_type == "corner":
        t.pensize(4)
        arc_colors = [palette["accent"], palette["secondary"], palette["primary"]]
        for r, col in zip((half * 0.9, half * 0.65, half * 0.4), arc_colors):
            go(-half, -half)          # bottom-left corner
            t.forward(r)
            t.left(90)
            t.pencolor(col)
            t.pendown()
            t.circle(r, 90)
            t.penup()

        # diamond in the opposite corner
        side = quarter * 0.8
        go(quarter, quarter - side * 0.7071, 45)
        t.pensize(2)
        shape(4, side, palette["accent"], palette["primary"])

        go(quarter, quarter)
        t.color(palette["secondary"])
        t.dot(quarter / 3)

    # ------------------------------------------
    # OPTION 2: BORDER TILE
    # Row of triangles along one edge + dotted line
    # ------------------------------------------
    elif tile_type == "border":
        t.pensize(2)
        for i in range(4):
            go(-half + i * quarter, -half)
            col = palette["primary"] if i % 2 == 0 else palette["secondary"]
            shape(3, quarter, palette["accent"], col)

        # dotted line above the triangles
        for i in range(8):
            go(-half + size / 16 + i * size / 8, quarter * 0.3)
            t.dot(size / 25, palette["accent"])

        # thin line along the opposite edge
        t.pencolor(palette["accent"])
        t.pensize(3)
        go(-half, quarter * 1.4)
        t.pendown()
        t.forward(size)
        t.penup()

    # ------------------------------------------
    # OPTION 3: CENTER TILE
    # Diamond, hexagon, ring and rays
    # ------------------------------------------
    else:
        # diamond (square turned 45 degrees)
        reach = half * 0.85
        t.pensize(3)
        go(0, -reach, 45)
        shape(4, reach * 1.4142, palette["accent"], palette["primary"])

        # hexagon
        r = quarter * 1.1
        go(-r / 2, -r * 0.866)
        t.pensize(2)
        shape(6, r, palette["accent"], palette["secondary"])

        # ring
        go(0, -quarter * 0.55)
        t.pensize(3)
        t.color(palette["accent"], palette["primary"])
        t.pendown()
        t.begin_fill()
        t.circle(quarter * 0.55)
        t.end_fill()
        t.penup()

        # short rays between the hexagon and the diamond
        t.pencolor(palette["accent"])
        t.pensize(2)
        for i in range(8):
            go(0, 0, i * 45 + 22.5)
            t.forward(quarter * 1.2)
            t.pendown()
            t.forward(quarter * 0.45)
            t.penup()

        # center dot
        go(0, 0)
        t.dot(quarter / 3, palette["bg"])

    # ==========================================
    # DRAW BORDER: double frame
    # ==========================================
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

    ######################### YOUR CHANGES END HERE #############################

    # ==========================================
    # TURTLE TEARDOWN
    # ==========================================
    t.penup()
    t.setheading(0)
    t.pencolor((0, 0, 0))