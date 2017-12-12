
<h1> Phish Lens </h1>  
A machine learning enabled chrome extension to smartly identify possible phished pages.

Get the chrome extesnion <a href ="https://chrome.google.com/webstore/detail/phish-lens/omcddbobcimeodadbojljnnodfmmkhme">here</a>. 

<a href ="https://chrome.google.com/webstore/detail/phish-lens/omcddbobcimeodadbojljnnodfmmkhme"> <img src="https://lh6.googleusercontent.com/eER1zqe2C9OclD0jOQ6HEHBabVMHbrbHPTqqDTYtFfd_0A2BgfLPP6trKE0JBUFdgAWfCCa3V9QAyesFAgTx=w1275-h703"> </a>

<h1> What is Phishing? </h1>

Phishing is a process to steal user's sensitive information over the internet by tricking a user to enter his information on a disguised or a fake site which is a replica of the authentic site. Leading web portals get trapped because of phishing attacks each day. Thousands of passwords are stolen without either the users or the portals knowing about it, sometimes users also lose money from their bank accounts. Companies end up paying a lot of money in the courts to deal with such attacks.

<h1> Why is phishing dangerous?</h1>
There are numerous threats that phishing brings in. Primary threat from phishing is theft of identity of the users. 
Users emphasise on data security and privacy, they go to great lenghts to protect thier information from the attackers. A single breach can expose the user to multitude of threats, which include credit card fraud, credit score damage, and sometimes precious digital assets. There are also intangible threats, such as damage to credibility, loss of trust,
or embarrassment; having personal information stolen can cost a great deal more than lost cash.

<h1> Why a chrome extesnsion? </h1> 
We identify that Google Chrome browser is a popular web browser and a Chrome extension is an easier way for users to use our product and services. For this reason, we built a chrome extension with machine learning capability to detect phishing sites and notify the user in real time.

<h1> Design </h1> 

The architecure diagram is as shown below 

<img src="https://lh6.googleusercontent.com/7dh_DDffuNHG3KwBNtI5ZAMhCK0_m6jD_No95wFBnL4WAZ2-hqNAykvsvo7RuhPdtA0fU4Rfj9f2OBFLlxca=w1275-h703">

<h1> Implementation </h1>

Chrome Extension is the client that is interfacing with the user on the Google Chrome browser. Every time user enters a
new URL on the address bar, PhishLens will make an API call to the backend server. Backend server will send back a response to PhisLens. Correspondingly, PhishLens will notify a user if the URL is a phishing site. Backend server receives a request from PhishLens Chrome extension to check whether the URL is pointing to a genuine site. Then, backend server will make an API call to the Machine Learning server to check the validity of the URL. Machine Learning server uses a decision tree classifier to
predict whether a URL is a phishing site or not. The dataset that is used to train this classifier was prepared from the list of URLs (Phishing URLs and legitimate URLs). We converted each of the URLs to a set of parameters that corresponds to the URL rules output. Prior to running through these rules, we will also check with PhishTank API whether the URL is
already reported as a phishing site in their database or not. If it is not in the PhishTank database, URL will be converted into parameters and then fed into decision tree classifier.

<h1> Machine Learning rules </h1>

<img src="https://lh5.googleusercontent.com/Z_U6ExcCkGcdmRRd91FfZdknDRzrOldQoOi7ypuUP3aZsYBKcnQCO29c5E8ABnguSNBeJMTm12kSsRpbpG-x=w1275-h703">

<img src="https://lh6.googleusercontent.com/7-oq4E1PN4FpKTf4i3YxP6rv1NTvBQLXrTfJOHJ3bUVwZPNDF7IJ9Hvq8ZOx-DGB53fvEgNyNbC6TYknnQNK=w1275-h703">

<img src="https://lh5.googleusercontent.com/_O-54x8TReLlL56f0UZG3mZJ838ipkHMGK0mAiFIwXuaV2Cc4xkG8R3vUIk-wwvkWwrk4wXcl729FoT9LUZc=w1275-h703">

For example:
https://account-security-system.cf/recovery-chekpoint-login.html

If we ran through the above site to the Machine Learning Rules, the resultant parameters will look something like below:
[ -1,0,-1,-1,-1,1,-1,-1,1,-1,1 ]
These parameters are then fed to the decision tree. The decision tree internally compares these parameters with the existing set of datasets and returns a boolean valueof True if URL is a phishing site and False otherwise.


<h1> Conclusion and future work </h1>

In this project, we have built a Chrome Extension that has successfully detected phishing URLs. Our implementation is not 100% accurate, however, we can increase detection accuracy by doing the following:
1. Train the Machine Learning classifier with larger dataset so that it can improve the prediction accuracy of detecting
phishing sites.
2. Implement additional machine learning rules to differentiate a common pattern shared among phish site and non-phish site.

<h1> Acknowledgement </h1>

We would like to thank Professor Rakesh Ranjan, Dept. of Computer Software Engineering, San Jose State University, for immense motivation and guidance throughout the project.

<h1> Special Credits </h1>

* Lichman, M. (2013). UCI Machine Learning Repository http://archive.ics.uci.edu/ml. Irvine, CA: University of California, School of Information and Computer Science.

* Nicolas Papernot (2016) Detecting phishing websites using a decision tree https://github.com/npapernot/phishing-detection

* Sheng S, Magnien B, Kumaraguru P, Acquisti A, Cranor LF, Hong J, Nunge E (2007) Anti-phishing phil: the design and evaluation of a game that teaches people not to fall for phish. In: Proceedings of the SOUPS, Pittsburg, pp 88–99

* Sara Radicati, PhD; Principal Analyst: Justin Levenstein. Statistics Report 2013-2017.The Radicati Group, Inc. A Technology Market Research Firm.

