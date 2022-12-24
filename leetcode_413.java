class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int cnt = 0;
        int arrLength = nums.length;
        int total = 0;

        if(nums.length < 3) return 0;
            // for(int j=0; j<arrLength)

        // for(int i=arrLength-1; i>=2; i--){// 3개 연속일 때
        //     if(nums[i] - nums[i-1] == nums[i-1]-nums[i-2]){
        //         cnt++;
        //         total += cnt;
        //     }else {
        //         cnt = 0;
        //     }
        // }

        
        for(int i=0; i<nums.length-2; i++) {
            if(nums[i+2]-nums[i+1] == nums[i+1]-nums[i]){
                cnt++;
                total += cnt;
            }else cnt=0;
        }

        return total;
    }
}