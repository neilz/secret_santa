from random import shuffle
from copy import copy

def assign_santas(santas_conf):
    assignments = copy(santas_conf)
    santas = assignments.keys()
    for s in santas:
        assignments[s]['assignee'] = None
    assignments = assign(assignments)
    return assignments


def is_valid(assignments):
    for (key, value) in assignments.iteritems():
        if value['assignee'] in value['blacklist']:
            return False
        elif key == value['assignee']:
            return False
    return True


def is_complete(assignments):
    for (key, value) in assignments.iteritems():
        if not value['assignee'] or value['assignee'] in value['blacklist']:
            return False
    return True


def get_unassigned(assignments):
    santas = assignments.keys()
    assigned = []
    unassigned = []
    for v in assignments.values():
        if v['assignee']:
            assigned.append( v['assignee'] )

    for s in santas:
        if not s in assigned:
            unassigned.append(s)
    return unassigned


def assign(assignments, last_assigned=None):
    if is_complete(assignments):
        return assignments

    for (key, value) in assignments.iteritems():
        santa = value
        if value['assignee']:
            continue
        unassigned = get_unassigned(assignments)
        shuffle(unassigned)
        for u in unassigned:
            assign2 = copy(assignments)
            assign2[key]['assignee'] = u
            if is_valid(assign2):
                return assign(assign2, key)

    # start over
    for a in assignments.keys():
        assignments[a]['assignee'] = None
    return assign(assignments, last_assigned)
