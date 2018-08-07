import pyodbc
from re import search
import requests
import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
  version='2016-05-19',
  username='097b33ba-77e7-444d-8785-addd599916ea',
  password='kqeMMTBN3uxb'
)

data1 = json.dumps(tone_analyzer.tone(text='NO, NO We are happy together right now'), indent=2)
datar = json.loads(data1, encoding='utf-8')
x = json.dumps(datar)
data1 = json.loads(x)
print(data1)

r1 = max(data1['document_tone']['tone_categories'][0]['tones'][0]['score'],data1['document_tone']['tone_categories'][0]['tones'][1]['score'],data1['document_tone']['tone_categories'][0]['tones'][2]['score'],data1['document_tone']['tone_categories'][0]['tones'][3]['score'],data1['document_tone']['tone_categories'][0]['tones'][4]['score'])

print(r1)
for i in range(0,4):
      if( float(r1)== float(data1['document_tone']['tone_categories'][0]['tones'][i]['score'])):
         print("The Emotion recognised Words : "+str(data1['document_tone']['tone_categories'][0]['tones'][i]['tone_id']))

con = pyodbc.connect("DRIVER={SQL Server};server=LAPTOP-411L5QR0\SIDDHU;database=Lied;uid=sa;pwd=siddhu")
cursor = con.cursor()

cursor.execute("select * from Table_2")
row = cursor.fetchone()
inf = cursor.fetchone()
rows = cursor.fetchall()
frameIn = []
k = 0

for row in rows:
        r = max(float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]))
        for i in range(1, 8):
            if(r == float(row[i])):
                column = inf.cursor_description
                print(column[i][0])
                frameIn.append(column[i][0])
                k=k+1



for i in range (0, len(frameIn)-1):

    if(frameIn[i]!=frameIn[i+1]):
        if(frameIn[i+1]!='neutral'):
           print("Red Flag detected ")
           print("Change from "+frameIn[i]+" to "+frameIn[i+1]+" detected at the frame "+str(i))
           print("Compare to real emotion to verify Change")