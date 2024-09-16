import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

cities = ['Atlanta',        'Boston',         'Calgary',
          'Charleston',    'Chicago',        'Dallas',
          'Denver',        'Duluth',         'El Paso',
          'Helena',        'Houston',        'Kansas City',
          'Las Vegas',     'Little Rock',    'Los Angeles',
          'Miami',         'Montreal',       'Nashville',
          'New Orleans',   'New York',       'Oklahoma City',
          'Omaha',         'Phoenix',        'Pittsburgh',
          'Portland',      'Raleigh',        'Saint Louis',
          'Salt Lake City', 'San Francisco',  'Santa Fe',
          'Sault St Marie', 'Seattle',        'Toronto',
          'Vancouver',     'Washington',     'Winnipeg']

# 0 grey
# 1 red
# 2 orange
# 3 yellow
# 4 green
# 5 blue
# 6 pink
# 7 white
# 8 black

routes = [
    ['Atlanta', 'Nashville', 0, 1, 0], #0
    ['Atlanta', 'Charleston', 0, 2, 0], #1
    ['Atlanta', 'Miami', 5, 5, 0], #2
    ['Atlanta', 'Raleigh', 0, 2, 0], #3
    ['Atlanta', 'Raleigh', 0, 2, 0], #4
    ['Atlanta', 'New Orleans', 2, 4, 0], #5
    ['Atlanta', 'New Orleans', 3, 4, 0], #6
    ['Boston', 'Montreal', 0, 2, 0], #7
    ['Boston', 'Montreal', 0, 2, 0], #8
    ['Boston', 'New York', 1, 2, 0], #9
    ['Boston', 'New York', 3, 2, 0], #10
    ['Calgary', 'Vancouver', 0, 3, 0], #11
    ['Calgary', 'Winnipeg', 7, 6, 0], #12
    ['Calgary', 'Helena', 0, 4, 0], #13
    ['Calgary', 'Seattle', 0, 4, 0], #14
    ['Charleston', 'Raleigh', 0, 2, 0], #15
    ['Charleston', 'Miami', 6, 4, 0], #16
    ['Chicago', 'Toronto', 7, 4, 0], #17
    ['Chicago', 'Pittsburgh', 2, 3, 0], #18
    ['Chicago', 'Pittsburgh', 8, 3, 0], #19
    ['Chicago', 'Saint Louis', 4, 2, 0], #20
    ['Chicago', 'Saint Louis', 7, 2, 0], #21
    ['Chicago', 'Omaha', 5, 4, 0], #22
    ['Chicago', 'Duluth', 1, 3, 0], #23
    ['Dallas', 'Oklahoma City', 0, 2, 0], #24
    ['Dallas', 'Oklahoma City', 0, 2, 0], #25
    ['Dallas', 'Little Rock', 0, 2, 0], #26
    ['Dallas', 'Houston', 0, 1, 0], #27
    ['Dallas', 'Houston', 0, 1, 0], #28
    ['Dallas', 'El Paso', 1, 4, 0], #29
    ['Denver', 'Helena', 4, 4, 0], #30
    ['Denver', 'Omaha', 6, 4, 0], #31
    ['Denver', 'Kansas City', 8, 4, 0], #32
    ['Denver', 'Kansas City', 2, 4, 0], #33
    ['Denver', 'Oklahoma City', 1, 4, 0], #34
    ['Denver', 'Santa Fe', 0, 2, 0], #35
    ['Denver', 'Phoenix', 7, 5, 0], #36
    ['Denver', 'Salt Lake City', 1, 3, 0], #37
    ['Denver', 'Salt Lake City', 3, 3, 0], #38
    ['Duluth', 'Omaha', 0, 2, 0], #39
    ['Duluth', 'Omaha', 0, 2, 0], #40
    ['Duluth', 'Helena', 2, 6, 0], #41
    ['Duluth', 'Winnipeg', 8, 4, 0], #42
    ['Duluth', 'Sault St Marie', 0, 3, 0], #43
    ['Duluth', 'Toronto', 6, 6, 0], #44
    ['El Paso', 'Houston', 4, 6, 0], #45
    ['El Paso', 'Los Angeles', 8, 6, 0], #46
    ['El Paso', 'Phoenix', 0, 3, 0], #47
    ['El Paso', 'Santa Fe', 0, 2, 0], #48
    ['El Paso', 'Oklahoma City', 3, 5, 0], #49
    ['Helena', 'Omaha', 1, 5, 0], #50
    ['Helena', 'Salt Lake City', 6, 3, 0], #51
    ['Helena', 'Seattle', 3, 6, 0], #52
    ['Helena', 'Winnipeg', 5, 4, 0], #53
    ['Houston', 'New Orleans', 0, 2, 0], #54
    ['Kansas City', 'Omaha', 0, 1, 0], #55
    ['Kansas City', 'Omaha', 0, 1, 0], #56
    ['Kansas City', 'Oklahoma City', 0, 2, 0], #57
    ['Kansas City', 'Oklahoma City', 0, 2, 0], #58
    ['Kansas City', 'Saint Louis', 5, 2, 0], #59
    ['Kansas City', 'Saint Louis', 6, 2, 0], #60
    ['Las Vegas', 'Los Angeles', 0, 2, 0], #61
    ['Las Vegas', 'Salt Lake City', 2, 3, 0], #62
    ['Little Rock', 'Oklahoma City', 0, 2, 0], #63
    ['Little Rock', 'Nashville', 7, 3, 0], #64
    ['Little Rock', 'New Orleans', 4, 3, 0], #65
    ['Little Rock', 'Saint Louis', 0, 2, 0], #66
    ['Los Angeles', 'San Francisco', 3, 3, 0], #67
    ['Los Angeles', 'San Francisco', 6, 3, 0], #68
    ['Los Angeles', 'Phoenix', 0, 3, 0], #69
    ['Miami', 'New Orleans', 1, 6, 0], #70
    ['Montreal', 'New York', 5, 3, 0], #71
    ['Montreal', 'Toronto', 0, 3, 0], #72
    ['Montreal', 'Sault St Marie', 8, 5, 0], #73
    ['Nashville', 'Saint Louis', 0, 2, 0], #74
    ['Nashville', 'Pittsburgh', 3, 4, 0], #75
    ['Nashville', 'Raleigh', 8, 3, 0], #76
    ['New York', 'Washington', 2, 2, 0], #77
    ['New York', 'Washington', 8, 2, 0], #78
    ['New York', 'Pittsburgh', 7, 2, 0], #79
    ['New York', 'Pittsburgh', 4, 2, 0], #80
    ['Oklahoma City', 'Santa Fe', 5, 3, 0], #81
    ['Phoenix', 'Santa Fe', 0, 3, 0], #82
    ['Pittsburgh', 'Saint Louis', 4, 5, 0], #83
    ['Pittsburgh', 'Toronto', 0, 2, 0], #84
    ['Pittsburgh', 'Washington', 0, 2, 0], #85
    ['Pittsburgh', 'Raleigh', 0, 2, 0], #86
    ['Portland', 'Seattle', 0, 1, 0], #87
    ['Portland', 'Seattle', 0, 1, 0], #88
    ['Portland', 'Salt Lake City', 5, 6, 0], #89
    ['Portland', 'San Francisco', 4, 5, 0], #90
    ['Portland', 'San Francisco', 6, 5, 0], #91
    ['Raleigh', 'Washington', 0, 2, 0], #92
    ['Raleigh', 'Washington', 0, 2, 0], #93
    ['Salt Lake City', 'San Francisco', 7, 5, 0], #94
    ['Salt Lake City', 'San Francisco', 2, 5, 0], #95
    ['Sault St Marie', 'Toronto', 0, 2, 0], #96
    ['Sault St Marie', 'Winnipeg', 0, 6, 0], #97
    ['Seattle', 'Vancouver', 0, 1, 0], #98
    ['Seattle', 'Vancouver', 0, 1, 0] #99
]



