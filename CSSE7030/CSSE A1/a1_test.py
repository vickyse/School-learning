from constants import *

# 5.1.2
# recipe=("cake","egg","sugar")

# def get_recipe_name(recipe: tuple[str, str]) -> str:
#    return recipe[0]

# x=get_recipe_name(recipe)
# print(x)

# 5.1.3
# raw_imgredient=("0.5 tsp salt")
# raw_imgredient_splited=raw_imgredient.split()
# # def parse_ingredient(raw_imgredient) -> tuple[float, str, str]:
# #    raw_imgredient_splited=raw_imgredient.split()
# #    return float(raw_imgredient_splited[0]), raw_imgredient_splited[1], raw_imgredient_splited[2]

# def parse_ingredient(raw_imgredient_detail: str) -> tuple[float, str, str]:
#     raw_imgredient_splited=raw_imgredient_detail.split()
#     return float(raw_imgredient_splited[0]), raw_imgredient_splited[1], raw_imgredient_splited[2]

# print (raw_imgredient_splited)
# x=parse_ingredient(raw_imgredient)
# print(x)


# 5.1.4
# y=parse_ingredient(raw_imgredient)
# print(y)
# x=parse_ingredient(raw_imgredient)
# print(type(x))
# x=parse_ingredient(raw_imgredient)
# print(x)


# 5.1.4
# def create_recipe() -> tuple[str, str]:
#    list_for_create_recipe=[]
#    recipes_name=input("Please enter the recipe name: ")
#    list_for_create_recipe.append(recipes_name)
#    ingredient=input("Please enter an ingredient:")
#    while ingredient != "":
#        list_for_create_recipe.append(ingredient)
#        ingredient=input("Please enter an ingredient: ")
#    tuple_for_creat_recipe=tuple(list_for_create_recipe)
#    return tuple_for_creat_recipe

# x=create_recipe()
# print(x)


# 5.1.5
# recipe=("peanut butter", "300 g peaunts, 0.5 tsp salt, 2 tsp oil")
# # recipe_list=list(recipe)
# # splited_recipe_list=recipe_list[1].split(", ")
# # str_splited_recipe_list=str(splited_recipe_list)
# #for number_of_ingredients in range(0, len(splited_recipe_list)):
# #   print(splited_recipe_list[number_of_ingredients])

# recipe_str=str(recipe)
# recipe_str_splited=recipe_str.split()
# recipe_str_splited_without_name=recipe_str_splited[2:]
# #print(recipe_str_splited_without_name[0])

# def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
#    recipe_list=list(recipe)
#    splited_recipe_list=recipe_list[1].split(", ")
#    for number_of_ingredients in range (0,len(splited_recipe_list)):
#         s_splited_recipe_list=splited_recipe_list[number_of_ingredients].split()
#         return(float(s_splited_recipe_list[0]), s_splited_recipe_list[1], s_splited_recipe_list[2])

# x=recipe_ingredients(("peanut butter", "300 g peaunts, 0.5 tsp salt, 2 tsp oil"))
# print(x)
# x=recipe_ingredients(recipe)
# print(x)

# recipe_list=list(recipe)
# splited_recipe_list=recipe_list[1].split(", ")
# s_splited_recipe_list=splited_recipe_list[2].split()
# print(float(s_splited_recipe_list[0]), s_splited_recipe_list[1], s_splited_recipe_list[2:])

# 5.1.6

# recipes=[]
# def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
#    recipes.append((new_recipe))
#    return recipes

# new_recipe=("cake", "2 eggs", "30 g sugar")
# x=add_recipe(new_recipe, recipes)
# new_recipe2=("cookie", "an egg", "20 g sugar")
# x=add_recipe(new_recipe2, recipes)
# splited_recipes=recipes
# print(recipes)

# 5.1.7

# def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
#    for number in range(0,len(recipes)):
#        if recipe_name in recipes[number][0]:
#            return recipes[number]
#        else:
#            continue

# recipe_name="cookeie"
# y=find_recipe(recipe_name, recipes)
# print(y)

