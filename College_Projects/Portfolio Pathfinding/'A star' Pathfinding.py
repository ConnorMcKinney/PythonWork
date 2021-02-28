import random
from tkinter import *
import time
import timeit

class Maze:
    def line(self, x1, y1, x2, y2, colour):
        if colour == None:
            colour == "black"
        self.canvas.create_line(x1, y1, x2, y2, fill=colour, width=3)
        
    def update_nodes(self, final):
        extra = 0
        count = 0
        #self.canvas.delete("all")
        #print("update")
        for r in range(0, self.sizey):
            for c in range(0, self.sizex):
                node = self.findnodebycr(c, r)
                #print("Node == " + str(node))

                if node[12]:
                    count += 1
                    midx = 3 + self.squaresize/2
                    midy = 3 + self.squaresize/2
                    posx = midx + c*(self.squaresize+extra)
                    posy = midy + r*(self.squaresize+extra)
                    
                    for i,v in enumerate(node[11]):
                        self.canvas.delete(v)

                    node[11] = []

                    if node[7]: #Is part of the path
                        if final:
                            rect = self.canvas.create_rectangle(posx-self.squaresize/2, posy-self.squaresize/2, posx+self.squaresize/2, posy+self.squaresize/2, outline="#5500ff", fill="#5500ff")
                            self.canvas.tag_raise(rect)
                            node[11].append(rect)
                        else:
                            rect = self.canvas.create_rectangle(posx-self.squaresize/2, posy-self.squaresize/2, posx+self.squaresize/2, posy+self.squaresize/2, outline="#"+self.colorcode, fill="#"+self.colorcode)
                            self.canvas.tag_raise(rect)
                            node[11].append(rect)
                            
                    if node[2] == True: #left
                        node[11].append(self.line(posx-self.squaresize/2, posy-self.squaresize/2, posx-self.squaresize/2, posy+self.squaresize/2, node[6]))
                    if node[3] == True: #right
                        node[11].append(self.line(posx+self.squaresize/2, posy-self.squaresize/2, posx+self.squaresize/2, posy+self.squaresize/2, node[6]))
                    if node[4] == True: #up
                        node[11].append(self.line(posx-self.squaresize/2, posy-self.squaresize/2, posx+self.squaresize/2, posy-self.squaresize/2, node[6]))
                    if node[5] == True: #down
                        node[11].append(self.line(posx-self.squaresize/2, posy+self.squaresize/2, posx+self.squaresize/2, posy+self.squaresize/2, node[6]))
                    if node[2] == False or node[3] == False or node[4] == False or node[5] == False:
                        self.line(posx, posy, posx+2, posy+2, node[6])
                        #print(node)

                    node[12] = False
                        
                    #if node[2] == True and node[3] == True and node[4] == True and node[5] == True:
                        #print(str(node) + " is fully closed off...")
                    #if (r*self.sizey + c)%2 == 0:
                        #self.line(posx, posy, posx+2, posy+2)
        self.canvas.update()#_idletasks()
        #print(str(count) + " nodes updated.")
    

    def distbet(self, node1, node2):
        movesdown = int(node1[0]) - int(node2[0])
        movesover = int(node1[1]) - int(node2[1])
        dist = (movesover**2 + movesdown**2)**(1/2)
        #print("movesover == " + str(movesover))
        #print("movesdown == " + str(movesdown))
        #print("length == " + str(dist))
        return dist

    def checklistfornode(self, node):
        if node in self.nodes:
            return True
        else:
            print("node: " + node + " does not exist.")
            return False

    def findnodebycr(self, c, r):
        if c <0 or c > self.sizex-1 or r < 0 or r > self.sizey-1:
            #print("rejected node (" + str(c) + ", " + str(r))
            return False
        #print(len(self.nodes))
        #print("Guessing in findnodebycr: " + str(self.sizey*c + r))
