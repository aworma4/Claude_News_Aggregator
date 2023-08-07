# Evidence House Hackathon AI Code
A basic streamlit app that uses Claude AI API calls to submit engineered prompts and return the results.
The intention was to provide rapid information on various news topics as follows:
  * A webscraping layer that takes a sample of article from the web (this can be a balanced sample, this could be a weighted sample or it could simply be the top N results for that given topic)
  * Summarises + performs sentiment analysis on these articles.
  * Generates typical tweets/press releases to this evetn
  * Pulls in relevant gov.uk articles and compares these to the news for differences in information

The code itself is very basic and poorly written - it was written in about 5 hours. 

# Using the code 
* Load in required packages from requirements.txt
* Add in your own api key to the api.txt file
* Launch streamlit with : streamlit run streamlit_app_trimmed.py

# Notes
Currently the app pulls in .txt files generated by the webscraper.py code. For this to work for an arbitrary news topics (rather than the chosen web topic) the two code modules need to be combined:
* Webscraper
* Streamlit (with the claude api function(
Note that searches can be cached so a webscraping search only need be performed once.
