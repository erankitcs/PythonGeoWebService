import pandas
from get_geocode import getgeocode

def read_csvfile(filename):
    df=pandas.read_csv(filename,skipinitialspace=True)

    if 'Address' in df.columns:
        col_name='Address'
    elif 'address' in df.columns:
        col_name='address'
    else:
        msg="Given files does not contain Address or address column"
        return (1,msg,col_name)

    df["Location"]=df[col_name].apply(getgeocode)
    df["Latitude"]=df["Location"].apply(lambda x: x.latitude if x !=None else None)
    df["Longitude"]=df["Location"].apply(lambda x: x.longitude if x !=None else None)
    df = df.drop('Location', 1)
    #print(df)
    msg="File processed."
    return (0,df,col_name)

#print(read_csvfile("location1.csv"))
