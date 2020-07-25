import pandas as pd
import numpy as np

import pymongo as pm
client = pm.MongoClient('localhost', 27017)
db = client['psych']

question = db['ANDTHETRUTHCOMESOUT']
question.insert_one({"quest":"if USER_NAME could only speak one word today, what would he/she say"})
question.insert_one({"quest":"where whould USER_NAME not mind waiting"})
question.insert_one({"quest":"would USER_NAME rather live permanently in your house or with dogs"})


            
