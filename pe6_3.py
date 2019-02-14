lengte = input('Wat is je lengte in centimeters?')
def L(attractie):
    if int(attractie) >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')
    return attractie

L(lengte)