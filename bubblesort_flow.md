# 파이썬 코드 실행 순서도

Start(Start)
    A[Convert Dictionary to List of Tuples]
    B[Set i to 0]
    C{Is i < len(items) - 1?}
    D[Set j to 0]
    E{Is j < len(items) - 1 - i?}
    F{items[j][1] > items[j + 1][1]?}
    G[Swap items[j] and items[j + 1]]
    H[Increment j by 1]
    I[Increment i by 1]
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
