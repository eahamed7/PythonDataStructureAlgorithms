import random
import time

# Iterative Binary Search Function 
# It returns location of x in given array arr if present, 
# else returns -1 
def binary_search(arr, l, r, x): 
  
    while l <= r: 
        mid = l + (r - l)//2; 
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
    # If we reach here, then the element was not present 
    return -1

def linear_search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1

# Python program for implementation of Bubble Sort
 
def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# Python program for implementation of Insertion or Insert Sort
 
def insert_sort(arr):
    n = len(arr)

    for i in range(1, n):   #first item is skipped
        current_value = arr[i]
        position = i 
        while position> 0 and arr[position-1]> current_value: #go backwards through arr
            arr[position] = arr[position-1] # move entry up one in arr
            position = position-1           # look at previous entry next
        arr[position] = current_value   # put in right place in sorted list so far

# Python program for implementation of merge_sort

  
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]  #create 2 arrays for each half - this uses extra storage (space)
        righthalf = arr[mid:]

        merge_sort(lefthalf) #sort two parts first recursively 
        merge_sort(righthalf)

        # Now merge the 2 halves; both are sorted

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1


# Python program for implementation of quick sort

def do_quick_sort(arr):
   quick_sort(arr,0,len(arr)-1)

def quick_sort(arr,first,last):
   if first<last:

       splitpoint = partition(arr,first,last)

       quick_sort(arr,first,splitpoint-1)
       quick_sort(arr,splitpoint+1,last)


def partition(arr,first,last):
   pivotvalue = arr[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = arr[leftmark]
           arr[leftmark] = arr[rightmark]
           arr[rightmark] = temp

   temp = arr[first]
   arr[first] = arr[rightmark]
   arr[rightmark] = temp
   return rightmark

def make_random_list(size):
    return [random.randint(0,(size**2)) for i in range(size)]

def menu():
    choice = int(input("""
1 to recreate the list of data
2 to do a linear search
3 to do a binary search
4 to do a bubble sort
5 to do an insertion sort
6 to do a merge sort
7 to do a quick sort
0 to quit
-> """))
    return choice

random_list = (make_random_list(10000)) # set up default list of 10000

choice = -1

while choice != 0:
    choice = menu()

    if choice == 1:
        size = int(input("Enter size of list (> 0) : "))
        print ("making random list of", size, "elements")
        random_list = (make_random_list(size))
    elif choice == 2:
        print ("Linear search of list of", len(random_list))
        s1 = time.perf_counter()
        linear_search (random_list, -5)
        s2 = time.perf_counter()
        print ('Linear search took ', s2-s1)
    elif choice == 3:
        print ("Binary search of list of", len(random_list))
        sorted_list = list(random_list) #have to sort list to do binary search
        sorted_list.sort()  #make a copy and sort it
        s1 = time.perf_counter()
        result = binary_search(sorted_list, 0, len(sorted_list)-1, -5) 
        s2 = time.perf_counter()
        print ('Binary search took ',s2-s1)
    elif choice == 4:
        print ("bubble sort of list of", len(random_list))
        list_to_sort = list(random_list) #copy list so original still unsorted
        s1 = time.perf_counter()
        bubble_sort(list_to_sort) 
        s2 = time.perf_counter()
        print ('Bubble sort took ',s2-s1)
        #print (random_list) #check
        #print (list_to_sort)
    elif choice == 5:
        print ("insert sort of list of", len(random_list))
        list_to_sort = list(random_list) #copy list so original still unsorted
        s1 = time.perf_counter()
        insert_sort(list_to_sort) 
        s2 = time.perf_counter()
        print ('Insert sort took ',s2-s1)
        #print (random_list) #check
        #print (list_to_sort)
    elif choice == 6:
        print ("merge sort of list of", len(random_list))
        list_to_sort = list(random_list) #copy list so original still unsorted
        s1 = time.perf_counter()
        merge_sort(list_to_sort) 
        s2 = time.perf_counter()
        print ('merge sort took ',s2-s1)
        #print (random_list) #check
        #print (list_to_sort)

    elif choice == 7:
        print ("quick sort of list of", len(random_list))
        list_to_sort = list(random_list) #copy list so original still unsorted
        s1 = time.perf_counter()
        do_quick_sort(list_to_sort) 
        s2 = time.perf_counter()
        print ('quick sort took ',s2-s1)
        #print (random_list) #check
        #print (list_to_sort)
