from kalah import Kalah

import streamlit as st
from PIL import Image, ImageDraw, ImageFont


if "game" not in st.session_state:
    st.session_state.game = Kalah(6, 2)
    st.session_state.name_one = ""
    st.session_state.name_two = ""

game = st.session_state.game





def draw_board(game):
    WIDTH, HEIGHT = 800, 400
    HOLE_RADIUS = 40
    HOME_WIDTH, HOME_HEIGHT = 70, 200

    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 30)

    # holes places
    holes_p1 = [(150 + i * 100, 250) for i in range(game.holes)]
    holes_p2 = [(650 - i * 100, 100) for i in range(game.holes)]
    home_p2 = (20, 100)
    home_p1 = (700, 100)

    # draw holes
    for i, (x, y) in enumerate(holes_p1):
        draw.ellipse([x - HOLE_RADIUS, y - HOLE_RADIUS, x + HOLE_RADIUS, y + HOLE_RADIUS], fill="lightgray", outline="black")
        draw.text((x - 10, y - 10), str(game.kalah[i]),font=font ,  fill="blue")

    for i, (x, y) in enumerate(holes_p2):
        draw.ellipse([x - HOLE_RADIUS, y - HOLE_RADIUS, x + HOLE_RADIUS, y + HOLE_RADIUS], fill="lightgray", outline="black")
        draw.text((x - 10, y - 10), str(game.kalah[game.holes + 1 + i]),font=font ,  fill="blue")

    # dram houses
    draw.rectangle([home_p1[0], home_p1[1], home_p1[0] + HOME_WIDTH, home_p1[1] + HOME_HEIGHT], fill="gray", outline="black")
    draw.text((home_p1[0] + 20, home_p1[1] + 80), str(game.kalah[game.player_one_home]),font=font , fill="black")

    draw.rectangle([home_p2[0], home_p2[1], home_p2[0] + HOME_WIDTH, home_p2[1] + HOME_HEIGHT], fill="gray", outline="black")
    draw.text((home_p2[0] + 20, home_p2[1] + 80), str(game.kalah[game.player_two_home]),font=font , fill="black")

    return img





# check if is already send
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if not st.session_state.form_submitted:
    with st.form("my_form"):
        st.title("Register")
        name_one = st.text_input("Name first player")
        name_two_w = st.text_input("Name second player")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state.name_one = name_one
            st.session_state.name_two = name_two_w
            st.session_state.form_submitted = True
            st.rerun()  # refresh to show just needed form
else:
    if not game.done():
        st.markdown("<h1 style='text-align: center; color: #b38b00;'>Kalah Game</h1>",
                    unsafe_allow_html=True)
        st.markdown(
            f"<h1 style='text-align: center; color: #b38b00;'> player {st.session_state.name_one if game.curr_player else st.session_state.name_two}</h1>",
            unsafe_allow_html=True)

        # ✅ save img and show
        img = draw_board(game)
        img.save("board.png")
        st.image("board.png", use_container_width =True)


        # ✅ יצירת כפתורים לחורים החוקיים
        # col1, col2 = st.columns(2)
        # for i in range(game.holes):
        #     if game.curr_player == 0 and game.kalah[i] > 0:
        #         if col1.button(f"Move {i+1}", key=f"p1_{i}"):
        #             game.play(i)
        #             st.rerun()
        #     if game.curr_player == 1 and game.kalah[game.holes + 1 + i] > 0:
        #         if col2.button(f"Move {i+1}", key=f"p2_{i}"):
        #             game.play(game.holes + 1 + i)
        #             st.rerun()
        cols = st.columns(game.holes)  # יצירת עמודות כמספר החורים

        for i in range(game.holes):
            if game.curr_player == 0:
                disabled = game.kalah[i] == 0  # אם אין זרעים בחור, הכפתור יהיה מושבת
                with cols[i]:  # מציגים את הכפתור בעמודה המתאימה
                    if st.button(f"{game.kalah[i]}", key=f"p1_{i}", disabled=disabled):
                        game.play(i)
                        st.rerun()

        for i in range(game.holes):
            if game.curr_player == 1:
                hole_index = len(game.kalah) - i -2# game.holes + 1 + i
                disabled = game.kalah[hole_index] == 0
                with cols[i]:
                    if st.button(f"{game.kalah[hole_index]}", key=f"p2_{i}", disabled=disabled):
                        game.play(hole_index)
                        st.rerun()

    else:
        st.markdown(f"<h1 style='text-align: center; color: #b38b00;'>we have a winner \n {game.winner}</h1>",
                        unsafe_allow_html=True)