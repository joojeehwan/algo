# 1. 모든 레코드 조회하기



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

 

**출력**

ANIMAL_IDANIMAL_TYPEDATETIMEINTAKE_CONDITIONNAMESEX_UPON_INTAKE

| A349996 | Cat  | 2018-01-22 14:32:00 | Normal | Sugar  | Neutered Male |
| ------- | ---- | ------------------- | ------ | ------ | ------------- |
| A350276 | Cat  | 2017-08-13 13:50:00 | Normal | Jewel  | Spayed Female |
| A350375 | Cat  | 2017-03-06 15:01:00 | Normal | Meo    | Neutered Male |
| A352555 | Dog  | 2014-08-08 04:20:00 | Normal | Harley | Spayed Female |

..이하 생략

## sol)

**동물 보호소에 들어온 모든 정보**를 **ANIMAL_ID 순으로**(오름차순) 조회하는 SQL문을 작성해야 합니다.

조회되는 정보들은 모든 column을 포함해야 합니다.

------

조회 : SELECT 문을 활용합니다.

------

모든 열을 조회하므로 * 를 사용하여, 각 테이블의 값들을 SELECT 문으로 검색할 수 있습니다.

그리고 **order by** 를 사용하여, 정렬 기준이 될 컬럼을 지정합니다.

```mysql
SELECT *
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;
```

만일, ANIMAL_ID의 역순으로 정렬하고 싶을 경우에는

```mysql
SELECT * FROM ANIMAL_INS order by ANIMAL_ID desc; 
```

끝에 **desc**라고 붙입니다. (붙이지 않으면 asc, 즉 오름차순이 기본입니다.)



## 오라클 풀이

* 동물의 정보를 담은 테이블의 모든 레코드를 ANIMAL_ID순으로 조회하는 SQL문입니다. 
* SELECT * 으로 모든 칼럼을 선택하며, ORDER BY ANIMAL_ID로 레코드를 ANIMAL_ID순으로 정렬합니다.

```sql
SELECT * 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



-----

-----

# 2. 역순 정렬하기

**문제 설명**

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.

| NAME   | DATETIME            |
| ------ | ------------------- |
| Rocky  | 2016-06-07 09:17:00 |
| Shelly | 2015-01-29 15:01:00 |
| Benji  | 2016-04-19 13:28:00 |
| Jackie | 2016-01-03 16:25:00 |
| *Sam   | 2016-03-13 11:17:00 |

..이하 생략

## sol)

위와 같은 테이블 데이터로 **NAME과 DATETIME만**을 조회하는데, 정렬 결과는 ANIMAL_ID의 역순으로 조회되어야 합니다.

- 조회하는 열 : NAME, DATETIME
- 정렬 기준이 되는 열 : ANIMAL_ID
- 정렬은 내림차순

```mysql
SELECT NAME, DATETIME FROM ANIMAL_INS order by ANIMAL_ID desc;
```



## 오라클 풀이

* 동물의 정보를 담은 테이블에서 모든 동물의 이름과 보호 시작일을 조회하되, ANIMAL_ID의 역순으로 출력합니다. 
* SELECT로 이름, 보호 시작일을 선택하고 ORDER BY를 사용하여 정렬하되, DESC(Descending, 내림차순을 의미)으로 내림차순 정렬합니다.



````sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
````



----

-----

# 3.아픈  동물 찾기

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

 

동물 보호소에 들어온 동물 중 아픈 동물[1](https://programmers.co.kr/learn/courses/30/lessons/59036#fn1)의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | -------- | --------------- |
| A365172   | Dog         | 2014-08-26 12:53:00 | Normal           | Diablo   | Neutered Male   |
| A367012   | Dog         | 2015-09-16 09:06:00 | Sick             | Miller   | Neutered Male   |
| A365302   | Dog         | 2017-01-08 16:34:00 | Aged             | Minnie   | Spayed Female   |
| A381217   | Dog         | 2017-07-08 09:41:00 | Sick             | Cherokee | Neutered Male   |

이 중 아픈 동물은 Miller와 Cherokee입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME     |
| --------- | -------- |
| A367012   | Miller   |
| A381217   | Cherokee |



## sol) 

위 정보들에서 아픈 동물(INTAKE_CONDITION=’Sick’)의 아이디와 이름을, 아이디 순으로 조회하는 SQL문을 작성해야 합니다.

------

- 조회 : SELECT 를 활용합니다.
- 조건 : WHERE 절을 활용합니다.
- 정렬 : order by 를 활용합니다.

------

조회할 열은 ANIMAL_ID 와 NAME이고, 그 데이터 중 INTAKE_CONDITION이 Sick 인 row만 출력해야 합니다. 그리고 **order by** 를 사용하여, 정렬 기준이 될 컬럼을 지정합니다.

````mysql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = "Sick" order by ANIMAL_ID
````



## 오라클 풀이

* 아픈 동물은 INTAKE_CONDITION이 Sick인 경우를 의미합니다. 
* SELECT로 동물의 아이디와 이름을 선택하고, WHERE절로 아픈 동물만 추출하여 출력되는 행을 제한합니다. 
* 오라클에서 동일한 값을 찾는 비교연산자는 =입니다.



```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID;
```



----

---



# 4.동물의 아이디와 이름

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

동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ANIMAL_ID | NAME         |
| --------- | ------------ |
| A349996   | Sugar        |
| A350276   | Jewel        |
| A350375   | Meo          |
| A352555   | Harley       |
| A352713   | Gia          |
| A352872   | Peanutbutter |
| A353259   | Bj           |

((이하 생략))

##  sol)

````mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
````



## 오라클 풀이



```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