# 5.1.8
# def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
#    for number in range(0,len(recipes)):
#        if name in recipes[number][0]:
#            del recipes[number]

# name="cookie"
# y=remove_recipe(name, recipes)
# print(recipes)

# 5.1.9
# recipe=("cake", "2 eggs", "20 g coffee")

# x=str(recipe)
# y=x.split(", ")
# print(x)
# for number in range(0, len(y)):
#    if "coffee" in y[number]:
#        z=recipe[number].split()
#        print (tuple(float(z[0])))

# recipe=('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
# def get_ingredient_amout(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str] | None:
#    str_of_recipe=str(recipe)
#    splited_str_of_recipe=str_of_recipe.split(",")
#    for number in range(0, len(splited_str_of_recipe)):
#        if ingredient in splited_str_of_recipe[number]:
#            splited_recipe=recipe[number].split()
#            return (float(splited_recipe[0]), splited_recipe[1], splited_recipe[2])
# z=get_ingredient_amout("peanuts", recipe)
# print(z)

# 5.1.10
# shopping_list=[]
# x=(200.0, "g", "sugar")
# y=(300.0, "g", "salt")
# z=(300.0, "g", "sugar")
# shopping_list.append(list(x))
# shopping_list.append(list(y))

# for number in range(0, len(shopping_list)):
#     if list(z)[1:] == shopping_list[number][1:]:
#         shopping_list[number][0]=list(x)[0]+list(z)[0]
#         print(shopping_list)

# shopping_list=[]
# def add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str]] | None) -> None:
#     if len(shopping_list) == 0:
#         shopping_list.append(ingredient_details)
#     else:
#         for number in range(0, len(shopping_list)):
#             if ingredient_details[1:]==shopping_list[number][1:]:
#                 shopping_list[number]=(shopping_list[number][0]+ingredient_details[0], shopping_list[number][1], shopping_list[number][2])

# a=(300.0, "g", "sugar")
# add_to_shopping_list(a, shopping_list)
# c=(200.0, "g", "sugar")
# add_to_shopping_list(c, shopping_list)
# print(shopping_list)

# 5.1.11

# shopping_list=[(200.0, "g", "sugar"), (500.0, "g", "water")]

# x=("water")
# y=300.0
# for number in range(0, len(shopping_list)):
#     if x == shopping_list[number][2]:
#         if shopping_list[number][0] - y<=0 :
#             del shopping_list[number]
#         else:
#             shopping_list[number] = (shopping_list[number][0]-y, shopping_list[number][1], shopping_list[number][2])
#     else:
#         pass
# print(shopping_list)

# def remove_from_shopping_list(ingredient_name: str, amount:float, shopping_list: list) -> None:
#     for number in range(0, len(shopping_list)):
#         if ingredient_name == shopping_list[number][2]:
#             if shopping_list[number][0]-amount<=0:
#                 del shopping_list[number]
#             else:
#                 shopping_list[number]=(shopping_list[number][0]-amount, shopping_list[number][1], shopping_list[number][2])
#         else:
#             pass

# remove_from_shopping_list("sugar", 20.0, shopping_list)
# print(shopping_list)

# 5.1.12
# CHOCOLATE_PEANUT_BUTTER_SHAKE = ('chocolate peanut butter banana shake',
# 	'1 large banana,2 tbsp peanut butter,2 pitted dates,1 tbsp cacao powder,240 ml almond milk,0.5 cup ice,1 tbsp cocao nibs,1 tbsp flax seed')
# BROWNIE = ('chocolate brownies',
# 	'2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,80 g Nuttelex,125 g self-raising flour,70 g ground almonds,50 g cocoa powder,0.2 tsp baking powder,250 g sugar,1.5 tsp vanilla extract')
# PEANUT_BUTTER = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')

# x=PEANUT_BUTTER[1].split(",")
# y=(x[1]).split()
# print(y)

