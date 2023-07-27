import streamlit as st
from claude_query import claude_query

st.set_page_config(page_title='FlashResponse', page_icon=':boom:', layout="centered", initial_sidebar_state="expanded") 
color = 'blue'
st.write(f"<style>div.block-container{{background-color: {color};}}</style>", unsafe_allow_html=True)


tabs = ["FlashResponse", "Summaries","Sentiment", "Tweets", "Press Releases", "Government Policy Summary", "Response Ideation"] 
article_file = 'heat-wave/combined_8_uk_articles.txt'
print(article_file)


genre=None # to make it global
with open(article_file, encoding='utf-8') as f:
    URLS = f.read().strip()
#print(URLS)
#####
URLS_GOVUK = URLS


selected_tab = st.sidebar.radio("Tabs", tabs)

start_prompt = 'You are a human analyst. '
hide_text =False

if selected_tab == "FlashResponse":
    st.header("FlashResponse")
    st.write("Welcome to the home page!")

    #genre = st.selectbox("Select a news topic", ["Heatwave", "Emmergency Alert"])
    st.session_state.genre  = st.text_input('Select a news topic to analyse',placeholder ='Heatwave')
    #print(st.session_state.genre)
    
    if st.session_state.genre==None:
        st.session_state.genre='Heatwave'
    
    st.write("You selected:", st.session_state.genre)
    


    #initial prompot 
    # prompt I



elif selected_tab == "Summaries":
    st.header("Summaries")
    st.subheader(f"**This is the summaries page, it gives summaries for the most important articles relating to {st.session_state.genre}!**")

    query = f'Considering the following {URLS}. Summarise each in 1 sentence.'
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

    
elif selected_tab == "Tweets":
    st.header("Tweets")
    st.subheader(f"**This is the tweets page, it gives a range of tweet respones for the press office based on the articles analysed, for the most important article relating to {st.session_state.genre}!**")

    query = f'Considering the following {URLS}. Create 3 tweets for the UK government press office of varying tones.'
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


elif selected_tab == "Press Releases":
    st.header("Press Releases")
    st.subheader(f"**This is the Press Releases page, it gives a standard Press Releases respones based on the articles analysed, for the most important articles relating to {st.session_state.genre}!**")

    query = f'Considering the following {URLS}. Create a press release for the UK government press office of varying tones.'
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


elif selected_tab == "Government Policy Summary":
    st.header("Government Policy Summary")
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


elif selected_tab == "Response Ideation":
    st.header("Response Ideation")
    st.subheader(f"**This is the Response Ideation page, it gives examples of the types of respones the UK governmetn could take, relating to {st.session_state.genre}!**")

    query = f'Considering the following {URLS}. Create 5 different UK government policy responses of varying tones.'
    _, output = claude_query(initial_prompt = start_prompt, query = query)
    st.write(output)

    toggle = st.checkbox('Toggle for prompt')

    if 'toggle' not in st.session_state:
        st.session_state.toggle = False 
    

    
    if st.session_state.toggle:
        st.write(f'For the following query: \n {_}')
    else:
        st.write('Toggle for prompt')


elif selected_tab == "Sentiment":
    st.header("Sentiment")
    st.subheader(f"**This is the general news sentiment page, it gives the general sentiment, relating to the following topic {st.session_state.genre}!**")

    query = f'Considering the following {URLS}. What is the general sentiment score (out of 10) of the proceeding article and why have you given it that score.'
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