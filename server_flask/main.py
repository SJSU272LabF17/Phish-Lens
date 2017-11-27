# import sys
import os
import shutil
import time
import traceback
import urllib

from flask import Flask, request, jsonify
import pandas as pd
# from sklearn.externals import joblib

# -----------------------------------------------------------
from sklearn import tree
from sklearn.metrics import accuracy_score
from urlparse import urlparse
from pyfav import get_favicon_url
import numpy as np
import json
import re
import requests

from rules import rule111_ip, rule112_length, rule113_tinyurl, rule114_atsymbol, rule115_doubleslash, rule116_prefix, rule117_subdomain, rule1110_favicon, rule1111_non_standard_port, rule1112_https


def load_data():
    """
    This helper function loads the dataset saved in the CSV file
    and returns 4 numpy arrays containing the training set inputs
    and labels, and the testing set inputs and labels.
    """

    # Load the training data from the CSV file
    training_data = np.genfromtxt('data/dataset.csv', delimiter=',', dtype=np.int32)

    """
    Each row of the CSV file contains the features collected on a website
    as well as whether that website was used for phishing or not.
    We now separate the inputs (features collected on each website)
    from the output labels (whether the website is used for phishing).
    """

    # Extract the inputs from the training data array (all columns but the last one)
    inputs = training_data[:,:-1]
    print "**** inputs ****"
    print inputs
    print len(inputs)

    # Extract the outputs from the training data array (last column)
    outputs = training_data[:, -1]
    print "**** outputs ****"
    print outputs
    print len(outputs)

    # Separate the training (first 2,000 websites) and testing data (last 456)
    training_inputs = inputs[:2000]
    training_outputs = outputs[:2000]
    testing_inputs = inputs[2000:]
    testing_outputs = outputs[2000:]

    # Return the four arrays
    return training_inputs, training_outputs, testing_inputs, testing_outputs

def load_custom_data():
    """
    This helper function loads the dataset saved in the CSV file
    and returns 4 numpy arrays containing the training set inputs
    and labels, and the testing set inputs and labels.
    """

    # Load the training data from the CSV file
    training_data = np.genfromtxt('data/custom_dataset.csv', delimiter=',', dtype=np.int32)

    """
    Each row of the CSV file contains the features collected on a website
    as well as whether that website was used for phishing or not.
    We now separate the inputs (features collected on each website)
    from the output labels (whether the website is used for phishing).
    """

    # Extract the inputs from the training data array (all columns but the last one)
    inputs = training_data[:,:-1]
    print "**** inputs ****"
    print inputs
    print len(inputs)

    # Extract the outputs from the training data array (last column)
    outputs = training_data[:, -1]
    print "**** outputs ****"
    print outputs
    print len(outputs)

    # Separate the training (first 2,000 websites) and testing data (last 456)
    custom_training_inputs = inputs[:900]
    custom_training_outputs = outputs[:900]
    custom_testing_inputs = inputs[900:]
    custom_testing_outputs = outputs[900:]

    # Return the four arrays
    return custom_training_inputs, custom_training_outputs, custom_testing_inputs, custom_testing_outputs


def check_phishtank(url):
    myjson = {
        "url": url,
        "format": "json",
        "app_key": "71eb7c67c1f4f2088cf27e3d75216f49edccffc5712c6bde5a4a3fee5e6055f8"
        }
    print "--------------myjson"
    print myjson

    url = 'http://checkurl.phishtank.com/checkurl/'
    headers = {"content-type":"application/x-www-form-urlencoded"}
    res = requests.post(url, headers=headers, data=myjson)
    print 'response from server:',res.text
    
    resjson = res.json()
    print resjson
    print "-----"
    print resjson['results']

    in_database = False
    if 'in_database' in resjson['results']:
        in_database = resjson['results']['in_database']

    valid = False
    if 'valid' in resjson['results']:
        valid = resjson['results']['valid']

    verified = False
    if 'verified' in resjson['results']:
        verified = resjson['results']['verified']

    print "-----resjson['results']['in_database']"
    print in_database
    print "-----resjson['results']['valid']"
    print valid
    
    # finalVerdict = (in_database and valid)
    # print 'finalVerdict ='
    # print finalVerdict

    # return jsonify({ 'isExisted': finalVerdict })
    return { 'in_database': in_database, 'valid': valid, 'verified': verified }


# -----------------------------------------------------------

app = Flask(__name__)

# train_inputs, train_outputs, test_inputs, test_outputs = ''
train_inputs = ''
train_outputs = ''
test_inputs = ''
test_outputs = ''

custom_train_inputs = ''
custom_train_outputs = ''
custom_test_inputs = ''
custom_test_outputs = ''



