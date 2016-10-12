#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for Tests"""

import conversions
import unittest

class KnownValues(unittest.TestCase):
    knownValues = ( (0.0, 273.15, 32.0),
                    (300.0, 573.15, 572.0),
                    (25.49, 298.64, 77.882),
                    (200, 473.15, 392),
                    (150.00, 423.15, 302.00),
                    (-220.00, 53.15, -364.00),
                    (-40.0, 233.15, -40.0),
                    )

    def testConvertCelciusToKelvin(self):
        print "\nNow testing convertCelciusToKelvin() function:"

        for i in range(0,len(self.knownValues)):
            result = conversions.convertCelciusToKelvin(self.knownValues[i][0]) 
            kelvin = self.knownValues[i][1]
            self.assertEqual(kelvin, result) 
            print "   testing celcius = %f; %f = %f; Passed" % (self.knownValues[i][0], kelvin, result)

    def testConvertCelciusToFahrenheit(self):
        print "\nNow testing convertCelciusToFahrenheit function:"

        for i in range(0,len(self.knownValues)):
            result = conversions.convertCelciusToFahrenheit(self.knownValues[i][0]) 
            fahrenheit = self.knownValues[i][2]
            self.assertEqual(fahrenheit, result) 
            print "   testing celcius = %f; %f = %f; Passed" % (self.knownValues[i][0], fahrenheit, result)

    def testConvertFahrenheitToCelcius(self):
        print "\nNow testing convertFahrenheitToCelcius function:"

        for i in range(0,len(self.knownValues)):
            result = conversions.convertFahrenheitToCelcius(self.knownValues[i][2]) 
            celcius = self.knownValues[i][0]
            self.assertEqual(celcius, result) 
            print "   testing fahrenheit = %f; %f = %f; Passed" % (self.knownValues[i][2], celcius, result)

    def testConvertFahrenheitToKelvin(self):
        print "\nNow testing convertFahrenheitToKelvin function:"

        for i in range(0,len(self.knownValues)):
            result = conversions.convertFahrenheitToKelvin(self.knownValues[i][2]) 
            kelvin = self.knownValues[i][1]
            self.assertEqual(kelvin, result) 
            print "   testing fahrenheit = %f; %f = %f; Passed" % (self.knownValues[i][2], kelvin, result)

    def testConvertKelvinToCelcius(self):
        print "\nNow testing convertKelvinToCelcius function:"

        for i in range(0,len(self.knownValues)):
            result = conversions.convertKelvinToCelcius(self.knownValues[i][1]) 
            celcius = self.knownValues[i][0]
            self.assertEqual(celcius, result) 
            print "   testing kelvin = %f; %f = %f; Passed" % (self.knownValues[i][1], celcius, result)

    def testConvertKelvinToFahrenheit(self):
        print "\nNow testing convertKelvinToFahrenheit function:"

        for i in range(0,len(self.knownValues)):
            result = conversions.convertKelvinToFahrenheit(self.knownValues[i][1]) 
            fahrenheit = self.knownValues[i][2]
            self.assertEqual(fahrenheit, result) 
            print "   testing kelvin = %f; %f = %f; Passed" % (self.knownValues[i][1], fahrenheit, result)



if __name__ == "__main__":
    unittest.main()
