# Activity 2
Json = {
    "Store": {
        "Name": "Video Game Store",
        "Location": "Online",
        "Currency": "COP",
        "Products": [
            {
                "Game": "Super Mario Bros",
                "Label": "Nintendo",
                "Release Date": 1985,
                "Console": "Nintendo Entertainment System",
                "Price": 79900,
                "Stock": 50,
                "Description": "The classic game that started Mario's adventure in the video game world.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario Bros 2",
                "Label": "Nintendo",
                "Release Date": 1988,
                "Console": "Nintendo Entertainment System",
                "Price": 99900,
                "Stock": 30,
                "Description": "A different adventure, with new enemies and innovative gameplay.",
                "Rating": {
                    "★★★★": 8
                }
            },
            {
                "Game": "Super Mario Bros 3",
                "Label": "Nintendo",
                "Release Date": 1988,
                "Console": "Nintendo Entertainment System",
                "Price": 119900,
                "Stock": 20,
                "Description": "One of the best games in the series, with new power-ups and more complex levels.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario World",
                "Label": "Nintendo",
                "Release Date": 1990,
                "Console": "Super Nintendo Entertainment System",
                "Price": 139900,
                "Stock": 40,
                "Description": "An adventure in Dinosaur Land, introducing Yoshi and new worlds.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario 64",
                "Label": "Nintendo",
                "Release Date": 1996,
                "Console": "Nintendo 64",
                "Price": 179900,
                "Stock": 15,
                "Description": "Mario's leap into 3D, exploring castles and collecting stars.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario Sunshine",
                "Label": "Nintendo",
                "Release Date": 2002,
                "Console": "Nintendo GameCube",
                "Price": 149900,
                "Stock": 25,
                "Description": "An adventure on Isle Delfino where Mario uses a water device to clean pollution.",
                "Rating": {
                    "★★★★": 8
                }
            },
            {
                "Game": "Super Mario Galaxy",
                "Label": "Nintendo",
                "Release Date": 2007,
                "Console": "Nintendo Wii",
                "Price": 219900,
                "Stock": 10,
                "Description": "Mario in space, with gravity and unique planetary worlds.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario Galaxy 2",
                "Label": "Nintendo",
                "Release Date": 2010,
                "Console": "Nintendo Wii",
                "Price": 219900,
                "Stock": 8,
                "Description": "The sequel to Super Mario Galaxy, with more worlds and new power-ups.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario 3D World",
                "Label": "Nintendo",
                "Release Date": 2013,
                "Console": "Nintendo Wii U",
                "Price": 179900,
                "Stock": 35,
                "Description": "A 3D Mario game with co-op multiplayer and platforming in different dimensions.",
                "Rating": {
                    "★★★★": 8
                }
            },
            {
                "Game": "Super Mario Odyssey",
                "Label": "Nintendo",
                "Release Date": 2017,
                "Console": "Nintendo Switch",
                "Price": 219900,
                "Stock": 50,
                "Description": "A big adventure in an open world, with Cappy and new powers for Mario.",
                "Rating": {
                    "★★★★★": 10
                }
            },
            {
                "Game": "Super Mario Bros. Wonder",
                "Label": "Nintendo",
                "Release Date": 2023,
                "Console": "Nintendo Switch",
                "Price": 219900,
                "Stock": 100,
                "Description": "A new Mario game with special powers and surprising levels.",
                "Rating": {
                    "★★★★": 9
                }
            }
        ]
    }
}

menu = """
Welcome to the virtual video game store. Filter your search using the options 1 to 3:
[1] Price
[2] Compatibility
[3] Release Date
"""
print(menu)
option = input("Enter an option between 1 and 3: ")

if option == '1':
    balance = int(input("Enter your balance in COP: "))
    for i in Json["Store"]["Products"]:
        if balance <= i["Price"]:
            print("You don't have enough balance to buy", i["Game"], "( Price: $", i["Price"], ")","\n")
        else:
            print("You can buy", i["Game"], "with your balance.", "\nPrice: $", i["Price"],"\n")

elif option == '2':
    option2 = input("Enter the name of your console: ")
    for i in Json["Store"]["Products"]:
        if option2.lower() == i["Console"].lower():
            print(i["Game"], "\nDescription:", i["Description"], "\nRelease Date:", i["Release Date"],
                  "\nPrice: $", i["Price"], "\nConsole:", i["Console"], "\nStock:", i["Stock"],"\n")

elif option == '3':
    year = int(input("Enter the cutoff year to display titles released up to that year: "))
    for i in Json["Store"]["Products"]:
        if year >= i["Release Date"]:
            print(i["Game"], "\nDescription:", i["Description"], "\nRelease Date:", i["Release Date"],
                  "\nPrice: $", i["Price"], "\nConsole:", i["Console"], "\nStock:", i["Stock"],"\n")

else:
    print("Invalid option, try again.")
