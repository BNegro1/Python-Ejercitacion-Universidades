# Construya un programa que encuentre la palabra más larga en un texto, considere que 
# todas las palabras estarán separadas por espacio. Una vez resuelto el ejercicio

# Ejercicio realizado sin LISTAS.

# Solicitamos datos:

texto = input("Ingrese un texto: ")

# Dividimos el texto en palabras
pal = texto.split()  

# Inicia el PRIMER indice de la palabra del texto
pal_larga = pal[0]  

# Iteramos desde 1 hasta el "infinito"
for x in pal[1:]:  
    # Se comprueba que "x" (palabra actual) sea mayor (en longitud) a "pal_larga"
    if len(x) > len(pal_larga):
        # Actualizamos la palabra
        pal_larga = x  

# Imprimimos resultado.
print("Texto completo: ", texto)
print("La palabra más larga es:", pal_larga)

