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
*	스토리텔링   
-어디서든 사용할 수 있는 것이 장점   
-부모님들도 편하게 사용할 수 있도록 구성   
-단체 사진을 찍을 수 있고, 핸드폰 분실의 위험이 없음   
-개발 시 테스트하기 편함

*	구현 목록
1.	서보모터 이용하여 각도 조절
2.	추천 포즈
3.	수동 필터 기능과 자동 필터 기능으로 나누어서 이용할 수 있도록 구현. 자동 필터 기능을 이용한다면 조도 센서 이용할 수 있도록 하여 주변 밝기 등을 고려하여 자동으로 필터가 제공되고, 수동 필터를 이용한다면 자신이 원하는 대로 필터를 선택할 수 있도록 함
4.	시간, 환경(밤, 역광 등), 연령대 별로 잘 찍을 수 있도록 하는 가이드라인 제공
5.	수동 필터 기능과 자동 필터 가능
6.	인원수 별로 랜덤 포즈 추천
7.	커뮤니티를 만들어서 포토 스팟 알려주도록 구현(추가 기능으로 구현)
8.	예시 사진을 게재 후 해당 사진을 누르면 같은 설정으로 사진을 찍을 수 있도록 구현
9.	타이머 구현

*	세부 사항
1.	모바일 웹 이용(접근성이 좋은 것은 모바일이지만 웹으로 구현)
2.	sw를 우선으로 하지만 3d 프린터로 외관 구현할 수 있도록 함
3.	날씨 데이터 가져와서 연동
4.	휴대용(캐리어 또는 삼각대로 휴대 가능하도록 함)
5.	거치용   
-예약제   
-횟수 제한이 아니라 시간 제한 방식 사용   
-결제 시스템 도입(촬영된 사진 게시 시 할인)   
-짐 내려놓는 곳 제공   
-전체 전송(qr, 링크 등을 이용하여 웹에 올려서 다운로드 받을 수 있도록 하는 형식) 및 선택하여 프린트(추가)   
-회원가입 기능을 만들지 않고 일회용 비밀번호 사용할 수 있도록 구현   
*	추가 기능   
-지도(촬영 위치 수집 및 동의)   
-폴라로이드 출력(실제 폴라로이드와 연동)   
-결제시스템   
-커뮤니티
*	유지보수 측면   
-비올 때   
-관리 시스템
