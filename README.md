# Python Scripts

Here goes some useful scripts developed along the years with python.


## Table of contents
* [Write Action As Log](#write-action-as-log)
* [Release_History](#release-history)
* [Author](#author)

## Write Action As Log

This function receives some parameters and creates a txt file with the log of the operations.

### Setup and Usage
#### Setup
```python
import writelog as writelog
#Import the function calling the import on your code
```

```python
writeActionAsLog.py
#Change the value of the variable folder for new name
folder = "name_folder"
#Or change all the path of the file that will be saved with the log. If you leave in blank, the path will be relative with the executed file.
path = ""
#to
path = "/home/user/Documents/your_folder"
```

#### Usage

Call the the function with the proper arguments.
```python
writeLog(type_msg, id_program, system_msg, log_msg)

# type_msg: Type of the returned message. Possible Values = OK or NOK
# id_program: Name of the program/code you would like to log.
# system_msg: Error message, captured by the system Excepctions.
# log_msg: Custom message 
```
Just call the function passing the arguments.

```python
if TRUE:
    writeLog("OK", "id_program1", "", "Successfully.")
else:
    writeLog("NOK", "id_program1", "", "Error.")
```

or

```python
try:
    writeLog("OK", "id_program1", "", "Successfully.")
exception IOError as error:
    writeLog("NOK", "id_program1", error, "")
```
## Release History

* 0.0.1
  * Work in progress.
## Author
Created by @Daniel Algauer
