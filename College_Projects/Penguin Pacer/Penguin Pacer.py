import pgzrun
from pgzero.builtins import Actor, keyboard
import random
import time
import handle_scores
import os

# Change these to change the physical size of the window. I make no guarantees that this will not break the game in
# certain resolutions.
WIDTH = 600
HEIGHT = 500

char_image = Actor("penguin_resized_larger")
seed = None
seeded = False
while not seeded:
    seed = input("Input an integer seed to generate a maze or input '1' for a random seed: ")
    if seed.isnumeric():
        if seed == "1":
            seed = random.randint(0, 999999999)
            seeded = True
        else:
            seed = int(seed)
            seeded = True
    else:
        print("That is not a valid seed. Try again.")

sized = False
while not sized:
    num_col = input("Input a integer number of columns for the maze: ")
    if num_col.isnumeric():
        if int(num_col) > 0:
            num_col = int(num_col)
        else:
            print("That is not a valid input.")
            continue
    else:
        print("That is not a valid input.")
        continue
    num_row = input("Input a integer number of rows for the maze: ")
    if num_row.isnumeric():
        if int(num_row) > 0:
            num_row = int(num_row)
        else:
            print("That is not a valid input.")
            continue
    else:
        print("That is not a valid input.")
        continue
    sized = True

width = WIDTH
height = HEIGHT

nodesize = (width/num_col, height/num_row)

startpos = (nodesize[0]/2, nodesize[1]/2)
endpos = num_row*num_col - 1

random.seed(seed)
print("Your seed is %i."%seed)
print("Navigate to the game window and press any button to begin.")

draw_maze = False

tiles = []
connections = []
effects = []

for r in range(0, num_row):
    for c in range(0, num_col):
        topleft = ((width/num_col)*c, (height/num_row)*r)
        #print(topleft, c, r)
        bottomright = ((width/num_col)*(c+1), (height/num_row)*(r+1))
        new_rect = Rect((topleft, bottomright))
        tiles.append(new_rect)
effects.append(("finish_flag", endpos))
"""
0  1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
"""

