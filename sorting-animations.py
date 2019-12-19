from decimal import *
import sys
import random
import time
import math
import pygame

# change these to whatever values you want
width = 400
height = 500

# Defining some colors
black = (0,0,0)
color = (120,255,120)
white = (255,255,255)

pygame.init()
clock = pygame.time.Clock()

# draw unsorted rray
def draw(arr):
    screen.fill(black)

    for i in range(width):
        x1 = x2 = i
        y1 = height
        y2 = height - arr[i]
        pointlist = [(x1,y1), (x2, y2)]
        pygame.draw.lines(screen, color, False, pointlist, 1)

    pygame.display.update()
    clock.tick(200)

# draw the sorted array
def drawSorted(arr):
    screen.fill(black)

    for i in range(width):
        x1 = x2 = i
        y1 = height
        y2 = height - arr[i]
        pointlist = [(x1,y1), (x2, y2)]
        pygame.draw.lines(screen, white, False, pointlist, 1)

    pygame.display.update()

# create and randomise array
def generateArray():
    arr = []
    for i in range(width):
        arr.append(random.randint(0,height))
    random.shuffle(arr)
    return arr

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
    temp = [0]*width
    mergesort(arr, temp, 0, width-1)

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

if __name__ == "__main__":

    size = (width,height)
    screen = pygame.display.set_mode(size)

    arr = generateArray()
    finished = False
    while True:
        if len(sys.argv) >= 2 and not finished:
            if sys.argv[1] == "merge":
                pygame.display.set_caption("Merge Sort")
                performMergeSort(arr)
            elif sys.argv[1] == "bubble":
                pygame.display.set_caption("Bubble Sort")
                print("WARNING: This may take a while...")
                bubbleSort(arr)
            elif sys.argv[1] == "bogo":
                pygame.display.set_caption("Bogo sort")
                print("This is definitely gonna take a while...")
                bogoSort(arr)
            elif sys.argv[1] == "heap":
                pygame.display.set_caption("Heap sort")
                heapSort(arr)
            else:
                print("Not a valid option please try again")
        elif finished:
            drawSorted(arr)
        else:
            print("Not enough command line arguments")
        finished = True
