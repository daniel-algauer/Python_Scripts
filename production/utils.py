#import Libs
import datetime
import os
import pandas as pd

#You can alter the path of the folder to any place you want.
folder = "logs"

def log_message(type_msg, id_program, function_name, system_msg, log_msg):
    #get id_program and creates a new log file / OK or NOK
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
        print("Error on create file: %s"%outputname)
        print("------ Error: %s"%error)
    finally:
        if result:
            print("File: %s | %s | copied."%(date, outputname))
