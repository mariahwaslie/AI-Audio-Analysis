import ffmpeg


# Define the M3U8 file and the output MP3 file
m3u8_file = 'a.m3u8'
mp3_file = 'a.mp3'

# Open the M3U8 file and read its contents
with open(m3u8_file, 'r') as file:
    m3u8_contents = file.read()

# Extract the first video stream URL
video_url = m3u8_contents.splitlines()[2]

# Use ffmpeg to extract the audio from the video stream and convert it to MP3
ffmpeg.input(video_url).output(mp3_file, vn=0).run()