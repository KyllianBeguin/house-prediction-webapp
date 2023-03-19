def predict(surface : float, rooms : int, town : str):

    town_mapper = {
        "high" : {
            "towns" : ["paris", "marseille", "lyon"],
            "index_ref" : 10
        },
        "medium" : {
            "towns" : ["rennes", "caen"],
            "index_ref" : 6
        },
        "low" : {
            "towns" : ["amiens", "tourcoing"],
            "index_ref" : 3
        }
    }

    for key, val in town_mapper.items():
        if town in val["towns"]:
            use_index = val["index_ref"]
            print(use_index)
            price_house_predicted = (surface/rooms)*(use_index)
            return price_house_predicted