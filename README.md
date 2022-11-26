# Minería
Scripts de construcción del dataset del proyecto de Minería de Datos, en CUCEI.

Estos scripts hacen webscraping de inmuebles24, un sitio web para anunciar compra y renta de casas e inmuebles.

# Archivos

El repo contiene los siguientes archivos:
- `scraper.sh`: Ejecuta el script de Selenium n veces, utilizamos un script de bash porque hacer repetidas conexiones en el mismo script de Python
activa la protección contra bots de Cloudflard y bloquea el webscraper. También concatena los CSVs resultantes en uno solo.
- `webscraper.py`: Se conecta a inmuebles24 y guarda en un CSV los siguientes datos de cada publicación:
  - Dirección.
  - Tamaño del terreno.
  - Tamaño de la construcción.
  - Cantidad de recámaras.
  - Cantidad de baños.
  - Cantidad de estacionamientos.
  - Precio.
- `cleaner.py`: Limpia el dataset, separa la información, dejando sólo los números, además, si no hay cantidad de baños, la reemplaza con la moda tomando
en cuenra la cantidad de recámaras.
- `calzada.py`: Dado el dataset completo y un subconjunto cuyos elementos estén al oeste de la calzada independencia, marca una columna booleana en
donde se coloca 1 para las instancias al oeste de la calzada y un 0 para las instancias al este de la calzada, la columna se colocó manualmente y se
llenó con 0, el script cambia por 1 las instancias correspondientes.
