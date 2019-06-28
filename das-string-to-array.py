""" 
# This function receives a .txt file as input.
# The function extracts the text on every "." find and splits for each row.
# a table is printed as columns title | date+time
# python3.6+
# Program: das-string-to-array.py
# Description: Print text strings based on separator numpy output example
# versão: 1.0
# Dependencies: os, datetime, pandas as pd, numpy as pd
# Created: 28/06/2019 
# Last Modified: 28/06/2019
# Modifications:
#
 """
#imports
import os, datetime
import pandas as pd
import numpy as numpy

def main():
    ## Variable
    # Total of columns and their names, should be in acoordance with the size and type of results
    columns = ["Date", "Title"]
    #results array with the lines readed on the input file
    result = []
    #data do arquivo, hoje
    date = datetime.datetime.now().strftime('%d.%m.%Y')
    time = datetime.datetime.now().strftime('%X')
    date = date + "|" + time

    #inputFilePath = input("Type the path+file to extract the text (ex.: /home/usr/file_name.txt): ")
    #use one or another
    inputFilePath = "teste.txt"

    #open file
    f = open(inputFilePath, "r")
    #read all the file as one string.
    inputString = f.read().strip()
    #close file
    f.close()

    #Split text based on some pattern.
    pattern = "."
    inputTxt = inputString.rstrip().strip().lstrip().split(pattern)

    #for len total string to read (-1 because the text ends with '.')
    for i in range(len(inputTxt)-1):
        #print("Total reg.: {} Loop:{} : {}".format(len(inputTxt)- 1, i, inputTxt[i]))
        try:
            str_act = inputTxt[i]
            if not str_act == "":
                newLine = str_act.strip()
                lines = [date, newLine]
                result.append(lines)
        except Exception as error:
            print("--- Error -E: %s"%error)
            continue
        finally:
            dataTable = pd.DataFrame(result, columns=columns)
    try:
        print("------------------ Convert text files separeted by '.' or 'any sep'in excel cells -------------------")
        print("---- Execution for: {} itens.\n".format(len(inputTxt)-1))
        print("---- Results:")
        print(dataTable)
    except Exception as error:
        print("--- Error -E:.%s"%error)
    finally:
        print("\n---- Success. %i lines printed."%(len(dataTable)))

if __name__ == "__main__":
    main()
