public class reverse_num {
    public static void main(String[] args){
        class Solution {
    public int reverse(int x) {
        int output = 0;
        int last = 0;
        

        while(x != 0){
            last = x % 10;
            output = (output * 10) +last;
            x = x/10;
        
        }
        if (output > Integer.MAX_VALUE / 10 || output < Integer.MIN_VALUE / 10) {
                return 0; // return 0 if overflow
            }
        return output;
    }
}
    }
}
