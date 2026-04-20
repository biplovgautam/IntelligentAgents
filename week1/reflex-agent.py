A = (0,0)
B = (0,1)

def reflex_agent(percept):
    location, status = percept
    if status == "Dirty":
        return "Clean"
    elif location == A:
        return "Right"
    elif location == B:
        return "left"
    
def run():
    print(reflex_agent((A,"Dirty")),)
    print(reflex_agent((A,"Clean")),)
    print(reflex_agent((B,"Dirty")),)
run()