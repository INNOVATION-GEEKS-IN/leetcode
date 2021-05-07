// URL : https://leetcode.com/problems/defanging-an-ip-address/

// Example 1:

// Input: address = "1.1.1.1"
// Output: "1[.]1[.]1[.]1"
// Example 2:

// Input: address = "255.100.50.0"
// Output: "255[.]100[.]50[.]0"
 

// Constraints:

// The given address is a valid IPv4 address.

char * defangIPaddr(char * address){
    char *str = malloc(sizeof(char)*100 );
    int str_ind = 0;
    for(int ind=0;address[ind];ind++) {
        if(address[ind] == '.') {
            str[str_ind++] = '[';
            str[str_ind++] = '.';
            str[str_ind++] = ']';
            continue;
        }
        str[str_ind++] = address[ind];
    }
    
    return str;
}