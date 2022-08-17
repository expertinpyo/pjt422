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
        "token": "10000000tokenij7",
        "trash_type": "GER",
        "amount": 0.030516731011519305,
        "status": "SAF",
        "location_x": 500.0,
        "location_y": 275.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij2",
        "trash_type": "CAN",
        "amount": 0.39567317000601965,
        "status": "SAF",
        "location_x": 520.0,
        "location_y": 275.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij8",
        "trash_type": "PET",
        "amount": 0.2547395649309665,
        "status": "SAF",
        "location_x": 540.0,
        "location_y": 275.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij7",
        "trash_type": "PPR",
        "amount": 0.20624465914118073,
        "status": "SAF",
        "location_x": 207.0,
        "location_y": 123.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij8",
        "trash_type": "PET",
        "amount": 0.7990576815531738,
        "status": "WAR",
        "location_x": 227.0,
        "location_y": 123.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij7",
        "trash_type": "GLA",
        "amount": 0.4028814180969468,
        "status": "CAU",
        "location_x": 247.0,
        "location_y": 123.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij7",
        "trash_type": "CAN",
        "amount": 0.3172476461213324,
        "status": "SAF",
        "location_x": 1020.0,
        "location_y": 350.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "GLA",
        "amount": 0.0460652562736833,
        "status": "SAF",
        "location_x": 1020.0,
        "location_y": 370.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij9",
        "trash_type": "PPR",
        "amount": 0.6065556850920341,
        "status": "CAU",
        "location_x": 1020.0,
        "location_y": 390.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "amount": 0.7844222573429906,
        "status": "WAR",
        "location_x": 657.0,
        "location_y": 280.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "amount": 0.13924511123742733,
        "status": "SAF",
        "location_x": 657.0,
        "location_y": 300.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.12142118427245874,
        "status": "SAF",
        "location_x": 657.0,
        "location_y": 320.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.817770847453445,
        "status": "WAR",
        "location_x": 190.0,
        "location_y": 125.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.8620393108225235,
        "status": "WAR",
        "location_x": 210.0,
        "location_y": 125.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "CAN",
        "amount": 0.34252462668506756,
        "status": "SAF",
        "location_x": 230.0,
        "location_y": 125.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "amount": 0.841768384326108,
        "status": "WAR",
        "location_x": 910.0,
        "location_y": 120.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "amount": 0.42734769912454174,
        "status": "CAU",
        "location_x": 910.0,
        "location_y": 140.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "amount": 0.39609125002832424,
        "status": "SAF",
        "location_x": 910.0,
        "location_y": 160.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.29879878359908485,
        "status": "SAF",
        "location_x": 600.0,
        "location_y": 255.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "PPR",
        "amount": 0.9715665004216151,
        "status": "WAR",
        "location_x": 620.0,
        "location_y": 255.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "GLA",
        "amount": 0.6849604352945702,
        "status": "CAU",
        "location_x": 640.0,
        "location_y": 255.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij1",
        "trash_type": "PET",
        "amount": 0.8755098839098002,
        "status": "WAR",
        "location_x": 280.0,
        "location_y": 392.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij9",
        "trash_type": "CAN",
        "amount": 0.19471351384690372,
        "status": "SAF",
        "location_x": 300.0,
        "location_y": 392.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij2",
        "trash_type": "PPR",
        "amount": 0.6498442851038031,
        "status": "CAU",
        "location_x": 320.0,
        "location_y": 392.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "CAN",
        "amount": 0.6133930498635991,
        "status": "CAU",
        "location_x": 1090.0,
        "location_y": 230.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij1",
        "trash_type": "GLA",
        "amount": 0.6705732246724992,
        "status": "CAU",
        "location_x": 1090.0,
        "location_y": 250.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij3",
        "trash_type": "PPR",
        "amount": 0.832515905899631,
        "status": "WAR",
        "location_x": 1090.0,
        "location_y": 270.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "CAN",
        "amount": 0.5553321002933499,
        "status": "CAU",
        "location_x": 120.0,
        "location_y": 245.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "PPR",
        "amount": 0.6170303467431675,
        "status": "CAU",
        "location_x": 140.0,
        "location_y": 245.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "amount": 0.6007294448350335,
        "status": "CAU",
        "location_x": 160.0,
        "location_y": 245.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij4",
        "trash_type": "PET",
        "amount": 0.9337748708924442,
        "status": "WAR",
        "location_x": 575.0,
        "location_y": 320.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij7",
        "trash_type": "CAN",
        "amount": 0.1476025706848848,
        "status": "SAF",
        "location_x": 575.0,
        "location_y": 340.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij7",
        "trash_type": "PPR",
        "amount": 0.01795622111691042,
        "status": "SAF",
        "location_x": 575.0,
        "location_y": 360.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij4",
        "trash_type": "PPR",
        "amount": 0.8789473960370197,
        "status": "WAR",
        "location_x": 1016.0,
        "location_y": 160.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "GLA",
        "amount": 0.621216476781266,
        "status": "CAU",
        "location_x": 1016.0,
        "location_y": 180.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.8036200370937253,
        "status": "WAR",
        "location_x": 1016.0,
        "location_y": 200.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 486.0,
        "location_y": 60.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 486.0,
        "location_y": 80.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 486.0,
        "location_y": 100.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 507.0,
        "location_y": 344.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 507.0,
        "location_y": 364.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 507.0,
        "location_y": 384.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 142.0,
        "location_y": 92.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 162.0,
        "location_y": 92.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 182.0,
        "location_y": 92.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 342.0,
        "location_y": 357.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 362.0,
        "location_y": 357.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 382.0,
        "location_y": 357.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 50.0,
        "location_y": 324.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 50.0,
        "location_y": 344.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 50.0,
        "location_y": 364.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 408.0,
        "location_y": 321.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 428.0,
        "location_y": 321.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 448.0,
        "location_y": 321.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 131.0,
        "location_y": 276.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "location_x": 131.0,
        "location_y": 296.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 131.0,
        "location_y": 316.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 301.0,
        "location_y": 247.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 321.0,
        "location_y": 247.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 341.0,
        "location_y": 247.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 351.0,
        "location_y": 77.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "location_x": 351.0,
        "location_y": 97.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 351.0,
        "location_y": 117.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 514.0,
        "location_y": 357.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 534.0,
        "location_y": 357.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 554.0,
        "location_y": 357.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "location_x": 419.0,
        "location_y": 111.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "location_x": 439.0,
        "location_y": 111.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "location_x": 459.0,
        "location_y": 111.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 440.0,
        "location_y": 190.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 440.0,
        "location_y": 210.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 440.0,
        "location_y": 230.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 73,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2273",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 251.0,
        "location_y": 79.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 74,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2274",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 251.0,
        "location_y": 99.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 75,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2275",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 251.0,
        "location_y": 119.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 76,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2276",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 263.0,
        "location_y": 259.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 77,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2277",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 283.0,
        "location_y": 259.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 78,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2278",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 303.0,
        "location_y": 259.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 79,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2279",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 317.0,
        "location_y": 123.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 80,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2280",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 317.0,
        "location_y": 143.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 81,
        "floor": {
            "pk": 9,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "어학관"
            }
        },
        "token": "2281",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 317.0,
        "location_y": 163.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 82,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B182",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 519.0,
        "location_y": 194.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 83,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B183",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 539.0,
        "location_y": 194.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 84,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B184",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 559.0,
        "location_y": 194.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 85,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B185",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 211.0,
        "location_y": 127.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 86,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B186",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 211.0,
        "location_y": 147.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 87,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B187",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 211.0,
        "location_y": 167.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 88,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B188",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 183.0,
        "location_y": 331.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 89,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B189",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 203.0,
        "location_y": 331.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 90,
        "floor": {
            "pk": 10,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3B190",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 223.0,
        "location_y": 331.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 91,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3191",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 516.0,
        "location_y": 372.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 92,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3192",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 536.0,
        "location_y": 372.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 93,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3193",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 556.0,
        "location_y": 372.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 94,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3194",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 54.0,
        "location_y": 247.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 95,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3195",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 74.0,
        "location_y": 247.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 96,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3196",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 94.0,
        "location_y": 247.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 97,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3197",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 198.0,
        "location_y": 342.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 98,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3198",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 218.0,
        "location_y": 342.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 99,
        "floor": {
            "pk": 11,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "3199",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 238.0,
        "location_y": 342.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 100,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32100",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 581.0,
        "location_y": 157.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 101,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32101",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 601.0,
        "location_y": 157.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 102,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32102",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 621.0,
        "location_y": 157.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 103,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32103",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 206.0,
        "location_y": 190.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 104,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32104",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 206.0,
        "location_y": 210.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 105,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32105",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 206.0,
        "location_y": 230.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 106,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32106",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 405.0,
        "location_y": 53.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 107,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32107",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 425.0,
        "location_y": 53.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 108,
        "floor": {
            "pk": 12,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "32108",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 445.0,
        "location_y": 53.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 109,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1109",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 53.0,
        "location_y": 197.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 110,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1110",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 53.0,
        "location_y": 217.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 111,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1111",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 53.0,
        "location_y": 237.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 112,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1112",
        "trash_type": "CAN",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 37.0,
        "location_y": 89.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 113,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1113",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 37.0,
        "location_y": 109.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 114,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1114",
        "trash_type": "GER",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 37.0,
        "location_y": 129.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 115,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1115",
        "trash_type": "PPR",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 481.0,
        "location_y": 270.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 116,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1116",
        "trash_type": "PET",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 481.0,
        "location_y": 290.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
        "discard_users": []
    },
    {
        "id": 117,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1117",
        "trash_type": "GLA",
        "amount": 0.0,
        "status": "SAF",
        "location_x": 481.0,
        "location_y": 310.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T14:53:19.497787+09:00",
        "updated_at": "2022-08-17T14:53:19.497787+09:00",
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