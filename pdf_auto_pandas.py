import tabula
from tabula.io import read_pdf

tables_page10 = tabula.read_pdf("ResultadoVale.pdf", pages="10")
# print(len(tables_page10 ))
# print(tables_page10 [0])

first_table = tables_page10[0]
first_table.columns = first_table.iloc[0]
first_table[[0, 1]] = first_table["Variação percentual"].str.split(" ", expand=True)
first_table = first_table[1:9]
first_table = first_table.set_index("R$ milhões")
first_table.columns = first_table.iloc[0]
first_table = first_table[1:]
first_table = first_table.drop("1T21/4T20 1T21/1T20", axis=1)
print(first_table)
