class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> s_freq = new HashMap<>();
        Map<Character, Integer> t_freq = new HashMap<>();


        for (char letter: s.toCharArray()){
            s_freq.put(letter, s_freq.getOrDefault(letter, 0) + 1);
        }

        for (char letter: t.toCharArray()){
            t_freq.put(letter, t_freq.getOrDefault(letter, 0) + 1);
        }

        return s_freq.equals(t_freq);

    }
}
