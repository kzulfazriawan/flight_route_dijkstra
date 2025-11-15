## Overview
A simple python application to solve the "**Travel from A to B with cheapest cost within K stops**" (LeetCode #787). The main
solutions is using priority-queue Dijkstra algorithm with stop limits. The data fixtures is using json data file as the
only valid input for the parameters.

## How it works
1. The application extract the json file that containing valid key, for example:
```json
{
    "n": 4,
    "flights": [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200]
    ],
    "src": 0,
    "dst": 3,
    "k": 1
}
```
2. Processing the algorithm to find the cheapest route between the source and destination, the main algorithm is implemented
in file **src/services.py**. By using the Dijkstra algorithm with stop restriction the priority queue will looking for the
cheapest cost available.
3. Running the **main.py** file with extra arguments to pointing the destination path of the JSON file. The **main.py** is the
executed file on the shell console and print the result, to run it checkout the README.md