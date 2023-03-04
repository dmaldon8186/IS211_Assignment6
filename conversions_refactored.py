def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    temperature_units = ['celsius', 'fahrenheit', 'kelvins']
    distance_units = ['miles', 'yards', 'meters']

    if fromUnit in temperature_units and toUnit in temperature_units:
        if fromUnit == 'celsius' and toUnit == 'kelvins':
            return round(value+273.15,2)
        elif fromUnit == 'celsius' and toUnit == 'fahrenheit':
            return round((9/5)*value+32,2)
        elif fromUnit == 'fahrenheit' and toUnit == 'celsius':
            return round((5/9)*(value-32),2)
        elif fromUnit == 'kelvins' and toUnit == 'celsius':
            return round(value-273.15,2)
        elif fromUnit == 'fahrenheit' and toUnit == 'kelvins':
            return round((5/9)*(value-32)+273.15,2)
        elif fromUnit == 'kelvins' and toUnit == 'fahrenheit':
            return round((9/5)*(value-273.15)+32,2)
    
    if fromUnit in distance_units and toUnit in distance_units:
        if fromUnit == 'miles' and toUnit == 'yards':
            return round(value*1760, 2)
        elif fromUnit == 'miles' and toUnit == 'meters':
            return round(value*1609.344, 2)
        elif fromUnit == 'yards' and toUnit == 'miles':
            return round(value/1760, 2)
        elif fromUnit == 'yards' and toUnit == 'meters':
            return round(value*0.9144, 2)
        elif fromUnit == 'meters' and toUnit == 'miles':
            return round(value/1609.344, 2)
        elif fromUnit == 'meters' and toUnit == 'yards':
            return round(value*1.0936, 2)
    
    elif fromUnit == toUnit:
        return value
        
    else:
        raise Exception(f"Cannot convert from {fromUnit} to {toUnit}")