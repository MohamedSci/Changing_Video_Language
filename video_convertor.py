# -*- coding: utf-8 -*-
"""Video_Convertor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PXJ5B9YvtIsyQTUWaXjTtF7x3vYebxZh

**Extracting audio from a video file using Python, you can use the moviepy library. **
"""

pip install moviepy

from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to a new file
    audio_clip.write_audiofile(output_audio_path, codec='mp3')  # You can choose the desired audio codec

    # Close the clips
    video_clip.close()
    audio_clip.close()

# Replace 'input_video.mp4' and 'output_audio.mp3' with your video and desired audio file paths
input_video_path = 'input_video.mp4'
output_audio_path = 'output_audio.mp3'

extract_audio(input_video_path, output_audio_path)

print(f"Audio extracted from video and saved to {output_audio_path}")

"""**Converting an audio file to a transcript text file using Python, you can leverage the SpeechRecognition library, which supports several ASR engines, including Google Web Speech API.**"""

pip install SpeechRecognition

import speech_recognition as sr

def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    # Load the audio file
    audio_file = sr.AudioFile(audio_file_path)

    # Use the Google Web Speech API for transcription
    with audio_file as source:
        audio_data = recognizer.record(source)

    try:
        # Use Google Web Speech API to transcribe the audio
        text_result = recognizer.recognize_google(audio_data)
        return text_result
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

    return None

# Replace 'path/to/your/audio/file.wav' with the path to your audio file
audio_path = 'path/to/your/audio/file.wav'
transcript = audio_to_text(audio_path)

if transcript:
    # Save the transcript to a text file
    with open('transcript.txt', 'w') as file:
        file.write(transcript)
    print("Transcription successful. Text saved to transcript.txt.")
else:
    print("Transcription failed.")

"""***Converting an Arabic transcript text file to an MP3 audio file using Python, you can use the gTTS (Google Text-to-Speech) library.***"""

pip install gtts

from gtts import gTTS

def text_to_audio(text, output_file):
    # Language parameter is set to 'ar' for Arabic
    tts = gTTS(text=text, lang='ar')

    # Save the generated audio to a file
    tts.save(output_file)

# Replace 'input_text.txt' with the path to your Arabic transcript text file
input_text_file = 'input_text.txt'
output_audio_file = 'output_audio.mp3'

# Read the Arabic text from the file
with open(input_text_file, 'r', encoding='utf-8') as file:
    arabic_text = file.read()

# Convert Arabic text to MP3 audio
text_to_audio(arabic_text, output_audio_file)

print(f"Audio file saved to {output_audio_file}")

"""** Replacing the original audio in a video file with an external audio file using Python, you can use the moviepy library. **"""

pip install moviepy

from moviepy.editor import VideoFileClip, AudioFileClip

def replace_audio(video_path, audio_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the external audio clip
    audio_clip = AudioFileClip(audio_path)

    # Set the video clip's audio to the external audio
    video_clip = video_clip.set_audio(audio_clip)

    # Write the result to a new file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Close the clips
    video_clip.close()
    audio_clip.close()

# Replace 'input_video.mp4', 'input_audio.mp3' with your video and audio file paths
input_video_path = 'input_video.mp4'
input_audio_path = 'input_audio.mp3'
output_video_path = 'output_video_with_external_audio.mp4'

replace_audio(input_video_path, input_audio_path, output_video_path)

print(f"Video with external audio saved to {output_video_path}")