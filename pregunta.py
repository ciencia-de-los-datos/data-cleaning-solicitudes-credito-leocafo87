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


    #Limpiar Campo línea_credito
    df['línea_credito'] = df['línea_credito'].str.replace('.','',regex=True)
    df['línea_credito'] = df['línea_credito'].str.replace('-','',regex=True)
    df['línea_credito'] = df['línea_credito'].str.replace('_','',regex=True)
    df['línea_credito'] = df['línea_credito'].str.replace(' ','',regex=True)

    #Limpiar Campo idea de negocio
    df['idea_negocio'] = df['idea_negocio'].str.replace('.','',regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.replace('-','',regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.replace('_','',regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.replace(' ','',regex=True)

    #Limpiar Campo tipo_de_emprendimiento
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace('.','',regex=True)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace('-','',regex=True)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace('_','',regex=True)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace(' ','',regex=True)

    #Limpiar Campo barrio
    df['barrio'] = df['barrio'].str.replace('.','',regex=True)
    df['barrio'] = df['barrio'].str.replace('-','',regex=True)
    df['barrio'] = df['barrio'].str.replace('_','',regex=True)
    df['barrio'] = df['barrio'].str.replace(' ','',regex=True)

    #Limpiar Campo monto_del_credito
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$','',regex=True)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','',regex=True)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(' ','',regex=True)
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x[0:x.find('.')+1] if x.find('.') != -1 else x)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('.','',regex=True)

    #Limpiar la fecha
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], infer_datetime_format=True)

    #eliminar registos con campos vacios
    df = df.dropna()

    #Eliminamos duplicados
    df = df.drop_duplicates()

    return df
