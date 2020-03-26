import pickle

canteen2 = {
    'chicken rice': [[['Steamed chicken rice',2.80,618],['Roasted chicken rice',2.80,524],['Lemon chicken rice',2.80,575],['Roasted Pork rice',2.80,405],['Char siew rice',2.80,595]],
                     []],
    'noodles': [[['Ban Mian',3.50,475],['Braised pork noodles',3.50,659],['Pork ribs noodles',4.00,696],['Sliced fish soup',3.50,349],['Seafood soup',3.50,306]],
                []],
    'waffles': [[['plain waffle',1.30,142],['chocolate waffle',1.80,250],['Peanut waffle',1.80,263],['Ham and Cheese waffle',2.20,297],['Ice cream waffle(3scoops',2.50,321]],
                []],
    'xiao long bau': [[['Xiao Long Bao (6pcs)',4.80,372],['Chicken Siew Mai (6pcs)',4.20,630],['Shanghai Deep Fried Dumpling (6pcs)',4.80,593],['Beijing Steamed Dumpling (6pcs)',4.80,467],['Shan Dong Pancake',1.80,285]],
                      []],
    'indian': [[['Plain Naan/Prata',1.00,164],['Nasi Briyani',4.00,880],['Chicken Curry',2.50,450],['Fried Rice',3.50,580],['Butter Chicken',3.50,391]],
               []]
     }

koufu    = {
    'pasta express': [[['Carbonara',5.10,630],['Beef Bolognese',5.10,564],['Spaghetti + Sauce',2.60,218],['Meat Toppings',1.00,180],['Vegetable Toppings',0.50,65]],
                      []],
    'japanese': [[['Chicken Karaage Don',4.50,599],['Oyako Don',4.60,506],['Salmon Don',4.80,565],['Chicken Teriyaki Don',4.50,561],['Hotplate Chicken Set',4.20,588]],
                 []],
    'vegetarian': [[['Vegetarian Curry Noodle',4.00,563],['Vegetarian Kway Chap',3.80,648],['Vegetarian Laksa',3.80,700],['Vegetarian Hor Fun',3.80,667],['Vegetarian Chicken Rice',3.00,618]],
                   []],
    'mixed rice': [[['3 Veg',2.70,195],['1 Meat + 1 Veg',2.50,245],['1 Meat + 2 Veg',3.00,310],['2 Meat + 1 Veg',3.50,345],['2 Meat + 2 Veg',3.90,605]],
                   []],
    'drinks': [[['Milo',1.50,414],['Iced Lemon Tea',1.40,142],['Water Chestnut',1.40,97],['Fresh Fruits',0.50,52],['Fruit Juice',2.00,120]],
               [['Coffee/Tea & French Toast',2.20,376],['Coffee/Tea & Cheese Toast',2.20,407],['Youtiao with Soy Milk',2.40,345],['Char Siew Pau with Coffee/Tea',2.40,378]]]
    }

tamarind = {
    'mala': [[['Vegetable Bundle',0.80,65],['Enoki Mushroom',0.80,87],['Pork Belly/Beef',1.00,180],['Fish',1.20,246],['Noodle',1.00,294]],
             []],
    'western': [[['Chicken Chop',5.00,522],['Grilled Fish',5.20,540],['Beef Steak',6.00,603],['Chicken Burger',3.50,536],['Lamb Chop',5.50,685]],
                []],
    'korean': [[['Bibimbap',5.20,940],['Mini Kimbap',2.40,79],['Ramen',4.80,436],['Kimchi Soup',4.00,469],['Kimchi Fried Rice',4.80,674]],
               []],
    'japanese': [[['Oyako Don',4.50,506],['Salmon Don',5.50,565],['Ebi Fry Don',4.50,585],['Hotplate Chicken Set',4.30,588],['Miso Chicken Noodle',4.30,472]],
                 []],
    'drinks': [[['Coffee/Tea',1,20,34],['Milo',1.30,414],['Iced Lemon Tea',1.40,142],['Water Chestnut',1.40,97],['Bandung',1.40,150]],
               [['Char Siew Pau with Coffee/Tea',2.40,378],['Carrot Cake with Coffee/Tea',2.50,402],['Pancake with Topping',2.80,423],['Toast with Coffee/Tea',2.20,326]]]
    }

