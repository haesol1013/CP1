"""""""""
# 계절별 활동 추천 시스템

## 설명
사용자로부터 현재 온도와 계절을 입력받아 적절한 활동을 추천하세요. 활동 추천은 다음과 같이 결정됩니다:

- 여름:
    - 30도 이상: "수영"
    - 그 외: "트레킹"
- 겨울:
    - 0도 이하: "스키"
    - 그 외: "겨울 산책"
- 봄과 가을:
    - 20도 이상: "자전거 타기"
    - 그 외: "도서관 방문"

## 입력 설명
- 첫 번째 입력: 현재 온도 (정수, 섭씨도)
- 두 번째 입력: 계절 ("summer", "winter", "spring", "fall")

## 출력 설명
- 추천 활동 출력
- Swimming, Trekking, Skiing, Winter walk, Biking,Visit the library


### 입력 예시 1 
32
summer
### 출력 예시 1
Swimming

### 입력 예시 2 
22
spring
### 출력 예시 2
Biking
"""""""""

temperature = int(input())
season = input()

if season == "summer":
    print("Swimming" if temperature >= 30 else "Trekking")
elif season == "winter":
    print("Skiing" if temperature <= 0 else "Winter walk")
else:
    print("Biking" if temperature >= 20 else "Visit the library")
