import csv

title_index = 1


def main():
    print()
    print("Welcome to the Bob Ross Database! You can look at different sets of Data in this program.")
    print()
    print("You can search by Episode or Painting or Item.")
    search = input("What do you want to search by? ")
    if search.lower() == "episode":
        print("Seasons go 1 to 31 and Episodes go 1 to 13.")
        Season = input("Which Season? ")
        episode = input("Which episode? ")
        title = find_by_episode(Season,episode)
        print(f"In episode {episode} season {Season} Bob Ross's painting was named {title}.")
    elif search.lower() == "painting":
        painting = input("Which painting do you want to search for? ")
        episode = find_by_painting(painting)
        print(f"{painting.capitalize()} appeared in {episode}!")
    elif search.lower() == "item":
        item = input("What item would you like to look up? ")
        epidode = find_by_item(item)
    

def Bob_Ross_Data(key_column_index):
    dictionary = {}
    with open("Bob Ross CSV.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]            
            dictionary[key] = row_list
    return dictionary

def find_by_episode(Season,episode):
    data_table = Bob_Ross_Data(0)
    if int(Season) < 10:
        Season =  "S0" + str(Season)
    else:
        Season =  "S" + str(Season)

    if int(episode) < 10:
        episode =  "E0" + str(episode)
    else:
        episode =  "E" + str(episode)
    data = str(Season) + str(episode)
    if data in data_table:
        painting = data_table[data]
        title = painting[title_index]
    return_items(painting)
    return title

def find_by_painting(painting):
    data_table = Bob_Ross_Data(1)
    format_painting = (f'"{painting.upper()}"')
    if format_painting in data_table:
        data = data_table[format_painting]
        episode = data[0]
        item_list = return_items(data)
        print(item_list)
    else:
        print("That painting is not found in the database.")
    return episode

def find_by_item(item):
    items = make_item_list()
    index = items.index(item.upper())
    with open("Bob Ross CSV.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        painting_list = []
        for row_list in reader:
            if row_list[index+2] == "1":
                painting_list.append(row_list[1].capitalize())
            else:
                pass
    print(painting_list)
    

def make_item_list():
    items =['APPLE FRAME','AURORA BOREALIS','BARN','BEACH','BOAT','BRIDGE','BUILDING','BUSHES','CABIN','CACTUS'
    ,'CIRCLE FRAME','CIRRUS','CLIFF','CLOUDS','CONIFER','CUMULUS','DECIDUOUS','DIANE ANDRE','DOCK','DOUBLE OVAL FRAME'
    ,'FARM','FENCE','FIRE','FLORIDA FRAME','FLOWERS','FOG','FRAMED','GRASS','GUEST','HALF CIRCLE FRAME','HALF OVAL FRAME',
    'HILLS','LAKE','LAKES','LIGHTHOUSE','MILL','MOON','MOUNTAIN','MOUNTAINS','NIGHT','OCEAN','OVAL FRAME','PALM TREES','PATH',
    'PERSON','PORTRAIT','RECTANGLE 3D FRAME','RECTANGULAR FRAME','RIVER','ROCKS','SEASHELL FRAME','SNOW','SNOWY MOUNTAIN',
    'SPLIT FRAME','STEVE ROSS','STRUCTURE','SUN','TOMB FRAME','TREE','TREES','TRIPLE FRAME','WATERFALL','WAVES','WINDMILL',
    'WINDOW FRAME','WINTER','WOOD FRAMED']
    return items

def return_items(data):
    items = make_item_list()
    index = -2
    item_list = []
    for i in data:
        if i == '1':
            hello = items[index]
            item_list.append(hello.capitalize())
            index = index + 1
        else:
            index = index + 1
    return item_list


main()