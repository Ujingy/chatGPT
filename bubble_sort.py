

def bubble_sort(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    n = len(keys)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                # 이름을 기준으로 정렬
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
                values[j], values[j + 1] = values[j + 1], values[j]

    sorted_dict = {keys[i]: values[i] for i in range(n)}
    return sorted_dict

# 주어진 딕셔너리
data = {'John': 130, 'Sarah': 140, 'Emma': 120, 'Michael': 150, 'Emily': 135}

# 정렬된 딕셔너리 출력
sorted_data = bubble_sort(data)
print(sorted_data)
