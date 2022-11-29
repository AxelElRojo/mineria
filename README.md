# Minería
Scripts utilizados para la construcción del dataset del proyecto de Minería de Datos, en CUCEI.

Estos scripts hacen webscraping de inmuebles24, un sitio web para anunciar compra y renta de casas e inmuebles.

# ¿Qué es Webscraping?
Es una técnica utilizada para extraer datos de páginas web de manera automatizada, en pocas palabras, el webscraping nos permite conseguir grandes cantidades de datos de una página web sin tener que hacer el trabajo manual. En este caso, el webscraping se utiliza para construir el dataset del proyecto, el dataset consiste en anuncios de casas en venta.

Utilizamos Selenium para el webscraping, es un conjunto de herramientas que automatizan navegadores mediante una API y permiten el webscraping mediante la misma.
# Dependencias
Los scripts dependen de las siguientes librerías:
- `selenium`
- `pandas`

Además, se utilizan otras librerías incluídas, que no es necesario instalar.
# Archivos
El repo contiene los siguientes archivos:
- `scraper.sh`: Ejecuta el script de Selenium n veces, utilizamos un script de bash porque hacer repetidas conexiones en el mismo script de Python
activa la protección contra DDoS de Cloudflare y bloquea el webscraper. También concatena los CSVs resultantes en uno solo.
- `webscraper.py`: Se conecta a inmuebles24 y guarda en un CSV los siguientes datos de cada publicación:
  - Dirección.
  - Tamaño del terreno.
  - Tamaño de la construcción.
  - Cantidad de recámaras.
  - Cantidad de baños.
  - Cantidad de estacionamientos.
  - Precio.
- `cleaner.py`: Limpia el dataset, separa la información, dejando sólo los números, además, si no hay cantidad de baños, la reemplaza con la moda tomando
en cuenta la cantidad de recámaras.
- `calzada.py`: Dado el dataset completo y un subconjunto cuyos elementos estén al oeste de la calzada independencia, marca una columna booleana en
donde se coloca 1 para las instancias al oeste de la calzada y un 0 para las instancias al este de la calzada, la columna se colocó manualmente y se
llenó con 0, el script cambia por 1 las instancias correspondientes.

Es importante mencionar que los nombres de los archivos están hardcodeados y se tiene que tener cuidado para no sobreescribir nada.

# Utilización
El proceso que desarrollamos es bastante manual y se puede mejorar:
1. Se modificó `scraper.sh` para que el `for` esté entre las páginas del sitio web que se desean obtener.
2. Se ejecutó `scraper.sh`.
2. Se eliminaron los archivos remanentes.
3. Manualmente, se revisaron las instancias para verificar que los datos se hayan escrito correctamente, como los anuncios descargados son escritos y
publicados por personas, puede que tengan datos erróneos o mal acomodados, esto no lo pudimos arreglar con un script, así que lo hicimos manualmente.
4. Utilizando My Maps de Google, cargamos el CSV al mapa y seguimos el siguiente proceso:
    1. Eliminamos instancias en otras ciudades o países.
    2. Corregimos las direcciones de instancias no encontradas.
    3. Eliminamos las instancias que se encontraban fuera del anillo periférico, esto para lograr cierta estabilidad en los precios.
    4. Marcamos un polígono para encontrar las instancias al oeste de la calzada independencia.
    5. Se extrajo el subconjunto de las instancias al oeste de la calzada independencia.
    - [El mapa](https://www.google.com/maps/d/u/1/edit?mid=1FHQUsdTBDr88wdZcOiM8Awf1FwmzNXQ&ll=20.658776894534554%2C-103.3306438&z=12) es accesible 
desde un navegador.
5. Se creó la columna calzada en el dataset, se llenaron todas las instancias con 0.
6. Se ejecutó `calzada.py`, que cambió a 1 la columna calzada en las instancias correspondientes.
