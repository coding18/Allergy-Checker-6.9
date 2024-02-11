food_dict = {
    "pizza": ["dough", "tomato sauce", "cheese", "toppings"],
    "burger":
    ["burger bun", "beef patty", "cheese", "lettuce", "tomato", "onion"],
    "pasta": ["pasta noodles", "tomato sauce", "meatballs", "parmesan cheese"],
    "salad": ["lettuce", "tomato", "cucumber", "onion", "dressing"],
    "sandwich": ["bread", "meat", "cheese", "lettuce", "tomato"],
    "soup": ["broth", "vegetables", "meat"],
    "tacos": ["tortillas", "meat", "cheese", "lettuce", "tomato"],
    "burritos":
    ["tortillas", "meat", "rice", "beans", "cheese", "lettuce", "tomato"],
    "enchiladas": ["tortillas", "meat", "cheese", "sauce"],
    "fajitas": ["meat", "vegetables", "tortillas"],
    "stir-fry": ["meat", "vegetables", "sauce"],
    "fried rice": ["rice", "meat", "vegetables", "eggs"],
    "sushi": ["rice", "fish", "vegetables"],
    "sashimi": ["fish"],
    "chicken": ["chicken breast", "chicken thighs", "chicken wings"],
    "beef": ["beef steak", "ground beef", "beef roast"],
    "pork": ["pork chops", "pork tenderloin", "ground pork"],
    "fish": ["salmon", "tuna", "cod"],
    "vegetables": ["broccoli", "carrots", "celery", "onions", "peppers"],
    "dairy": ["milk", "cheese", "yogurt"],
    "grains": ["rice", "pasta", "bread"],
    "spices":
    ["salt", "pepper", "garlic powder", "onion powder", "chili powder"],
    "dal": ["lentils", "spices"],
    "samosas": ["dough", "potatoes", "peas", "spices"],
    "naan": ["bread", "yeast", "water", "flour"],
    "tandoori chicken": ["chicken", "yogurt", "spices"],
    "tikka masala": ["chicken", "tomato sauce", "spices"],
    "butter chicken": ["chicken", "tomato sauce", "butter", "spices"],
    "vindaloo": ["meat", "potatoes", "spices"],
    "biryani": ["rice", "meat", "vegetables", "spices"],
    "chutney": ["fruit", "spices"],
    "pad thai": [
        "rice noodles", "shrimp", "chicken", "tofu", "peanuts", "bean sprouts",
        "lime", "fish sauce", "tamarind sauce", "palm sugar", "dried shrimp",
        "garlic", "shallots", "red chili pepper", "vegetable oil"
    ],
    "tom yum goong": [
        "shrimp", "lemongrass", "galangal", "kaffir lime leaves", "lime juice",
        "fish sauce", "chilies", "mushrooms", "tomatoes", "cilantro"
    ],
    "green curry": [
        "chicken", "green chilies", "coconut milk", "lemongrass", "galangal",
        "kaffir lime leaves", "fish sauce", "lime juice", "basil leaves"
    ],
    "massaman curry": [
        "chicken", "potatoes", "peanuts", "coconut milk", "lemongrass",
        "galangal", "kaffir lime leaves", "fish sauce", "palm sugar",
        "cinnamon", "cardamom", "cumin"
    ],
    "pad see ew": [
        "rice noodles", "chicken", "shrimp", "chinese broccoli", "soy sauce",
        "oyster sauce", "garlic", "black pepper"
    ],
    "som tum": [
        "papaya", "tomatoes", "green beans", "peanuts", "lime juice",
        "fish sauce", "chilies", "garlic", "sugar"
    ],
    "larb": [
        "ground chicken", "lime juice", "fish sauce", "chilies", "mint leaves",
        "cilantro", "red onion", "roasted rice powder"
    ],
    "khao man gai": [
        "chicken", "rice", "garlic", "ginger", "soy sauce", "sesame oil",
        "cucumber"
    ],
    "roti": ["flatbread", "wheat flour", "water", "oil"],
    "mango sticky rice": ["mango", "sticky rice", "coconut milk"],
    "maraq": ["lentils", "spices"],
    "suqaar": ["diced beef", "soup"],
    "odkac": ["dried beef, goat, or camel meat", "ghee"],
    "xalwo": ["ground meat", "potatoes", "onion", "vegetables", "flour"],
    "gahsaato": ["coconut"],
    "camboo": ["mango"],
    "seytuun": ["guava"],
    "moos": ["banana"],
    "liinbanbeelmo": ["grapefruit"],
    "mapo tofu": [
        "tofu", "ground beef", "fermented bean paste", "doubanjiang", "garlic",
        "ginger", "sichuan peppercorns"
    ],
    "kung pao chicken": [
        "chicken", "peanuts", "vegetables", "soy sauce", "shaoxing wine",
        "ginger", "garlic"
    ],
    "chow mein":
    ["noodles", "vegetables", "meat", "soy sauce", "oyster sauce"],
    "fried rice": ["rice", "meat", "vegetables", "eggs"],
    "wonton soup": ["wontons", "broth", "vegetables"],
    "dumplings": ["dough", "filling"],
    "spring rolls": ["dough", "filling"],
    "lo mein": ["noodles", "vegetables", "meat", "sauce"],
    "egg foo young": ["eggs", "vegetables", "meat", "sauce"],
    "sweet and sour pork":
    ["pork", "vegetables", "pineapple", "sweet and sour sauce"],
    "moo shu pork": ["pork", "vegetables", "mushrooms", "hoisin sauce"],
    "general tso's chicken": ["chicken", "vegetables", "sweet and sour sauce"],
    "noodles": ["noodles", "vegetables", "meat", "sauce"],
    "lasagna": [
        "lasagna noodles", "ricotta cheese", "mozzarella cheese",
        "ground beef", "tomato sauce", "onion", "garlic", "basil", "oregano"
    ],
    "spaghetti carbonara":
    ["spaghetti", "eggs", "bacon", "Parmesan cheese", "black pepper"],
    "risotto": [
        "Arborio rice", "white wine", "chicken broth", "onion", "garlic",
        "Parmesan cheese"
    ],
    "tiramisu": [
        "ladyfingers", "espresso", "mascarpone cheese", "eggs", "sugar",
        "cocoa powder"
    ],
    "creme brulee": ["egg yolks", "sugar", "cream", "vanilla extract"],
    "ravioli": ["pasta", "cheese", "meat", "vegetables", "sauce"],
    "fettuccine": ["pasta", "cheese", "meat", "vegetables", "sauce"],
    "chocolate": ["chocolate", "milk", "sugar"],
    "coffee": ["coffee beans", "water", "sugar", "milk"],
    "tea": ["tea leaves", "water", "sugar", "milk"],
    "juice": ["fruit juice", "sugar", "water"],
    "chocolate milk": ["chocolate", "milk", "sugar"],
    "cookies": ["flour", "sugar", "butter", "eggs", "vanilla extract"],
    "cake":
    ["flour", "sugar", "eggs", "milk", "baking powder", "vanilla extract"],
    "pie": ["flour", "sugar", "eggs", "milk", "butter", "vanilla extract"],
    "ice cream": ["milk", "cream", "sugar", "vanilla extract"],
    "popcorn": ["popcorn kernels", "sugar", "water"],
    "chips": ["potatoes", "salt", "flour", "butter"],
    "burgers": ["beef patty", "buns", "lettuce", "tomato", "cheese"],
    "gulab jamun": ["sugar", "cashew nuts", "milk", "almonds"],
    "kaju katli":
    ["rice flour", "cashew nuts", "milk", "almonds", "silver stuff"],
    "poutine": ["french fries", "cheese", "sauce"],
    "french fries": ["potatoes", "salt", "butter"],
    "mac and cheese": ["pasta", "cheese", "milk", "butter"],
    "chicken nuggets": ["chicken", "salt", "flour", "butter"],
    "fried chicken": ["chicken", "oil", "salt", "pepper"],
    "gluten free food": ["You gonna starve tonight"],
    "fish sticks": ["fish", "salt", "flour", "butter"]
}

allergens = {
    "milk", "butter", "cheese", "yogurt", "cream", "ice cream", "milkshake",
    "smoothie", "ice", "chocolate milk", "eggs", "fish", "fish sauce",
    "fish roast", "fish soup", "fish stew", "fish salad", "fish", "oyster",
    "shrimp", "crab", "lobster", "clam", "mussels", "scallops", "shellfish"
}

allergy = input("Do you have allergies?  (y/n): ")

if allergy.lower() == "y":
  all = input("What are your allergies? ")
  if all != "gluten":
    food = input("Enter the dish you're going to eat: ")
    for ingredient in food_dict[food]:
      if ingredient in all and allergens:
        print("You can't eat that dish")
        break
    else:
      if food in food_dict:
        print(f"Ingredients for {food}:")
        for ingredient in food_dict[food]:
          print(ingredient)

      else:
        print("Food not found in the list.")

  else:
    print("You can't eat anything with gluten")

else:
  food = input("Enter the dish you're going to eat: ")
  if food in food_dict:
    print(f"Ingredients for {food}:")
    for ingredient in food_dict[food]:
      print(ingredient)
  else:
    print("Food not found in the list.")
