# 1.고양이와 개는 몇 마리 있을까

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

동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ---- | --------------- |
| A373219   | Cat         | 2014-07-29 11:43:00 | Normal           | Ella | Spayed Female   |
| A377750   | Dog         | 2017-10-25 17:17:00 | Normal           | Lucy | Spayed Female   |
| A354540   | Cat         | 2014-12-11 11:48:00 | Normal           | Tux  | Neutered Male   |

고양이는 2마리, 개는 1마리 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_TYPE | count |
| ----------- | ----- |
| Cat         | 2     |
| Dog         | 1     |





## sol)

------

- 조회 : SELECT 를 활용합니다.
- 수량 세기 : COUNT 를 활용합니다.
- 그룹으로 묶기 : GROUP BY 를 활용합니다.

------

**ANIMAL_TYPE이 같은 것들끼리 GROUP으로 묶어서 조회**하기 위해, GROUP BY를 사용합니다.

ANIMAL_TYPE을 GROUP BY절에 적용하면, **ANIMAL_TYPE 이 같은 것들을 그룹화할 것입니다.**

이에 대하여 COUNT(ANIMAL_TYPE)을 한다면, 그룹화된 것들 각각의 갯수를 구할 수 있게 됩니다.

```mysql
SELECT ANIMAL_TYPE ,COUNT(*)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

- (20.9.25 수정) 추가된 조건으로 cat이 dog보다 앞에 나오도록 해야 합니다. 따라서, 맨 끝에 `ORDER BY ANIMAL_TYPE`을 추가하면 정답으로 처리됩니다.



\* GROUP BY

해당 컬럼을 기준으로 GROUP화 함

 

\* COUNT()

해당 컬럼의 개수를 조회

 

-> **ANIMAL_TYPE이 같은 것들끼리 GROUP으로 묶고 COUNT로 개수 조회**



----

---



# 2.동명 동물 수 찾기

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

동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME   | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | ------ | --------------- |
| A396810   | Dog         | 2016-08-22 16:13:00 | Injured          | Raven  | Spayed Female   |
| A377750   | Dog         | 2017-10-25 17:17:00 | Normal           | Lucy   | Spayed Female   |
| A355688   | Dog         | 2014-01-26 13:48:00 | Normal           | Shadow | Neutered Male   |
| A399421   | Dog         | 2015-08-25 14:08:00 | Normal           | Lucy   | Spayed Female   |
| A400680   | Dog         | 2017-06-17 13:29:00 | Normal           | Lucy   | Spayed Female   |
| A410668   | Cat         | 2015-11-19 13:41:00 | Normal           | Raven  | Spayed Female   |

- Raven 이름은 2번 쓰였습니다.
- Lucy 이름은 3번 쓰였습니다
- Shadow 이름은 1번 쓰였습니다.

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| NAME  | COUNT |
| ----- | ----- |
| Lucy  | 3     |
| Raven | 2     |

##  sol)

- 동물의 이름 갯수를 조회하는 것이므로, NAME에 **COUNT 함수를** 적용할 것입니다.
- **NULL 값이 아닌 것을 비교하는 방법**은 **IS NOT NULL** 을 붙입니다.
- NAME을 **그룹화**하여, 그것의 갯수를 셀 것이므로 **GROUP BY** 를 활용합니다.
- **HAVING 은 GROUP 화 한 이후에 적용**되는 것으로, 그룹화되어 나온 결과에 **조건식**을 적용합니다.

```mysql
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS WHERE NAME is NOT NULL GROUP BY NAME HAVING COUNT(NAME) >= 2 
```

------

**[GROUP BY, HAVING 설명]**

우선, **쿼리문의 실행 순서**에 대해 알 필요가 있습니다.

**SELECT -** 5순위 (필수)

**FROM -** 1순위 (필수)

**WHERE -** 2순위

**GROUP BY -** 3순위

**HAVING -** 4순위

**ORDER BY -** 6순위

------

즉, 조회 대상 테이블을 가장 먼저 정하고, 그것을 토대로 데이터를 조회합니다.

부가적인 조건을 거는 WHERE, GROUP BY, HAVING, ORDER BY들도 각각의 순서가 있습니다.

이 때, **HAVING 은 GROUP BY가 적용된 이후에 실행**됨을 알 수 있습니다.

**ORDER BY**는 모든 데이터들을 조회가 완료된 다음, 최후에 정렬함을 알 수 있습니다.





*COUNT()

행의 개수 조회 

- COUNT(*) : NULL 을 포함한 모든 행 개수 조회
- COUNT(컬럼명) : NULL을 제외한 행 개수 조회

 

\* HAVING 절

GROUP BY 절에 의해 생성된 결과 값 중 원하는 조건에 부합하는 자료만 보고자 할 때 사용

GROUP BY 의 WHERE 절과 같음

 

--> NAME별로 GROUP BY 한 후 COUNT

HAVING 절로 COUNT가 2이상인 값만 조회





----

----

# 3.입양시각 구하기

**문제 설명**

ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

NAMETYPENULLABLE

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

예시

SQL문을 실행하면 다음과 같이 나와야 합니다.

| HOUR | COUNT |
| ---- | ----- |
| 9    | 1     |
| 10   | 2     |
| 11   | 13    |
| 12   | 10    |
| 13   | 14    |
| 14   | 9     |
| 15   | 7     |
| 16   | 10    |
| 17   | 12    |
| 18   | 16    |
| 19   | 2     |

##  sol1)

------

- 조회 : SELECT 를 활용합니다.
- 수량 세기 : COUNT 를 활용합니다.
- 그룹으로 묶기 : GROUP BY 를 활용합니다.
- 시간 추출 : HOUR 을 활용합니다.

------

- **TYPE이 DATETIME 인 데이터에서 시간만 추출하려면 HOUR을 사용합니다.**

```mysql
SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT FROM ANIMAL_OUTS GROUP BY HOUR(DATETIME) HAVING HOUR >= 9 and HOUR <= 19 
```

SELECT 문의 **HOUR(DATETIME) HOUR** 은, 조회 결과 나온 **열의 이름을 HOUR로 설정하겠다는 뜻**입니다.

- HAVING을 사용하지 않고, 아래와 같이 **WHERE**를 이용할 수도 있습니다.

```mysql
SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT FROM ANIMAL_OUTS WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19 GROUP BY HOUR(DATETIME) 
```

- **시간 순으로 정렬**하려면 맨 끝에 `ORDER BY HOUR` 를 입력해야 합니다.

##  sol2)

```mysql
SELECT HOUR(DATETIME), COUNT(DATETIME)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME);
```

\* HOUR()

TYPE이 DATETIME 인 데이터에서 시간만 추출하려면 HOUR을 사용

DATETIME 자료형은 (year, month, day, hour, minute, second)로 이뤄짐

 

\* BETWEEN 

컬럼명 BETWEEN 시작값 AND 종료값 

- empno BETWEEN 7000 AND 7600 : empno이 7000에서 7600까지인 행만 조회
- AGE BETWEEN 30 AND 40 : 나이가 30에서 40까지인 행만 조회



----

----



# 4.입양시각 구하기

**문제 설명**

ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

예시

SQL문을 실행하면 다음과 같이 나와야 합니다.

| HOUR | COUNT |
| ---- | ----- |
| 0    | 0     |
| 1    | 0     |
| 2    | 0     |
| 3    | 0     |
| 4    | 0     |
| 5    | 0     |
| 6    | 0     |
| 7    | 3     |
| 8    | 1     |
| 9    | 1     |
| 10   | 2     |
| 11   | 13    |
| 12   | 10    |
| 13   | 14    |
| 14   | 9     |
| 15   | 7     |
| 16   | 10    |
| 17   | 12    |
| 18   | 16    |
| 19   | 2     |
| 20   | 0     |
| 21   | 0     |
| 22   | 0     |
| 23   | 0     |





## sol)

위 테이블 데이터를 토대로, **입양 시간대별로 입양이 몇 건이나 발생했는지 조회**해야 합니다.

- **(1) 과 다른 점이라면, 모든 시간대(0시~23시)를 조회해야 합니다.**
- 갑자기 난이도가 상승한 레벨 4의 문제로, **쿼리문에서 로컬 변수를 활용하는 문제**입니다.

------

```mysql
SET @hour := -1; -- 변수 선언 
SELECT (@hour := @hour + 1) as HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT 
FROM ANIMAL_OUTS 
WHERE @hour < 23 
```

------

- SET 옆에 변수명과 초기값을 설정

  할 수 있습니다.

  - @가 붙은 변수는 프로시저가 종료되어도 **유지**된다고 생각하면 됩니다.
  - 이를 통해 값을 누적하여 0부터 23까지 표현할 수 있습니다.

- @hour은 초기값을 -1로 설정합니다. PL/-SQL 문법에서 **:=**은 비교 연산자 =과 혼동을 피하기 위한의 **대입 연산**입니다.

- SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행하게 됩니다.

- 이 때

   

  처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0

  이 저장됩니다.

  - HOUR 값이 0부터 시작할 수 있습니다.
  - WHERE @hour < 23일 때까지, @hour 값이 **계속 + 1씩 증가**합니다.



----

\* SET

어떤 변수에 특정 값을 할당하는 것 (변수 선언)

- [SET @var = 5;]   [SET @var := 5;]   [SELECT @var := 5]
- 위 세가지 표현으로 가능
- '=' : MySQL에서 대입연산자, 비교연산자 2가지로 사용 됨 (SET 명령어에서만 대입 연산자로 인식)
- ':=' : MySQL에서 대입 연산자로만 사용 됨 
- 변수 사용 시 명시적으로 대입 연산자의 의미만을 갖는 ':=' 의 사용을 권장

---> hour 변수를 -1로 선언해 22까지 +1씩 증가 시킴 (따라서 hour은 0부터 23까지 생성됨)

DATETIME의 hour과 hour변수의 값이 동일할 때의 행 카운트