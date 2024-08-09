import streamlit as st



def hindiPoem():
    st.markdown("<h3>Agnipath</h3>", unsafe_allow_html=True)
    paragraph = """
        वृक्ष हों भले खड़े,<br>
        हो घने, हो बड़े,<br>
        एक पत्र छाँह भी,<br>
        माँग मत, माँग मत, माँग मत,<br>
        अग्निपथ, अग्निपथ, अग्निपथ।

        """
    return st.markdown(f"<p style='color:#393232;'>{paragraph}", unsafe_allow_html=True)