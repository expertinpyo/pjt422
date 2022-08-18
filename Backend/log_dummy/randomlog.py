import random

trash_list = [
    {
        "id": 1,
        "group": {
            "pk": 1,
            "name": "B2A1",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B21",
        "trash_type": "CAN",
        "amount": 0.191689367328017,
        "status": "SAF",
        "location_x": 504.0,
        "location_y": 252.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 2,
        "group": {
            "pk": 1,
            "name": "B2A1",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B22",
        "trash_type": "CAN",
        "amount": 0.2627558197436344,
        "status": "SAF",
        "location_x": 524.0,
        "location_y": 252.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 3,
        "group": {
            "pk": 1,
            "name": "B2A1",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B23",
        "trash_type": "PET",
        "amount": 0.8223920084231785,
        "status": "WAR",
        "location_x": 564.0,
        "location_y": 252.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 4,
        "group": {
            "pk": 2,
            "name": "B2A2",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B24",
        "trash_type": "GER",
        "amount": 0.26003990887143125,
        "status": "SAF",
        "location_x": 356.0,
        "location_y": 396.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 5,
        "group": {
            "pk": 2,
            "name": "B2A2",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B25",
        "trash_type": "PET",
        "amount": 0.4626127130342925,
        "status": "CAU",
        "location_x": 376.0,
        "location_y": 396.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 6,
        "group": {
            "pk": 2,
            "name": "B2A2",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B26",
        "trash_type": "PPR",
        "amount": 0.012792811252505643,
        "status": "SAF",
        "location_x": 416.0,
        "location_y": 396.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 7,
        "group": {
            "pk": 3,
            "name": "B2A3",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B27",
        "trash_type": "CAN",
        "amount": 0.9302771862315875,
        "status": "WAR",
        "location_x": 362.0,
        "location_y": 295.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 8,
        "group": {
            "pk": 3,
            "name": "B2A3",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B28",
        "trash_type": "PPR",
        "amount": 0.7384724050830096,
        "status": "WAR",
        "location_x": 382.0,
        "location_y": 295.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 9,
        "group": {
            "pk": 3,
            "name": "B2A3",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B29",
        "trash_type": "GLA",
        "amount": 0.3968666458108687,
        "status": "SAF",
        "location_x": 422.0,
        "location_y": 295.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 10,
        "group": {
            "pk": 4,
            "name": "B2A4",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B210",
        "trash_type": "GER",
        "amount": 0.230252550253485,
        "status": "SAF",
        "location_x": 78.0,
        "location_y": 129.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 11,
        "group": {
            "pk": 4,
            "name": "B2A4",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B211",
        "trash_type": "PPR",
        "amount": 0.45610536767184473,
        "status": "CAU",
        "location_x": 98.0,
        "location_y": 129.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 12,
        "group": {
            "pk": 4,
            "name": "B2A4",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B212",
        "trash_type": "GLA",
        "amount": 0.2611010219731572,
        "status": "SAF",
        "location_x": 138.0,
        "location_y": 129.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 13,
        "group": {
            "pk": 5,
            "name": "B2A5",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B213",
        "trash_type": "PPR",
        "amount": 0.8111019822258914,
        "status": "WAR",
        "location_x": 331.0,
        "location_y": 311.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 14,
        "group": {
            "pk": 5,
            "name": "B2A5",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B214",
        "trash_type": "PPR",
        "amount": 0.08676248906137685,
        "status": "SAF",
        "location_x": 331.0,
        "location_y": 331.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 15,
        "group": {
            "pk": 5,
            "name": "B2A5",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B215",
        "trash_type": "PET",
        "amount": 0.37500542513413904,
        "status": "SAF",
        "location_x": 331.0,
        "location_y": 371.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 16,
        "group": {
            "pk": 6,
            "name": "B2A6",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B216",
        "trash_type": "CAN",
        "amount": 0.7418626212386411,
        "status": "WAR",
        "location_x": 573.0,
        "location_y": 379.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 17,
        "group": {
            "pk": 6,
            "name": "B2A6",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B217",
        "trash_type": "CAN",
        "amount": 0.6635936632442574,
        "status": "CAU",
        "location_x": 593.0,
        "location_y": 379.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 18,
        "group": {
            "pk": 6,
            "name": "B2A6",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B218",
        "trash_type": "PPR",
        "amount": 0.6042359448195352,
        "status": "CAU",
        "location_x": 633.0,
        "location_y": 379.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 19,
        "group": {
            "pk": 7,
            "name": "B2A7",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B219",
        "trash_type": "GLA",
        "amount": 0.007558030730937637,
        "status": "SAF",
        "location_x": 125.0,
        "location_y": 389.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 20,
        "group": {
            "pk": 7,
            "name": "B2A7",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B220",
        "trash_type": "GLA",
        "amount": 0.795980461687362,
        "status": "WAR",
        "location_x": 145.0,
        "location_y": 389.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 21,
        "group": {
            "pk": 7,
            "name": "B2A7",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B221",
        "trash_type": "GER",
        "amount": 0.8924380081157516,
        "status": "WAR",
        "location_x": 185.0,
        "location_y": 389.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 22,
        "group": {
            "pk": 8,
            "name": "B2A8",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B222",
        "trash_type": "GER",
        "amount": 0.11874565512017243,
        "status": "SAF",
        "location_x": 135.0,
        "location_y": 206.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 23,
        "group": {
            "pk": 8,
            "name": "B2A8",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B223",
        "trash_type": "PET",
        "amount": 0.3490288587576169,
        "status": "SAF",
        "location_x": 135.0,
        "location_y": 226.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 24,
        "group": {
            "pk": 8,
            "name": "B2A8",
            "floor": {
                "pk": 1,
                "name": "B2",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B224",
        "trash_type": "CAN",
        "amount": 0.7835359637887168,
        "status": "WAR",
        "location_x": 135.0,
        "location_y": 266.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 25,
        "group": {
            "pk": 9,
            "name": "B1B1",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B125",
        "trash_type": "GLA",
        "amount": 0.9827274186748337,
        "status": "WAR",
        "location_x": 516.0,
        "location_y": 300.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 26,
        "group": {
            "pk": 9,
            "name": "B1B1",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B126",
        "trash_type": "PPR",
        "amount": 0.3442013248699405,
        "status": "SAF",
        "location_x": 516.0,
        "location_y": 320.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 27,
        "group": {
            "pk": 9,
            "name": "B1B1",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B127",
        "trash_type": "PET",
        "amount": 0.8904476186665138,
        "status": "WAR",
        "location_x": 516.0,
        "location_y": 360.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 28,
        "group": {
            "pk": 10,
            "name": "B1B2",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B128",
        "trash_type": "GER",
        "amount": 0.7480087661607718,
        "status": "WAR",
        "location_x": 400.0,
        "location_y": 198.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 29,
        "group": {
            "pk": 10,
            "name": "B1B2",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B129",
        "trash_type": "GLA",
        "amount": 0.8326379991305373,
        "status": "WAR",
        "location_x": 420.0,
        "location_y": 198.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 30,
        "group": {
            "pk": 10,
            "name": "B1B2",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B130",
        "trash_type": "PET",
        "amount": 0.23119718877101025,
        "status": "SAF",
        "location_x": 460.0,
        "location_y": 198.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 31,
        "group": {
            "pk": 11,
            "name": "B1B3",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B131",
        "trash_type": "PPR",
        "amount": 0.8679844651486235,
        "status": "WAR",
        "location_x": 455.0,
        "location_y": 250.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 32,
        "group": {
            "pk": 11,
            "name": "B1B3",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B132",
        "trash_type": "GLA",
        "amount": 0.4553088815806626,
        "status": "CAU",
        "location_x": 455.0,
        "location_y": 270.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 33,
        "group": {
            "pk": 11,
            "name": "B1B3",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B133",
        "trash_type": "CAN",
        "amount": 0.5872396919456941,
        "status": "CAU",
        "location_x": 455.0,
        "location_y": 310.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 34,
        "group": {
            "pk": 12,
            "name": "B1B4",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B134",
        "trash_type": "GLA",
        "amount": 0.9488837307802783,
        "status": "WAR",
        "location_x": 66.0,
        "location_y": 153.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 35,
        "group": {
            "pk": 12,
            "name": "B1B4",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B135",
        "trash_type": "PPR",
        "amount": 0.6959473963429391,
        "status": "CAU",
        "location_x": 66.0,
        "location_y": 173.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 36,
        "group": {
            "pk": 12,
            "name": "B1B4",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B136",
        "trash_type": "GER",
        "amount": 0.03243690586459802,
        "status": "SAF",
        "location_x": 66.0,
        "location_y": 213.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 37,
        "group": {
            "pk": 13,
            "name": "B1B5",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B137",
        "trash_type": "PPR",
        "amount": 0.3674037296766668,
        "status": "SAF",
        "location_x": 547.0,
        "location_y": 267.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 38,
        "group": {
            "pk": 13,
            "name": "B1B5",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B138",
        "trash_type": "GER",
        "amount": 0.1945507947039541,
        "status": "SAF",
        "location_x": 547.0,
        "location_y": 287.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 39,
        "group": {
            "pk": 13,
            "name": "B1B5",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B139",
        "trash_type": "GER",
        "amount": 0.43362767880614295,
        "status": "CAU",
        "location_x": 547.0,
        "location_y": 327.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 40,
        "group": {
            "pk": 14,
            "name": "B1B6",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B140",
        "trash_type": "CAN",
        "amount": 0.03693217188188902,
        "status": "SAF",
        "location_x": 444.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 41,
        "group": {
            "pk": 14,
            "name": "B1B6",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B141",
        "trash_type": "PPR",
        "amount": 0.279078862735612,
        "status": "SAF",
        "location_x": 464.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 42,
        "group": {
            "pk": 14,
            "name": "B1B6",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B142",
        "trash_type": "GLA",
        "amount": 0.23735631015001257,
        "status": "SAF",
        "location_x": 504.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 43,
        "group": {
            "pk": 15,
            "name": "B1B7",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B143",
        "trash_type": "CAN",
        "amount": 0.5300369464439345,
        "status": "CAU",
        "location_x": 240.0,
        "location_y": 193.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 44,
        "group": {
            "pk": 15,
            "name": "B1B7",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B144",
        "trash_type": "PET",
        "amount": 0.6730251405244109,
        "status": "CAU",
        "location_x": 240.0,
        "location_y": 213.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 45,
        "group": {
            "pk": 15,
            "name": "B1B7",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B145",
        "trash_type": "CAN",
        "amount": 0.6332035035537502,
        "status": "CAU",
        "location_x": 240.0,
        "location_y": 253.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 46,
        "group": {
            "pk": 16,
            "name": "B1B8",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B146",
        "trash_type": "GLA",
        "amount": 0.43850398189136197,
        "status": "CAU",
        "location_x": 357.0,
        "location_y": 322.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 47,
        "group": {
            "pk": 16,
            "name": "B1B8",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B147",
        "trash_type": "CAN",
        "amount": 0.8274023436155962,
        "status": "WAR",
        "location_x": 377.0,
        "location_y": 322.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 48,
        "group": {
            "pk": 16,
            "name": "B1B8",
            "floor": {
                "pk": 2,
                "name": "B1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1B148",
        "trash_type": "CAN",
        "amount": 0.6761455729704132,
        "status": "CAU",
        "location_x": 417.0,
        "location_y": 322.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 49,
        "group": {
            "pk": 17,
            "name": "1C1",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1149",
        "trash_type": "PET",
        "amount": 0.8633597302620355,
        "status": "WAR",
        "location_x": 582.0,
        "location_y": 221.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 50,
        "group": {
            "pk": 17,
            "name": "1C1",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1150",
        "trash_type": "PPR",
        "amount": 0.4606760535727218,
        "status": "CAU",
        "location_x": 582.0,
        "location_y": 241.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 51,
        "group": {
            "pk": 17,
            "name": "1C1",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1151",
        "trash_type": "GLA",
        "amount": 0.2807953997824537,
        "status": "SAF",
        "location_x": 582.0,
        "location_y": 281.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 52,
        "group": {
            "pk": 18,
            "name": "1C2",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1152",
        "trash_type": "CAN",
        "amount": 0.5251394706452039,
        "status": "CAU",
        "location_x": 135.0,
        "location_y": 85.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 53,
        "group": {
            "pk": 18,
            "name": "1C2",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1153",
        "trash_type": "GER",
        "amount": 0.7683645163309321,
        "status": "WAR",
        "location_x": 135.0,
        "location_y": 105.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 54,
        "group": {
            "pk": 18,
            "name": "1C2",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1154",
        "trash_type": "PPR",
        "amount": 0.9355919177356092,
        "status": "WAR",
        "location_x": 135.0,
        "location_y": 145.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 55,
        "group": {
            "pk": 19,
            "name": "1C3",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1155",
        "trash_type": "GER",
        "amount": 0.3963397798448989,
        "status": "SAF",
        "location_x": 34.0,
        "location_y": 38.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 56,
        "group": {
            "pk": 19,
            "name": "1C3",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1156",
        "trash_type": "CAN",
        "amount": 0.9420208193240218,
        "status": "WAR",
        "location_x": 54.0,
        "location_y": 38.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 57,
        "group": {
            "pk": 19,
            "name": "1C3",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1157",
        "trash_type": "CAN",
        "amount": 0.7172890245932045,
        "status": "WAR",
        "location_x": 94.0,
        "location_y": 38.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 58,
        "group": {
            "pk": 20,
            "name": "1C4",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1158",
        "trash_type": "PPR",
        "amount": 0.1809806834129476,
        "status": "SAF",
        "location_x": 213.0,
        "location_y": 152.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 59,
        "group": {
            "pk": 20,
            "name": "1C4",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1159",
        "trash_type": "PPR",
        "amount": 0.24849108216199178,
        "status": "SAF",
        "location_x": 233.0,
        "location_y": 152.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 60,
        "group": {
            "pk": 20,
            "name": "1C4",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1160",
        "trash_type": "CAN",
        "amount": 0.892926061090166,
        "status": "WAR",
        "location_x": 273.0,
        "location_y": 152.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 61,
        "group": {
            "pk": 21,
            "name": "1C5",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1161",
        "trash_type": "PPR",
        "amount": 0.6864801910833617,
        "status": "CAU",
        "location_x": 569.0,
        "location_y": 103.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 62,
        "group": {
            "pk": 21,
            "name": "1C5",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1162",
        "trash_type": "CAN",
        "amount": 0.25075370577109435,
        "status": "SAF",
        "location_x": 589.0,
        "location_y": 103.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 63,
        "group": {
            "pk": 21,
            "name": "1C5",
            "floor": {
                "pk": 3,
                "name": "1",
                "building": {
                    "pk": 1,
                    "name": "공학관"
                }
            }
        },
        "token": "1163",
        "trash_type": "PET",
        "amount": 0.951494512349635,
        "status": "WAR",
        "location_x": 629.0,
        "location_y": 103.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 64,
        "group": {
            "pk": 22,
            "name": "B2D1",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B264",
        "trash_type": "GLA",
        "amount": 0.2898807432199385,
        "status": "SAF",
        "location_x": 300.0,
        "location_y": 288.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 65,
        "group": {
            "pk": 22,
            "name": "B2D1",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B265",
        "trash_type": "GER",
        "amount": 0.827530690579478,
        "status": "WAR",
        "location_x": 300.0,
        "location_y": 308.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 66,
        "group": {
            "pk": 22,
            "name": "B2D1",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B266",
        "trash_type": "PPR",
        "amount": 0.4758808525449686,
        "status": "CAU",
        "location_x": 300.0,
        "location_y": 348.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 67,
        "group": {
            "pk": 23,
            "name": "B2D2",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B267",
        "trash_type": "GLA",
        "amount": 0.659588004979447,
        "status": "CAU",
        "location_x": 233.0,
        "location_y": 95.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 68,
        "group": {
            "pk": 23,
            "name": "B2D2",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B268",
        "trash_type": "PPR",
        "amount": 0.22078447388333045,
        "status": "SAF",
        "location_x": 233.0,
        "location_y": 115.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 69,
        "group": {
            "pk": 23,
            "name": "B2D2",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B269",
        "trash_type": "CAN",
        "amount": 0.8102641748394692,
        "status": "WAR",
        "location_x": 233.0,
        "location_y": 155.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 70,
        "group": {
            "pk": 24,
            "name": "B2D3",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B270",
        "trash_type": "GER",
        "amount": 0.67417930246674,
        "status": "CAU",
        "location_x": 444.0,
        "location_y": 174.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 71,
        "group": {
            "pk": 24,
            "name": "B2D3",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B271",
        "trash_type": "PET",
        "amount": 0.6056906427756955,
        "status": "CAU",
        "location_x": 444.0,
        "location_y": 194.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 72,
        "group": {
            "pk": 24,
            "name": "B2D3",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B272",
        "trash_type": "PPR",
        "amount": 0.6658613575616155,
        "status": "CAU",
        "location_x": 444.0,
        "location_y": 234.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 73,
        "group": {
            "pk": 25,
            "name": "B2D4",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B273",
        "trash_type": "GER",
        "amount": 0.5940075353295157,
        "status": "CAU",
        "location_x": 110.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 74,
        "group": {
            "pk": 25,
            "name": "B2D4",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B274",
        "trash_type": "GER",
        "amount": 0.023853477152695812,
        "status": "SAF",
        "location_x": 130.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 75,
        "group": {
            "pk": 25,
            "name": "B2D4",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B275",
        "trash_type": "CAN",
        "amount": 0.6963892258927024,
        "status": "CAU",
        "location_x": 170.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 76,
        "group": {
            "pk": 26,
            "name": "B2D5",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B276",
        "trash_type": "PPR",
        "amount": 0.24368066262219035,
        "status": "SAF",
        "location_x": 518.0,
        "location_y": 46.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 77,
        "group": {
            "pk": 26,
            "name": "B2D5",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B277",
        "trash_type": "PPR",
        "amount": 0.11770692623585499,
        "status": "SAF",
        "location_x": 518.0,
        "location_y": 66.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 78,
        "group": {
            "pk": 26,
            "name": "B2D5",
            "floor": {
                "pk": 4,
                "name": "B2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B278",
        "trash_type": "CAN",
        "amount": 0.043676411191038045,
        "status": "SAF",
        "location_x": 518.0,
        "location_y": 106.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 79,
        "group": {
            "pk": 27,
            "name": "B1E1",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B179",
        "trash_type": "PET",
        "amount": 0.9191509110942804,
        "status": "WAR",
        "location_x": 367.0,
        "location_y": 43.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 80,
        "group": {
            "pk": 27,
            "name": "B1E1",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B180",
        "trash_type": "PET",
        "amount": 0.1894088661393718,
        "status": "SAF",
        "location_x": 367.0,
        "location_y": 63.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 81,
        "group": {
            "pk": 27,
            "name": "B1E1",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B181",
        "trash_type": "GLA",
        "amount": 0.525049493072776,
        "status": "CAU",
        "location_x": 367.0,
        "location_y": 103.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 82,
        "group": {
            "pk": 28,
            "name": "B1E2",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B182",
        "trash_type": "GLA",
        "amount": 0.33733519055588046,
        "status": "SAF",
        "location_x": 275.0,
        "location_y": 201.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 83,
        "group": {
            "pk": 28,
            "name": "B1E2",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B183",
        "trash_type": "GLA",
        "amount": 0.6953959784493681,
        "status": "CAU",
        "location_x": 275.0,
        "location_y": 221.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 84,
        "group": {
            "pk": 28,
            "name": "B1E2",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B184",
        "trash_type": "CAN",
        "amount": 0.6364270280939105,
        "status": "CAU",
        "location_x": 275.0,
        "location_y": 261.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 85,
        "group": {
            "pk": 29,
            "name": "B1E3",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B185",
        "trash_type": "GLA",
        "amount": 0.059124269926560724,
        "status": "SAF",
        "location_x": 408.0,
        "location_y": 50.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 86,
        "group": {
            "pk": 29,
            "name": "B1E3",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B186",
        "trash_type": "GLA",
        "amount": 0.6768429087075617,
        "status": "CAU",
        "location_x": 428.0,
        "location_y": 50.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 87,
        "group": {
            "pk": 29,
            "name": "B1E3",
            "floor": {
                "pk": 5,
                "name": "B1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2B187",
        "trash_type": "GER",
        "amount": 0.8601695235302975,
        "status": "WAR",
        "location_x": 468.0,
        "location_y": 50.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 88,
        "group": {
            "pk": 30,
            "name": "1F1",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2188",
        "trash_type": "PET",
        "amount": 0.6425412896602981,
        "status": "CAU",
        "location_x": 139.0,
        "location_y": 82.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 89,
        "group": {
            "pk": 30,
            "name": "1F1",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2189",
        "trash_type": "PPR",
        "amount": 0.8861783621747512,
        "status": "WAR",
        "location_x": 139.0,
        "location_y": 102.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 90,
        "group": {
            "pk": 30,
            "name": "1F1",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2190",
        "trash_type": "PET",
        "amount": 0.5663830188227177,
        "status": "CAU",
        "location_x": 139.0,
        "location_y": 142.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 91,
        "group": {
            "pk": 31,
            "name": "1F2",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2191",
        "trash_type": "GLA",
        "amount": 0.8214031487410118,
        "status": "WAR",
        "location_x": 144.0,
        "location_y": 126.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 92,
        "group": {
            "pk": 31,
            "name": "1F2",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2192",
        "trash_type": "CAN",
        "amount": 0.8363451121306227,
        "status": "WAR",
        "location_x": 144.0,
        "location_y": 146.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 93,
        "group": {
            "pk": 31,
            "name": "1F2",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2193",
        "trash_type": "PPR",
        "amount": 0.0921266383301429,
        "status": "SAF",
        "location_x": 144.0,
        "location_y": 186.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 94,
        "group": {
            "pk": 32,
            "name": "1F3",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2194",
        "trash_type": "GER",
        "amount": 0.00848969754995721,
        "status": "SAF",
        "location_x": 339.0,
        "location_y": 138.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 95,
        "group": {
            "pk": 32,
            "name": "1F3",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2195",
        "trash_type": "PET",
        "amount": 0.6783120050329793,
        "status": "CAU",
        "location_x": 339.0,
        "location_y": 158.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 96,
        "group": {
            "pk": 32,
            "name": "1F3",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2196",
        "trash_type": "GLA",
        "amount": 0.6846401768359032,
        "status": "CAU",
        "location_x": 339.0,
        "location_y": 198.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 97,
        "group": {
            "pk": 33,
            "name": "1F4",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2197",
        "trash_type": "PET",
        "amount": 0.5226222961566246,
        "status": "CAU",
        "location_x": 551.0,
        "location_y": 104.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 98,
        "group": {
            "pk": 33,
            "name": "1F4",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2198",
        "trash_type": "GER",
        "amount": 0.4045620785964833,
        "status": "CAU",
        "location_x": 571.0,
        "location_y": 104.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 99,
        "group": {
            "pk": 33,
            "name": "1F4",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "2199",
        "trash_type": "GLA",
        "amount": 0.8430404260271229,
        "status": "WAR",
        "location_x": 611.0,
        "location_y": 104.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 100,
        "group": {
            "pk": 34,
            "name": "1F5",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "21100",
        "trash_type": "PPR",
        "amount": 0.7293839163102588,
        "status": "WAR",
        "location_x": 447.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 101,
        "group": {
            "pk": 34,
            "name": "1F5",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "21101",
        "trash_type": "PET",
        "amount": 0.6598846157734632,
        "status": "CAU",
        "location_x": 467.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 102,
        "group": {
            "pk": 34,
            "name": "1F5",
            "floor": {
                "pk": 6,
                "name": "1",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "21102",
        "trash_type": "PPR",
        "amount": 0.06099806091826554,
        "status": "SAF",
        "location_x": 507.0,
        "location_y": 378.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 103,
        "group": {
            "pk": 35,
            "name": "2G1",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22103",
        "trash_type": "PET",
        "amount": 0.2362743251408701,
        "status": "SAF",
        "location_x": 353.0,
        "location_y": 393.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 104,
        "group": {
            "pk": 35,
            "name": "2G1",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22104",
        "trash_type": "GLA",
        "amount": 0.8201949009602107,
        "status": "WAR",
        "location_x": 373.0,
        "location_y": 393.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 105,
        "group": {
            "pk": 35,
            "name": "2G1",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22105",
        "trash_type": "CAN",
        "amount": 0.8949751238983017,
        "status": "WAR",
        "location_x": 413.0,
        "location_y": 393.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 106,
        "group": {
            "pk": 36,
            "name": "2G2",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22106",
        "trash_type": "GLA",
        "amount": 0.69105277771596,
        "status": "CAU",
        "location_x": 581.0,
        "location_y": 90.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 107,
        "group": {
            "pk": 36,
            "name": "2G2",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22107",
        "trash_type": "PPR",
        "amount": 0.9289781554340193,
        "status": "WAR",
        "location_x": 601.0,
        "location_y": 90.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 108,
        "group": {
            "pk": 36,
            "name": "2G2",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22108",
        "trash_type": "PPR",
        "amount": 0.2812811422534025,
        "status": "SAF",
        "location_x": 641.0,
        "location_y": 90.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 109,
        "group": {
            "pk": 37,
            "name": "2G3",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22109",
        "trash_type": "CAN",
        "amount": 0.07174527397657116,
        "status": "SAF",
        "location_x": 422.0,
        "location_y": 113.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 110,
        "group": {
            "pk": 37,
            "name": "2G3",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22110",
        "trash_type": "CAN",
        "amount": 0.12912113729881625,
        "status": "SAF",
        "location_x": 422.0,
        "location_y": 133.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 111,
        "group": {
            "pk": 37,
            "name": "2G3",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22111",
        "trash_type": "PPR",
        "amount": 0.8241714331571405,
        "status": "WAR",
        "location_x": 422.0,
        "location_y": 173.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 112,
        "group": {
            "pk": 38,
            "name": "2G4",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22112",
        "trash_type": "GLA",
        "amount": 0.04168567245468113,
        "status": "SAF",
        "location_x": 299.0,
        "location_y": 130.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 113,
        "group": {
            "pk": 38,
            "name": "2G4",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22113",
        "trash_type": "GLA",
        "amount": 0.08659401877423245,
        "status": "SAF",
        "location_x": 319.0,
        "location_y": 130.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 114,
        "group": {
            "pk": 38,
            "name": "2G4",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22114",
        "trash_type": "GER",
        "amount": 0.537387263825434,
        "status": "CAU",
        "location_x": 359.0,
        "location_y": 130.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 115,
        "group": {
            "pk": 39,
            "name": "2G5",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22115",
        "trash_type": "CAN",
        "amount": 0.36408266934414757,
        "status": "SAF",
        "location_x": 349.0,
        "location_y": 96.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 116,
        "group": {
            "pk": 39,
            "name": "2G5",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22116",
        "trash_type": "GER",
        "amount": 0.8156645575177205,
        "status": "WAR",
        "location_x": 369.0,
        "location_y": 96.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 117,
        "group": {
            "pk": 39,
            "name": "2G5",
            "floor": {
                "pk": 7,
                "name": "2",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "22117",
        "trash_type": "CAN",
        "amount": 0.791717054377628,
        "status": "WAR",
        "location_x": 409.0,
        "location_y": 96.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 118,
        "group": {
            "pk": 40,
            "name": "3H1",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23118",
        "trash_type": "PPR",
        "amount": 0.32420305000905847,
        "status": "SAF",
        "location_x": 313.0,
        "location_y": 297.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 119,
        "group": {
            "pk": 40,
            "name": "3H1",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23119",
        "trash_type": "GER",
        "amount": 0.310880928463363,
        "status": "SAF",
        "location_x": 333.0,
        "location_y": 297.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 120,
        "group": {
            "pk": 40,
            "name": "3H1",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23120",
        "trash_type": "CAN",
        "amount": 0.8002851513724273,
        "status": "WAR",
        "location_x": 373.0,
        "location_y": 297.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 121,
        "group": {
            "pk": 41,
            "name": "3H2",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23121",
        "trash_type": "GER",
        "amount": 0.3872809456409434,
        "status": "SAF",
        "location_x": 485.0,
        "location_y": 342.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 122,
        "group": {
            "pk": 41,
            "name": "3H2",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23122",
        "trash_type": "PPR",
        "amount": 0.3648035063972026,
        "status": "SAF",
        "location_x": 505.0,
        "location_y": 342.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 123,
        "group": {
            "pk": 41,
            "name": "3H2",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23123",
        "trash_type": "GLA",
        "amount": 0.3185043513105651,
        "status": "SAF",
        "location_x": 545.0,
        "location_y": 342.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 124,
        "group": {
            "pk": 42,
            "name": "3H3",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23124",
        "trash_type": "GER",
        "amount": 0.9386161338466225,
        "status": "WAR",
        "location_x": 523.0,
        "location_y": 76.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 125,
        "group": {
            "pk": 42,
            "name": "3H3",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23125",
        "trash_type": "PPR",
        "amount": 0.32617485849156946,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 76.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 126,
        "group": {
            "pk": 42,
            "name": "3H3",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23126",
        "trash_type": "PET",
        "amount": 0.3289916548038957,
        "status": "SAF",
        "location_x": 583.0,
        "location_y": 76.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 127,
        "group": {
            "pk": 43,
            "name": "3H4",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23127",
        "trash_type": "GLA",
        "amount": 0.548006347037904,
        "status": "CAU",
        "location_x": 320.0,
        "location_y": 188.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 128,
        "group": {
            "pk": 43,
            "name": "3H4",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23128",
        "trash_type": "GLA",
        "amount": 0.21328999855924136,
        "status": "SAF",
        "location_x": 320.0,
        "location_y": 208.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 129,
        "group": {
            "pk": 43,
            "name": "3H4",
            "floor": {
                "pk": 8,
                "name": "3",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "23129",
        "trash_type": "PPR",
        "amount": 0.5364192153187316,
        "status": "CAU",
        "location_x": 320.0,
        "location_y": 248.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 130,
        "group": {
            "pk": 44,
            "name": "4I1",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24130",
        "trash_type": "PET",
        "amount": 0.030151482065846724,
        "status": "SAF",
        "location_x": 254.0,
        "location_y": 63.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 131,
        "group": {
            "pk": 44,
            "name": "4I1",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24131",
        "trash_type": "PPR",
        "amount": 0.9103977297270817,
        "status": "WAR",
        "location_x": 274.0,
        "location_y": 63.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 132,
        "group": {
            "pk": 44,
            "name": "4I1",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24132",
        "trash_type": "PET",
        "amount": 0.8916871375730465,
        "status": "WAR",
        "location_x": 314.0,
        "location_y": 63.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 133,
        "group": {
            "pk": 45,
            "name": "4I2",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24133",
        "trash_type": "PET",
        "amount": 0.725413116359147,
        "status": "WAR",
        "location_x": 46.0,
        "location_y": 271.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 134,
        "group": {
            "pk": 45,
            "name": "4I2",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24134",
        "trash_type": "CAN",
        "amount": 0.10745121409483605,
        "status": "SAF",
        "location_x": 46.0,
        "location_y": 291.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 135,
        "group": {
            "pk": 45,
            "name": "4I2",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24135",
        "trash_type": "GER",
        "amount": 0.6752406524532768,
        "status": "CAU",
        "location_x": 46.0,
        "location_y": 331.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 136,
        "group": {
            "pk": 46,
            "name": "4I3",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24136",
        "trash_type": "PPR",
        "amount": 0.6560546961705449,
        "status": "CAU",
        "location_x": 507.0,
        "location_y": 94.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 137,
        "group": {
            "pk": 46,
            "name": "4I3",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24137",
        "trash_type": "PPR",
        "amount": 0.45353300875122093,
        "status": "CAU",
        "location_x": 507.0,
        "location_y": 114.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 138,
        "group": {
            "pk": 46,
            "name": "4I3",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24138",
        "trash_type": "GER",
        "amount": 0.5019321358116946,
        "status": "CAU",
        "location_x": 507.0,
        "location_y": 154.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 139,
        "group": {
            "pk": 47,
            "name": "4I4",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24139",
        "trash_type": "CAN",
        "amount": 0.23704478310257548,
        "status": "SAF",
        "location_x": 339.0,
        "location_y": 228.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 140,
        "group": {
            "pk": 47,
            "name": "4I4",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24140",
        "trash_type": "PPR",
        "amount": 0.5186286597131473,
        "status": "CAU",
        "location_x": 339.0,
        "location_y": 248.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 141,
        "group": {
            "pk": 47,
            "name": "4I4",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24141",
        "trash_type": "PET",
        "amount": 0.9496663051092811,
        "status": "WAR",
        "location_x": 339.0,
        "location_y": 288.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 142,
        "group": {
            "pk": 48,
            "name": "4I5",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24142",
        "trash_type": "PPR",
        "amount": 0.7263565838766266,
        "status": "WAR",
        "location_x": 180.0,
        "location_y": 83.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 143,
        "group": {
            "pk": 48,
            "name": "4I5",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24143",
        "trash_type": "GER",
        "amount": 0.7607267456318832,
        "status": "WAR",
        "location_x": 200.0,
        "location_y": 83.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 144,
        "group": {
            "pk": 48,
            "name": "4I5",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24144",
        "trash_type": "GLA",
        "amount": 0.23219064292639158,
        "status": "SAF",
        "location_x": 240.0,
        "location_y": 83.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 145,
        "group": {
            "pk": 49,
            "name": "4I6",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24145",
        "trash_type": "CAN",
        "amount": 0.807429191508444,
        "status": "WAR",
        "location_x": 122.0,
        "location_y": 316.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 146,
        "group": {
            "pk": 49,
            "name": "4I6",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24146",
        "trash_type": "CAN",
        "amount": 0.6965069829194469,
        "status": "CAU",
        "location_x": 142.0,
        "location_y": 316.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 147,
        "group": {
            "pk": 49,
            "name": "4I6",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24147",
        "trash_type": "PET",
        "amount": 0.6366666511856314,
        "status": "CAU",
        "location_x": 182.0,
        "location_y": 316.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 148,
        "group": {
            "pk": 50,
            "name": "4I7",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24148",
        "trash_type": "PPR",
        "amount": 0.14054993836546903,
        "status": "SAF",
        "location_x": 169.0,
        "location_y": 245.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 149,
        "group": {
            "pk": 50,
            "name": "4I7",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24149",
        "trash_type": "CAN",
        "amount": 0.8469945521149631,
        "status": "WAR",
        "location_x": 189.0,
        "location_y": 245.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 150,
        "group": {
            "pk": 50,
            "name": "4I7",
            "floor": {
                "pk": 9,
                "name": "4",
                "building": {
                    "pk": 2,
                    "name": "어학관"
                }
            }
        },
        "token": "24150",
        "trash_type": "PET",
        "amount": 0.2691173983263836,
        "status": "SAF",
        "location_x": 229.0,
        "location_y": 245.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 151,
        "group": {
            "pk": 51,
            "name": "B2J1",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2151",
        "trash_type": "PET",
        "amount": 0.7027635609619973,
        "status": "WAR",
        "location_x": 503.0,
        "location_y": 135.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 152,
        "group": {
            "pk": 51,
            "name": "B2J1",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2152",
        "trash_type": "GLA",
        "amount": 0.4095030674167167,
        "status": "CAU",
        "location_x": 503.0,
        "location_y": 155.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 153,
        "group": {
            "pk": 51,
            "name": "B2J1",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2153",
        "trash_type": "GLA",
        "amount": 0.5292759909254552,
        "status": "CAU",
        "location_x": 503.0,
        "location_y": 195.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 154,
        "group": {
            "pk": 52,
            "name": "B2J2",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2154",
        "trash_type": "CAN",
        "amount": 0.6344049683085928,
        "status": "CAU",
        "location_x": 317.0,
        "location_y": 51.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 155,
        "group": {
            "pk": 52,
            "name": "B2J2",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2155",
        "trash_type": "PET",
        "amount": 0.9042561165932345,
        "status": "WAR",
        "location_x": 317.0,
        "location_y": 71.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 156,
        "group": {
            "pk": 52,
            "name": "B2J2",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2156",
        "trash_type": "GLA",
        "amount": 0.46101076436986055,
        "status": "CAU",
        "location_x": 317.0,
        "location_y": 111.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 157,
        "group": {
            "pk": 53,
            "name": "B2J3",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2157",
        "trash_type": "CAN",
        "amount": 0.30436296671653473,
        "status": "SAF",
        "location_x": 178.0,
        "location_y": 112.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 158,
        "group": {
            "pk": 53,
            "name": "B2J3",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2158",
        "trash_type": "PET",
        "amount": 0.3558104429262431,
        "status": "SAF",
        "location_x": 178.0,
        "location_y": 132.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 159,
        "group": {
            "pk": 53,
            "name": "B2J3",
            "floor": {
                "pk": 10,
                "name": "B2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B2159",
        "trash_type": "GLA",
        "amount": 0.44831232940106214,
        "status": "CAU",
        "location_x": 178.0,
        "location_y": 172.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 160,
        "group": {
            "pk": 54,
            "name": "B1K1",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1160",
        "trash_type": "CAN",
        "amount": 0.4107764743072123,
        "status": "CAU",
        "location_x": 294.0,
        "location_y": 41.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 161,
        "group": {
            "pk": 54,
            "name": "B1K1",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1161",
        "trash_type": "PET",
        "amount": 0.6891076722605283,
        "status": "CAU",
        "location_x": 294.0,
        "location_y": 61.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 162,
        "group": {
            "pk": 54,
            "name": "B1K1",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1162",
        "trash_type": "CAN",
        "amount": 0.9499353034845859,
        "status": "WAR",
        "location_x": 294.0,
        "location_y": 101.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 163,
        "group": {
            "pk": 55,
            "name": "B1K2",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1163",
        "trash_type": "PPR",
        "amount": 0.12186906646374385,
        "status": "SAF",
        "location_x": 118.0,
        "location_y": 290.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 164,
        "group": {
            "pk": 55,
            "name": "B1K2",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1164",
        "trash_type": "CAN",
        "amount": 0.2560281465186377,
        "status": "SAF",
        "location_x": 138.0,
        "location_y": 290.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 165,
        "group": {
            "pk": 55,
            "name": "B1K2",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1165",
        "trash_type": "PPR",
        "amount": 0.24088618608543721,
        "status": "SAF",
        "location_x": 178.0,
        "location_y": 290.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 166,
        "group": {
            "pk": 56,
            "name": "B1K3",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1166",
        "trash_type": "CAN",
        "amount": 0.9713043947196154,
        "status": "WAR",
        "location_x": 522.0,
        "location_y": 389.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 167,
        "group": {
            "pk": 56,
            "name": "B1K3",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1167",
        "trash_type": "PPR",
        "amount": 0.1417652766457267,
        "status": "SAF",
        "location_x": 522.0,
        "location_y": 409.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 168,
        "group": {
            "pk": 56,
            "name": "B1K3",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1168",
        "trash_type": "PPR",
        "amount": 0.5292279106139278,
        "status": "CAU",
        "location_x": 522.0,
        "location_y": 449.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 169,
        "group": {
            "pk": 57,
            "name": "B1K4",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1169",
        "trash_type": "GLA",
        "amount": 0.5896500293245307,
        "status": "CAU",
        "location_x": 132.0,
        "location_y": 238.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 170,
        "group": {
            "pk": 57,
            "name": "B1K4",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1170",
        "trash_type": "GER",
        "amount": 0.136347533404806,
        "status": "SAF",
        "location_x": 132.0,
        "location_y": 258.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 171,
        "group": {
            "pk": 57,
            "name": "B1K4",
            "floor": {
                "pk": 11,
                "name": "B1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "3B1171",
        "trash_type": "CAN",
        "amount": 0.79586522728717,
        "status": "WAR",
        "location_x": 132.0,
        "location_y": 298.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 172,
        "group": {
            "pk": 58,
            "name": "1L1",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31172",
        "trash_type": "CAN",
        "amount": 0.7259679071494792,
        "status": "WAR",
        "location_x": 102.0,
        "location_y": 186.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 173,
        "group": {
            "pk": 58,
            "name": "1L1",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31173",
        "trash_type": "CAN",
        "amount": 0.5237211234682692,
        "status": "CAU",
        "location_x": 122.0,
        "location_y": 186.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 174,
        "group": {
            "pk": 58,
            "name": "1L1",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31174",
        "trash_type": "GLA",
        "amount": 0.0165255878693501,
        "status": "SAF",
        "location_x": 162.0,
        "location_y": 186.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 175,
        "group": {
            "pk": 59,
            "name": "1L2",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31175",
        "trash_type": "PPR",
        "amount": 0.12288867399908876,
        "status": "SAF",
        "location_x": 413.0,
        "location_y": 272.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 176,
        "group": {
            "pk": 59,
            "name": "1L2",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31176",
        "trash_type": "GER",
        "amount": 0.29790004206348075,
        "status": "SAF",
        "location_x": 413.0,
        "location_y": 292.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 177,
        "group": {
            "pk": 59,
            "name": "1L2",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31177",
        "trash_type": "PPR",
        "amount": 0.15679842475515238,
        "status": "SAF",
        "location_x": 413.0,
        "location_y": 332.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 178,
        "group": {
            "pk": 60,
            "name": "1L3",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31178",
        "trash_type": "PET",
        "amount": 0.8868143928354565,
        "status": "WAR",
        "location_x": 434.0,
        "location_y": 276.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 179,
        "group": {
            "pk": 60,
            "name": "1L3",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31179",
        "trash_type": "GLA",
        "amount": 0.6619322580633576,
        "status": "CAU",
        "location_x": 434.0,
        "location_y": 296.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 180,
        "group": {
            "pk": 60,
            "name": "1L3",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31180",
        "trash_type": "PPR",
        "amount": 0.43765227085382785,
        "status": "CAU",
        "location_x": 434.0,
        "location_y": 336.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 181,
        "group": {
            "pk": 61,
            "name": "1L4",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31181",
        "trash_type": "PET",
        "amount": 0.7524366976570314,
        "status": "WAR",
        "location_x": 494.0,
        "location_y": 112.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 182,
        "group": {
            "pk": 61,
            "name": "1L4",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31182",
        "trash_type": "GLA",
        "amount": 0.19708270837192776,
        "status": "SAF",
        "location_x": 494.0,
        "location_y": 132.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 183,
        "group": {
            "pk": 61,
            "name": "1L4",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31183",
        "trash_type": "GER",
        "amount": 0.10132826181682053,
        "status": "SAF",
        "location_x": 494.0,
        "location_y": 172.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 184,
        "group": {
            "pk": 62,
            "name": "1L5",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31184",
        "trash_type": "GLA",
        "amount": 0.10263170505050356,
        "status": "SAF",
        "location_x": 200.0,
        "location_y": 108.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 185,
        "group": {
            "pk": 62,
            "name": "1L5",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31185",
        "trash_type": "PET",
        "amount": 0.6469181947372326,
        "status": "CAU",
        "location_x": 200.0,
        "location_y": 128.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 186,
        "group": {
            "pk": 62,
            "name": "1L5",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31186",
        "trash_type": "GLA",
        "amount": 0.8610030779361596,
        "status": "WAR",
        "location_x": 200.0,
        "location_y": 168.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 187,
        "group": {
            "pk": 63,
            "name": "1L6",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31187",
        "trash_type": "CAN",
        "amount": 0.30145317446491804,
        "status": "SAF",
        "location_x": 535.0,
        "location_y": 278.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 188,
        "group": {
            "pk": 63,
            "name": "1L6",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31188",
        "trash_type": "GLA",
        "amount": 0.5613632129072745,
        "status": "CAU",
        "location_x": 535.0,
        "location_y": 298.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 189,
        "group": {
            "pk": 63,
            "name": "1L6",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31189",
        "trash_type": "GLA",
        "amount": 0.8873232690017546,
        "status": "WAR",
        "location_x": 535.0,
        "location_y": 338.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 190,
        "group": {
            "pk": 64,
            "name": "1L7",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31190",
        "trash_type": "PET",
        "amount": 0.07881143695657455,
        "status": "SAF",
        "location_x": 509.0,
        "location_y": 161.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 191,
        "group": {
            "pk": 64,
            "name": "1L7",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31191",
        "trash_type": "PET",
        "amount": 0.8571783968625092,
        "status": "WAR",
        "location_x": 509.0,
        "location_y": 181.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 192,
        "group": {
            "pk": 64,
            "name": "1L7",
            "floor": {
                "pk": 12,
                "name": "1",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "31192",
        "trash_type": "GER",
        "amount": 0.45371239627387105,
        "status": "CAU",
        "location_x": 509.0,
        "location_y": 221.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 193,
        "group": {
            "pk": 65,
            "name": "2M1",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32193",
        "trash_type": "PPR",
        "amount": 0.28769510757610384,
        "status": "SAF",
        "location_x": 233.0,
        "location_y": 263.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 194,
        "group": {
            "pk": 65,
            "name": "2M1",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32194",
        "trash_type": "PPR",
        "amount": 0.04101587763362191,
        "status": "SAF",
        "location_x": 253.0,
        "location_y": 263.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 195,
        "group": {
            "pk": 65,
            "name": "2M1",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32195",
        "trash_type": "CAN",
        "amount": 0.6941350537049175,
        "status": "CAU",
        "location_x": 293.0,
        "location_y": 263.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 196,
        "group": {
            "pk": 66,
            "name": "2M2",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32196",
        "trash_type": "CAN",
        "amount": 0.5686739434248805,
        "status": "CAU",
        "location_x": 88.0,
        "location_y": 374.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 197,
        "group": {
            "pk": 66,
            "name": "2M2",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32197",
        "trash_type": "GLA",
        "amount": 0.8245668551845633,
        "status": "WAR",
        "location_x": 88.0,
        "location_y": 394.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 198,
        "group": {
            "pk": 66,
            "name": "2M2",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32198",
        "trash_type": "GLA",
        "amount": 0.9903242617083834,
        "status": "WAR",
        "location_x": 88.0,
        "location_y": 434.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 199,
        "group": {
            "pk": 67,
            "name": "2M3",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32199",
        "trash_type": "PPR",
        "amount": 0.9420830557319827,
        "status": "WAR",
        "location_x": 569.0,
        "location_y": 277.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 200,
        "group": {
            "pk": 67,
            "name": "2M3",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32200",
        "trash_type": "GLA",
        "amount": 0.4133878599257187,
        "status": "CAU",
        "location_x": 569.0,
        "location_y": 297.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 201,
        "group": {
            "pk": 67,
            "name": "2M3",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32201",
        "trash_type": "CAN",
        "amount": 0.5094215150992925,
        "status": "CAU",
        "location_x": 569.0,
        "location_y": 337.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 202,
        "group": {
            "pk": 68,
            "name": "2M4",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32202",
        "trash_type": "CAN",
        "amount": 0.47405269697269226,
        "status": "CAU",
        "location_x": 300.0,
        "location_y": 121.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 203,
        "group": {
            "pk": 68,
            "name": "2M4",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32203",
        "trash_type": "GLA",
        "amount": 0.7164751580320072,
        "status": "WAR",
        "location_x": 320.0,
        "location_y": 121.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 204,
        "group": {
            "pk": 68,
            "name": "2M4",
            "floor": {
                "pk": 13,
                "name": "2",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "32204",
        "trash_type": "PPR",
        "amount": 0.4040298222333639,
        "status": "CAU",
        "location_x": 360.0,
        "location_y": 121.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 205,
        "group": {
            "pk": 69,
            "name": "3N1",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33205",
        "trash_type": "GER",
        "amount": 0.3075750012996875,
        "status": "SAF",
        "location_x": 328.0,
        "location_y": 308.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 206,
        "group": {
            "pk": 69,
            "name": "3N1",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33206",
        "trash_type": "GLA",
        "amount": 0.6264625630710369,
        "status": "CAU",
        "location_x": 328.0,
        "location_y": 328.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 207,
        "group": {
            "pk": 69,
            "name": "3N1",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33207",
        "trash_type": "GER",
        "amount": 0.39216269718407837,
        "status": "SAF",
        "location_x": 328.0,
        "location_y": 368.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 208,
        "group": {
            "pk": 70,
            "name": "3N2",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33208",
        "trash_type": "GER",
        "amount": 0.6212643081693316,
        "status": "CAU",
        "location_x": 200.0,
        "location_y": 141.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 209,
        "group": {
            "pk": 70,
            "name": "3N2",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33209",
        "trash_type": "PET",
        "amount": 0.7719514190697395,
        "status": "WAR",
        "location_x": 200.0,
        "location_y": 161.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 210,
        "group": {
            "pk": 70,
            "name": "3N2",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33210",
        "trash_type": "GER",
        "amount": 0.06679545156316102,
        "status": "SAF",
        "location_x": 200.0,
        "location_y": 201.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 211,
        "group": {
            "pk": 71,
            "name": "3N3",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33211",
        "trash_type": "GLA",
        "amount": 0.397428291120825,
        "status": "SAF",
        "location_x": 245.0,
        "location_y": 221.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 212,
        "group": {
            "pk": 71,
            "name": "3N3",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33212",
        "trash_type": "GER",
        "amount": 0.7854937215073889,
        "status": "WAR",
        "location_x": 245.0,
        "location_y": 241.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 213,
        "group": {
            "pk": 71,
            "name": "3N3",
            "floor": {
                "pk": 14,
                "name": "3",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "33213",
        "trash_type": "PPR",
        "amount": 0.5829032787573435,
        "status": "CAU",
        "location_x": 245.0,
        "location_y": 281.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 214,
        "group": {
            "pk": 72,
            "name": "4O1",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34214",
        "trash_type": "CAN",
        "amount": 0.9575204014584047,
        "status": "WAR",
        "location_x": 263.0,
        "location_y": 135.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 215,
        "group": {
            "pk": 72,
            "name": "4O1",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34215",
        "trash_type": "CAN",
        "amount": 0.7930599613566349,
        "status": "WAR",
        "location_x": 283.0,
        "location_y": 135.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 216,
        "group": {
            "pk": 72,
            "name": "4O1",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34216",
        "trash_type": "GLA",
        "amount": 0.02356643041879558,
        "status": "SAF",
        "location_x": 323.0,
        "location_y": 135.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 217,
        "group": {
            "pk": 73,
            "name": "4O2",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34217",
        "trash_type": "PPR",
        "amount": 0.7737530951926597,
        "status": "WAR",
        "location_x": 138.0,
        "location_y": 86.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 218,
        "group": {
            "pk": 73,
            "name": "4O2",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34218",
        "trash_type": "GLA",
        "amount": 0.7769947917147239,
        "status": "WAR",
        "location_x": 138.0,
        "location_y": 106.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 219,
        "group": {
            "pk": 73,
            "name": "4O2",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34219",
        "trash_type": "CAN",
        "amount": 0.930472055252812,
        "status": "WAR",
        "location_x": 138.0,
        "location_y": 146.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 220,
        "group": {
            "pk": 74,
            "name": "4O3",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34220",
        "trash_type": "GLA",
        "amount": 0.4479014987287949,
        "status": "CAU",
        "location_x": 386.0,
        "location_y": 47.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 221,
        "group": {
            "pk": 74,
            "name": "4O3",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34221",
        "trash_type": "CAN",
        "amount": 0.5559700523886743,
        "status": "CAU",
        "location_x": 406.0,
        "location_y": 47.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 222,
        "group": {
            "pk": 74,
            "name": "4O3",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34222",
        "trash_type": "CAN",
        "amount": 0.07385983630109916,
        "status": "SAF",
        "location_x": 446.0,
        "location_y": 47.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 223,
        "group": {
            "pk": 75,
            "name": "4O4",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34223",
        "trash_type": "GLA",
        "amount": 0.3453727380287166,
        "status": "SAF",
        "location_x": 570.0,
        "location_y": 190.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 224,
        "group": {
            "pk": 75,
            "name": "4O4",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34224",
        "trash_type": "GER",
        "amount": 0.3887902221153229,
        "status": "SAF",
        "location_x": 590.0,
        "location_y": 190.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 225,
        "group": {
            "pk": 75,
            "name": "4O4",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34225",
        "trash_type": "GLA",
        "amount": 0.7974563524076161,
        "status": "WAR",
        "location_x": 630.0,
        "location_y": 190.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 226,
        "group": {
            "pk": 76,
            "name": "4O5",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34226",
        "trash_type": "PET",
        "amount": 0.883728892529779,
        "status": "WAR",
        "location_x": 404.0,
        "location_y": 64.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 227,
        "group": {
            "pk": 76,
            "name": "4O5",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34227",
        "trash_type": "GER",
        "amount": 0.6648449573580549,
        "status": "CAU",
        "location_x": 424.0,
        "location_y": 64.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 228,
        "group": {
            "pk": 76,
            "name": "4O5",
            "floor": {
                "pk": 15,
                "name": "4",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "34228",
        "trash_type": "GLA",
        "amount": 0.43384125118093375,
        "status": "CAU",
        "location_x": 464.0,
        "location_y": 64.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 229,
        "group": {
            "pk": 77,
            "name": "5P1",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35229",
        "trash_type": "GER",
        "amount": 0.12099288712952672,
        "status": "SAF",
        "location_x": 265.0,
        "location_y": 105.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 230,
        "group": {
            "pk": 77,
            "name": "5P1",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35230",
        "trash_type": "GLA",
        "amount": 0.5031031628458539,
        "status": "CAU",
        "location_x": 265.0,
        "location_y": 125.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 231,
        "group": {
            "pk": 77,
            "name": "5P1",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35231",
        "trash_type": "GER",
        "amount": 0.879182661994193,
        "status": "WAR",
        "location_x": 265.0,
        "location_y": 165.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 232,
        "group": {
            "pk": 78,
            "name": "5P2",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35232",
        "trash_type": "GLA",
        "amount": 0.7921571104799843,
        "status": "WAR",
        "location_x": 484.0,
        "location_y": 98.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 233,
        "group": {
            "pk": 78,
            "name": "5P2",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35233",
        "trash_type": "PET",
        "amount": 0.41698883100064543,
        "status": "CAU",
        "location_x": 484.0,
        "location_y": 118.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 234,
        "group": {
            "pk": 78,
            "name": "5P2",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35234",
        "trash_type": "GLA",
        "amount": 0.20642026995713136,
        "status": "SAF",
        "location_x": 484.0,
        "location_y": 158.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 235,
        "group": {
            "pk": 79,
            "name": "5P3",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35235",
        "trash_type": "GER",
        "amount": 0.38144844721125826,
        "status": "SAF",
        "location_x": 454.0,
        "location_y": 256.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 236,
        "group": {
            "pk": 79,
            "name": "5P3",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35236",
        "trash_type": "PPR",
        "amount": 0.7362997501868584,
        "status": "WAR",
        "location_x": 474.0,
        "location_y": 256.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 237,
        "group": {
            "pk": 79,
            "name": "5P3",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35237",
        "trash_type": "GLA",
        "amount": 0.9653959927493361,
        "status": "WAR",
        "location_x": 514.0,
        "location_y": 256.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 238,
        "group": {
            "pk": 80,
            "name": "5P4",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35238",
        "trash_type": "GLA",
        "amount": 0.046117359192197394,
        "status": "SAF",
        "location_x": 52.0,
        "location_y": 46.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 239,
        "group": {
            "pk": 80,
            "name": "5P4",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35239",
        "trash_type": "PET",
        "amount": 0.018145172067134174,
        "status": "SAF",
        "location_x": 72.0,
        "location_y": 46.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 240,
        "group": {
            "pk": 80,
            "name": "5P4",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35240",
        "trash_type": "PET",
        "amount": 0.258145802884173,
        "status": "SAF",
        "location_x": 112.0,
        "location_y": 46.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 241,
        "group": {
            "pk": 81,
            "name": "5P5",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35241",
        "trash_type": "GLA",
        "amount": 0.9683316933941393,
        "status": "WAR",
        "location_x": 485.0,
        "location_y": 251.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 242,
        "group": {
            "pk": 81,
            "name": "5P5",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35242",
        "trash_type": "GLA",
        "amount": 0.8770709150732251,
        "status": "WAR",
        "location_x": 505.0,
        "location_y": 251.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 243,
        "group": {
            "pk": 81,
            "name": "5P5",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35243",
        "trash_type": "PPR",
        "amount": 0.5158317431186054,
        "status": "CAU",
        "location_x": 545.0,
        "location_y": 251.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 244,
        "group": {
            "pk": 82,
            "name": "5P6",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35244",
        "trash_type": "GLA",
        "amount": 0.9221875829571254,
        "status": "WAR",
        "location_x": 272.0,
        "location_y": 30.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 245,
        "group": {
            "pk": 82,
            "name": "5P6",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35245",
        "trash_type": "PPR",
        "amount": 0.583722633818624,
        "status": "CAU",
        "location_x": 272.0,
        "location_y": 50.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 246,
        "group": {
            "pk": 82,
            "name": "5P6",
            "floor": {
                "pk": 16,
                "name": "5",
                "building": {
                    "pk": 3,
                    "name": "경영대학관"
                }
            }
        },
        "token": "35246",
        "trash_type": "GER",
        "amount": 0.07165943270940112,
        "status": "SAF",
        "location_x": 272.0,
        "location_y": 90.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 247,
        "group": {
            "pk": 83,
            "name": "B2Q1",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2247",
        "trash_type": "GLA",
        "amount": 0.18166836105201667,
        "status": "SAF",
        "location_x": 226.0,
        "location_y": 94.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 248,
        "group": {
            "pk": 83,
            "name": "B2Q1",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2248",
        "trash_type": "GLA",
        "amount": 0.8038602130231041,
        "status": "WAR",
        "location_x": 246.0,
        "location_y": 94.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 249,
        "group": {
            "pk": 83,
            "name": "B2Q1",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2249",
        "trash_type": "PPR",
        "amount": 0.39271096177280274,
        "status": "SAF",
        "location_x": 286.0,
        "location_y": 94.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 250,
        "group": {
            "pk": 84,
            "name": "B2Q2",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2250",
        "trash_type": "PET",
        "amount": 0.19778684484816145,
        "status": "SAF",
        "location_x": 194.0,
        "location_y": 280.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 251,
        "group": {
            "pk": 84,
            "name": "B2Q2",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2251",
        "trash_type": "GLA",
        "amount": 0.5935232355086217,
        "status": "CAU",
        "location_x": 194.0,
        "location_y": 300.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 252,
        "group": {
            "pk": 84,
            "name": "B2Q2",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2252",
        "trash_type": "CAN",
        "amount": 0.06876482305525466,
        "status": "SAF",
        "location_x": 194.0,
        "location_y": 340.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 253,
        "group": {
            "pk": 85,
            "name": "B2Q3",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2253",
        "trash_type": "PPR",
        "amount": 0.08251731827455544,
        "status": "SAF",
        "location_x": 422.0,
        "location_y": 220.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 254,
        "group": {
            "pk": 85,
            "name": "B2Q3",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2254",
        "trash_type": "GER",
        "amount": 0.5298541338482131,
        "status": "CAU",
        "location_x": 422.0,
        "location_y": 240.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 255,
        "group": {
            "pk": 85,
            "name": "B2Q3",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2255",
        "trash_type": "PPR",
        "amount": 0.967297351179369,
        "status": "WAR",
        "location_x": 422.0,
        "location_y": 280.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 256,
        "group": {
            "pk": 86,
            "name": "B2Q4",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2256",
        "trash_type": "GLA",
        "amount": 0.701450632022496,
        "status": "WAR",
        "location_x": 296.0,
        "location_y": 235.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 257,
        "group": {
            "pk": 86,
            "name": "B2Q4",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2257",
        "trash_type": "PPR",
        "amount": 0.4684075057539425,
        "status": "CAU",
        "location_x": 316.0,
        "location_y": 235.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 258,
        "group": {
            "pk": 86,
            "name": "B2Q4",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2258",
        "trash_type": "PPR",
        "amount": 0.3278475385391255,
        "status": "SAF",
        "location_x": 356.0,
        "location_y": 235.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 259,
        "group": {
            "pk": 87,
            "name": "B2Q5",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2259",
        "trash_type": "PET",
        "amount": 0.7434253708706702,
        "status": "WAR",
        "location_x": 93.0,
        "location_y": 149.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 260,
        "group": {
            "pk": 87,
            "name": "B2Q5",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2260",
        "trash_type": "PET",
        "amount": 0.909246576413567,
        "status": "WAR",
        "location_x": 93.0,
        "location_y": 169.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 261,
        "group": {
            "pk": 87,
            "name": "B2Q5",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2261",
        "trash_type": "GER",
        "amount": 0.14050967380182267,
        "status": "SAF",
        "location_x": 93.0,
        "location_y": 209.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 262,
        "group": {
            "pk": 88,
            "name": "B2Q6",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2262",
        "trash_type": "CAN",
        "amount": 0.3555179618216655,
        "status": "SAF",
        "location_x": 470.0,
        "location_y": 153.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 263,
        "group": {
            "pk": 88,
            "name": "B2Q6",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2263",
        "trash_type": "PPR",
        "amount": 0.362709976389316,
        "status": "SAF",
        "location_x": 490.0,
        "location_y": 153.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 264,
        "group": {
            "pk": 88,
            "name": "B2Q6",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2264",
        "trash_type": "GLA",
        "amount": 0.6078873360740806,
        "status": "CAU",
        "location_x": 530.0,
        "location_y": 153.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 265,
        "group": {
            "pk": 89,
            "name": "B2Q7",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2265",
        "trash_type": "GLA",
        "amount": 0.7442642497126192,
        "status": "WAR",
        "location_x": 391.0,
        "location_y": 36.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 266,
        "group": {
            "pk": 89,
            "name": "B2Q7",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2266",
        "trash_type": "PPR",
        "amount": 0.7559308402024192,
        "status": "WAR",
        "location_x": 391.0,
        "location_y": 56.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 267,
        "group": {
            "pk": 89,
            "name": "B2Q7",
            "floor": {
                "pk": 17,
                "name": "B2",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B2267",
        "trash_type": "GER",
        "amount": 0.7799289229134159,
        "status": "WAR",
        "location_x": 391.0,
        "location_y": 96.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 268,
        "group": {
            "pk": 90,
            "name": "B1R1",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1268",
        "trash_type": "GER",
        "amount": 0.8065566501575612,
        "status": "WAR",
        "location_x": 413.0,
        "location_y": 56.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 269,
        "group": {
            "pk": 90,
            "name": "B1R1",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1269",
        "trash_type": "GLA",
        "amount": 0.010928830108053567,
        "status": "SAF",
        "location_x": 413.0,
        "location_y": 76.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 270,
        "group": {
            "pk": 90,
            "name": "B1R1",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1270",
        "trash_type": "PET",
        "amount": 0.1946610013910065,
        "status": "SAF",
        "location_x": 413.0,
        "location_y": 116.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 271,
        "group": {
            "pk": 91,
            "name": "B1R2",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1271",
        "trash_type": "CAN",
        "amount": 0.5531533555332754,
        "status": "CAU",
        "location_x": 305.0,
        "location_y": 381.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 272,
        "group": {
            "pk": 91,
            "name": "B1R2",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1272",
        "trash_type": "PPR",
        "amount": 0.5767720792588132,
        "status": "CAU",
        "location_x": 305.0,
        "location_y": 401.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 273,
        "group": {
            "pk": 91,
            "name": "B1R2",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1273",
        "trash_type": "PPR",
        "amount": 0.4601943803796288,
        "status": "CAU",
        "location_x": 305.0,
        "location_y": 441.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 274,
        "group": {
            "pk": 92,
            "name": "B1R3",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1274",
        "trash_type": "GLA",
        "amount": 0.5550847308581259,
        "status": "CAU",
        "location_x": 381.0,
        "location_y": 332.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 275,
        "group": {
            "pk": 92,
            "name": "B1R3",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1275",
        "trash_type": "GER",
        "amount": 0.7358563407480112,
        "status": "WAR",
        "location_x": 381.0,
        "location_y": 352.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 276,
        "group": {
            "pk": 92,
            "name": "B1R3",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1276",
        "trash_type": "PET",
        "amount": 0.20338993405546235,
        "status": "SAF",
        "location_x": 381.0,
        "location_y": 392.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 277,
        "group": {
            "pk": 93,
            "name": "B1R4",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1277",
        "trash_type": "GER",
        "amount": 0.4078581468807042,
        "status": "CAU",
        "location_x": 309.0,
        "location_y": 213.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 278,
        "group": {
            "pk": 93,
            "name": "B1R4",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1278",
        "trash_type": "GLA",
        "amount": 0.25964520231856203,
        "status": "SAF",
        "location_x": 309.0,
        "location_y": 233.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 279,
        "group": {
            "pk": 93,
            "name": "B1R4",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1279",
        "trash_type": "GLA",
        "amount": 0.06271719612629079,
        "status": "SAF",
        "location_x": 309.0,
        "location_y": 273.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 280,
        "group": {
            "pk": 94,
            "name": "B1R5",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1280",
        "trash_type": "PPR",
        "amount": 0.8188949929364439,
        "status": "WAR",
        "location_x": 425.0,
        "location_y": 116.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 281,
        "group": {
            "pk": 94,
            "name": "B1R5",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1281",
        "trash_type": "GER",
        "amount": 0.9601507644697856,
        "status": "WAR",
        "location_x": 445.0,
        "location_y": 116.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 282,
        "group": {
            "pk": 94,
            "name": "B1R5",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1282",
        "trash_type": "GLA",
        "amount": 0.8302734754511635,
        "status": "WAR",
        "location_x": 485.0,
        "location_y": 116.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 283,
        "group": {
            "pk": 95,
            "name": "B1R6",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1283",
        "trash_type": "GLA",
        "amount": 0.27430157090211316,
        "status": "SAF",
        "location_x": 219.0,
        "location_y": 279.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 284,
        "group": {
            "pk": 95,
            "name": "B1R6",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1284",
        "trash_type": "PET",
        "amount": 0.06387329917818407,
        "status": "SAF",
        "location_x": 219.0,
        "location_y": 299.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 285,
        "group": {
            "pk": 95,
            "name": "B1R6",
            "floor": {
                "pk": 18,
                "name": "B1",
                "building": {
                    "pk": 4,
                    "name": "체육관"
                }
            }
        },
        "token": "4B1285",
        "trash_type": "CAN",
        "amount": 0.7130344193521503,
        "status": "WAR",
        "location_x": 219.0,
        "location_y": 339.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 286,
        "group": {
            "pk": 96,
            "name": "B2S1",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2286",
        "trash_type": "GLA",
        "amount": 0.30726528933941144,
        "status": "SAF",
        "location_x": 363.0,
        "location_y": 374.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 287,
        "group": {
            "pk": 96,
            "name": "B2S1",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2287",
        "trash_type": "PPR",
        "amount": 0.7511361246977953,
        "status": "WAR",
        "location_x": 363.0,
        "location_y": 394.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 288,
        "group": {
            "pk": 96,
            "name": "B2S1",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2288",
        "trash_type": "CAN",
        "amount": 0.04820177393300096,
        "status": "SAF",
        "location_x": 363.0,
        "location_y": 434.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 289,
        "group": {
            "pk": 97,
            "name": "B2S2",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2289",
        "trash_type": "GLA",
        "amount": 0.789709830429439,
        "status": "WAR",
        "location_x": 76.0,
        "location_y": 151.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 290,
        "group": {
            "pk": 97,
            "name": "B2S2",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2290",
        "trash_type": "GLA",
        "amount": 0.908753893988703,
        "status": "WAR",
        "location_x": 96.0,
        "location_y": 151.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 291,
        "group": {
            "pk": 97,
            "name": "B2S2",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2291",
        "trash_type": "PPR",
        "amount": 0.2923457685229297,
        "status": "SAF",
        "location_x": 136.0,
        "location_y": 151.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 292,
        "group": {
            "pk": 98,
            "name": "B2S3",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2292",
        "trash_type": "CAN",
        "amount": 0.9890142992985916,
        "status": "WAR",
        "location_x": 528.0,
        "location_y": 137.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 293,
        "group": {
            "pk": 98,
            "name": "B2S3",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2293",
        "trash_type": "GLA",
        "amount": 0.4837031224347089,
        "status": "CAU",
        "location_x": 548.0,
        "location_y": 137.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 294,
        "group": {
            "pk": 98,
            "name": "B2S3",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2294",
        "trash_type": "PPR",
        "amount": 0.7455603147964904,
        "status": "WAR",
        "location_x": 588.0,
        "location_y": 137.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 295,
        "group": {
            "pk": 99,
            "name": "B2S4",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2295",
        "trash_type": "GER",
        "amount": 0.03639316177090168,
        "status": "SAF",
        "location_x": 32.0,
        "location_y": 382.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 296,
        "group": {
            "pk": 99,
            "name": "B2S4",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2296",
        "trash_type": "GLA",
        "amount": 0.39356789739317155,
        "status": "SAF",
        "location_x": 32.0,
        "location_y": 402.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 297,
        "group": {
            "pk": 99,
            "name": "B2S4",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2297",
        "trash_type": "CAN",
        "amount": 0.36382308763929194,
        "status": "SAF",
        "location_x": 32.0,
        "location_y": 442.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 298,
        "group": {
            "pk": 100,
            "name": "B2S5",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2298",
        "trash_type": "GLA",
        "amount": 0.038588978939567364,
        "status": "SAF",
        "location_x": 407.0,
        "location_y": 67.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 299,
        "group": {
            "pk": 100,
            "name": "B2S5",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2299",
        "trash_type": "CAN",
        "amount": 0.6388814636866537,
        "status": "CAU",
        "location_x": 407.0,
        "location_y": 87.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 300,
        "group": {
            "pk": 100,
            "name": "B2S5",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2300",
        "trash_type": "PPR",
        "amount": 0.7281343881224012,
        "status": "WAR",
        "location_x": 407.0,
        "location_y": 127.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 301,
        "group": {
            "pk": 101,
            "name": "B2S6",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2301",
        "trash_type": "PET",
        "amount": 0.6085918962010554,
        "status": "CAU",
        "location_x": 35.0,
        "location_y": 349.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 302,
        "group": {
            "pk": 101,
            "name": "B2S6",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2302",
        "trash_type": "GER",
        "amount": 0.23712579829481284,
        "status": "SAF",
        "location_x": 55.0,
        "location_y": 349.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 303,
        "group": {
            "pk": 101,
            "name": "B2S6",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2303",
        "trash_type": "GLA",
        "amount": 0.6704798559734465,
        "status": "CAU",
        "location_x": 95.0,
        "location_y": 349.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 304,
        "group": {
            "pk": 102,
            "name": "B2S7",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2304",
        "trash_type": "CAN",
        "amount": 0.9143125355650127,
        "status": "WAR",
        "location_x": 412.0,
        "location_y": 302.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 305,
        "group": {
            "pk": 102,
            "name": "B2S7",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2305",
        "trash_type": "PPR",
        "amount": 0.5552524087385153,
        "status": "CAU",
        "location_x": 412.0,
        "location_y": 322.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 306,
        "group": {
            "pk": 102,
            "name": "B2S7",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2306",
        "trash_type": "PPR",
        "amount": 0.8564004275336051,
        "status": "WAR",
        "location_x": 412.0,
        "location_y": 362.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 307,
        "group": {
            "pk": 103,
            "name": "B2S8",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2307",
        "trash_type": "PPR",
        "amount": 0.13505300891057892,
        "status": "SAF",
        "location_x": 199.0,
        "location_y": 220.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 308,
        "group": {
            "pk": 103,
            "name": "B2S8",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2308",
        "trash_type": "PET",
        "amount": 0.5740920949297365,
        "status": "CAU",
        "location_x": 199.0,
        "location_y": 240.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 309,
        "group": {
            "pk": 103,
            "name": "B2S8",
            "floor": {
                "pk": 19,
                "name": "B2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B2309",
        "trash_type": "GLA",
        "amount": 0.5723021776782279,
        "status": "CAU",
        "location_x": 199.0,
        "location_y": 280.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 310,
        "group": {
            "pk": 104,
            "name": "B1T1",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1310",
        "trash_type": "GLA",
        "amount": 0.7454562472824097,
        "status": "WAR",
        "location_x": 279.0,
        "location_y": 311.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 311,
        "group": {
            "pk": 104,
            "name": "B1T1",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1311",
        "trash_type": "PPR",
        "amount": 0.2673492678977568,
        "status": "SAF",
        "location_x": 279.0,
        "location_y": 331.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 312,
        "group": {
            "pk": 104,
            "name": "B1T1",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1312",
        "trash_type": "CAN",
        "amount": 0.5807971928056717,
        "status": "CAU",
        "location_x": 279.0,
        "location_y": 371.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 313,
        "group": {
            "pk": 105,
            "name": "B1T2",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1313",
        "trash_type": "PET",
        "amount": 0.3460510527035482,
        "status": "SAF",
        "location_x": 101.0,
        "location_y": 380.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 314,
        "group": {
            "pk": 105,
            "name": "B1T2",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1314",
        "trash_type": "PET",
        "amount": 0.3570461011316848,
        "status": "SAF",
        "location_x": 101.0,
        "location_y": 400.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 315,
        "group": {
            "pk": 105,
            "name": "B1T2",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1315",
        "trash_type": "PPR",
        "amount": 0.22864766923274082,
        "status": "SAF",
        "location_x": 101.0,
        "location_y": 440.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 316,
        "group": {
            "pk": 106,
            "name": "B1T3",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1316",
        "trash_type": "CAN",
        "amount": 0.5978451295835987,
        "status": "CAU",
        "location_x": 543.0,
        "location_y": 280.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 317,
        "group": {
            "pk": 106,
            "name": "B1T3",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1317",
        "trash_type": "PPR",
        "amount": 0.672605685833018,
        "status": "CAU",
        "location_x": 563.0,
        "location_y": 280.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 318,
        "group": {
            "pk": 106,
            "name": "B1T3",
            "floor": {
                "pk": 20,
                "name": "B1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "5B1318",
        "trash_type": "GER",
        "amount": 0.8491992832702567,
        "status": "WAR",
        "location_x": 603.0,
        "location_y": 280.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 319,
        "group": {
            "pk": 107,
            "name": "1U1",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51319",
        "trash_type": "PPR",
        "amount": 0.9601372687555876,
        "status": "WAR",
        "location_x": 493.0,
        "location_y": 268.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 320,
        "group": {
            "pk": 107,
            "name": "1U1",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51320",
        "trash_type": "PPR",
        "amount": 0.881140006499327,
        "status": "WAR",
        "location_x": 493.0,
        "location_y": 288.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 321,
        "group": {
            "pk": 107,
            "name": "1U1",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51321",
        "trash_type": "PPR",
        "amount": 0.3245651135023222,
        "status": "SAF",
        "location_x": 493.0,
        "location_y": 328.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 322,
        "group": {
            "pk": 108,
            "name": "1U2",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51322",
        "trash_type": "GER",
        "amount": 0.9058007533312588,
        "status": "WAR",
        "location_x": 563.0,
        "location_y": 224.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 323,
        "group": {
            "pk": 108,
            "name": "1U2",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51323",
        "trash_type": "GER",
        "amount": 0.769926553286807,
        "status": "WAR",
        "location_x": 563.0,
        "location_y": 244.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 324,
        "group": {
            "pk": 108,
            "name": "1U2",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51324",
        "trash_type": "GER",
        "amount": 0.9643030710662714,
        "status": "WAR",
        "location_x": 563.0,
        "location_y": 284.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 325,
        "group": {
            "pk": 109,
            "name": "1U3",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51325",
        "trash_type": "GER",
        "amount": 0.7884147790971247,
        "status": "WAR",
        "location_x": 527.0,
        "location_y": 254.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 326,
        "group": {
            "pk": 109,
            "name": "1U3",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51326",
        "trash_type": "GER",
        "amount": 0.7404183154715281,
        "status": "WAR",
        "location_x": 547.0,
        "location_y": 254.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 327,
        "group": {
            "pk": 109,
            "name": "1U3",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51327",
        "trash_type": "GLA",
        "amount": 0.08842609793023781,
        "status": "SAF",
        "location_x": 587.0,
        "location_y": 254.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 328,
        "group": {
            "pk": 110,
            "name": "1U4",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51328",
        "trash_type": "PPR",
        "amount": 0.37951382718936466,
        "status": "SAF",
        "location_x": 40.0,
        "location_y": 256.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 329,
        "group": {
            "pk": 110,
            "name": "1U4",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51329",
        "trash_type": "PET",
        "amount": 0.04972923040990507,
        "status": "SAF",
        "location_x": 60.0,
        "location_y": 256.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 330,
        "group": {
            "pk": 110,
            "name": "1U4",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51330",
        "trash_type": "GLA",
        "amount": 0.03666832516956908,
        "status": "SAF",
        "location_x": 100.0,
        "location_y": 256.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 331,
        "group": {
            "pk": 111,
            "name": "1U5",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51331",
        "trash_type": "PET",
        "amount": 0.7805725364919214,
        "status": "WAR",
        "location_x": 560.0,
        "location_y": 144.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 332,
        "group": {
            "pk": 111,
            "name": "1U5",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51332",
        "trash_type": "PET",
        "amount": 0.5237138363037519,
        "status": "CAU",
        "location_x": 560.0,
        "location_y": 164.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 333,
        "group": {
            "pk": 111,
            "name": "1U5",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51333",
        "trash_type": "GER",
        "amount": 0.16945749664069687,
        "status": "SAF",
        "location_x": 560.0,
        "location_y": 204.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 334,
        "group": {
            "pk": 112,
            "name": "1U6",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51334",
        "trash_type": "CAN",
        "amount": 0.4148606628059388,
        "status": "CAU",
        "location_x": 160.0,
        "location_y": 144.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 335,
        "group": {
            "pk": 112,
            "name": "1U6",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51335",
        "trash_type": "PPR",
        "amount": 0.4301502269371532,
        "status": "CAU",
        "location_x": 180.0,
        "location_y": 144.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 336,
        "group": {
            "pk": 112,
            "name": "1U6",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51336",
        "trash_type": "CAN",
        "amount": 0.028662039045037058,
        "status": "SAF",
        "location_x": 220.0,
        "location_y": 144.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 337,
        "group": {
            "pk": 113,
            "name": "1U7",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51337",
        "trash_type": "GLA",
        "amount": 0.7588785552801405,
        "status": "WAR",
        "location_x": 332.0,
        "location_y": 130.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 338,
        "group": {
            "pk": 113,
            "name": "1U7",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51338",
        "trash_type": "GER",
        "amount": 0.2837271024200315,
        "status": "SAF",
        "location_x": 352.0,
        "location_y": 130.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 339,
        "group": {
            "pk": 113,
            "name": "1U7",
            "floor": {
                "pk": 21,
                "name": "1",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "51339",
        "trash_type": "PET",
        "amount": 0.4299067374127683,
        "status": "CAU",
        "location_x": 392.0,
        "location_y": 130.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 340,
        "group": {
            "pk": 114,
            "name": "2V1",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52340",
        "trash_type": "GLA",
        "amount": 0.16982282928557724,
        "status": "SAF",
        "location_x": 234.0,
        "location_y": 92.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 341,
        "group": {
            "pk": 114,
            "name": "2V1",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52341",
        "trash_type": "CAN",
        "amount": 0.7383321456036652,
        "status": "WAR",
        "location_x": 234.0,
        "location_y": 112.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 342,
        "group": {
            "pk": 114,
            "name": "2V1",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52342",
        "trash_type": "CAN",
        "amount": 0.2071794657424667,
        "status": "SAF",
        "location_x": 234.0,
        "location_y": 152.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 343,
        "group": {
            "pk": 115,
            "name": "2V2",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52343",
        "trash_type": "PET",
        "amount": 0.6326609063449934,
        "status": "CAU",
        "location_x": 436.0,
        "location_y": 387.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 344,
        "group": {
            "pk": 115,
            "name": "2V2",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52344",
        "trash_type": "GER",
        "amount": 0.9623836341788322,
        "status": "WAR",
        "location_x": 436.0,
        "location_y": 407.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 345,
        "group": {
            "pk": 115,
            "name": "2V2",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52345",
        "trash_type": "CAN",
        "amount": 0.2661571109793811,
        "status": "SAF",
        "location_x": 436.0,
        "location_y": 447.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 346,
        "group": {
            "pk": 116,
            "name": "2V3",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52346",
        "trash_type": "GER",
        "amount": 0.8357891632951411,
        "status": "WAR",
        "location_x": 582.0,
        "location_y": 194.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 347,
        "group": {
            "pk": 116,
            "name": "2V3",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52347",
        "trash_type": "GLA",
        "amount": 0.29346560847533576,
        "status": "SAF",
        "location_x": 582.0,
        "location_y": 214.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    },
    {
        "id": 348,
        "group": {
            "pk": 116,
            "name": "2V3",
            "floor": {
                "pk": 22,
                "name": "2",
                "building": {
                    "pk": 5,
                    "name": "중앙도서관"
                }
            }
        },
        "token": "52348",
        "trash_type": "GER",
        "amount": 0.47077815755859,
        "status": "CAU",
        "location_x": 582.0,
        "location_y": 254.0,
        "created_at": "2022-08-12T21:42:33.643848+09:00",
        "updated_at": "2022-08-12T21:42:33.643848+09:00",
        "discard_users": []
    }
]

for i in range(5, 9):
    if i == 6:
        nn = 31
    elif i == 8:
        nn = 13
    else:
        nn = 32
    for j in range(1, nn):        
        dd = '0' + str(j) if len(str(j)) == 1 else str(j)
        day = '20220' + str(i) + dd
        cnt = 0
        data = ''
        while cnt < 1000:
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
            sen = f'{day} {time} {target["group"]["floor"]["building"]["name"]} {target["group"]["floor"]["building"]["pk"]} {target["group"]["floor"]["name"]} {target["group"]["floor"]["pk"]} {target["token"]} {target["trash_type"]} {rand_zero+rand_rfid} {target["amount"]}'
            data += sen
            data += '\n'
            target["amount"] = random.random()
            cnt += 1

        f = open(f'20220{str(i)+dd}', 'w', encoding='UTF-8')
        f.write(data)
        f.close()