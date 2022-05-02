MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 600,
    "coffee": 400,
}

commands = {"off": "Turns off the machine.", 
            "menu": "Gets the menu including prices",
            "refill": "Refills the coffee machine ingredients",
            "cahsout": "Take all the current money inside the machine",
            "totalpurchase": "How much the machine has earnt(excl. taxes)",
            "report": "Reports state of the current resources",
            "help": "Prints out all the commands you can use",
            "transactions": "Prints out the list of transactions"
            }