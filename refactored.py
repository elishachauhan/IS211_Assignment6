#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for refactored conversions."""

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    temp = ["celsius", "fahrenheit", "kelvin"]
    anyToCelsius = ["value", "(value-32)*5/9", "value-273.15"]
    celsiusToAny = ["value", "(value*9/5)+32", "value+273.15"]
    dist = ["meters", "miles", "yards"]
    anyTOMeters = ["value", "value/0.00062137", "value/1.0936"]
    meterToAny = ["value", "value*0.00062137", "value*1.0936"]

    if fromUnit.lower() in temp:
        if not(toUnit.lower() in temp):
            raise ConversionNotPossible
        else:
            try:
                value = float(value)
            except:
                raise ConversionNotPossible
            else:
                value = eval(anyToCelsius[temp.index(fromUnit.lower())])
                value = eval(celsiusToAny[temp.index(toUnit.lower())])
                return round(value, 2)

    elif fromUnit.lower() in dist:
        if not(toUnit.lower() in dist):
            raise ConversionNotPossible
        else:
            try:
                value = float(value)
            except:
                raise ConversionNotPossible
            else:
                value = eval(anyTOMeters[dist.index(fromUnit.lower())])
                value = eval(meterToAny[dist.index(toUnit.lower())])
                return round(value, 2)
    else:
        raise ConversionNotPossible
