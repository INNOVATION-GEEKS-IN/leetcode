/*
URL : https://leetcode.com/problems/reverse-integer/
 Example 1:
 Input: x = 123
 Output: 321
 Example 2:
 Input: x = -123
 Output: -321
 Example 3:
 Input: x = 120
 Output: 21
 Example 4:
 Input: x = 0
 Output: 0

 Constraints:
 -231 <= x <= 231 - 1
*/

#include <stdio.h>
#include <stdlib.h>

int reverse(int x){
    int sign = x<0 ? -1 : 1;
    x = abs(x);
    int num=0;
    while(x !=0){
        num*=10;
        num += x%10;
        x/=10;
    }
    return num*sign;
}

int main() {
    printf("%d\n", reverse(123));
    printf("%d\n", reverse(-123));
    printf("%d\n", reverse(0)); 
    printf("%d\n", reverse(1534236469));
    return 0;
}