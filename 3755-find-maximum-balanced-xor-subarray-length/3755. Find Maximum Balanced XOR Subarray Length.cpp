class Solution {
public:
    int maxBalancedSubarray(vector<int>& nums) {
        int x = 0;
        int e = 0;
        int o = 0;
        map<pair<int, int>, int> m;
        m[{0, 0}] = -1;
        int res = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] % 2){
                o ++;
            }
            else{
                e++;
            }
            x^=nums[i];
            
            if(m.find({o-e, x}) != m.end()){
                res = max(res, i - m[{o-e, x}]);
            }
            else{
                m[{o-e, x}] = i;
            }
        }
        return res;
    }
};