"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Vic, Hong"
__email__ = "vic61316@gmail.com"
__date__ = "13/03/2023"

from constants import *

# Write your functions here

recipes = []
recipes_list = []
shopping_list = []
list_for_ls_a = [
    "chocolate",
    "chocolate brownies",
    "seitan",
    "cinnamon rolls",
    "peanut butter",
    "omelette",
]


# 5.1.1
def num_hours() -> float:
    return 100.0


# 5.1.2
"""get the recipe's name of the recipe"""


def get_recipe_name(recipe: tuple[str, str]) -> str:
    return recipe[0]


# 5.1.3
"""divide ingredient amount and the ingredient"""


def parse_ingredient(raw_imgredient_detail: str) -> tuple[float, str, str]:
    raw_imgredient_splited = raw_imgredient_detail.split()
    raw_imgredient_splited_final = " ".join(raw_imgredient_splited[2:])
    """if the ingredient name have composite words, this code would make it from items into a single item in the list."""
    return (
        float(raw_imgredient_splited[0]),
        raw_imgredient_splited[1],
        raw_imgredient_splited_final,
    )


# 5.1.4
"""create the recipes that you want to cook"""


def create_recipe() -> tuple[str, str]:
    list_for_create_recipe = []
    recipes_name = input("Please enter the recipe name: ")
    list_for_create_recipe.append(recipes_name)
    list_for_ingredient = []
    ingredient = input("Please enter an ingredient: ")
    while ingredient != "":
        list_for_ingredient.append(ingredient)
        ingredient = input("Please enter an ingredient: ")
    final_list_for_ingredient = ",".join(list_for_ingredient)
    """this code will put all of the amount, measure, and ingredient name into a single item in a list"""
    list_for_create_recipe.append(final_list_for_ingredient)
    return tuple(list_for_create_recipe)


# 5.1.5
"""extract the amount of a few ingredients"""


def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    recipe_list = list(recipe)
    splited_recipe_list = recipe_list[1].split(",")
    final_list = []
    for number in range(0, len(splited_recipe_list)):
        s_splited_recipe_list = splited_recipe_list[number].split(maxsplit=2)
        """maxsplit = 2 would secure that all the ingredient name become a single item in a list"""
        value = (
            float(s_splited_recipe_list[0]),
            s_splited_recipe_list[1],
            s_splited_recipe_list[2],
        )
        final_list.append(value)
    return tuple(final_list)


# 5.1.6
"""put a recipe into the recipeslist"""


def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    recipes.append((new_recipe))
    return recipes


# 5.1.7
"""use a keyword to find whether it is in the recipeslist, if so, also show the details of it"""


def find_recipe(
    recipe_name: str, recipes: list[tuple[str, str]]
) -> tuple[str, str] | None:
    for number in range(0, len(recipes)):
        if recipe_name in recipes[number][0]:
            return recipes[number]


# 5.1.8
"""remove a recipe which was in the recipeslist by name"""


def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    for number in range(0, len(recipes)):
        if name in recipes[number][0]:
            del recipes[number]
        return recipes


# 5.1.9
"""get the total amount of a ingredient in recipes"""


def get_ingredient_amount(
    ingredient: str, recipe: tuple[str, str]
) -> tuple[float, str] | None:
    count = 0
    str_of_recipe = str(recipe)
    str_of_recipe2 = str_of_recipe.strip("'()")
    """divide ingredient's name and details"""
    splited_str_of_recipe = str_of_recipe2.split(", '")
    final_splited_str_of_recipe = splited_str_of_recipe[1].split(",")
    """divide everry ingredient details into a simgle item in the list"""
    for number in range(0, len(final_splited_str_of_recipe)):
        if ingredient in final_splited_str_of_recipe[number]:
            splited_recipe = final_splited_str_of_recipe[number].split()
            x = (float(splited_recipe[0]), (splited_recipe[1]))
            return x
        else:
            count += 1
        if count == len(final_splited_str_of_recipe):
            return None


# 5.1.10
"""add ingredient and its details into shoppinglist and show it"""


def add_to_shopping_list(ingredient_details, shopping_list):
    count = 0
    if len(shopping_list) == 0:
        shopping_list.append(ingredient_details)
    else:
        for number in range(0, len(shopping_list)):
            if ingredient_details[1:] == shopping_list[number][1:]:
                shopping_list[number] = (
                    shopping_list[number][0] + ingredient_details[0],
                    shopping_list[number][1],
                    shopping_list[number][2],
                )
                break
            else:
                count += 1
        if count == len(shopping_list):
            shopping_list.append(ingredient_details)
            """this code is for those ingredient that haven't exist in soppinglist and the len(shopping_list) is >0"""
        else:
            pass


# 5.1.11
"""remove ingredient and its details from shoppinglist"""


def remove_from_shopping_list(
    ingredient_name: str, amount: float, shopping_list: list
) -> None:
    for number in range(0, len(shopping_list)):
        if ingredient_name == shopping_list[number][2]:
            if shopping_list[number][0] - amount <= 0:
                del shopping_list[number]
                break
            else:
                shopping_list[number] = (
                    shopping_list[number][0] - amount,
                    shopping_list[number][1],
                    shopping_list[number][2],
                )
        else:
            pass
        """if ingredient is not in shoppinglist, pass the code"""


