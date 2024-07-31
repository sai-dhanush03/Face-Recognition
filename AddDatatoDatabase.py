import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {

    'databaseURL': "https://facerecognition-raghavanteam-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Yuva sai",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123456":
        {
            "name": "Haneesha",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "555555":
        {
            "name": "Ragavan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Naga Umesh",
            "major": "Creator",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "sai dhanusha",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
