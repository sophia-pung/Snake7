#current ISSUES:
#enemy snake not changing positions when pellet position changes- DONE
#enemy snake is not moving- DONE
#enemy snake needs to change position of pellet
#enemy snake needs to add segment to it each pellet it eats
#enemy snake needs to move slower than the main snake

import turtle, random

class Game:
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)

        #Initializing the segments of snake and snake itself
        print("HERE2")
        self.player = Snake(315, 315, 'green')
        print("HERE")
        #Initializing enemy snake
        print("HERE3")
        self.enemy = Enemy() #I don't 100% get how this works
        print("HERE4")
        #Initializing pellet
        self.pellet = Pellet("Red")

        #controls to move snake and to restart the game
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.restart, 'r')
        print("HEREAAA")
        self.enemy.grow1()
        print("CURETTNYLHERE")
        self.enemy.move1(self.pellet)
        print("IMHERE")
        self.gameloop()
        turtle.listen()
        turtle.mainloop()

        #Initializing the enemy snake outside of the loop
        #Enemy.grow1()
        #Enemy.towards(self.pellet)

    def restart(self):
        #using r key to restart the game and execute everything as it was before
        turtle.clearscreen()
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        self.segments = []
        self.segments1 = []
        self.player = Snake(315, 315, 'green')
        self.enemy = Enemy()
        self.pellet = Pellet("Red")
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.restart, 'r')
        self.enemy.grow1()
        self.enemy.move1(self.pellet)
        self.gameloop()
        turtle.listen()
        turtle.mainloop()

    def distance(self, enemyx, enemyy, pellet):
        #distance between location of enemy snake move and the pellet
        self.pellet_coordinates = (pellet.xp, pellet.yp)
        self.enemy_turtle_coordinates = (enemyx, enemyy)
        return(((abs(enemyy-pellet.yp)**2)+abs(enemyx-pellet.xp)**2)**.5)

    def gameloop(self):
        #main gameloop > everything originates from here
        if self.player.length() == True:
            turtle.write("YOU WON")
        elif self.enemy.length1() == True:
            turtle.write("YOU LOST")
        else:
            if self.player.collision() == True:
                self.player.move(self.pellet)
                print("moving")
                self.enemy.move1(self.pellet)
                turtle.ontimer(self.gameloop, 200)
            elif self.player.collision() == False:
                turtle.write("Game Over", move=False, align='center')

class Enemy():
    def __init__(self, colors='purple'):
        self.vx = 30
        print("enemy1")
        self.vy = 0
        xe = 15 + 30*random.randint(0,19)
        ye = 15 + 30*random.randint(0,19)
        self.xe = xe
        print(self.xe)
        self.ye = ye
        print(self.ye)
        self.segments1 = []
        print("enemy2")
        print("enemy3")
        print("enemy4")

    def towards(self, pellet):
        #function to return a list of the x and y coordinates of the shortest path to the pellet
        direction_list = [30, 30, -30, -30]
        distance_dictionary = {}
        print("SELF.XE = ", self.xe)
        print("SELF.YE = ", self.ye)
        self.distance1 = Game.distance(self, (self.xe + direction_list[0]), (self.ye), pellet)
        print("d1", self.distance1)
        distance_dictionary["distance1"] = [self.distance1, (self.xe + direction_list[0]), (self.ye)]
        self.distance2 = Game.distance(self, (self.xe), (self.ye + direction_list[1]), pellet)
        print("d2", self.distance2)
        distance_dictionary["distance2"] = [self.distance2, (self.xe), ((self.ye) + direction_list[1])]
        self.distance3 = Game.distance(self, (self.xe + direction_list[2]), (self.ye), pellet)
        print("d3", self.distance3)
        distance_dictionary["distance3"] = [self.distance3, (self.xe + direction_list[2]), (self.ye)]
        self.distance4 = Game.distance(self, (self.xe), (self.ye + direction_list[3]), pellet)
        print("d4", self.distance4)
        distance_dictionary["distance4"] = [self.distance4, self.xe, (self.ye + direction_list[3])]
        shortest_distance = float(distance_dictionary["distance1"][0])
        shortest_name = "distance1"
        if (float(distance_dictionary["distance1"][0]) <= float(distance_dictionary["distance2"][0])) and (float(distance_dictionary["distance1"][0]) <= float(distance_dictionary["distance3"][0])) and (float(distance_dictionary["distance1"][0]) <= float(distance_dictionary["distance4"][0])):
            shortest_distance = float(distance_dictionary["distance1"][0])
            shortest_name = "distance1"
        elif (float(distance_dictionary["distance2"][0]) <= float(distance_dictionary["distance1"][0])) and (float(distance_dictionary["distance2"][0]) <= float(distance_dictionary["distance3"][0])) and (float(distance_dictionary["distance2"][0]) <= float(distance_dictionary["distance4"][0])):
            shortest_distance = float(distance_dictionary["distance2"][0])
            shortest_name = "distance2"
        elif (float(distance_dictionary["distance3"][0]) <= float(distance_dictionary["distance1"][0])) and (float(distance_dictionary["distance3"][0]) <= float(distance_dictionary["distance2"][0])) and (float(distance_dictionary["distance3"][0]) <= float(distance_dictionary["distance4"][0])):
            shortest_distance = float(distance_dictionary["distance3"][0])
            shortest_name = "distance3"
        elif (float(distance_dictionary["distance4"][0]) <= float(distance_dictionary["distance1"][0])) and (float(distance_dictionary["distance4"][0]) <= float(distance_dictionary["distance2"][0])) and (float(distance_dictionary["distance4"][0]) <= float(distance_dictionary["distance3"][0])):
            shortest_distance = float(distance_dictionary["distance4"][0])
            shortest_name = "distance4"
        print("IM HERE")
        print(shortest_name)
        self.list = [distance_dictionary[shortest_name][1], distance_dictionary[shortest_name][2]]
        print("LIST", self.list)
        return(self.list)
        # need position of pellet
        # make snake go towards pellet
        # location must shrink in direction it takes or be equal to the distance of another distance
        # if distances are equal, turtle moves towards one that comes first or move towards random of the two

    def grow1(self):
        #creates a new head segment for enemy snake
        head3 = turtle.Turtle()
        head3.speed(0)
        head3.fillcolor("purple")
        head3.shape("square")
        head3.shapesize(1.5, 1.5)
        head3.penup()
        head3.setpos(self.xe, self.ye)
        self.segments1.append(head3)
        print("SEGMETNS", self.segments1)

    def move1(self, pellet):
        #moving the enemy snake
        list2 = self.towards(pellet)
        self.xe = list2[0]
        self.ye = list2[1]
        print("pellet position:", pellet.xp, ", ", pellet.yp)
        if self.xe == pellet.xp and self.ye == pellet.yp:
            self.grow1()
            pellet.draw_circle()#move pellet
            #must follow head
        else:
            for i in range(len(self.segments1) - 1):
                #each segment is a turtle method> set pos
                self.segments1[i].setpos(self.segments1[i+1].pos())
                #self.segments[i].x = self.segments[i+1].x
                #self.segments[i].y = self.segments[i+1].y
                #i is segment after current segment
            print("SEGMENTS", self.segments1)
            print("SELF.X", self.xe)
            print("SELF.Y", self.ye)
            self.segments1[-1].setpos(self.xe, self.ye)
            #all little turtles
        #all little turtles

    def length1(self):
        if len(self.segments1) >= 7:
            return True
        else:
            return False

    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_left(self):
        self.vx = -30
        self.vy = 0
    def go_up(self):
        self.vx = 0
        self.vy = 30

