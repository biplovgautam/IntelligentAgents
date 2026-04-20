# #table driven agent
# A = (0, 0)
# B = (1, 0)
# percepts = []
# table = {
#     ((A, 'Clean'),): 'Right',
#     ((A, 'Dirty'),): 'Clean',
#     ((B, 'Clean'),): 'Left',
#     ((B, 'Dirty'),): 'Clean',

#     ((A, 'Dirty'), (A, 'Clean')): 'Right',
#     ((A, 'Clean'), (B, 'Dirty')): 'Clean',
#     ((B, 'Clean'), (A, 'Dirty')): 'Clean',
#     ((B, 'Dirty'), (B, 'Clean')): 'Left',

#     ((A, 'Dirty'), (A, 'Clean'), (B, 'Dirty')): 'Clean',
#     ((B, 'Dirty'), (B, 'Clean'), (A, 'Dirty')): 'Clean',
# }

# def lookup_table(percepts, table):
#     action = table.get(tuple(percepts))
#     return action

# def table_driven_agent(percept):
#     percepts.append(percept)
#     action = lookup_table(percepts, table)
#     return action

# def run():
#     print(table_driven_agent((A, 'Dirty')), percepts)
#     print(table_driven_agent((A, 'Clean')), percepts)
#     print(table_driven_agent((B, 'Dirty')), percepts)

# run()



#### cw
A = (0,0)
B = (0,1)
C = (1,1)
percept=[]
table = {
    ((A,"Clean"),):"Right",
    ((A,"Dirty"),):"Clean",
    ((C,"Clean"),(B,"Clean"),):"Left",
    ((B,"Dirty"),(B,"Clean"),):"Left",
    ((A,"Clean"),(B,"Clean"),):"Right",
    ((B,"Dirty"),):"Clean",
    ((C,"Clean"),):"Left"

}

def lookup_table(history):
    action = table.get(tuple(history))
    return action

def table_driven_agent(percept):
    history.append(percept)
    action = lookup_table(history)
    return action