// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        int n = 23;
        boolean flag = true;
        
        for(int i = 2;i*i<n;i++){
            if(n%i == 0){
                flag = false;
                break;
            }
        }
        if(flag == true){
            System.out.println(n+" prime number");
        }
        else{
            System.out.println(n+" not prime number");
        }
    }
}
