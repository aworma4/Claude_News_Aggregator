'''
Function to query claude
'''
import os 
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import streamlit as st

@st.cache_data()
def claude_query(initial_prompt = 'You are a human analyst.', query = ''):
    '''
    
    '''

    #get api key
    # import API key
    with open('api.txt') as f:
        API_KEY = f.read().strip() 
    #import anthropic 
    
    
    os.environ["ANTHROPIC_API_KEY"] = API_KEY


    ### create query
    anthropic = Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=API_KEY,
    )

    #create query
    query1 = initial_prompt + query

    #get results 
    completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} {query1} {AI_PROMPT}",
)
    output = completion.completion

    return query1, output