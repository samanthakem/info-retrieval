from surprise import Dataset, evaluate
from surprise import KNNBasic
from surprise.model_selection import cross_validate
from collections import defaultdict
import os, io

def get_top_recommendations(predictions, N = 5):
  top_recs = defaultdict(list)
  for uid, iid, true_r, est, _ in predictions:
    top_recs[uid].append((iid, est))
    
  for uid, user_ratings in top_recs.items():
    user_ratings.sort(key = lambda x: x[1], reverse = True)
    top_recs[uid] = user_ratings[:N]
    
  return top_recs

def convert_item_ids_to_names():
  file_name = (os.path.expanduser('~') + '/.surprise_data/ml-100k/ml-100k/u.item')
  rid_to_name = {}
  with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
    for line in f:
      line = line.split('|')
      rid_to_name[line[0]] = line[1]
  return rid_to_name

data = Dataset.load_builtin("ml-100k")
training_set = data.build_full_trainset()

sim_options = {
  'name': 'pearson_baseline',
  'user_based': True
}

knn = KNNBasic(sim_options=sim_options)

# cross_validate(knn, data, measures=['RMSE'], cv=10, verbose=False)

knn.fit(training_set)

test_set = training_set.build_anti_testset()
predictions = knn.test(test_set)

# top_recommendations = get_top_recommendations(predictions)

# print (top_recommendations)
# ids_to_names = convert_item_ids_to_names()

# uid = str(input("Digite um ID: "))

# for mid, rating in top_recommendations[uid]:
#   print(ids_to_names[mid])

# r = knn.trainset.to_inner_iid(uid)

# neighbors = knn.get_neighbors(r, k=3)

# print(neighbors)