# Stock App project
This project calculates taxes and measured result of stock transactions

## Requirements
The following requirements are needed to run the application
- python 3.11
- Install python modules in _requirements.txt_

Ex:
```
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Project structure
In this section the structure of folders and files of the project will be explained

### Artifacts folder
By default, the output files of the application, such as graphs and tables are saved in the folder **./artifacts**

### Stock Calculator folder
The calculator module, that parsers the input csv files and performs the calculations is in the **./stock_calculator** folder. 
This module defines two implementations of the calculation logic, one using the basic resources of python, and another using the resources of the Pandas framework.
The first was used for validation and comparison purposes only.

### Presentation folder
In the **./presentation** folder is the module that defines the creation of exported views, both for csv files and graphics in png and html format

### Tests folder
In the **./tests** folder, tests were developed that test the two calculator implementations for the two csv files provided in the specification file
