import boto3
import pandas as pd 
 
df = pd.read_excel('ssmparams.xlsx',sheet_name='Sheet1')
print(df.head())

ssm = boto3.client('ssm')
def parameter_add():
    try:
        res = ssm.put_parameter(
            Name = '/divyaproject/db2/{}'.format(df['Name'].loc[0]),
            Value = df['value'][0],
            Type = df['type'][0],
            Overwrite = False
            )
        print('Successful')
    except Exception as e:
        if "ParameterAlreadyExists" in str(e):
            print('Parameter already exists')
                

parameter_add()


