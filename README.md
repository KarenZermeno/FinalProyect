# POKEAPI

## To have a interface form making HTTP requests we need to import REQUEST LIBRARY. It allow interact with web services, consume APIs and acces online resources easily an efficiently.
## Import matplotlib which is used to create 2D visualizations and plots.  Assign it a shorter and more convenient alias.
## PIL allows open, manipulate and save different image formats.
##  URLIB.REQUEST is used to import the urlopen function The urllib library is a Python library that provides a set of modules for working with URLs and performing various URL-related operations
## The JSON library is useful to work with web services that return data in JSON format, saving or reading  structures data in files, so then this library will help us to show owr pokemon query.
## need to importate OS library to can interact with the operating system on wich the program is running.

## creat an infinite loop that will continue to run until a break statmen is set by usuary, doing that with a WHILE LOOP TRUE.
# the pokemon's name given by the pokeapi are in lowercase, so then we have to make any input of the usuary to lowercase to can have a correct answer by the program. Also, give to da usuary the possibility to finish the loop by the exit word.
## then we need to build a URL to get the pokemon information using the pokeapi
## Have to check if the request was not succeful, need to be 200 code, if the information couldn't obtain a pokemon, then, a not found pokemon mesage is shown and continue with the next iteration of the loop.
## The response is loaded in JSON format into the data variable. This converts the received data into a Python dictionary that can be easily manipulated.\

## now need to check if there is a possible error or if something goes wrong.
### The URL of the image of the front of the Pokémon is obtained from the loaded data.
### the image is opened using Image.open and displayed with plt.imshow(image) and plt.show().
### display's on the screen the pokemons statics such as a name, weight, height, abilities, moves and types.
### now creat a pokedex folder if it don't exist alredy using osmakedirs(pokedex_folder).
### Save the data dictionary in a JSON file inside the "pokedex" folder with the name of the Pokémon as the filename.
### If any exception happened in the try block, the except Exception as e: block is caught and executed. In case of an error, the specific error message is printed using print("Error:", e).
### Once the program has finished displaying the information and saving the JSON file, it returns to the beginning of the loop and re-requests the user for the JSON file.#   4 p r o y e c t  
 #   4 p r o y e c t  
 #   F i n a l P r o y e c t  
 