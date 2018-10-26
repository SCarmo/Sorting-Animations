from Tkinter import *
from decimal import *
import random
import time
import math
tk = Tk()

# change these to whatever values you want
WIDTH = 400
HEIGHT = 200


canvas = Canvas(tk, width=WIDTH, height=HEIGHT)

def main():
    arr = generateArray()
    if len(sys.argv) >= 2:
        if sys.argv[1] == "merge":
            displayCanvas("Merge sort visualisation")
            performMergeSort(arr)
            drawSorted(arr)
        elif sys.argv[1] == "bubble":
            displayCanvas("Bubble sort visualisation")
            print("WARNING: This may take a while...")
            print("Shows why bubble sort is rarely used")
            bubbleSort(arr)
            drawSorted(arr)
        elif sys.argv[1] == "bogo":
            displayCanvas("Bogo sort visualisation")
            print("This is definitely gonna take a while...")
            bogoSort(arr)
            drawSorted(arr)
        else:
            print("Not a valid option please try again")
    else:
        print("Not enough command line arguments")

    print("finished")

'''----------------Bogo sort animation----------------'''

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
def drawSorted(arr):
    canvas.delete("all")
    for i in range(WIDTH):
        canvas.create_line(i, HEIGHT, i, HEIGHT-arr[i], fill="blue")
    tk.update()
    canvas.mainloop()   

# create and randomise array
def generateArray():
    arr = []
    for i in range(WIDTH):
        arr.append(random.randint(0,HEIGHT))
    random.shuffle(arr)
    return arr

main()