# shopping_list=[]
# def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
#     for number in range(0, len(recipes)):
#         splited_recipes=recipes[number][1].split(",")
#         for number_2 in range(0, len(splited_recipes)):
#             ingredient_list=[]
#             ingredient_in_shopping_list=splited_recipes[number_2].split()
#             ingredient_list.append(float(ingredient_in_shopping_list[0]))
#             ingredient_list.append(ingredient_in_shopping_list[1])
#             join_ingredient_in_shopping_list=" ".join(ingredient_in_shopping_list[2:])
#             ingredient_list.append(join_ingredient_in_shopping_list)
#             shopping_list.append(tuple(ingredient_list))

# generate_shopping_list([CHOCOLATE_PEANUT_BUTTER_SHAKE, BROWNIE, PEANUT_BUTTER])
# print(shopping_list)


# def generate_shopping(recipes) -> list[tuple[float, str, str]]:

# 5.1.13
# shopping_list=[(1.0, 'large', 'banana'), (2.0, 'tbsp', 'peanut'), (2.0, 'pitted', 'dates'), (1.0, 'tbsp', 'cacao'), (240.0, 'ml', 'almond'), (0.5, 'cup', 'ice'), (1.0, 'tbsp', 'cocao'), (1.0, 'tbsp', 'flax'), (2.0, 'tbsp', 'flaxseed'), (200.0, 'g', 'dark'), (0.5, 'tsp', 'coffee'), (80.0, 'g', 'Nuttelex'), (125.0, 'g', 'self-raising'), (70.0, 'g', 'ground'), (50.0, 'g', 'cocoa'), (0.2, 'tsp', 'baking'), (250.0, 'g', 'sugar'), (1.5, 'tsp', 'vanilla'), (300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil')]
# for number in range(0, len(x)):
# 	print("|", (str((x)[number][0])).center(7, " "), "|", str(((x)[number][1])).center(9, " "), "|", str(((x)[number][2])).center(16, " "), "|")

# def display_ingredient(shopping_list: list[tuple[float, str, str]]) -> None:
# 	sorted_recipes=sorted(shopping_list, key=lambda x:x[2][0])
# 	for number in range(0, len(sorted_recipes)):
# 		print ("|", (str((sorted_recipes)[number][0])).center(7, " "), "|", str(((sorted_recipes)[number][1])).center(9, " "), "|", str(((sorted_recipes)[number][2])).center(16, " "), "|")

# display_ingredient([(1.0, 'large', 'banana'), (2.0, 'tbsp', 'peanut'), (2.0, 'pitted', 'dates'), (1.0, 'tbsp', 'cacao'), (240.0, 'ml', 'almond'), (0.5, 'cup', 'ice'), (1.0, 'tbsp', 'cocao'), (1.0, 'tbsp', 'flax'), (2.0, 'tbsp', 'flaxseed'), (200.0, 'g', 'dark'), (0.5, 'tsp', 'coffee'), (80.0, 'g', 'Nuttelex'), (125.0, 'g', 'self-raising'), (70.0, 'g', 'ground'), (50.0, 'g', 'cocoa'), (0.2, 'tsp', 'baking'), (250.0, 'g', 'sugar'), (1.5, 'tsp', 'vanilla'), (300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil')])
# recipes=[(1.0, 'large', 'banana'), (2.0, 'tbsp', 'peanut'), (2.0, 'pitted', 'dates'), (1.0, 'tbsp', 'cacao'), (240.0, 'ml', 'almond'), (0.5, 'cup', 'ice'), (1.0, 'tbsp', 'cocao'), (1.0, 'tbsp', 'flax'), (2.0, 'tbsp', 'flaxseed'), (200.0, 'g', 'dark'), (0.5, 'tsp', 'coffee'), (80.0, 'g', 'Nuttelex'), (125.0, 'g', 'self-raising'), (70.0, 'g', 'ground'), (50.0, 'g', 'cocoa'), (0.2, 'tsp', 'baking'), (250.0, 'g', 'sugar'), (1.5, 'tsp', 'vanilla'), (300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil')]
# sorted_recipes=sorted(recipes, key=lambda x:x[2][0])
# print(sorted_recipes)

