import random

trash_list = [
    {
        "id": 1,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B1GER1",
        "trash_type": "PET",
        "amount": 0.36410439035977804,
        "status": "SAF",
        "location_x": 193.0,
        "location_y": 318.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 2,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B1PET2",
        "trash_type": "CAN",
        "amount": 0.8834496492009626,
        "status": "WAR",
        "location_x": 601.0,
        "location_y": 245.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 3,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B1CAN3",
        "trash_type": "GLA",
        "amount": 0.6174855911451103,
        "status": "CAU",
        "location_x": 390.0,
        "location_y": 328.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 4,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B1GLA4",
        "trash_type": "GER",
        "amount": 0.6870223673904081,
        "status": "CAU",
        "location_x": 141.0,
        "location_y": 71.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 5,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B1PPR5",
        "trash_type": "PPR",
        "amount": 0.05545018283309777,
        "status": "SAF",
        "location_x": 345.0,
        "location_y": 385.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 6,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B2GER6",
        "trash_type": "CAN",
        "amount": 0.8750065274599773,
        "status": "WAR",
        "location_x": 432.0,
        "location_y": 68.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 7,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B2PET7",
        "trash_type": "PET",
        "amount": 0.9786272350225013,
        "status": "WAR",
        "location_x": 355.0,
        "location_y": 290.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 8,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B2CAN8",
        "trash_type": "CAN",
        "amount": 0.04169305551492919,
        "status": "SAF",
        "location_x": 166.0,
        "location_y": 260.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 9,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B2GLA9",
        "trash_type": "GER",
        "amount": 0.49996978936830117,
        "status": "CAU",
        "location_x": 525.0,
        "location_y": 444.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 10,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "1B2PPR10",
        "trash_type": "PET",
        "amount": 0.3510793182596492,
        "status": "SAF",
        "location_x": 511.0,
        "location_y": 160.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 11,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "11GER11",
        "trash_type": "CAN",
        "amount": 0.7150418984541856,
        "status": "WAR",
        "location_x": 553.0,
        "location_y": 186.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 12,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "11PET12",
        "trash_type": "PET",
        "amount": 0.6090723725020453,
        "status": "CAU",
        "location_x": 435.0,
        "location_y": 232.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 13,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "11CAN13",
        "trash_type": "PET",
        "amount": 0.22617629915602233,
        "status": "SAF",
        "location_x": 573.0,
        "location_y": 304.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 14,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "11GLA14",
        "trash_type": "PET",
        "amount": 0.7880095453344461,
        "status": "WAR",
        "location_x": 314.0,
        "location_y": 221.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 15,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "11PPR15",
        "trash_type": "CAN",
        "amount": 0.9571089621238394,
        "status": "WAR",
        "location_x": 152.0,
        "location_y": 444.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 16,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "12GER16",
        "trash_type": "CAN",
        "amount": 0.5293151483766056,
        "status": "CAU",
        "location_x": 573.0,
        "location_y": 61.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 17,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "12PET17",
        "trash_type": "PPR",
        "amount": 0.5974602214286241,
        "status": "CAU",
        "location_x": 12.0,
        "location_y": 98.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 18,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "12CAN18",
        "trash_type": "CAN",
        "amount": 0.8592431433158799,
        "status": "WAR",
        "location_x": 184.0,
        "location_y": 17.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 19,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "12GLA19",
        "trash_type": "PET",
        "amount": 0.5140265856573888,
        "status": "CAU",
        "location_x": 14.0,
        "location_y": 300.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 20,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "12PPR20",
        "trash_type": "PPR",
        "amount": 0.3585168607350333,
        "status": "SAF",
        "location_x": 173.0,
        "location_y": 114.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 21,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "13GER21",
        "trash_type": "GLA",
        "amount": 0.5410465372354647,
        "status": "CAU",
        "location_x": 562.0,
        "location_y": 226.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 22,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "13PET22",
        "trash_type": "PPR",
        "amount": 0.8445258596647196,
        "status": "WAR",
        "location_x": 357.0,
        "location_y": 295.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 23,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "13CAN23",
        "trash_type": "GER",
        "amount": 0.0009116750600142165,
        "status": "SAF",
        "location_x": 638.0,
        "location_y": 389.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 24,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "13GLA24",
        "trash_type": "CAN",
        "amount": 0.934750307230058,
        "status": "WAR",
        "location_x": 638.0,
        "location_y": 123.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 25,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "13PPR25",
        "trash_type": "PET",
        "amount": 0.2068146972295518,
        "status": "SAF",
        "location_x": 347.0,
        "location_y": 383.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 26,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "14GER26",
        "trash_type": "GLA",
        "amount": 0.16828156646250814,
        "status": "SAF",
        "location_x": 436.0,
        "location_y": 331.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 27,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "14PET27",
        "trash_type": "PPR",
        "amount": 0.6257160860482859,
        "status": "CAU",
        "location_x": 364.0,
        "location_y": 397.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 28,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "14CAN28",
        "trash_type": "GER",
        "amount": 0.0018290485111537302,
        "status": "SAF",
        "location_x": 452.0,
        "location_y": 16.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 29,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "14GLA29",
        "trash_type": "PET",
        "amount": 0.9889239478358383,
        "status": "WAR",
        "location_x": 318.0,
        "location_y": 62.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 30,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관"
            }
        },
        "token": "14PPR30",
        "trash_type": "GER",
        "amount": 0.10972165751899865,
        "status": "SAF",
        "location_x": 428.0,
        "location_y": 212.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 31,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B1GER31",
        "trash_type": "GER",
        "amount": 0.13195662940117037,
        "status": "SAF",
        "location_x": 424.0,
        "location_y": 245.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 32,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B1PET32",
        "trash_type": "PPR",
        "amount": 0.1279109701280483,
        "status": "SAF",
        "location_x": 539.0,
        "location_y": 121.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 33,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B1CAN33",
        "trash_type": "GER",
        "amount": 0.5760516857432226,
        "status": "CAU",
        "location_x": 402.0,
        "location_y": 21.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 34,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B1GLA34",
        "trash_type": "PET",
        "amount": 0.3305497273665703,
        "status": "SAF",
        "location_x": 357.0,
        "location_y": 206.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 35,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B1PPR35",
        "trash_type": "GER",
        "amount": 0.2520404210728132,
        "status": "SAF",
        "location_x": 486.0,
        "location_y": 423.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 36,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B2GER36",
        "trash_type": "PPR",
        "amount": 0.556216300473699,
        "status": "CAU",
        "location_x": 430.0,
        "location_y": 331.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 37,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B2PET37",
        "trash_type": "PET",
        "amount": 0.0792691315046713,
        "status": "SAF",
        "location_x": 604.0,
        "location_y": 30.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 38,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B2CAN38",
        "trash_type": "GLA",
        "amount": 0.057177913290081595,
        "status": "SAF",
        "location_x": 32.0,
        "location_y": 141.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 39,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B2GLA39",
        "trash_type": "PET",
        "amount": 0.1802218964098805,
        "status": "SAF",
        "location_x": 551.0,
        "location_y": 7.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 40,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "2B2PPR40",
        "trash_type": "PET",
        "amount": 0.25053945234861996,
        "status": "SAF",
        "location_x": 185.0,
        "location_y": 389.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 41,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "21GER41",
        "trash_type": "PET",
        "amount": 0.20406328715688093,
        "status": "SAF",
        "location_x": 38.0,
        "location_y": 382.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 42,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "21PET42",
        "trash_type": "PPR",
        "amount": 0.8745419627180936,
        "status": "WAR",
        "location_x": 479.0,
        "location_y": 380.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 43,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "21CAN43",
        "trash_type": "GER",
        "amount": 0.9313173984128624,
        "status": "WAR",
        "location_x": 144.0,
        "location_y": 167.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 44,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "21GLA44",
        "trash_type": "GLA",
        "amount": 0.9869592245893837,
        "status": "WAR",
        "location_x": 546.0,
        "location_y": 64.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 45,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "21PPR45",
        "trash_type": "PET",
        "amount": 0.6368207239442791,
        "status": "CAU",
        "location_x": 425.0,
        "location_y": 183.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 46,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "22GER46",
        "trash_type": "GER",
        "amount": 0.4697496037201705,
        "status": "CAU",
        "location_x": 412.0,
        "location_y": 240.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 47,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "22PET47",
        "trash_type": "PET",
        "amount": 0.5994924871681402,
        "status": "CAU",
        "location_x": 537.0,
        "location_y": 57.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 48,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "22CAN48",
        "trash_type": "CAN",
        "amount": 0.403501825315305,
        "status": "CAU",
        "location_x": 624.0,
        "location_y": 241.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 49,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "22GLA49",
        "trash_type": "PET",
        "amount": 0.11219559633960263,
        "status": "SAF",
        "location_x": 511.0,
        "location_y": 222.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 50,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "22PPR50",
        "trash_type": "PET",
        "amount": 0.5502393929107533,
        "status": "CAU",
        "location_x": 80.0,
        "location_y": 176.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 51,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "23GER51",
        "trash_type": "PPR",
        "amount": 0.6737168745457914,
        "status": "CAU",
        "location_x": 373.0,
        "location_y": 169.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 52,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "23PET52",
        "trash_type": "GER",
        "amount": 0.4629645855873281,
        "status": "CAU",
        "location_x": 327.0,
        "location_y": 332.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 53,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "23CAN53",
        "trash_type": "CAN",
        "amount": 0.42619192963076635,
        "status": "CAU",
        "location_x": 485.0,
        "location_y": 322.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 54,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "23GLA54",
        "trash_type": "GLA",
        "amount": 0.7935957370990534,
        "status": "WAR",
        "location_x": 242.0,
        "location_y": 21.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 55,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "23PPR55",
        "trash_type": "PET",
        "amount": 0.34342631542604174,
        "status": "SAF",
        "location_x": 539.0,
        "location_y": 86.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 56,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "24GER56",
        "trash_type": "PET",
        "amount": 0.4721479885484966,
        "status": "CAU",
        "location_x": 31.0,
        "location_y": 88.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 57,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "24PET57",
        "trash_type": "GER",
        "amount": 0.9013549553316011,
        "status": "WAR",
        "location_x": 336.0,
        "location_y": 220.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 58,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "24CAN58",
        "trash_type": "CAN",
        "amount": 0.4085506375162613,
        "status": "CAU",
        "location_x": 73.0,
        "location_y": 16.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 59,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "24GLA59",
        "trash_type": "PET",
        "amount": 0.07662150466206308,
        "status": "SAF",
        "location_x": 38.0,
        "location_y": 365.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 60,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관"
            }
        },
        "token": "24PPR60",
        "trash_type": "GLA",
        "amount": 0.6804692779899763,
        "status": "CAU",
        "location_x": 31.0,
        "location_y": 323.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 61,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B1GER61",
        "trash_type": "CAN",
        "amount": 0.4360810392531639,
        "status": "CAU",
        "location_x": 162.0,
        "location_y": 179.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 62,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B1PET62",
        "trash_type": "GER",
        "amount": 0.6210862889233772,
        "status": "CAU",
        "location_x": 563.0,
        "location_y": 396.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 63,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B1CAN63",
        "trash_type": "PPR",
        "amount": 0.07034801256402712,
        "status": "SAF",
        "location_x": 603.0,
        "location_y": 194.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 64,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B1GLA64",
        "trash_type": "PET",
        "amount": 0.768814984980113,
        "status": "WAR",
        "location_x": 394.0,
        "location_y": 368.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 65,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B1PPR65",
        "trash_type": "CAN",
        "amount": 0.3253268900534081,
        "status": "SAF",
        "location_x": 547.0,
        "location_y": 77.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 66,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B2GER66",
        "trash_type": "PPR",
        "amount": 0.2550667185666461,
        "status": "SAF",
        "location_x": 428.0,
        "location_y": 424.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 67,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B2PET67",
        "trash_type": "GER",
        "amount": 0.9515144362873268,
        "status": "WAR",
        "location_x": 503.0,
        "location_y": 242.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 68,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B2CAN68",
        "trash_type": "GER",
        "amount": 0.05249870874288842,
        "status": "SAF",
        "location_x": 47.0,
        "location_y": 141.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 69,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B2GLA69",
        "trash_type": "GLA",
        "amount": 0.026998409090424724,
        "status": "SAF",
        "location_x": 265.0,
        "location_y": 283.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 70,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "3B2PPR70",
        "trash_type": "PET",
        "amount": 0.8180154975788916,
        "status": "WAR",
        "location_x": 53.0,
        "location_y": 161.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 71,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "31GER71",
        "trash_type": "CAN",
        "amount": 0.83151535579346,
        "status": "WAR",
        "location_x": 220.0,
        "location_y": 51.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 72,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "31PET72",
        "trash_type": "CAN",
        "amount": 0.0938051257844903,
        "status": "SAF",
        "location_x": 266.0,
        "location_y": 375.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 73,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "31CAN73",
        "trash_type": "PPR",
        "amount": 0.9881372440413996,
        "status": "WAR",
        "location_x": 450.0,
        "location_y": 187.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 74,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "31GLA74",
        "trash_type": "GER",
        "amount": 0.5471927875081366,
        "status": "CAU",
        "location_x": 176.0,
        "location_y": 322.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 75,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "31PPR75",
        "trash_type": "CAN",
        "amount": 0.2823233097692618,
        "status": "SAF",
        "location_x": 257.0,
        "location_y": 288.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 76,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "32GER76",
        "trash_type": "GLA",
        "amount": 0.0033805621389132456,
        "status": "SAF",
        "location_x": 8.0,
        "location_y": 41.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 77,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "32PET77",
        "trash_type": "CAN",
        "amount": 0.6991733480247034,
        "status": "CAU",
        "location_x": 381.0,
        "location_y": 132.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 78,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "32CAN78",
        "trash_type": "CAN",
        "amount": 0.83011788593779,
        "status": "WAR",
        "location_x": 329.0,
        "location_y": 253.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 79,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "32GLA79",
        "trash_type": "CAN",
        "amount": 0.5779890437888482,
        "status": "CAU",
        "location_x": 208.0,
        "location_y": 223.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 80,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "32PPR80",
        "trash_type": "GER",
        "amount": 0.3443123746401422,
        "status": "SAF",
        "location_x": 309.0,
        "location_y": 232.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 81,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "33GER81",
        "trash_type": "CAN",
        "amount": 0.33729398062874905,
        "status": "SAF",
        "location_x": 572.0,
        "location_y": 78.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 82,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "33PET82",
        "trash_type": "PPR",
        "amount": 0.6871760926698018,
        "status": "CAU",
        "location_x": 364.0,
        "location_y": 405.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 83,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "33CAN83",
        "trash_type": "GLA",
        "amount": 0.31517670644095586,
        "status": "SAF",
        "location_x": 240.0,
        "location_y": 210.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 84,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "33GLA84",
        "trash_type": "PPR",
        "amount": 0.4090121750892459,
        "status": "CAU",
        "location_x": 9.0,
        "location_y": 391.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 85,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "33PPR85",
        "trash_type": "GLA",
        "amount": 0.4749394534593704,
        "status": "CAU",
        "location_x": 575.0,
        "location_y": 99.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 86,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "34GER86",
        "trash_type": "CAN",
        "amount": 0.675857361415715,
        "status": "CAU",
        "location_x": 132.0,
        "location_y": 421.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 87,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "34PET87",
        "trash_type": "GLA",
        "amount": 0.034945764227199305,
        "status": "SAF",
        "location_x": 163.0,
        "location_y": 3.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 88,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "34CAN88",
        "trash_type": "PPR",
        "amount": 0.5920418206474387,
        "status": "CAU",
        "location_x": 227.0,
        "location_y": 146.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 89,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "34GLA89",
        "trash_type": "GLA",
        "amount": 0.5111515495448148,
        "status": "CAU",
        "location_x": 403.0,
        "location_y": 353.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 90,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관"
            }
        },
        "token": "34PPR90",
        "trash_type": "GLA",
        "amount": 0.0598001623847374,
        "status": "SAF",
        "location_x": 421.0,
        "location_y": 147.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 91,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B1GER91",
        "trash_type": "GER",
        "amount": 0.6569500396036903,
        "status": "CAU",
        "location_x": 343.0,
        "location_y": 445.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 92,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B1PET92",
        "trash_type": "GER",
        "amount": 0.8924384126571778,
        "status": "WAR",
        "location_x": 167.0,
        "location_y": 296.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 93,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B1CAN93",
        "trash_type": "CAN",
        "amount": 0.8142424494585025,
        "status": "WAR",
        "location_x": 91.0,
        "location_y": 135.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 94,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B1GLA94",
        "trash_type": "PET",
        "amount": 0.3276027964724616,
        "status": "SAF",
        "location_x": 603.0,
        "location_y": 91.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 95,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B1PPR95",
        "trash_type": "PET",
        "amount": 0.43343608591041394,
        "status": "CAU",
        "location_x": 409.0,
        "location_y": 10.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 96,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B2GER96",
        "trash_type": "GLA",
        "amount": 0.4439070265221574,
        "status": "CAU",
        "location_x": 420.0,
        "location_y": 36.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 97,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B2PET97",
        "trash_type": "PET",
        "amount": 0.05840559603739903,
        "status": "SAF",
        "location_x": 116.0,
        "location_y": 12.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 98,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B2CAN98",
        "trash_type": "PPR",
        "amount": 0.4325465316641254,
        "status": "CAU",
        "location_x": 455.0,
        "location_y": 141.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 99,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B2GLA99",
        "trash_type": "GLA",
        "amount": 0.18110519414212112,
        "status": "SAF",
        "location_x": 134.0,
        "location_y": 15.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 100,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "4B2PPR100",
        "trash_type": "PPR",
        "amount": 0.6229370952467161,
        "status": "CAU",
        "location_x": 304.0,
        "location_y": 262.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 101,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "41GER101",
        "trash_type": "CAN",
        "amount": 0.054706255585146746,
        "status": "SAF",
        "location_x": 579.0,
        "location_y": 272.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 102,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "41PET102",
        "trash_type": "PET",
        "amount": 0.8589415372581772,
        "status": "WAR",
        "location_x": 448.0,
        "location_y": 50.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 103,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "41CAN103",
        "trash_type": "PET",
        "amount": 0.7100264222911008,
        "status": "WAR",
        "location_x": 482.0,
        "location_y": 199.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 104,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "41GLA104",
        "trash_type": "PET",
        "amount": 0.673188730583374,
        "status": "CAU",
        "location_x": 308.0,
        "location_y": 392.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 105,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "41PPR105",
        "trash_type": "GER",
        "amount": 0.4361130042261565,
        "status": "CAU",
        "location_x": 366.0,
        "location_y": 84.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 106,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "42GER106",
        "trash_type": "CAN",
        "amount": 0.7827129768297103,
        "status": "WAR",
        "location_x": 194.0,
        "location_y": 396.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 107,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "42PET107",
        "trash_type": "PET",
        "amount": 0.28046734538908413,
        "status": "SAF",
        "location_x": 295.0,
        "location_y": 334.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 108,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "42CAN108",
        "trash_type": "GLA",
        "amount": 0.9215973617921978,
        "status": "WAR",
        "location_x": 439.0,
        "location_y": 165.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 109,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "42GLA109",
        "trash_type": "PPR",
        "amount": 0.8956838620420163,
        "status": "WAR",
        "location_x": 102.0,
        "location_y": 241.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 110,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "42PPR110",
        "trash_type": "GLA",
        "amount": 0.4873933144301029,
        "status": "CAU",
        "location_x": 233.0,
        "location_y": 264.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 111,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "43GER111",
        "trash_type": "GER",
        "amount": 0.14183292753215637,
        "status": "SAF",
        "location_x": 52.0,
        "location_y": 25.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 112,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "43PET112",
        "trash_type": "GER",
        "amount": 0.9895258852356547,
        "status": "WAR",
        "location_x": 393.0,
        "location_y": 374.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 113,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "43CAN113",
        "trash_type": "GLA",
        "amount": 0.1557066929318186,
        "status": "SAF",
        "location_x": 280.0,
        "location_y": 232.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 114,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "43GLA114",
        "trash_type": "PET",
        "amount": 0.2576096629843191,
        "status": "SAF",
        "location_x": 456.0,
        "location_y": 324.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 115,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "43PPR115",
        "trash_type": "PPR",
        "amount": 0.48104129052825884,
        "status": "CAU",
        "location_x": 96.0,
        "location_y": 243.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 116,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "44GER116",
        "trash_type": "PET",
        "amount": 0.20864886570089314,
        "status": "SAF",
        "location_x": 394.0,
        "location_y": 321.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 117,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "44PET117",
        "trash_type": "PET",
        "amount": 0.833449360524977,
        "status": "WAR",
        "location_x": 302.0,
        "location_y": 101.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 118,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "44CAN118",
        "trash_type": "GLA",
        "amount": 0.41552637608090526,
        "status": "CAU",
        "location_x": 89.0,
        "location_y": 232.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 119,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "44GLA119",
        "trash_type": "GLA",
        "amount": 0.22493088096749725,
        "status": "SAF",
        "location_x": 556.0,
        "location_y": 82.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 120,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관"
            }
        },
        "token": "44PPR120",
        "trash_type": "CAN",
        "amount": 0.04320273001853181,
        "status": "SAF",
        "location_x": 573.0,
        "location_y": 142.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 121,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B1GER121",
        "trash_type": "PET",
        "amount": 0.9015649029612246,
        "status": "WAR",
        "location_x": 441.0,
        "location_y": 150.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 122,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B1PET122",
        "trash_type": "PET",
        "amount": 0.21862751667463154,
        "status": "SAF",
        "location_x": 319.0,
        "location_y": 10.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 123,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B1CAN123",
        "trash_type": "GLA",
        "amount": 0.7890319035360369,
        "status": "WAR",
        "location_x": 135.0,
        "location_y": 389.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 124,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B1GLA124",
        "trash_type": "PPR",
        "amount": 0.6567435069500184,
        "status": "CAU",
        "location_x": 276.0,
        "location_y": 414.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 125,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B1PPR125",
        "trash_type": "PPR",
        "amount": 0.7984999353054694,
        "status": "WAR",
        "location_x": 361.0,
        "location_y": 304.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 126,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B2GER126",
        "trash_type": "CAN",
        "amount": 0.3614002113799082,
        "status": "SAF",
        "location_x": 51.0,
        "location_y": 169.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 127,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B2PET127",
        "trash_type": "GLA",
        "amount": 0.7802173842813984,
        "status": "WAR",
        "location_x": 322.0,
        "location_y": 167.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 128,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B2CAN128",
        "trash_type": "GLA",
        "amount": 0.5634303757996159,
        "status": "CAU",
        "location_x": 22.0,
        "location_y": 229.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 129,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B2GLA129",
        "trash_type": "PPR",
        "amount": 0.6619445039067052,
        "status": "CAU",
        "location_x": 620.0,
        "location_y": 387.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 130,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "5B2PPR130",
        "trash_type": "GLA",
        "amount": 0.8157828644505123,
        "status": "WAR",
        "location_x": 516.0,
        "location_y": 175.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 131,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "51GER131",
        "trash_type": "PPR",
        "amount": 0.6717660101206088,
        "status": "CAU",
        "location_x": 152.0,
        "location_y": 4.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 132,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "51PET132",
        "trash_type": "GER",
        "amount": 0.045092172252151785,
        "status": "SAF",
        "location_x": 434.0,
        "location_y": 358.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 133,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "51CAN133",
        "trash_type": "PET",
        "amount": 0.35620371416306273,
        "status": "SAF",
        "location_x": 104.0,
        "location_y": 119.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 134,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "51GLA134",
        "trash_type": "PET",
        "amount": 0.4625823493396487,
        "status": "CAU",
        "location_x": 389.0,
        "location_y": 446.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 135,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "51PPR135",
        "trash_type": "PPR",
        "amount": 0.767774618749601,
        "status": "WAR",
        "location_x": 177.0,
        "location_y": 141.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 136,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "52GER136",
        "trash_type": "PPR",
        "amount": 0.40097224269427134,
        "status": "CAU",
        "location_x": 28.0,
        "location_y": 137.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 137,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "52PET137",
        "trash_type": "CAN",
        "amount": 0.5559831420423164,
        "status": "CAU",
        "location_x": 155.0,
        "location_y": 432.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 138,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "52CAN138",
        "trash_type": "GLA",
        "amount": 0.6992037865070919,
        "status": "CAU",
        "location_x": 631.0,
        "location_y": 31.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 139,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "52GLA139",
        "trash_type": "GER",
        "amount": 0.009373170631864602,
        "status": "SAF",
        "location_x": 231.0,
        "location_y": 176.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 140,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "52PPR140",
        "trash_type": "GER",
        "amount": 0.31382665472297455,
        "status": "SAF",
        "location_x": 368.0,
        "location_y": 334.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 141,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "53GER141",
        "trash_type": "PET",
        "amount": 0.7370473611181837,
        "status": "WAR",
        "location_x": 633.0,
        "location_y": 55.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 142,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "53PET142",
        "trash_type": "CAN",
        "amount": 0.3358108470450777,
        "status": "SAF",
        "location_x": 602.0,
        "location_y": 361.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 143,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "53CAN143",
        "trash_type": "PPR",
        "amount": 0.9968260742437254,
        "status": "WAR",
        "location_x": 34.0,
        "location_y": 319.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 144,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "53GLA144",
        "trash_type": "GLA",
        "amount": 0.48516552809760516,
        "status": "CAU",
        "location_x": 86.0,
        "location_y": 132.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 145,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "53PPR145",
        "trash_type": "CAN",
        "amount": 0.8241391244633549,
        "status": "WAR",
        "location_x": 435.0,
        "location_y": 111.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 146,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "54GER146",
        "trash_type": "PPR",
        "amount": 0.7206783266504259,
        "status": "WAR",
        "location_x": 596.0,
        "location_y": 148.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 147,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "54PET147",
        "trash_type": "GER",
        "amount": 0.07308479677992186,
        "status": "SAF",
        "location_x": 593.0,
        "location_y": 356.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 148,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "54CAN148",
        "trash_type": "CAN",
        "amount": 0.16968439472035612,
        "status": "SAF",
        "location_x": 581.0,
        "location_y": 99.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 149,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "54GLA149",
        "trash_type": "PET",
        "amount": 0.48467602208870453,
        "status": "CAU",
        "location_x": 97.0,
        "location_y": 358.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    },
    {
        "id": 150,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "54PPR150",
        "trash_type": "PET",
        "amount": 0.037365975476513325,
        "status": "SAF",
        "location_x": 321.0,
        "location_y": 194.0,
        "created_at": "2022-08-08T17:01:11.657856+09:00",
        "updated_at": "2022-08-08T17:01:11.657856+09:00",
        "discard_users": []
    }
]

for i in range(5, 9):
    if i == 6:
        nn = 31
    else:
        nn = 32
    for j in range(1, nn):        
        dd = '0' + str(j) if len(str(j)) == 1 else str(j)
        day = '20220' + str(i) + dd


        cnt = 0
        data = ''
        while cnt < 3000:
            idx = random.randrange(150)
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
            sen = f'{day} {time} {target["floor"]["building"]["name"]} {target["floor"]["building"]["pk"]} {target["floor"]["name"]} {target["floor"]["pk"]} {target["token"]} {target["trash_type"]} {rand_zero+rand_rfid} {target["amount"]}'
            data += sen
            data += '\n'
            target["amount"] = random.random()
            cnt += 1

        f = open(f'20220{str(i)+dd}', 'w', encoding='UTF-8')
        f.write(data)
        f.close()