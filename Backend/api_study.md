# api

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