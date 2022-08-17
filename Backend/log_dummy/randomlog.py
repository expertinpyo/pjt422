import random 

trash_list = [
    {
        "id": 1,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "GLA",
        "amount": 0.6346277880064001,
        "status": "CAU",
        "location_x": 500.0,
        "location_y": 275.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 1,
        "discard_users": []
    },
    {
        "id": 2,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij3",
        "trash_type": "PPR",
        "amount": 0.0934726831677154,
        "status": "SAF",
        "location_x": 520.0,
        "location_y": 275.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 1,
        "discard_users": []
    },
    {
        "id": 3,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij3",
        "trash_type": "PET",
        "amount": 0.927956062731758,
        "status": "WAR",
        "location_x": 540.0,
        "location_y": 275.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 1,
        "discard_users": []
    },
    {
        "id": 4,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "PPR",
        "amount": 0.8583013655464262,
        "status": "WAR",
        "location_x": 207.0,
        "location_y": 123.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 2,
        "discard_users": []
    },
    {
        "id": 5,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "GLA",
        "amount": 0.8822247664515837,
        "status": "WAR",
        "location_x": 227.0,
        "location_y": 123.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 2,
        "discard_users": []
    },
    {
        "id": 6,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij6",
        "trash_type": "GER",
        "amount": 0.7374912259276587,
        "status": "WAR",
        "location_x": 247.0,
        "location_y": 123.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 2,
        "discard_users": []
    },
    {
        "id": 7,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij8",
        "trash_type": "GLA",
        "amount": 0.938858092943237,
        "status": "WAR",
        "location_x": 1020.0,
        "location_y": 350.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 3,
        "discard_users": []
    },
    {
        "id": 8,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "CAN",
        "amount": 0.5927984580780831,
        "status": "CAU",
        "location_x": 1020.0,
        "location_y": 370.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 3,
        "discard_users": []
    },
    {
        "id": 9,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij8",
        "trash_type": "PET",
        "amount": 0.5788567031153529,
        "status": "CAU",
        "location_x": 1020.0,
        "location_y": 390.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 3,
        "discard_users": []
    },
    {
        "id": 10,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000186490f2",
        "trash_type": "GER",
        "amount": 0.8240899974698471,
        "status": "WAR",
        "location_x": 657.0,
        "location_y": 280.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 4,
        "discard_users": []
    },
    {
        "id": 11,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "1000000089ff6e7a",
        "trash_type": "PET",
        "amount": 0.27085346342021666,
        "status": "SAF",
        "location_x": 657.0,
        "location_y": 300.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 4,
        "discard_users": []
    },
    {
        "id": 12,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "GLA",
        "amount": 0.7623332450022294,
        "status": "WAR",
        "location_x": 657.0,
        "location_y": 320.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 4,
        "discard_users": []
    },
    {
        "id": 13,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "GER",
        "amount": 0.6225241285034303,
        "status": "CAU",
        "location_x": 190.0,
        "location_y": 125.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 5,
        "discard_users": []
    },
    {
        "id": 14,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "GLA",
        "amount": 0.09708788400237023,
        "status": "SAF",
        "location_x": 210.0,
        "location_y": 125.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 5,
        "discard_users": []
    },
    {
        "id": 15,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "PPR",
        "amount": 0.8626757386582095,
        "status": "WAR",
        "location_x": 230.0,
        "location_y": 125.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 5,
        "discard_users": []
    },
    {
        "id": 16,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "CAN",
        "amount": 0.6781866224223265,
        "status": "CAU",
        "location_x": 910.0,
        "location_y": 120.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 6,
        "discard_users": []
    },
    {
        "id": 17,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "PET",
        "amount": 0.43484587236572536,
        "status": "CAU",
        "location_x": 910.0,
        "location_y": 140.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 6,
        "discard_users": []
    },
    {
        "id": 18,
        "floor": {
            "pk": 2,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenasd",
        "trash_type": "GLA",
        "amount": 0.41307170088021183,
        "status": "CAU",
        "location_x": 910.0,
        "location_y": 160.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 6,
        "discard_users": []
    },
    {
        "id": 19,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij1",
        "trash_type": "PPR",
        "amount": 0.4757737560875044,
        "status": "CAU",
        "location_x": 600.0,
        "location_y": 255.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 7,
        "discard_users": []
    },
    {
        "id": 20,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij8",
        "trash_type": "GLA",
        "amount": 0.7280861506941434,
        "status": "WAR",
        "location_x": 620.0,
        "location_y": 255.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 7,
        "discard_users": []
    },
    {
        "id": 21,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij6",
        "trash_type": "PET",
        "amount": 0.36331864389132595,
        "status": "SAF",
        "location_x": 640.0,
        "location_y": 255.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 7,
        "discard_users": []
    },
    {
        "id": 22,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "PET",
        "amount": 0.1518980313889825,
        "status": "SAF",
        "location_x": 280.0,
        "location_y": 392.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 8,
        "discard_users": []
    },
    {
        "id": 23,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij4",
        "trash_type": "PPR",
        "amount": 0.6776319048814731,
        "status": "CAU",
        "location_x": 300.0,
        "location_y": 392.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 8,
        "discard_users": []
    },
    {
        "id": 24,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij3",
        "trash_type": "GER",
        "amount": 0.674567399323091,
        "status": "CAU",
        "location_x": 320.0,
        "location_y": 392.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 8,
        "discard_users": []
    },
    {
        "id": 25,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij9",
        "trash_type": "GLA",
        "amount": 0.4009205818304974,
        "status": "CAU",
        "location_x": 1090.0,
        "location_y": 230.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 9,
        "discard_users": []
    },
    {
        "id": 26,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij5",
        "trash_type": "PPR",
        "amount": 0.764085075081819,
        "status": "WAR",
        "location_x": 1090.0,
        "location_y": 250.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 9,
        "discard_users": []
    },
    {
        "id": 27,
        "floor": {
            "pk": 3,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij8",
        "trash_type": "CAN",
        "amount": 0.3804156298647331,
        "status": "SAF",
        "location_x": 1090.0,
        "location_y": 270.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 9,
        "discard_users": []
    },
    {
        "id": 28,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij8",
        "trash_type": "GLA",
        "amount": 0.6360284877819891,
        "status": "CAU",
        "location_x": 120.0,
        "location_y": 245.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 10,
        "discard_users": []
    },
    {
        "id": 29,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij7",
        "trash_type": "PET",
        "amount": 0.5230610485573411,
        "status": "CAU",
        "location_x": 140.0,
        "location_y": 245.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 10,
        "discard_users": []
    },
    {
        "id": 30,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij1",
        "trash_type": "GER",
        "amount": 0.8954623967847901,
        "status": "WAR",
        "location_x": 160.0,
        "location_y": 245.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 10,
        "discard_users": []
    },
    {
        "id": 31,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "PET",
        "amount": 0.7892614542802272,
        "status": "WAR",
        "location_x": 575.0,
        "location_y": 320.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 11,
        "discard_users": []
    },
    {
        "id": 32,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij2",
        "trash_type": "GLA",
        "amount": 0.29647806956506595,
        "status": "SAF",
        "location_x": 575.0,
        "location_y": 340.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 11,
        "discard_users": []
    },
    {
        "id": 33,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij3",
        "trash_type": "GER",
        "amount": 0.21983602548621206,
        "status": "SAF",
        "location_x": 575.0,
        "location_y": 360.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 11,
        "discard_users": []
    },
    {
        "id": 34,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij5",
        "trash_type": "CAN",
        "amount": 0.734244494889422,
        "status": "WAR",
        "location_x": 1016.0,
        "location_y": 160.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 12,
        "discard_users": []
    },
    {
        "id": 35,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij1",
        "trash_type": "GER",
        "amount": 0.6148610374023142,
        "status": "CAU",
        "location_x": 1016.0,
        "location_y": 180.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 12,
        "discard_users": []
    },
    {
        "id": 36,
        "floor": {
            "pk": 4,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "평생교육관"
            }
        },
        "token": "10000000tokenij6",
        "trash_type": "PPR",
        "amount": 0.42085540638223917,
        "status": "CAU",
        "location_x": 1016.0,
        "location_y": 200.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 12,
        "discard_users": []
    },
    {
        "id": 37,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B137",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 113.0,
        "location_y": 244.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 13,
        "discard_users": []
    },
    {
        "id": 38,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B138",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 113.0,
        "location_y": 264.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 13,
        "discard_users": []
    },
    {
        "id": 39,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B139",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 113.0,
        "location_y": 284.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 13,
        "discard_users": []
    },
    {
        "id": 40,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B140",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 506.0,
        "location_y": 247.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 14,
        "discard_users": []
    },
    {
        "id": 41,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B141",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 506.0,
        "location_y": 267.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 14,
        "discard_users": []
    },
    {
        "id": 42,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B142",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 506.0,
        "location_y": 287.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 14,
        "discard_users": []
    },
    {
        "id": 43,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B143",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 437.0,
        "location_y": 80.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 15,
        "discard_users": []
    },
    {
        "id": 44,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B144",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 437.0,
        "location_y": 100.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 15,
        "discard_users": []
    },
    {
        "id": 45,
        "floor": {
            "pk": 5,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1B145",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 437.0,
        "location_y": 120.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 15,
        "discard_users": []
    },
    {
        "id": 46,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1146",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 504.0,
        "location_y": 180.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 16,
        "discard_users": []
    },
    {
        "id": 47,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1147",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 524.0,
        "location_y": 180.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 16,
        "discard_users": []
    },
    {
        "id": 48,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1148",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 544.0,
        "location_y": 180.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 16,
        "discard_users": []
    },
    {
        "id": 49,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1149",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 239.0,
        "location_y": 264.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 17,
        "discard_users": []
    },
    {
        "id": 50,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1150",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 239.0,
        "location_y": 284.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 17,
        "discard_users": []
    },
    {
        "id": 51,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1151",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 239.0,
        "location_y": 304.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 17,
        "discard_users": []
    },
    {
        "id": 52,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1152",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 197.0,
        "location_y": 132.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 18,
        "discard_users": []
    },
    {
        "id": 53,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1153",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 217.0,
        "location_y": 132.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 18,
        "discard_users": []
    },
    {
        "id": 54,
        "floor": {
            "pk": 6,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "기숙사"
            }
        },
        "token": "1154",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 237.0,
        "location_y": 132.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 18,
        "discard_users": []
    },
    {
        "id": 55,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B155",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 288.0,
        "location_y": 201.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 19,
        "discard_users": []
    },
    {
        "id": 56,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B156",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 308.0,
        "location_y": 201.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 19,
        "discard_users": []
    },
    {
        "id": 57,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B157",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 328.0,
        "location_y": 201.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 19,
        "discard_users": []
    },
    {
        "id": 58,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B158",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 502.0,
        "location_y": 152.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 20,
        "discard_users": []
    },
    {
        "id": 59,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B159",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 522.0,
        "location_y": 152.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 20,
        "discard_users": []
    },
    {
        "id": 60,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B160",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 542.0,
        "location_y": 152.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 20,
        "discard_users": []
    },
    {
        "id": 61,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B161",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 129.0,
        "location_y": 276.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 21,
        "discard_users": []
    },
    {
        "id": 62,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B162",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 149.0,
        "location_y": 276.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 21,
        "discard_users": []
    },
    {
        "id": 63,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2B163",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 169.0,
        "location_y": 276.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 21,
        "discard_users": []
    },
    {
        "id": 64,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2164",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 602.0,
        "location_y": 222.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 22,
        "discard_users": []
    },
    {
        "id": 65,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2165",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 622.0,
        "location_y": 222.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 22,
        "discard_users": []
    },
    {
        "id": 66,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2166",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 642.0,
        "location_y": 222.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 22,
        "discard_users": []
    },
    {
        "id": 67,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2167",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 384.0,
        "location_y": 269.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 23,
        "discard_users": []
    },
    {
        "id": 68,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2168",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 384.0,
        "location_y": 289.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 23,
        "discard_users": []
    },
    {
        "id": 69,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2169",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 384.0,
        "location_y": 309.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 23,
        "discard_users": []
    },
    {
        "id": 70,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2170",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 404.0,
        "location_y": 290.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 24,
        "discard_users": []
    },
    {
        "id": 71,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2171",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 424.0,
        "location_y": 290.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 24,
        "discard_users": []
    },
    {
        "id": 72,
        "floor": {
            "pk": 8,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2172",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 444.0,
        "location_y": 290.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 24,
        "discard_users": []
    },
    {
        "id": 73,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B173",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 532.0,
        "location_y": 158.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 25,
        "discard_users": []
    },
    {
        "id": 74,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B174",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 532.0,
        "location_y": 178.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 25,
        "discard_users": []
    },
    {
        "id": 75,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B175",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 532.0,
        "location_y": 198.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 25,
        "discard_users": []
    },
    {
        "id": 76,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B176",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 166.0,
        "location_y": 151.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 26,
        "discard_users": []
    },
    {
        "id": 77,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B177",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 186.0,
        "location_y": 151.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 26,
        "discard_users": []
    },
    {
        "id": 78,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B178",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 206.0,
        "location_y": 151.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 26,
        "discard_users": []
    },
    {
        "id": 79,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B179",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 210.0,
        "location_y": 313.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 27,
        "discard_users": []
    },
    {
        "id": 80,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B180",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 210.0,
        "location_y": 333.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 27,
        "discard_users": []
    },
    {
        "id": 81,
        "floor": {
            "pk": 9,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B181",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 210.0,
        "location_y": 353.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 27,
        "discard_users": []
    },
    {
        "id": 82,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B182",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 373.0,
        "location_y": 80.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 28,
        "discard_users": []
    },
    {
        "id": 83,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B183",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 373.0,
        "location_y": 100.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 28,
        "discard_users": []
    },
    {
        "id": 84,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B184",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 373.0,
        "location_y": 120.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 28,
        "discard_users": []
    },
    {
        "id": 85,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B185",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 348.0,
        "location_y": 144.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 29,
        "discard_users": []
    },
    {
        "id": 86,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B186",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 368.0,
        "location_y": 144.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 29,
        "discard_users": []
    },
    {
        "id": 87,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B187",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 388.0,
        "location_y": 144.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 29,
        "discard_users": []
    },
    {
        "id": 88,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B188",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 288.0,
        "location_y": 367.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 30,
        "discard_users": []
    },
    {
        "id": 89,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B189",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 308.0,
        "location_y": 367.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 30,
        "discard_users": []
    },
    {
        "id": 90,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B190",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 328.0,
        "location_y": 367.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 30,
        "discard_users": []
    },
    {
        "id": 91,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4191",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 560.0,
        "location_y": 373.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 31,
        "discard_users": []
    },
    {
        "id": 92,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4192",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 580.0,
        "location_y": 373.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 31,
        "discard_users": []
    },
    {
        "id": 93,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4193",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 600.0,
        "location_y": 373.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 31,
        "discard_users": []
    },
    {
        "id": 94,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4194",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 35.0,
        "location_y": 172.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 32,
        "discard_users": []
    },
    {
        "id": 95,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4195",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 35.0,
        "location_y": 192.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 32,
        "discard_users": []
    },
    {
        "id": 96,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4196",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 35.0,
        "location_y": 212.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 32,
        "discard_users": []
    },
    {
        "id": 97,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4197",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 286.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 33,
        "discard_users": []
    },
    {
        "id": 98,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4198",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 306.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 33,
        "discard_users": []
    },
    {
        "id": 99,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4199",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 326.0,
        "is_connected": True,
        "created_at": "2022-08-17T18:33:54.565388+09:00",
        "updated_at": "2022-08-17T18:33:54.565388+09:00",
        "group": 33,
        "discard_users": []
    }
]
for i in range(5, 9):
    if i == 6:
        nn = 31
    elif i == 8:
        nn = 16
    else:
        nn = 32
    for j in range(1, nn):        
        dd = '0' + str(j) if len(str(j)) == 1 else str(j)
        day = '20220' + str(i) + dd
        cnt = 0
        data = ''
        while cnt < 500:
            idx = random.randrange(len(trash_list))
            target = trash_list[idx]
            
            sec = str(random.randint(0, 59))
            min = str(random.randint(0, 59))
            hr = str(random.randint(0, 23))
            
            sec = '0'*(2-len(sec)) + sec
            min = '0'*(2-len(min)) + min
            hr = '0'*(2-len(hr)) + hr
            
            time = hr + ':' + min + ':' + sec

            rand_rfid = str(random.randint(1, 1000))
            rand_zero = '0' * (10-len(rand_rfid))
            sen = f'{day} {time} {target["floor"]["building"]["pk"]} {target["floor"]["pk"]} {target["token"]} {target["trash_type"]}'
            data += sen
            data += '\n'
            cnt += 1

        f = open(f'20220{str(i)+dd}.log', 'w', encoding='UTF-8')
        f.write(data)
        f.close()