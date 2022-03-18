import pandas as pd
import itertools




df = pd.read_csv(
        r"C:\Users\9820937G\OneDrive - SNCF\Bureau\export - 2021-10-07T163521.355.csv",
        sep=";")
    
    
    
df.pop("date_capture_socle")


    
    
df.replace()
    
df["segment_scheduleInformation_departureDate"] = df[
        "segment_scheduleInformation_departureDate"].str[:10]

   
    
    
df["segment_scheduleInformation_departureDate"] = pd.to_datetime(
        df["segment_scheduleInformation_departureDate"])


df= df.loc[
    (df["segment_scheduleInformation_departureDate"] >= '2021-08-31')
    &
    (df["segment_scheduleInformation_departureDate"]<= '2021-08-31')
    &
    (df["segment_transportationServiceOffer"] =='TGV')
    ] 

    
df["date_capture"] = pd.to_datetime(
        df["date_capture"])

    
df["Nombre_de_reservations_actives_payees"].astype(int)
    
df["CA_reservations_actives_payees"
       ]=df["CA_reservations_actives_payees"
       ].str.replace(',','.'
                     ).astype(float)
    
pd.to_numeric(df["CA_reservations_actives_payees"], errors='coerce').isnull()          

df["Cumul_CA_reservations_actives_payees"
       ]=df["Cumul_CA_reservations_actives_payees"
       ].str.replace(',','.'
                     ).astype(float)
    
pd.to_numeric(df["Cumul_CA_reservations_actives_payees"], errors='coerce').isnull()            
            
df = df[[   "segment_transportationServiceOffer",
         "product_fareCode",
             "segment",
        "segment_scheduleInformation_departureDate",
            "date_capture",             
             "Nombre_de_reservations_actives_payees",
             "CA_reservations_actives_payees",
             "Cumul_Nombre_de_reservations_actives_payees",
             "Cumul_CA_reservations_actives_payees"]]

df=df.groupby(["segment_transportationServiceOffer",
         "product_fareCode",
             "segment",
        "segment_scheduleInformation_departureDate",
        "date_capture"]).sum(["Nombre_de_reservations_actives_payees",
          "CA_reservations_actives_payees",
           "Cumul_Nombre_de_reservations_actives_payees",
            "Cumul_CA_reservations_actives_payees"])

df.reset_index(inplace=True, level=["segment_transportationServiceOffer",
         "product_fareCode",
             "segment",
        "segment_scheduleInformation_departureDate",
        "date_capture"])

df.to_html(r"C:\Users\9820937G\OneDrive - SNCF\Bureau\my_html1.html",
           columns=[ 
               "segment_transportationServiceOffer",
         "product_fareCode",
             "segment",
        "segment_scheduleInformation_departureDate",
            "date_capture",             
             "Nombre_de_reservations_actives_payees",
             "CA_reservations_actives_payees",
             "Cumul_Nombre_de_reservations_actives_payees",
             "Cumul_CA_reservations_actives_payees"])

    
dt = pd.date_range('08/01/2021 00:00:00', '08/01/2021 12:00:00',
                       freq='H').strftime("%d/%m/%Y %H:%M:%S").tolist()
    
    
fare_codes = df["product_fareCode"].unique()
segments = df["segment"].unique()
segmenttrans = df["segment_transportationServiceOffer"].unique()
dateheuredepart = df["segment_scheduleInformation_departureDate"].unique()
    
    
da = pd.DataFrame(itertools.product(dt,
                                        fare_codes,
                                        segments,
                                        segmenttrans,
                                        dateheuredepart))

da[0] = pd.to_datetime(da[0])
da.rename(columns={0: 'date_capture',
                       1: 'product_fareCode',
                       2: 'segment',
                       3: 'segment_transportationServiceOffer',
                       4: 'segment_scheduleInformation_departureDate'},
              inplace=True)


ds = da.merge(df, on=['segment_transportationServiceOffer',
                      'product_fareCode',
                      'segment',
                      'segment_scheduleInformation_departureDate'
                       ], how="left")

ds.pop("date_capture_y")
ds.rename(columns={'date_capture_x': 'date_capture'},inplace=True)

ds.sort_values(by=["date_capture"])
ds = ds.ffill()
ds[["segment_transportationServiceOffer",
        "segment_scheduleInformation_departureDate",
        "segment_transportationServiceOffer"]] = ds[[
            "segment_transportationServiceOffer",
            "segment_scheduleInformation_departureDate",
            "segment_transportationServiceOffer"]].bfill()
            
            
ds = ds.fillna(0)

ds = ds[[   "segment_transportationServiceOffer",
         "product_fareCode",
             "segment",
        "segment_scheduleInformation_departureDate",
            "date_capture",             
             "Nombre_de_reservations_actives_payees",
             "CA_reservations_actives_payees",
             "Cumul_Nombre_de_reservations_actives_payees",
             "Cumul_CA_reservations_actives_payees"]]

ds=ds.groupby(["segment_transportationServiceOffer",
         "product_fareCode",
             "segment",
        "segment_scheduleInformation_departureDate",
        "date_capture"]).sum(["Nombre_de_reservations_actives_payees",
          "CA_reservations_actives_payees",
           "Cumul_Nombre_de_reservations_actives_payees",
            "Cumul_CA_reservations_actives_payees"])
                              
ds.to_html(r"C:\Users\9820937G\OneDrive - SNCF\Bureau\ds 2021-08-31 TGV.html",
           columns=[  "Nombre_de_reservations_actives_payees",
             "CA_reservations_actives_payees",
             "Cumul_Nombre_de_reservations_actives_payees",
             "Cumul_CA_reservations_actives_payees"])