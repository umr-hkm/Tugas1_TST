import json
from fastapi import FastAPI

with open("data_mhs.json", "r") as read_file:
    data = json.load(read_file)

app = FastAPI()

@app.get('/')
def homepage():
    return "halo"

@app.get('/mahasiswa/{NIM}')
def read_mahasiswa(NIM: str):
    for mahasiswa in data['mahasiswa']:
        if mahasiswa['NIM'] == NIM:
            return mahasiswa
    return {"Data" : "NotFound"}