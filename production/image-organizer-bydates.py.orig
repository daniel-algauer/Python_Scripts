""" 
# python3.6+
# Program: image-organizer-bydates.py
# Name: ImageOrganizer
# Description: This program copie every image on certain folder and organize byDates with the exif data, if founded.
#              This program also uses utils.py to create a log files.
#              For details on how to execute, plase go to def main():
# versão: 1.2
# Dependencies: os, datetime, pandas as pd, numpy as pd
# Created: 06/28/2019 
# Last Modified: 10/15/2019
# Modifications: log in excel generated with utils
#
 """
import os, datetime, sys, shutil
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import pandas as pd
import numpy as np
import utils
ID_PROGRAM = "ImageOrganizer"

""" 
TYPES_FILES = [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".7z", ".arj",
".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip", ".bin", ".dmg", ".iso", ".toast", ".vcd", ".csv", ".dat",
".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml", ".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe",
".gadget", ".jar", ".py", ".wsf", ".fnt", ".fon", ".otf", ".ttf", ".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png",
".ps", ".psd", ".svg", ".tif", ".tiff", ".asp", ".aspx", ".cer", ".cfm", ".cgi", ".pl", ".css", ".htm", ".html", ".js", ".jsp",
".part", ".php", ".py", ".rss", ".xhtml", ".key", ".odp", ".pps", ".ppt", ".pptx", ".c", ".class", ".cpp", ".cs", ".h", ".java",
".sh", ".swift", ".vb", ".ods", ".xlr", ".xls", ".xlsx", ".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns",
".ico", ".ini", ".lnk", ".msi", ".sys", ".tmp", ".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg",
".mpeg", ".rm", ".swf", ".vob", ".wmv", ".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".wpd"] 
"""

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found.")
    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == "GPSInfo":
            if idx not in exif:
                raise ValueError("No EXIF geotagging found.")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
    return geotagging

def getParamsImg(file_path):
    result = {}
    #time of most recent content modification
    recent_mod_file = datetime.datetime.fromtimestamp(os.stat(file_path).st_mtime).strftime("%Y/%m/%d")
    #platform dependent; time of most recent metadata change on Unix, or the time of creation on Windows
    recent_meta_file = datetime.datetime.fromtimestamp(os.stat(file_path).st_ctime).strftime("%Y/%m/%d")
    dates = {
        "DateRecentModification": recent_mod_file,
        "DateRecenteMetadaCreation": recent_meta_file
    }
    result["FilePath"] = file_path
    result["Msg"] = ""
    msg_err = ""
    try:
        working_img = Image.open(file_path)
        working_img.verify()
        working_img = Image.open(file_path)
        exif = working_img._getexif()
        working_img.close()
        if not exif:
            result["Msg"] = "Exif data not found."
        else:
            for (key, val) in exif.items():
                decoded = TAGS.get(key, key)
                if key in TAGS:
                    if "Date" in decoded:
                        val = datetime.datetime.strptime(val, "%Y:%m:%d %H:%M:%S").strftime("%Y/%m/%d")
                        dates[decoded] = val
                    else:
                        result[decoded] = val
                else:
                    msg_err = "No TAG Identified: " + str(key) + " | decoded: " + str(decoded)
    except (IOError, EOFError, ValueError, Exception) as err:
        msg_err = str(sys.exc_info()[0])
        msg_err = str(file_path) + str("|") + str(err) + str("|") + str(msg_err)
        utils.log_message("NOK", ID_PROGRAM, "getParameters", "", msg_err)
    except ValueError as error:
        msg_err = str(error)
        utils.log_message("NOK", ID_PROGRAM, "getParameters", "", msg_err)
    finally:
        #if working_img:
        if not result["Msg"]:
            result["Msg"] = msg_err
    dates["DateOldest"] = setOldestDate(dates)
    result["Dates"] = dates
    if result:
        utils.log_message("OK", ID_PROGRAM, "getParameters", "", "Parameters OK.")
    return result

def setOldestDate(dates):
    aux = {}
    for (i, j) in dates.items():
        aux[i] = j
    minimo = min(aux, key=aux.get)
    result = aux[minimo]
    return result

