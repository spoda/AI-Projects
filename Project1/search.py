# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())"""
    dfsStack = util.Stack()
    dfsVisit = []
    finalPath = {}
    goalPath = []
    goalPath2 = []
    topStack = problem.getStartState()
    dfsStack.push(topStack)
    while (dfsStack.isEmpty() == False):
        topStack = dfsStack.pop()
        """print "topStack: ", topStack"""
        dfsVisit.append(topStack)
        if (problem.isGoalState(topStack) == True):
            """print "Currently Breaking Out"""
            break
        for dest in problem.getSuccessors(topStack):
            """print "dfsVisit", dfsVisit"""
            if (dest[0] not in dfsVisit):
                """print "dest added: ", dest"""
                dfsStack.push(dest[0])
                finalPath[dest[0]] = (topStack, dest[1])
    if (problem.isGoalState(topStack)):
        while (topStack != problem.getStartState()):
            goalPath.append(finalPath.get(topStack)[1])
            topStack = finalPath.get(topStack)[0]
        for i in range (goalPath.__len__(),0,-1):
            goalPath2.append(goalPath[i-1])
        """print "goalPath", goalPath2"""
        return goalPath2
    else:
        return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    bfsQueue = util.Queue()
    bfsVisit = []
    finalPath = {}
    goalPath = []
    goalPath2 = []
    topQueue = problem.getStartState()
    bfsQueue.push(topQueue)
    while (bfsQueue.isEmpty() == False):
        topQueue = bfsQueue.pop()
        bfsVisit.append(topQueue)
        if (problem.isGoalState(topQueue) == True):
            break
        for dest in problem.getSuccessors(topQueue):
            if (dest[0] not in bfsVisit and finalPath.get(dest[0]) == None):
                bfsQueue.push(dest[0])
                finalPath[dest[0]] = (topQueue, dest[1])
    if (problem.isGoalState(topQueue)):
        while (topQueue != problem.getStartState()):
            goalPath.append(finalPath.get(topQueue)[1])
            topQueue = finalPath.get(topQueue)[0]
        for i in range (goalPath.__len__(),0,-1):
            goalPath2.append(goalPath[i-1])
        return goalPath2
    else:
        return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first. """
    "*** YOUR CODE HERE ***"
    ucsQueue = util.PriorityQueue()
    ucsVisit = []
    ucsFinalPath = {}
    ucsGoalPath = []
    ucsGoalPath2 =[]
    totalCost = 0
    topQueue = problem.getStartState()
    ucsFinalPath[topQueue] = (("0","0"), "0", 0)
    ucsQueue.push(topQueue, 0)
    while(ucsQueue.isEmpty() == False):
        topQueue = ucsQueue.pop()
        ucsVisit.append(topQueue)
        if (problem.isGoalState(topQueue) == True):
            break
        for dest in problem.getSuccessors(topQueue):
            if(ucsFinalPath.get(dest[0])==None) and (dest[0] not in ucsVisit):
                totalCost = dest[2]+(ucsFinalPath.get(topQueue)[2])
                ucsQueue.push(dest[0], totalCost)
                ucsFinalPath[dest[0]]=(topQueue, dest[1],totalCost) 
            elif (ucsFinalPath.get(dest[0])!=None) and (dest[0] not in ucsVisit): 
                nodeVal = ucsFinalPath.get(dest[0])[2]
                totalCost = dest[2] + ucsFinalPath.get(topQueue)[2]
                if (nodeVal > totalCost):
                    ucsQueue.push(dest[0], totalCost)
                    ucsFinalPath[dest[0]] = (topQueue, dest[1], totalCost)
    if (problem.isGoalState(topQueue) == True):
        while (topQueue != problem.getStartState()):
            ucsGoalPath.append(ucsFinalPath.get(topQueue)[1])
            topQueue = ucsFinalPath.get(topQueue)[0]
        for i in range (ucsGoalPath.__len__(),0,-1):
            ucsGoalPath2.append(ucsGoalPath[i-1])
        return ucsGoalPath2
    else:
        return []  
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    aQueue = util.PriorityQueue()
    aVisit = []
    aFinalPath = {}
    aGoalPath = []
    aGoalPath2 =[]
    topQueue = problem.getStartState()
    hVal = heuristic(topQueue,problem)
    aFinalPath[topQueue] = (("0","0"), "0", hVal)
    aQueue.push(topQueue, 0)
    while(aQueue.isEmpty() == False):
        topQueue = aQueue.pop()
        aVisit.append(topQueue)
        if (problem.isGoalState(topQueue) == True):
            break
        for dest in problem.getSuccessors(topQueue):
            if(aFinalPath.get(dest[0])==None) and ((dest[0] not in aVisit)):
                totalCost = dest[2]+(aFinalPath.get(topQueue)[2]) 
                totalH = dest[2]+(aFinalPath.get(topQueue)[2]) + heuristic(dest[0], problem)
                aQueue.push(dest[0], totalH)
                aFinalPath[dest[0]]=(topQueue, dest[1],totalCost) 
            elif (aFinalPath.get(dest[0])!=None) and (dest[0] not in aVisit): 
                nodeVal = aFinalPath.get(dest[0])[2]
                totalCost = dest[2] + aFinalPath.get(topQueue)[2]
                if (nodeVal > totalCost):
                    totalH = totalCost + heuristic(dest[0], problem)
                    aQueue.push(dest[0], totalH)
                    aFinalPath[dest[0]] = (topQueue, dest[1], totalCost)
    if (problem.isGoalState(topQueue) == True):
        while (topQueue != problem.getStartState()):
            aGoalPath.append(aFinalPath.get(topQueue)[1])
            topQueue = aFinalPath.get(topQueue)[0]
        for i in range (aGoalPath.__len__(),0,-1):
            aGoalPath2.append(aGoalPath[i-1])
        return aGoalPath2
    else:
        return []  
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
