import streamlit as st
import random
import os
import difflib

def is_match(value, correct_title, threshold=0.6):
    '''basic comparsion for misspelled words'''

    similarity = difflib.SequenceMatcher(None, value.lower(), correct_title.lower()).ratio()
    st.session_state['show_number'] += 1
    return similarity >= threshold


def launch_game(path: str):
    '''Control the flow of the game and choosing a random Show for the player to guess'''

    # choosing a show randomly from the file and storing its name and emojies
    games_list = open(path, encoding="utf-8").readlines()
    index = random.randint(0, len(games_list)-1)
    show, emoji = games_list[index].split('/')
    emoji.strip()
    show.strip().lower()
    
    # display the emojies, the text input box, and the button 
    col1, col2, col3 = st.columns([1, 2, 1])  # Side padding with center focus
    with col2:
        st.markdown(f"<p style='text-align: center; font-size: 46px;'>{emoji}</p>", unsafe_allow_html=True)
        value = st.text_input("Your Guess")
    
    # check if the session_state is empty then add a 'name' attribute to store show names and add the first appearing show
    if 'show' not in st.session_state:
        st.session_state['show'] = []
        st.session_state['show'].append(show)

    # game basic comparsion
    if value == "":
        pass
    elif is_match(value, st.session_state['show'][-1]) or value.lower() in st.session_state['show'][-1].lower():
        st.balloons()
        st.markdown(f"<p style='text-align: center; color: green; font-size: 18px;'>✅ Correct! <strong>{st.session_state['show'][-1]}</strong> is the right answer</p>", unsafe_allow_html=True)
        st.session_state['score'] += 1
    else:
        st.markdown(f"<p style='text-align: center; color: red; font-size: 18px;'>❌ Wrong! The correct answer was <strong>{st.session_state['show'][-1]}</strong></p>", unsafe_allow_html=True)

    # add the next name to appear immedietly
    st.session_state['show'].append(show.lower())

    with col2:
        st.markdown(f"<h4 style='text-align: center;'>Score: {st.session_state['score']}/{st.session_state['show_number']}</h4>", unsafe_allow_html=True)

def match_selection():
    '''Retrieve the show data (show, emojies)'''

    if 'score' not in st.session_state:
        st.session_state['score'] = 0

    if 'show_number' not in st.session_state:
        st.session_state['show_number'] = 0


    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown("<p style='font-size: 24px; text-align: center;'>✨ Choose a Category</p>", unsafe_allow_html=True)
        selection = st.radio(
            "",
            ["📺 Netflix series", "🧚 Disney", "🚀 Spacetoon", "🎮 MBC3", "🎨 Cartoon Network"],
            label_visibility="collapsed"
        )

    if selection == "🎨 Cartoon Network":
        # read the file path from os to generalize its location format
        cn = os.path.join(os.path.dirname(__file__), "cn.txt")
        launch_game(cn)
    
    elif selection == "🧚 Disney":
        Disney = os.path.join(os.path.dirname(__file__), "Disney.txt")
        launch_game(Disney)
    
    elif selection == "🚀 Spacetoon":
        spacet = os.path.join(os.path.dirname(__file__), "st.txt")
        launch_game(spacet)

    elif selection == "🎮 MBC3":
        mbc3 = os.path.join(os.path.dirname(__file__), "MBC3.txt")
        launch_game(mbc3)             

    elif selection == "📺 Netflix series":
        Netflix = os.path.join(os.path.dirname(__file__), "Netflix.txt")
        launch_game(Netflix)

# main code
st.set_page_config("Guess The Show By Emoji", "✨", layout="wide")

# page styling
st.markdown("""
    <style>
    /* 🔲 Dark but gentle background */
    .stApp {
        background-color: #1c1c1e;  /* Soft charcoal */
    }

    /* 🎨 General text styling */
    h1, h2, h3 {
        color: #ff66c4 !important;  /* Neon pink for headers */
        text-shadow: 0 0 4px #ff66c4;
    }

    h4, p, label {
        color: #66fcf1 !important;  /* Aqua accents for prompts */
        text-shadow: none;
    }

    /* 🎮 Text input box */
    .stTextInput > div > input {
        background-color: #2f2f33 !important;
        color: #000000 !important;  /* Black typed text for visibility */
        border: 2px solid #ff66c4 !important;
        padding: 10px;
        border-radius: 8px;
    }

    /* 🧾 Subheader tweaks */
    .stMarkdown div {
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #6c63ff;'>🎭 Guess the Show by Emojis!</h1>", unsafe_allow_html=True)
match_selection()
st.subheader("", divider='blue') # last part of the page