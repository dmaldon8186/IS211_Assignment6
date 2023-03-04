
def convertCelsiusToKelvin(celsius):
    kelvins = celsius+273.15
    
    return round(kelvins,2)


def convertCelsiusToFahrenheit(celsius):
    fahrenheit = (9/5)*celsius+32
    
    return round(fahrenheit,2)


def convertFahrenheitToCelsius(fahrenheit):
    celsius = (5/9)*(fahrenheit-32)

    return round(celsius,2)


def convertFahrenheitToKelvin(fahrenheit):
    kelvins = (5/9)*(fahrenheit-32)+273.15

    return round(kelvins,2)


def convertKelvinToCelsius(kelvins):
    celsius = kelvins-273.15

    return round(celsius,2)


def convertKelvinToFahrenheit(kelvins):
    fahrenheit = (9/5)*(kelvins-273.15)+32

    return round(fahrenheit,2)
