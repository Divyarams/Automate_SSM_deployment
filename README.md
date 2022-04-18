# Automate_SSM_deployment

When we have parameters stored in Excel files and need to create SSM paramaters, use the code to automate deployment to SSM Parameter.
The format of the headers in excel file should be Name, type and value. Make sure valid string, SecureString entries are given in each cell.

Load the data in an dataframe and perform operations for split and strip if necessary. Once loaded in dataframe, reference the value in SSM boto3 function call as arguments.

The Python code is written with Exception handling try and except commands.