canteen14 = {
    'mixed rice': [[['Rice/Porridge',0.80,200],['Fish',1.20,246],['Chicken/Pork',1.00,180],['Vegetable/Egg/Tofu',0.50,65],['Bee Hoon',0.80,294]],
                   []],
    'noodles': [[['Dan Dan Noodle',4.00,498],['Ban Mian',3.50,475],['Braised Beef Noodle',4.50,659],['Wanton Noodle',3.5,409],['Sliced Fish Soup',3.50,349]],
                []],
    'mala': [[['Nasi Lemak',2.80,494],['Mee Goreng',3.00,660],['Mee Rebus',3.00,558],['Mee Siam',3.00,519],['Mee Soto',3.00,432]],
             []],
    'korean': [[['Kimchi Fried Rice',5.00,674],['Ramen',4.50,436],['Bibimbap',5.50,940],['Beef Bulgogi Set',5.50,793],['Korean Rice Cake (6pcs)',3.60,224]],
               []],
    'drinks': [[['Fresh Fruits',0.50,52],['Fruit Juice',2.00,120],['Tea/Coffee',1.20,34],['Milo',1.20,414],['Bandung',1.40,150]],
               [['Coffee/Tea & French Toast',2.20,376],['Coffee/Tea & Cheese Toast',2.20,407],['Coffee/Tea',1.20,34],['Milo',1.30,414]]]
    }

northspine = {
    'macdonalds': [[['FilletOFish Meal',5.50,545],['McWings Meal',6.00,605],['McSpicy Meal',7.50,675],['McChicken Meal',5.50,530],['Chicken McNugget Meal',5.95,585]],
                   [['Hotcakes Meal',5,50,550],['EggMcMuffin Meal',5.00,450],['Breakfast Wrap Meal',7.00,295],['Fillet O Fish Meal',5.50,545]]],
    'starbucks': [[['Java Chip Frappucino',8.90,460],['Caffe Latte',4.90,230],['Soy Chai Tea Latte',8.90,350],['Caramel Macchiato',8.90,250],['Vanilla Latte',7.90,100]],
                  []],
    'chicken rice': [[['Steamed Chicken Rice',3.20,618],['Roasted Chicken Rice',3.20,524],['Chicken Cutlet Rice',3.20,571],['Roasted Pork Rice',3.20,405],['Char Siew Rice',3.20,495]],
                     []],
    'western': [[['Chicken Chop',5.20,522],['Fish & Chips',5.50,848],['Chicken Cutlet ',5.20,579],['Beef Steak',6.20,603],['Grilled Fish',5.50,540]],
                []],
    'noodles': [[['Ban Mian',3.20,475],['Seafood Soup',3.50,306],['U Mian',3.80,475],['Steamed Dumplings (6pcs)',3.60,467],['Tom Yum Ban Mian',5.00,525]],
                []]
    }


compiled_data = {}
compiled_data['Tamarind'] = tamarind
compiled_data['North Spine'] = northspine
compiled_data['Koufu'] = koufu
compiled_data['Canteen 2'] = canteen2
compiled_data['Canteen 14'] = canteen14


canteen = ['Koufu','North Spine', 'Canteen 14', 'Canteen 2', 'Tamarind']




