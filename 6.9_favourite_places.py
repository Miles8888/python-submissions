favorite_places = {
    'jack': ('montreall', 'seattle'),
    'mark': ('detroit', 'teluride'),
    'michael': ('paris', 'london'),
}

for name, places in favorite_places.items():
    print("{}'s favourite places are:".format(name.title()))
    for place in places:
        print("  {}".format(place.title()))