##        for i, v in self.nodes.items():
##            #print("Checking value: " + str(v[0]) + ", " + str(v[1]))
##            if v[0] == c:
##                if v[1] == r:
##                    #print("returning node " + str(i))
##                    #print("Guessing in findnodebycr: " + str(self.sizey*c + r))
##                    print(i)
##                    print(self.sizey*c + r)
##                    print("")
##                    return self.nodes[i]
##        return False
        try:
            return self.nodes[self.sizey*c + r]
        except:
            print("Findnodebycr: no node found for " + str(r) +":"+str(c))
            return False

    def check_adjacent(self, node):
        currentc = node[0]
        currentr = node[1]

        left = self.findnodebycr(currentc-1, currentr)
        right = self.findnodebycr(currentc+1, currentr)
        up = self.findnodebycr(currentc, currentr+1)
        down = self.findnodebycr(currentc, currentr-1)
        adjacent = []

        
        if left and not left in self.beento:
            adjacent.append(left)
        if right and not right in self.beento:
            adjacent.append(right)
        if up and not up in self.beento:
            adjacent.append(up)
        if down and not down in self.beento:
            adjacent.append(down)
        if len(adjacent) > 0:
            return True
        else:
            return False

    def check_adjacent_path(self, node):
        currentc = node[0]
        currentr = node[1]

        left = self.findnodebycr(currentc-1, currentr)
        right = self.findnodebycr(currentc+1, currentr)
        up = self.findnodebycr(currentc, currentr+1)
        down = self.findnodebycr(currentc, currentr-1)
        adjacent1 = []

        
        if left and left[3] == False and left not in self.beento: #and self.distbet(left, end) <= self.distbet(left, start):
            adjacent1.append(left)
            #print("appended ")
        if right and right[2] == False and right not in self.beento: #and self.distbet(right, end) <= self.distbet(left, start):
            adjacent1.append(right)
            #print("appended ")
        if up and up[4] == False and up not in self.beento: #and self.distbet(up, end) <= self.distbet(up, start):
            adjacent1.append(up)
            #print("appended ")
        if down and down[5] == False and down not in self.beento: #and self.distbet(down, end) <= self.distbet(down, start):
            adjacent1.append(down)
            #print("appended ")
            
        if len(adjacent1) > 0:
            print(str(adjacent1) + " are adjacent to " + str(node))
            
            return True
        else:
            return False

    def create_path_iter(self, start):
        startx = start[0]
        starty = start[1]
        start = self.findnodebycr(startx, starty)
        currentnode = start

        while True:
            #step += 1
            #print("Step == " + str(step))
            #print("Num beento == " + str(len(self.beento)))
        
            currentc = int(currentnode[0])
            currentr = int(currentnode[1])

            left = self.findnodebycr(currentc-1, currentr)
            right = self.findnodebycr(currentc+1, currentr)
            up = self.findnodebycr(currentc, currentr+1)
            down = self.findnodebycr(currentc, currentr-1)
            #print(left, right, up, down)
            adjacent = []

            
            if left != False and not left in self.beento:
                for i in range(0, self.leftbias):
                    adjacent.append(left)
            if right != False and not right in self.beento:
                for i in range(0, self.rightbias):
                    adjacent.append(right)
            if up != False and not up in self.beento:
                for i in range(0, self.upbias):
                    adjacent.append(up)
            if down != False and not down in self.beento:
                for i in range(0, self.downbias):
                    adjacent.append(down)
                        
            if len(adjacent) != 0:
                num = random.randint(0, len(adjacent)-1)
                #print(adjacent[num] == left,adjacent[num] == right,adjacent[num] == up,adjacent[num] == down)
                #print(adjacent)
                #print(currentnode)
                #if len(self.beento) >2:
                    #print(self.beento[len(self.beento)-1])
                if adjacent[num] == left:

                    currentnode[2] = False
                    left[3] = False
                    #print("1moved into " + str(left))
                    self.beento.append(currentnode)
                    currentnode = left
                if adjacent[num] == right:

                    currentnode[3] = False
                    right[2] = False
                    #print("2moved into " + str(right))
                    self.beento.append(currentnode)
                    currentnode = right
                if adjacent[num] == up:

                    currentnode[5] = False
                    up[4] = False
                    #print("3moved into " + str(up))
                    self.beento.append(currentnode)
                    currentnode = up
                if adjacent[num] == down:

                    currentnode[4] = False
                    down[5] = False
                    #print("4moved into " + str(down))
                    #print(down not in self.beento)
                    self.beento.append(currentnode)
                    currentnode = down

            else:
                newnode = None
                for i in range(len(self.beento)-1, 0, -1):
                    if self.check_adjacent(self.beento[i]):
                        self.beento.append(currentnode)
                        currentnode = self.beento[i]
                        newnode = self.beento[i]
                        #print("Backtracked to " + str(currentnode))
                        break
                
                if newnode == None:
                    print("No more nodes.")
                    self.update_nodes(False)
                    break                        

    def create_path(self, currentnode):

        self.currentc = None
        self.currentr = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        
        self.currentc = currentnode[0]
        self.currentr = currentnode[1]

        self.left = self.findnodebycr(self.currentc-1, self.currentr)
        self.right = self.findnodebycr(self.currentc+1, self.currentr)
        self.up = self.findnodebycr(self.currentc, self.currentr+1)
        self.down = self.findnodebycr(self.currentc, self.currentr-1)
        #print(left, right, up, down)
        self.adjacent = []

        
        if self.left != False and not self.left in self.beento:
            for i in range(0, self.leftbias):
                self.adjacent.append(self.left)
        if self.right != False and not self.right in self.beento:
            for i in range(0, self.rightbias):
                self.adjacent.append(self.right)
        if self.up != False and not self.up in self.beento:
            for i in range(0, self.upbias):
                self.adjacent.append(self.up)
        if self.down != False and not self.down in self.beento:
            for i in range(0, self.downbias):
                self.adjacent.append(self.down)
                    
        if len(self.adjacent) != 0:
            num = random.randint(0, len(self.adjacent)-1)
            #print(adjacent[num] == left,adjacent[num] == right,adjacent[num] == up,adjacent[num] == down)
            #print(adjacent)
            #print(currentnode)
            #if len(self.beento) >2:
                #print(self.beento[len(self.beento)-1])
            if self.adjacent[num] == self.left:

                currentnode[2] = False
                self.left[3] = False
                #print("1moved into " + str(left))
                self.beento.append(currentnode)
                currentnode = self.left
            if self.adjacent[num] == self.right:

                currentnode[3] = False
                self.right[2] = False
                #print("2moved into " + str(right))
                self.beento.append(currentnode)
                currentnode = self.right
            if self.adjacent[num] == self.up:

                currentnode[5] = False
                self.up[4] = False
                #print("3moved into " + str(up))
                self.beento.append(currentnode)
                currentnode = self.up
            if self.adjacent[num] == self.down:

                currentnode[4] = False
                self.down[5] = False
                #print("4moved into " + str(down))
                #print(down not in self.beento)
                self.beento.append(currentnode)
                currentnode = self.down

        else:
            newnode = None
