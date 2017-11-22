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

    print "-----resjson['results']['in_database']"
    print in_database
    print "-----resjson['results']['valid']"
    print valid
    
    finalVerdict = (in_database and valid)
    print 'finalVerdict ='
    print finalVerdict

    # return jsonify({ 'isExisted': finalVerdict })
    return finalVerdict



def rule01_ip(url):
    # \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    print 'rule01_ip function -> ' + url
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    matchObj = re.search(regex, url);
    print matchObj
    if matchObj:
        return 1
    else:
        return -1

def rule02_length(url):
    print 'rule02_length function -> ' + url

    if len(url) < 54:
      return -1
    elif len(url) >= 54 and len(url) <= 75:
      return 0
    else:
      return 1

def rule10_favicon(url):
    print 'rule10_favicon ->' + url
    favicon_url = get_favicon_url(url);
    if favicon_url == None:
        return 1
    if url not in favicon_url:
        return -1
    else:
        return 1

def rule11_non_standard_port(url):
    print 'rule11_non_standard_port ->' + url
    parsed_url = urlparse(url);
    port_number = parsed_url.port;
    accepted_ports = [None, 21, 22, 23, 80, 443, 445, 1433, 1521, 3306, 3389];
    if port_number in accepted_ports:
        return 1
    else:
        return -1


# -----------------------------------------------------------

app = Flask(__name__)

# train_inputs, train_outputs, test_inputs, test_outputs = ''
train_inputs = ''
train_outputs = ''
test_inputs = ''
test_outputs = ''


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
    print "^^^^^^^^^^^^^^^^^ json_.['input'] "
    print json_['input']


    phistank = check_phishtank(json_['url'])
    print " ----------- phistank"
    print phistank
    if phistank:
        return jsonify({'result': "Phishing site"})
    else:

        # # Load the training data
        # train_inputs, train_outputs, test_inputs, test_outputs = load_data()
        # print "Training data loaded."

        # Create a decision tree classifier model using scikit-learn
        classifier = tree.DecisionTreeClassifier()
        print "Decision tree classifier created."

        print "Beginning model training."
        # Train the decision tree classifier
        classifier.fit(train_inputs, train_outputs)
        print "Model training completed."


        attribute = []
        print '###################'
        # url = 'http://88.204.202.98/2/paypal.ca/index.html'
        # url = 'http://0x58.0xCC.0xCA.0x62/2/paypal.ca/index.html'
        attribute.append(rule01_ip(json_['url']))
        attribute.append(rule02_length(json_['url']))
        attribute.append(rule10_favicon(json_['url']))
        attribute.append(rule11_non_standard_port(json_['url']))
        # attribute.append(rule12_favicon(json_['url']))
        print attribute
        print '###################'



        # Use the trained classifier to make predictions on the test data
        # rudy_inputs = [-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,0,1,1,1,1,-1,-1,-1,-1,1,1,-1]
        predictions = classifier.predict([json_['input']])
        print "test_inputs ------"
        # print test_inputs
        # print len(test_inputs)
        print "Predictions on testing data computed."
        print predictions
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
            return jsonify({'result': "Phishing site"})
        else:
            return jsonify({'result': 'You are safe.'})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception, e:
        port = 80

    try:
        # Load the training data
        train_inputs, train_outputs, test_inputs, test_outputs = load_data()
        print "Training data loaded."

    except Exception, e:
        print 'No model here'
        print 'Train first'


    app.run(host='0.0.0.0', port=port, debug=True)
