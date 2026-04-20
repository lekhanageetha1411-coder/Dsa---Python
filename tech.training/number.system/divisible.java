// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        String n = "123456789";
        int div = 7;
        int rem = 0;
        for(int i=0;i<n.length();i++){
            rem =(rem * 10 + n.charAt(i)-'0')%div;
        }
        if(rem == 0){
            System.out.println("Divisible.");
        }
        else{
            System.out.println(" not Divisible.");
        }
    }
}