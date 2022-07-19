# 1.루시와 엘라찾기

**문제 설명**

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.

예시

이때 결과는 아이디 순으로 조회해주세요. 예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME  | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ----- | --------------- |
| A373219   | Cat         | 2014-07-29 11:43:00 | Normal           | Ella  | Spayed Female   |
| A377750   | Dog         | 2017-10-25 17:17:00 | Normal           | Lucy  | Spayed Female   |
| A353259   | Dog         | 2016-05-08 12:57:00 | Injured          | Bj    | Neutered Male   |
| A354540   | Cat         | 2014-12-11 11:48:00 | Normal           | Tux   | Neutered Male   |
| A354597   | Cat         | 2014-05-02 12:16:00 | Normal           | Ariel | Spayed Female   |

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME | SEX_UPON_INTAKE |
| --------- | ---- | --------------- |
| A373219   | Ella | Spayed Female   |
| A377750   | Lucy | Spayed Female   |



## sol)

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY ANIMAL_ID;
```

\* IN

WHERE 컬럼명 IN ('값', '값2')

컬럼에서 값들에 해당되는 행만 조회

값에 해당되지 않는 행을 조회하려면 NOT IN



----

-----

# 2.이름에 el이 들어가는 동물 찾기



**문제 설명**

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다. 동물 보호소에 들어온 동물 이름 중, 이름에 EL이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME         | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ------------ | --------------- |
| A355753   | Dog         | 2015-09-10 13:14:00 | Normal           | Elijah       | Neutered Male   |
| A352872   | Dog         | 2015-07-09 17:51:00 | Aged             | Peanutbutter | Neutered Male   |
| A353259   | Dog         | 2016-05-08 12:57:00 | Injured          | Bj           | Neutered Male   |
| A373219   | Cat         | 2014-07-29 11:43:00 | Normal           | Ella         | Spayed Female   |
| A382192   | Dog         | 2015-03-13 13:14:00 | Normal           | Maxwell 2    | Intact Male     |

- 이름에 'el'이 들어가는 동물은 Elijah, Ella, Maxwell 2입니다.
- 이 중, 개는 Elijah, Maxwell 2입니다.

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME      |
| --------- | --------- |
| A355753   | Elijah    |
| A382192   | Maxwell 2 |



## sol)

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%'
ORDER BY NAME;
```

 

\* AND

- A AND B : A와 B가 모두 True면 반환

\* LIKE

조회 조건 값이 명확하지 않을 때 사용 LIKE 연산자는 ‘~와 같다’라는 의미

%는 ‘모든 문자’라는 의미고, _는 ‘한 글자’라는 의미

- NAME LIKE '%원' : 이름이 원으로 끝나는 행 조회
- ID LIKE '_K_' : ID의 가운데가 K이고 3글자인 행 조회

 

\* MySQL에서는 대소문자를 구분하지 않음

때문에 '%el%'로 처리 가능 

----

---

# 3.중성화 여부 파악하기

**문제 설명**

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME      | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | --------- | --------------- |
| A355753   | Dog         | 2015-09-10 13:14:00 | Normal           | Elijah    | Neutered Male   |
| A373219   | Cat         | 2014-07-29 11:43:00 | Normal           | Ella      | Spayed Female   |
| A382192   | Dog         | 2015-03-13 13:14:00 | Normal           | Maxwell 2 | Intact Male     |

- 중성화한 동물: Elijah, Ella
- 중성화하지 않은 동물: Maxwell 2

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME      | 중성화 |
| --------- | --------- | ------ |
| A355753   | Elijah    | O      |
| A373219   | Ella      | O      |
| A382192   | Maxwell 2 | X      |

※ 컬럼 이름은 일치하지 않아도 됩니다.



## sol1)

````mysql
-- 코드를 입력하세요
-- 중성화된 동물을 SEX_UPON_INTAKE 컬럼에서 Neutered, Spayed 로 찾음
-- 동물 아이디, 이름, 중성화 여부
-- 아이디 순으로 정렬
-- 중성화가 되어 있다면 'O' 'X'로 표기
SELECT ANIMAL_ID, NAME, 
IF((SEX_UPON_INTAKE LIKE "Neutered%") OR (SEX_UPON_INTAKE LIKE "Spayed%"), "O", "X")  AS "중성화" 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;

# IF (조건문, 참일때 값, 거짓일때 값)
````



## sol2)

