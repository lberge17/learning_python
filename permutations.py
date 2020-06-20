def recursivePermutate(prefix, suffix, results):
    if len(suffix) == 0:
        results.append(prefix)
    else:
        # loop over suffix and recursively call this function to continue apppending letters to the prefix until the suffix is exhausted
        for char in suffix:
            recursivePermutate(prefix + char, suffix[0: suffix.index(char)] + suffix[suffix.index(char) + 1: len(suffix)], results)


def permutateString(string):
    results = []
    recursivePermutate("", string, results)
    for str in results:
        print(str)


permutateString('tokyo')

# Granted this does not account for repeat characters