#Actividad 1
json_data = [
    {
        "fase": "cuartos de final",
        "resultados": [
            {
                "local": "Chelsea",
                "visitante": "Real Madrid",
                "resultado": "1-3",
                "tarjetas": {
                    "rojas": 0,
                    "amarillas": 3
                }
            },
            {
                "local": "Villarreal",
                "visitante": "Bayern Múnich",
                "resultado": "1-0",
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
                "resultado": "1-3",
                "tarjetas": {
                    "rojas": 0,
                    "amarillas": 6
                }
            }
        ]
    }
]


for i in json_data[0]["resultados"]:
    print(i["tarjetas"]["rojas"])