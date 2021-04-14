# import itertools
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
import json
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

id1 = ''
out = ''
# flutter post and get section
app = Flask(__name__)


@app.route('/id', methods=['GET', 'POST'])
def idRoute():
    global id1
    global out
    global response

    if request.method == 'POST':

        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        id1 = request_data['id']

        lst = list((SerialNumber, computerID, pcName, processor, memory, storage, oS, display))
        np_array = np.array(lst)
        transpose = np_array.T
        tp_lst = transpose.tolist()
        try:
            templateHand = open('template.txt', 'r')
        except FileNotFoundError as fnfe:
            response = "Seems to be a filing error! Please contact our support team!"

        # This is temporary. The serial no. is currently just an auto number and later will be
        # customised and the scanner app will be used to extract the value from the QR code
        # x = int(input("Input the serial number of the Device:\t"))
        x = id1
        print(SerialNumber)
        if x in SerialNumber or x == -1:
            try:

                count = 0
                if x == -1:
                    print("{:<12} {:<12} {:<8} {:<20} {:<10} {:<15} {:<15} {:<25} ".format('Serial Number', 'Computer ID',
                                                                                           'PC Name',
                                                                                           'Processor', 'Memory (RAM)',
                                                                                           'Storage', 'OS',
                                                                                           'Display'))
                    out = "{:<12} {:<12} {:<8} {:<20} {:<10} {:<15} {:<15} {:<25} ".format('Serial Number', 'Computer ID',
                                                                                           'PC Name',
                                                                                           'Processor', 'Memory (RAM)',
                                                                                           'Storage', 'OS',
                                                                                           'Display')

                    print("\n")
                    for a, b, c, d, e, f, g, h in tp_lst:
                        print("{:<12} {:<12} {:<8} {:<20} {:<10} {:<15} {:<15} {:<25} ".format(a, b, c, d, e, f, g, h))
                        print("\n")
                        out += "{:<12} {:<12} {:<8} {:<20} {:<10} {:<15} {:<15} {:<25} ".format(a, b, c, d, e, f, g, h) + "\n"
                    response = out
                else:
                    out = ""
                    for line in templateHand:
                        line = line.rstrip()
                        if count<8:
                            out += line + "\t" + str(lst[count][x - 1]) + "\n"
                            print(line + "\t" + str(lst[count][x - 1]))
                        else:
                            print(softwareInstalled)
                            sI = softwareInstalled[x-1].split('|')
                            for y in sI:
                                print('\t\t', y, '\n')
                        count = count + 1
                    response = out
                print("\n")
                return " "





            except TypeError as te:
                response = "This is an incorrect data type "
                return " "

        else:
            response = "This is not our PC or this QR code is not supported..."
            return " "
    else:
        return jsonify('id', response)


if __name__ == "__main__":
    app.run(debug=True)
