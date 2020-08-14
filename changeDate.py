import bpy
import csv
with open('Users/mac/Desktop/Blender/DATES.csv') as f:
    dates=list(csv.reader(f))

dates[0][0]='January 2019'
res=[]
for d in dates:
    s=d[0]
    s=s[:-5]
    res.append(s)

def update(scene):
    frame_curr=bpy.context.scene.frame_current
    if(frame_curr==0):
        text=bpy.data.objects['Date']
        text.data.body="1 January"
    else:
        k=int(frame_curr/4)
        text=bpy.data.objects['Date']
        text.data.body=res[k]

def register():
    bpy.app.handlers.frame_change_post.append(update)    

def unregister():
    bpy.app.handlers.frame_change_post.remove(update)

register()
