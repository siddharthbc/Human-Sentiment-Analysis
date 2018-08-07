
import http.client,urllib.request, urllib.parse, urllib.error, base64, sys
import time
import pyodbc
import json

con = pyodbc.connect("DRIVER={SQL Server};server=LAPTOP-411L5QR0\SIDDHU;database=Lied;uid=sa;pwd=siddhu")
cursor = con.cursor()
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'd55a5a67b2584bb180178d3b2b33b314',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = []
conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')

for i in range(382, 461):
    frame = 'frame' + str(i) +'.jpg'
    path = r'C:\Users\Siddharth\Desktop\Python Programs\data\\' + frame

    try:

        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, open(path,'rb').read(), headers)
        response = conn.getresponse()
        data = response.read()
        dataf = json.loads(data, encoding='utf-8')
        x = json.dumps(dataf)
        data = json.loads(x)
        print(str(i+1))
        print(data)
        cursor.execute("INSERT INTO Table_4(fno, anger, contempt, disgust, fear, happiness, neutral, sadness, surprise) VALUES (?,?,?,?,?,?,?,?,?)", str(i), str(data[0]['scores']['anger']), str(data[0]['scores']['contempt']),str(data[0]['scores']['disgust']),str(data[0]['scores']['fear']),str(data[0]['scores']['happiness']),str(data[0]['scores']['neutral']),str(data[0]['scores']['sadness']),str(data[0]['scores']['surprise']))

        if(i%19 == 0 and i != 0):
            time.sleep(65)

    except Exception as e:
        print(e.args)

conn.close()
con.commit()
con.close()