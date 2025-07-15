class Solution {
  public:
    bool divby13(string &s) {
        int rem = 0,n = s.size();
        for(int i = 0;i<n;i++){
            rem = rem * 10 + s[i] - '0';
            rem = rem % 13;
        }
        return (rem == 0);
    }
};