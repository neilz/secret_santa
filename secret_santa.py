import readline
import os
import yaml
import sys
from pairer import assign_santas
from messenger import notify_santas, test_sms

def print_assignments(assignments):
    for santa in assignments.keys():
        print "%s (%s) has been assigned %s" % (santa, assignments[santa]["phone"], assignments[santa]["assignee"])

def get_santas_conf():
    if not os.path.isfile('./santas.yml'):
        print "ERROR: Config file santas.yml does not exist!"
        exit(1)
    data = None
    with open("./santas.yml", 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print "ERROR: Failed to load config file santas.yml"
            print(exc)
            exit(1)

    santas = data['santas'].keys()
    for key, value in data['santas'].iteritems():
        for v in value['blacklist']:
            if not v in santas:
                print "ERROR: Santa %s has unknown blacklisted assignee %s" % (key, v)
                exit(1)

    return data['santas']

def get_twilio_conf():
    if not os.path.isfile('./twilio.yml'):
        print "ERROR: Config file twilio.yml does not exist!"
        exit(1)
    data = None
    with open("./twilio.yml", 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print "ERROR: Failed to load config file twilio.yml"
            print(exc)
            exit(1)

    return data['twilio']



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Please specify an available action: run, test_run, test_sms"
        exit(1)

    # load santas config
    santas_conf = get_santas_conf()
    twilio_conf = get_twilio_conf()

    # get assignments
    assignments = assign_santas(santas_conf)

    if sys.argv[1] == "run":
        print "Running Secret Santa..."
        notify_santas(assignments)
    elif sys.argv[1] == "test_run":
        print "Running Secret Santa test..."
        print_assignments(assignments)
    elif sys.argv[1] == "test_sms":
        print "Sending test SMS message to %s ..." % twilio_conf['test_number']
        test_sms(twilio_conf)
    else:
        print "Invalid action: " + sys.argv[1]
        print "Please specify an available action: run, test_run, test_sms"
