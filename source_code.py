import streamlit as st
import random
import time

# file initilizing and writting data
with open('guessgameCN.txt', 'w', encoding='utf-8') as CN:
    CN.write('''Adventure Time/	🏰👦🐶🌈
The Amazing World of Gumball/	🐱🐟🏫😂
Regular Show/	🦝🦅🏞️😂
Steven Universe/	💎👦🌌🎶
Teen Titans Go!/	🦸‍♂️🦸‍♀️🌆😂
Ben 10/	👦👽🛡️🔄
The Powerpuff Girls/	👧👧👧💥🌆
Dexter's Laboratory/	🧪🔬👨‍🔬🏠
Johnny Bravo/	💪🕶️😂👱‍♂️
Samurai Jack/	🥷⚔️🌌👊
Courage the Cowardly Dog/	🐶😱👻🏠
Ed, Edd n Eddy/	😂🏠👦🍬
The Grim Adventures of Billy & Mandy/	💀👦👧😂
Codename: Kids Next Door/	🧒🕵️‍♂️🌍🔍
Foster's Home for Imaginary Friends/	🏠👻👫🎨
The Marvelous Misadventures of Flapjack/	🚢👦🍬🌊
Chowder/	🍲👦🍴😂
Total Drama Island/	🏝️🎭😂🏆
The Secret Saturdays/	🐉🕵️‍♂️🌍🔍
Generator Rex/	🤖👦💥🌆
Sym-Bionic Titan/	🤖👦👧💥
Young Justice/	🦸‍♂️🦸‍♀️🌆💥
Justice League/	🦸‍♂️🦸‍♀️🌍💥
Batman: The Animated Series/	🦇🦸‍♂️🌆🔍
Green Lantern: The Animated Series/	💡🦸‍♂️🌌💥
Static Shock/	⚡🦸‍♂️🌆💥
Teen Titans/	🦸‍♂️🦸‍♀️🌆💥
The Looney Tunes Show/	🐰🦆😂🎬
Tom and Jerry/	🐱🐭😂🏠
Scooby-Doo, Where Are You!/	🐶🕵️‍♂️👻🚐
The Flintstones/	🦕🏠👨‍👩‍👧‍👦🚗
The Jetsons/	🚀🏠👨‍👩‍👧‍👦🤖
Scooby-Doo/	🐶🕵️‍♂️👻🚐
The Powerpuff Girls/	👧👧👧💥🌆
Johnny Bravo/	💪🕶️😂👱‍♂️
Dexter's Laboratory/	🧪🔬👨‍🔬🏠
Samurai Jack/	🥷⚔️🌌👊
Courage the Cowardly Dog/	🐶😱👻🏠
Ed, Edd n Eddy/	😂🏠👦🍬
The Grim Adventures of Billy & Mandy/	💀👦👧😂
Codename: Kids Next Door/	🧒🕵️‍♂️🌍🔍
Foster's Home for Imaginary Friends/	🏠👻👫🎨
Ben 10/	👦👽🛡️🔄
Teen Titans/	🦸‍♂️🦸‍♀️🌆💥
Avatar: The Last Airbender/	🌊🔥🌪️🌍
Winx Club/	🧚‍♀️🌸🦋🏰
Totally Spies!/	🕵️‍♀️👧🔍🌆
Kim Possible/	🥷🧑‍🦰🦸‍♀️📱
Lilo & Stitch/	👽🏝️👧🐶
The Fairly OddParents/	🧚‍♂️👦🧚‍♀️🏠''')
    
