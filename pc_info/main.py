# import itertools
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
import json




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
        x = request_data['id']

        room = int(x.split('-')[0])
        try:
            id1 = int(x.split('-')[1])
            devtest = True
        except (TypeError, ValueError) :
            id1 = x.split('-')[1]
            id2 = int(id1[2:])

            devtest = False

        if room == 102:
            try:
                df = pd.read_excel("IRDC-Lab-102-Inventory.xlsx")
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
                condition = df['Condition'].tolist()

                lst = list((SerialNumber, computerID, pcName, processor, memory, storage, oS, display,
                            softwareInstalled, users, diskPartition, condition))

                try:
                    templateHand = open('template.txt', 'r')
                except FileNotFoundError as fnfe:
                    response = "Seems to be a filing error! Please contact our support team! 001"
            except (FileNotFoundError, KeyError):
                response = "Seems to be a filing error! Please contact our support team! 000"
        elif room == 104:
            if devtest:
                try:
                    df = pd.read_excel("IRDC-Lab-104-Inventory.xlsx", 'PC')
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
                    condition = df['Condition'].tolist()

                    lst = list((SerialNumber, computerID, pcName, processor, memory, storage, oS, display,
                                softwareInstalled, users, diskPartition, condition))

                    try:
                        templateHand = open('template.txt', 'r')
                    except FileNotFoundError as fnfe:
                        response = "Seems to be a filing error! Please contact our support team! 002"


                except (FileNotFoundError, KeyError):
                    response = "Seems to be a filing error! Please contact our support team! 003"
            else:
                try:
                    df = pd.read_excel("IRDC-Lab-104-Inventory.xlsx", '3D')
                    SerialNumber = df['Serial Number'].tolist()
                    deviceID = df['3D Printer ID'].tolist()
                    deviceName = df['3D Printer Name'].tolist()
                    model = df['Model'].tolist()
                    modelYear = df['Model Year'].tolist()
                    power = df['Power'].tolist()
                    condition = df['Condition'].tolist()
                    details = df['Details of Condition'].tolist()
                    totTimeUsed = df['Total Time Used'].tolist()
                    sKB = df['Starter Kit Box'].tolist()

                    lst = list((SerialNumber, deviceID, deviceName, model, modelYear, power, condition, details,
                                totTimeUsed,sKB))

                    try:
                        templateHand = open('template2.txt', 'r')
                    except FileNotFoundError as fnfe:
                        response = "Seems to be a filing error! Please contact our support team! 004"
                except (FileNotFoundError, KeyError):
                    response = "Seems to be a filing error! Please contact our support team! 005"
        elif room == 107:
            try:
                df = pd.read_excel("IRDC-Lab-107-Inventory.xlsx")
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
                condition = df['Condition'].tolist()

                lst = list((SerialNumber, computerID, pcName, processor, memory, storage, oS, display,
                            softwareInstalled, users, diskPartition, condition))

                try:
                    templateHand = open('template.txt', 'r')
                except FileNotFoundError as fnfe:
                    response = "Seems to be a filing error! Please contact our support team! 006"



            except (FileNotFoundError, KeyError):
                response = "Seems to be a filing error! Please contact our support team! 007"

        else:
            response = "Seems to be a filing error! Please contact our support team! 008"






        if devtest:
            if x in computerID:
                try:

                    count = 0

                    out = ""
                    for line in templateHand:
                        line = line.rstrip()
                        if count<12:
                            out += line + "\t" + str(lst[count][id1 -1]) + "\n"
                            print(line + "\t" + str(lst[count][id1 -1]))
                        else:
                            print(softwareInstalled)
                            sI = softwareInstalled[id1 -1].split('|')
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

        else:
            if x in deviceID:
                try:
                    count = 0
                    out = ""
                    for line in templateHand:
                        line = line.rstrip()
                        out += line + "\t" + str(lst[count][id2 - 1]) + "\n"
                        print(line + "\t" + str(lst[count][id2 - 1]))
                        count = count + 1
                    response = out
                    print("\n")
                    return " "

                except TypeError as te:
                    response = "This is an incorrect data type "
                    return " "

    else:
        return jsonify('id', response)


if __name__ == "__main__":
    app.run(debug=True)