# 5.1.14
# def sanitise_command(command: str) -> str:
#     command_1 = command.strip(" 1234567890")
#     command_2 = command_1.lower()
#     print (command_2)

# z=sanitise_command("cooaa4444   4558")

# list=["1"]
# list2=["2","3"]
# list3=", ".join(list2)
# list.append(list3)
# print(list)

# 5.1.12
# shopping_list=[]
# def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
#     for number in range(0, len(recipes)):
#         splited_recipes=recipes[number][1].split(",")
#         for number_2 in range(0, len(splited_recipes)):
#             ingredient_list=[]
#             ingredient_in_shopping_list=splited_recipes[number_2].split()
#             ingredient_list.append(float(ingredient_in_shopping_list[0]))
#             ingredient_list.append(ingredient_in_shopping_list[1])
#             join_ingredient_in_shopping_list=" ".join(ingredient_in_shopping_list[2:])
#             ingredient_list.append(join_ingredient_in_shopping_list)
#             shopping_list.append(tuple(ingredient_list))
#     for number2 in range(0, len(shopping_list)):
#         for number3 in range(, len(shopping_list)):
#             if shopping_list[number2][3] ==


# generate_shopping_list([CHOCOLATE_PEANUT_BUTTER_SHAKE, BROWNIE, PEANUT_BUTTER])
# print(shopping_list)

# shopping_list=[(0.5, 'tsp', 'salt'), (300.0, 'g', 'peanuts'), (2.0, 'tsp', 'oil')]
# def add_to_shopping_list(ingredient_details, shopping_list):
#     count=0
#     if len(shopping_list) == 0:
#         shopping_list.append(ingredient_details)
#     else:
#         for number in range(0, len(shopping_list)):
#             if ingredient_details[1:]==shopping_list[number][1:]:
#                 shopping_list[number]=(shopping_list[number][0]+ingredient_details[0], shopping_list[number][1], shopping_list[number][2])
#                 break
#             else:
#                 count+=1
#         if count == len(shopping_list):
#             shopping_list.append(ingredient_details)
#         else:
#             pass


# def create_recipe() -> tuple[str, str]:
#     """create the recipes that you want to cook"""
#     list_for_create_recipe = []
#     recipes_name = input("Please enter the recipe name: ")
#     # list_for_ls_a.append(recipes_name)
#     list_for_create_recipe.append(recipes_name)
#     list_for_ingredient = []
#     ingredient = input("Please enter an ingredient:")
#     while ingredient != "":
#         list_for_ingredient.append(ingredient)
#         ingredient = input("Please enter an ingredient: ")
#     final_list_for_ingredient = ",".join(list_for_ingredient)
#     list_for_create_recipe.append(final_list_for_ingredient)
#     print(tuple(list_for_create_recipe))


# create_recipe()


# def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
#     """extract the amount of a few ingredients"""
#     recipe_list = list(recipe)
#     splited_recipe_list = recipe_list[1].split(",")
#     final_list = []
#     for number in range(0, len(splited_recipe_list)):
#         s_splited_recipe_list = splited_recipe_list[number].split()
#         value = (
#             float(s_splited_recipe_list[0]),
#             s_splited_recipe_list[1],
#             s_splited_recipe_list[2],
#         )
#         final_list.append(value)
#     print(tuple(final_list))


# recipe_ingredients(("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil"))


# def find_recipe(
#     recipe_name: str, recipes: list[tuple[str, str]]
# ) -> tuple[str, str] | None:
#     for number in range(0, len(recipes)):
#         if recipe_name in recipes[number][0]:
#             print(recipes[number])
#         else:
#             print(None)


# recipes = [("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil")]
# find_recipe("cake", recipes)


# def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
#     """remove a recipe which was in the recipeslist by name"""
#     for number in range(0, len(recipes)):
#         if name in recipes[number][0]:
#             del recipes[number]


