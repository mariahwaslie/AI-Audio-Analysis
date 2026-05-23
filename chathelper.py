import streamlit as st
from openai import OpenAI
from moviepy.editor import VideoFileClip
from yt_dlp import YoutubeDL
import os
from dotenv import load_dotenv

load_dotenv()
api_key =os.getenv("API")
client = OpenAI(api_key=api_key)

def audio(filename):
    audio_file= open(filename, 'rb')
    transcription =client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
    )

    return transcription.text

def notes(transcription):
    response =client.chat.completions.create(
        model='gpt-3.5-turbo',
        temperature=0,
        messages=[
            {
                'role':'system',
                "content": 'you are a professional tutor, note taker, and researcher trained to create comprehensive notes, guides,and summarizations from video transcripts. I would like you to read the following text create long detailed comprehensive notes and study guide for the following text.'
            },
            {
                'role':'user',
                "content": transcription}

        ]
    )
    return response.choices[0].message.content

def download_youtube_video(url):
    if not url:
        return None

    try:
        download_options = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        with YoutubeDL(download_options) as ydl:
            info = ydl.extract_info(str(url), download=True)
            filename = ydl.prepare_filename(info)

        base, ext = os.path.splitext(filename)
        audio_file = base + ".mp3"
        st.write(f"{info.get('title', 'Video')} has been successfully downloaded as {audio_file}")
        return audio_file
    except Exception as error:
        st.error("Could not download audio from that YouTube URL.")
        st.info("If the error mentions FFmpeg or ffprobe, install FFmpeg and restart Streamlit so your terminal can find it.")
        st.exception(error)
        return None


#extract audio from a video

st.subheader("YouTube Video Notes")
st.write('enter a youtube link ')

with st.chat_message('user'):
    link = st.chat_input('enter url here')

yfile = download_youtube_video(link)
if yfile:
    st.audio(yfile, format='audio/mp3', loop=False)
    transcription = audio(yfile)
    n = notes(transcription)
    st.write(n)

#
# with st.chat_message('ai'):
#     st.write('welcome to chathelper audio analysis\nwhat do you need help with today?\n')
#     st.write('1. Analyze audio/lecture\n2. Draft a Document\n3. Be a personal tutor')
#
# choice = st.selectbox('What do you want to do?', ('Analyze audio/lecture', 'Draft a Document', 'Be a personal tutor'))
# if choice == 'Analyze audio/lecture':
# with st.chat_message('user'):
# # # st.write('your choice is: ' + str(choice))
# #
#     with st.chat_message('ai'):
#         st.write('pick the filetype')
#         filetype = st.selectbox('file type', ('none','mp3', 'mp4'))
#
#         file = st.chat_input('give the file path of the audio file')
#         if file is not None:
#             st.write(str(file))
#
#         if filetype == 'mp3' and file:
#             st.audio(file, format='audio/mp3', loop=False)
#             transcription = audio(file)
#             n = notes(transcription)
#             st.write_stream(n)
#
#         elif filetype == 'mp4' and file:
#             st.video(file, loop=False)
#
#
#             video = VideoFileClip(file)
#             audio = video.audio
#                 # store the audiofile
#             vid_name = file.split('.mp4')[0]
#             audio_file_name = vid_name + '.mp3'
#             audio.write_audiofile(audio_file_name)
#
#             st.write("audio file extraction complete enter  "+audio_file_name+ " \nchoose mp3 filetype and enter the file name")
#
#
#         #
# #
# #
# # while choice == '1':
# #     if 'mp3' in file:
# #         st.audio(file, format='audio/mp3', loop=False)
# #         transcription = audio(file)
# #         n = notes(transcription)
# #         st.write(n)
# #
# #
# #     elif 'mp4' in file:
# #         st.video(file, loop=False)
# #         video = VideoFileClip(file)
# #         audio=video.audio
# #                 #store the audiofile
# #         vid_name = file.split('.mp4')[0]
# #         audio_file_name = vid_name + '.mp3'
# #         audio.write_audiofile(audio_file_name)
# #         video.close()
# #         file = f"{vid_name}.mp3"
#         continue
#
#     else:
#         st.write('file must be mp3')
#         file= st.text_input('enter the file path of the audio file')
#
#
