import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date

# Set page configuration
st.set_page_config(page_title="Meine Hundedaten", page_icon="🐕", layout="wide")

st.title("App zum Sammeln von Daten der Hunde")



st.subheader('1. Hund - Flips')

data_df = pd.DataFrame(
    {
        "Tierarzt": [
            datetime(2024, 5, 5, 15, 30),
            datetime(2024, 6, 12, 4, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "Tierarzt": st.column_config.DatetimeColumn(
            "Tiierarzt",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)


st.subheader('2. Hund - Luna')

data_df = pd.DataFrame(
    {
        "Tierarzt": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2024, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "Tierarzt": st.column_config.DatetimeColumn(
            "Tierarzt",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)

st.subheader('Gewicht Hunde')
df = pd.DataFrame(
    [
       {"Gewicht": "02.02.2024", "Kilogramm": 3, "Zielgewicht über 3 Kilogramm": True},
       {"Gewicht": "06.04.2024", "Kilogramm": 3.1, "Zielgewicht über 3 Kilogramm": True},
       {"Gewicht": "10.02.2024", "Kilogramm": 2.9, "Zielgewicht über 3 Kilogramm": False},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["Kilogramm"].idxmax()]["Gewicht"]
st.markdown(f"Dieses Gewicht gefällt mir am meisten  **{favorite_command}** 🥳")


st.subheader('Gewicht Flips und Luna')
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Flips", "Luna"])
st.line_chart(chart_data)

st.subheader('Geburtstage')
d = st.date_input("Geburtstag Flips", datetime(2014, 3, 9))
st.write('Flips Geburtstag ist am:', d)

d = st.date_input("Geburtstag Luna", datetime(2012, 3, 5))
st.write('Lunas Geburtstag ist am:', d)


add_selectbox = st.sidebar.selectbox(
    "Gewicht Hunde",
    ("2022", "2023", "2024")
)


st.subheader('Notfallnummer')
st.write('Im Notfall folgende, *Nummer!*, wählen :dog:')

container = st.container(border=True)
container.write("Notfallnummer: Tierarzt......, Tierspital.......")
st.write("Meine Nummer........")

if 'x' not in st.session_state:
    st.session_state['x'] = 0
button = st.button('increment X by 1')

if button:
    st.session_state['x'] += 1

st.write('x', st.session_state['x'])
