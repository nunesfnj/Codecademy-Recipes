class Recipe():
    recipes_list = [{0: [20, 4.8, 2.2, 30, 'whey_max_cookies']}, {1: [0, 47, 0, 50, 'dextrose_growth']}]
    recipes_by_keys = {0: 'taca 200ml de agua na boqueteleira + o pozinho e marcha', 1: 'esse aq eh açucar purin, so taca agua e ta pronto sovetinho'}
    def __init__(self, index):

        self.protein = Recipe.recipes_list[index][index][0]
        self.carbs = Recipe.recipes_list[index][index][1]
        self.fat = Recipe.recipes_list[index][index][2]
        self.portion = Recipe.recipes_list[index][index][3]
        self.name = Recipe.recipes_list[index][index][4]

for i in range(len(Recipe.recipes_list)):
    recipe_i = Recipe(i)
    # print(f"recipe_{i + 1} info:")
    # print(recipe_i.protein, 'protein')
    # print(recipe_i.carbs, 'carbs')
    # print(recipe_i.fat, 'fat')
    # print(f"portion of {recipe_i.portion}g")
    # print(recipe_i.name, '\n')

macro_goal = input('para qual macro vc quer a melhor receita (para uma porcao normal)?: (p, c, f)')

if macro_goal == 'p':
    protein_deficit = float(input('quantos g de proteina faltam no seu dia?: '))
    diff = 1000
    closest_goal = None
    for i in range(len(Recipe.recipes_list)):
        if (protein_deficit - Recipe.recipes_list[i][i][0]) < diff:
            closest_goal = Recipe.recipes_list[i][i]
            diff = protein_deficit - Recipe.recipes_list[i][i][0]

if macro_goal == 'c':
    carbs_deficit = float(input('quantos g de carboidratos faltam no seu dia?: '))
    diff = 1000
    closest_goal = None
    for i in range(len(Recipe.recipes_list)):
        if (carbs_deficit - Recipe.recipes_list[i][i][1]) < diff:
            closest_goal = Recipe.recipes_list[i][i]
            diff = carbs_deficit - Recipe.recipes_list[i][i][1]
            
if macro_goal == 'f':
    fat_deficit = float(input('quantos g de gordura faltam no seu dia?: '))
    diff = 1000
    closest_goal = None
    for i in range(len(Recipe.recipes_list)):
        if (fat_deficit - Recipe.recipes_list[i][i][2]) < diff:
            closest_goal = Recipe.recipes_list[i][i]
            diff = fat_deficit - Recipe.recipes_list[i][i][2]

print(f'sua melhor escolha é: ', closest_goal)


#segunda logica que oferece escolher qual receita de uma lista de opcoes viaveis

# recipes_options = []
# choice = 1 #

# print(f'receita escolhida: {Recipe.recipes_list[choice][choice][4]}\n') #name
# print(f'''macros per portion of {recipe_i.portion}g:\n
#       {recipe_i.protein}g of protein
#       {recipe_i.carbs}g of carbs
#       {recipe_i.fat}g of fat\n''')
# print(Recipe.recipes_by_keys[choice])


