<h1>Map Builder</h1>

Módulo encargado de crear una representación digital del entorno de trabajo.

Para este estudio la representación e intercambio de datos de los elementos geográficos se la hizo en formato GeoJson, este posee la particularidad de tener un objeto “features” donde se puede incluir las diferentes entidades, estas divididas a su vez en “geometry”y “properties”.

- “Geometry”: Posee el tipo de geometría y sus coordenadas (lat,log).
- “Properties”: Contiene la información de los atributos.  


## Prerequisites


1. Ubuntu 
2. python3
3. shapely
4. pycountry
5. json

<h1>Next steps</h1>

- [ ] Cree un proyecto GeoJson de la Granja cuyos elementos serán definidos según el tipo de entidad y una serie de propiedades intrínsecas.
- [ ] Para este estudio se han definido las siguientes entidades: 
 - AgriFarm
 - AgriParcel
 - Building 
 - RoadSegment
 - RestrictedTrafficArea
   
- [ ] Exportar el archivo con los datos modelados en formato GeoJSON. 
- [ ] Generar un registro donde se encuentre los scripts de cada entidad con sus propiedades para luego rellenarlas.
- [ ] Extraer cada una de las entidades por separado y generar un archivo .json con un identificador único para cada uno.


