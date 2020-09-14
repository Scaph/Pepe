import requests
import os
import sys
try:
    from bs4 import BeautifulSoup as bs
    try:
        import webbrowser
    except ImportError:
        os.system('pip install webbrowser')

        print('Installing webbrowser...')

        print('Ejecuta de nuevo tu script...')

        exit()
except ImportError:
    os.system('pip install webbrowser')

    print('Installing bs4...')

    print('Ejecuta de nuevo tu script...')

    exit()
# José Eduardo Rivera Gámez
'''
Para empezar en los import ya los tenía en mi laptop, por lo que no ocupe el
except.
Se buscará en la página de la UANL, pregunta sobre la página incial y la página
final; si esto tiene error como que se puso al revés, se intercambia y se
soluciona. Después con un for con "i" se basa de la página incial al final,
se utiliza el import request aquí para obtener el código de la página, para
saber si nos dio resultado se pone el estado de 200, si no, es un error.
Si se halló la página correctamente, con el BeautifulSoup(bs) se hace como
más bonito el código en html para que sea fácil de utlizar en python. Con esto
se busca la etiqueta "h3 a" ese nos manda el link de la notica en su respectiva
página, pero en cada link(con un for) tenemos que comprobar que no haya estado
diferente de 200, ya que hayamos puesto el código bonito encontraremos
unos párrafos con la letra "p" y si esa letra coincide con la dependencia que
sugerimos al incio, se no estará abriendo el link gracias al import webbrowser.
'''
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo", url2)
                        webbrowser.open(url2)
                        break

