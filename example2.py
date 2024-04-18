import JianYingApi  , uuid


#########Step1 新建视频项目

# d = JianYingApi.Drafts.Create_New_Drafts(r"d:\JianyingPro Drafts/草稿2") # Create New Project
d = JianYingApi.Drafts.Create_New_Drafts(r"d:\JianyingPro Drafts/PulpFiction2") # Create New Project

# Create Two Tracks
text1_track = d.Content.NewTrack(TrackType="text")
video_track = d.Content.NewTrack(TrackType="video")
efect_track = d.Content.NewTrack(TrackType="effect")

# add text material
text1_material_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name="text1_material"))
text1_track_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name="text1_track"))
d.Content.AddMaterial(Mtype="texts", Content={
    "id": text1_material_id,
    "type": "text",
    "content":   "{\"text\":\"this is a text\",\"styles\":[{\"size\":15,\"fill\":{\"content\":{\"solid\":{\"color\":[1,1,1]}}},\"range\":[0,14]}]}"
})
d.Content.Add2Track(Track_id=text1_track["id"], Content={
    "id": text1_track_id,
    "material_id": text1_material_id,
    "target_timerange": {
        "duration": 200600000,
        "start": 0
    },
})


# Add Video Material
video_path = r"D:\videoshome\test\t.mp4"
video_name = "PulpFiction-v1"
video_material_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=video_name+"_material"))
video_track_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=video_name+"_track"))
d.Meta.Import2Lib(path=video_path,metetype="video")
d.Content.AddMaterial(Mtype="videos",Content={"category_name":"local","extra_type_option":0,
                                              "has_audio":True,"id":video_material_id,
                            "material_name":video_name,"path":video_path,"type":"video"})
d.Content.Add2Track(Track_id=video_track["id"],Content=
        { 
          "id":video_track_id,
          "material_id":video_material_id,
          "visible":True,
          "volume":1,
          "source_timerange": {
            "duration": 605000000,
            "start": 2050633333
          }, "target_timerange": {
            "duration": 605000000,
            "start": 0
          }})

# Add Effects
effect_name = "萤火"
effect_resource_id="7006265184050221576"
effect_id="1357502"

effect_material_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=effect_name+"_material"))
effect_track_id = str(uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=effect_name+"_track"))
d.Content.AddMaterial(Mtype="video_effects",Content=
  {"apply_target_type":2,"effect_id":effect_id,"id":effect_material_id,"name":effect_name,
   "render_index":0,"effect_resource_id":effect_resource_id,"resource_id":effect_resource_id,
   "type":"video_effect","value":1})
d.Content.Add2Track(Track_id=efect_track["id"],Content=
        {
          "id": effect_track_id,
          "material_id": effect_material_id,
          "render_index": 11000,
          "speed": 1,
          "target_timerange": {
            "duration": 500600000,
            "start": 0
          },
          "visible": True,
          "volume": 1
        }
    )
# Save
d.Save()

#########Step2 打开剪映识别
# ins = JianYingApi.Jy_Warp.Instance(JianYing_Exe_Path=r"d:\JianyingPro Drafts")