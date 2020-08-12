# Compare elements using Python and TwitterSearch API
TwitterSearch allows us to search within Twitter data. The solution compares two elements and generates a percentage graph as HTML output.
 
$ Create TwitterSearch App
Go to apps.twitter.com
Login
Click on ‘ Create New App ’ button
Fill in the details
After the app is created. Go to its details
Go to Keys and Access Tokens
Copy Consumer Key and Consumer Secret keys
# Configure the Twitter Script
Open config.py file
Paste Consumer Key in place of YOUR_CONSUMER_KEY_HERE
Paste Consumer Secret key in place of YOUR_CONSUMER_SECRET_KEY_HERE
# Install Requirements
Run this command in terminal to install the required packages
pip install -r requirements.txt
# Use the app

Type this command in terminal to use the script
./twitter.py <keyword1> <keyword2>
A html page will be generated with name in current folder
With name keyword1 keyword2 - datatime.html
 


