
1. A[시작: 딕셔너리 data를 items 리스트로 변환]
2. B[바깥 for문 시작: i=0부터 len(items)-1까지]
3. C[안쪽 for문 시작: j=0부터 len(items)-1-i까지]
4. D{items[j][1] > items[j+1][1] 인가?}
5. E[두 원소의 위치를 바꾼다 (Swap)]
6. F[안쪽 for문 반복: j 증가]
7. G[바깥 for문 반복: i 증가]
8. H[정렬 완료: items 출력]
``` mermaid
graph TD
    A --> B
    B --> C
    C --> D
    D -- 예 --> E
    E --> F
    D -- 아니오 --> F
    F -- 다시 안쪽 for문으로 --> C
    F -- 안쪽 for문 종료 --> G
    G -- 다시 바깥 for문으로 --> B
    G -- 바깥 for문 종료 --> H
```