timing = { 'Canteen 2' : {'chicken rice' : [(9,20),(9,20),(9,20)],
                          'noodles': [(9,20),(9,20),(9,20)],
                          'waffles' : [(9,22),0,0],
                          'xiao long bau' : [(9,20),0,0],
                          'indian' : [(9,22),(9,22),0]},
           'Koufu' : {'pasta express' : [(10,20),(10,20),0],
                          'japanese' : [(10,20),0,0],
                          'vegetarian' : [(9,20),0,0],
                          'mixed rice' : [(8,20),(8,20),0],
                          'drinks' : [(8,20),(8,20),(8,20)]},
           'Tamarind' : {'mala' : [(10,20),(10,20),(10,19)],
                         'western' : [(10,20),(10,20),0],
                         'korean' : [(11,20),(11,20),(11,20)],
                         'japanese' : [(11,20),0,0],
                         'drinks' : [(8,21),(8,21),(8,21)]},
           'Canteen 14' : {'mixed rice' : [(9,20),(9,20),(9,20)],
                           'noodles' : [(10,20),(10,20),0],
                           'mala' : [(11,20),(11,20),0],
                           'korean' : [(11,20),(11,20),(11,20)],
                           'drinks' : [(8,22),(8,22),(8,22)]},
           'North Spine' : {'macdonalds' : [(0,24),(0,24),(0,24)],
                           'starbucks' : [(0,24),(0,24),(0,24)],
                           'chicken rice' : [(9,18),0,0],
                           'western' : [(9,18),0,0],
                           'noodles' : [(9,18),0,0]}
           }

waiting = { 'Canteen 2' : {'chicken rice' : [1,2.5],
                          'noodles': [1.5,3],
                          'waffles' : [1,1.5],
                          'xiao long bau' : [2,3],
                          'indian' : [2.5,3.5]},
           'Koufu' : {'pasta express' : [1.5,2.5],
                          'japanese' : [1.5,3],
                          'vegetarian' : [1,1.5],
                          'mixed rice' : [2,3],
                          'drinks' : [1,0.5]},
           'Tamarind' : {'mala' : [4,5],
                         'western' : [2,3],
                         'korean' : [2.5,3.5],
                         'japanese' : [2,3],
                         'drinks' : [1,0.5]},
           'Canteen 14' : {'mixed rice' : [1.5,2.5],
                           'noodles' : [1.5,3],
                           'mala' : [4,5],
                           'korean' : [2,3.5],
                           'drinks' : [1,0.5]},
           'North Spine' : {'macdonalds' : [2,2.5],
                           'starbucks' : [2,2],
                           'chicken rice' : [1,1.5],
                           'western' : [2.5,3],
                           'noodles' : [1,0.5]}
           }







coordinates = {
    'Canteen 2': (435,513),
    'Canteen 14': (290,304),
    'Tamarind': (415,224),
    'North Spine': (79,504),
    'Koufu': (292,766)
    }

red_bus= {
     'Graduate Halls': (461,172),
     'Nanyang Crescent': (388,213),
     'Hall 12 & 13':(220,345),
     'Lee Wee Nam Library':(209,528),
     'School of Biological Sciences': (115,624),
     'School of Comm. Studies': (143,788),
     'Hall 7': (262,880),
     'Innovation Centre': (345,788),
     'Hall 4' : (471,718),
     'Hall 1': (548,634),
     'Canteen 2': (435,483),
     'Hall 8 & 9': (449,367),
     'Hall 11': (502,245)    
     }

red = ['Graduate Hall','Nanyang Crescent','Hall 12 & 13','Lee Wee Nam Library','School of Biological Sciences','School of Comm. Studies','Hall 7','Innovation Centre','Hall 4','Hall 1','Canteen 2','Hall 8 & 9','Hall 11']
   
blue_bus={
     'Opp. Hall 11': (502,245),
     'Opp. Hall 8 & 9': (449,367),
     'Hall 6': (491,536),
     'Hall 4' : (471,718),
     'Opp. Innovation Centre': (345,789),
     'SPMS': (231,798),
     'School of Comm. Studies': (145,780),
     'School of Biological Sciences': (114,654),
     'Opp. Lee Wee Nam Library':(216,513),
     'Hall 16': (204,404),
     'Hall 14 & 15': (285,285),
     'Nanyang Crescent': (396,205)    

     }


blue= ['Opp. Hall 11','Opp. Hall 8 & 9','Hall 6','Hall 4','Opp. Innovation Centre','SPMS','School of Comm. Studies','School of Biological Sciences','Opp. Lee Wee Nam Library','Hall 16','Hall 14 & 15','Nanyang Crescent']  

favourites = []