def removeTags(list_tags):
    tags = ["MakerNote", "Copyright", "UserComment"]
    new_list = {}
    for (key, val) in list_tags.items():
        if not key in tags:
            new_list[key] = val
        else:
            utils.log_message("OK", ID_PROGRAM, "removeTags", "", "Tag " + key + " removed.")    
    utils.log_message("OK", ID_PROGRAM, "removeTags", "", "Tags removed.")
    return new_list

def saveCopyFileImg(filename, params, output_folder, last_folder):
    to_folders = {
        "year": "",
        "month": "",
        "day": ""
    }
    files_copied = ""
    for (key, val) in params.items():
        if "Dates" in key:
            for (i, j) in val.items():
                if i == "DateOldest":
                    to_folders["year"] = datetime.datetime.strptime(j, "%Y/%m/%d").strftime("%Y")
                    to_folders["month"] = datetime.datetime.strptime(j, "%Y/%m/%d").strftime("%B")
                    to_folders["day"] = datetime.datetime.strptime(j, "%Y/%m/%d").strftime("%d")
    destine_dir = str(output_folder + to_folders["year"] + "/" + to_folders["month"] + "/")
    if last_folder:
        destine_dir = str(output_folder + to_folders["year"] + "/" + to_folders["month"] + "/" + last_folder + "/") 
    try:
        if not os.path.isdir(destine_dir):
            os.makedirs(os.path.dirname(destine_dir), mode=0o777)
        name = os.path.basename(filename)   
        destine_dir = destine_dir + name
        shutil.copy2(filename, destine_dir)
        file_copied = True
    except (IOError, EOFError, ValueError, Exception) as err:
        msg_err = str(sys.exc_info()[0])
        utils.log_message("NOK", ID_PROGRAM, "saveCopyFile", msg_err, err)  
    
    if file_copied:
        msg_result = str("Saved to: (" + destine_dir + ")")
        utils.log_message("OK", ID_PROGRAM, "saveCopyFile", msg_result, "OK")
    return file_copied

    

def findFiles(rootFolder, typesFiles, output_folder):
    list_files = []
    last_folder = ""
    result = False
    print("Escanning folder: " + rootFolder)
    for root, dirs, files in os.walk(rootFolder):
        for name in files:
            file_to_write = os.path.join(root, name)
            if file_to_write.endswith(tuple(typesFiles)):
                params = removeTags(getParamsImg(file_to_write))
                last_folder = os.path.basename(os.path.normpath(root))
                if last_folder == rootFolder:
                    last_folder = ""
                try:
                    result = saveCopyFileImg(file_to_write, params, output_folder, last_folder)
                    #print(file_to_write, params, output_folder, last_folder)
                    list_files.append(file_to_write)
                except Exception as identifier:
                    utils.log_message("NOK", ID_PROGRAM, "findFiles", "File not copied: " + file_to_write, str(identifier))
                    continue
            else:
                utils.log_message("NOK", ID_PROGRAM, "findFiles", "File format not identified: ", file_to_write)
    if result: 
        utils.log_message("OK", ID_PROGRAM, "findFiles", "Finished", str(result))
    return list_files

def main():
    #change this to your root folder you would like to scan for images
    rootFolder = "/Pictures/"
    
    #change this to the folder you would like to save the new structure - Copied images
    output_folder = "/Results/"
    
    #change this to any image type you want/or not to copie
    type_files = [".png", ".jpg", ".jpeg", ".raw", ".cr2", ".CR2", ".JPG", ".JPEG", ".png", ".PNG", ".ttf", ".ai", ".bmp", ".gif", ".ico", ".ps", ".psd", ".svg", ".tif", ".tiff"]
    
    #Find files and copie, main function - returns de list of files copied
    files_results = findFiles(rootFolder, type_files, output_folder)
    
    #change this to the folder you would like to save your logs
    outputDirLogs = "/logs/"

    #this creates an excel file with your images + path you copied
    columns = ["Saved images"]
    filename = "file_name"
    date = datetime.datetime.today().strftime("%Y_%m_%d")
    utils.writeDataToExcel(files_results, columns, outputDirLogs, filename, str(date))
    
    #end of program
    if files_results:
        print("End of program")
        print("Files copied to: ", output_folder)

if __name__ == "__main__":
    main()
