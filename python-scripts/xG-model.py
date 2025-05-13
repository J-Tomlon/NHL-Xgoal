import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt  

def main():
    
    shots2023 = pd.read_csv("./raw-data/shots_2023.csv")

    test = shots2023[-['shotID', 'xCord', 'yCord']]
    print(test)
main()