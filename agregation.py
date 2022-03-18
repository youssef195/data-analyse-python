df = pd.read_csv(
        r"C:\Users\9820937G\OneDrive - SNCF\Bureau\testexport2.csv",
        sep=";")
    
df.pop("Cumul_Nombre_de_reservations_actives_payees")
df.pop("Cumul_CA_reservations_actives_payees")
df.pop("date_capture_socle")
    
df.replace()
    
df["segment_scheduleInformation_departureDate"] = df[
        "segment_scheduleInformation_departureDate"].str[:10]
    
    
    
df["segment_scheduleInformation_departureDate"] = pd.to_datetime(
        df["segment_scheduleInformation_departureDate"])
    
df["date_capture"] = pd.to_datetime(
        df["date_capture"])
    
    
df["Nombre_de_reservations_actives_payees"].astype(int)
    
    df["CA_reservations_actives_payees"
       ]=df["CA_reservations_actives_payees"
       ].str.replace(',','.'
                     ).astype(float)
    
    pd.to_numeric(df["CA_reservations_actives_payees"], errors='coerce').isnull()
    df.dtypes
    
    df["CA_reservations_actives_payees"
       ]=df["CA_reservations_actives_payees"
            ].astype(float)
            
    df = df[["date_capture",
             "product_fareCode",
             "segment",
             "segment_transportationServiceOffer",
        "segment_scheduleInformation_departureDate",
             
             "Nombre_de_reservations_actives_payees",
             "CA_reservations_actives_payees"]]
    
    
    dt = pd.date_range('08/01/2021', '08/31/2021',
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
                       1: "product_fareCode",
                       2: "segment",
                       3: "segment_transportationServiceOffer",
                       4: "segment_scheduleInformation_departureDate"},
              inplace=True)
    
    
    ds = da.merge(df, on=["segment_scheduleInformation_departureDate",
                          "product_fareCode",
                          "segment",
                          "segment_transportationServiceOffer",
                          ], how="left")
    
    
    
    ds.sort_values(by=["date_capture_x"])
    ds = ds.ffill()
    ds[["segment_transportationServiceOffer",
        "segment_scheduleInformation_departureDate",
        "segment_transportationServiceOffer"]] = ds[[
            "segment_transportationServiceOffer",
            "segment_scheduleInformation_departureDate",
            "segment_transportationServiceOffer"]].bfill()
    ds = ds.fillna(0)
    
    ds.pop("date_capture_y")
    
    df.dtypes
    da.dtypes
    ds.dtypes
        
    
    nbresa = ds.pivot_table(
        
        values= ["Nombre_de_reservations_actives_payees"],
        
        index=["segment_transportationServiceOffer",
               "segment",
               "product_fareCode",
               "segment_scheduleInformation_departureDate"],
        
             
        columns=["date_capture_x"],
                
             )
    
    ca=ds.pivot_table(
        
        values= ["CA_reservations_actives_payees"],
        
        index=["segment_transportationServiceOffer",
               "segment",
               "product_fareCode",
               "segment_scheduleInformation_departureDate"],
        
             
        columns=["date_capture_x"],
                
             )
    
    ds = pd.concat((nbresa,ca),axis=1)
    
    ds.grouby(by=["segment_transportationServiceOffer",
               "segment",
               "product_fareCode",
               "segment_scheduleInformation_departureDate"])
    
    
    ds.to_csv(r"C:\Users\9820937G\OneDrive - SNCF\Bureau\ds.csv", index=True)