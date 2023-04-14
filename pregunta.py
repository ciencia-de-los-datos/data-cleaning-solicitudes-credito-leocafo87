"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    #df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    column_names = ["id","sexo","tipo_de_emprendimiento","idea_negocio","barrio","estrato","comuna_ciudadano","fecha_de_beneficio","monto_del_credito","línea_credito"]
    df = pd.read_csv("solicitudes_credito.csv", sep=";", skiprows=1,names=column_names)

    #Elimina la col id
    df = df.drop('id', axis=1)

    #Convertir todo a minusculas
    df = df.applymap(lambda s: s.lower() if type(s) == str else s)
    
    # Date check  
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True)
    
    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)

    # Lowercase check
    df['sexo'] = df['sexo'].str.lower().astype(str).str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
     
    # Whitespaces, hyphen and underscore checks
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()

    # Money check
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)   
    
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)

    #eliminar registos con campos vacios
    df = df.dropna()

    #Eliminamos duplicados
    df = df.drop_duplicates()

    return df
