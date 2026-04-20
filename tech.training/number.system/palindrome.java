class Solution {
    public boolean isPalindrome(int x) {
        int output = 0;
        int pal = x;
        int last = 0;

        if(x<0){
            return false;
        }

        while(x != 0){
            last = x%10;
            output =(output*10)+last;
            x = x/10;

        }
        if(pal == output){
            return true;
        }
        else{
            return false;
        }

    }
}