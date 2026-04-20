
public class binary_to_decimal {
    public static void main(String[] args){
        int n = 1011;
        int output = 0;
        int power = 0;

        while(n != 0){
            int last = n%10;
            output += last*Math.pow(2,power);
            power++;
            n=n/10;
            
        }
        System.out.println("output is:"+output);

    }
    
}
