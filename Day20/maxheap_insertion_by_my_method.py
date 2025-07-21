def insert_maxheap(arr, k, newindex):
    if newindex == 1:
        arr[newindex - 1] = k
        return arr
    else:
        child_index = newindex - 1
        parent_index = child_index // 2
        if arr[parent_index] < k:
            arr[child_index] = arr[parent_index]
            newindex = parent_index + 1
            return insert_maxheap(arr, k, newindex)
        else:
            arr[newindex - 1] = k
            return arr


if __name__ == "__main__":
    print("Enter your max heap tree in array form ")
    arr = list(map(int, input("Enter space seperated values -> ").split()))
    print("Enter the value you want to insert in max heap -> ")
    k = int(input())
    arr.append(k)
    newarr = insert_maxheap(arr, k, newindex=len(arr))
    print(newarr)
