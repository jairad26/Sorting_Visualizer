import time

def merge_sort(data, drawData, tick):
	merge_sort_alg(data, 0, len(data) - 1, drawData, tick)


def merge_sort_alg(data, left, right, drawData, tick):
	if (left < right):
		middle = (left + right) // 2
		merge_sort_alg(data, left, middle, drawData, tick)
		merge_sort_alg(data, middle + 1, right, drawData, tick)
		merge(data, left, middle, right, drawData, tick)

def merge(data, left, middle, right, drawData, tick):
	drawData(data, getColorArray(len(data), left, middle, right))
	time.sleep(tick)

	leftPart = data[left:middle + 1]
	rightPart = data[middle + 1: right + 1]

	leftIdx = rightIdx = 0

	for curr in range(left, right + 1):
		if (leftIdx < len(leftPart) and rightIdx < len(rightPart)):
			if(leftPart[leftIdx] <= rightPart[rightIdx]):
				data[curr] = leftPart[leftIdx]
				leftIdx = leftIdx + 1
			else:
				data[curr] = rightPart[rightIdx]
				rightIdx = rightIdx + 1

		elif (leftIdx < len(leftPart)):
			data[curr] = leftPart[leftIdx]
			leftIdx = leftIdx + 1
		else:
			data[curr] = rightPart[rightIdx]
			rightIdx = rightIdx + 1

	drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
	time.sleep(tick)

def getColorArray(len, left, middle, right):
	colorArray = []

	for i in range(len):
		if( i >= left and i <= right):
			if(i <= middle):
				colorArray.append("yellow")
			else:
				colorArray.append("red")
		else:
			colorArray.append("white")

	return colorArray

##data = [1, 4, 12, 43, 6, 27]
##merge_sort(data, 0, 0)
##print(data)
