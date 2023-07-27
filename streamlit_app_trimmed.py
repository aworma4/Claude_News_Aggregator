import streamlit as st
from claude_query import claude_query
from PIL import Image



st.set_page_config(page_title='FlashResponse (HITL)', page_icon=':boom:', layout="centered", initial_sidebar_state="expanded") 
color = 'blue'
st.write(f"<style>div.block-container{{background-color: {color};}}</style>", unsafe_allow_html=True)


tabs = ["FlashResponse (HITL)", "HITL SentAnalyser", "Media Impressions", "Response Whiteboard", "Government Policy Summary","Media Government Comparison"] 
article_file = 'heat-wave/combined_8_uk_articles.txt'  # contains text of urls from artilces_Sampled
articles_sampled = 'news_articles_URLS.txt'  #contains urls of webpages scraped

gov_file = 'heat-wave/combined_gov_uk_Articles.txt'
gov_file_most_relevance = 'heat-wave/fake_policy.txt'
gov_uk_urls = 'gov_uk_urls.txt'

with open(gov_uk_urls, encoding='utf-8') as f:
    URLS_GOVUK_list = f.read().strip()

with open(articles_sampled, encoding='utf-8') as f:
    URLS_list = f.read().strip()

genre=None # to make it global
with open(article_file, encoding='utf-8') as f:
    URLS = f.read().strip()
#print(URLS)
#####
with open(gov_file, encoding='utf-8') as f:
    URLS_GOVUK = f.read().strip()
with open(gov_file_most_relevance, encoding='utf-8') as f:
    URLS_GOVUK_most_relevance = f.read().strip()

with open('heat-wave/k_shot_output.txt', encoding='utf-8') as f:
    k_shot_output = f.read().strip()


st.session_state.genre='Heatwave'


selected_tab = st.sidebar.radio("Tabs", tabs)

start_prompt = 'You are a human analyst. '
hide_text =False

if selected_tab == "FlashResponse":
    st.header("FlashResponse")
    st.write("Welcome to the home page!")

    #genre = st.selectbox("Select a news topic", ["Heatwave", "Emmergency Alert"])
    st.session_state.genre  = st.text_input('Select a news topic to analyse',placeholder ='Heatwave')
    #print(st.session_state.genre)
    

    
    st.write("You selected:", st.session_state.genre)

    toggle = st.checkbox('Toggle for URLs used')

    if 'toggle' not in st.session_state:
        st.session_state.toggle = False
    
    if toggle:
        st.session_state.toggle = not st.session_state.toggle 
    
    if st.session_state.toggle:
        st.write("Article used", URLS_list)
        st.write("Gov UK articles used", URLS_GOVUK_list)
    else:
        st.write('Toggle for prompt')


    #initial prompot 
    # prompt I



elif selected_tab == "Media Impressions":
    st.header("Media Impressions")
    st.subheader(f"**This is the Media Impressions page, it produces a summary of each article or an overall descriptive sentiment score with reasons. Which relates to the topic,  {st.session_state.genre}!**")

    media_type = st.selectbox("Select a Type of analysis", ["Summarise Themes", "Summarise each Article", "Fraction of Topics", "Overall Sentiment"])

    if media_type == "Summarise each Article":
        query = f'Considering the following {URLS}. Summarise each separte article in 1 sentence.'
        query_short = f'Considering the following {URLS_list}. Summarise each seperate article in 1 sentence.'

    elif media_type == "Summarise Themes":
        query = f'Considering the following {URLS}. Summarise the top 5 themes in the preceeding articles, include quotes from these articles.'
        query_short = f'Considering the following {URLS_list}. Summarise the top 5 themes in the preceeding articles, include quotes from these articles'

        
    elif media_type == "Fraction of Topics":
            query = f'Considering the following {URLS}. Give me a sense about the overall sentiment of these 8 articles, highlighting different themes (max 5) and the percentage of coverage.'
            query_short = f'Considering the following {URLS_list}. Give me a sense about the overall sentiment of these 8 articles, highlighting different themes (max 5) and the percentage of coverage.'

    elif media_type == 'Overall Sentiment':
            query = f'Considering the following articles {URLS}. What is the general sentiment score (between -1 and 1 where -1 is maximally negative and 1 is maximally positive) of the proceeding articles and why have you given that score.'
            query_short = f'Considering the following articles {URLS_list}. What is the general sentiment score (between -1 and 1 where -1 is maximally negative and 1 is maximally positive) of the proceeding articles and why have you given that score.'

    
    #img = Image.open('heat-wave/media_image.jpg')
    #st.image(img)

