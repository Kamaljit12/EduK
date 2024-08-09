import streamlit as st



def EnglishPoem():
    st.title("The Road Not Taken")
    paragraph = """
    Two roads diverged in a yellow wood,
    And sorry I could not travel both,
    And be one traveler, long I stood,
    And looked down one as far as I could,
    To where it bent in the undergrowth;,

    Then took the other, as just as fair,
    And having perhaps the better claim,
    Because it was grassy and wanted wear;
    Though as for that the passing there,
    Had worn them really about the same,

    And both that morning equally lay,
    In leaves no step had trodden black.,
    Oh I kept the first for another day!,
    Yet knowing how way leads on to way,
    I doubted if I should ever come back.,

    I shall be telling th...
    """
    for row in paragraph.split(','):
        # rows =  st.markdown(f"<p>{row}</p>", unsafe_allow_html=True)
        row = st.text(row)
        row
    # Add a video from a URL
    st.title("This is the video of this poem")
    # Or add a video from a local file
    with open("videos/_The Road Not Taken_ by Robert Frost.mp4", "rb") as video_file:
        st.video(video_file.read())