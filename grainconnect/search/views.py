from django.shortcuts import render
from django.http import JsonResponse
import json


def get_index(request):
    array = [-1, 8, 22, 67, 71, 79, 80, 81, 90, 100]
    search_value = int(request.GET.get("value", 1))
    found_index = -1
    #Implement search using binary search, O(logn)
    #sort array
    array.sort()

    start_index = 0
    end_index = len(array) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2

        if search_value == array[mid_index]:
            found_index = mid_index
            break
        elif search_value > array[mid_index]:
            start_index = mid_index + 1          
        elif search_value < array[mid_index]:
            end_index = mid_index - 1
            

    return JsonResponse({"index":found_index})

    

