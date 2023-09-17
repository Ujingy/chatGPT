# 버블 정렬 과정
## 입력 데이터
``` yaml
John: 130, Sarah: 140, Emma: 120, Michael: 150, Emily: 135
```
## 시퀀스 다이어그램(딕셔너리 버블정렬)
* Start[시작]
    1. A[items 리스트 초기화: 딕셔너리 data에서 items로 변환]
    2. B{바깥 for문: i=0부터 len(items)-1}
    3. C{안쪽 for문: j=0부터 len(items)-1-i}
    4. D{items[j][1] > items[j+1][1] 확인}
    5. E[items[j]와 items[j+1] 위치 교환 (Swap)]
    6. F[j 증가하여 다음 원소 비교]
    7. G[i 증가]
* End[종료 및 items 출력]
    
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
