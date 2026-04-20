public class fibnacc {
    public static int fib(int n) {
        if(n == 0) return 0;
        if(n == 1) return 1;

        int a = 0;
        int b = 1;
        int c = 0;
        
        for (int i = 2;i <= n;i++){
            c = a + b;
            a = b; 
            b = c;  
        }
        return c;
        
    }
    public static void main(String[] args){
        int n = 6;
        System.out.println("the finacci of num "+n+" is:"+ fib(n));
    }
}

