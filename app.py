#start
import streamlit as st



from streamlit_webrtc import webrtc_streamer, WebRtcMode
def record_audio():
    with st.spinner("Recording..."):
        audio_recorder = webrtc_streamer(
            key="audio-recorder",
            mode=WebRtcMode.AUDIO_RECVONLY,  # Receive audio only 
            audio_receiver_size=256,  # Adjust as needed
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]} 
        )

        while True:
            if audio_recorder.audio_receiver:
                sound_bytes = audio_recorder.audio_receiver.get_frames(timeout=5)
                break  # Exit the loop after recording some audio

    st.success("Recording complete!")
    return sound_bytes  

# Record Button
if st.button("Record Voice"):
    sound_bytes = record_audio()

    # Further processing (Save the audio, display waveform, etc.)
    if sound_bytes:
        st.audio(sound_bytes, format="audio/wav")