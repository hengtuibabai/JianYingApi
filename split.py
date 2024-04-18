# -*- coding: utf-8 -*-
# -------------------------------

# @软件：PyCharm
# @PyCharm：自行填入你的版本号
# @Python：自行填入你的版本号
# @项目：JianYingApi

# -------------------------------

# @文件：split.py
# @时间：2024/4/18 16:26
# @作者：你的名称/当然你也可以使用命令获取计算机账户名称
# @邮箱：你的邮箱账号

# -------------------------------
from scenedetect import detect, ContentDetector
import JianYingApi, uuid
# import datetime


d = JianYingApi.Drafts.Create_New_Drafts(r"d:\JianyingPro Drafts/PulpFiction2") # Create New Project

# prepare video materials

scene_list = detect('datas/t60.mp4', ContentDetector())
print(scene_list)

video_track = d.Content.NewTrack(TrackType="video")
video_path = r"d:/work2/JianYings/JianYingApi/datas/t60.mp4"

for i, scene in enumerate(scene_list):
    print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
        i+1,
        scene[0].get_timecode(), scene[0].get_frames(),
        scene[1].get_timecode(), scene[1].get_frames(),))

    str_micro_second_time_from = int(scene[0].get_seconds() * 1000_000)
    print(str_micro_second_time_from)

    str_micro_second_time_to = int(scene[1].get_seconds() * 1000_000)
    print(str_micro_second_time_to)


    video_name = "test-v-" + str(i)
    video_material_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=video_name + "_material"))
    video_track_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=video_name + "_track"))
    d.Meta.Import2Lib(path=video_path, metetype="video")
    d.Content.AddMaterial(Mtype="videos", Content={"category_name": "local", "extra_type_option": 0,
                                                   "has_audio": True, "id": video_material_id,
                                                   "material_name": video_name, "path": video_path, "type": "video"})
    d.Content.Add2Track(Track_id=video_track["id"], Content=
    {
        "id": video_track_id,
        "material_id": video_material_id,
        "visible": True,
        "volume": 1,
        "source_timerange": {
            "duration": str_micro_second_time_to - str_micro_second_time_from,
            "start": str_micro_second_time_from
        },
        "target_timerange": {
            "duration": str_micro_second_time_to - str_micro_second_time_from,
            "start": str_micro_second_time_from
        }
    })

d.Save()
