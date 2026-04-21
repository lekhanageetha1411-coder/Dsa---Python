height = [1,2,3,4,5,6,7,8]
left = 0
right = len(height)-1
max_area = 0

while left < right:
    h = min(height[left],height[right])
    width = right - left
    area = h * width

    max_area = max(max_area,area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(max_area)
        
        