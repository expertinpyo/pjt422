# api

0719

| url | method | 설명 |
| --- | --- | --- |
| api/v1/buildings/<int:building_pk>/ | POST, PUT, DELETE, GET | 건물 등록, 수정, 삭제, 조회 |
| api/v1/floors/ | GET | 건물의 전체 층 조회 |
| api/v1/floors/<int:floors_pk>/ | POST, DELETE, GET | 건물 층 추가, 삭제, 조회 |
| api/v1/buildings/<int:building_pk>/trashbins/ | GET | 전체 쓰레기통 정보 조회 |
| api/v1/buildings/<int:building_pk>/trashbins/<int:trashbin_pk>/ | GET | 개별 쓰레기통 정보 조회 |
| api/v1/managers/ | GET | 전체 관리자 조회 |
| api/v1/managers/<int:manager_pk>/ | PUT, POST, DELETE | 관리자 수정, 생성 삭제 |
| api/v1/students/ | GET | 사용자 전체 조회 |
| api/v1/students/<int:student_pk>/ | PUT, POST, DELETE | 사용자 수정, 생성, 삭제 |
- url 주소에 추가적으로 campus 명이 들어가야 할 것
- django 프로젝트에서 app은 campus/accounts
- 위의 api는 변경 가능성 높음(대략적)

0720

수정

| [campus] |  |  |
| --- | --- | --- |
| api/v1/<campus_name> | GET | 캠퍼스 내 모든 건물 조회 |
| api/v1/<campus_name>/all | GET | 캠퍼스 내 모든 쓰레기통 조회 |
| api/v1/<campus_name>/<building_name> | GET | 건물 내 모든 층 조회 |
| api/v1/<campus_name>/<building_name>/all | GET | 건물 내 모든 쓰레기통 조회 |
| api/v1/<campus_name>/<building_name>/<floor_name> | GET | 건물 내 층별 모든 쓰레기 통 조회 |
| api/v1/<campus_name>/<building_name>/<floor_name>/<trashbin_id> | GET | 쓰레기통 상세 조회 |
|  |  |  |
| [statistics] |  |  |
| api/v1/<campus_name>/statistics | GET | 통계 |
|  |  |  |
| [settings] |  |  |
| api/v1/<campus_name>/settings/buildings | GET | 캠퍼스 내 건물 목록 조회 |
| api/v1/<campus_name>/settings/buildings | POST | 캠퍼스 내 건물 추가 |
| api/v1/<campus_name>/settings/buildings | PUT / DELETE | 캠퍼스 내 건물 변경, 삭제 |
| api/v1/<campus_name>/settings/buildings/<int:building_id> | GET | 건물 내 모든 층 + 층별 쓰레기통 정보 조회 |
| api/v1/<campus_name>/settings/buildings/<int:building_id> | POST | 해당 건물 내 층 추가 |
| api/v1/<campus_name>/settings/buildings/<int:building_id> | PUT / DELETE | 해당 건물 내 층 변경, 삭제 |
| api/v1/<campus_name>/settings/buildings/<int:building_id>/<int:floor_id> | GET | 해당 층 내 모든 쓰레기통 정보 조회 |
| api/v1/<campus_name>/settings/buildings/<int:building_id>/<int:floor_id> | POST | 해당 층 내 쓰레기통 추가 |
| api/v1/<campus_name>/settings/buildings/<int:building_id>/<int:floor_id> | PUT / DELETE | 해당 층 내 쓰레기통 변경, 삭제 |
| api/v1/<campus_name>/settings/accounts/ | GET | 해당 캠퍼스 내 관리자 목록 조회 |
| api/v1/<campus_name>/settings/accounts/ | POST | 해당 캠퍼스 내 관리자 추가 |
| api/v1/<campus_name>/settings/accounts/ | PUT / DELETE | 해당 캠퍼스 내 관리자 변경, 삭제 |
| api/v1/<campus_name>/settings/students | GET | 해당 캠퍼스 내 학생 목록 조회 |
| api/v1/<campus_name>/settings/students | POST | 해당 캠퍼스 내 학생 추가 |
| api/v1/<campus_name>/settings/students | PUT / DELETE | 해당 캠퍼스 내 학생 변경, 삭제 |