from typing import List


class BadCharacter(object):
    def __init__(self, pattern: str, search_text: str):
        self._pattern = pattern.upper()
        self._search_text = search_text.upper()

    def preprocess(self, process_text: str, bad_character_pos: int) -> int:
        """preprocessor for determining next move"""

        # getting variables ready
        s = process_text
        p = self._pattern

        # if no last occurence of bad character found in text
        # should slide the pattern  pass the bad character
        preprocess_result = bad_character_pos + 1

        for j in range(bad_character_pos - 1, -1, -1):
            # if exist any character same as bad character
            # return number of pos need to move to align them
            if p[j] == s[bad_character_pos]:
                preprocess_result = bad_character_pos - j
                break

        return preprocess_result

    def search(self) -> List[int]:
        """main search func"""

        # getting variables ready
        s = self._search_text
        p = self._pattern
        p_len, s_len, s_pos = len(p), len(s), 0
        found_index_list = []

        while s_pos <= s_len - p_len:
            bad_character_pos = -1
            # checking bad char existence
            for i in range(p_len - 1, -1, -1):
                if s[s_pos + i] != p[i]:
                    bad_character_pos = i
                    break

            if bad_character_pos == -1:
                # append position index to result list
                s_pos += 1
                found_index_list.append(s_pos)
            else:
                # apply bad character preprocessing
                s_pos += self.preprocess(s[s_pos : s_pos + p_len], bad_character_pos)
        return found_index_list
