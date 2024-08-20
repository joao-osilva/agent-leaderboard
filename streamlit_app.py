import streamlit as st

leaderboard_pg = st.Page("leaderboard.py", title="Leaderboard", icon=":material/leaderboard:")
submit_agent_pg = st.Page("submit_agent.py", title="Submit New", icon=":material/add:")
search_agent = st.Page("search_agents.py", title="Find Agents", icon=":material/search:")

pg = st.navigation([leaderboard_pg, submit_agent_pg, search_agent])

st.set_page_config(page_title="Leaderboard", page_icon=":material/leaderboard:")

st.title("Welcome to AI agents leaderboard!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


pg.run()
