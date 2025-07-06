import streamlit as st
import random
import time
import os

def launch_game(path: str):
    '''Control the flow of the game and choosing a random Show for the player to guess'''
    
    # choosing a show randomly from the file and storing its name and emojies
    games_list = open(path, encoding="utf-8").readlines()
    index = random.randint(0, len(games_list)-1)
    name, emoji = games_list[index].split('/')
    emoji.strip()
    name.strip()
    
    # a short delay to view the emojies and the show name together for a while of time 
    time.sleep(1)
    
    # display the emojies, the text input box, and the button 
    st.write(emoji)
    value = (st.text_input("Your Guess")).lower()
    st.subheader('', divider='red')
    button = st.button("Check")
    
    # check if the session_state is empty then add a 'name' attribute to store show names and add the first appearing show
    if 'name' not in st.session_state:
        st.session_state['name'] = []
        st.session_state['name'].append(name.lower())
    
    # check for the show name after clicking the button
    if button: #static file + write on file at the beggining
        if value in st.session_state['name']:
            st.balloons()
            st.write(f"Correct! \n{value} is the right answer")
        else:
            st.write(f"wrong 😓 ({st.session_state['name'][-1]}) is the right answer")
        
        # add the next name to appear immedietly
        st.session_state['name'].append(name.lower())    


def match_selection():
    '''Retrieve the show data (name, emojies)'''
    # store the selection choice and match it with the same category
    selection = st.segmented_control('',  ["Netflix series", "Disney", "Spacetoon", "MBC3", "Cartoon Network"])

    if selection == "Cartoon Network":
        # read the file path from os to generalize its location format
        cn = os.path.join(os.path.dirname(__file__), "cn.txt")
        launch_game(cn)
    
    elif selection == "Disney":
        Disney = os.path.join(os.path.dirname(__file__), "Disney.txt")
        launch_game(Disney)  
    
    elif selection == "Spacetoon":
        st = os.path.join(os.path.dirname(__file__), "st.txt")
        launch_game(st) 

    elif selection == "MBC3":
        mbc3 = os.path.join(os.path.dirname(__file__), "MBC3.txt")
        launch_game(mbc3)                   

    elif selection == "Netflix series":
        Netflix = os.path.join(os.path.dirname(__file__), "Netflix.txt")
        launch_game(Netflix)     

# main code
st.set_page_config("Guess The Show By Emoji", "✨", layout="wide")
st.header("Guess Game Emoji", divider='blue')
st.subheader("Choose a Category", divider='red')
st.subheader("Based on the Emojies Bellow .. Guess The Name Of The Show")
match_selection()
st.subheader("", divider='blue')
