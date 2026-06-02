# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd
import os


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    ruta_principal = "files/input"
    salida = {}

    with os.scandir(ruta_principal) as carpetas_padres:
        for carpeta_padre in carpetas_padres:
            if carpeta_padre.is_dir():
                lineas=[]
                contador = 0
                with os.scandir(carpeta_padre.path) as carpetas_hijos:
                    for carpeta_hijo in carpetas_hijos:
                        if carpeta_hijo.is_dir():
                            with os.scandir(carpeta_hijo.path) as archivos:
                                for archivo in archivos:
                                    if archivo.is_file():
                                        with open(archivo.path, "r", encoding="utf-8") as f:
                                            for line in f:
                                                linea ={"id": contador, "phrase": line.strip(), "target": carpeta_hijo.name}
                                                lineas.append(linea)
                                                contador = contador + 1


                salida[carpeta_padre.name]=lineas
    
    for carpeta in salida:
        if not os.path.exists("files/output"):
            os.makedirs("files/output")
        df = pd.DataFrame(salida[carpeta])
        df.to_csv(f"files/output/{carpeta}_dataset.csv", index=False)

pregunta_01()
    
