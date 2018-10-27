from Tkinter import *
from decimal import *
import random
import time
import math
tk = Tk()

# change these to whatever values you want
WIDTH = 400
HEIGHT = 500
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)

def main():
    arr = generateArray()
    start = 0
    end = 0
    if len(sys.argv) >= 2:
        if sys.argv[1] == "merge":
            displayCanvas("Merge sort visualisation")
            start = time.time()
            performMergeSort(arr)
            end = time.time()
        elif sys.argv[1] == "bubble":
            displayCanvas("Bubble sort visualisation")
            print("WARNING: This may take a while...")
            start = time.time()
            bubbleSort(arr)
            end = time.time()
        elif sys.argv[1] == "bogo":
            displayCanvas("Bogo sort visualisation")
            print("This is definitely gonna take a while...")
            start = time.time()
            bogoSort(arr)
            end = time.time()
        elif: sys.argv[1] == "heap":
            displayCanvas("Heap sort visualisation")
            start = time.time()
            heapSort(arr)
            end = time.time()
        else:
            print("Not a valid option please try again")
        if end:
            drawSorted(arr,start,end)
    else:
        print("Not enough command line arguments")

'''----------------Heap sort animation----------------'''
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)
    
    draw(arr)
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
'''---------------------------------------------------'''

'''----------------Bogo sort animation----------------'''
# cause why not
def bogoSort(arr):
    sorted = arr.sort()
    while arr != sorted:
        random.shuffle(arr)
        draw(arr)

'''---------------------------------------------------'''


'''----------------Merge sort animation----------------'''

def performMergeSort(arr):
    temp = [0]*WIDTH
    mergesort(arr, temp, 0, WIDTH-1)

def mergesort(arr,temparr,left,right):
    if left < right:
        mid = int((left + right)/2)
        mergesort(arr,temparr,left,mid)
        mergesort(arr,temparr,mid+1,right)
        merge(arr,temparr,left,mid + 1,right)

    else:
        pass

def merge(arr,temp,left,mid,right):
    left_end = mid - 1
    temp_pos = left
    size = right - left + 1

    while left <= left_end and mid<=right:
        if arr[left] <= arr[mid]:
            temp[temp_pos] = arr[left]
            temp_pos = temp_pos + 1
            left = left + 1
        else:
            temp[temp_pos] = arr[mid]
            temp_pos = temp_pos + 1
            mid = mid + 1

    while left<=left_end:
        temp[temp_pos] = arr[left]
        left = left + 1
        temp_pos = temp_pos + 1

    while mid <= right:
        temp[temp_pos] = arr[mid]
        mid = mid + 1
        temp_pos = temp_pos + 1

    for i in range(0,size):
        arr[right] = temp[right]
        right = right - 1
        draw(arr)
'''----------------------------------------------------'''


'''----------------Bubble sort animation----------------'''

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def bubbleSort(arr):

    i = 0
    j = 0

    while i < len(arr):
        draw(arr)
        a = arr[j]
        b = arr[j+1]
        if a > b:
            swap(arr,j,j+1)

        j = j + 1
        if j >= len(arr)-i-1:
            j = 0
            i = i + 1
'''----------------------------------------------------'''


# draw unsorted array
def draw(arr):
    canvas.delete("all")
    for i in range(WIDTH):
        canvas.create_line(i, HEIGHT, i, HEIGHT-arr[i], fill="orange")
    tk.update()

# draw the canvas
def displayCanvas(string):
    tk.title(string)
    canvas.pack()
    canvas.config()
    canvas.configure(background="black")

# draw the sorted array
def drawSorted(arr,start,end):
    canvas.delete("all")
    for i in range(WIDTH):
        canvas.create_line(i, HEIGHT, i, HEIGHT-arr[i], fill="blue")
    tk.update()
    print("Finished in {} seconds".format(round(end-start, 3)))
    canvas.mainloop()   

# create and randomise array
def generateArray():
    arr = []
    for i in range(WIDTH):
        arr.append(random.randint(0,HEIGHT))
    random.shuffle(arr)
    return arr

main()