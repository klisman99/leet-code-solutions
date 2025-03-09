function groupAnagrams(strs: string[]): string[][] {
    const anagrams: { [key: string]: string[]} = {};

    for (let i = 0; i < strs.length; i++) {
        const sortedWord = strs[i].split("").sort().join();

        if (!anagrams[sortedWord]) {
            anagrams[sortedWord] = [];
        }

        anagrams[sortedWord].push(strs[i]);
    }

    const groups: string[][] = [];

    for (let i in anagrams) {
        groups.push(anagrams[i]);
    }

    return groups;
};