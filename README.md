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

#### Usage

Call the the function with the proper arguments
```python
writeLog(type_msg, id_program, system_msg, log_msg)

# type_msg: Type of the returned message. Possible Values = OK or NOK
# id_program: Name of the program/code you would like to log.
# system_msg: Error message, captured by the system Excepctions.
# log_msg: Custom message 
```
When need, just call the function passing the arguments

```python
if TRUE:
    writeLog("OK", "id_program1", "", "Successfully.")
else:
    writeLog("NOK", "id_program2", "", "Error.")
```

or

```python
try:
    writeLog("OK", "id_program1", "", "Successfully.")
exception IOError as error:
    writeLog("NOK", "id_program2", error, "")
```
## Release History

* 0.0.1
  * Work in progress
## Author
Created by @Daniel Algauer
