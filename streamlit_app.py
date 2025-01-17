"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.write("""<html>
    <h1>hello</h1>

            
</html>""", unsafe_allow_html=True)


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

    
    
    st.write("""<style> 

            
            .css-ffhzg2 {
    background: linear-gradient(270deg, #094883, #4b0f94);
    background-size: 400% 400%;

    -webkit-animation: gradientbackground 20s ease infinite;
    -moz-animation: gradientbackground 20s ease infinite;
    animation: gradientbackground 20s ease infinite;
}

@-webkit-keyframes gradientbackground {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}
@-moz-keyframes gradientbackground {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}
@keyframes gradientbackground {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}
            
        .css-1hynsf2 { 
            filter: drop-shadow(5px 5px 28px #BC2E2E);
            width: 100%;
            border-radius: 25px;
            }
            
        .css-1hynsf2:hover { 
            filter: drop-shadow(5px 5px 28px #fff);
            }
            
        p { 
            color: black;
            font-size: 2rem;
            }
            
        .stSlider {
            width: auto;
            outline: 5px;
            outline: groove;
            outline-width: 5px;
            padding-inline: 25px;            
            }
            
         .marks { 
            border-radius: 25px;
            }
            
</style>""", unsafe_allow_html=True)
