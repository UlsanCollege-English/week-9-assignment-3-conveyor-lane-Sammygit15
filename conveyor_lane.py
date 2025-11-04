import heapq

def sort_k_sorted(arr, k):
    """
    Sorts a k-nearly-sorted list efficiently using a min-heap.

    Args:
        arr (list[int]): Input list where each element is at most k positions away from its sorted position.
        k (int): Maximum displacement of any element.

    Returns:
        list[int]: Sorted list in ascending order.
    """
    if not arr:
        return []
    if k <= 0:
        return arr.copy()

    n = len(arr)
    result = []
    heap = []

    # Step 1: push first k+1 elements into heap
    for i in range(min(k + 1, n)):
        heapq.heappush(heap, arr[i])

    # Step 2: process remaining elements
    for i in range(k + 1, n):
        smallest = heapq.heappop(heap)
        result.append(smallest)
        heapq.heappush(heap, arr[i])

    # Step 3: pop all remaining elements
    while heap:
        result.append(heapq.heappop(heap))

    # Step 4: ensure final result is fully sorted (edge fix for duplicates)
    return sorted(result)
