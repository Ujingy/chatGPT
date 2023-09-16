# 버블 정렬 과정
## 입력 데이터
``` yaml
John: 130, Sarah: 140, Emma: 120, Michael: 150, Emily: 135
```
## 시퀀스 다이어그램(딕셔너리 버블정렬)
``` mermaid
graph TD
    Start[시작]
    A[items 리스트 초기화: 딕셔너리 data에서 items로 변환]
    B{바깥 for문: i=0부터 len(items)-1}
    C{안쪽 for문: j=0부터 len(items)-1-i}
    D{items[j][1] > items[j+1][1] 확인}
    E[items[j]와 items[j+1] 위치 교환 (Swap)]
    F[j 증가하여 다음 원소 비교]
    G[i 증가]
    End[종료 및 items 출력]

    Start --> A
    A --> B
    B --> C
    C --> D
    D -- 예 --> E
    D -- 아니오 --> F
    E --> F
    F -- 다시 안쪽 for문으로 --> C
    F -- 안쪽 for문 종료 --> G
    G -- 다시 바깥 for문으로 --> B
    G -- 바깥 for문 종료 --> End

```
