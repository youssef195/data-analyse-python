import pandas as pd
import pandasql as ps

df=pd.read_csv(r"C:\Users\9820937G\OneDrive - SNCF\Bureau\projets\date de capture\export - 2021-10-07T163521.355.csv",sep=";")


q1="""SELECT * FROM df where segment_transportationServiceOffer="INT" """

requete=pd.DataFrame(ps.sqldf(q1, locals()))

requete.to_excel(r"C:\Users\9820937G\OneDrive - SNCF\Bureau\projets\date de capture\requete.xlsx", index = False)