class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        viable_triplets = []
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            else:
                viable_triplets.append(triplet)

        for i in range(0, 3):
            found_val = False
            for trip in viable_triplets:
                if target[i] == trip[i]:
                    found_val = True

            if not found_val: return False

        return True