with open('guessgameDisney.txt', 'w', encoding='utf-8') as Disney:
    Disney.write('''The Lion King/	🦁👑🌅🎶
Snow White and the Seven Dwarfs/	👸🍎🌲🧙‍♀️
Beauty and the Beast/	🌹👸🐻🏰
Pinocchio/	🤥🧚‍♂️🐋🎠
Frozen/	❄️👭⛄🏔️
Moana/	🌊🚤🌺🏝️
Aladdin/	🧞‍♂️🕌🐒🌟
Cinderella/	👠🎃👸🕛
The Little Mermaid/	🧜‍♀️🌊🐠🎶
Mulan/	🏹👸🐉⚔️
Pocahontas/	🌳🛶👸🍂
Tangled/	🌟👸🏰🌺
Hercules/	💪⚡🏛️👹
Tarzan/	🦍🌳👨‍🦱🏞️
The Jungle Book/	🐻🐍🐅🌴
Peter Pan/	🧚‍♂️🏴‍☠️🌟🗺️
Sleeping Beauty/	👸🛌🐉🧙‍♀️
Dumbo/	🐘🎪🎩🎠
Bambi/	🦌🌲🔥🌸
Alice in Wonderland/	🐇🎩🌀👧
The Aristocats/	🐱🎶🎩🗼
Lady and the Tramp/	🐶🍝🌙❤️
101 Dalmatians/	🐾🐶👩‍👧‍👦🚗
The Hunchback of Notre Dame/	🏰🔔👨‍🦱🔥
Lilo & Stitch/	👽🏝️👧🐶
The Nightmare Before Christmas/	🎃🎄👻🎶
Toy Story/	🤠🚀🧸👦
Monsters, Inc./	👹🚪👧🏢
Finding Nemo/	🐠🌊🐢🦈
The Incredibles/	🦸‍♂️🦸‍♀️👨‍👩‍👧‍👦💥
Ratatouille/	🐭🍳👨‍🍳🇫🇷
Up/	🎈🏠👴🐶
WALL-E/	🤖🌍🚀❤️
Brave/	🏹👸🐻🏴󠁧󠁢󠁳󠁣󠁴󠁿
Zootopia/	🦊🐰🚓🌆
Big Hero 6/	🤖👨‍🔬💥🏙️
Coco/	🎸💀👨‍👩‍👧‍👦🌺
Inside Out/	😊😢😡😱
Cars/	🚗🏁🏎️🌄
A Bug's Life/	🐜🌾🐞🦗
The Princess and the Frog/	👸🐸🎹🎶
Wreck-It Ralph/	👾🎮🍬🏆
Frozen II/	❄️👭🍂🌊
Ralph Breaks the Internet/	💻👾🌐🎮
Tangled/	🌟👸🏰🌺
The Good Dinosaur/	🦕🌲👦🌄
Onward/	🧙‍♂️🧝‍♂️🚐🗺️
Soul/	🎹👻🎶🌌
Raya and the Last Dragon/	🐉👸⚔️🌊
Luca/	🧜‍♂️🏖️🍝🇮🇹''')
    
with open('guessgameMBC3.txt', 'w', encoding='utf-8') as MBC3:
    MBC3.write('''Detective Conan/	🕵️‍♂️🔍🧠💼
Captain Tsubasa/	⚽🏆🇯🇵👟
Dragon Ball Z/	🐉👊💥🌌
Naruto/	🥷🍥🔥🌪️
One Piece/	🏴‍☠️🌊👒⚓
Digimon Adventure/	🐉🌐👾🧒
Hunter x Hunter/	🏹🧒🌲👊
Beyblade/	🌀⚔️🏆👦
Slam Dunk/	🏀⛹️‍♂️🏆🇯🇵
Inazuma Eleven/	⚽⚡🏆👟
Pokemon/	🐉⚡🎮🔍
Doraemon/	🐱🕰️🧒🔧
Tom and Jerry/	🐱🐭😂🏠
The Adventures of Tintin/	🕵️‍♂️🌍🚢🔍
The Smurfs/	👨‍👩‍👧‍👦🏞️🔵🍄
The Flintstones/	🦕🏠👨‍👩‍👧‍👦🚗
The Jetsons/	🚀🏠👨‍👩‍👧‍👦🤖
Looney Tunes/	🐰🦆😂🎬
Scooby-Doo/	🐶🕵️‍♂️👻🚐
The Powerpuff Girls/	👧👧👧💥🌆
Johnny Bravo/	💪🕶️😂👱‍♂️
Dexter's Laboratory/	🧪🔬👨‍🔬🏠
Samurai Jack/	🥷⚔️🌌👊
Courage the Cowardly Dog/	🐶😱👻🏠
Ed, Edd n Eddy/	😂🏠👦🍬
The Grim Adventures of Billy & Mandy/	💀👦👧😂
Codename: Kids Next Door/	🧒🕵️‍♂️🌍🔍
Foster's Home for Imaginary Friends/	🏠👻👫🎨
Ben 10/	👦👽🛡️🔄
Teen Titans/	🦸‍♂️🦸‍♀️🌆💥
Avatar: The Last Airbender/	🌊🔥🌪️🌍
Winx Club/	🧚‍♀️🌸🦋🏰
Totally Spies!/	🕵️‍♀️👧🔍🌆
Kim Possible/	🥷🧑‍🦰🦸‍♀️📱
Lilo & Stitch/	👽🏝️👧🐶
The Fairly OddParents/	🧚‍♂️👦🧚‍♀️🏠
SpongeBob SquarePants/	🍍🧽🌊😂
Jimmy Neutron/	🧠👦🚀🔬
Danny Phantom/	👻👦🕵️‍♂️🌆
My Life as a Teenage Robot/	🤖👧🌆🔧
The Wild Thornberrys/	🦁🌍🚐👨‍👩‍👧‍👦
Rugrats/	👶🍼🏠😂
Hey Arnold!/	🏫👦🏠😂
Rocko's Modern Life/	🐨🏠😂🌆
Invader Zim/	👽🌆😂🔍
The Angry Beavers/	🦫🏠😂🌲
CatDog/	🐱🐶🏠😂
Rocket Power/	🛹🏄‍♂️🏄‍♀️🌆
As Told by Ginger/	👧🏫🏠😂
Invader Zim/	👽🌆😂🔍''')  

