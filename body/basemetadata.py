from users.basemetadata import BaseData, UpdateBaseData

UserProfileMetadata = BaseData({
    "name": "test",
    "birthday": "1999-01-01",
    "height": 180,
    "weight": '70',
    "phone": "010-1234-5678",
    "email": "test@gmail.com",
    "gender": 1,
    "fcm_id": "test",
    "address": "test"
})

BloodPressureMetadata = BaseData({
    "systolic": 100,
    "diastolic": 100,
    "pulse": 60,
    "recorded_at": "2023-02-03 08:17:17"
})

UserWeightMetadata = BaseData({
    "weight": 87.0,
    "body_fat": 23.0,
    "bmi": 23.0,
    "recorded_at": "2023-02-03 08:17:17"
})

BloodSugarMetadata = BaseData({
    "sugar": 123.0,
    "timeperiod": 1,
    "recorded_at": "2023-02-03 08:17:17",
    "drug": 1,
    "exercise": 1
})

UserRecordsMetadata = BaseData({
    "diet": 1,
})

UserRecordsDELMetadata = BaseData({
    "blood_sugar[]": [1],
    "blood_pressure[]": [1],
    "user_weight[]": [1]
})

UserDiaryMetadata =   {
    "id": 0,
    "user_id": 0,
    "systolic": 0,
    "diastolic": 0,
    "pulse": 0,
    "weight": 0.0,
    "body_fat": 0.0,
    "bmi": 0.0,
    "sugar": 0.0,
    "exercise": 0,
    "drug": 0,
    "timeperiod": 0,
    "description": "",
    "meal": 0,
    "tag": [{
      "name": [""],
      "message": ""
    }],
    "image": ["http://www.example.com"],
    "location": {
      "lat": "",
      "lng": ""
    },
    "reply": "",
    "recorded_at": "",
    "type": ""
}


UserDietMetadata = BaseData({
    "description": "good",
    "meal": 0,
    "tag[]": ["dinner"],
    "image": 1,
    "lat": 120.5,
    "lng": 323.5,
    "recorded_at": "2023-02-03 08:17:17"
})

UserA1cMetadata = BaseData({
    "a1c": 10,
    "recorded_at": "2023-02-07 04:54:43"
})

UserA1cDELMetadata = BaseData({
    "ids[]": [1, 2, 3]
})

UserMedicalMetadata = BaseData({
    "diabetes_type": 0,
    "oad": True,
    "insulin": True,
    "anti_hypertensives": True
})

UserDrugUsedMetadata = BaseData({
    "type": 0,
    "name": "test",
    "recorded_at": "2023-02-07 04:54:43"
})

UserCareMetadata = BaseData({
    "message": "hi"
})

UserProfileVipMetadata = {
    "id": 1,
    "user_id": 18,
    "level": 0,
    "remark": 0.0,
    "started_at": "2023-02-03 08:17:17",
    "ended_at": "2023-02-03 08:17:17",
    "created_at": "2023-02-03 08:17:17",
    "updated_at": "2023-02-03 08:17:17",
}

UserBadgeMetadata = BaseData({
    "badge": 1.
})

UserTestMetadata = {
    "id": 1,
    "name": "",
    "account": "t57@gmail.com",
    "email": "t7357@gmail.com",
    "phone": "",
    "fb_id": "未設置",
    "status": "VIP",
    "group": "0",
    "birthday": "1989-06-04",
    "height": 0.0,
    "weight": 0.0,
    "gender": 1,
    "address": "",
    "unread_records": [0,0,0],
    "verified": 1,
    "privacy_policy": 1,
    "must_change_password": 0,
    "fcm_id": "",
    "login_times": 15,
    "created_at": "2023-10-21T18:38:32.264218+08:00",
    "updated_at": "2023-10-21T18:53:44.500654+08:00",
    "default": {
        "id": 1,
        "sugar_delta_max": 0.0,
        "sugar_delta_min": 0.0,
        "sugar_morning_max": 0.0,
        "sugar_morning_min": 0.0,
        "sugar_evening_max": 0.0,
        "sugar_evening_min": 0.0,
        "sugar_before_max": 0.0,
        "sugar_before_min": 0.0,
        "sugar_after_max": 0.0,
        "sugar_after_min": 0.0,
        "systolic_max": 0,
        "systolic_min": 0,
        "diastolic_max": 0,
        "diastolic_min": 0,
        "pulse_max": 0,
        "pulse_min": 0,
        "weight_max": 0.0,
        "weight_min": 0.0,
        "bmi_max": 0.0,
        "bmi_min": 0.0,
        "body_fat_max": 0.0,
        "body_fat_min": 0.0,
        "user_id": 1,
        "created_at": "2023-10-21 10:38:50",
        "updated_at": "2023-10-21 10:38:50"
    },
    "setting": {
        "id": 1,
        "user_id": 1,
        "after_recording": 0,
        "no_recording_for_a_day": 0,
        "over_max_or_under_min": 0,
        "after_meal": 0,
        "unit_of_sugar": 0,
        "unit_of_weight": 0,
        "unit_of_height": 0,
        "created_at": "2023-10-21 10:38:50",
        "updated_at": "2023-10-21 10:38:50"
    },
    "vip": {
        "id": 1,
        "user_id": 1,
        "level": 0,
        "remark": 0.0,
        "started_at": "2023-10-21 10:53:44",
        "ended_at": "2024-10-20 10:53:44",
        "created_at": "2023-10-21 10:53:44",
        "updated_at": "2023-10-21 10:53:44"
    }
}