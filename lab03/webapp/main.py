from flask import Flask, render_template
# from flask import request
# from surprise import Dataset, evaluate
# from surprise import KNNBasic
# from surprise.model_selection import cross_validate
# from collections import defaultdict
# import os, io

app = Flask(__name__)

top_recommendations = []

@app.route('/', methods=['GET'])
def main():
  return "OK"
  # return render_template('index.html')

# @app.route('/', methods=['POST'])
# def get_recommendation():
#   uid = request.form['uid']
#   if top_recommendations == []:
#     run_collaborative_filtering()
#   ids_to_names = convert_item_ids_to_names()
#   movies = []
#   for mid, rating in top_recommendations[uid]:
#     movies.append(ids_to_names[mid])

#   neighbors = knn.get_neighbors(knn.trainset.to_inner_iid(uid), k=3)
#   return render_template('index.html', movies=movies, similar_users=neighbors)

# def get_top_recommendations(predictions, N = 5):
#   top_recs = defaultdict(list)
#   for uid, iid, true_r, est, _ in predictions:
#     top_recs[uid].append((iid, est))
    
#   for uid, user_ratings in top_recs.items():
#     user_ratings.sort(key = lambda x: x[1], reverse = True)
#     top_recs[uid] = user_ratings[:N]
    
#   return top_recs

# def convert_item_ids_to_names():
#   file_name = (os.path.expanduser('~') + '/.surprise_data/ml-100k/ml-100k/u.item')
#   rid_to_name = {}
#   with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
#     for line in f:
#       line = line.split('|')
#       rid_to_name[line[0]] = line[1]
#   return rid_to_name

# def run_collaborative_filtering():
#   global top_recommendations
#   global knn
#   data = Dataset.load_builtin("ml-100k")
#   training_set = data.build_full_trainset()
#   sim_options = {
#     'name': 'pearson_baseline',
#     'user_based': True
#   }
#   knn = KNNBasic(sim_options=sim_options)
#   knn.fit(training_set)
#   test_set = training_set.build_anti_testset()
#   predictions = knn.test(test_set)
#   top_recommendations = get_top_recommendations(predictions)

#   return 'OK'

if __name__ == "__main__":
  app.run()