from PyPDF2 import PdfReader, PdfWriter
import getpass

pdf_writer = PdfWriter() #Crea una instancia de PdfWriter, que se usará para crear un nuevo archivo PDF.
pdf_reader = PdfReader("document.pdf")

for page_num in range(len(pdf_reader.pages)): #Este bucle for recorre todas las páginas del archivo PDF
    pdf_writer.add_page(pdf_reader.pages[page_num])

password = getpass.getpass(prompt="Ingrese el password: ")
print(password) #Muestra la contraseña ingresada en la consola. Normalmente, esta línea se omitiría para no exponer la contraseña en texto plano.
pdf_writer.encrypt(password)

with open("document_protected.pdf", "wb") as file:
    pdf_writer.write(file) #Escribe el contenido del pdf_writer en el archivo "document-protected.pdf".