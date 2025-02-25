import tabula
from tabula.io import read_pdf

table_list = tabula.read_pdf("ResultadoVale.pdf", pages="11")   
table_list = tabula.read_pdf("http://www.vale.com/PT/investors/information-market/quarterly-results/ResultadosTrimestrais/Vale_IFRS_1T21_BRL_v26042021_vf.pdf", pages="all")
print(len(table_list))
for table in table_list:
    print(table)

