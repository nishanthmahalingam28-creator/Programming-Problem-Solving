import java.util.Scanner;
class ConstructorOverloading{
    long accountnumber;
    long balance;
    double interestrate;
    int age=32;
    //Constructor with no parameters
    ConstructorOverloading()
    {
        this.age=age;
    }
    //Constructor with all parameters
    ConstructorOverloading(long accountnumber, long balance, double interestrate){
        this.accountnumber=accountnumber;
        this.balance=balance;
        this.interestrate=interestrate;
    }
    //Constructor with accountnumber and balance
    ConstructorOverloading(long accountnumber, long balance){
        this.accountnumber=accountnumber;
        this.balance=balance;
    }
    

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the account number: ");
        long accountnumber=sc.nextLong();
        System.out.println("Enter the balance: ");
        long balance=sc.nextLong();
        System.out.println("Enter the interest rate: ");
        double interestrate=sc.nextDouble();
        ConstructorOverloading co=new ConstructorOverloading();
        ConstructorOverloading co1=new ConstructorOverloading(accountnumber, balance, interestrate);
        ConstructorOverloading co2=new ConstructorOverloading(accountnumber, balance);
        
        System.out.println("Age: "+co.age);
        System.out.println("Account number: "+co1.accountnumber);
        System.out.println("Balance: "+co1.balance);
        System.out.println("Interest rate: "+co1.interestrate);
        System.out.println("Account number: "+co2.accountnumber);
        System.out.println("Balance: "+co2.balance);
        sc.close();
    }
}
