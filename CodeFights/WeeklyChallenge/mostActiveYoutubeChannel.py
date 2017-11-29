# https://codefights.com/challenge/nSCSyfZCQemG3rTWf/solutions

# You've been YouTube surfing lately a lot, and after a while noticed that most of
# the videos you've seen so far were posted by the same channel.
# You want to find the most active channel, i.e. the channel that posted the majority of the videos you've seen.
#
# Given videoIDs list representing the unique video identifiers, return the title of the most active channel.
# If there is a tie, return the lexicographically smallest title.
#
# In this task you should use the YouTube Data API.

import urllib.request
import json

def mostActiveYoutubeChannel(videoIDs):
    channel = {}
    active_num = 0
    best_channel = ""
    address = ""
    url_start = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id="
    api_key = "&key={Insert Your API KEY}"
    video_id = ""

    for v in videoIDs:
        address = url_start + v + api_key
        with urllib.request.urlopen(address) as f:
            text = f.read()
            decodetext = text.decode("utf-8")
        text_2_json = json.loads(decodetext)
        channel_title = text_2_json["items"][0]["snippet"]["channelTitle"]
        print(channel_title)
        if channel_title not in channel:
            channel[channel_title] = 1
        else:
            channel[channel_title] += 1
    for c in channel:
        if channel[c] > active_num:
            active_num = channel[c]
            best_channel = c
        if channel[c] == active_num:
            if len(best_channel) > 0 and c[0] < best_channel[0]:
                best_channel = c
    return best_channel
