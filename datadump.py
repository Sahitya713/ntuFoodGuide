import pickle
from data import *


with open('datadump.pickle','wb') as obj:
    pickle.dump(canteen2, obj)
    pickle.dump(koufu, obj)
    pickle.dump(tamarind, obj)
    pickle.dump(canteen14, obj)
    pickle.dump(northspine, obj)
    pickle.dump(compiled_data, obj)
    pickle.dump(canteen, obj)
    pickle.dump(timing, obj)
    pickle.dump(waiting, obj)
    pickle.dump(coordinates, obj)
    pickle.dump(red_bus, obj)
    pickle.dump(red, obj)
    pickle.dump(blue_bus, obj)
    pickle.dump(blue, obj)
    pickle.dump(favourites, obj)
    


