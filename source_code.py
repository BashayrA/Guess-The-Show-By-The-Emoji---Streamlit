import streamlit as st
import random
import time
import os

def launch_game(path: str, progress = 0):
    '''Control the flow of the game and choosing a random Show for the player to guess'''

    # choosing a show randomly from the file and storing its name and emojies
    games_list = open(path, encoding="utf-8").readlines()
    index = random.randint(0, len(games_list)-1)
    show, emoji = games_list[index].split('/')
    emoji.strip()
    show.strip().lower()
    
    # display the emojies, the text input box, and the button 
    st.write(emoji)
    value = (st.text_input("Your Guess")).lower()
    st.subheader('', divider='red')
    
    # check if the session_state is empty then add a 'name' attribute to store show names and add the first appearing show
    if 'show' not in st.session_state:
        st.session_state['show'] = []
        st.session_state['show'].append(show)
        st.session_state['score'] = 0
    
    if value == "":
        pass
        #st.write("text field is empty")
    
    elif value in st.session_state['show'][-1]:
        st.balloons()
        st.write(f"Correct! {st.session_state['show'][-1]} is the right answer")
        st.session_state['score'] += 1

    else:
        st.write(f"wrong 😓 ({st.session_state['show'][-1]}) is the right answer")

    # add the next name to appear immedietly
    st.session_state['show'].append(show.lower())    

    # adding the score counter
    st.write('Score: ', st.session_state['score']*'🌟')

def match_selection():
    '''Retrieve the show data (show, emojies)'''
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
        spacet = os.path.join(os.path.dirname(__file__), "st.txt")
        launch_game(spacet) 

    elif selection == "MBC3":
        mbc3 = os.path.join(os.path.dirname(__file__), "MBC3.txt")
        launch_game(mbc3)                   

    elif selection == "Netflix series":
        Netflix = os.path.join(os.path.dirname(__file__), "Netflix.txt")
        launch_game(Netflix)     

# main code
st.set_page_config("Guess The Show By Emoji", "✨", layout="wide")
st.header("Guess The Show By Emojies", divider='blue')
st.subheader("Choose a Category", divider='red')
st.subheader("Based on the Emojies Bellow .. Guess The Name Of The Show")
match_selection()
st.subheader("", divider='blue')