```mysql
SELECT ANIMAL_ID, NAME, (CASE 
                         WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
                         WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
                         ELSE 'X'
                         END) AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

\* LIKE

칼럼에서 부분적으로 일치하는 행을 찾을때 사용

 

- 컬럼명 LIKE 'A%' : A로 시작하는 행
- 컬럼명 LIKE '%A%' : A를 포함하는 행

 

\* CASE문

조건에 따라 값을 지정함

 

CASE 

  WHEN 조건 THEN '반환 값'

  WHEN 조건 THEN '반환 값'

  ELSE 'WHEN 조건에 해당 안되는 경우 반환 값'

END



---

----



# 4.오랜 기간 보호한 동물(2)

**문제 설명**

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

NAMETYPENULLABLE

| ANIMAL_ID        | VARCHAR(N) | FALSE |
| ---------------- | ---------- | ----- |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE |
| DATETIME         | DATETIME   | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME             | VARCHAR(N) | TRUE  |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE |

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

 

**출력**

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

ANIMAL_IDANIMAL_TYPEDATETIMEINTAKE_CONDITIONNAMESEX_UPON_INTAKE

| A399552 | Dog  | 2013-10-14 15:38:00 | Normal | Jack     | Neutered Male |
| ------- | ---- | ------------------- | ------ | -------- | ------------- |
| A379998 | Dog  | 2013-10-23 11:42:00 | Normal | Disciple | Intact Male   |
| A370852 | Dog  | 2013-11-03 15:04:00 | Normal | Katie    | Spayed Female |
| A403564 | Dog  | 2013-11-18 17:03:00 | Normal | Anna     | Spayed Female |

가장 늦게 들어온 동물은 Anna이고, Anna는 2013-11-18 17:03:00에 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

시간

2013-11-18 17:03:00



## sol)

```mysql
SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_INS a JOIN ANIMAL_OUTS b ON a.ANIMAL_ID = b.ANIMAL_ID
ORDER BY b.DATETIME-a.DATETIME DESC
LIMIT 2;
```

\* DATE 끼리 기본적인 연산 가능 (+,- 등)

 

\* LIMIT

LIMIT 구를 이용해 상위 N개 행만 조회

- limit 3, 7 : 위에서 3부터 7까지의 정보 추출
- limit 5 : 위에서 5개의 정보 추출

```mysql
SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_INS a JOIN ANIMAL_OUTS b ON a.ANIMAL_ID = b.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME)
LIMIT 2;
```

\* DATEDIFF

두개의 날짜값의 차이를 int로 반환하는 Mssql 내장함수

- DATEDIFF('구분자','Start_Date','End_Date')
- Start_Date와 End_Date는 차이를 구할 두개의 날짜값을 넣는곳이고 '구분자'는 어떤차이를 구할지 정해주는 부분

 

---

----

# 5.DATETIME에서 DATE로 형 변환

**문제 설명**

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜[1](https://programmers.co.kr/learn/courses/30/lessons/59414?language=oracle#fn1)를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

예시

예를 들어, ANIMAL_INS 테이블이 다음과 같다면

ANIMAL_INS

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME   | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ------ | --------------- |
| A349996   | Cat         | 2018-01-22 14:32:00 | Normal           | Sugar  | Neutered Male   |
| A350276   | Cat         | 2017-08-13 13:50:00 | Normal           | Jewel  | Spayed Female   |
| A350375   | Cat         | 2017-03-06 15:01:00 | Normal           | Meo    | Neutered Male   |
| A352555   | Dog         | 2014-08-08 04:20:00 | Normal           | Harley | Spayed Female   |
| A352713   | Cat         | 2017-04-13 16:29:00 | Normal           | Gia    | Spayed Female   |

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME   | 날짜       |
| --------- | ------ | ---------- |
| A349996   | Sugar  | 2018-01-22 |
| A350276   | Jewel  | 2017-08-13 |
| A350375   | Meo    | 2017-03-06 |
| A352555   | Harley | 2014-08-08 |
| A352713   | Gia    | 2017-04-13 |

 

## sol)

```mysql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

\* DATE_FORMAT

DATE_FORMAT(날짜 , 형식) : 날짜를 지정한 형식으로 출력

- DATE_FORMAT(날짜 , '%Y') : 4자리 년도
- DATE_FORMAT(날짜 , '%d') : 일자(2자리)



----

-----

----

# 참고

1. https://jione-e.tistory.com/76