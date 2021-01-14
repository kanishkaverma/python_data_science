#%%
#%%
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i, len(nums)):


                if nums[i]+nums[j]==target:
                    return i,j
 



# %%
sol = Solution()
print(sol.twoSum([3,2,4],6))



#%%
if target_num == nums[i]: 
                print(nums.index(target_num,i)

                if target_num != nums[i]:
                    answer.append(nums.index(target_num, i))
                elif answer:
                    answer.append(i)
                    break
                else: 
                    print("lol")
            else: 
                pass

#%%
class Solution(object):
    def findKthPositive(self, arr, k):
        map= dict()
        key=0
        if arr[0] == 1 : 
            for i in range(len(arr)): 
                diff = arr[index + 1 ] - arr[index] 
                if diff > 1 : 
                    for i in range(diff+1):
                        map[key] = arr[index] + i
                        key = key + 1
            print(map)
        else: 
            map[key] = 1 
            
# %%
