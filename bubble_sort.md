# 버블 정렬 과정
## 입력 데이터
``` yaml
John: 130, Sarah: 140, Emma: 120, Michael: 150, Emily: 135
```
## 시퀀스 다이어그램(딕셔너리 버블정렬)
``` mermaid
graph TD
    A[('John', 130), ('Sarah', 140), ('Emma', 120), ('Michael', 150), ('Emily', 135)] -->|Step 1| B[('John', 130), ('Emma', 120), ('Sarah', 140), ('Michael', 150), ('Emily', 135)]
    B -->|Step 2| C[('John', 130), ('Emma', 120), ('Sarah', 140), ('Michael', 150), ('Emily', 135)]
    C -->|Step 3| D[('John', 130), ('Emma', 120), ('Sarah', 140), ('Emily', 135), ('Michael', 150)]
    D -->|Step 4| E[('Emma', 120), ('John', 130), ('Sarah', 140), ('Emily', 135), ('Michael', 150)]
    E -->|Step 5| F[('Emma', 120), ('John', 130), ('Sarah', 140), ('Emily', 135), ('Michael', 150)]
    F -->|Step 6| G[('Emma', 120), ('John', 130), ('Emily', 135), ('Sarah', 140), ('Michael', 150)]
    G -->|Step 7| H[('Emma', 120), ('John', 130), ('Emily', 135), ('Sarah', 140), ('Michael', 150)]
    H -->|Step 8| I[('Emma', 120), ('John', 130), ('Emily', 135), ('Sarah', 140), ('Michael', 150)]
    I -->|Step 9| J[('Emma', 120), ('John', 130), ('Emily', 135), ('Sarah', 140), ('Michael', 150)]
    J --> K[{'Emma': 120, 'John': 130, 'Emily': 135, 'Sarah': 140, 'Michael': 150}]
```