# recipes = [
#     ("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil"),
#     (
#         "cinnamon rolls",
#         "480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla extract",
#     ),
# ]
# remove_recipe("brownie", recipes)
# remove_recipe("cinnamon rolls", recipes)
# print(recipes)


# def get_ingredient_amount(
#     ingredient: str, recipe: tuple[str, str]
# ) -> tuple[float, str] | None:
#     """get the total amount of a ingredient in recipes"""
#     str_of_recipe = str(recipe)
#     splited_str_of_recipe = str_of_recipe.split(",")
#     for number in range(0, len(splited_str_of_recipe)):
#         if ingredient in splited_str_of_recipe[number]:
#             splited_recipe = splited_str_of_recipe[number].split()
#             x = (float(splited_recipe[0]), (splited_recipe[1]))
#             print(x)


# recipe = (
#     "cinnamon rolls",
#     "480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla extract",
# )


# get_ingredient_amount("almond milk", recipe)


# def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
#     sorted_recipes = sorted(shopping_list, key=lambda x: x[2][0])
#     for number in range(0, len(sorted_recipes)):
#         print(
#             "|",
#             (str((sorted_recipes)[number][0])).center(7, "x"),
#             "|",
#             str(((sorted_recipes)[number][1])).center(9, "x"),
#             "|",
#             str(((sorted_recipes)[number][2])).center(16, "x"),
#             "|",
#         )


# display_ingredients(
#     [
#         (
#             "chocolate peanut butter banana shake",
#             "1 large banana,2 tbsp peanut butter,2 pitted dates,1 tbsp cacao powder,240 ml almond milk,0.5 cup ice,1 tbsp cocao nibs,1 tbsp flax seed",
#         )
#     ]
# )


# def create_recipe() -> tuple[str, str]:
#     """create the recipes that you want to cook"""
#     list_for_create_recipe = []
#     recipes_name = input("Please enter the recipe name: ")
#     # list_for_ls_a.append(recipes_name)
#     list_for_create_recipe.append(recipes_name)
#     list_for_ingredient = []
#     ingredient = input("Please enter an ingredient: ")
#     while ingredient != "":
#         list_for_ingredient.append(ingredient)
#         ingredient = input("Please enter an ingredient: ")
#     final_list_for_ingredient = ",".join(list_for_ingredient)
#     list_for_create_recipe.append(final_list_for_ingredient)
#     return tuple(list_for_create_recipe)


# create_recipe()


# def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
#     """extract the amount of a few ingredients"""
#     recipe_list = list(recipe)
#     splited_recipe_list = recipe_list[1].split(",")
#     final_list = []
#     for number in range(0, len(splited_recipe_list)):
#         s_splited_recipe_list = splited_recipe_list[number].split(maxsplit=2)
#         value = (
#             float(s_splited_recipe_list[0]),
#             s_splited_recipe_list[1],
#             s_splited_recipe_list[2],
#         )
#         final_list.append(value)
#     return tuple(final_list)


# x = recipe_ingredients(
#     (
#         "chocolate peanut butter banana shake",
#         "1 large banana,2 tbsp peanut butter,2 pitted dates,1 tbsp cacao "
#         "powder,240 ml almond milk,0.5 cup ice,1 tbsp cocao nibs,1 tbsp flax seed",
#     )
# )
# print(x)


# def find_recipe(
#     recipe_name: str, recipes: list[tuple[str, str]]
# ) -> tuple[str, str] | None:
#     for number in range(0, len(recipes)):
#         if recipe_name in recipes[number][0]:
#             return recipes[number]


# recipes = [
#     ("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil"),
#     (
#         "chocolate brownies",
#         "2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,80 g "
#         "Nuttelex,125 g self-raising flour,70 g ground almonds,50 g cocoa "
#         "powder,0.2 tsp baking powder,250 g sugar,1.5 tsp vanilla extract",
#     ),
#     (
#         "cinnamon rolls",
#         "480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry yeast,5.5 cup "
#         "flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp cinnamon,160 g "
#         "powdered sugar,30 ml almond milk,0.5 tsp vanilla extract",
#     ),
# ]

