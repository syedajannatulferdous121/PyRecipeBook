import json

def load_recipes():
    try:
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
    except FileNotFoundError:
        recipes = []
    return recipes

def save_recipes(recipes):
    with open('recipes.json', 'w') as file:
        json.dump(recipes, file, indent=4)

def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    instructions = input("Enter the cooking instructions: ")
    cuisine = input("Enter the cuisine type: ")
    recipe = {
        'name': name,
        'ingredients': ingredients,
        'instructions': instructions,
        'cuisine': cuisine
    }
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")

def view_recipes():
    if not recipes:
        print("No recipes found.")
        return
    print("Cuisine Types:")
    cuisine_types = set(recipe['cuisine'] for recipe in recipes)
    for index, cuisine in enumerate(cuisine_types, start=1):
        print(f"{index}. {cuisine}")
    choice = input("Enter the cuisine number to view recipes: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(cuisine_types):
            print("Invalid cuisine number.")
            return
    except ValueError:
        print("Invalid input.")
        return
    selected_cuisine = list(cuisine_types)[choice - 1]
    selected_recipes = [recipe for recipe in recipes if recipe['cuisine'] == selected_cuisine]
    if not selected_recipes:
        print(f"No recipes found for cuisine '{selected_cuisine}'.")
        return
    for index, recipe in enumerate(selected_recipes, start=1):
        print(f"\nRecipe {index}:")
        print(f"Name: {recipe['name']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"\nInstructions:")
        print(recipe['instructions'])

def delete_recipe():
    view_recipes()
    if not recipes:
        return
    choice = input("Enter the recipe number to delete: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(recipes):
            print("Invalid recipe number.")
            return
    except ValueError:
        print("Invalid input.")
        return
    recipe = recipes.pop(choice - 1)
    save_recipes(recipes)
    print(f"Recipe '{recipe['name']}' deleted successfully!")

def display_menu():
    print("\nPyRecipeBook - Recipe Management System")
    print("1. Add Recipe")
    print("2. View Recipes")
    print("3. Delete Recipe")
    print("4. Exit")

recipes = load_recipes()

# Preloaded recipes
recipes += [
    {
        'name': 'Biryani',
        'ingredients': [
            '2 cups Basmati rice',
            '500g Chicken',
            '1/2 cup Yogurt',
            '2 tsp Ginger-garlic paste',
            '2 tsp Biryani masala',
            '1 tsp Turmeric powder',
            '2 Onions (sliced)',
            '4 Green chilies (slit)',
            '4 tbsp Oil',
            'Salt to taste'
        ],
        'instructions': '''
            1. Wash the rice and soak it for 30 minutes. Drain and set aside.
            2. Heat oil in a large pan and fry the sliced onions until golden brown. Remove half of the fried onions and set aside.
            3. In the same pan, add ginger-garlic paste and green chilies. Sauté for a minute.
            4. Add chicken pieces and cook until they turn white. Then, add yogurt, turmeric powder, biryani masala, and salt. Mix well and cook for 5-7 minutes.
            5. In a separate pot, bring water to a boil. Add the soaked and drained rice, along with some salt. Cook until the rice is 70% done. Drain the rice.
            6. Layer the partially cooked rice over the chicken in the pan. Sprinkle the reserved fried onions on top.
            7. Cover the pan with a tight-fitting lid and cook on low heat for about 15-20 minutes until the rice is fully cooked and flavors are well blended.
            8. Serve the flavorful biryani hot with raita or salad.
        ''',
        'cuisine': 'Bangladeshi'
    },
    {
        'name': 'Roshogolla',
        'ingredients': [
            '1 liter Milk',
            '2 tbsp Lemon juice',
            '1 cup Sugar',
            '4 cups Water'
        ],
        'instructions': '''
            1. Boil the milk in a large pot.
            2. Once the milk comes to a boil, add lemon juice gradually while stirring continuously until the milk curdles and the whey separates.
            3. Turn off the heat and let it sit for 2-3 minutes.
            4. Line a strainer or colander with a muslin cloth or cheesecloth. Pour the curdled milk into the strainer to separate the whey.
            5. Rinse the curdled milk under running water to remove the lemon flavor.
            6. Gather the edges of the cloth and squeeze out any excess water. Hang the cloth for 30 minutes to remove remaining water.
            7. In the meantime, prepare the sugar syrup by dissolving sugar in water and boiling it for 5 minutes.
            8. Once the curdled milk is well-drained, transfer it to a clean surface and knead it for 5-7 minutes until it becomes smooth and soft.
            9. Divide the dough into small portions and shape them into round balls.
            10. Drop the balls into the sugar syrup and cover the pot. Cook on medium heat for 10-12 minutes until the balls become light and spongy.
            11. Remove from heat and let the rasgullas cool down to room temperature.
            12. Refrigerate and serve the chilled rasgullas for a delightful dessert.
        ''',
        'cuisine': 'Bangladeshi'
    },
    {
        'name': 'Shorshe Ilish',
        'ingredients': [
            '500g Hilsa fish',
            '4 tbsp Mustard paste',
            '1/2 tsp Turmeric powder',
            '4 Green chilies (slit)',
            '4 tbsp Mustard oil',
            'Salt to taste'
        ],
        'instructions': '''
            1. Marinate the fish with turmeric powder and salt. Set aside for 15 minutes.
            2. Heat mustard oil in a pan and fry the marinated fish until golden brown on both sides. Remove the fish from the pan and set aside.
            3. In the same pan, add the green chilies and sauté for a minute.
            4. Reduce the heat and add the mustard paste. Stir well to mix with the oil and cook for 2-3 minutes.
            5. Add salt and 1 cup of warm water to the pan. Mix well to make a sauce.
            6. Gently slide the fried fish into the sauce. Cover the pan and cook on low heat for 5-7 minutes until the fish is cooked and the flavors are infused.
            7. Serve the Shorshe Ilish with steamed rice for a traditional Bengali delight.
        ''',
        'cuisine': 'Bangladeshi'
    },
    {
        'name': 'Jerk Chicken',
        'ingredients': [
            '2 lbs Chicken',
            '1/4 cup Soy sauce',
            '2 tbsp Lime juice',
            '2 tbsp Brown sugar',
            '1 tbsp Olive oil',
            '4 cloves Garlic (minced)',
            '2 tsp Ginger (minced)',
            '2 tsp Thyme',
            '2 tsp Allspice',
            '1 tsp Cinnamon',
            '1 tsp Nutmeg',
            '1 tsp Black pepper',
            '1 tsp Salt',
            '2 Scotch bonnet peppers (minced)'
        ],
        'instructions': '''
            1. In a bowl, combine soy sauce, lime juice, brown sugar, olive oil, minced garlic, minced ginger, thyme, allspice, cinnamon, nutmeg, black pepper, salt, and minced Scotch bonnet peppers.
            2. Place the chicken in a ziplock bag and pour the marinade over it. Seal the bag and refrigerate for at least 2 hours or overnight.
            3. Preheat the grill to medium-high heat.
            4. Remove the chicken from the marinade, allowing any excess to drip off.
            5. Grill the chicken for about 6-8 minutes per side, or until it reaches an internal temperature of 165°F (74°C).
             6. Remove the chicken from the grill and let it rest for a few minutes.
            7. Serve the jerk chicken with rice, beans, and a side of grilled vegetables for a flavorful Caribbean meal.
        ''',
        'cuisine': 'Caribbean'
    },
    {
        'name': 'Pho',
        'ingredients': [
            '8 cups Beef or Chicken broth',
            '250g Rice noodles',
            '300g Beef or Chicken (sliced)',
            '1 Onion (sliced)',
            '2 cloves Garlic (minced)',
            '1 tbsp Ginger (minced)',
            '2 Star anise',
            '2 Cinnamon sticks',
            '4 tbsp Fish sauce',
            '1 Lime (cut into wedges)',
            'Bean sprouts, Basil, Cilantro, Jalapeno (for garnish)'
        ],
        'instructions': '''
            1. In a large pot, add the broth, star anise, cinnamon sticks, onion, garlic, and ginger. Bring to a boil and let it simmer for 30 minutes to infuse the flavors.
            2. Meanwhile, cook the rice noodles according to the package instructions. Drain and set aside.
            3. Remove the star anise and cinnamon sticks from the broth. Add the sliced beef or chicken and cook for a few minutes until cooked through.
            4. Stir in the fish sauce and adjust the seasoning if needed.
            5. Divide the cooked noodles into serving bowls. Ladle the hot broth with beef or chicken over the noodles.
            6. Serve the pho with lime wedges, bean sprouts, basil, cilantro, and jalapeno on the side. Let each person customize their bowl with the desired garnishes.
        ''',
        'cuisine': 'Vietnamese'
    },
    {
        'name': 'Bibimbap',
        'ingredients': [
            '2 cups Cooked rice',
            '200g Beef (sliced)',
            '1 Carrot (julienned)',
            '1 Zucchini (julienned)',
            '1 cup Spinach',
            '4 Eggs',
            '2 tbsp Sesame oil',
            '2 tbsp Soy sauce',
            '1 tbsp Gochujang (Korean chili paste)',
            '2 cloves Garlic (minced)',
            'Salt to taste',
            'Vegetable oil (for frying)'
        ],
        'instructions': '''
            1. Marinate the beef slices with soy sauce, sesame oil, minced garlic, and salt. Set aside for 15 minutes.
            2. Heat a pan with vegetable oil and sauté the marinated beef until cooked. Set aside.
            3. In the same pan, add a little more oil and stir-fry the carrots and zucchini until tender-crisp. Season with salt. Set aside.
            4. Blanch the spinach in boiling water for a minute. Drain and squeeze out the excess water. Season with salt and sesame oil. Set aside.
            5. Fry the eggs sunny-side up or to your desired doneness.
            6. In a serving bowl, place the cooked rice at the bottom. Arrange the cooked beef, carrots, zucchini, spinach, and fried eggs on top in separate sections.
            7. Serve the bibimbap with gochujang on the side. Mix everything together before eating to enjoy the delicious flavors.
        ''',
        'cuisine': 'Korean'
    },
    {
        'name': 'Sauerbraten',
        'ingredients': [
            '2 lbs Beef roast',
            '2 cups Beef broth',
            '1 cup Red wine',
            '1 Onion (sliced)',
            '2 Carrots (sliced)',
            '2 stalks Celery (sliced)',
            '4 cloves Garlic (minced)',
            '4 Bay leaves',
            '10 Peppercorns',
            '4 tbsp Vegetable oil',
            '2 tbsp Flour',
            '2 tbsp Brown sugar',
            '2 tbsp Red wine vinegar',
            'Salt and pepper to taste'
        ],
        'instructions': '''
            1. In a large bowl, combine red wine, beef broth, sliced onion, carrots, celery, minced garlic, bay leaves, peppercorns, salt, and pepper. Mix well to make the marinade.
            2. Place the beef roast in a ziplock bag and pour the marinade over it. Seal the bag and refrigerate for at least 2 days, turning the roast occasionally.
            3. Remove the beef roast from the marinade and pat it dry with paper towels. Reserve the marinade.
            4. Heat vegetable oil in a large pot or Dutch oven over medium-high heat. Sear the beef roast on all sides until browned.
            5. Reduce the heat to low. Sprinkle flour and brown sugar over the roast, and cook for a few minutes, stirring continuously.
            6. Slowly pour the reserved marinade and red wine vinegar into the pot, scraping the bottom to release any browned bits.
            7. Cover the pot and simmer on low heat for about 3-4 hours until the meat is tender, stirring occasionally.
            8. Remove the beef roast from the pot and let it rest for a few minutes before slicing.
            9. Strain the cooking liquid and return it to the pot. Bring the liquid to a boil and simmer for a few minutes until it thickens to a gravy consistency.
            10. Serve the sliced sauerbraten with the thickened gravy, along with potatoes or dumplings for a traditional German meal.
        ''',
        'cuisine': 'German'
    }
]

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_recipe()
    elif choice == '2':
        view_recipes()
    elif choice == '3':
        delete_recipe()
    elif choice == '4':
        print("Thank you for using PyRecipeBook. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