@app.route('/test', methods=['POST'])
def test():
    myjson = {
        "url": "https://www.facebook.com",
        "format": "json",
        "app_key": "71eb7c67c1f4f2088cf27e3d75216f49edccffc5712c6bde5a4a3fee5e6055f8"
        }
    print "--------------myjson"
    print myjson

    print "--------------request"
    print request.json

    url = 'http://checkurl.phishtank.com/checkurl/'
    headers = {"content-type":"application/x-www-form-urlencoded"}
    res = requests.post(url, headers=headers, data=request.json)
    print 'response from server:',res.text
    
    resjson = res.json()
    print resjson
    print "-----"
    print resjson['results']

    in_database = False
    if 'in_database' in resjson['results']:
        in_database = resjson['results']['in_database']

    valid = False
    if 'valid' in resjson['results']:
        valid = resjson['results']['valid']

    print "-----resjson['results']['in_database']"
    print in_database
    print "-----resjson['results']['valid']"
    print valid
    
    finalVerdict = (in_database and valid)
    print 'finalVerdict ='
    print finalVerdict
    return jsonify({ 'isExisted': finalVerdict })
    # return finalVerdict



@app.route('/check', methods=['POST'])
def check():
    print "Tutorial: Training a decision tree to detect phishing websites"

    json_ = request.json
    print "^^^^^^^^^^^^^^^^^ json_ "
    print json_

    phistank = check_phishtank(json_['url'])
    print " ----------- phistank"
    print phistank
    if phistank['in_database']==True and phistank['valid']==True:
        return jsonify({'result': True})
    elif phistank['in_database']==False and phistank['valid']==False:

        # # Load the training data
        # train_inputs, train_outputs, test_inputs, test_outputs = load_data()
        # print "Training data loaded."

        # Create a decision tree classifier model using scikit-learn
        # classifier = tree.DecisionTreeClassifier()
        custom_classifier = tree.DecisionTreeClassifier()
        
        print "Decision tree classifier created."

        print "Beginning model training."
        # Train the decision tree classifier
        # classifier.fit(train_inputs, train_outputs)
        custom_classifier.fit(custom_train_inputs, custom_train_outputs)
        
        print "Model training completed."


        attribute = []
        print '###################'
        # url = 'http://88.204.202.98/2/paypal.ca/index.html'
        # url = 'http://0x58.0xCC.0xCA.0x62/2/paypal.ca/index.html'
        # attribute.append(rule01_ip(json_['url']))
        # attribute.append(rule02_length(json_['url']))
        # attribute.append(rule10_favicon(json_['url']))
        # attribute.append(rule11_non_standard_port(json_['url']))
        # attribute.append(rule12_favicon(json_['url']))

        url = json_['url']
        attribute.append(rule111_ip(url))
        attribute.append(rule112_length(url))
        attribute.append(rule113_tinyurl(url))
        attribute.append(rule114_atsymbol(url))
        attribute.append(rule115_doubleslash(url))
        attribute.append(rule116_prefix(url))
        attribute.append(rule117_subdomain(url))
        attribute.append(rule1110_favicon(url))
        attribute.append(rule1111_non_standard_port(url))
        attribute.append(rule1112_https(url))
        
        print 'attribute='
        print attribute
        print '###################'


        # Use the trained classifier to make predictions on the test data
        # rudy_inputs = [-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,0,1,1,1,1,-1,-1,-1,-1,1,1,-1]
        # predictions = classifier.predict([json_['input']])
        predictions = custom_classifier.predict([attribute])
        print "------ test_inputs ------"
        # print test_inputs
        # print len(test_inputs)
        print "Predictions on testing data computed."
        print predictions
        print "----------------- -------"
        # print len(predictions)

        # Print the accuracy (percentage of phishing websites correctly predicted)

        rudy_outputs = [-1]
        print "test_outputs"
        print len(test_outputs)
        # accuracy = 100.0 * accuracy_score(test_outputs, predictions)
        # accuracy = 100.0 * accuracy_score(rudy_outputs, predictions)
        # print "The accuracy of your decision tree on testing data is: " + str(accuracy)
        # return jsonify({'message': "The accuracy of your decision tree on testing data is: " + str(accuracy)})
        

        if predictions[0] == 1:
            return jsonify({'result': True})
        else:
            return jsonify({'result': False})
    else:
        return jsonify({'result': False})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception, e:
        port = 80

    try:
        # Load the training data
        train_inputs, train_outputs, test_inputs, test_outputs = load_data()
        print "Training data loaded."

        custom_train_inputs, custom_train_outputs, custom_test_inputs, custom_test_outputs = load_custom_data()
        print "Custom training data loaded."


    except Exception, e:
        print 'No model here'
        print 'Train first'


    app.run(host='0.0.0.0', port=port, debug=True)
