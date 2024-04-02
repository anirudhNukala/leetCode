#include <string>
#include <unordered_map>
using namespace std;

class Solution {
    public:
        int romanToInt(string s) {
            unordered_map<char, int> romanVal = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
            int total = 0;

            for (int i = 0; i < s.length(); i++) {
                if (i + 1 < s.length() && romanVal[s[i]] < romanVal[s[i + 1]]) {
                    total -= romanVal[s[i]];
                } else {
                    total += romanVal[s[i]];
                }
            }

            return total;
        }
};