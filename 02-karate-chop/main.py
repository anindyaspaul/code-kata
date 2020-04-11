from typing import List, Callable


def binary_search_v1(query: int, data: List[int]) -> int:
    """Iterative solution

    Returns the first occurrence if there are multiple instances
    of query.
    """

    pos = -1

    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start+end)//2
        if data[mid] > query:
            end = mid-1
        elif data[mid] < query:
            start = mid+1
        else:
            # We have found the query. But we want
            # to find the first occurrence of the query.
            # Thus, we keep searching in the smaller half.
            # Alternatively, to search for the last index,
            # we have to set start = mid+1.
            pos = mid
            end = mid-1
    
    return pos
        

def binary_search_v2(query: int, data: List[int]) -> int:
    """Recursive solution by passing start and end indices

    Returns the first occurrence if there are multiple instances
    of query.
    """

    def binary_search_v2_recur(start, end):
        """Find the query between start and end recursively
        """

        if start > end:
            return -1
        
        mid = (start+end)//2
        if data[mid] > query:
            pos = binary_search_v2_recur(start, mid-1)
        elif data[mid] < query:
            pos = binary_search_v2_recur(mid+1, end)
        else:
            pos = binary_search_v2_recur(start, mid-1)
            pos = mid if pos == -1 else pos
        
        return pos

    return binary_search_v2_recur(0, len(data)-1)


def binary_search_v3(query: int, data: List[int]) -> int:
    """Recursive solution by passing list slices

    Returns the first occurrence if there are multiple instances
    of query.
    """

    mid = (len(data)-1)//2

    if mid < 0:
        return -1
    
    if data[mid] > query:
        return binary_search_v3(query, data[:mid])
    elif data[mid] < query:
        pos = binary_search_v3(query, data[mid+1:])
        return -1 if pos == -1 else mid+1 + pos
    else:
        pos = binary_search_v3(query, data[:mid])
        return mid if pos == -1 else pos


def test_binary_search(binary_search: Callable[[int, List[int]], int]) -> None:
    assert -1 == binary_search(3, [])
    assert -1 == binary_search(3, [1])
    assert  0 == binary_search(1, [1])

    assert  0 == binary_search(1, [1, 3, 5])
    assert  1 == binary_search(3, [1, 3, 5])
    assert  2 == binary_search(5, [1, 3, 5])
    assert -1 == binary_search(0, [1, 3, 5])
    assert -1 == binary_search(2, [1, 3, 5])
    assert -1 == binary_search(4, [1, 3, 5])
    assert -1 == binary_search(6, [1, 3, 5])

    assert  0 == binary_search(1, [1, 3, 5, 7])
    assert  1 == binary_search(3, [1, 3, 5, 7])
    assert  2 == binary_search(5, [1, 3, 5, 7])
    assert  3 == binary_search(7, [1, 3, 5, 7])
    assert -1 == binary_search(0, [1, 3, 5, 7])
    assert -1 == binary_search(2, [1, 3, 5, 7])
    assert -1 == binary_search(4, [1, 3, 5, 7])
    assert -1 == binary_search(6, [1, 3, 5, 7])
    assert -1 == binary_search(8, [1, 3, 5, 7])

    assert  0 == binary_search(1, [1, 1, 3, 5, 7])
    assert  1 == binary_search(3, [1, 3, 3, 3, 5, 7])


def main() -> None:
    test_binary_search(binary_search_v1)
    test_binary_search(binary_search_v2)
    test_binary_search(binary_search_v3)


if __name__ == '__main__':
    main()
