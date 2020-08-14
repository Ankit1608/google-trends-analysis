import bpy
import csv
with open('Users/mac/Desktop/TrendsProject/2018/2018.csv') as f:
    zdata=list(csv.reader(f))

with open('Users/mac/Desktop/TrendsProject/2018/color.csv') as f:
    color=list(csv.reader(f))
color[0][0]='Bahubali 2'
temp=0
states=zdata[0][1:]
tempdata=zdata[1:]
for i in tempdata:
    i=i[1:]
    for j in range(0,31):
        for k in color:
            if(i[j]==k[0]):
                obj1=bpy.data.objects[states[j]]
                bpy.context.view_layer.objects.active = obj1
                obj2=bpy.context.object.active_material
                obj2.diffuse_color=(float(k[1])/255,float(k[2])/255,float(k[3])/255,1)
                obj2.keyframe_insert(data_path="diffuse_color", frame=temp)
                obj2.keyframe_insert(data_path="diffuse_color", frame=temp+23)                
    temp=temp+28
