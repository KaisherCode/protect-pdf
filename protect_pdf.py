import os
import pandas as pd # Esta libreria nos permite leer el archivo .csv

import PyPDF2

# Función encriptar PDF
def lock_pdf(pdf_dir,Password):
    filename = os.path.basename(pdf_dir)
    pdf = open(pdf_dir,"rb")
    pdf_data = PyPDF2.PdfReader(pdf)
    pages_num = len(pdf_data.pages)
    output = PyPDF2.PdfWriter(pdf)

    for i in range(pages_num):
        inputPdf = PyPDF2.PdfReader(pdf)
        output.add_page(inputPdf._get_page(i))
        output.encrypt(str(Password))
        save_dir = os.path.join(os.getcwd(),"ProtectedPDF",filename)
        with open(save_dir,"wb") as outputStream:
            output.write(outputStream)
    pdf.close()
    
# Lee el archivo password_setting.csv 
csv_settings = pd.read_csv(r"/home/kaisher/developer/projects/protect-pdf/password_setting.csv") 

# Leer fila por fila los datos del archivo password_setting.csv
for row in csv_settings.itertuples():
    print("Protegiendo el PDF {file} con clave: {password}".format(file=row.Ruta,password=row.Clave))
    lock_pdf(row.Ruta,row.Clave)
