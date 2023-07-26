import requests # import libray requests
import matplotlib.pyplot as plt # import libray matplotlib to generate visualizations and grafics
from PIL import Image # import Pil to open, save and handle an image
from urllib.request import urlopen # allow to open a URL and get the data associated with that URL
import json #import JSON Library to convert Python objects to a valid JSON representation
import os # import OS to interact with the operating system on which the program is running


while True: 
    pokemon = input("Enter a pokemon or write exit to finish: ").lower() # prompt the user to enter a pokemon's name,
    #and with the lower method we convert the written name to lowercase letters, also give to the usuary the option
    #by writting "exit" to finish the program
  
    if pokemon.lower() == 'exit': #convert exit to lowercase letters
        break #finish the program
    
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon #set a variable with the URL + the pokemon's given by
    #the usuary
    answer = requests.get(url) #makes a GET request to the specified URL

    if answer.status_code != 200: #If the request fails with a status code other than 200 the status code is 
        #printed to indicate that there was an error in the request.
        print("Pokemon not found")
        continue #otherwise, the application continues

    data = answer.json() # set a new variable assigning it the content converted from http in json format
    
    try: #start a try block
        url_image = data['sprites']['front_default'] #stores URL pointing to an image of the Pokémo by 
        # acces to the key sprites in the data dictionary, also the front_default key 
        image = Image.open(urlopen(url_image)) #open image using the open function of the image module and 
        #use urlopen to get the content of the URL containing the image.


        plt.title(data['name']) # The image is displayed in a popup window using the matplotlib
        imgplot = plt.imshow(image) # displays the image stored in the image variable
        plt.show() # displays the popup window with the image.

        print("\n--- Pokemon Statistics ---")
        print("Name:", data['name']) # print the pokemon's name contained in the data dictionary
        print("Weight:", data['weight']) # print the pokemon's weight contained in the data dictionary
        print("Height:", data['height']) # print the pokemon's height contained in the data dictionary
        print("Abilities:", ', '.join([ability['ability']['name'] for ability in data['abilities']]))
        # print the pokemon's abilities contained in the data dictionary
        print("Moves:", ', '.join([move['move']['name'] for move in data['moves']]))
        # print the pokemon's moves contained in the data dictionary
        print("Types:", ', '.join([poke_type['type']['name'] for poke_type in data['types']]))
        # print the pokemon's types contained in the data dictionary

        pokedex_folder = "pokedex" #open a pokedex folder
        if not os.path.exists(pokedex_folder): # this will be used to store JSON files with the information 
            # about the pokemon called 
            os.makedirs(pokedex_folder) #  used to create a folder in the file system
          
        with open(f"{pokedex_folder}/{data['name']}.json", "w") as file: # opens a file in write mode
            #with the direction to store the file '{datos['name']}.json' set the file's name using the 'name' key
            #from the directory data 
            json.dump(data, file) # write the contents of the data dictionary to the open file
        # The reserved word "with" assures that the file will be automatically closed once the code
        # block inside it has been completed.
        
    except Exception as e: # catches any exceptions occurring in the previous code block
        print("Bug:", e) # an error message is printed indicating that an exception has occurred
        continue #used to move to the next iteration of a loop
