"""
q1ph writing as Dr Keith Reid
26 March 2024
exmple code for Eme
"""

import networkx as nx
import matplotlib.pyplot as plt

def get_testing_or_not():
    testing_or_not = "yes"
    return testing_or_not

def get_values():
    values = ["Quietness", "Patience","Loving\nAnimals"]
    return values

def draw_values():
    subax1 = plt.subplot(111)
    nx.draw(values_chart, with_labels=True, font_weight='bold')
    print("Close the drawing down to end the program and maybe run tests :)")
    plt.show()

if __name__ == "__main__":
                 
    values_chart   = nx.Graph()
    values         = get_values()
    
    values_chart.add_nodes_from(values)
    values_chart.add_edge(values[1], values[2])
    
    draw_values()

def test_get_values():
    values = get_values()
    assert type(values)==list, "Should be a list of strings"
    assert type(values[0])==str, "Should be a string"

def tests():
    testing_or_not = get_testing_or_not()
    if testing_or_not == "yes":
        test_get_values()
        print("passed all tests")

tests()
