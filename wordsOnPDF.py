#El objetivo de este programa es buscar una palabra y contarla

import PyPDF2

pdfFile = open('HistMex.pdf', 'rb') #abre el documento

libro=list()
libroLimpio=list()
busqueda=input("Quiero buscar la palabra: ")
contador=0

reader=PyPDF2.PdfFileReader(pdfFile) #lee el documento
pags=reader.numPages    #identifica numero de paginas
print("\n El documento tiene ", pags, " paginas")

#ciclo para extraer texto de cada pagina y limpiar de , las palaras
for n in range(pags):
    page=reader.getPage(n)
    text=page.extractText()
    palabrasPag=text.split()
    for palabra in palabrasPag:
        limpiar=palabra.strip(",")
        libro.append(limpiar)

#iclo para limpiar de espacios y puntos las palabras
for palabra in libro:
    limpiar=palabra.replace("."," ")
    limpianuevo=limpiar.lstrip()
    libroLimpio.append(limpianuevo)

#print(libroLimpio)

for palabra in libroLimpio:
    if palabra == busqueda:
        contador=contador+1

print("\n Y la palabra ",busqueda," aparece ", contador, "veces")

pdfFile.close()
