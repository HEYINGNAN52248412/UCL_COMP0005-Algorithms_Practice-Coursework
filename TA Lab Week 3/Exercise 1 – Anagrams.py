def sort_anagrams (strings: List[str]):
    anagrams_map: dict[str, list[str]] = {}
    for string in strings:
        sorted_string = "".join(sorted(string))

        if sorted_string not in anagrams_map:
            anagrams_map[sorted_string] = []
            
        anagrams_map[sorted_string].append(string)

    return_list = []
    for key, value in anagrams_map.items():
        return_list.append(value)

    return return_list