# 5.1.12
"""generate the whole shopplinglist base on what you want to cook in cook book"""
shopping_list = []


def generate_shopping_list(
    recipes: list[tuple[str, str]]
) -> list[tuple[float, str, str]]:
    for number in range(0, len(recipes)):
        splited_recipes = recipes[number][1].split(",")
        """this code divide the recipe's name and its ingredient"""
        for number_2 in range(0, len(splited_recipes)):
            ingredient_list = []
            ingredient_in_shopping_list = splited_recipes[number_2].split()
            """this code split all the ingredient list into the single list, and its form = amout, measure, and ingredient name"""
            ingredient_list.append(float(ingredient_in_shopping_list[0]))
            ingredient_list.append(ingredient_in_shopping_list[1])
            join_ingredient_in_shopping_list = " ".join(ingredient_in_shopping_list[2:])
            """make sure to deal the ingredient name that its name is over two words"""
            ingredient_list.append(join_ingredient_in_shopping_list)
            shopping_list.append(tuple(ingredient_list))
    return shopping_list


# 5.1.13
"""print shoppinglist out as a more readable form"""


def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    shopping_list.sort(key=lambda x: x[2])
    list_for_determining_max = []
    for amount in shopping_list:
        str_of_amount = str(amount[0])
        list_for_determining_max.append(len(str_of_amount))
    max_amount_of_ingredient_amount = max(list_for_determining_max)
    list_for_determining_max = []
    for measure in shopping_list:
        list_for_determining_max.append(len(measure[1]))
    max_amount_of_ingredient_measure = max(list_for_determining_max)
    list_for_determining_max = []
    for ingredient_name in shopping_list:
        list_for_determining_max.append(len(ingredient_name[2]))
    max_amount_of_ingredient_name = max(list_for_determining_max)

    for ingredient in shopping_list:
        print(
            "| {:>{}} | {:^{}} | {:<{}} |".format(
                ingredient[0],
                max_amount_of_ingredient_amount,
                ingredient[1],
                max_amount_of_ingredient_measure + 1,
                ingredient[2],
                max_amount_of_ingredient_name + 1,
            )
        )


# 5.1.14
"""modify the input and output it as a standerd form"""


def sanitise_command(command: str) -> str:
    command_1 = command.strip(" 1234567890_")
    command_2 = command_1.lower()
    return command_2


# 5.1.15
"""whole function run"""


def main():
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE,
        BROWNIE,
        SEITAN,
        CINNAMON_ROLLS,
        PEANUT_BUTTER,
        MUNG_BEAN_OMELETTE,
    ]
    # Write the rest of your code here

    command = input("Please enter a command: ")

    while command not in "Qq":
        if command == "H" or command == "h":
            print("H or h: Help")
            print("mkrec: creates a recipe, add to cook book.")
            print("add {recipe}: adds a recipe to the collection.")
            print("rm {recipe}: removes a recipe from the collection.")
            print(
                "rm -i {ingredient_name} {amount}: removes ingredient from shopping list."
            )
            print("ls -i: list all recipes in shopping cart.")
            print("ls -a: list all available recipes in cook book.")
            print("ls -s: display shopping list.")
            print("g or G: generates a shopping list.")
            print("Q or q: Quit.")
            command = input("Please enter a command: ")
        elif command[:4] == "add ":
            sanitise_command(command)
            splited_command = command.split()
            command_for_interaction = "_".join(splited_command[1:])
            add_recipe(command_for_interaction.upper(), recipes)
            command = input("Please enter a command: ")
        elif command[:3] == "rm ":
            splited_command = command.split()
            command_for_interaction_2 = " ".join(splited_command[1:])
            remove_recipe(command_for_interaction_2, recipes)
            command = input("Please enter a command: ")
        elif command == "g" or command == "G":
            final_recipe_for_g = []
            for str_of_recipe in recipes:
                i = globals()[str_of_recipe]
                final_recipe_for_g.append(recipe_ingredients(i))
            for number in range(0, len(final_recipe_for_g)):
                display_ingredients(final_recipe_for_g[number])
            command = input("Please enter a command: ")
        elif command == "ls":
            list_for_ls = []
            if len(recipes) == 0:
                print("No recipe in meal plan yet")
            else:
                for str_of_recipe in recipes:
                    i = globals()[str_of_recipe]
                    list_for_ls.append(i)
            print(list_for_ls)
            command = input("Please enter a command: ")
        elif command == "mkrec":
            create_recipe()
            command = input("Please enter a command: ")
        elif command[:4] == "ls -a":
            for number in range(0, len(list_for_ls_a)):
                print(list_for_ls_a[number])
        # elif command == "rm {ingredient_name} {amount}":

        # elif command[:4] == "ls -s":

        else:
            command = input("Please enter a command: ")


if __name__ == "__main__":
    main()
