def contarPal(frase):
    contador = dict()
    palabras = frase.split()
    for palabra in palabras:
        cantLetras = len(palabra)
        contador[cantLetras] = []
    for palabra in palabras:
        cantLetras = len(palabra)
        contador[cantLetras].append(palabra)
    return contador

frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás
que te gustaría automatizar alguna tarea. Por ejemplo, podrías desearrealizar
una búsqueda y reemplazo en un gran número DE archivos de texto,o renombrar y
reorganizar un montón de archivos con fotos de unamaneracompleja.
Tal vez quieras escribir alguna pequeña base de datospersonalizada, o una
aplicación  especializada con interfaz gráfica,o UN juego simple.'''

print (contarPal(frase))
