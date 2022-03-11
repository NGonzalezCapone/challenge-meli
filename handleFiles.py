import requests
import json
import io

bearer_token= "ya29.A0ARrdaM88fxt2LD1HzCtj5ltNbFndxaRamT-ilr8-6tZr146pVPt_eP-h_E2GbEt1nHu7pi1MQAA-Wn3DIqKkLM5qv_a2kzefP2ScQKFbs_kcyaxjU5lRJeBeSuZ8osMxjv7gnYTyFVgGFjCPEKZO5q6WuO3D7A"  

class HandleFiles:
    def __init__(self):
        self.headers={"Authorization": "Bearer {}".format(bearer_token)}

    def searchWord(self,fileId,word):
        response1 = self.fileExists(fileId)
        if(not response1):
            print(response1)
            return response1
        else:
            response = requests.get(
                'https://www.googleapis.com/drive/v3/files?q=fullText%20contains%20%27{palabra}%27'.format(palabra=word),
                headers=self.headers)
            archivos = response.json()
            for archivo in archivos['files']:
                if archivo['id'] == fileId:
                    print(response)
                    return response
            print("Existe el archivo pero no contiene la palabra buscada")
            return 0
    
    def fileExists(self,fileId):
        response = requests.get(
                'https://www.googleapis.com/drive/v3/files/{}'.format(fileId),
                headers=self.headers)
        return response
              
    def createFile(self,name,description):
            para = {
                "name": name,
                "description" : description
            }
            files = {
                'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            }
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=self.headers,
                files=files)

            information = r.json()
            print(r)
            print('id: %s' % information['id'], 'titulo: %s' % name, 'description: %s' % description)
            return information['id'], r

    def deleteFile(self,fileId):
        response1 = self.fileExists(fileId)
        if(not response1):
            print(response1)
            return 0
        else:
            r = requests.delete('https://www.googleapis.com/drive/v3/files/{}'.format(fileId),
            headers=self.headers)
            print(r)
            return r

    def createFileWithText(self,name,description,text):
            para = {
                "name": name,
                "description" : description,
                "mimeType": "application/vnd.google-apps.document"
            }
            files = {
                'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': ('file', io.BytesIO(text.encode('utf-8')), 'text/plain')
            }
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=self.headers,
                files=files)

            information = r.json()
            print(r)
            print('id: %s' % information['id'], 'titulo: %s' % name, 'description: %s' % description)
            return information['id'], r
            

        

        

