## 문자열
- 이뮤터블 객체다.(수정불가)
- 새 객체 만드는 개념
- 정수도 이뮤터블.
## 문자열 슬라이싱
* s[start:end:step] (start~end-1까지)
* 생략하면 양쪽 끝으로 맞춰진다고 생각.
* s[::-1] : 뒤집기

## 함수와 메서드
- 함수 안에 메서드가 있다.
- 객체에 종속된 함수가 메서드
- .split("기준문자") 리스트로 반환.
- .find("찾는문자") 위치를 반환.없으면 -1
- .index("찾는문자") 위치를 반환.없으면 오류
- .count("개수를 셀 문자")
- .replace("기존문자","새로운문자") 치환하여 반환.=>받아줘야한다.(이뮤터블일때)
- ."삽입할 문자".join("삽입 대상 문자열") 문자열, 리스트 튜플 가능