
'''
Given a set of tiles (represented by numbers from 0 - 9), a valid configuration of tiles for success at this game happens only when the entire set can be divided such that:
- There is at least 1 pair [e.g. - 9,9]
- There can be any number of triples. [e.g. - 1,1,1]. No. of triplets can be 0 as well.
- There can be any increasing triple [e.g. - 1,2,3]. No. of increasing triplets can be 0 as well.
'''
class Solution:
    @staticmethod
    def is_mahjong_win(tiles):
        if len(tiles) <= 0:
            return False
        return Solution.is_mahjong_win_helper(tiles, 0, False, {})

    @staticmethod
    def is_mahjong_win_helper(tiles, index, has_pair, map):
        if index not in map:
            remaining_tiles = len(tiles) - index
            if remaining_tiles == 1:
                return False
            elif remaining_tiles == 2:
                return Solution.does_pair_exist(tiles, index)
            elif remaining_tiles == 3:
                return has_pair and (
                    Solution.does_regular_triplet_exist(tiles, index)
                    or Solution.does_increasing_triplet_exist(tiles, index)
                )
            result = (
                (
                    Solution.does_pair_exist(tiles, index)
                    and Solution.is_mahjong_win_helper(tiles, index + 2, True, map)
                )
                or (
                    Solution.does_regular_triplet_exist(tiles, index)
                    and Solution.is_mahjong_win_helper(tiles, index + 3, has_pair, map)
                )
                or (
                    Solution.does_increasing_triplet_exist(tiles, index)
                    and Solution.is_mahjong_win_helper(tiles, index + 3, has_pair, map)
                )
            )
            map[index] = result
        return map[index]

    @staticmethod
    def does_pair_exist(tiles, start_index):
        return (
            start_index < len(tiles)
            and start_index + 1 < len(tiles)
            and tiles[start_index] == tiles[start_index + 1]
        )   

    @staticmethod
    def does_regular_triplet_exist(tiles, start_index):
        first = start_index
        second = start_index + 1
        third = start_index + 2
        return (
            first < len(tiles)
            and second < len(tiles)
            and third < len(tiles)
            and tiles[first] == tiles[second] == tiles[third]
        )

    @staticmethod
    def does_increasing_triplet_exist(tiles, start_index):
        first = start_index
        second = start_index + 1
        third = start_index + 2
        return (
            first < len(tiles)
            and second < len(tiles)
            and third < len(tiles)
            and int(tiles[second]) == int(tiles[first]) + 1
            and int(tiles[third]) == int(tiles[second]) + 1
        )

if __name__ == "__main__":
    print(Solution.is_mahjong_win("123"))
    print(Solution.is_mahjong_win("11223344555678"))
    print(Solution.is_mahjong_win("12233344555599"))
    print(Solution.is_mahjong_win("11133678"))
    print(Solution.is_mahjong_win("12733344558559"))