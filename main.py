import random
import json 


with open('./project_db.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)


all_cats = []
all_cat_items = []

for item in data.keys():
    all_cats.append(item)

for a in all_cats:
    for b in data[a]:
        all_cat_items.append(data[a][b])


def get_input():
    print("=================")
    print("Available Categories:\n{}".format(", ".join(all_cats)))
    chosen_category = input("Enter Chosen Category\n")

    return chosen_category


def random_game():
    random_cat = random.choice(all_cats)
    
    all_items = []

    for item in data[random_cat]:
        all_items.append(data[random_cat][item])

    rand_item = random.choice(all_items)

    game_complete(random_cat, rand_item)


def category_game():
    chosen_cat = get_input()

    all_items = []

    for item in data[chosen_cat]:
        all_items.append(data[chosen_cat][item])

    rand_item = random.choice(all_items)

    game_complete(chosen_cat, rand_item)


def list_all_items():
    print("All Items By Category\n")

    for item in all_cats:
        print("===================")
        print(item)
        print('-------------------')

        for ite in all_cat_items:
            print(ite)

    print("===================")


def game_complete(x,y):
    print("=====================")
    print("Category: {}".format(x))
    print("Project: {}".format(y))
    print("=====================")



actions = ["complete-random", "select-category-random-project", "list-all-projects"]

chosen_action = input("Available Commands Are:\n{}\nPlease Enter Method Of Project Selection\n".format(", ".join(actions)))

if chosen_action.lower() == "complete-random":
    random_game()
elif chosen_action.lower() == "select-category-random-project":
    category_game()
else:
    list_all_items()