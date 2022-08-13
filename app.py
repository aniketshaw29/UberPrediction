import pickle

model = pickle.load(open('uber_weeklyRide_prediction_model.pkl','rb'))  #rb = read binary
print(int(model.predict([[30,1710000,9630,80]])))