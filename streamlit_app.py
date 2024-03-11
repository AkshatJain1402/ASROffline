#start
import streamlit as st
col1,col2 ,col3=st.columns(3)

with st.container():
    
    st.title("Customer Care")
    st.image("UI.jpg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with col1:
        st.header("streaming ASR")
        st.image("https://static.streamlit.io/examples/cat.jpg")

        
        clicked=st.button("Click me for translation",key="my_btn")
    with col2:
        st.header("offline ASR")
        st.file_uploader("upload your recording ", type=None, accept_multiple_files=False, key=None,  on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        clicked=st.button("Click me for translation",key="my_btn")
    with col3:
        st.header('Results')
        text_contents="the results "
        st.write(text_contents)

        st.download_button("your transcription",text_contents, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)




       








