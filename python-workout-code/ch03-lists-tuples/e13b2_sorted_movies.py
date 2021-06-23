#!/usr/bin/env python3
"""Solution to chapter 3, exercise 13, beyond 2: sorted_movies"""


import operator
from collections import namedtuple

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}


def sort_movies():
    sort_by = input("Enter sort field (name/length/director): ").strip()

    if sort_by in FIELDS:

        output = []
        template = '{0:30} {1:3} {2:20}'
        for one_movie in sorted(MOVIES, key=operator.itemgetter(FIELDS[sort_by])):
            output.append(template.format(*one_movie))
        return output

    print(f'No such field {sort_by}')