trains = [45 for _ in range(3)]
hands = [[] for _ in range(3)]
train_deck = [i+1 for i in range(8)]*12 + [-1 for _ in range(14)]
random.shuffle(train_deck)
visible_cards = train_deck[:5]

print(train_deck)
print(visible_cards)


def draw(card, player):
    global visible_cards, train_deck
    
    if card < 5:
        if card > len(visible_cards)-1:
            return False
        hands[player].append(visible_cards[card])
        train_deck.pop(card)
        visible_cards = train_deck[:5]
        return True
    elif len(train_deck) > 5:
        hands[player].append(train_deck[5])
        train_deck.pop(5)
        return True
    else:
        return False


def build(route, player, color):
    global routes, train_deck

    #print('Trying to build ', routes[route])
    if trains[player] <= routes[route][3]:
        return False
    if routes[route][2] == 0 or routes[route][2] == color:
        x = [i for i in hands[player] if i == color]
        #print(color, len(x))

        if routes[route][4] != 0:
            #print('Failed, someone else built')
            return False
        elif len(x) >= routes[route][3]:
            for _ in range(routes[route][3]):
                hands[player].remove(color)
            train_deck += [color]*routes[route][3]
            visible_cards = train_deck[:5]
            for _ in range(5):
                if len(train_deck) > 1:
                    train_deck.pop(0)
            random.shuffle(train_deck)
            train_deck = visible_cards + train_deck
            routes[route][4] = player+1
            trains[player] -= routes[route][3]

            for other_route in routes:
                if other_route[0] == routes[route][0] and other_route[1] == routes[route][1] and other_route != routes[route]: 
                    other_route[4] = -1

            print('Worked!')
        else:
            #print('Failed, not enough cards')
            return False
    else:
        #print('Failed, not the right color, the right color is ', routes[route][2])
        return False