##            if len(self.beento) == len(self.nodes):
##                #done = True
##                #break
##                print("Done")
##                self.update_nodes()
##                return False
            for i in range(len(self.beento)-1, 0, -1):
                if self.check_adjacent(self.beento[i]):
                    self.beento.append(currentnode)
                    currentnode = self.beento[i]
                    newnode = self.beento[i]
                    #print("Backtracked to " + str(currentnode))
                    break
            
            if newnode == None:
                print("No more nodes.")
                self.update_nodes(False)
                return False
        self.update_nodes(False)
        self.create_path(currentnode)

    def clean_nodes(self):
        count = 0
        for c in range(0, self.sizex):
            #print("r == " + str(r))
            for r in range(0, self.sizey):
                #self.nodes[count] = [c, r, True, True, True, True, None, False, 9999, 9999, None]
                self.nodes[count][6] = None
                self.nodes[count][7] = None
                self.nodes[count][12] = True
                count += 1

    def finalpath(self, start, end):

        self.clean_nodes()
        
        start[6] = "#4e03fc"
        start[7] = True
        start[8] = 0
        start[9] = self.dist_btw(start, end)
        start[12] = True

        currentnode = start

        while True:
            #print("loop")
            self.mark_as_path(currentnode, "backward")
            if currentnode == end:
                print("Finished!!!")                
                self.update_nodes(False)#self.update_nodes(True)
                #input("Input to finish pathfinding")
                break
            
            currentnode = currentnode[10]
            time.sleep(.05)
            self.update_nodes(False)#self.update_nodes(True)

    def clean_node(self, node):
        node[6] = None
        node[7] = None
        node[12] = True

    def clean_beento_nodes(self):
        for i,v in enumerate(self.beento):
            v[6] = None
            v[7] = None
            v[12] = True

    def mark_as_path(self, cell, setting):
        if setting == "forward":        
            cell[6] = "#3deb34"
            cell[7] = True
            cell[12] = True
        elif setting == "backward":
            cell[6] = "#4e03fc"
            cell[7] = True
            cell[12] = True

    def list_difference(self, li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif
            
    def dist_btw(self, cell1, cell2):
        return ((cell2[0]-cell1[0])**2 + (cell2[1]-cell1[1])**2)

    def set_from_parent(self, cell):
        #self.clean_beento_nodes()
        show_list = []
        current = cell
        count = 0
        while current:
            count += 1
            #self.mark_as_path(current, "forward")
            show_list.append(current)
            current = current[10]

        print(str(count) + " Nodes in the tree.")

        diff = self.list_difference(self.last_show, show_list)
        print(str(len(diff)) + " differences")
        for i,v in enumerate(diff):
            if v != cell:
                if v not in show_list:
                    self.clean_node(v)
                else:
                    self.mark_as_path(v, "forward")
        
        return show_list, len(diff)

    def pathfind(self, start, end):
        self.beento[:] = []
        self.openlist = []
        self.closedlist = []
        self.last_show = []
        currentnode = None#start
        endnode = end

        start[8] = 0
        start[9] = self.dist_btw(start, end)
        
        
        #self.beento.append(start)
        self.openlist.append(start)
        #self.closedlist.append(start)
        
        nextnode = None
        while True:

            if currentnode == endnode:
                print("Finished!!!")
                self.beento.append(currentnode)
                #print(str(self.beento))
                self.update_nodes(False)
                self.finalpath(end, start)
                break
            #print("currentnode == " + str(currentnode))

            adjacent1 = []

            if currentnode:
                currentc = currentnode[0]
                currentr = currentnode[1]

                left = self.findnodebycr(currentc-1, currentr)
                right = self.findnodebycr(currentc+1, currentr)
                up = self.findnodebycr(currentc, currentr+1)
                down = self.findnodebycr(currentc, currentr-1)
    ##            print("left == " + str(left))
    ##            print("right == " + str(right))
    ##            print("up == " + str(up))
    ##            print("down == " + str(down))
                

                #8 is g
                #9 is h
                #10 is parent

                if left and left[3] == False and not (left in self.openlist) and not (left in self.closedlist): #and self.distbet(left, end) <= self.distbet(left, start):
                    adjacent1.append(left)
                    #print("appended ")
                elif left in self.openlist and left[3] == False:
                    if currentnode[8] + 1 < left[8]:
                        left[8] = currentnode[8] + 1
                        left[10] = currentnode
                        print("Reestablished parent")
                if right and right[2] == False and not (right in self.openlist) and not (right in self.closedlist): #and self.distbet(right, end) <= self.distbet(left, start):
                    adjacent1.append(right)
                    #print("appended ")
                elif right in self.openlist and right[2] == False:
                    if currentnode[8] + 1 < right[8]:
                        right[8] = currentnode[8] + 1
                        right[10] = currentnode
                        print("Reestablished parent")
                if up and up[4] == False and not (up in self.openlist) and not (up in self.closedlist): #and self.distbet(up, end) <= self.distbet(up, start):
                    adjacent1.append(up)
                    #print("appended ")
                elif up in self.openlist and up[4] == False:
                    if currentnode[8] + 1 < up[8]:
                        up[8] = currentnode[8] + 1
                        up[10] = currentnode
                        print("Reestablished parent")
                if down and down[5] == False and not (down in self.openlist) and not (down in self.closedlist): #and self.distbet(down, end) <= self.distbet(down, start):
                    adjacent1.append(down)
                    #print("appended ")
                elif down in self.openlist and down[5] == False:
                    if currentnode[8] + 1 < down[8]:
                        down[8] = currentnode[8] + 1
                        down[10] = currentnode
                        print("Reestablished parent")
                #print(adjacent1)


            if len(adjacent1) != 0:


                #print(len(adjacent1))
                for i,v in enumerate(adjacent1):
                    v[8] = currentnode[8] + 1
                    v[9] = self.dist_btw(v, end)
                    v[10] = currentnode
                    #print("Adding " + str(v) + " to openlist")
                    self.openlist.append(v)

            nextmove = False
            if len(self.openlist) != 0:
                #print("Length of openlist is " + str(len(self.openlist)))
                lowestF = 99999
                
                for i,v in enumerate(self.openlist):
                    f = v[8] + v[9]
                    if f < lowestF:
                        lowestF = f
                        nextmove = v

                        
                #print("Next move is " + str(nextmove))
                self.closedlist.append(nextmove)
                self.openlist.remove(nextmove)
                #print(nextmove in self.openlist)
                
                self.mark_as_path(nextmove, "forward")
                currentnode = nextmove

                #self.last_show, updates = self.set_from_parent(nextmove)
                #print(currentnode[0], currentnode[1])
                time.sleep(.05)
                
                
                #time1 = timeit.timeit()
                self.update_nodes(False)
                #print(timeit.timeit() - time1)
                self.beento.append(currentnode)
                #time.sleep(0.005*updates**2)
                #print("Nextnode == " + str(nextnode))
                #currentnode = nextnode
                #self.update_nodes()
            else:
                print("No more tiles in openlist")
                break

                
    def p(self, x):
        print(x)
        self.canvas.after(100, self.p(10))

            
    def __init__(self, sizex, sizey, mazestart, pathstart, pathend, rtd, list1):
        t1 = timeit.default_timer()
        self.nodes = dict()
        self.beento = []

        #Maze options. Currently has to be square for unknown reasons
        self.cwidth = 1005
        self.cheight = 1005
        self.sizex = sizex
        self.sizey = sizey
        self.sizetotal = self.sizex*self.sizey
        size1 = self.cwidth//self.sizex
        size2 = self.cheight//self.sizey
        #print(size1, size2)
        
        if size1 < size2:
            finalsize = size1
        else:
            finalsize = size2
            
        self.squaresize = finalsize
        self.leftbias = 1
        self.rightbias = 1
        self.upbias = 1
        self.downbias = 1

        #Some variables to cut down on memory usage in the recursive version
        self.adjacent = None
        self.currentc = None
        self.currentr = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        
        count = 0
        for c in range(0, sizex):
            #print("r == " + str(r))
            for r in range(0, sizey):
                #print(r*sizey+c)
                #column, row, wall, wall, wall, wall, color, fill_rect, g, h, parent, parts, update
                self.nodes[count] = [c, r, True, True, True, True, None, False, 9999, 9999, None, [None, None, None, None, None], True]
                count += 1
                #print("created node " + str(count) + " at position " + str(c), str(r))
                #print("c == " + str(c))
        #print("nodes == " + str(self.nodes))
        #for i in self.nodes:
            #self.findnodebycr(self.nodes[i][0], self.nodes[i][1])
        start = self.findnodebycr(mazestart[0], mazestart[1])

        self.root = Tk()
        self.canvas = Canvas(width=self.cwidth, height=self.cheight, bg="#A9A9A9")
        self.canvas.pack()

        if sizex*sizey > 25**2 or rtd == False:
            self.create_path_iter(start)
            t2 = timeit.default_timer()
        else:
            self.create_path(start)
            t2 = timeit.default_timer()
        list1.append(str(sizex) + "x" + str(sizey) + ":" + str(t2-t1))
        input("Input to begin pathfinding: ")
        self.colorcode = "ff6600"#input("Input html color code: ")
        self.pathfind(self.findnodebycr(pathstart[0], pathstart[1]), self.findnodebycr(pathend[0], pathend[1]))


#sys.setrecursionlimit(1500)
#good mazes: (25, 25, 10112), (20, 20, 115)
#broken mazes: 319
num = 5#random.randint(0, 1000)
#print("seed == " + str(num))
random.seed(101)
#random.seed(num)
list1 = []
sx = 40 #size x
sy = 40 # size y
#(sizex, sizey, mazestart, pathfindstart, pathfindend, watch it generate)
Maze(sx, sy, (sx//2, sy//2), (0, 0), (sx-1, sy-1), False, list1)
print(list1)

print("Halted")
#input("Halted")



















