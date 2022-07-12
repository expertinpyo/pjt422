# 공통-Sub PJT 1

# 웹/모바일(웹 IoT) 스켈레톤 프로젝트

<!-- 필수 항목 -->

## 카테고리

| Application | Domain | Language | Framework |
| ---- | ---- | ---- | ---- |
| :white_check_mark: Desktop Web | :black_square_button: AI | :white_check_mark: JavaScript | :black_square_button: Vue.js |
| :black_square_button: Mobile Web | :black_square_button: Big Data | :black_square_button: TypeScript | :white_check_mark: React |
| :white_check_mark: Responsive Web | :black_square_button: Blockchain | :black_square_button: C/C++ | :black_square_button: Angular |
| :black_square_button: Android App | :white_check_mark: IoT | :black_square_button: C# | :white_check_mark: Node.js |
| :black_square_button: iOS App | :black_square_button: AR/VR/Metaverse | :black_square_button: ​Python | :black_square_button: Flask/Django |
| :black_square_button: Desktop App | :black_square_button: Game | :black_square_button: Java | :black_square_button: Spring/Springboot |
| | | :black_square_button: Kotlin | |

<!-- 필수 항목 -->

## 프로젝트 소개

* 프로젝트명: 임베디드 KIT 연동 웹 서비스
* 서비스 특징: 웹/모바일(웹 IoT) 프로젝트를 위한 스켈레톤 프로젝트
* 주요 기능
  - 회원 관리
  - 카테고리 관리
  - 투표 관리(키오스크 포함)
* 주요 기술
  - Single Page Application
  - Raspberry Pi
  - REST API
* 참조 리소스
  * Material-UI: React Component Library 
* 배포 환경
  - URL: // 웹 서비스, 랜딩 페이지, 프로젝트 소개 등의 배포 URL 기입
  - 테스트 계정: // 로그인이 필요한 경우, 사용 가능한 테스트 계정(ID/PW) 기입

<!-- 자유 양식 -->

## 팀 소개
* 김ㅇㅇ: 팀장, 프론트엔드 개발
* 이ㅇㅇ: 부팀장, 기획 및 와이어프레임 작성, 프론트엔드 개발
* 박ㅇㅇ: 백엔드 개발 및 QA 담당
* 홍ㅇㅇ: 백엔드 개발, Swagger API 문서 관리
* 전ㅇㅇ: 코드 리뷰 및 인프라 담당, CI/CD, HTTPS, Docker 구성

<!-- 자유 양식 -->

## 프로젝트 상세 설명

// 개발 환경, 기술 스택, 시스템 구성도, ERD, 기능 상세 설명 등

SSAFY 인생 네컷

###	스토리텔링   

- 어디서든 사용할 수 있는 것이 장점   
- 부모님들도 편하게 사용할 수 있도록 구성   
- 단체 사진을 찍을 수 있고, 핸드폰 분실의 위험이 없음   
- 개발 시 테스트하기 편함
- 많은 비용과 긴 시간이 소요되는 스냅 촬영에 비해 접근성이 좋음
- 무거운 촬영장비를 들고 다니지 않아도 고화질의 사진을 촬영할 수 있음


###	구현 목록

1.	서보모터 이용하여 각도 조절
2.	인원수 별로 랜덤 포즈 추천
3.	수동 필터 기능과 자동 필터 기능으로 나누어서 이용할 수 있도록 구현. 자동 필터 기능을 이용한다면 조도 센서 이용할 수 있도록 하여 주변 밝기 등을 고려하여 자동으로 필터가 제공되고, 수동 필터를 이용한다면 자신이 원하는 대로 필터를 선택할 수 있도록 함
4.	시간, 환경(밤, 역광 등), 연령대 별로 잘 찍을 수 있도록 하는 가이드라인 제공
5.	타이머 구현
6.	예시 사진을 게재 후 해당 사진을 누르면 같은 설정으로 사진을 찍을 수 있도록 구현
7.	커뮤니티를 만들어서 포토 스팟 알려주도록 구현(추가 기능으로 구현)

###	세부 사항

1.	모바일 웹 이용(접근성이 좋은 것은 모바일이지만 웹으로 구현)
2.	sw를 우선으로 하지만 3d 프린터로 외관 구현할 수 있도록 함
3.	날씨 데이터 가져와서 연동
4.	휴대용(캐리어 또는 삼각대로 휴대 가능하도록 함)
5.	거치용   

6. 예약제   
7. 횟수 제한이 아니라 시간 제한 방식 사용   
8. 결제 시스템 도입(촬영된 사진 게시 시 할인)   
9. 짐 내려놓는 곳 제공   
10. 전체 전송(qr, 링크 등을 이용하여 웹에 올려서 다운로드 받을 수 있도록 하는 형식) 및 선택하여 프린트(추가)   
11. 회원가입 기능을 만들지 않고 일회용 비밀번호 사용할 수 있도록 구현   

###	추가 기능   

- 지도(촬영 위치 수집 및 동의)   
- 폴라로이드 출력(실제 폴라로이드와 연동)   
- 결제시스템   
- 커뮤니티

###	유지보수 측면   

- 비올 때   
- 관리 시스템

<주제> ~~
* 배경
- 사람들이 무분별하게 쓰레기를 버림
- 음식물이 묻어서 재활용하기 어려움
* 아이디어
  * HW
* 초음파 센서
- 쓰레기통이 얼마나 찼는지 쓰레기통 외부의 LED로 사용자가 확인
- 관리자가 쓰레기가 얼마나 찼는지 웹으로 확인 가능
* NFC, RFID
- 쓰레기를 버릴 때 사용자가 무분별하게 버리지 않도록 태그 시에만 쓰레기통이 열림
- 관리자가 태그 시 쓰레기를 언제 비웠는지에 대한 데이터가 DB로 전송-
 ->일정 시간마다 쓰레기를 비울 수 있도록 구현
* HW 추가 사항
- 채로 음료 안의 알갱이 같은 것은 걸러지도록 하고, 나머지는 필터를 달아서 자연에 방류
- 컵 내의 내용물을 씻을 수 있는 곳
- 거울, 태그를 할 때마다 사진을 찍어서 양심 자극
- 다 찼을 때는 RFID를 찍어도 더 이상 열리지 않고 가장 가까운 쓰레기통을 알려줄 수 있도록 함
* Frontend(Vue.js)
  * 관리자 전용 화면
    - 층을 선택하면 해당 층의 단면도가 나오고, 쓰레기통의 위치가 표시됨
- 지도 내부에 쓰레기통 안의 내용물 양이 색과 숫자로 표현(hover도 사용 가능)
  * 사용자 전용 화면
    - 층을 선택하면 해당 층의 단면도가 나오고, 쓰레기통의 위치가 표시됨
- 쓰레기통 사용 가능 여부 확인
    * Frontend 추가 사항
      - 마지막으로 비워 둔 시간, 시간 별, 장소 별 통계를 내서 어느 곳에서 어느 시간에 쓰레기가 많이 찰지 예측
* Backend(Python DJango, Maria DB)
  * 구성요소
    - 각 쓰레기통 위치, 종류, 이벤트, 각 층/분류 등등


