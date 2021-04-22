import pickle
from collections import defaultdict

def recommendation_nickname(user):
    """
    Return the top-N recommendation for each user from a set of predictions.
    """
    user_games = []
    reco = ", "
    predictions = un_pickle_model()
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
      
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:5]
    
    
    for uid, user_ratings in top_n.items():
        if uid == user:
            user_games.append((uid, [iid for (iid, _) in user_ratings]))
    return (reco.join(user_games[0][1]))
   
    
            
            
    




def get_prediction(user_id):
    """ Given a list of feature values, return a prediction made by the model"""
    
    loaded_model = un_pickle_model()
    
    # Model is expecting a list of lists, and returns a list of predictions
    predictions = loaded_model.predict(user_id)
    # We are only making a single prediction, so return the 0-th value
    return predictions[0]

def un_pickle_model():
    """ Load the model from the .pkl file """
    with open("src/models/myfile.pickle", "rb") as model_file:
        loaded_model = pickle.load(model_file)
    return loaded_model

