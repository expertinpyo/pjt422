import random

trash_list = [
    {
        "id": 1,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B1GER1",
        "trash_type": "PET",
        "amount": 0.41360751731801737,
        "status": "CAU",
        "location_x": 509.0,
        "location_y": 270.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 2,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B1PET2",
        "trash_type": "PET",
        "amount": 0.48691280864445896,
        "status": "CAU",
        "location_x": 488.0,
        "location_y": 411.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 3,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B1CAN3",
        "trash_type": "CAN",
        "amount": 0.10735818604916225,
        "status": "SAF",
        "location_x": 339.0,
        "location_y": 179.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 4,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B1GLA4",
        "trash_type": "GER",
        "amount": 0.6145187170375099,
        "status": "CAU",
        "location_x": 48.0,
        "location_y": 441.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 5,
        "floor": {
            "pk": 1,
            "name": "B1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B1PPR5",
        "trash_type": "PET",
        "amount": 0.12969708676103497,
        "status": "SAF",
        "location_x": 86.0,
        "location_y": 373.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 6,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B2GER6",
        "trash_type": "CAN",
        "amount": 0.10920560910893462,
        "status": "SAF",
        "location_x": 613.0,
        "location_y": 357.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 7,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B2PET7",
        "trash_type": "GLA",
        "amount": 0.936303671504814,
        "status": "WAR",
        "location_x": 380.0,
        "location_y": 410.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 8,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B2CAN8",
        "trash_type": "PET",
        "amount": 0.8760722984545675,
        "status": "WAR",
        "location_x": 383.0,
        "location_y": 438.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 9,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B2GLA9",
        "trash_type": "PPR",
        "amount": 0.17068592501217594,
        "status": "SAF",
        "location_x": 590.0,
        "location_y": 296.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 10,
        "floor": {
            "pk": 2,
            "name": "B2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "11B2PPR10",
        "trash_type": "PPR",
        "amount": 0.8557904931547791,
        "status": "WAR",
        "location_x": 133.0,
        "location_y": 416.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 11,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "111GER11",
        "trash_type": "GER",
        "amount": 0.6692902204813053,
        "status": "CAU",
        "location_x": 617.0,
        "location_y": 66.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 12,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "111PET12",
        "trash_type": "PPR",
        "amount": 0.4744749742779073,
        "status": "CAU",
        "location_x": 486.0,
        "location_y": 175.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 13,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "111CAN13",
        "trash_type": "CAN",
        "amount": 0.976308083617422,
        "status": "WAR",
        "location_x": 579.0,
        "location_y": 332.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 14,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "111GLA14",
        "trash_type": "PPR",
        "amount": 0.7261427486854694,
        "status": "WAR",
        "location_x": 180.0,
        "location_y": 118.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 15,
        "floor": {
            "pk": 3,
            "name": "1",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "111PPR15",
        "trash_type": "PET",
        "amount": 0.4876039839354137,
        "status": "CAU",
        "location_x": 530.0,
        "location_y": 282.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 16,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "112GER16",
        "trash_type": "PPR",
        "amount": 0.306461100727476,
        "status": "SAF",
        "location_x": 357.0,
        "location_y": 110.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 17,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "112PET17",
        "trash_type": "PPR",
        "amount": 0.6425813392369045,
        "status": "CAU",
        "location_x": 5.0,
        "location_y": 321.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 18,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "112CAN18",
        "trash_type": "PET",
        "amount": 0.9195948468596115,
        "status": "WAR",
        "location_x": 86.0,
        "location_y": 196.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 19,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "112GLA19",
        "trash_type": "CAN",
        "amount": 0.8768400759656314,
        "status": "WAR",
        "location_x": 144.0,
        "location_y": 167.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 20,
        "floor": {
            "pk": 4,
            "name": "2",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "112PPR20",
        "trash_type": "GLA",
        "amount": 0.04075698937643368,
        "status": "SAF",
        "location_x": 164.0,
        "location_y": 311.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 21,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "113GER21",
        "trash_type": "PET",
        "amount": 0.05541986360802231,
        "status": "SAF",
        "location_x": 379.0,
        "location_y": 427.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 22,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "113PET22",
        "trash_type": "GER",
        "amount": 0.2917190439572057,
        "status": "SAF",
        "location_x": 228.0,
        "location_y": 47.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 23,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "113CAN23",
        "trash_type": "GER",
        "amount": 0.9668395504015701,
        "status": "WAR",
        "location_x": 625.0,
        "location_y": 307.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 24,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "113GLA24",
        "trash_type": "GLA",
        "amount": 0.12805981218620077,
        "status": "SAF",
        "location_x": 530.0,
        "location_y": 18.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 25,
        "floor": {
            "pk": 5,
            "name": "3",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "113PPR25",
        "trash_type": "GER",
        "amount": 0.1612546011841115,
        "status": "SAF",
        "location_x": 8.0,
        "location_y": 155.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 26,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "114GER26",
        "trash_type": "GER",
        "amount": 0.26058672585926823,
        "status": "SAF",
        "location_x": 249.0,
        "location_y": 348.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 27,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "114PET27",
        "trash_type": "PET",
        "amount": 0.14577657645822006,
        "status": "SAF",
        "location_x": 450.0,
        "location_y": 303.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 28,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "114CAN28",
        "trash_type": "PPR",
        "amount": 0.7604862060588654,
        "status": "WAR",
        "location_x": 410.0,
        "location_y": 201.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 29,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "114GLA29",
        "trash_type": "CAN",
        "amount": 0.9273543436057324,
        "status": "WAR",
        "location_x": 550.0,
        "location_y": 439.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 30,
        "floor": {
            "pk": 6,
            "name": "4",
            "building": {
                "pk": 1,
                "name": "공학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "114PPR30",
        "trash_type": "GLA",
        "amount": 0.6930401212149503,
        "status": "CAU",
        "location_x": 120.0,
        "location_y": 331.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 31,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B1GER31",
        "trash_type": "GLA",
        "amount": 0.16188987002224609,
        "status": "SAF",
        "location_x": 606.0,
        "location_y": 72.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 32,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B1PET32",
        "trash_type": "GLA",
        "amount": 0.731947380426901,
        "status": "WAR",
        "location_x": 345.0,
        "location_y": 391.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 33,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B1CAN33",
        "trash_type": "GER",
        "amount": 0.5930893549103379,
        "status": "CAU",
        "location_x": 302.0,
        "location_y": 11.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 34,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B1GLA34",
        "trash_type": "GLA",
        "amount": 0.8038241559003625,
        "status": "WAR",
        "location_x": 607.0,
        "location_y": 38.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 35,
        "floor": {
            "pk": 7,
            "name": "B1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B1PPR35",
        "trash_type": "CAN",
        "amount": 0.3493803502257876,
        "status": "SAF",
        "location_x": 237.0,
        "location_y": 95.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 36,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B2GER36",
        "trash_type": "PET",
        "amount": 0.6994045186100626,
        "status": "CAU",
        "location_x": 367.0,
        "location_y": 67.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 37,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B2PET37",
        "trash_type": "PET",
        "amount": 0.8777211814352769,
        "status": "WAR",
        "location_x": 107.0,
        "location_y": 337.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 38,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B2CAN38",
        "trash_type": "GER",
        "amount": 0.018445837965834322,
        "status": "SAF",
        "location_x": 578.0,
        "location_y": 264.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 39,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B2GLA39",
        "trash_type": "PET",
        "amount": 0.31235264332775003,
        "status": "SAF",
        "location_x": 426.0,
        "location_y": 270.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 40,
        "floor": {
            "pk": 8,
            "name": "B2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "12B2PPR40",
        "trash_type": "PET",
        "amount": 0.01904455493239643,
        "status": "SAF",
        "location_x": 79.0,
        "location_y": 441.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 41,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "121GER41",
        "trash_type": "CAN",
        "amount": 0.4568744765533077,
        "status": "CAU",
        "location_x": 188.0,
        "location_y": 142.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 42,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "121PET42",
        "trash_type": "CAN",
        "amount": 0.5730381233514822,
        "status": "CAU",
        "location_x": 519.0,
        "location_y": 156.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 43,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "121CAN43",
        "trash_type": "GER",
        "amount": 0.9966747484843353,
        "status": "WAR",
        "location_x": 519.0,
        "location_y": 380.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 44,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "121GLA44",
        "trash_type": "PET",
        "amount": 0.6098608301257251,
        "status": "CAU",
        "location_x": 407.0,
        "location_y": 368.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 45,
        "floor": {
            "pk": 9,
            "name": "1",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "121PPR45",
        "trash_type": "GLA",
        "amount": 0.053408981394847954,
        "status": "SAF",
        "location_x": 504.0,
        "location_y": 26.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 46,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "122GER46",
        "trash_type": "GLA",
        "amount": 0.6256514939533611,
        "status": "CAU",
        "location_x": 242.0,
        "location_y": 376.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 47,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "122PET47",
        "trash_type": "CAN",
        "amount": 0.601651066791958,
        "status": "CAU",
        "location_x": 618.0,
        "location_y": 61.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 48,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "122CAN48",
        "trash_type": "PPR",
        "amount": 0.9427793522350081,
        "status": "WAR",
        "location_x": 644.0,
        "location_y": 36.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 49,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "122GLA49",
        "trash_type": "CAN",
        "amount": 0.8197464908671505,
        "status": "WAR",
        "location_x": 318.0,
        "location_y": 381.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 50,
        "floor": {
            "pk": 10,
            "name": "2",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "122PPR50",
        "trash_type": "CAN",
        "amount": 0.4757604554561764,
        "status": "CAU",
        "location_x": 99.0,
        "location_y": 67.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 51,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "123GER51",
        "trash_type": "PPR",
        "amount": 0.1886786454663193,
        "status": "SAF",
        "location_x": 521.0,
        "location_y": 441.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 52,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "123PET52",
        "trash_type": "GER",
        "amount": 0.8689964952643203,
        "status": "WAR",
        "location_x": 175.0,
        "location_y": 266.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 53,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "123CAN53",
        "trash_type": "PET",
        "amount": 0.42122185535384726,
        "status": "CAU",
        "location_x": 402.0,
        "location_y": 109.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 54,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "123GLA54",
        "trash_type": "PET",
        "amount": 0.7219078340073469,
        "status": "WAR",
        "location_x": 4.0,
        "location_y": 15.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 55,
        "floor": {
            "pk": 11,
            "name": "3",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "123PPR55",
        "trash_type": "PPR",
        "amount": 0.3106746550148942,
        "status": "SAF",
        "location_x": 171.0,
        "location_y": 95.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 56,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "124GER56",
        "trash_type": "CAN",
        "amount": 0.6742514906905122,
        "status": "CAU",
        "location_x": 643.0,
        "location_y": 186.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 57,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "124PET57",
        "trash_type": "PET",
        "amount": 0.0709249045871504,
        "status": "SAF",
        "location_x": 371.0,
        "location_y": 395.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 58,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "124CAN58",
        "trash_type": "PPR",
        "amount": 0.5620069825720823,
        "status": "CAU",
        "location_x": 268.0,
        "location_y": 54.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 59,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "124GLA59",
        "trash_type": "GER",
        "amount": 0.7970124337333179,
        "status": "WAR",
        "location_x": 647.0,
        "location_y": 152.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 60,
        "floor": {
            "pk": 12,
            "name": "4",
            "building": {
                "pk": 2,
                "name": "어학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "124PPR60",
        "trash_type": "PPR",
        "amount": 0.6296401376502986,
        "status": "CAU",
        "location_x": 593.0,
        "location_y": 358.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 61,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B1GER61",
        "trash_type": "CAN",
        "amount": 0.9794777809452695,
        "status": "WAR",
        "location_x": 108.0,
        "location_y": 36.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 62,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B1PET62",
        "trash_type": "PPR",
        "amount": 0.6032062304222098,
        "status": "CAU",
        "location_x": 631.0,
        "location_y": 141.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 63,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B1CAN63",
        "trash_type": "PET",
        "amount": 0.48359948806974973,
        "status": "CAU",
        "location_x": 449.0,
        "location_y": 376.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 64,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B1GLA64",
        "trash_type": "GLA",
        "amount": 0.6126058457423971,
        "status": "CAU",
        "location_x": 155.0,
        "location_y": 205.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 65,
        "floor": {
            "pk": 13,
            "name": "B1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B1PPR65",
        "trash_type": "GER",
        "amount": 0.2757144696773598,
        "status": "SAF",
        "location_x": 546.0,
        "location_y": 383.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 66,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B2GER66",
        "trash_type": "PET",
        "amount": 0.7509451374668401,
        "status": "WAR",
        "location_x": 276.0,
        "location_y": 251.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 67,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B2PET67",
        "trash_type": "GER",
        "amount": 0.11093349309130107,
        "status": "SAF",
        "location_x": 202.0,
        "location_y": 165.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 68,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B2CAN68",
        "trash_type": "GLA",
        "amount": 0.6689814477873454,
        "status": "CAU",
        "location_x": 248.0,
        "location_y": 262.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 69,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B2GLA69",
        "trash_type": "GER",
        "amount": 0.22232888878552803,
        "status": "SAF",
        "location_x": 50.0,
        "location_y": 59.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 70,
        "floor": {
            "pk": 14,
            "name": "B2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "13B2PPR70",
        "trash_type": "PET",
        "amount": 0.6231341235764403,
        "status": "CAU",
        "location_x": 422.0,
        "location_y": 286.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 71,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "131GER71",
        "trash_type": "PPR",
        "amount": 0.18780638379304593,
        "status": "SAF",
        "location_x": 178.0,
        "location_y": 426.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 72,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "131PET72",
        "trash_type": "PET",
        "amount": 0.5522115372288647,
        "status": "CAU",
        "location_x": 113.0,
        "location_y": 126.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 73,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "131CAN73",
        "trash_type": "PPR",
        "amount": 0.4902210710336137,
        "status": "CAU",
        "location_x": 484.0,
        "location_y": 82.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 74,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "131GLA74",
        "trash_type": "GER",
        "amount": 0.30316375023244957,
        "status": "SAF",
        "location_x": 44.0,
        "location_y": 40.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 75,
        "floor": {
            "pk": 15,
            "name": "1",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "131PPR75",
        "trash_type": "CAN",
        "amount": 0.7961906282852929,
        "status": "WAR",
        "location_x": 628.0,
        "location_y": 215.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 76,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "132GER76",
        "trash_type": "GER",
        "amount": 0.024600467624020128,
        "status": "SAF",
        "location_x": 571.0,
        "location_y": 198.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 77,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "132PET77",
        "trash_type": "GER",
        "amount": 0.5688715652600658,
        "status": "CAU",
        "location_x": 121.0,
        "location_y": 364.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 78,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "132CAN78",
        "trash_type": "CAN",
        "amount": 0.5523943598372882,
        "status": "CAU",
        "location_x": 292.0,
        "location_y": 330.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 79,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "132GLA79",
        "trash_type": "CAN",
        "amount": 0.7170427474860491,
        "status": "WAR",
        "location_x": 220.0,
        "location_y": 412.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 80,
        "floor": {
            "pk": 16,
            "name": "2",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "132PPR80",
        "trash_type": "CAN",
        "amount": 0.9946257655857426,
        "status": "WAR",
        "location_x": 97.0,
        "location_y": 373.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 81,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "133GER81",
        "trash_type": "PET",
        "amount": 0.5533268890205173,
        "status": "CAU",
        "location_x": 72.0,
        "location_y": 30.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 82,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "133PET82",
        "trash_type": "PET",
        "amount": 0.5072641913599506,
        "status": "CAU",
        "location_x": 146.0,
        "location_y": 303.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 83,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "133CAN83",
        "trash_type": "PPR",
        "amount": 0.10333418232189462,
        "status": "SAF",
        "location_x": 425.0,
        "location_y": 19.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 84,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "133GLA84",
        "trash_type": "PPR",
        "amount": 0.2950210871911263,
        "status": "SAF",
        "location_x": 68.0,
        "location_y": 311.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 85,
        "floor": {
            "pk": 17,
            "name": "3",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "133PPR85",
        "trash_type": "PPR",
        "amount": 0.011629154611871084,
        "status": "SAF",
        "location_x": 248.0,
        "location_y": 90.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 86,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "134GER86",
        "trash_type": "CAN",
        "amount": 0.6623930469225193,
        "status": "CAU",
        "location_x": 331.0,
        "location_y": 18.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 87,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "134PET87",
        "trash_type": "GLA",
        "amount": 0.10072709629991172,
        "status": "SAF",
        "location_x": 464.0,
        "location_y": 242.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 88,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "134CAN88",
        "trash_type": "PET",
        "amount": 0.2483458709069417,
        "status": "SAF",
        "location_x": 462.0,
        "location_y": 85.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 89,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "134GLA89",
        "trash_type": "GER",
        "amount": 0.6644994343911783,
        "status": "CAU",
        "location_x": 79.0,
        "location_y": 107.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 90,
        "floor": {
            "pk": 18,
            "name": "4",
            "building": {
                "pk": 3,
                "name": "경영대학관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "134PPR90",
        "trash_type": "CAN",
        "amount": 0.0480875939327301,
        "status": "SAF",
        "location_x": 266.0,
        "location_y": 87.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 91,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B1GER91",
        "trash_type": "GER",
        "amount": 0.2507449578319081,
        "status": "SAF",
        "location_x": 237.0,
        "location_y": 269.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 92,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B1PET92",
        "trash_type": "GLA",
        "amount": 0.2313013557447603,
        "status": "SAF",
        "location_x": 197.0,
        "location_y": 294.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 93,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B1CAN93",
        "trash_type": "PET",
        "amount": 0.46968973708998796,
        "status": "CAU",
        "location_x": 155.0,
        "location_y": 140.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 94,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B1GLA94",
        "trash_type": "GLA",
        "amount": 0.05206406226427418,
        "status": "SAF",
        "location_x": 97.0,
        "location_y": 114.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 95,
        "floor": {
            "pk": 19,
            "name": "B1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B1PPR95",
        "trash_type": "PET",
        "amount": 0.15693116612498248,
        "status": "SAF",
        "location_x": 379.0,
        "location_y": 97.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 96,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B2GER96",
        "trash_type": "PET",
        "amount": 0.17283619515894288,
        "status": "SAF",
        "location_x": 58.0,
        "location_y": 327.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 97,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B2PET97",
        "trash_type": "CAN",
        "amount": 0.7027562378593477,
        "status": "WAR",
        "location_x": 325.0,
        "location_y": 82.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 98,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B2CAN98",
        "trash_type": "GER",
        "amount": 0.7201756966895255,
        "status": "WAR",
        "location_x": 172.0,
        "location_y": 57.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 99,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B2GLA99",
        "trash_type": "PET",
        "amount": 0.23796276472983036,
        "status": "SAF",
        "location_x": 571.0,
        "location_y": 31.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 100,
        "floor": {
            "pk": 20,
            "name": "B2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "14B2PPR100",
        "trash_type": "PET",
        "amount": 0.5638426178674353,
        "status": "CAU",
        "location_x": 511.0,
        "location_y": 182.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 101,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "141GER101",
        "trash_type": "GER",
        "amount": 0.33552647892010623,
        "status": "SAF",
        "location_x": 218.0,
        "location_y": 325.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 102,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "141PET102",
        "trash_type": "PET",
        "amount": 0.9359510295383939,
        "status": "WAR",
        "location_x": 9.0,
        "location_y": 291.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 103,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "141CAN103",
        "trash_type": "CAN",
        "amount": 0.754664096669843,
        "status": "WAR",
        "location_x": 615.0,
        "location_y": 352.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 104,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "141GLA104",
        "trash_type": "GLA",
        "amount": 0.7889070335674595,
        "status": "WAR",
        "location_x": 249.0,
        "location_y": 407.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 105,
        "floor": {
            "pk": 21,
            "name": "1",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "141PPR105",
        "trash_type": "CAN",
        "amount": 0.48338236640970966,
        "status": "CAU",
        "location_x": 34.0,
        "location_y": 331.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 106,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "142GER106",
        "trash_type": "GER",
        "amount": 0.10491009212530145,
        "status": "SAF",
        "location_x": 360.0,
        "location_y": 297.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 107,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "142PET107",
        "trash_type": "GLA",
        "amount": 0.012113876745548868,
        "status": "SAF",
        "location_x": 12.0,
        "location_y": 161.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 108,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "142CAN108",
        "trash_type": "GLA",
        "amount": 0.486379581766767,
        "status": "CAU",
        "location_x": 347.0,
        "location_y": 165.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 109,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "142GLA109",
        "trash_type": "GLA",
        "amount": 0.6740920295296792,
        "status": "CAU",
        "location_x": 480.0,
        "location_y": 135.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 110,
        "floor": {
            "pk": 22,
            "name": "2",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "142PPR110",
        "trash_type": "PPR",
        "amount": 0.06983216048426777,
        "status": "SAF",
        "location_x": 146.0,
        "location_y": 338.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 111,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "143GER111",
        "trash_type": "CAN",
        "amount": 0.9582087716593081,
        "status": "WAR",
        "location_x": 143.0,
        "location_y": 449.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 112,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "143PET112",
        "trash_type": "GER",
        "amount": 0.6883222651041662,
        "status": "CAU",
        "location_x": 549.0,
        "location_y": 254.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 113,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "143CAN113",
        "trash_type": "GLA",
        "amount": 0.14509975905669248,
        "status": "SAF",
        "location_x": 38.0,
        "location_y": 383.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 114,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "143GLA114",
        "trash_type": "PET",
        "amount": 0.6266435676484646,
        "status": "CAU",
        "location_x": 506.0,
        "location_y": 320.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 115,
        "floor": {
            "pk": 23,
            "name": "3",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "143PPR115",
        "trash_type": "PPR",
        "amount": 0.48132293763003,
        "status": "CAU",
        "location_x": 116.0,
        "location_y": 140.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 116,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "144GER116",
        "trash_type": "GER",
        "amount": 0.033308476815090415,
        "status": "SAF",
        "location_x": 44.0,
        "location_y": 149.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 117,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "144PET117",
        "trash_type": "PPR",
        "amount": 0.3463125291316723,
        "status": "SAF",
        "location_x": 37.0,
        "location_y": 224.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 118,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "144CAN118",
        "trash_type": "PET",
        "amount": 0.5692850940963058,
        "status": "CAU",
        "location_x": 562.0,
        "location_y": 396.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 119,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "144GLA119",
        "trash_type": "GLA",
        "amount": 0.7305711418229817,
        "status": "WAR",
        "location_x": 73.0,
        "location_y": 385.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 120,
        "floor": {
            "pk": 24,
            "name": "4",
            "building": {
                "pk": 4,
                "name": "체육관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "144PPR120",
        "trash_type": "CAN",
        "amount": 0.3281316972567533,
        "status": "SAF",
        "location_x": 8.0,
        "location_y": 202.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 121,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B1GER121",
        "trash_type": "CAN",
        "amount": 0.38678454873739065,
        "status": "SAF",
        "location_x": 369.0,
        "location_y": 33.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 122,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B1PET122",
        "trash_type": "CAN",
        "amount": 0.647104910076276,
        "status": "CAU",
        "location_x": 562.0,
        "location_y": 167.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 123,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B1CAN123",
        "trash_type": "PPR",
        "amount": 0.7921510591076073,
        "status": "WAR",
        "location_x": 555.0,
        "location_y": 344.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 124,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B1GLA124",
        "trash_type": "GLA",
        "amount": 0.15776160138923734,
        "status": "SAF",
        "location_x": 544.0,
        "location_y": 337.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 125,
        "floor": {
            "pk": 25,
            "name": "B1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B1PPR125",
        "trash_type": "GER",
        "amount": 0.533954856308741,
        "status": "CAU",
        "location_x": 532.0,
        "location_y": 97.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 126,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B2GER126",
        "trash_type": "GER",
        "amount": 0.09461484831920364,
        "status": "SAF",
        "location_x": 535.0,
        "location_y": 199.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 127,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B2PET127",
        "trash_type": "GER",
        "amount": 0.8310354839313094,
        "status": "WAR",
        "location_x": 467.0,
        "location_y": 132.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 128,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B2CAN128",
        "trash_type": "PPR",
        "amount": 0.8577156066924535,
        "status": "WAR",
        "location_x": 425.0,
        "location_y": 394.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 129,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B2GLA129",
        "trash_type": "CAN",
        "amount": 0.8110432911450232,
        "status": "WAR",
        "location_x": 125.0,
        "location_y": 85.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 130,
        "floor": {
            "pk": 26,
            "name": "B2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "15B2PPR130",
        "trash_type": "GER",
        "amount": 0.8249054193819568,
        "status": "WAR",
        "location_x": 529.0,
        "location_y": 177.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 131,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "151GER131",
        "trash_type": "GLA",
        "amount": 0.21461973113484645,
        "status": "SAF",
        "location_x": 393.0,
        "location_y": 424.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 132,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "151PET132",
        "trash_type": "GLA",
        "amount": 0.09943017294139878,
        "status": "SAF",
        "location_x": 249.0,
        "location_y": 281.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 133,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "151CAN133",
        "trash_type": "GLA",
        "amount": 0.9954454357558121,
        "status": "WAR",
        "location_x": 73.0,
        "location_y": 172.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 134,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "151GLA134",
        "trash_type": "GER",
        "amount": 0.6067851924186186,
        "status": "CAU",
        "location_x": 592.0,
        "location_y": 422.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 135,
        "floor": {
            "pk": 27,
            "name": "1",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "151PPR135",
        "trash_type": "PPR",
        "amount": 0.6108084697141408,
        "status": "CAU",
        "location_x": 303.0,
        "location_y": 173.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 136,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "152GER136",
        "trash_type": "GER",
        "amount": 0.9513818326707264,
        "status": "WAR",
        "location_x": 500.0,
        "location_y": 335.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 137,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "152PET137",
        "trash_type": "PPR",
        "amount": 0.07781365568794496,
        "status": "SAF",
        "location_x": 6.0,
        "location_y": 430.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 138,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "152CAN138",
        "trash_type": "GER",
        "amount": 0.8822379661187651,
        "status": "WAR",
        "location_x": 560.0,
        "location_y": 195.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 139,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "152GLA139",
        "trash_type": "PET",
        "amount": 0.8102196179378952,
        "status": "WAR",
        "location_x": 588.0,
        "location_y": 16.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 140,
        "floor": {
            "pk": 28,
            "name": "2",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "152PPR140",
        "trash_type": "GER",
        "amount": 0.6051767667287273,
        "status": "CAU",
        "location_x": 77.0,
        "location_y": 414.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 141,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "153GER141",
        "trash_type": "PPR",
        "amount": 0.7734549261117075,
        "status": "WAR",
        "location_x": 558.0,
        "location_y": 49.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 142,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "153PET142",
        "trash_type": "PET",
        "amount": 0.23262675428306023,
        "status": "SAF",
        "location_x": 420.0,
        "location_y": 184.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 143,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "153CAN143",
        "trash_type": "GLA",
        "amount": 0.06856565955237148,
        "status": "SAF",
        "location_x": 190.0,
        "location_y": 440.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 144,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "153GLA144",
        "trash_type": "CAN",
        "amount": 0.7049437366031501,
        "status": "WAR",
        "location_x": 145.0,
        "location_y": 2.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 145,
        "floor": {
            "pk": 29,
            "name": "3",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "153PPR145",
        "trash_type": "GLA",
        "amount": 0.7136337289313642,
        "status": "WAR",
        "location_x": 260.0,
        "location_y": 148.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 146,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "154GER146",
        "trash_type": "CAN",
        "amount": 0.33130950034910156,
        "status": "SAF",
        "location_x": 104.0,
        "location_y": 245.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 147,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "154PET147",
        "trash_type": "PET",
        "amount": 0.07192161783065287,
        "status": "SAF",
        "location_x": 95.0,
        "location_y": 103.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 148,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "154CAN148",
        "trash_type": "GER",
        "amount": 0.8528921519143379,
        "status": "WAR",
        "location_x": 458.0,
        "location_y": 270.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 149,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "154GLA149",
        "trash_type": "PPR",
        "amount": 0.673047434184291,
        "status": "CAU",
        "location_x": 213.0,
        "location_y": 101.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 150,
        "floor": {
            "pk": 30,
            "name": "4",
            "building": {
                "pk": 5,
                "name": "중앙도서관",
                "campus": {
                    "pk": 1,
                    "name": "서울대학교"
                }
            }
        },
        "token": "154PPR150",
        "trash_type": "PET",
        "amount": 0.2670719854147414,
        "status": "SAF",
        "location_x": 143.0,
        "location_y": 399.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 151,
        "floor": {
            "pk": 31,
            "name": "B1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B1GER151",
        "trash_type": "PET",
        "amount": 0.20308342226293197,
        "status": "SAF",
        "location_x": 403.0,
        "location_y": 449.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 152,
        "floor": {
            "pk": 31,
            "name": "B1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B1PET152",
        "trash_type": "GER",
        "amount": 0.8303051405426235,
        "status": "WAR",
        "location_x": 225.0,
        "location_y": 10.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 153,
        "floor": {
            "pk": 31,
            "name": "B1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B1CAN153",
        "trash_type": "GLA",
        "amount": 0.4694748335136525,
        "status": "CAU",
        "location_x": 210.0,
        "location_y": 262.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 154,
        "floor": {
            "pk": 31,
            "name": "B1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B1GLA154",
        "trash_type": "PPR",
        "amount": 0.7456693955530496,
        "status": "WAR",
        "location_x": 289.0,
        "location_y": 315.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 155,
        "floor": {
            "pk": 31,
            "name": "B1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B1PPR155",
        "trash_type": "GLA",
        "amount": 0.631055493193224,
        "status": "CAU",
        "location_x": 608.0,
        "location_y": 255.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 156,
        "floor": {
            "pk": 32,
            "name": "B2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B2GER156",
        "trash_type": "CAN",
        "amount": 0.8226528001999993,
        "status": "WAR",
        "location_x": 527.0,
        "location_y": 389.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 157,
        "floor": {
            "pk": 32,
            "name": "B2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B2PET157",
        "trash_type": "PPR",
        "amount": 0.07310698773979951,
        "status": "SAF",
        "location_x": 405.0,
        "location_y": 429.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 158,
        "floor": {
            "pk": 32,
            "name": "B2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B2CAN158",
        "trash_type": "PET",
        "amount": 0.9533866795673981,
        "status": "WAR",
        "location_x": 283.0,
        "location_y": 169.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 159,
        "floor": {
            "pk": 32,
            "name": "B2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B2GLA159",
        "trash_type": "GLA",
        "amount": 0.7847417401170127,
        "status": "WAR",
        "location_x": 574.0,
        "location_y": 320.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 160,
        "floor": {
            "pk": 32,
            "name": "B2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "21B2PPR160",
        "trash_type": "PPR",
        "amount": 0.8711344004295105,
        "status": "WAR",
        "location_x": 528.0,
        "location_y": 1.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 161,
        "floor": {
            "pk": 33,
            "name": "1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "211GER161",
        "trash_type": "PET",
        "amount": 0.8903884205837709,
        "status": "WAR",
        "location_x": 153.0,
        "location_y": 130.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 162,
        "floor": {
            "pk": 33,
            "name": "1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "211PET162",
        "trash_type": "GER",
        "amount": 0.4543068018571157,
        "status": "CAU",
        "location_x": 274.0,
        "location_y": 33.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 163,
        "floor": {
            "pk": 33,
            "name": "1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "211CAN163",
        "trash_type": "GER",
        "amount": 0.7094918793109538,
        "status": "WAR",
        "location_x": 381.0,
        "location_y": 173.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 164,
        "floor": {
            "pk": 33,
            "name": "1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "211GLA164",
        "trash_type": "CAN",
        "amount": 0.469295766050416,
        "status": "CAU",
        "location_x": 333.0,
        "location_y": 233.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 165,
        "floor": {
            "pk": 33,
            "name": "1",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "211PPR165",
        "trash_type": "PPR",
        "amount": 0.07313206750009726,
        "status": "SAF",
        "location_x": 15.0,
        "location_y": 228.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 166,
        "floor": {
            "pk": 34,
            "name": "2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "212GER166",
        "trash_type": "CAN",
        "amount": 0.9586146654853874,
        "status": "WAR",
        "location_x": 526.0,
        "location_y": 197.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 167,
        "floor": {
            "pk": 34,
            "name": "2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "212PET167",
        "trash_type": "CAN",
        "amount": 0.6203634573467821,
        "status": "CAU",
        "location_x": 437.0,
        "location_y": 73.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 168,
        "floor": {
            "pk": 34,
            "name": "2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "212CAN168",
        "trash_type": "GLA",
        "amount": 0.5483830997405325,
        "status": "CAU",
        "location_x": 426.0,
        "location_y": 381.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 169,
        "floor": {
            "pk": 34,
            "name": "2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "212GLA169",
        "trash_type": "PPR",
        "amount": 0.03288935426360673,
        "status": "SAF",
        "location_x": 628.0,
        "location_y": 110.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 170,
        "floor": {
            "pk": 34,
            "name": "2",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "212PPR170",
        "trash_type": "GER",
        "amount": 0.30450347548368173,
        "status": "SAF",
        "location_x": 362.0,
        "location_y": 205.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 171,
        "floor": {
            "pk": 35,
            "name": "3",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "213GER171",
        "trash_type": "PET",
        "amount": 0.07825358264925841,
        "status": "SAF",
        "location_x": 340.0,
        "location_y": 347.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 172,
        "floor": {
            "pk": 35,
            "name": "3",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "213PET172",
        "trash_type": "PPR",
        "amount": 0.5412438034529079,
        "status": "CAU",
        "location_x": 266.0,
        "location_y": 8.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 173,
        "floor": {
            "pk": 35,
            "name": "3",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "213CAN173",
        "trash_type": "GLA",
        "amount": 0.3774164211408716,
        "status": "SAF",
        "location_x": 227.0,
        "location_y": 103.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 174,
        "floor": {
            "pk": 35,
            "name": "3",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "213GLA174",
        "trash_type": "GER",
        "amount": 0.49991369331927027,
        "status": "CAU",
        "location_x": 612.0,
        "location_y": 248.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 175,
        "floor": {
            "pk": 35,
            "name": "3",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "213PPR175",
        "trash_type": "GLA",
        "amount": 0.19375748011096006,
        "status": "SAF",
        "location_x": 501.0,
        "location_y": 393.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 176,
        "floor": {
            "pk": 36,
            "name": "4",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "214GER176",
        "trash_type": "GLA",
        "amount": 0.28354451737625364,
        "status": "SAF",
        "location_x": 172.0,
        "location_y": 174.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 177,
        "floor": {
            "pk": 36,
            "name": "4",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "214PET177",
        "trash_type": "GER",
        "amount": 0.40326416974473756,
        "status": "CAU",
        "location_x": 60.0,
        "location_y": 119.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 178,
        "floor": {
            "pk": 36,
            "name": "4",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "214CAN178",
        "trash_type": "GLA",
        "amount": 0.8714605019402237,
        "status": "WAR",
        "location_x": 578.0,
        "location_y": 311.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 179,
        "floor": {
            "pk": 36,
            "name": "4",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "214GLA179",
        "trash_type": "PET",
        "amount": 0.985047940126091,
        "status": "WAR",
        "location_x": 495.0,
        "location_y": 221.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 180,
        "floor": {
            "pk": 36,
            "name": "4",
            "building": {
                "pk": 6,
                "name": "공학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "214PPR180",
        "trash_type": "GLA",
        "amount": 0.918415955120195,
        "status": "WAR",
        "location_x": 312.0,
        "location_y": 69.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 181,
        "floor": {
            "pk": 37,
            "name": "B1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B1GER181",
        "trash_type": "GER",
        "amount": 0.06225449523635129,
        "status": "SAF",
        "location_x": 516.0,
        "location_y": 393.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 182,
        "floor": {
            "pk": 37,
            "name": "B1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B1PET182",
        "trash_type": "PET",
        "amount": 0.814428412278265,
        "status": "WAR",
        "location_x": 394.0,
        "location_y": 62.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 183,
        "floor": {
            "pk": 37,
            "name": "B1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B1CAN183",
        "trash_type": "PPR",
        "amount": 0.22679943249896117,
        "status": "SAF",
        "location_x": 199.0,
        "location_y": 137.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 184,
        "floor": {
            "pk": 37,
            "name": "B1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B1GLA184",
        "trash_type": "GER",
        "amount": 0.6447251695954729,
        "status": "CAU",
        "location_x": 144.0,
        "location_y": 396.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 185,
        "floor": {
            "pk": 37,
            "name": "B1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B1PPR185",
        "trash_type": "PPR",
        "amount": 0.503237976984403,
        "status": "CAU",
        "location_x": 422.0,
        "location_y": 392.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 186,
        "floor": {
            "pk": 38,
            "name": "B2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B2GER186",
        "trash_type": "PET",
        "amount": 0.4003253760474351,
        "status": "CAU",
        "location_x": 355.0,
        "location_y": 101.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 187,
        "floor": {
            "pk": 38,
            "name": "B2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B2PET187",
        "trash_type": "CAN",
        "amount": 0.7269117612296134,
        "status": "WAR",
        "location_x": 213.0,
        "location_y": 199.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 188,
        "floor": {
            "pk": 38,
            "name": "B2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B2CAN188",
        "trash_type": "GLA",
        "amount": 0.32705031177664423,
        "status": "SAF",
        "location_x": 153.0,
        "location_y": 410.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 189,
        "floor": {
            "pk": 38,
            "name": "B2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B2GLA189",
        "trash_type": "CAN",
        "amount": 0.4110838362231577,
        "status": "CAU",
        "location_x": 225.0,
        "location_y": 302.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 190,
        "floor": {
            "pk": 38,
            "name": "B2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "22B2PPR190",
        "trash_type": "GER",
        "amount": 0.4934720442121181,
        "status": "CAU",
        "location_x": 39.0,
        "location_y": 145.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 191,
        "floor": {
            "pk": 39,
            "name": "1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "221GER191",
        "trash_type": "CAN",
        "amount": 0.7029997223813548,
        "status": "WAR",
        "location_x": 64.0,
        "location_y": 303.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 192,
        "floor": {
            "pk": 39,
            "name": "1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "221PET192",
        "trash_type": "GER",
        "amount": 0.9595566862595889,
        "status": "WAR",
        "location_x": 200.0,
        "location_y": 18.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 193,
        "floor": {
            "pk": 39,
            "name": "1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "221CAN193",
        "trash_type": "GER",
        "amount": 0.6378759635957865,
        "status": "CAU",
        "location_x": 319.0,
        "location_y": 445.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 194,
        "floor": {
            "pk": 39,
            "name": "1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "221GLA194",
        "trash_type": "PET",
        "amount": 0.011152608965706579,
        "status": "SAF",
        "location_x": 130.0,
        "location_y": 351.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 195,
        "floor": {
            "pk": 39,
            "name": "1",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "221PPR195",
        "trash_type": "CAN",
        "amount": 0.877395259195514,
        "status": "WAR",
        "location_x": 409.0,
        "location_y": 296.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 196,
        "floor": {
            "pk": 40,
            "name": "2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "222GER196",
        "trash_type": "GLA",
        "amount": 0.6788989530667311,
        "status": "CAU",
        "location_x": 21.0,
        "location_y": 129.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 197,
        "floor": {
            "pk": 40,
            "name": "2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "222PET197",
        "trash_type": "GLA",
        "amount": 0.7299130286260832,
        "status": "WAR",
        "location_x": 352.0,
        "location_y": 20.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 198,
        "floor": {
            "pk": 40,
            "name": "2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "222CAN198",
        "trash_type": "GLA",
        "amount": 0.5979327996504634,
        "status": "CAU",
        "location_x": 538.0,
        "location_y": 273.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 199,
        "floor": {
            "pk": 40,
            "name": "2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "222GLA199",
        "trash_type": "PPR",
        "amount": 0.6993725555429149,
        "status": "CAU",
        "location_x": 460.0,
        "location_y": 211.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 200,
        "floor": {
            "pk": 40,
            "name": "2",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "222PPR200",
        "trash_type": "GER",
        "amount": 0.5425656240298775,
        "status": "CAU",
        "location_x": 319.0,
        "location_y": 91.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 201,
        "floor": {
            "pk": 41,
            "name": "3",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "223GER201",
        "trash_type": "PPR",
        "amount": 0.6648399526871694,
        "status": "CAU",
        "location_x": 494.0,
        "location_y": 14.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 202,
        "floor": {
            "pk": 41,
            "name": "3",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "223PET202",
        "trash_type": "PET",
        "amount": 0.08263527946071547,
        "status": "SAF",
        "location_x": 426.0,
        "location_y": 94.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 203,
        "floor": {
            "pk": 41,
            "name": "3",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "223CAN203",
        "trash_type": "CAN",
        "amount": 0.5324441761540991,
        "status": "CAU",
        "location_x": 479.0,
        "location_y": 56.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 204,
        "floor": {
            "pk": 41,
            "name": "3",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "223GLA204",
        "trash_type": "GLA",
        "amount": 0.38497272223508217,
        "status": "SAF",
        "location_x": 252.0,
        "location_y": 403.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 205,
        "floor": {
            "pk": 41,
            "name": "3",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "223PPR205",
        "trash_type": "CAN",
        "amount": 0.4774424514175256,
        "status": "CAU",
        "location_x": 561.0,
        "location_y": 427.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 206,
        "floor": {
            "pk": 42,
            "name": "4",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "224GER206",
        "trash_type": "GER",
        "amount": 0.9262458694113643,
        "status": "WAR",
        "location_x": 101.0,
        "location_y": 363.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 207,
        "floor": {
            "pk": 42,
            "name": "4",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "224PET207",
        "trash_type": "PPR",
        "amount": 0.33826980550139096,
        "status": "SAF",
        "location_x": 537.0,
        "location_y": 254.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 208,
        "floor": {
            "pk": 42,
            "name": "4",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "224CAN208",
        "trash_type": "PPR",
        "amount": 0.9138938420344809,
        "status": "WAR",
        "location_x": 271.0,
        "location_y": 435.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 209,
        "floor": {
            "pk": 42,
            "name": "4",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "224GLA209",
        "trash_type": "GLA",
        "amount": 0.5532387192695456,
        "status": "CAU",
        "location_x": 407.0,
        "location_y": 341.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 210,
        "floor": {
            "pk": 42,
            "name": "4",
            "building": {
                "pk": 7,
                "name": "어학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "224PPR210",
        "trash_type": "PET",
        "amount": 0.3291896781123469,
        "status": "SAF",
        "location_x": 249.0,
        "location_y": 72.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 211,
        "floor": {
            "pk": 43,
            "name": "B1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B1GER211",
        "trash_type": "GER",
        "amount": 0.22959235780368503,
        "status": "SAF",
        "location_x": 86.0,
        "location_y": 47.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 212,
        "floor": {
            "pk": 43,
            "name": "B1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B1PET212",
        "trash_type": "PPR",
        "amount": 0.9716606473320132,
        "status": "WAR",
        "location_x": 81.0,
        "location_y": 351.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 213,
        "floor": {
            "pk": 43,
            "name": "B1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B1CAN213",
        "trash_type": "PPR",
        "amount": 0.9848264189049021,
        "status": "WAR",
        "location_x": 263.0,
        "location_y": 3.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 214,
        "floor": {
            "pk": 43,
            "name": "B1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B1GLA214",
        "trash_type": "CAN",
        "amount": 0.2879093553701114,
        "status": "SAF",
        "location_x": 74.0,
        "location_y": 240.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 215,
        "floor": {
            "pk": 43,
            "name": "B1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B1PPR215",
        "trash_type": "PET",
        "amount": 0.805501502965929,
        "status": "WAR",
        "location_x": 526.0,
        "location_y": 251.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 216,
        "floor": {
            "pk": 44,
            "name": "B2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B2GER216",
        "trash_type": "GER",
        "amount": 0.229100801396373,
        "status": "SAF",
        "location_x": 564.0,
        "location_y": 33.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 217,
        "floor": {
            "pk": 44,
            "name": "B2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B2PET217",
        "trash_type": "GLA",
        "amount": 0.08667524807850235,
        "status": "SAF",
        "location_x": 13.0,
        "location_y": 152.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 218,
        "floor": {
            "pk": 44,
            "name": "B2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B2CAN218",
        "trash_type": "GER",
        "amount": 0.19924713225655555,
        "status": "SAF",
        "location_x": 384.0,
        "location_y": 95.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 219,
        "floor": {
            "pk": 44,
            "name": "B2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B2GLA219",
        "trash_type": "CAN",
        "amount": 0.07245716838224081,
        "status": "SAF",
        "location_x": 425.0,
        "location_y": 74.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 220,
        "floor": {
            "pk": 44,
            "name": "B2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "23B2PPR220",
        "trash_type": "PET",
        "amount": 0.8997609962818367,
        "status": "WAR",
        "location_x": 498.0,
        "location_y": 268.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 221,
        "floor": {
            "pk": 45,
            "name": "1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "231GER221",
        "trash_type": "GER",
        "amount": 0.8557165536306853,
        "status": "WAR",
        "location_x": 150.0,
        "location_y": 438.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 222,
        "floor": {
            "pk": 45,
            "name": "1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "231PET222",
        "trash_type": "GER",
        "amount": 0.8871229273361082,
        "status": "WAR",
        "location_x": 76.0,
        "location_y": 144.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 223,
        "floor": {
            "pk": 45,
            "name": "1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "231CAN223",
        "trash_type": "CAN",
        "amount": 0.3447577287942487,
        "status": "SAF",
        "location_x": 58.0,
        "location_y": 431.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 224,
        "floor": {
            "pk": 45,
            "name": "1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "231GLA224",
        "trash_type": "PET",
        "amount": 0.20362899252957978,
        "status": "SAF",
        "location_x": 234.0,
        "location_y": 126.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 225,
        "floor": {
            "pk": 45,
            "name": "1",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "231PPR225",
        "trash_type": "GER",
        "amount": 0.3760721428062459,
        "status": "SAF",
        "location_x": 637.0,
        "location_y": 220.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 226,
        "floor": {
            "pk": 46,
            "name": "2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "232GER226",
        "trash_type": "GER",
        "amount": 0.3946646904376423,
        "status": "SAF",
        "location_x": 291.0,
        "location_y": 394.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 227,
        "floor": {
            "pk": 46,
            "name": "2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "232PET227",
        "trash_type": "PET",
        "amount": 0.5551101716635974,
        "status": "CAU",
        "location_x": 441.0,
        "location_y": 397.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 228,
        "floor": {
            "pk": 46,
            "name": "2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "232CAN228",
        "trash_type": "PET",
        "amount": 0.9129921733440851,
        "status": "WAR",
        "location_x": 253.0,
        "location_y": 38.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 229,
        "floor": {
            "pk": 46,
            "name": "2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "232GLA229",
        "trash_type": "GER",
        "amount": 0.8573779842132693,
        "status": "WAR",
        "location_x": 14.0,
        "location_y": 280.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 230,
        "floor": {
            "pk": 46,
            "name": "2",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "232PPR230",
        "trash_type": "PPR",
        "amount": 0.573183434286295,
        "status": "CAU",
        "location_x": 406.0,
        "location_y": 30.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 231,
        "floor": {
            "pk": 47,
            "name": "3",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "233GER231",
        "trash_type": "PET",
        "amount": 0.520003365385751,
        "status": "CAU",
        "location_x": 395.0,
        "location_y": 4.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 232,
        "floor": {
            "pk": 47,
            "name": "3",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "233PET232",
        "trash_type": "GLA",
        "amount": 0.14874832073250555,
        "status": "SAF",
        "location_x": 302.0,
        "location_y": 154.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 233,
        "floor": {
            "pk": 47,
            "name": "3",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "233CAN233",
        "trash_type": "CAN",
        "amount": 0.9803160124861645,
        "status": "WAR",
        "location_x": 185.0,
        "location_y": 113.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 234,
        "floor": {
            "pk": 47,
            "name": "3",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "233GLA234",
        "trash_type": "PPR",
        "amount": 0.7018958071773483,
        "status": "WAR",
        "location_x": 432.0,
        "location_y": 153.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 235,
        "floor": {
            "pk": 47,
            "name": "3",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "233PPR235",
        "trash_type": "GER",
        "amount": 0.6720230600048883,
        "status": "CAU",
        "location_x": 599.0,
        "location_y": 118.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 236,
        "floor": {
            "pk": 48,
            "name": "4",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "234GER236",
        "trash_type": "PPR",
        "amount": 0.5914654586511686,
        "status": "CAU",
        "location_x": 627.0,
        "location_y": 384.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 237,
        "floor": {
            "pk": 48,
            "name": "4",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "234PET237",
        "trash_type": "GER",
        "amount": 0.01906768890945365,
        "status": "SAF",
        "location_x": 532.0,
        "location_y": 313.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 238,
        "floor": {
            "pk": 48,
            "name": "4",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "234CAN238",
        "trash_type": "GER",
        "amount": 0.9056907986890254,
        "status": "WAR",
        "location_x": 326.0,
        "location_y": 280.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 239,
        "floor": {
            "pk": 48,
            "name": "4",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "234GLA239",
        "trash_type": "CAN",
        "amount": 0.013635571767902532,
        "status": "SAF",
        "location_x": 304.0,
        "location_y": 429.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 240,
        "floor": {
            "pk": 48,
            "name": "4",
            "building": {
                "pk": 8,
                "name": "경영대학관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "234PPR240",
        "trash_type": "PET",
        "amount": 0.3884434997628331,
        "status": "SAF",
        "location_x": 601.0,
        "location_y": 405.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 241,
        "floor": {
            "pk": 49,
            "name": "B1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B1GER241",
        "trash_type": "PET",
        "amount": 0.9518206161791449,
        "status": "WAR",
        "location_x": 512.0,
        "location_y": 94.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 242,
        "floor": {
            "pk": 49,
            "name": "B1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B1PET242",
        "trash_type": "PPR",
        "amount": 0.11318324971432348,
        "status": "SAF",
        "location_x": 171.0,
        "location_y": 313.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 243,
        "floor": {
            "pk": 49,
            "name": "B1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B1CAN243",
        "trash_type": "PPR",
        "amount": 0.10689508249379787,
        "status": "SAF",
        "location_x": 628.0,
        "location_y": 291.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 244,
        "floor": {
            "pk": 49,
            "name": "B1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B1GLA244",
        "trash_type": "PET",
        "amount": 0.8652095880024753,
        "status": "WAR",
        "location_x": 308.0,
        "location_y": 17.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 245,
        "floor": {
            "pk": 49,
            "name": "B1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B1PPR245",
        "trash_type": "PPR",
        "amount": 0.8265168294403769,
        "status": "WAR",
        "location_x": 592.0,
        "location_y": 380.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 246,
        "floor": {
            "pk": 50,
            "name": "B2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B2GER246",
        "trash_type": "CAN",
        "amount": 0.8147117105054766,
        "status": "WAR",
        "location_x": 59.0,
        "location_y": 276.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 247,
        "floor": {
            "pk": 50,
            "name": "B2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B2PET247",
        "trash_type": "GER",
        "amount": 0.34685664602833277,
        "status": "SAF",
        "location_x": 476.0,
        "location_y": 327.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 248,
        "floor": {
            "pk": 50,
            "name": "B2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B2CAN248",
        "trash_type": "GER",
        "amount": 0.8698389776637111,
        "status": "WAR",
        "location_x": 47.0,
        "location_y": 142.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 249,
        "floor": {
            "pk": 50,
            "name": "B2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B2GLA249",
        "trash_type": "GER",
        "amount": 0.7729025182883109,
        "status": "WAR",
        "location_x": 77.0,
        "location_y": 317.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 250,
        "floor": {
            "pk": 50,
            "name": "B2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "24B2PPR250",
        "trash_type": "CAN",
        "amount": 0.7639583301698274,
        "status": "WAR",
        "location_x": 294.0,
        "location_y": 313.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 251,
        "floor": {
            "pk": 51,
            "name": "1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "241GER251",
        "trash_type": "PET",
        "amount": 0.08546585570537102,
        "status": "SAF",
        "location_x": 390.0,
        "location_y": 282.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 252,
        "floor": {
            "pk": 51,
            "name": "1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "241PET252",
        "trash_type": "GER",
        "amount": 0.848176758543091,
        "status": "WAR",
        "location_x": 269.0,
        "location_y": 314.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 253,
        "floor": {
            "pk": 51,
            "name": "1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "241CAN253",
        "trash_type": "PPR",
        "amount": 0.046991475318448384,
        "status": "SAF",
        "location_x": 187.0,
        "location_y": 155.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 254,
        "floor": {
            "pk": 51,
            "name": "1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "241GLA254",
        "trash_type": "PPR",
        "amount": 0.695317053441856,
        "status": "CAU",
        "location_x": 503.0,
        "location_y": 248.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 255,
        "floor": {
            "pk": 51,
            "name": "1",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "241PPR255",
        "trash_type": "GER",
        "amount": 0.8941416033861626,
        "status": "WAR",
        "location_x": 284.0,
        "location_y": 142.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 256,
        "floor": {
            "pk": 52,
            "name": "2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "242GER256",
        "trash_type": "PET",
        "amount": 0.8574562862309123,
        "status": "WAR",
        "location_x": 503.0,
        "location_y": 225.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 257,
        "floor": {
            "pk": 52,
            "name": "2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "242PET257",
        "trash_type": "GLA",
        "amount": 0.01259257138036407,
        "status": "SAF",
        "location_x": 207.0,
        "location_y": 398.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 258,
        "floor": {
            "pk": 52,
            "name": "2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "242CAN258",
        "trash_type": "CAN",
        "amount": 0.6614067325572056,
        "status": "CAU",
        "location_x": 575.0,
        "location_y": 14.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 259,
        "floor": {
            "pk": 52,
            "name": "2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "242GLA259",
        "trash_type": "PET",
        "amount": 0.08146554521388072,
        "status": "SAF",
        "location_x": 199.0,
        "location_y": 19.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 260,
        "floor": {
            "pk": 52,
            "name": "2",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "242PPR260",
        "trash_type": "PPR",
        "amount": 0.0735612462522427,
        "status": "SAF",
        "location_x": 173.0,
        "location_y": 359.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 261,
        "floor": {
            "pk": 53,
            "name": "3",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "243GER261",
        "trash_type": "CAN",
        "amount": 0.15279095643240748,
        "status": "SAF",
        "location_x": 284.0,
        "location_y": 194.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 262,
        "floor": {
            "pk": 53,
            "name": "3",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "243PET262",
        "trash_type": "PET",
        "amount": 0.5340471024520471,
        "status": "CAU",
        "location_x": 189.0,
        "location_y": 406.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 263,
        "floor": {
            "pk": 53,
            "name": "3",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "243CAN263",
        "trash_type": "PPR",
        "amount": 0.5186517352194269,
        "status": "CAU",
        "location_x": 308.0,
        "location_y": 140.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 264,
        "floor": {
            "pk": 53,
            "name": "3",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "243GLA264",
        "trash_type": "PPR",
        "amount": 0.9244898474334026,
        "status": "WAR",
        "location_x": 504.0,
        "location_y": 271.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 265,
        "floor": {
            "pk": 53,
            "name": "3",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "243PPR265",
        "trash_type": "PET",
        "amount": 0.7812676532785024,
        "status": "WAR",
        "location_x": 221.0,
        "location_y": 342.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 266,
        "floor": {
            "pk": 54,
            "name": "4",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "244GER266",
        "trash_type": "GLA",
        "amount": 0.3471184928099226,
        "status": "SAF",
        "location_x": 10.0,
        "location_y": 173.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 267,
        "floor": {
            "pk": 54,
            "name": "4",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "244PET267",
        "trash_type": "PPR",
        "amount": 0.38516140235081375,
        "status": "SAF",
        "location_x": 573.0,
        "location_y": 116.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 268,
        "floor": {
            "pk": 54,
            "name": "4",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "244CAN268",
        "trash_type": "PET",
        "amount": 0.7402360892307398,
        "status": "WAR",
        "location_x": 519.0,
        "location_y": 29.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 269,
        "floor": {
            "pk": 54,
            "name": "4",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "244GLA269",
        "trash_type": "PPR",
        "amount": 0.4444352768391554,
        "status": "CAU",
        "location_x": 506.0,
        "location_y": 25.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 270,
        "floor": {
            "pk": 54,
            "name": "4",
            "building": {
                "pk": 9,
                "name": "체육관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "244PPR270",
        "trash_type": "CAN",
        "amount": 0.22552910605601983,
        "status": "SAF",
        "location_x": 20.0,
        "location_y": 386.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 271,
        "floor": {
            "pk": 55,
            "name": "B1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B1GER271",
        "trash_type": "CAN",
        "amount": 0.8228934859647922,
        "status": "WAR",
        "location_x": 276.0,
        "location_y": 219.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 272,
        "floor": {
            "pk": 55,
            "name": "B1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B1PET272",
        "trash_type": "PPR",
        "amount": 0.2685519750130414,
        "status": "SAF",
        "location_x": 217.0,
        "location_y": 382.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 273,
        "floor": {
            "pk": 55,
            "name": "B1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B1CAN273",
        "trash_type": "GLA",
        "amount": 0.04463801797566891,
        "status": "SAF",
        "location_x": 241.0,
        "location_y": 106.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 274,
        "floor": {
            "pk": 55,
            "name": "B1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B1GLA274",
        "trash_type": "GLA",
        "amount": 0.6564077711404285,
        "status": "CAU",
        "location_x": 110.0,
        "location_y": 108.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 275,
        "floor": {
            "pk": 55,
            "name": "B1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B1PPR275",
        "trash_type": "GLA",
        "amount": 0.052094851801348985,
        "status": "SAF",
        "location_x": 598.0,
        "location_y": 238.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 276,
        "floor": {
            "pk": 56,
            "name": "B2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B2GER276",
        "trash_type": "GER",
        "amount": 0.27966495446201245,
        "status": "SAF",
        "location_x": 249.0,
        "location_y": 13.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 277,
        "floor": {
            "pk": 56,
            "name": "B2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B2PET277",
        "trash_type": "CAN",
        "amount": 0.8203106908170021,
        "status": "WAR",
        "location_x": 338.0,
        "location_y": 355.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 278,
        "floor": {
            "pk": 56,
            "name": "B2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B2CAN278",
        "trash_type": "PET",
        "amount": 0.6974975557213534,
        "status": "CAU",
        "location_x": 384.0,
        "location_y": 335.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 279,
        "floor": {
            "pk": 56,
            "name": "B2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B2GLA279",
        "trash_type": "PPR",
        "amount": 0.7632416470142995,
        "status": "WAR",
        "location_x": 623.0,
        "location_y": 203.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 280,
        "floor": {
            "pk": 56,
            "name": "B2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "25B2PPR280",
        "trash_type": "PPR",
        "amount": 0.9818702427854343,
        "status": "WAR",
        "location_x": 57.0,
        "location_y": 230.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 281,
        "floor": {
            "pk": 57,
            "name": "1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "251GER281",
        "trash_type": "PET",
        "amount": 0.988235565263353,
        "status": "WAR",
        "location_x": 550.0,
        "location_y": 296.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 282,
        "floor": {
            "pk": 57,
            "name": "1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "251PET282",
        "trash_type": "CAN",
        "amount": 0.6872300026986371,
        "status": "CAU",
        "location_x": 452.0,
        "location_y": 157.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 283,
        "floor": {
            "pk": 57,
            "name": "1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "251CAN283",
        "trash_type": "PPR",
        "amount": 0.684718434331732,
        "status": "CAU",
        "location_x": 149.0,
        "location_y": 25.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 284,
        "floor": {
            "pk": 57,
            "name": "1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "251GLA284",
        "trash_type": "GER",
        "amount": 0.649078288488395,
        "status": "CAU",
        "location_x": 583.0,
        "location_y": 21.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 285,
        "floor": {
            "pk": 57,
            "name": "1",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "251PPR285",
        "trash_type": "PET",
        "amount": 0.14739004547456092,
        "status": "SAF",
        "location_x": 417.0,
        "location_y": 335.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 286,
        "floor": {
            "pk": 58,
            "name": "2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "252GER286",
        "trash_type": "PPR",
        "amount": 0.6001633565865689,
        "status": "CAU",
        "location_x": 74.0,
        "location_y": 255.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 287,
        "floor": {
            "pk": 58,
            "name": "2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "252PET287",
        "trash_type": "PPR",
        "amount": 0.5321273130422322,
        "status": "CAU",
        "location_x": 417.0,
        "location_y": 228.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 288,
        "floor": {
            "pk": 58,
            "name": "2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "252CAN288",
        "trash_type": "GLA",
        "amount": 0.9084724431002464,
        "status": "WAR",
        "location_x": 439.0,
        "location_y": 166.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 289,
        "floor": {
            "pk": 58,
            "name": "2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "252GLA289",
        "trash_type": "PPR",
        "amount": 0.12458489001022166,
        "status": "SAF",
        "location_x": 490.0,
        "location_y": 351.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 290,
        "floor": {
            "pk": 58,
            "name": "2",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "252PPR290",
        "trash_type": "GER",
        "amount": 0.8378518513878365,
        "status": "WAR",
        "location_x": 196.0,
        "location_y": 128.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 291,
        "floor": {
            "pk": 59,
            "name": "3",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "253GER291",
        "trash_type": "GLA",
        "amount": 0.5117547563247652,
        "status": "CAU",
        "location_x": 152.0,
        "location_y": 84.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 292,
        "floor": {
            "pk": 59,
            "name": "3",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "253PET292",
        "trash_type": "PET",
        "amount": 0.1472539238764532,
        "status": "SAF",
        "location_x": 173.0,
        "location_y": 4.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 293,
        "floor": {
            "pk": 59,
            "name": "3",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "253CAN293",
        "trash_type": "CAN",
        "amount": 0.6519915979903983,
        "status": "CAU",
        "location_x": 370.0,
        "location_y": 79.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 294,
        "floor": {
            "pk": 59,
            "name": "3",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "253GLA294",
        "trash_type": "CAN",
        "amount": 0.16270662001285663,
        "status": "SAF",
        "location_x": 95.0,
        "location_y": 288.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 295,
        "floor": {
            "pk": 59,
            "name": "3",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "253PPR295",
        "trash_type": "CAN",
        "amount": 0.4352079860552719,
        "status": "CAU",
        "location_x": 213.0,
        "location_y": 249.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 296,
        "floor": {
            "pk": 60,
            "name": "4",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "254GER296",
        "trash_type": "CAN",
        "amount": 0.2210154311644349,
        "status": "SAF",
        "location_x": 537.0,
        "location_y": 417.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 297,
        "floor": {
            "pk": 60,
            "name": "4",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "254PET297",
        "trash_type": "PET",
        "amount": 0.3479926109396916,
        "status": "SAF",
        "location_x": 0.0,
        "location_y": 29.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 298,
        "floor": {
            "pk": 60,
            "name": "4",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "254CAN298",
        "trash_type": "GLA",
        "amount": 0.7317915930074,
        "status": "WAR",
        "location_x": 47.0,
        "location_y": 36.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 299,
        "floor": {
            "pk": 60,
            "name": "4",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "254GLA299",
        "trash_type": "PET",
        "amount": 0.6168633782805887,
        "status": "CAU",
        "location_x": 192.0,
        "location_y": 95.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
        "discard_users": []
    },
    {
        "id": 300,
        "floor": {
            "pk": 60,
            "name": "4",
            "building": {
                "pk": 10,
                "name": "중앙도서관",
                "campus": {
                    "pk": 2,
                    "name": "연세대학교"
                }
            }
        },
        "token": "254PPR300",
        "trash_type": "GLA",
        "amount": 0.9052652522510614,
        "status": "WAR",
        "location_x": 286.0,
        "location_y": 26.0,
        "created_at": "2022-08-08T12:26:16.895703+09:00",
        "updated_at": "2022-08-08T12:26:16.895703+09:00",
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
        day = '2022/0' + str(i) + dd


        cnt = 0
        data = ''
        while cnt < 1000:
            idx = random.randrange(300)
            target = trash_list[idx]
            
            sec = str(random.randint(0, 59))
            min = str(random.randint(0, 59))
            hr = str(random.randint(0, 23))
            
            sec = '0'*(2-len(sec)) + sec
            min = '0'*(2-len(min)) + min
            hr = '0'*(2-len(hr)) + hr
            
            time = hr + ':' + min + ':' + sec

            rand_rfid = str(random.randint(1, 4999))
            rand_zero = '0' * (10-len(rand_rfid))
            sen = f'{day} {time} {target["floor"]["building"]["campus"]["name"]} {target["floor"]["building"]["name"]} {target["floor"]["name"]} {target["token"]} {target["trash_type"]} {rand_zero+rand_rfid} {target["amount"]}'
            data += sen
            data += '\n'
            target["amount"] = random.random()
            cnt += 1

        f = open(f'20220{str(i)+dd}', 'w', encoding='UTF-8')
        f.write(data)
        f.close()