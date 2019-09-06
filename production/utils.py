""" 
#Setup and Usage

import utils

#Dependencies/Libs

import datetime
import os
import pandas as pd


""" 
    """
    Your code
    ... 
    utils.log_message(type_msg, id_program, function_name, system_msg, log_msg)
    utils.log_message(String, String, String, String, String)

    utils.writeDataToExcel(data, columns, outputDir, file_name, date)
    writeDataToExcel(list, list, String, String, String)"""

"""

#version
 * 0.0.1 - Write log in a fixed file
 * 0.0.2 - Write log in a dinamic file based on type of msg,
           Logged at the same yourProgramPath/logs
 """
#import Libs
import datetime
import os
import pandas as pd

#Variables
#You can alter the path of the folder 
folder = "logs"


def log_message(type_msg, id_program, function_name, system_msg, log_msg):
    #pegar o nome do programa/codigo e criar um arquivo de log para ele

    #time_log
    now = datetime.datetime.now()
    date = now.strftime('%d_%m_%Y')
    time = now.strftime("%H:%M:%S")

    # define the name of the directory to be created
    fullPath = os.getcwd()+"/"+folder+"/"

    # define the access rights
    access_rights = 0o755
    if not os.path.exists(folder):
        os.mkdir(fullPath, access_rights)
    
    #arquivo a ser gerado
    # arquivo de log = id_programa_date_log
    out_name_file = fullPath + id_program + "-" + date + "-" + type_msg +"-log.txt"
    string_msg = str(type_msg + " | " + date + " | " + time + " | " + function_name + " | " + log_msg + "\n")

    #open the file as writea/append mode
    try:
        with open(out_name_file, 'a+') as my_file:
            #print("abriu ->", out_name_file)
            if system_msg == "":
                my_file.write(string_msg)
            else:
                string_msg = "" + type_msg + " | " + date + " | " + time + " | " + function_name + " | " + system_msg + " | " + log_msg + "\n"
                my_file.write(string_msg)
    except IOError as error:
        my_file.write("%s|%s|%s|%s|%s\n" % (type_msg, date, time, function_name, error))
    finally:
        my_file.close()

def writeDataToExcel(data, columns, outputDir, file_name, date):
    #outputDir = "/home/daniel/Documents/projetos_py/logs"
    #data = ["Teste", "teste2", "teste3"]
    #columns = ["dados"]
    #print(data, columns, outputDir, file_name, date)
    result = False
    try:
        table = pd.DataFrame(data, columns=columns)
        outputname = outputDir+file_name+"_"+date+'.xlsx'
        writer = pd.ExcelWriter(outputname)
        table.to_excel(writer, date)
        writer.save()
        result = True
    except Exception as error:
        print("Erro na gravacao do arquivo: %s"%outputname)
        print("------ Erro: %s"%error)
    finally:
        if result:
            print("File: %s | %s | Gravado com sucesso."%(date, outputname))