with open('guessgameN.txt', 'w', encoding='utf-8') as N:
    N.write('''Stranger Things/	👽🧒🔬🏠
The Witcher/	⚔️🧙‍♂️🐺👑
Money Heist/	💰🎭🔫🏦
Bridgerton/	👗💑🏰💌
The Crown/	👑🇬🇧📜🏛️
Narcos/	💊💵🔫🇨🇴
Black Mirror/	📺🧠🤖🌐
Ozark/	💵🔫🌲🏞️
The Umbrella Academy/	☂️🦸‍♂️🦸‍♀️🕰️
13 Reasons Why/	🎧📓💔🕵️‍♂️
Dark/	🕰️🔄🌌🇩🇪
Lucifer/	😈👨‍⚖️🔥🌆
The Queen's Gambit/	♟️👩‍🦰🧠🏆
You/	📚🔪🕵️‍♂️❤️
The Haunting of Hill House/	🏚️👻😱🛌
Emily in Paris/	👗🗼💌🇫🇷
The Mandalorian/	🚀👽🛡️👶
The Office/	🏢😂📄👔
Breaking Bad/	💊🔬🔫🚙
The Walking Dead/	🧟‍♂️🔫🏞️🚶‍♂️
House of Cards/	🏛️🃏🔪🇺🇸
Bojack Horseman/	🐴🍷🎬😂
The Good Place/	😇👿🏞️😂
Schitt's Creek/	🏘️😂💵👨‍👩‍👦
The Great British Bake Off/	🍰🇬🇧👩‍🍳🏆
The Last Kingdom/	⚔️👑🏰🇬🇧
Peaky Blinders/	🧢🔫🏙️🇬🇧
Stranger Things/	👽🧒🔬🏠
The Dragon Prince/	🐉👑🧙‍♂️🌌
The Chilling Adventures of Sabrina/	🧙‍♀️🔮👻🌑
The Dragon Prince/	🐉👑🧙‍♂️🌌
The Crown/	👑🇬🇧📜🏛️
The Stranger/	🕵️‍♂️🔍🏡🕵️‍♀️
The Society/	🏘️🧑‍🤝‍🧑🔍🌍
The Politician/	🏛️🎭🗳️🇺🇸
The OA/	👁️🌌🧠🔄
The Punisher/	🔫💀🛡️🇺🇸
The Rain/	🌧️🧟‍♂️🔬🏞️
The Spy/	🕵️‍♂️🇮🇱🔍🔫
The Umbrella Academy/	☂️🦸‍♂️🦸‍♀️🕰️
The Witcher/	⚔️🧙‍♂️🐺👑
The 100/	🚀🌍🧑‍🤝‍🧑🔄
The 4400/	👽🧑‍🤝‍🧑🔄🌌
The Alienist/	🕵️‍♂️🔍🧠🔪
The Boys/	🦸‍♂️🦸‍♀️🔪💥
The Expanse/	🚀🌌🧑‍🤝‍🧑🔄
The Flash/	⚡🦸‍♂️🏃‍♂️🔄
The Good Doctor/	🏥🧑‍⚕️🧠❤️
The Handmaid's Tale/	👩‍🦰🧑‍⚕️🔴🏛️
The Innocents/	🧑‍🤝‍🧑🔄🏞️🔍''')  

