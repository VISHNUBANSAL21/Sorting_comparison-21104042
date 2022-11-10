#Q-Compare Bubble sort and Selection sort ? 

# Bubble Sort
def bubbleSort(array):
    
  #  accessing each array element
  for i in range(len(array)):

    # comparing array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      if array[j] > array[j + 1]:

        # swapping elements 
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp   
        
'''
1.number of comparasions 
  Bubble sort repeatedly compares and swaps(if needed) adjacent elements in every pass.
  In i-th pass of Bubble Sort (ascending order), last (i-1) elements are already sorted, 
  and i-th largest element is placed at (N-i)-th position, i.e. i-th last position.as shown in the code
  comparasions;- n-i-1....
  Bubble sort employs two loops: an inner loop and an outer loop.
  The inner loop performs O(n) comparisons deterministically.
    
2. Number of swaps
     Best Case Sorted array as input. Or almost all elements are in proper place. [ O(N) ]. O(1) swaps.
     Worst Case: Reversely sorted / Very few elements are in proper place. [ O(N2) ] . O(N2) swaps.
     Average Case: [ O(N2) ] . O(N2) swaps.
     it is a simple sorting approach and also a stable sort
    
3. it is a inplace sorting algorithm  which modifies the original array's elements to sort the given array.'''


# Selection Sort
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            
            # selecting  the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put minimum at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
'''
1.no of comparasions 
  Selection sort selects i-th smallest element and places at i-th position.
  This algorithm divides the array into two parts: sorted (left) and unsorted (right) subarray. 
  It selects the smallest element from unsorted subarray and places in the first position of that subarray (ascending order).
  It repeatedly selects the next smallest element. 
    
  comparasions:- n-i....(as shown in the code 2nd for loop)
            
2. #Number of swaps
  Best Case [ O(N2) ]. And O(1) swaps.
  Worst Case: Reversely sorted, and when the inner loop makes a maximum comparison. [ O(N2) ] . Also, O(N) swaps.
  Average Case: [ O(N2) ] . Also O(N) swaps.
  It can also be used on list structures that make add and remove efficient, such as a linked list. Just remove the smallest element of unsorted part and end at the end of sorted part.
  The number of swaps reduced. O(N) swaps in all cases.
    
3. it can be in placce as well as out place algorithm
  In-Place sort.
    (When elements are shifted instead of being swapped (i.e. temp=a[min],
   then shifting elements from ar[i] to ar[min-1] one place up and then putting a[i]=temp).  
  Out-place:-              
    If swapping is opted for, the algorithm is not In-place.) '''