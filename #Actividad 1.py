#Actividad 1
json_data = [
    {
        "fase": "cuartos de final",
        "resultados": [
            {
                "local": "Chelsea",
                "visitante": "Real Madrid",
                "resultado": "3-2",
                "tarjetas": {
                    "rojas": 0,
                    "amarillas": 3
                }
            },
            {
                "local": "Villarreal",
                "visitante": "Bayern Múnich",
                "resultado": "1-2",
                "tarjetas": {
                    "rojas": 0,
                    "amarillas": 4
                }
            },
            {
                "local": "Manchester City",
                "visitante": "Atlético de Madrid",
                "resultado": "1-0",
                "tarjetas": {
                    "rojas": 0,
                    "amarillas": 7
                }
            },
            {
                "local": "Benfica",
                "visitante": "Liverpool",
                "resultado": "3-4",
                "tarjetas": {
                    "rojas": 0,
                    "amarillas": 6
                }
            }
        ]
    }
]


for i in json_data[0]["resultados"]:
    if i["resultado"][0] > i["resultado"][2]:
        ganador = i["local"]
    else:
        ganador = i["visitante"]
    print(f"Partido", i["local"], "vs.", i["visitante"],":")
    print(f"Tarjetas rojas: ", i["tarjetas"]["rojas"])
    print(f"Ganador: {ganador}")