# Descripción

Este programa implementa los siguientes métodos de búsqueda:
- No informados: Búsqueda en ancho (BPA), búsqueda en profundidad (BPP) y búsqueda en profundidad variable (BPPV)
- Informados: Heurística global, heurística local, método A*

Ofrece además dos interfaces Solver y GameState que permiten implementar rápidamente un problema que pueda ser solucionado
usándo los métodos de búsqueda, así como una interfaz Runner que facilita la implementación de scripts que provean parámetros
de configuración y muestren el resultado de la búsqueda.

Están ya implementados dos juegos a modo de problema: [EigthGame](https://www.cut-the-knot.org/SimpleGames/EightDigitPuzzle.shtml) y [CanibalGame](https://es.wikipedia.org/wiki/Acertijo_de_los_misioneros_y_los_can%C3%ADbales). Además, para el juego EightGame se implementó un frontend que facilita su visualización.

# Utlización

## Dependencias

Para la utilización de la función de generación de grafos, que muestra el camino de las soluciones, es necesario tener instalado
el programa [GraphViz](https://graphviz.org/download/).

Además, es necesario instalar las dependencias utilizadas por Python, utilizando el comando:
```bash
pip install -r requirements.txt
```

## Compilación

No se requiere compilación, el código está escrito enteramente en Python y todas las librerías instaladas ya están compiladas.

## Configuración
Se puede parametrizar la búsqueda y valores de los juegos desde el archivo `conf.json`, el mismo debe crearse siguiendo el template en `conf.json.template`.
Se muestran a continuación dos configuraciones posibles a modo de ejemplo.

```json
{
    "searchMethod": "bpa",
    "searchTimeout": 60000,
    "plotDecisionTree": false,
    "eight_game": {
        "initialGrid": [1, 2, 3, 5, 6, 0, 4, 7, 8],
        "goalGrid": [1, 2, 3, 4, 5, 6, 7, 8, 0],
    }
}
```

```json
{
    "searchMethod": "heu_weighted",
    "searchTimeout": 10000,
    "heuWeight": 0.5,
    "plotDecisionTree": true,
    "eight_game": {
        "initialGrid": [1, 2, 3, 5, 6, 0, 4, 7, 8],
        "goalGrid": [1, 2, 3, 4, 5, 6, 7, 8, 0],
        "heuristic": "correctness"
    }
}
```

## Ejecución
Ejecutar EightGame en la consola
```
python eight_game_runner.py
```
Ejecutar CanibalGame en la consola
```
python eight_game_runner.py
```
Ejecutar EightGame con el frontend
```
python eight_game_front.py
```