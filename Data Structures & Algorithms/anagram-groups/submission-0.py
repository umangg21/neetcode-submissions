class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words={}
        for word in strs:
            map_l = [0]*26
            for letter in word:
                map_l[ord(letter) - ord("a")] +=1
            
            key= tuple(map_l)
            if key not in dict_words:
                dict_words[key] =[]
            dict_words[key].append(word)

        return list(dict_words.values())
        