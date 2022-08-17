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
        "token": "10000000tokenij5",
        "trash_type": "CAN",
        "amount": 0.5470137758226679,
        "status": "CAU",
        "location_x": 318.0,
        "location_y": 109.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij4",
        "trash_type": "GER",
        "amount": 0.8374743523713207,
        "status": "WAR",
        "location_x": 338.0,
        "location_y": 109.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.6342219880872065,
        "status": "CAU",
        "location_x": 378.0,
        "location_y": 109.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.5323841828369269,
        "status": "CAU",
        "location_x": 500.0,
        "location_y": 322.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij1",
        "trash_type": "CAN",
        "amount": 0.3441600874669526,
        "status": "SAF",
        "location_x": 500.0,
        "location_y": 342.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "PPR",
        "amount": 0.3685185380615793,
        "status": "SAF",
        "location_x": 500.0,
        "location_y": 382.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij4",
        "trash_type": "PPR",
        "amount": 0.03718564646566924,
        "status": "SAF",
        "location_x": 910.0,
        "location_y": 332.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij7",
        "trash_type": "PPR",
        "amount": 0.8455298469367303,
        "status": "WAR",
        "location_x": 930.0,
        "location_y": 332.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.9584753458270303,
        "status": "WAR",
        "location_x": 970.0,
        "location_y": 332.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.5616948718823707,
        "status": "CAU",
        "location_x": 163.0,
        "location_y": 407.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.890804814581635,
        "status": "WAR",
        "location_x": 163.0,
        "location_y": 427.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.4002383431394465,
        "status": "CAU",
        "location_x": 163.0,
        "location_y": 467.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.7958789118067862,
        "status": "WAR",
        "location_x": 382.0,
        "location_y": 405.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.23224437710163748,
        "status": "SAF",
        "location_x": 382.0,
        "location_y": 425.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.9322918880814413,
        "status": "WAR",
        "location_x": 382.0,
        "location_y": 465.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.6234176639679968,
        "status": "CAU",
        "location_x": 388.0,
        "location_y": 331.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.7525602351740525,
        "status": "WAR",
        "location_x": 408.0,
        "location_y": 331.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.9883031296777999,
        "status": "WAR",
        "location_x": 448.0,
        "location_y": 331.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij5",
        "trash_type": "GLA",
        "amount": 0.15024281364267444,
        "status": "SAF",
        "location_x": 938.0,
        "location_y": 276.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij6",
        "trash_type": "PPR",
        "amount": 0.8208520403391419,
        "status": "WAR",
        "location_x": 938.0,
        "location_y": 296.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij2",
        "trash_type": "GER",
        "amount": 0.25005347832801683,
        "status": "SAF",
        "location_x": 938.0,
        "location_y": 336.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij6",
        "trash_type": "GER",
        "amount": 0.5175632297241678,
        "status": "CAU",
        "location_x": 640.0,
        "location_y": 397.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.792011687926477,
        "status": "WAR",
        "location_x": 640.0,
        "location_y": 417.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij8",
        "trash_type": "CAN",
        "amount": 0.5796089725918953,
        "status": "CAU",
        "location_x": 640.0,
        "location_y": 457.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij1",
        "trash_type": "GER",
        "amount": 0.5612867559050821,
        "status": "CAU",
        "location_x": 1145.0,
        "location_y": 445.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij6",
        "trash_type": "GLA",
        "amount": 0.18349985488996856,
        "status": "SAF",
        "location_x": 1145.0,
        "location_y": 465.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij9",
        "trash_type": "PET",
        "amount": 0.4495891449306214,
        "status": "CAU",
        "location_x": 1145.0,
        "location_y": 505.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij4",
        "trash_type": "PPR",
        "amount": 0.5707202610361813,
        "status": "CAU",
        "location_x": 270.0,
        "location_y": 490.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij8",
        "trash_type": "PPR",
        "amount": 0.7697830310937326,
        "status": "WAR",
        "location_x": 270.0,
        "location_y": 510.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij4",
        "trash_type": "GER",
        "amount": 0.468289254254031,
        "status": "CAU",
        "location_x": 270.0,
        "location_y": 550.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.31789665813675283,
        "status": "SAF",
        "location_x": 565.0,
        "location_y": 448.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij9",
        "trash_type": "GER",
        "amount": 0.494398910423671,
        "status": "CAU",
        "location_x": 565.0,
        "location_y": 468.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij2",
        "trash_type": "CAN",
        "amount": 0.5652592703014588,
        "status": "CAU",
        "location_x": 565.0,
        "location_y": 508.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.11530576631125633,
        "status": "SAF",
        "location_x": 516.0,
        "location_y": 366.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij8",
        "trash_type": "GLA",
        "amount": 0.2918145456889859,
        "status": "SAF",
        "location_x": 516.0,
        "location_y": 386.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "token": "10000000tokenij2",
        "trash_type": "PET",
        "amount": 0.18057662104764516,
        "status": "SAF",
        "location_x": 516.0,
        "location_y": 426.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.9855359703382663,
        "status": "WAR",
        "location_x": 371.0,
        "location_y": 364.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.5233842963299696,
        "status": "CAU",
        "location_x": 371.0,
        "location_y": 384.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.048097971150881325,
        "status": "SAF",
        "location_x": 371.0,
        "location_y": 424.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.8921692250731208,
        "status": "WAR",
        "location_x": 371.0,
        "location_y": 424.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.5404732787881352,
        "status": "CAU",
        "location_x": 371.0,
        "location_y": 444.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.278607784561397,
        "status": "SAF",
        "location_x": 371.0,
        "location_y": 484.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.18451039996908936,
        "status": "SAF",
        "location_x": 371.0,
        "location_y": 484.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.5213250473279951,
        "status": "CAU",
        "location_x": 371.0,
        "location_y": 504.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.3708162281088805,
        "status": "SAF",
        "location_x": 371.0,
        "location_y": 544.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.5778214939421341,
        "status": "CAU",
        "location_x": 96.0,
        "location_y": 250.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.4547367398864205,
        "status": "CAU",
        "location_x": 96.0,
        "location_y": 270.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.863814309907406,
        "status": "WAR",
        "location_x": 96.0,
        "location_y": 310.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.436199931488063,
        "status": "CAU",
        "location_x": 96.0,
        "location_y": 310.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.1681508426683116,
        "status": "SAF",
        "location_x": 96.0,
        "location_y": 330.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.9438799771779429,
        "status": "WAR",
        "location_x": 96.0,
        "location_y": 370.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.5570604102621249,
        "status": "CAU",
        "location_x": 96.0,
        "location_y": 370.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.7528346759157438,
        "status": "WAR",
        "location_x": 96.0,
        "location_y": 390.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.2206716265248707,
        "status": "SAF",
        "location_x": 96.0,
        "location_y": 430.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.5741046036602776,
        "status": "CAU",
        "location_x": 586.0,
        "location_y": 366.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.47582529838471843,
        "status": "CAU",
        "location_x": 606.0,
        "location_y": 366.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.8556243116050752,
        "status": "WAR",
        "location_x": 646.0,
        "location_y": 366.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.17367530488876426,
        "status": "SAF",
        "location_x": 646.0,
        "location_y": 366.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.756691305830598,
        "status": "WAR",
        "location_x": 666.0,
        "location_y": 366.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.9258111885362934,
        "status": "WAR",
        "location_x": 706.0,
        "location_y": 366.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.669288823133566,
        "status": "CAU",
        "location_x": 706.0,
        "location_y": 366.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.3828123801090879,
        "status": "SAF",
        "location_x": 726.0,
        "location_y": 366.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.12417126617766694,
        "status": "SAF",
        "location_x": 766.0,
        "location_y": 366.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.937191552105348,
        "status": "WAR",
        "location_x": 62.0,
        "location_y": 67.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.02052146169292124,
        "status": "SAF",
        "location_x": 82.0,
        "location_y": 67.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.8060414170623437,
        "status": "WAR",
        "location_x": 122.0,
        "location_y": 67.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.07714262668177663,
        "status": "SAF",
        "location_x": 122.0,
        "location_y": 67.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.22815121997013466,
        "status": "SAF",
        "location_x": 142.0,
        "location_y": 67.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.7143683804711318,
        "status": "WAR",
        "location_x": 182.0,
        "location_y": 67.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.6765544811175949,
        "status": "CAU",
        "location_x": 182.0,
        "location_y": 67.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.3033792485027387,
        "status": "SAF",
        "location_x": 202.0,
        "location_y": 67.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.12613579712220513,
        "status": "SAF",
        "location_x": 242.0,
        "location_y": 67.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.9405462795736033,
        "status": "WAR",
        "location_x": 543.0,
        "location_y": 54.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.372433127810448,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 74.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.43575744091606017,
        "status": "CAU",
        "location_x": 543.0,
        "location_y": 114.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.14586230353088536,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 114.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.2929750966502497,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 134.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.8766589449330863,
        "status": "WAR",
        "location_x": 543.0,
        "location_y": 174.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.656728333580114,
        "status": "CAU",
        "location_x": 543.0,
        "location_y": 174.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.037873618809380005,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 194.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.27282598327390817,
        "status": "SAF",
        "location_x": 543.0,
        "location_y": 234.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.196062300807758,
        "status": "SAF",
        "location_x": 184.0,
        "location_y": 277.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.17928067233188472,
        "status": "SAF",
        "location_x": 204.0,
        "location_y": 277.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "amount": 0.7489440669129281,
        "status": "WAR",
        "location_x": 244.0,
        "location_y": 277.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.7022045259817626,
        "status": "WAR",
        "location_x": 244.0,
        "location_y": 277.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.17571619461692456,
        "status": "SAF",
        "location_x": 264.0,
        "location_y": 277.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.029847231420663034,
        "status": "SAF",
        "location_x": 304.0,
        "location_y": 277.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GLA",
        "amount": 0.630984892629267,
        "status": "CAU",
        "location_x": 304.0,
        "location_y": 277.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.5852473715868313,
        "status": "CAU",
        "location_x": 324.0,
        "location_y": 277.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.13745448015315254,
        "status": "SAF",
        "location_x": 364.0,
        "location_y": 277.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.050737755662522255,
        "status": "SAF",
        "location_x": 388.0,
        "location_y": 142.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.40254234516079335,
        "status": "CAU",
        "location_x": 388.0,
        "location_y": 162.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.3802606971110295,
        "status": "SAF",
        "location_x": 388.0,
        "location_y": 202.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PET",
        "amount": 0.32784034737547085,
        "status": "SAF",
        "location_x": 388.0,
        "location_y": 202.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.8629511264910974,
        "status": "WAR",
        "location_x": 388.0,
        "location_y": 222.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.922487053696765,
        "status": "WAR",
        "location_x": 388.0,
        "location_y": 262.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "GER",
        "amount": 0.8177128803670017,
        "status": "WAR",
        "location_x": 388.0,
        "location_y": 262.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "PPR",
        "amount": 0.7036353049351076,
        "status": "WAR",
        "location_x": 388.0,
        "location_y": 282.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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
        "trash_type": "CAN",
        "amount": 0.8901512162142806,
        "status": "WAR",
        "location_x": 388.0,
        "location_y": 322.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 100,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1100",
        "trash_type": "PPR",
        "amount": 0.9160486340953148,
        "status": "WAR",
        "location_x": 124.0,
        "location_y": 275.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 101,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1101",
        "trash_type": "PET",
        "amount": 0.9573878910808088,
        "status": "WAR",
        "location_x": 144.0,
        "location_y": 275.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 102,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1102",
        "trash_type": "GER",
        "amount": 0.9581049637351221,
        "status": "WAR",
        "location_x": 184.0,
        "location_y": 275.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 103,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1103",
        "trash_type": "GER",
        "amount": 0.7571351490696036,
        "status": "WAR",
        "location_x": 184.0,
        "location_y": 275.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 104,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1104",
        "trash_type": "CAN",
        "amount": 0.972614121167804,
        "status": "WAR",
        "location_x": 204.0,
        "location_y": 275.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 105,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1105",
        "trash_type": "GLA",
        "amount": 0.826938053989474,
        "status": "WAR",
        "location_x": 244.0,
        "location_y": 275.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 106,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1106",
        "trash_type": "GER",
        "amount": 0.05814922653064969,
        "status": "SAF",
        "location_x": 244.0,
        "location_y": 275.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 107,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1107",
        "trash_type": "PET",
        "amount": 0.03780963290890316,
        "status": "SAF",
        "location_x": 264.0,
        "location_y": 275.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 108,
        "floor": {
            "pk": 12,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "4B1108",
        "trash_type": "GER",
        "amount": 0.5722736541342597,
        "status": "CAU",
        "location_x": 304.0,
        "location_y": 275.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 109,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41109",
        "trash_type": "CAN",
        "amount": 0.895741718397482,
        "status": "WAR",
        "location_x": 404.0,
        "location_y": 369.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 110,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41110",
        "trash_type": "GLA",
        "amount": 0.8732036734792662,
        "status": "WAR",
        "location_x": 424.0,
        "location_y": 369.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 111,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41111",
        "trash_type": "CAN",
        "amount": 0.3685641171313243,
        "status": "SAF",
        "location_x": 464.0,
        "location_y": 369.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 112,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41112",
        "trash_type": "PPR",
        "amount": 0.004634790312881942,
        "status": "SAF",
        "location_x": 464.0,
        "location_y": 369.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 113,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41113",
        "trash_type": "GER",
        "amount": 0.970442341339609,
        "status": "WAR",
        "location_x": 484.0,
        "location_y": 369.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 114,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41114",
        "trash_type": "GER",
        "amount": 0.10068084507342401,
        "status": "SAF",
        "location_x": 524.0,
        "location_y": 369.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 115,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41115",
        "trash_type": "PPR",
        "amount": 0.339250188351657,
        "status": "SAF",
        "location_x": 524.0,
        "location_y": 369.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 116,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41116",
        "trash_type": "GER",
        "amount": 0.6082681363646174,
        "status": "CAU",
        "location_x": 544.0,
        "location_y": 369.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 117,
        "floor": {
            "pk": 13,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "41117",
        "trash_type": "GER",
        "amount": 0.7138833747857437,
        "status": "WAR",
        "location_x": 584.0,
        "location_y": 369.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 118,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42118",
        "trash_type": "GER",
        "amount": 0.7211548572825865,
        "status": "WAR",
        "location_x": 512.0,
        "location_y": 187.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 119,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42119",
        "trash_type": "GER",
        "amount": 0.4944726864891732,
        "status": "CAU",
        "location_x": 532.0,
        "location_y": 187.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 120,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42120",
        "trash_type": "PET",
        "amount": 0.24516129910721418,
        "status": "SAF",
        "location_x": 572.0,
        "location_y": 187.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 121,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42121",
        "trash_type": "PPR",
        "amount": 0.47877271763745466,
        "status": "CAU",
        "location_x": 572.0,
        "location_y": 187.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 122,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42122",
        "trash_type": "GLA",
        "amount": 0.5204121582670225,
        "status": "CAU",
        "location_x": 592.0,
        "location_y": 187.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 123,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42123",
        "trash_type": "GLA",
        "amount": 0.6814751418157361,
        "status": "CAU",
        "location_x": 632.0,
        "location_y": 187.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 124,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42124",
        "trash_type": "GER",
        "amount": 0.5304128079926559,
        "status": "CAU",
        "location_x": 632.0,
        "location_y": 187.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 125,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42125",
        "trash_type": "CAN",
        "amount": 0.5212550464917908,
        "status": "CAU",
        "location_x": 652.0,
        "location_y": 187.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 126,
        "floor": {
            "pk": 14,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "42126",
        "trash_type": "GER",
        "amount": 0.45062470756848627,
        "status": "CAU",
        "location_x": 692.0,
        "location_y": 187.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 127,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43127",
        "trash_type": "PET",
        "amount": 0.3634726516574541,
        "status": "SAF",
        "location_x": 192.0,
        "location_y": 353.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 128,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43128",
        "trash_type": "PET",
        "amount": 0.5584836609002732,
        "status": "CAU",
        "location_x": 212.0,
        "location_y": 353.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 129,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43129",
        "trash_type": "PET",
        "amount": 0.023198646610298912,
        "status": "SAF",
        "location_x": 252.0,
        "location_y": 353.0,
        "group": "0",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 130,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43130",
        "trash_type": "GLA",
        "amount": 0.853173266239378,
        "status": "WAR",
        "location_x": 252.0,
        "location_y": 353.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 131,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43131",
        "trash_type": "PET",
        "amount": 0.5334754710735659,
        "status": "CAU",
        "location_x": 272.0,
        "location_y": 353.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 132,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43132",
        "trash_type": "PPR",
        "amount": 0.7472883934943365,
        "status": "WAR",
        "location_x": 312.0,
        "location_y": 353.0,
        "group": "1",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 133,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43133",
        "trash_type": "PET",
        "amount": 0.26684555024763934,
        "status": "SAF",
        "location_x": 312.0,
        "location_y": 353.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 134,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43134",
        "trash_type": "GLA",
        "amount": 0.7793821210999266,
        "status": "WAR",
        "location_x": 332.0,
        "location_y": 353.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
        "discard_users": []
    },
    {
        "id": 135,
        "floor": {
            "pk": 15,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관"
            }
        },
        "token": "43135",
        "trash_type": "PET",
        "amount": 0.10425860566451517,
        "status": "SAF",
        "location_x": 372.0,
        "location_y": 353.0,
        "group": "2",
        "is_connected": True,
        "created_at": "2022-08-17T12:11:00.217842+09:00",
        "updated_at": "2022-08-17T12:11:00.217842+09:00",
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