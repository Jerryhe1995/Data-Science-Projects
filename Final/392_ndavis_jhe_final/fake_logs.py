#This is a simulation of the users' dining data which is created by Noah Davis.

from sqlalchemy import create_engine
from sqlalchemy import text
from random import randint
import datetime
import random

# Define our DB
sr28_engine = create_engine('mysql://django:djangotest@127.0.0.1:8889/sr28')

# Create a connection to the DB
sr28 = sr28_engine.connect()

# Populate test diets

## DIET "A"

bfastA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Energ_Kcal` > 300 " \
      "AND `Shrt_Desc` LIKE :like_val " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val = "%CEREAL%")

bfast_drinkA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val = "%beverages,coffee%")

lunchA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` > 300 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "%subway%", like_val2 = "%burger%")

lunch_drinkA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val1 " \
      " AND `Energ_Kcal` > 100 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "%beverages,carb%")

dinnerA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` > 450 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "%steak%", like_val2 = "%pork%")

dinner_drinkA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` < 150 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "BEVERAGES%JUICE%", like_val2 = "BEVERAGES%")

snackA = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` < 200 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "SNACKS%", like_val2 = "doesnotexist")


## DIET "B"

bfastB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Energ_Kcal` > 300 " \
      "AND `Shrt_Desc` LIKE :like_val OR `Shrt_Desc` LIKE :like_val2 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val = "%PANCAKE%", like_val2 = "%WAFFLE%")

bfast_drinkB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val = "beverages%MILK%")

lunchB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 OR `Shrt_Desc` LIKE :like_val3 " \
      " AND `Energ_Kcal` > 200 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "MCDONALD%MAC%", like_val2 = "BURGER KING%WH%", like_val3 = "MCDONALD%SNDWCH%")


lunch_drinkB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val1 " \
      " AND `Energ_Kcal` > 200 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "%beverages,carb%")

dinnerB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` > 300 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "%spaghettios%", like_val2 = "%lucky charms%")

dinner_drinkB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` < 150 " \
      "ORDER BY RAND() " \
      "LIMIT 10"), like_val1 = "BEVERAGES%prot%", like_val2 = "BEVERAGES%egg%")

snackB = sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      "FROM ABBREV " \
      "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      " AND `Energ_Kcal` < 900 " \
      "ORDER BY RAND() " \
      "LIMIT 10"),  like_val1 = "snacks%popcorn%", like_val2 = "%reese%")

      #
      # sr28.execute(text("SELECT `Shrt_Desc` as name, `Energ_Kcal` as cals, `Protein_(g)` as protein, `Carbohydrt_(g)` as carbs, `Lipid_Tot_(g)` as fat " \
      # "FROM ABBREV " \
      # "WHERE `Shrt_Desc` LIKE :like_val1 OR `Shrt_Desc` LIKE :like_val2 " \
      # " AND `Energ_Kcal` < 300 " \
      # "ORDER BY RAND() " \
      # "LIMIT 10"), like_val1 = "SNACKS%popcorn%", like_val2 = "%twiz%")

diet_a = {}
diet_b = {}


# Initialize dictionaries containing generated meals

diet_a['lunch_drink'] = lunch_drinkA.fetchall()
diet_a['dinner_drink'] = dinner_drinkA.fetchall()
diet_a['snack'] = snackA.fetchall()
diet_a['lunch'] = lunchA.fetchall()
diet_a['dinner'] = dinnerA.fetchall()
diet_a['breakfast'] = bfastA.fetchall()
diet_a['breakfast_drink'] = bfast_drinkA.fetchall()

diet_b['lunch_drink'] = lunch_drinkB.fetchall()
diet_b['dinner_drink'] = dinner_drinkB.fetchall()
diet_b['snack'] = snackB.fetchall()
diet_b['lunch'] = lunchB.fetchall()
diet_b['dinner'] = dinnerB.fetchall()
diet_b['breakfast'] = bfastB.fetchall()
diet_b['breakfast_drink'] = bfast_drinkB.fetchall()

