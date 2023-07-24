#include <stdbool.h>

bool containsDuplicate(int* nums, int numsSize) {
    int i, j;
    bool valid = false;

    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                valid = true;
                break;
            }
        }
        if (valid) {
            break;
        }
    }

    return valid;
}
