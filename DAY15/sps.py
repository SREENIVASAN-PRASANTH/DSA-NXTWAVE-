def get_missing_sps(nums):
    seq_prefix_sum = 0
    for i in range(0,len(nums)):
        if i > 0 and nums[i] != nums[i -1] + 1:
            break
        seq_prefix_sum += nums[i]
        
    x = seq_prefix_sum
    while x in nums:
        x+= 1
    
    return x

if __name__ == "__main__":
    nums = [1,2,3,2,5]
    print(get_missing_sps(nums))