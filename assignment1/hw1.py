#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    
    histogram = [0] * 24
    times = [row[1] for row in airplane_data[1:] if row[1] != '']

    for time in times:
        hour = time.split(':')[0]
        if hour.isdigit() and int(hour) < len(histogram):
            histogram[int(hour)] += 1

    return histogram

def weigh_pokemons(filename, weight):
    with open(filename) as f:
        data = json.load(f)

    result = []

    for pokemon in data['pokemon']:
        if float(pokemon['weight'].split(' ')[0]) == weight:
            result.append(pokemon['name'])
    
    return result

def single_type_candy_count(filename):
    with open(filename) as f:
        data = json.load(f)

    candy_count = 0

    for pokemon in data['pokemon']:
        if len(pokemon['type']) == 1:
            candy_key = 'candy_count'

            if candy_key in pokemon.keys():
                candy_count += pokemon[candy_key]
    
    return candy_count

def reflections_and_projections(points):
    newPoints = []

    for point in points:

        # Reflect over the line y=1
        newPoint = [point[0], 2-point[1]]

        # Rotate the point π/2 radians around the origin
        rotationAngle = np.pi / 2

        newPoint = [
            newPoint[0] * np.cos(rotationAngle) - newPoint[1] * np.sin(rotationAngle),
            newPoint[0] * np.sin(rotationAngle) + newPoint[1] * np.cos(rotationAngle)
        ]

        # Project the point onto the line y = 3x
        lineProjScalar = 3
        matrixScalar = 1 / (lineProjScalar**2 + 1)

        newPoint = [
            round(matrixScalar * (newPoint[0] + newPoint[1] * lineProjScalar), 2),
            round(matrixScalar * (newPoint[0] * lineProjScalar + newPoint[1] * (lineProjScalar**2)), 2)
        ]

        newPoints.append(newPoint)

    return np.array(newPoints)

def normalize(image):
    return (255 / (image.max() - image.min())) * (image - image.min())

def sigmoid_normalize(image, a):
    return 255 * ((np.e ** (-1 * (a ** -1) * (image - 128)) + 1) ** -1)

print(histogram_times('airplane_crashes.csv'))