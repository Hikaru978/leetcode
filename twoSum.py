nums = [2, 7, 11, 15]
target = 17

def twoSum(nums, target):
    indices = []
    for i in range(0, len(nums), 1):
        #print(i)
        #j = 0
        j = i + 1
        while j < len(nums):
            print(nums[i], nums[j])
            print(nums[i] + nums[j])
            if((nums[i] + nums[j]) == target ):
                #print("["+str(i)+","+str(j)+"]", end="")
                indices.append(i)
                indices.append(j)
                return indices
            else:
                j += 1
            

twoSum(nums,target)
