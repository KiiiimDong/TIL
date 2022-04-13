# 크롤링 요악정리.
1. 기본셋팅
    -import requests 로 받는거.
    -import sqlite3 : sql 사용
    -from bs4 import Beautiful soup, soup = -Beautifulsoup(html_d,'html.parser) : 다루기 쉽게 담아줌.
    -r=requests.get(url)
2. ```python
     def f(n,x):
        for i in range(x):
            n=n.next_sibling
        return n.text.strip()
        ```
    다음것을 받아주는 메소드    
3. 저장(db)
    ```python
        conn=sqlite3.connect(db)
        c=conn.cursor()
        c.execute()
        c.executemany()
        conn.commit()
        conn.close()
    ```
4. 출력(db):
    ```python
        for i in c.fetchall:
            print(i)