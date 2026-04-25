// Online Java Compiler
// Use this editor to write, compile and run your Java code online in

class Main {
    public static void main(String[] args) {
        int n = 248;
        String output = " ";
        
        while(n != 0){
            output = (n%2) + output;
            n = n/2;
        }
        System.out.println("the output is:"+output);
    }
}
