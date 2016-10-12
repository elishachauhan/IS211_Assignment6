#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for Assignment 6"""

def convertCelciusToKelvin(celcius):
    return round(celcius+273.15, 10)


def convertFahrenheitToCelcius(fahrenheit):
    return round(((fahrenheit-32)*(5.0/9.0)), 10)


def convertFahrenheitToKelvin(fahrenheit):
    return round(((fahrenheit-32)*(5.0/9.0))+273.15, 10)


def convertKelvinToCelcius(kelvin):
    return round(kelvin-273.15, 10)


def convertKelvinToFahrenheit(kelvin):
    return round((((kelvin-273.15)* (9.0/5.0))+32), 10)




