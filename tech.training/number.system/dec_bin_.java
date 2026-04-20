// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        for(int i = 0;i<=10;i++){
            String output = " ";
            int n = i;
            
            while(n != 0){
                output = (n%2) + output;
                n = n/2;
            }
            System.out.println("the output of "+i+" is:"+output);
        }
        
    }
}