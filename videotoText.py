import json
from watson_developer_cloud import SpeechToTextV1

IBM_USERNAME = "f8a510b7-b3a1-40fe-87fd-6dff5a28542c"
IBM_PASSWORD = "PXLVTwbRKecY"

stt = SpeechToTextV1(username=IBM_USERNAME, password=IBM_PASSWORD)
audio_file = open(r"C:\Users\Siddharth\Music\Dateline Special Interview with Britney Spears _ Part 02_2.mp3", "rb")


with open('transcript_result.json', 'w') as fp:
    result = stt.recognize(audio_file, content_type="audio/x-flac",
                           continuous=True, timestamps=False,
                           max_alternatives=1)
    json.dump(result, fp, indent=2)
    print(result)