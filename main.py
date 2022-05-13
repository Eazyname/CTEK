import numpy as np
import pandas as pd

table = pd.read_csv("абоненты.csv", delimiter=';')
ct_norm = 301.26
ct_chetchik = 1.52

table["Начислено"] = np.where(table["Тип начисления"] == 1, ct_norm, round(ct_chetchik*(table["Текущее"]-table["Предыдущее"]),2))
table.to_csv("Начисления_абоненты.csv", sep=';', index = False, encoding='cp1251')

new_dom = table.groupby(["№ дома"]).agg({"Улица": "last", "Начислено": "sum"}).reset_index()
new_dom = new_dom.round({"Начислено": 2})
new_dom.to_csv("Начисления_дома.csv", sep=';', index = True, encoding='cp1251')

print("Готово")
