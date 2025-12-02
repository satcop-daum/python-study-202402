################################################################################
# pip install youtube-transcript-api
# pip install openpyxl
################################################################################

import re
import time

import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

################################################################################
def get_youtube_text(video_id):

    result = {
        'is_success': True,
        'text': '',
        'error_message': ''
    }

    try:
        transcript_list = YouTubeTranscriptApi().list(video_id)

        try:
            transcript = transcript_list.find_transcript(['ko'])
        except Exception:
            transcript = transcript_list.find_transcript(['en', 'a.en'])

        fetched_transcript = transcript.fetch()
        formatter = TextFormatter()
        result['text'] = formatter.format_transcript(fetched_transcript)

    except Exception as e:
        #print(f"오류가 발생했습니다: {e}")
        #print("해당 동영상에 접근 가능한 자막이 없거나, 동영상 ID가 잘못되었을 수 있습니다.")
        result['is_success'] = False
        result['error_message'] = str(e)

    return result
#end-def
################################################################################

################################################################################
def get_video_id(youtube_url):
    match = re.search(r"v=([^&]+)", youtube_url)
    return match.group(1) if match else None
#end-def
################################################################################

def main():
    df = pd.read_excel('./youtube.xlsx')
    df = df.astype({"자막": "object", "결과": "object", "에러메시지": "object"}, )

    for index, r in df.iterrows():
        youtube_url = r['유튜브_URL']
        video_id = get_video_id(youtube_url)
        result = get_youtube_text(video_id)

        df.at[index, '자막'] = result['text']
        df.at[index, '결과'] = result['is_success']
        df.at[index, '에러메시지'] = result['error_message']

        time.sleep(0.5)

    df.to_excel('./youtube_result.xlsx', index=False)

if __name__ == "__main__":
    main()
