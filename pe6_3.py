lengte = input('Wat is je lengte in centimeters?')
def lang_genoeg(attractie):
    if int(attractie) >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')
    return attractie

lang_genoeg(lengte)