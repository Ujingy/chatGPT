# 딕셔너리의 값으로 버블 정렬하기
``` python
data = {'John': 130, 'Sarah': 140, 'Emma': 120, 'Michael': 150, 'Emily': 135}

# 딕셔너리를 튜플의 리스트로 변환
items = list(data.items())

# 버블정렬
for i in range(len(items) - 1):
    for j in range(len(items) - 1 - i):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]
            print(items)  # 정렬 과정 출력

# 정렬된 딕셔너리로 변환
sorted_data = dict(items)
print(sorted_data)
```


# 파이썬 코드 실행 순서도

###
    Start(Start)
    A. [Convert Dictionary to List of Tuples]
    B. [Set i to 0]
    C. {Is i < len(items) - 1?}
    D. [Set j to 0]
    E. {Is j < len(items) - 1 - i?}
    F. {items[j][1] > items[j + 1][1]?}
    G. [Swap items[j] and items[j + 1]]
    H. [Increment j by 1]
    I. [Increment i by 1]
    End[Convert List of Tuples back to Dictionary]
    
``` mermaid
graph TD
    Start --> A
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> E
    E -- No --> I
    I --> C
    C -- No --> End

```
###
이 다이어그램은 다음과 같이 동작합니다:

1. 딕셔너리를 튜플의 리스트로 변환합니다.
2. 외부 루프를 시작합니다 (i를 사용하여).
3. 내부 루프를 시작합니다 (j를 사용하여).
4. j 위치의 튜플 값과 j+1 위치의 튜플 값을 비교합니다.
5. 필요한 경우 두 튜플을 교환합니다.
6. j 값을 증가시키고 내부 루프를 계속합니다.
7. 내부 루프가 완료되면 i 값을 증가시키고 외부 루프를 계속합니다.
8. 모든 정렬이 완료되면 튜플의 리스트를 다시 딕셔너리로 변환합니다.
Mermaid를 사용하여 위의 UML 다이어그램을 웹 페이지에 렌더링하려면, 해당 Mermaid 코드를 웹 페이지 HTML에 포함시켜야 합니다.

# 딕셔너리 버블정렬 시퀀스 다이어그램
``` mermaid
sequenceDiagram
    participant User
    participant Code
    participant Dictionary
    participant List
    participant BubbleSort

    User->>Code: Start
    Code->>Dictionary: Initialize data
    Code->>List: Convert to list of tuples (items)
    loop for i in range
        Code->>BubbleSort: Outer loop starts
        loop for j in range
            Code->>BubbleSort: Inner loop starts
            opt items[j][1] > items[j + 1][1]
                BubbleSort->>List: Swap items
            end
        end
    end
    Code->>Dictionary: Convert list back to sorted dictionary
    User->>Code: View sorted result
```

