# Pablo Perez
# 1770045

class FoodItem:
    # Define constructor with parameters to initialize name, fat, carbs, protein
    def __init__(self, name, fat, carbs, protein):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":

    name1 = input()
    fat1 = float(input())
    carbs1 = float(input())
    protein1 = float(input())
    servings = float(input())

    test = FoodItem(None, 0, 0, 0)
    test.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, test.get_calories(servings)))
    print("")

    food_item = FoodItem(name1, fat1, carbs1, protein1)
    food_item.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, food_item.get_calories(servings)))