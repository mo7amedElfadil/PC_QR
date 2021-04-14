import pandas as pd
import numpy as np

try:
    df = pd.read_excel("IRDC_Lab_107_Inventory.xlsx")
    SerialNumber = df['Serial Number'].tolist()
    computerID = df['Computer ID'].tolist()
    pcName = df['PC Name'].tolist()
    processor = df['Processor'].tolist()
    memory = df['Memory (RAM)'].tolist()
    storage = df['Storage'].tolist()
    oS = df['OS'].tolist()
    display = df['Display'].tolist()
    softwareInstalled = df['Software Installed'].tolist()
    users = df['Users'].tolist()
    diskPartition = df['Disk Partition'].tolist()

except (FileNotFoundError, KeyError):
    response = "Seems to be a filing error! Please contact our support team!"





for x in softwareInstalled:
    sI = x.split('|')
    for y in sI:
        print('\t\t' , y , '\n')