destinations_deck = []

class GraphVisualization:
    def __init__(self):
        self.visual = []  # List to store edges and color indices
        self.positions = {}  # Dictionary to store node positions

    def addEdge(self, a, b, color):
        temp = (a, b, color)
        self.visual.append(temp)
        # Track the count of edges between the same cities

    def setNodePosition(self, node, position):
        # Assign a specific position to a node
        self.positions[node] = position

    def visualize(self):
        # Color map: index -> color
        color_map = {
            -1: 'black',
            0: 'gray',
            1: 'red',  
            2: 'green',
            3: 'blue',
            4: 'yellow'
        }

        G = nx.MultiGraph()  # MultiGraph allows multiple edges between nodes
        
        # Extract edges and corresponding colors
        edges = [(edge[0], edge[1]) for edge in self.visual]
        colors = [color_map[edge[2]] for edge in self.visual]  # Map numbers to colors
        
        G.add_edges_from(edges)

        pos = {'Atlanta': [1017,-511], 
       'Boston': [1240,-120],
       'Calgary': [268,-49],
       'Charleston': [1142,-512],
       'Chicago': [844,-302],
       'Dallas': [707,-645],
       'Denver': [481,-435],
       'Duluth': [720,-218],
       'El Paso': [465,-677],
       'Helena': [403,-227],
       'Houston': [763,-698],
       'Kansas City': [700,-410],
       'Las Vegas': [231,-540],
       'Little Rock': [801,-532],
       'Los Angeles': [144,-618],
       'Miami': [1185,-732],
       'Montreal': [1148,-40],
       'Nashville': [949,-465],
       'New Orleans': [890,-687],
       'New York': [1175,-222],
       'Oklahoma City': [670,-515],
       'Omaha': [679,-342],
       'Phoenix': [306,-607],
       'Pittsburgh': [1059,-281],
       'Portland': [60,-214],
       'Raleigh': [1105,-433],
       'Saint Louis': [824,-411],
       'Salt Lake City': [306,-392],
       'San Francisco': [40,-477],
       'Santa Fe': [471,-555],
       'Sault St Marie': [892,-130],
       'Seattle': [88,-145],
       'Toronto': [1037,-160],
       'Vancouver': [93,-72],
       'Washington': [1184,-343],
       'Winnipeg':[570,-62],
        }


        # Draw the nodes and labels
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos)

        # Draw each edge with a different curvature if it is a parallel edge
        edge_seen = defaultdict(int)  # Tracks how many times each edge has been drawn
        for i, edge in enumerate(edges):
            # Check how many times this edge has been drawn
            edge_key = (edge[0], edge[1]) if edge[0] < edge[1] else (edge[1], edge[0])
            edge_seen[edge_key] += 1

            # Apply curvature based on how many times we've seen this edge
            curvature = 0.08 * edge_seen[edge_key] * (-1)**int((i+1)%2)
            nx.draw_networkx_edges(
                G, pos, edgelist=[edge], edge_color=[colors[i]], width=3,
                connectionstyle=f'arc3, rad={curvature}', arrows=True  # Force FancyArrowPatch
            )
        
        plt.show()


def show_graph():
    board = GraphVisualization()
    for edge in routes:
        board.addEdge(edge[0], edge[1], edge[4])
    board.visualize()

#for i in range(100):
#    draw(0, random.randint(0,2))
for _ in range(100000):
    for pl in range(3):
        if random.random() > 0.7:
            draw(0, pl)
        else:
            built = False
            for col in range(9):
                if build(random.randint(1,99), pl, col):
                    built = True
            if not built:
                draw(0, pl)
print(trains)

show_graph()