# 1.최댓값 구하기

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

##  sol)

```mysql
SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS;
```

* MAX()

해당 컬럼의 최댓값을 반환

시간의 경우 최댓값은 가장 최근 시간을 반환



---

----

# 2.최솟값 구하기

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

동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | -------- | --------------- |
| A399552   | Dog         | 2013-10-14 15:38:00 | Normal           | Jack     | Neutered Male   |
| A379998   | Dog         | 2013-10-23 11:42:00 | Normal           | Disciple | Intact Male     |
| A370852   | Dog         | 2013-11-03 15:04:00 | Normal           | Katie    | Spayed Female   |
| A403564   | Dog         | 2013-11-18 17:03:00 | Normal           | Anna     | Spayed Female   |

가장 먼저 들어온 동물은 Jack이고, Jack은 2013-10-14 15:38:00에 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

시간

2013-10-14 15:38:00

##  sol)

```mysql
SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS;
```

* MIN()

해당 컬럼의 최솟값을 반환

시간의 경우 최솟값은 가장 과거의 시간을 반환



---

----

# 3.동물수 구하기

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

 

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | -------- | --------------- |
| A399552   | Dog         | 2013-10-14 15:38:00 | Normal           | Jack     | Neutered Male   |
| A379998   | Dog         | 2013-10-23 11:42:00 | Normal           | Disciple | Intact Male     |
| A370852   | Dog         | 2013-11-03 15:04:00 | Normal           | Katie    | Spayed Female   |
| A403564   | Dog         | 2013-11-18 17:03:00 | Normal           | Anna     | Spayed Female   |

 

동물 보호소에 들어온 동물은 4마리입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| count |
| ----- |
| 4     |

※ 컬럼 이름(위 예제에서는 count)은 일치하지 않아도 됩니다.



## sol)

동물이 몇 마리 들어왔는지 조회하기 위해, ANIMAL_ID 값을 기준으로 카운트를 해 보겠습니다.

- COUNT 는 SQL 문법에 존재하는 집계함수입니다.
- 함수 내에 들어간 컬럼에 존재하는 데이터의 갯수를 출력합니다.

```mysql
SELECT COUNT(ANIMAL ID) FROM ANIMAL_INS 

```



----

----



# 4.중복 제거하기

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

동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

예시

예를 들어 ANIMAL_INS 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
| --------- | ----------- | ------------------- | ---------------- | -------- | --------------- |
| A562649   | Dog         | 2014-03-20 18:06:00 | Sick             | NULL     | Spayed Female   |
| A412626   | Dog         | 2016-03-13 11:17:00 | Normal           | *Sam     | Neutered Male   |
| A563492   | Dog         | 2014-10-24 14:45:00 | Normal           | *Sam     | Neutered Male   |
| A513956   | Dog         | 2017-06-14 11:54:00 | Normal           | *Sweetie | Spayed Female   |

보호소에 들어온 동물의 이름은 NULL(없음), *Sam, *Sam, *Sweetie입니다. 이 중 NULL과 중복되는 이름을 고려하면, 보호소에 들어온 동물 이름의 수는 2입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| count |
| ----- |
| 2     |

※ 컬럼 이름(위 예제에서는 count)은 일치하지 않아도 됩니다.

## sol)

위 테이블 데이터를 토대로, 동물 보호소에 들어온 **동물의 이름이 몇 개인지 조회**하는 SQL문을 작성해야 합니다.

- 단, 동물의 이름이 중복되는 경우 하나로 칩니다.
- 동물의 이름이 NULL인 경우는 집계하지 않습니다.

------

- 동물의 이름 갯수를 조회하는 것이므로, NAME에 **COUNT 함수를** 적용할 것입니다.
- 컬럼 내 같은 데이터가 존재하면, 중복을 제거하기 위해 **DISTINCT**를 사용합니다.
- **중복 데이터를 제거하고자 하는 열은 NAME 이므로, 옆에 DISTINCT 키워드**를 붙입니다.
- **NULL 값이 아닌 것을 비교하는 방법**은 **IS NOT NULL** 을 붙입니다.

```mysql
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL
```

\*  COUNT()

해당 칼럼의 행 개수를 조회

COUNT(*) : NULL을 포함한 모든 행의 개수 조회

COUNT(컬럼명) : NULL을 제외한 행의 개수 조회



\* DISTINCT

이름 컬럼에서 중복을 제외시키기 위해서 사용

DISTINCT는 컬럼에서 중복을 제외시키는 명령어



**[DISTINCT 사용 시 주의할 점]**

- DISTINCT 키워드는 옆에 온 모든 컬럼을 고려하여 중복 제거를 진행합니다.

- 즉, **SELECT** DISTINCT COL1, COL2 …를 진행할 경우

  - **COL1과 COL2 값이 모두 동일한 row들을 1개로** 칩니다.

- 다시 말하면, DISTINCT 는 SELECT 구문에 여러 컬럼명이 올 때, 그 중 **한 개에 대해서만 적용할 수 없다는 말이 됩니다.**

  - **SELECT** (DISTINCT COL1), COL2 **FROM …**는 오류입니다.

  - COL1 의 중복된 데이터를 제거한 뒤 COL2를 가져와야 할 텐데, 이 중 어떤 COL2 값을 가져와야 하는지 알 수 없기 때문입니다.

  - | COL1 | COL2 |
    | ---- | ---- |
    | A    | 1    |
    | A    | 2    |
    | B    | 3    |
    | C    | 4    |

    위에서 COL1에 대해서만 DISTINCT를 한다고 예를 들어 보겠습니다.

    A는 중복이 제거되어 A 하나만 보여져야 할 것입니다.

    그러나, 테이블에 열은 2개가 존재합니다.

    **COL1 열 하나에 대해서 중복제거를 하면, COL2 에 있는 값인 1과 2 중 어느 것을 출력해야 하는지 모호합니다.**

    그러므로 DISTINCT 는 모든 컬럼을 고려하여 진행할 수 밖에 없습니다.

    

----

----

----

# 참고

1. https://jione-e.tistory.com/34?category=962393
2. https://chanhuiseok.github.io/categories/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4/