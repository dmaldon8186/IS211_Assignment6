import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius
from conversions import convertKelvinToFahrenheit
from conversions_refactored import convert

class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        result = convertCelsiusToKelvin(300)
        expected_result = 573.15
        self.assertEqual (result, expected_result)

    def test_convertCelsiusToFahrenheit(self):
        result = convertCelsiusToFahrenheit(300)
        expected_result = 572
        self.assertEqual (result, expected_result)

    def test_convertFahrenheitToCelsius(self):
        result = convertFahrenheitToCelsius(300)
        expected_result = 148.89
        self.assertEqual (result, expected_result)

    def test_convertFahrenheitToKelvin(self):
        result = convertFahrenheitToKelvin(300)
        expected_result = 422.04
        self.assertEqual (result, expected_result)

    def test_convertKelvinToCelsius(self):
        result = convertKelvinToCelsius(300)
        expected_result = 26.85
        self.assertEqual (result, expected_result)

    def test_convertKelvinToFahrenheit(self):
        result = convertKelvinToFahrenheit(300)
        expected_result = 80.33
        self.assertEqual (result, expected_result)
    
    def test_convert_CelsiusToKelvin(self):
        result = convert("celsius", "kelvins", 300)
        expected_result = 573.15
        self.assertEqual (result, expected_result)

    def test_convert_CelsiusToFahrenheit(self):
        result = convert("celsius", "fahrenheit", 300)
        expected_result = 572
        self.assertEqual (result, expected_result)

    def test_convert_FahrenheitToCelsius(self):
        result = convert("fahrenheit", "celsius", 300)
        expected_result = 148.89
        self.assertEqual (result, expected_result)

    def test_convert_FahrenheitToKelvin(self):
        result = convert("fahrenheit", "kelvins", 300)
        expected_result = 422.04
        self.assertEqual (result, expected_result)

    def test_convert_KelvinToCelsius(self):
        result = convert("kelvins", "celsius", 300)
        expected_result = 26.85
        self.assertEqual (result, expected_result)

    def test_convert_KelvinToFahrenheit(self):
        result = convert("kelvins", "fahrenheit", 300)
        expected_result = 80.33
        self.assertEqual (result, expected_result)

    def test_convert_MilesToYards(self):
        result = convert("miles", "yards", 100)
        expected_result = 176000
        self.assertEqual (result, expected_result)

    def test_convert_MilesToMeters(self):
        result = convert("miles", "meters", 100)
        expected_result = 160934.4
        self.assertEqual (result, expected_result)

    def test_convert_YardsToMiles(self):
        result = convert("yards", "miles", 100)
        expected_result = 0.06
        self.assertEqual (result, expected_result)

    def test_convert_YardsToMeters(self):
        result = convert("yards", "meters", 100)
        expected_result = 91.44
        self.assertEqual (result, expected_result)

    def test_convert_MetersToMiles(self):
        result = convert("meters", "miles", 100)
        expected_result = 0.06
        self.assertEqual (result, expected_result)

    def test_convert_MetersToYards(self):
        result = convert("meters", "yards", 100)
        expected_result = 109.36
        self.assertEqual (result, expected_result)
        
if __name__ == '__main__':
    unittest.main()