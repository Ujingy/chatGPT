# 버블 정렬 과정
## 입력 데이터
``` yaml
John: 130, Sarah: 140, Emma: 120, Michael: 150, Emily: 135
```
## 시퀀스 다이어그램(딕셔너리 버블정렬)
``` mermaid
graph TD
    Start --> A[Emma, John, Sarah, Michael, Emily]
    A --> B[Emma, John, Sarah, Emily, Michael]
    B --> C[Emma, John, Emily, Sarah, Michael]
    C --> D[Emma, Emily, John, Sarah, Michael]
    ... --> Z[Emma, Emily, John, Sarah, Michael]  {# 여기서 ... 은 중간 과정을 생략하였음을 나타냅니다. #}
    Z --> End

```
