#!/usr/bin/python3
def square_matrix_simple(mat=[]):
    new_list = []
    if len(mat) == 0:
        return new_list

    new_list = [[i*i for i in j] for j in mat]
    return new_list