#What is the general sentiment score (out of 10) of the proceeding article and why have you given it that score.'
    
    _, output = claude_query(initial_prompt = start_prompt, query = query)
    st.write(output)

    toggle = st.checkbox('Toggle for prompt')

    if 'toggle' not in st.session_state:
        st.session_state.toggle = False
    
    if toggle:
        st.session_state.toggle = not st.session_state.toggle 
    
    if st.session_state.toggle:
        st.write(f'For the following query: \n {query_short}')
    else:
        st.write('Toggle for prompt')




elif selected_tab == "Response Whiteboard":
    st.header("Tweets or Press Releases")
    st.subheader(f"**This assists with crafting responses to the selected news item ({st.session_state.genre}) either in a tweet or press release form.!**")
    
    media_type = st.selectbox("Select a Type of output", ["Tweet", "Press Release"])

    if media_type == "Tweet":
            query = f'Considering the following {URLS}. Create 3 tweets for the UK government press office of varying tones.'
            query_short = f'Considering the following {URLS_list}. Create 3 tweets for the UK government press office of varying tones.'        
    elif media_type == "Press Release":
        query = f'Considering the following {URLS}. Create a press release for the UK government press office of varying tones.'
        query_short = f'Considering the following {URLS_list}. Create a press release for the UK government press office of varying tones.'        
    
    _, output = claude_query(initial_prompt = start_prompt, query = query)
    st.write(output)

    toggle = st.checkbox('Toggle for prompt')

    if 'toggle' not in st.session_state:
        st.session_state.toggle = False
    
    if toggle:
        st.session_state.toggle = not st.session_state.toggle 
    
    if st.session_state.toggle:
        st.write(f'For the following query: \n {query_short}')
    else:
        st.write('Toggle for prompt')


elif selected_tab == 'HITL SentAnalyser':
        article  = st.text_input('Select one news article for aspect based training',placeholder ='https://dailyuknews.com/science/what-caused-the-greece-wildfires-and-how-is-the-rhodes-blaze-spreading/')

        aspect  = st.text_input('Select an aspect based on which you want to perform the sentiment analysis',placeholder ='Public perception.')

        article2  = st.text_input('Select unseen test document',placeholder ='https://www.dailymail.co.uk/wires/reuters/article-12323727/WHO-warns-dengue-risk-global-warming-pushes-cases-near-historic-highs.html')

    


        if st.button('Click Me'):
            st.write('1 Shot (Human in the loop) learning complete!')
            st.write(k_shot_output)


elif selected_tab == "Government Policy Summary":
    st.header("Media Missinformation")
    st.subheader(f"**This is the current government policy page, it summaries the top articles on gov.uk relating to the selected news incident, {st.session_state.genre}!**")

    query = f'Considering the following {URLS_GOVUK}. Summarise each article.'
    _, output = claude_query(initial_prompt = start_prompt, query = query)
    st.write(output)

    toggle = st.checkbox('Toggle for prompt')

    if 'toggle' not in st.session_state:
        st.session_state.toggle = False 
    
    if toggle:
        st.session_state.toggle = not st.session_state.toggle 
    
    if st.session_state.toggle:
        st.write(f'For the following query: \n {_}')
    else:
        st.write('Toggle for prompt')



elif selected_tab == "Media Government Comparison":
    st.header("Media Government Comparison")
    st.subheader(f"**This is the comparison between current government policy versus the selected news incident, it looks for miss information and gaps in policy {st.session_state.genre}!**")

    query = f'Look for differences between UK government policy: {URLS_GOVUK_most_relevance} and the following news articles: {URLS}. Summarise each difference in a bullet pointed list, if there are none print nothing.'
    _, output = claude_query(initial_prompt = start_prompt, query = query)
    st.write(output)

    query = f'Highlight any of the following bullet points that relate to miss information, {output}'

    st.subheader('Missinformation Detected')
    _, output2 = claude_query(initial_prompt = start_prompt, query = query)
    st.write(output2)
    
    toggle = st.checkbox('Toggle for prompt')

    if 'toggle' not in st.session_state:
        st.session_state.toggle = False 
    
    if toggle:
        st.session_state.toggle = not st.session_state.toggle 
    
    if st.session_state.toggle:
        st.write(f'For the following query: \n {_}')
    else:
        st.write('Toggle for prompt')