with open('guessgamest.txt', 'w', encoding='utf-8') as spacetoon:
    spacetoon.write('''Detective Conan/	🕵️‍♂️🔍🧠💼
Captain Tsubasa/	⚽🏆🇯🇵👟
Dragon Ball Z/	🐉👊💥🌌
Naruto/	🥷🍥🔥🌪️
One Piece/	🏴‍☠️🌊👒⚓
Digimon Adventure/	🐉🌐👾🧒
Hunter x Hunter/	🏹🧒🌲👊
Beyblade/	🌀⚔️🏆👦
Slam Dunk/	🏀⛹️‍♂️🏆🇯🇵
Inazuma Eleven/	⚽⚡🏆👟
Pokemon/	🐉⚡🎮🔍
Doraemon/	🐱🕰️🧒🔧
Tom and Jerry/	🐱🐭😂🏠
The Adventures of Tintin/	🕵️‍♂️🌍🚢🔍
The Smurfs/	👨‍👩‍👧‍👦🏞️🔵🍄
The Flintstones/	🦕🏠👨‍👩‍👧‍👦🚗
The Jetsons/	🚀🏠👨‍👩‍👧‍👦🤖
Looney Tunes/	🐰🦆😂🎬
Scooby-Doo/	🐶🕵️‍♂️👻🚐
The Powerpuff Girls/	👧👧👧💥🌆
Johnny Bravo/	💪🕶️😂👱‍♂️
Dexter's Laboratory/	🧪🔬👨‍🔬🏠
Samurai Jack/	🥷⚔️🌌👊
Courage the Cowardly Dog/	🐶😱👻🏠
Ed, Edd n Eddy/	😂🏠👦🍬
The Grim Adventures of Billy & Mandy/	💀👦👧😂
Codename: Kids Next Door/	🧒🕵️‍♂️🌍🔍
Foster's Home for Imaginary Friends/	🏠👻👫🎨
Ben 10/	👦👽🛡️🔄
Teen Titans/	🦸‍♂️🦸‍♀️🌆💥
Avatar: The Last Airbender/	🌊🔥🌪️🌍
Winx Club/	🧚‍♀️🌸🦋🏰
Totally Spies!/	🕵️‍♀️👧🔍🌆
Kim Possible/	🥷🧑‍🦰🦸‍♀️📱
Lilo & Stitch/	👽🏝️👧🐶
The Fairly OddParents/	🧚‍♂️👦🧚‍♀️🏠
SpongeBob SquarePants/	🍍🧽🌊😂
Jimmy Neutron/	🧠👦🚀🔬
Danny Phantom/	👻👦🕵️‍♂️🌆
My Life as a Teenage Robot/	🤖👧🌆🔧
The Wild Thornberrys/	🦁🌍🚐👨‍👩‍👧‍👦
Rugrats/	👶🍼🏠😂
Hey Arnold!/	🏫👦🏠😂
Rocko's Modern Life/	🐨🏠😂🌆
Invader Zim/	👽🌆😂🔍
The Angry Beavers/	🦫🏠😂🌲
CatDog/	🐱🐶🏠😂
Rocket Power/	🛹🏄‍♂️🏄‍♀️🌆
As Told by Ginger/	👧🏫🏠😂''')  
 

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
    value = st.text_input("Your Guess")
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
            st.write(f"wrong 😓   ({st.session_state['name'][-1]}) is the right answer")
        
        # add the next name to appear immedietly
        st.session_state['name'].append(name.lower())    


def match_selection():
    '''Retrieve the show data (name, emojies)'''
    # store the selection choice and match it with the same category
    selection = st.segmented_control('',  ["Netflix series", "Disney", "Spacetoon", "MBC3", "Cartoon Network"])

    match selection:
        case "Netflix series":
            launch_game("guessgameN.txt")
  
        case "Disney":
            launch_game("guessgameDisney.txt")  
    
        case "Spacetoon":
            launch_game("guessgamest.txt") 

        case "MBC3":
            launch_game("guessgameMBC3.txt")                   

        case "Cartoon Network":
            launch_game("guessgameCN.txt")     

# main code
st.set_page_config("Guess The Show By Emoji", "✨", layout="wide")
st.header("Guess Game Emoji", divider='blue')
st.subheader("Choose a Category", divider='red')
st.subheader("Based on the Emojies Bellow .. Guess The Name Of The Show")
match_selection()
st.subheader("", divider='blue')
