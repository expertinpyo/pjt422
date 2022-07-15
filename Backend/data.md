# 데이터베이스 공부 - 성능 최적화
## 
추천 링크 
https://sparkdia.tistory.com/19 - RDBMS 성능 최적화
http://blog.skby.net/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%ED%8A%9C%EB%8B%9D-db-tuning/ - 데이터베이스 튜닝 기법
https://dataonair.or.kr/db-tech-reference/d-guide/dbms-2/?mod=document&uid=62471 - databible

https://cocoon1787.tistory.com/778 - 데이터 무결성 관련 => 추후 외래키 설정 여부를 판단해보자

RDBMS의 성능이 좋다의 기준
=> 얼마나 많은 사용자가 얼마나 빨리 데이터를 처리할 수 있느냐

단순 쿼리 실행 속도의 빠름을 의미하는 것이 아닌
  "쿼리 실행 시 내부적으로 얼마나 많은 블럭을 I/O 했는지"가 중요

