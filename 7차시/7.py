def binary_search(data, key):
    data.sort()

    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) //2

        if data[mid] == key:
            print("검색 성공!\n%d번 인덱스에 key값이 존재합니다.\n" %mid)
            return 0
        
        elif data[mid] > key:
            end = mid - 1

        elif data[mid] < key:
            start = mid + 1

    return 0