# # print("A")
# for a in diet_a:
#       print(len(diet_a[a].fetchall()))
#
# print("B")
# for b in diet_b:
#       print(len(diet_b[b].fetchall()))

sr28.close()

# # Print Values
# for row in snackB:
#     print("food:", row['name'])

# Number of fake users
user_n = 100

# Split diet in half, no particular reason
users_a = user_n / 2
users_b = user_n / 2

# Number of days to log
days_n = 30


# functions for randomizing weight
def create_weight():
      weight = randint(150,250)
      return weight

def decrease_weight(weight_in):

      # Decrease weight by 1 to 10
      new_weight = weight_in - randint(1,10)

      return new_weight

def increase_weight(weight_in):

      # Increase weight by 1 to 10
      new_weight = weight_in + randint(1,10)

      return new_weight

# Engine for analytics
analytics_engine = create_engine('mysql://django:djangotest@127.0.0.1:8889/a_test')

# Connection for analytics test
analytics = analytics_engine.connect()


for user in range(0,int(user_n/2)):
    user_id = user+1
    weight = create_weight()

    # Fake log dates for one month beginning today
    log_date = datetime.date.today()

    # Log 9000 meals
    for log in range(0,days_n):
        log_date += datetime.timedelta(days=1)
        breakfast = diet_b['breakfast'][randint(0,9)]
        breakfast_drink = diet_b['breakfast_drink'][randint(0,9)]
        lunch = diet_b['lunch'][randint(0,9)]
        lunch_drink = diet_b['lunch_drink'][randint(0,9)]
        dinner = diet_a['dinner'][randint(0,9)]
        dinner_drink = diet_b['dinner_drink'][randint(0,9)]
        snack = diet_b['snack'][randint(0,9)]
        weight = random.choice([increase_weight(weight),decrease_weight(weight)])
        # just for fun


        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='breakfast', log_date1=log_date, food1=breakfast['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=breakfast['protein'], fat1 = breakfast['fat'], cals1 = breakfast['cals'], carbs1 = breakfast['carbs'])

        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='dinner', log_date1=log_date, food1=dinner['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=dinner['protein'], fat1 = dinner['fat'], cals1 = dinner['cals'], carbs1 = dinner['carbs'])

        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='breakfast_drink', log_date1=log_date, food1=breakfast_drink['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=breakfast_drink['protein'], fat1 = breakfast_drink['fat'], cals1 = breakfast_drink['cals'], carbs1 = breakfast_drink['carbs'])

        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='lunch', log_date1=log_date, food1=lunch['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=lunch['protein'], fat1 = lunch['fat'], cals1 = lunch['cals'], carbs1 = lunch['carbs'])

        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='lunch_drink', log_date1=log_date, food1=lunch_drink['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=lunch_drink['protein'], fat1 = lunch_drink['fat'], cals1 = lunch_drink['cals'], carbs1 = lunch_drink['carbs'])

        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='dinner_drink', log_date1=log_date, food1=dinner_drink['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=dinner_drink['protein'], fat1 = dinner_drink['fat'], cals1 = dinner_drink['cals'], carbs1 = dinner_drink['carbs'])

        analytics.execute(text("INSERT INTO test_meal(servings, type, log_date, food, user_id, mood, weight, protein, cals, fat, carbs) " \
                                     "VALUES(:servings1, :type1, :log_date1, :food1, :user_id1, :mood1, :weight1, :protein1, :cals1, :fat1, :carbs1)"),
                                    servings1=random.uniform(1,3), type1='snack', log_date1=log_date, food1=snack['name'], user_id1=user_id, mood1=random.choice(['grumpy','sleepy','agitated','ambivalent','motivated','amorous']), weight1=weight, protein1=snack['protein'], fat1 = snack['fat'], cals1 = snack['cals'], carbs1 = snack['carbs'])

        #print(lunch['protein'])







