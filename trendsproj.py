import pandas as pd
import xlsxwriter

geodata= pd.read_csv('geoMap.csv')
timedata= pd.read_csv('multiTimeline.csv')

#weeee cleansing and shit
geodata=geodata.fillna(0)
timedata=timedata.fillna(0)
timedata=timedata.replace('<1',0)
column=timedata.columns
for string in column:
    if(string!='Week'):
        timedata[string] = timedata[string].astype(int)

time = timedata.iloc[:,:].values
geo = geodata.iloc[:,:].values

#Slicing all the searches which were >1.
res=[]
var1=len(time[0])
for i in range(0,52):
    day=time[i, :]
    lis=[]
    for j in range(1,var1):
        if(day[j]>15):  
            lis.append(j)
            
    res.append(lis)
   

# Comparing all the >1 searches and considering the max
doublefucks=[]
var2=len(geo)
for i in res:
    fin=[]
    fuck=[]
    for j in i:
        if not fin:
            for curr in range(0,var2):
                fin.append(geo[curr,j])
                fuck.append(j)
        else:   
             for curr in range(0,var2):
                if(fin[curr]<geo[curr,j]):
                    fin[curr]=geo[curr,j]
                    fuck[curr]=j
        
    doublefucks.append(fuck)
   
#Now it is gonna make sense... kagebushino jutsu 
columns=geodata.columns       
finalfucks=[]    
for i in doublefucks:
    somemorefucks=[]
    for j in i:
        somemorefucks.append(columns[j])
    finalfucks.append(somemorefucks)
    
    
#Writting it in excel
with xlsxwriter.Workbook('test.xlsx') as workbook:    
    worksheet = workbook.add_worksheet()
    
    for row_num, data in enumerate(finalfucks):
        worksheet.write_row(row_num, 0, data)
    
    
    
    
    
    