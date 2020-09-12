# FlyCombi
Trabajo Final de Algoritmos y Programación II - FIUBA
https://algoritmos-rw.github.io/algo2/tps/2018_2/tp3/

## Ejecución

```
$ python3 flycombi.py <aeropuertos>.csv <vuelos>.csv
```
Donde ```<aeropuertos>.csv``` es un archivo csv que contiene los nombres de los aeropuertos, sus códigos y sus coordenadas.
Ejemplo: **aeropuertos_inventados.csv**
Nombre | Código | Latitud | Longitud
-------|--------|---------|---------
La Terminal	| JFK	| 0	| 0
Lanus	| LAN	| 0	| 0
Shelbyville	| SHE	| 0	| 0
Atlantis | ATL | 0 | 0
Riverdale	| RIV	| 0	| 0
Wacanda	| WAC	| 0	| 0
Narnia | NAR | 0 | 0
Gotica | BAT | 0 | 0
Pueblo Paleta | ASH	| 0	| 0
San Fransokyo	| BH6	| 0	| 0

Donde ```<vuelos>.csv``` es un archivo csv que contiene información de los vuelos: origen, destino, tiempo de viaje, precio y cantidad de vuelos.
Ejemplo: **vuelos_inventados.csv**
Origen | Destino | Tiempo | Precio | Vuelos
-------|---------|--------|--------|-------
JFK|BH6|344|684|3402
JFK|ATL|250|344|2178
JFK|LAN|459|824|3690
SHE|ATL|208|952|2601
RIV|WAC|329|987|2636
WAC|NAR|463|900|3071
SHE|RIV|353|482|3950
ATL|RIV|492|846|1991
WAC|BAT|348|798|2820
SHE|NAR|246|975|1591
LAN|ASH|456|895|3655
BH6|NAR|196|546|1003
BH6|ASH|322|348|2018
NAR|ATL|164|526|2773
ASH|LAN|391|793|1913
LAN|BAT|181|703|1157

## Comandos

### listar_operaciones
Lista todos los comandos.

### camino_mas
Recibe un origen, un destino y un modo ('barato', 'rapido') y devuelve el camino más barato o rápido, según se solicite.
```
camino_mas barato,Pueblo Paleta,Narnia
```

### camino_escalas
Recibe un origen y un destino y devuelve el camino con menos escalas.
```
camino_escalas Gotica,Wakanda
```

### nueva_aerolinea
Recibe una ruta a un archivo csv en donde devuelve los vuelos de una nueva aerolínea, que pasa por todos los aeropuertos de la forma más económica.
```
nueva_aerolinea nueva_aerolinea.csv
```

### centralidad_aprox
Devuelve los n aeropuertos más importantes, por su cantidad de vuelos y  destinos, de manera aproximada.
```
centralidad_aprox 5
```

### centralidad
Ídem, pero la medida es más exacta.
```
centralidad 5
```

### vacaciones 
Recibe un origen y devuelve una ruta de n destinos para visitar.
```
vacaciones Narnia 5
```