# x = find_recipe("cinnamon rolls", recipes)
# print(x)


# def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
#     """remove a recipe which was in the recipeslist by name"""
#     for number in range(0, len(recipes)):
#         if name in recipes[number][0]:
#             del recipes[number]
#         return recipes


# recipes = [
#     ("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil"),
#     (
#         "cinnamon rolls",
#         "480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry yeast,5.5 cup "
#         "flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp cinnamon,160 g "
#         "powdered sugar,30 ml almond milk,0.5 tsp vanilla extract",
#     ),
# ]

# remove_recipe("peanut butter", recipes)

# print(recipes)


# def get_ingredient_amount(
#     ingredient: str, recipe: tuple[str, str]
# ) -> tuple[float, str] | None:
#     """get the total amount of a ingredient in recipes"""
#     str_of_recipe = str(recipe)
#     splited_str_of_recipe = str_of_recipe.split(",")
#     for number in range(0, len(splited_str_of_recipe)):
#         if ingredient in splited_str_of_recipe[number]:
#             splited_recipe = splited_str_of_recipe[number].split()
#             x = (float(splited_recipe[0]), (splited_recipe[1]))
#             return x


# recipe = ("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil")
# get_ingredient_amount("peanuts", recipe)
# print(recipe)


# def get_ingredient_amount(ingredient, recipe):
#     """get the total amount of a ingredient in recipes"""
#     count = 0
#     str_of_recipe = str(recipe)
#     str_of_recipe2 = str_of_recipe.strip("'()")
#     splited_str_of_recipe = str_of_recipe2.split(", '")
#     final_splited_str_of_recipe = splited_str_of_recipe[1].split(",")
#     for number in range(0, len(final_splited_str_of_recipe)):
#         if ingredient in splited_str_of_recipe[number]:
#             splited_recipe = final_splited_str_of_recipe[number].split()
#             x = (float(splited_recipe[0]), (splited_recipe[1]))
#             return x
#         else:
#             count += 1
#         if count == len(final_splited_str_of_recipe):
#             return None


# recipe = ("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil")
# z = get_ingredient_amount("", recipe)
# print(z)

# shopping_list = []


# def generate_shopping_list(
#     recipes: list[tuple[str, str]]
# ) -> list[tuple[float, str, str]]:
#     for number in range(0, len(recipes)):
#         splited_recipes = recipes[number][1].split(",")
#         for number_2 in range(0, len(splited_recipes)):
#             ingredient_list = []
#             ingredient_in_shopping_list = splited_recipes[number_2].split()
#             ingredient_list.append(float(ingredient_in_shopping_list[0]))
#             ingredient_list.append(ingredient_in_shopping_list[1])
#             join_ingredient_in_shopping_list = " ".join(ingredient_in_shopping_list[2:])
#             ingredient_list.append(join_ingredient_in_shopping_list)
#             shopping_list.append(tuple(ingredient_list))
#         print(shopping_list)


# generate_shopping_list(
#     [
#         ("peanut butter", "300 g peanuts,0.5 tsp salt,2 tsp oil"),
#         (
#             "chocolate brownies",
#             "2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,80 g "
#             "Nuttelex,125 g self-raising flour,70 g ground almonds,50 g cocoa "
#             "powder,0.2 tsp baking powder,250 g sugar,1.5 tsp vanilla extract",
#         ),
#     ]
# )

# 5.1.13
# """print shoppinglist out as a more readable form"""


# 5.1.13
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
                max_amount_of_ingredient_measure,
                ingredient[2],
                max_amount_of_ingredient_name,
            )
        )


x = display_ingredients(
    [
        (1.0, "large", "banana"),
        (2.0, "tbsp", "peanut butter"),
        (2.0, "pitted", "dates"),
        (1.0, "tbsp", "cacao powder"),
        (240.0, "ml", "almond milk"),
        (0.5, "cup", "ice"),
        (1.0, "tbsp", "cocao nibs"),
        (1.0, "tbsp", "flax seed"),
    ]
)
