# 웹/모바일(웹 IoT) 스켈레톤 프로젝트

<!-- 필수 항목 -->

## 카테고리

| Application | Domain | Language | Framework |
| ---- | ---- | ---- | ---- |
| :white_check_mark: Desktop Web | :black_square_button: AI | :white_check_mark: JavaScript | :white_check_mark: Vue.js |
| :black_square_button: Mobile Web | :black_square_button: Big Data | :black_square_button: TypeScript | :black_square_button: React |
| :white_check_mark: Responsive Web | :black_square_button: Blockchain | :black_square_button: C/C++ | :black_square_button: Angular |
| :black_square_button: Android App | :white_check_mark: IoT | :black_square_button: C# | :black_square_button: Node.js |
| :black_square_button: iOS App | :black_square_button: AR/VR/Metaverse | :white_check_mark: ​Python | :white_check_mark: Flask/Django |
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

# 쓰레기통 관리 시스템

##	스토리텔링   
__*배경*__
- 사람들이 무분별하게 쓰레기를 버림
- 음식물이 묻어서 재활용하기 어려움
<br/>

__*아이디어*__
1. HW
	* 초음파 센서
		- 쓰레기통이 얼마나 찼는지 쓰레기통 외부의 LED로 사용자가 확인
		- 관리자가 쓰레기가 얼마나 찼는지 웹으로 확인 가능

	* NFC, RFID
		- 쓰레기를 버릴 때 사용자가 무분별하게 버리지 않도록 태그 시에만 쓰레기통이 열림
		- 관리자가 태그 시 쓰레기를 언제 비웠는지에 대한 데이터가 DB로 전송
	  -->일정 시간마다 쓰레기를 비울 수 있도록 구현

	* HW 추가 사항
		- 채로 음료 안의 알갱이 같은 것은 걸러지도록 하고, 나머지는 필터를 달아서 자연에 방류
		- 컵 내의 내용물을 씻을 수 있는 곳
		- 거울, 태그를 할 때마다 사진을 찍어서 양심 자극
		- 다 찼을 때는 RFID를 찍어도 더 이상 열리지 않고 가장 가까운 쓰레기통을 알려줄 수 있도록 함

<br/>

2. Frontend(Vue.js)
	* 관리자 전용 화면
		- 층을 선택하면 해당 층의 단면도가 나오고, 쓰레기통의 위치가 표시됨
		- 지도 내부에 쓰레기통 안의 내용물 양이 색과 숫자로 표현(hover도 사용 가능)
    	- 비운지 오래된 쓰레기통은 경고 아이콘을 표시한다.

    * 사용자 전용 화면
      - 층을 선택하면 해당 층의 단면도가 나오고, 쓰레기통의 위치가 표시됨
      - 쓰레기통 사용 가능 여부 확인

    * Frontend 추가 사항
      - 마지막으로 비워 둔 시간, 시간 별, 장소 별 통계를 내서 어느 곳에서 어느 시간에 쓰레기가 많이 찰지 예측
<br/>

3. Backend(Python DJango, Maria DB)
	* 구성요소
	  - 각 쓰레기통 위치, 종류, 이벤트, 각 층/분류 등등
<br/>

##	구현 목록


##	세부 사항


##	추가 기능   


##	유지보수 측면   
