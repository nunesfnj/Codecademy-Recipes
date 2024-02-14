class Recipe():
    recipes_list = [{0: [20, 4.8, 2.2, 30, 'whey_max_cookies']}, {1: [0, 47, 0, 50, 'dextrose_growth']}]
    recipes_by_keys = {0: 'taca 200ml de agua na boqueteleira + o pozinho e marcha'}
    def __init__(self, index):

        self.protein = Recipe.recipes_list[index][index][0]
        self.carbs = Recipe.recipes_list[index][index][1]
        self.fat = Recipe.recipes_list[index][index][2]
        self.portion = Recipe.recipes_list[index][index][3]
        self.name = Recipe.recipes_list[index][index][4]

for i in range(len(Recipe.recipes_list)):
    recipe_i = Recipe(i)
    print(f"recipe_{i + 1} info:")
    print(recipe_i.protein, 'protein')
    print(recipe_i.carbs, 'carbs')
    print(recipe_i.fat, 'fat')
    print(f"portion of {recipe_i.portion}g")
    print(recipe_i.name, '\n')
