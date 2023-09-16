# 버블 정렬 과정
## 입력 데이터
``` yaml
John: 130, Sarah: 140, Emma: 120, Michael: 150, Emily: 135
```
## 시퀀스 다이어그램(딕셔너리 버블정렬)
``` mermaid
graph TD
    A[시작: 딕셔너리 data를 items 리스트로 변환]
    B[바깥 for문 시작: i=0부터 len(items)-1까지]
    C[안쪽 for문 시작: j=0부터 len(items)-1-i까지]
    D{items[j][1] > items[j+1][1] 인가?}
    E[두 원소의 위치를 바꾼다 (Swap)]
    F[안쪽 for문 다음 단계로]
    G[바깥 for문 다음 단계로]
    H[정렬 완료: items 출력]
    
    A --> B
    B --> C
    C --> D
    D -- 예 --> E
    D -- 아니오 --> F
    E --> F
    F --> C
    C --> G
    G --> B
    B --> H
```
