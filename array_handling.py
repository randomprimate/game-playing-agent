#!/usr/bin/python

"""
Basic array handling
"""


# Retrieve values of empty fields
def values_of_empty_fields(arr):
    return [n for n in arr if n == 0]


# Return index of empty fields
def index_of_empty_fields(arr):
    return [i for i, n in enumerate(arr) if n == 0]


# All 0 elements from left side of current position
def sweep_left(arr):
    left_available = []
    for i, e in enumerate(arr):
        if e == 0:
            left_available.append(i)
        elif e == 1:
            left_available = []
    return left_available


# All 0 elements from right side of current position
def sweep_right(arr, ix):
    right_available = []
    for i, e in enumerate(arr):
        if e == 0:
            right_available.append(i + ix)
        elif e == 1 and i != ix:
            break
    return right_available


# All horizontal 0 elements
def sweep_horizontal(arr, cur):
    available_hor = []
    pos = cur[0]

    arr_lft = arr[0:pos+1]
    arr_rgt = arr[pos:]
    available_hor.extend(sweep_left(arr_lft))
    available_hor.extend(sweep_right(arr_rgt, pos))

    return available_hor

# Get all available elements, remove blocked and current
# def get_available(arr):
#    available = []
#    hor = sweep_horizontal(arr)
#    available.extend(hor) # , vert, diag)

#    return available


# Base array init
a = []
a = [0, 1, 0, 0, 1, 0, 2, 0, 0, 1, 0, 1, 0]

"""
Basic matrix handling
"""


# Human readable  matrix
def render_matrix(r, c, m):
    print('')
    for i in range(r):
        for ix in range(c):
            print(' ' + str(m[ix][i]), end=' ')
        print('')
    print('')


# Create matrix method
def create_matrix(r, c, e):
    for i in range(c):
        e[i] = [0] * r
    return e


# Retrieve values of empty fields
def values_empty_matrix_elements(c, m):
    em = []
    for c in m:
        em.append([n for n in c if n == 0])
    return em


# Return coordinates from nested lists
def nested_lists_to_coords(lst):
    em = []
    for i, n in enumerate(lst):
        em.extend([(i, nn) for nn in n])
    return em


# Get row from current position
def current_pos_row(m, cur):
    row = []
    for c in m:
        row.append(c[cur[1]])
    return row


# Retrieve available horizontal moves
def get_av_hor(c, m, cur):
    coords = []
    hor_av = sweep_horizontal(current_pos_row(m, cur), cur)
    for e in hor_av:
        coords.append((e, cur[1]))
    return coords


# Return index of available fields
def index_available_matrix_elements(c, m, cur):
    em = []
    for c in m:
        em.append([i for i, n in enumerate(c) if n == 0])
    em = nested_lists_to_coords(em)
    for e in em:
        if e[1] == cur[1] and e not in get_av_hor(c, m, cur):
            em.remove(e)
    return em


"""
# Debug
rows = 3
columns = 6
elements = [0] * columns
current_pos = (1, 1)
m = create_matrix(rows, columns, elements)
m[0][0] = 1
m[1][1] = 1
m[2][1] = 1
render_matrix(rows, columns, m)
available = index_available_matrix_elements(columns, m, current_pos)
import code; code.interact(local=dict(globals(), **locals()))
"""