class maze:
    def __init__(self, columns, rows, tile_list, start, end, gamemode):
        self.columns = columns
        self.rows = rows
        self.num_nodes = columns*rows
        self.tile_list = tile_list
        self.start_tile = start
        self.end_tile = end
        self.gamemode = gamemode
        self.fish_nodes = []
        self.draw_maze = False

        self.nodelist = []
        for i in range(0, len(tile_list)):
            #set all exits to closed
            #up, down, left, right
            nodeinfo = [i, False, False, False, False]
            self.nodelist.append(nodeinfo)
        self.create_path()

    def get_adjacent(self, node):
        nodes = []
        #up, down, left, right
        if (node - self.columns) >= 0:
            nodes.append((node - self.columns, "up"))
        if (node + self.columns) < (self.columns*self.rows):
            nodes.append((node + self.columns, "down"))
        if (node % self.columns) != 0:
            nodes.append((node - 1, "left"))
        if ((node + 1) % self.columns) != 0:
            nodes.append((node + 1, "right"))
        return nodes

    def filter_beento(self, nodes, beento_list):
        #print("Nodes before: ", nodes)
        good_nodes = []
        for node in nodes:
            if node[0] not in beento_list:
                #print("Removed node %i"%node[0])
                good_nodes.append(node)
        #print("Nodes after: ", good_nodes)
        return good_nodes

    def create_path(self):
        currentnode = self.nodelist[self.start_tile][0]
        beento = []
        beento.append(currentnode)
        while currentnode != None:
            adjacent_list = self.filter_beento(self.get_adjacent(currentnode), beento)

            if adjacent_list:
                next_node = random.choice(adjacent_list)

                if next_node[1] == "up":
                    self.nodelist[currentnode][1] = True
                    self.nodelist[next_node[0]][2] = True
                elif next_node[1] == "down":
                    self.nodelist[currentnode][2] = True
                    self.nodelist[next_node[0]][1] = True
                elif next_node[1] == "left":
                    self.nodelist[currentnode][3] = True
                    self.nodelist[next_node[0]][4] = True
                elif next_node[1] == "right":
                    self.nodelist[currentnode][4] = True
                    self.nodelist[next_node[0]][3] = True

                #self.draw_connection(current_node, next_node[1])
                currentnode = next_node[0]
                beento.append(currentnode)

            else:
                # print("Need to backtrack")
                # print(len(beento), beento)
                can_move = False
                for i in reversed(beento):
                    adjacent_list = self.filter_beento(self.get_adjacent(i), beento)
                    if adjacent_list:
                        currentnode = i
                        can_move = True
                if not can_move:
                    currentnode = None
                    if len(beento) < self.num_nodes:
                        raise ValueError("Not enough nodes created. Try a different seed.")
        self.place_fish()
        self.handle_mode()
    def place_fish(self): # keep fish from being too close together on the map
        for i in range(0, random.randint(1, 3)):
            position = random.randint(num_col, self.num_nodes-num_col//2)
            if position not in self.fish_nodes:
                self.fish_nodes.append(position)
                effects.append(("fish_resized", position))
                #print("Fish on %i"%position)


    def handle_mode(self):
        if self.gamemode == "normal":
            self.draw_connections(self.nodelist)
        if self.gamemode == "limited":
            self.draw_connections()

    def draw_connections(self, nodes):
        for node in nodes:
            if tiles[node[0]]:
                #left side, top side
                x = tiles[node[0]].x
                y = tiles[node[0]].y
                if node[1]: #up
                    new_rect = Rect(1, 1, 1, 1)
                    new_rect.size = nodesize[0]-2, 2
                    new_rect.center = x+nodesize[0]/2, y
                    connections.append(new_rect)
                if node[2]:
                    new_rect = Rect(1, 1, 1, 1)
                    new_rect.size = nodesize[0] - 2, 2
                    new_rect.center = x + nodesize[0] / 2, y+nodesize[1]
                    connections.append(new_rect)
                if node[3]: #left
                    new_rect = Rect(1, 1, 1, 1)
                    new_rect.size = 2, nodesize[1]-2
                    new_rect.centerx = (x)
                    new_rect.centery = y+nodesize[1]/2
                    connections.append(new_rect)
                if node[4]:
                    new_rect = Rect(1, 1, 1, 1)
                    new_rect.size = 2, nodesize[1]-2
                    new_rect.center = x + nodesize[0], y + nodesize[1]/2
                    connections.append(new_rect)

path = maze(num_col, num_row, tiles, 0, 15, "normal")

class char:

    def __init__(self):
        self.position = 0
        self.sprite = char_image
        self.move_to_rect(0)
        self.time1 = 0
        self.fish = 0
        self.can_move = False

    def move(self, direction):
        if player.can_move == False:
            return
        newpos = None
        if direction == "up":
            if self.position - num_col >= 0:
                if path.nodelist[self.position][1]:
                    newpos = self.position - num_col
        elif direction == "down":
            if self.position + num_col < num_col*num_row:
                if path.nodelist[self.position][2]:
                    newpos = self.position + num_col
        elif direction == "left":
            if self.position % num_col != 0:
                if path.nodelist[self.position][3]:
                    newpos = self.position - 1
        elif direction == "right":
            if (self.position + 1) % num_col != 0:
                if path.nodelist[self.position][4]:
                    newpos = self.position + 1

        if newpos == None:
            # print("'%s' is not a valid move!"%direction)
            return
        else:
            if newpos == endpos:
                total = time.perf_counter() - self.time1
                total = total*(.8)**player.fish
                high_score = handle_scores.get_high_score(seed, num_col, num_row)
                if high_score > total or not high_score:
                    print("New high score!")
                    print("Score was %.2f seconds with %i fish collected on seed %i with a %ix%i field." % (total, player.fish, seed, num_col, num_row))
                    handle_scores.write_score(seed, num_col, num_row, total)
                else:
                    print("Your Score: %.2f\nHigh Score: %.2f"%(total, high_score))
                    
                input("")

                player.can_move = False
            if newpos in path.fish_nodes:
                self.fish += 1
                path.fish_nodes.remove(newpos)
                effects.remove(("fish_resized", newpos))
                draw()

            self.move_to_rect(newpos)

    def move_to_rect(self, pos):
        if pos < num_row*num_col and pos >= 0:
            self.sprite.pos = tiles[pos].x + nodesize[0]/2, tiles[pos].y + nodesize[1]/2
            self.position = pos
            #print(pos)

player = char()

def draw():
    screen.clear()
    if path.draw_maze:
        for rect in tiles:
            r = 255#random.randint(0, 255)
            g = 255#random.randint(0, 255)
            b = 255#random.randint(0, 255)
            screen.draw.rect(rect, (r, g, b))
        for rect in connections:
            r = 0
            g = 0
            b = 0
            screen.draw.filled_rect(rect, (r, g, b))
        if effects:
            for effect in effects:
                screen.blit(effect[0], tiles[effect[1]])

        player.sprite.draw()
   # else:


def on_key_down(key):
    if player.time1 == 0:
        player.time1 = time.perf_counter()
        path.draw_maze = True
        player.can_move = True
    elif key == keys.UP:
        player.move("up")
    elif key == keys.DOWN:
        player.move("down")
    elif key == keys.LEFT:
        player.move("left")
    elif key == keys.RIGHT:
        player.move("right")
    else:
        print(key)
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()