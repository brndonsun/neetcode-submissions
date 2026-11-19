class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        //Add empty list (trivally true)
        result.add(new ArrayList<>());

        for(int curr : nums){
            int curr_size = result.size();

            for(int i = 0; i < curr_size; i++){
                List<Integer> subset = new ArrayList<>(result.get(i));
                subset.add(curr);
                result.add(subset);
            }
        }

        return result;
    }
}