class Snake:
    def __init__(self,x,y,color):
        print("here")
        self.vx = 30
        self.vy = 0
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.grow()

    def length(self):
        if len(self.segments) >= 7:
            return True
        else:
            return False

    def grow(self):
        #creates a new head segment
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape("square")
        head.shapesize(1.5, 1.5)
        head.penup()
        print("SELF", self)
        print(self.x)
        head.setpos(self.x, self.y)
        self.segments.append(head)

    def move(self, pellet):
        #function to move snake
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x == pellet.xp and self.y == pellet.yp:
            self.grow()
            pellet.draw_circle()#move pellet
            #must follow head
        else:
            print("SEGMELENGTH", self.segments)
            for i in range(len(self.segments) - 1):
                #each segment is a turtle method> set pos
                self.segments[i].setpos(self.segments[i+1].pos())
                #self.segments[i].x = self.segments[i+1].x
                #self.segments[i].y = self.segments[i+1].y
                #i is segment after current segment
            print(self.x, self.y, 'here')
            self.segments[-1].setpos(self.x, self.y)

    def collision(self):
        #EDIT FUNCTION SO THAT IT ACCOUNTS FOR SNAKES COLLIDING INTO EACHOTHER
        if 0 < self.x < 600 and 0 < self.y < 600:
            n=self.segments[-1]
            for i in range(len(self.segments)-1):
                if self.segments[i].pos() == n.pos():
                    return False
            return True
        else:
            return False

    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_left(self):
        self.vx = -30
        self.vy = 0
    def go_up(self):
        self.vx = 0
        self.vy = 30
        #check if x coordinate = self.x and y = self.y (make segment and new spot, need for loop)

class Pellet:
    def __init__(self, colorp = "Red"):
        xp = 15 + 30*random.randint(0,19)
        yp = 15 + 30*random.randint(0,19)
        self.head2 = turtle.Turtle()
        self.head2.speed(0)
        self.head2.fillcolor(colorp)
        self.head2.shape("circle")
        self.head2.shapesize(1, 1)
        self.head2.penup()
        self.draw_circle()

    def draw_circle(self):
        xp = 15 + 30*random.randint(0,19)
        yp = 15 + 30*random.randint(0,19)
        self.xp = xp
        self.yp = yp
        self.head2.setpos(self.xp, self.yp)

#mysnake = Snake(315, 315, 'green')
#mysnake.grow()
Game()
