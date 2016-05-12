from openpyxl import load_workbook
from sys import argv
import os, xlrd, csv
from wideReader import wideReader
from longReader import longReader
from traceback import print_exc
from salute import salute

def main(filepath):
    #  toma un path a un archivo de excel con IMEIS y
    #  crea un archivo csv con el formato apropiado
    #  para subirlo a la pagina de la Arcotel.

    print salute
    directory = os.path.dirname(filepath)

    #  read excel and create a dictionary of imeis and serial numbers
    imeiDictionaryList = readExcelFile(filepath)

    if imeiDictionaryList:
        #split the list of dictionaries into sublists of 100 elements
        imeiDictionaryList = splitImeiList(imeiDictionaryList)

        #create a file for each sublist
        nfile = 1
        for dictList in imeiDictionaryList:
            filename = "imeiList"+str(nfile)+".csv"
            createCsvFile(dictList, directory, filename)
            nfile+=1
    else:
        print "Sorry, I couldn't create the IMEI file."


def readExcelFile(filepath):
    #takes in a path to a excel file and returns
    #a list of dictionaries of imeis and serials.

    wb = xlrd.open_workbook(filepath)
    sh = wb.sheet_by_index(0)
    #Determines the template of the excel file and
    #Decides which function to use in parsing
    if sh.ncols > 1:
        imeiList = wideReader(sh)
    else:
        imeiList = longReader(sh)
    return imeiList


def splitImeiList(dictList):
    #takes a list of dictionaries and
    #returns a list of lists of no more than 100 dictionaries

    splitDictList = []
    tempList = []
    n_element = 1

    for d in dictList:
        if len(tempList) >= 100:
            splitDictList.append(tempList)
            tempList = []
            tempList.append(d)
        else:
            tempList.append(d)
            if n_element == len(dictList): #if it is the las element of the list, add and return
                splitDictList.append(tempList)
                return splitDictList

        n_element+=1
    return splitDictList 



def createCsvFile (dictList, directory, filename):
    #creates an Arcotel formatted csv file in the selected directory
    newcsv = open(directory + "/"+filename, mode='w')
    nelements = len(dictList)
    n_element = 1               #counter of records written

    if dictList[0].has_key('imei2'):    #this is a two-IMEI file
        for d in dictList:
            if n_element == nelements:
                newcsv.writelines(d['imei1']+","+d['serial']+'\n')
                newcsv.writelines(d['imei2']+","+d['serial'])
            else:
                newcsv.writelines(d['imei1']+","+d['serial']+'\n')
                newcsv.writelines(d['imei2']+","+d['serial']+'\n')
            n_element+=1
    elif dictList[0].has_key('serial'): #this is a normal IMEI file
        for d in dictList:
            if n_element == nelements:
                newcsv.writelines(d['imei1']+','+d['serial'])
            else:
                newcsv.writelines(d['imei1']+','+d['serial']+'\n')
            n_element+=1
    
    print "Your CSV File: %s is ready. %i records added." %(filename, len(dictList))

    return

if __name__ == "__main__":
    try:
        #filepath = 'D:/myScripts/csvmaker/testfiles/wide1.XLS'
        filepath = argv[1]
        main(filepath)
        raw_input(" ")
    except:
        print_exc() 
        raw_input('')
