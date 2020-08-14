import bpy
import csv
with open('Users/mac/Desktop/TrendsProject/2018/2018.csv') as f:
    zdata=list(csv.reader(f))

states=zdata[0][1:]
def my_handler(scene):
    frame_curr=bpy.context.scene.frame_current
    k=int(frame_curr/28)
    names=zdata[k+1][1:]
    for i in range(0,31):
        text=bpy.data.objects['T'+str(states[i])]
        text.data.body=str(names[i])

def register():
    bpy.app.handlers.frame_change_post.append(my_handler)    

def unregister():
    bpy.app.handlers.frame_change_post.remove(my_handler)

register()
