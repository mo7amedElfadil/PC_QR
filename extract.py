import itertools
import pandas as pd

df = pd.read_excel("file.xlsx")
SerialNumber = df['Serial Number'].tolist()
ComputerID = df['Computer ID'].tolist()
PCName = df['PC Name'].tolist()
Processor = df['Processor'].tolist()
Memory = df['Memory'].tolist()
Storage = df['Storage'].tolist()
OS = df['OS'].tolist()
Display = df['Display'].tolist()


templateHand = open('template.txt', 'r')

for i in range(len(SerialNumber)):
    for line in templateHand:
        line=line.rstrip()
        words= line.split()
        print(line + ": " + SerialNumber[i])
