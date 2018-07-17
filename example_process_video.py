import json

from pigeon_tracker.tracker import ColorTracker

lower_red = (170, 100, 100)
upper_red = (180, 255, 255)

t = ColorTracker(lower_red, upper_red)
# t.hsv = False
# t.original = False
# t.tracking_mask = False

video_list = ['a.mp4', 'b.mp4']

result = t.track_video('/home/kiview/Videos/GOPR0645.mp4', 900)


result_json = json.dumps(result)
with open("result.json", "w") as text_file:
    print(result_json, file=text_file)