----

-----



# 5.여러기준으로 정렬하기

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

동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.

예시

예를 들어, ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME  | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ----- | --------------- |
| A349996   | Cat         | 2018-01-22 14:32:00 | Normal           | Sugar | Neutered Male   |
| A350276   | Cat         | 2017-08-13 13:50:00 | Normal           | Jewel | Spayed Female   |
| A396810   | Dog         | 2016-08-22 16:13:00 | Injured          | Raven | Spayed Female   |
| A410668   | Cat         | 2015-11-19 13:41:00 | Normal           | Raven | Spayed Female   |

1. 이름을 사전 순으로 정렬하면 다음과 같으며, 'Jewel', 'Raven', 'Sugar'
2. 'Raven'이라는 이름을 가진 개와 고양이가 있으므로, 이 중에서는 보호를 나중에 시작한 고양이를 먼저 조회합니다.

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME  | DATETIME            |
| --------- | ----- | ------------------- |
| A350276   | Jewel | 2017-08-13 13:50:00 |
| A396810   | Raven | 2016-08-22 16:13:00 |
| A410668   | Raven | 2015-11-19 13:41:00 |
| A349996   | Sugar | 2018-01-22 14:32:00 |



## sol)

위 테이블 데이터들에서, 모든 동물의 아이디 / 이름 / 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해야 합니다.

**단, 1. 이름이 같은 동물이 있다면 2. 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.**

이 조건으로부터 order by 절에 들어갈 열 조건이 2개임을 알 수 있습니다.

------

- 조회 : SELECT 를 활용합니다.
- 정렬 : order by 를 활용합니다. order by 절에 쓰인 column 명 순서대로 정렬을 진행합니다. **이 때, 정렬 기준이 되는 열을 여러 개 지정하려면 ,로 연결하여 작성하면 됩니다.**
- 예를 들어 **order by NAME, DATETIME desc** 이라고 쓰면, name의 오름차순 순서대로 정렬하고, name이 동일할 경우 DATETIME의 내림차순 순서대로 정렬하게 됩니다.

------

```mysql
SELECT ANIMAL_ID, NAME, DATETIME from ANIMAL_INS order by NAME asc, DATETIME desc 
```

- NAME 에 붙인 asc는 없어도 상관없지만, DATETIME을 내림차순 정렬하기 위해 붙인 desc와 구분이 더욱 잘 되도록 작성한 것입니다.



## 오라클 풀이

* SELECT로 출력할 칼럼인 아이디, 이름, 보호 시작일을 선택합니다. 
* ORDER BY를 사용하여 이름 순으로 정렬하되 이름이 같다면 보호를 나중에 시작한 동물을 먼저, 즉 내림차순 정렬해야 합니다. 
* 이름은 디폴트 설정값인 오름차순으로 정렬할 것이므로 NAME만 써주고, 보호 시작일은 뒤에 DESC를 써서 내림차순 정렬임을 명시해줍니다. 
* DESC는 바로 앞 칼럼인 보호 시작일에만 적용됩니다. 

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```



----

-----



# 6.상위 n개 레코드

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

동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | -------- | --------------- |
| A399552   | Dog         | 2013-10-14 15:38:00 | Normal           | Jack     | Neutered Male   |
| A379998   | Dog         | 2013-10-23 11:42:00 | Normal           | Disciple | Intact Male     |
| A370852   | Dog         | 2013-11-03 15:04:00 | Normal           | Katie    | Spayed Female   |
| A403564   | Dog         | 2013-11-18 17:03:00 | Normal           | Anna     | Spayed Female   |

이 중 가장 보호소에 먼저 들어온 동물은 Jack입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

NAME

Jack

※ 보호소에 가장 먼저 들어온 동물은 한 마리인 경우만 테스트 케이스로 주어집니다.

## sol)

- MySQL의 경우 : NAME 값을 조회하는데 **가장 맨 위 행 1개만**을 조회하기 위해 **LIMIT 구문**을 사용해야 합니다.
- LIMIT 1 : 맨 위에서부터 1개까지의 정보 조회
- LIMIT 3 : 맨 위에서부터 3개까지의 정보 조회
- LIMIT 2, 6 : 위에서 2번째부터 6번째까지의 정보 조회

```mysql
 SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1 
```



## 오라클 풀이

* 우선 서브 쿼리를 사용하여 보호 시작일로 오름차순 정렬합니다.
*  보호 시작일로 정렬된 이름 칼럼이 저장된 서브 쿼리로부터 WHERE ROWNUM = 1을 통해 가장 먼저 들어온 동물의 이름이 있는 첫번째 행만 출력하게 됩니다.

````sql
SELECT NAME
FROM (SELECT NAME
     FROM ANIMAL_INS
     ORDER BY DATETIME)
WHERE ROWNUM = 1;
````



----

-----

----

# 참고

1. https://chanhuiseok.github.io/posts/db-3/
2. https://jione-e.tistory.com/62?category=962393