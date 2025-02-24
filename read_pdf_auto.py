import tabula
from tabula.io import read_pdf

table_list = tabula.read_pdf("ResultadoVale.pdf", pages="all")
print(len(table_list))